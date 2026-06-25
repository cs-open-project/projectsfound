#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import scraper


def flatten_projects(categorized):
    """将按成熟度-分类-子分类嵌套的项目结构拍平为扁平字典

    Args:
        categorized: 嵌套结构的项目数据

    Returns:
        扁平字典，key 为大写项目名，value 包含 name 和 maturity
    """
    flat = {}
    for maturity, categories in categorized.items():
        for cat_name, subcats in categories.items():
            for subcat_name, projects in subcats.items():
                for proj in projects:
                    name = proj["name"]
                    upper_name = name.upper()
                    flat[upper_name] = {"name": name, "maturity": maturity}
    return flat


def distinguish_projects(existed_projects, all_projects):
    """对比已有项目和新数据，区分出新增、毕业、孵化晋级、归档的项目

    Args:
        existed_projects: 已有的项目字典，key 为大写项目名
        all_projects: 新获取的项目数据，按成熟度分层组织

    Returns:
        (new_projects, graduate_projects, incubating_projects, archived_projects) 四个字典
    """
    new_projects = {}
    graduate_projects = {}
    incubating_projects = {}
    archived_projects = {}

    # 将嵌套结构拍平，方便直接比较
    new_flat = flatten_projects(all_projects)

    for upper_name, info in new_flat.items():
        name = info["name"]
        maturity = info["maturity"]

        if upper_name not in existed_projects:
            # 新项目
            new_projects[name] = {"name": name, "maturity": maturity}
        else:
            prev_maturity = existed_projects[upper_name].get("maturity")
            # 从非 graduated 升级到 graduated
            if prev_maturity != "graduated" and maturity == "graduated":
                graduate_projects[name] = {"name": name, "prev_maturity": prev_maturity}
            # 从 sandbox 晋级到 incubating
            if prev_maturity == "sandbox" and maturity == "incubating":
                incubating_projects[name] = {"name": name, "prev_maturity": prev_maturity}
            # 从非 archived 变为 archived
            if prev_maturity != "archived" and maturity == "archived":
                archived_projects[name] = {"name": name, "prev_maturity": prev_maturity}

    return new_projects, graduate_projects, incubating_projects, archived_projects


def read_existed_projects():
    """从 README.md 解析已有项目信息，用于和新数据对比

    返回字典的 key 为大写项目名，value 包含 name 和 maturity
    """
    projects = {}
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")

    if not os.path.exists(readme_path):
        return projects

    import re
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    current_maturity = None
    for line in content.split("\n"):
        # 通过二级标题判断当前处于哪个成熟度章节
        if line.startswith("## Graduated "):
            current_maturity = "graduated"
        elif line.startswith("## Incubating "):
            current_maturity = "incubating"
        elif line.startswith("## Sandbox "):
            current_maturity = "sandbox"
        elif line.startswith("## Archived "):
            current_maturity = "archived"
        elif line.strip().startswith("- **") and current_maturity:
            # 先匹配带链接的格式：- **[名称](url)** — 描述
            match = re.search(r'- \*\*\[([^\]]+)\]\(', line)
            if not match:
                # 再匹配不带链接的格式：- **名称** — 描述
                match = re.search(r'- \*\*([^*]+?)\*\*', line)
            if match:
                name = match.group(1).strip()
                upper_name = name.upper()
                projects[upper_name] = {"name": name, "maturity": current_maturity}

    return projects


def generate_changelog(new_projects, graduate_projects, incubating_projects, archived_projects):
    """将项目变更记录写入 CHANGELOG_PROJECTS.md，新变更插入到文件开头

    格式：最新的日期在最前面，按时间倒序排列
    """
    if len(new_projects) == 0 and len(archived_projects) == 0 and len(graduate_projects) == 0 and len(incubating_projects) == 0:
        return

    changelog_path = "CHANGELOG_PROJECTS.md"
    # 文件头部固定格式：自动生成声明 + 标题
    header = """<!-- 此文件由程序自动生成，请勿手动修改 -->

# CNCF 项目历史

"""

    # 构造本次变更的条目
    new_entry_lines = []
    new_entry_lines.append(time.strftime('%Y-%m-%d\n\n', time.localtime()))

    for name in new_projects:
        maturity = new_projects[name]["maturity"]
        new_entry_lines.append("- Project New: {} [{}]\n\n".format(name, maturity))

    for name in graduate_projects:
        prev = graduate_projects[name].get("prev_maturity", "unknown")
        new_entry_lines.append("- Project Graduated: {} [from {}]\n\n".format(name, prev))

    for name in incubating_projects:
        prev = incubating_projects[name].get("prev_maturity", "unknown")
        new_entry_lines.append("- Project Incubating: {} [from {}]\n\n".format(name, prev))

    for name in archived_projects:
        prev = archived_projects[name].get("prev_maturity", "unknown")
        new_entry_lines.append("- Project Archived: {} [from {}]\n\n".format(name, prev))

    if os.path.exists(changelog_path):
        # 文件已存在：读取旧内容，去掉 header 后拼接到新内容后面
        with open(changelog_path, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
        # 跳过 header（5行：注释、空行、标题、空行、空行）
        existing_content = "".join(lines[5:])
        with open(changelog_path, "w", encoding="utf-8") as fp:
            fp.write(header)
            fp.writelines(new_entry_lines)
            fp.write(existing_content)
    else:
        # 文件不存在：创建新文件
        with open(changelog_path, "w", encoding="utf-8") as fp:
            fp.write(header)
            fp.writelines(new_entry_lines)


def main():
    # 1. 从 CNCF Landscape 获取最新项目数据
    data = scraper.fetch_landscape_data()
    categorized = scraper.process_projects(data)

    # 2. 从 README.md 读取已有项目，用于对比变化
    existed_projects = read_existed_projects()

    # 3. 对比新旧数据，区分新增、毕业、孵化晋级、归档的项目
    new_projects, graduate_projects, incubating_projects, archived_projects = distinguish_projects(existed_projects, categorized)

    # 4. 有变化时才生成 changelog 和打印信息
    has_changes = (len(new_projects) > 0 or len(graduate_projects) > 0
                   or len(incubating_projects) > 0 or len(archived_projects) > 0)

    if has_changes:
        generate_changelog(new_projects, graduate_projects, incubating_projects, archived_projects)

        if new_projects:
            print("new projects:", ",".join(new_projects.keys()))
        if graduate_projects:
            print("graduated projects:", ",".join(graduate_projects.keys()))
        if incubating_projects:
            print("incubating projects:", ",".join(incubating_projects.keys()))
        if archived_projects:
            print("archived projects:", ",".join(archived_projects.keys()))

    # 5. 生成最新的 README.md
    content = scraper.generate_markdown(categorized)
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()
