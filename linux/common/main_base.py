# -*- coding: utf-8 -*-
"""
通用的基金会主程序逻辑，支持 landscape 格式的数据源

用法：
    from common.main_base import run_foundation
    run_foundation(
        landscape_url="...",
        foundation_name="CNCF",
        foundation_title="# CNCF Projects",
        base_dir=os.path.dirname(__file__),
    )
"""

import os
import sys
import time
import re
from typing import Dict

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from landscape import (
    fetch_landscape_data,
    process_projects,
    generate_markdown,
)


def flatten_projects(categorized):
    """将按成熟度-分类-子分类嵌套的项目结构拍平为扁平字典"""
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
    """对比已有项目和新数据，区分出新增、毕业、孵化晋级、归档的项目"""
    new_projects = {}
    graduate_projects = {}
    incubating_projects = {}
    archived_projects = {}

    new_flat = flatten_projects(all_projects)

    for upper_name, info in new_flat.items():
        name = info["name"]
        maturity = info["maturity"]

        if upper_name not in existed_projects:
            new_projects[name] = {"name": name, "maturity": maturity}
        else:
            prev_maturity = existed_projects[upper_name].get("maturity")
            if prev_maturity != "graduated" and maturity == "graduated":
                graduate_projects[name] = {"name": name, "prev_maturity": prev_maturity}
            if prev_maturity == "sandbox" and maturity == "incubating":
                incubating_projects[name] = {"name": name, "prev_maturity": prev_maturity}
            if prev_maturity != "archived" and maturity == "archived":
                archived_projects[name] = {"name": name, "prev_maturity": prev_maturity}

    return new_projects, graduate_projects, incubating_projects, archived_projects


def read_existed_projects(readme_path: str):
    """从 README.md 解析已有项目信息

    Args:
        readme_path: README.md 文件路径
    """
    projects = {}

    if not os.path.exists(readme_path):
        return projects

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    current_maturity = None
    for line in content.split("\n"):
        if line.startswith("## Graduated "):
            current_maturity = "graduated"
        elif line.startswith("## Incubating "):
            current_maturity = "incubating"
        elif line.startswith("## Sandbox "):
            current_maturity = "sandbox"
        elif line.startswith("## Archived "):
            current_maturity = "archived"
        elif line.strip().startswith("- **") and current_maturity:
            match = re.search(r'- \*\*\[([^\]]+)\]\(', line)
            if not match:
                match = re.search(r'- \*\*([^*]+?)\*\*', line)
            if match:
                name = match.group(1).strip()
                upper_name = name.upper()

                # 从 README 行提取描述
                desc = ""
                dash_match = re.search(r'—\s*(.+)', line)
                if dash_match:
                    desc = dash_match.group(1).strip()

                projects[upper_name] = {
                    "name": name,
                    "maturity": current_maturity,
                    "description": desc,
                }

    return projects


def generate_changelog(
    new_projects,
    graduate_projects,
    incubating_projects,
    archived_projects,
    changelog_path: str,
    changelog_title: str,
):
    """将项目变更记录写入 CHANGELOG_PROJECTS.md"""
    if (len(new_projects) == 0 and len(archived_projects) == 0
            and len(graduate_projects) == 0 and len(incubating_projects) == 0):
        return

    header = f"""<!-- 此文件由程序自动生成，请勿手动修改 -->

# {changelog_title}

"""

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
        with open(changelog_path, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
        existing_content = "".join(lines[5:])
        with open(changelog_path, "w", encoding="utf-8") as fp:
            fp.write(header)
            fp.writelines(new_entry_lines)
            fp.write(existing_content)
    else:
        with open(changelog_path, "w", encoding="utf-8") as fp:
            fp.write(header)
            fp.writelines(new_entry_lines)


def run_foundation(
    landscape_url: str,
    foundation_name: str,
    foundation_title: str,
    changelog_title: str,
    base_dir: str,
    landscape_site_url: str = "https://landscape.cncf.io/",
):
    """运行基金会主程序

    Args:
        landscape_url: landscape.yml 的 URL
        foundation_name: 基金会名称（如 "CNCF"）
        foundation_title: README 标题（如 "# CNCF Projects"）
        changelog_title: CHANGELOG 标题（如 "CNCF 项目历史"）
        base_dir: 基金会目录路径
        landscape_site_url: Landscape 官网链接（用于 README 展示）
    """
    readme_path = os.path.join(base_dir, "README.md")
    changelog_path = os.path.join(base_dir, "CHANGELOG_PROJECTS.md")

    data = fetch_landscape_data(landscape_url)
    categorized = process_projects(data)

    existed_projects = read_existed_projects(readme_path)

    # 用已有项目的较长描述更新 categorized 中的描述
    for maturity, categories in categorized.items():
        for cat_name, subcats in categories.items():
            for subcat_name, projects in subcats.items():
                for proj in projects:
                    upper_name = proj["name"].upper()
                    if upper_name in existed_projects:
                        existed_desc = existed_projects[upper_name].get("description", "") or ""
                        if len(existed_desc) > len(proj.get("description", "") or ""):
                            proj["description"] = existed_desc

    new_projects, graduate_projects, incubating_projects, archived_projects = \
        distinguish_projects(existed_projects, categorized)

    has_changes = (len(new_projects) > 0 or len(graduate_projects) > 0
                   or len(incubating_projects) > 0 or len(archived_projects) > 0)

    if has_changes:
        generate_changelog(
            new_projects,
            graduate_projects,
            incubating_projects,
            archived_projects,
            changelog_path,
            changelog_title,
        )

        # 构建项目名到描述的映射
        name_to_desc = {}
        for maturity, categories in categorized.items():
            for cat_name, subcats in categories.items():
                for subcat_name, projects in subcats.items():
                    for proj in projects:
                        name_to_desc[proj["name"]] = proj.get("description") or ""

        print(f"\n{'='*50}")
        print(f" {foundation_name} 项目变更")
        print(f"{'='*50}")

        if new_projects:
            print(f"\n🆕 新增项目 ({len(new_projects)}):")
            for name in sorted(new_projects.keys()):
                maturity = new_projects[name]["maturity"]
                desc = name_to_desc.get(name, "")
                desc_line = f" - {desc[:128]}..." if len(desc) > 128 else (f" - {desc}" if desc else "")
                print(f"   • {name} [{maturity}]{desc_line}")

        if graduate_projects:
            print(f"\n🎓 毕业升级 ({len(graduate_projects)}):")
            for name in sorted(graduate_projects.keys()):
                prev = graduate_projects[name].get("prev_maturity", "unknown")
                desc = name_to_desc.get(name, "")
                desc_line = f" - {desc[:128]}..." if len(desc) > 128 else (f" - {desc}" if desc else "")
                print(f"   • {name} [{prev} → graduated]{desc_line}")

        if incubating_projects:
            print(f"\n🔄 孵化晋级 ({len(incubating_projects)}):")
            for name in sorted(incubating_projects.keys()):
                prev = incubating_projects[name].get("prev_maturity", "unknown")
                desc = name_to_desc.get(name, "")
                desc_line = f" - {desc[:128]}..." if len(desc) > 128 else (f" - {desc}" if desc else "")
                print(f"   • {name} [{prev} → incubating]{desc_line}")

        if archived_projects:
            print(f"\n📁 已归档 ({len(archived_projects)}):")
            for name in sorted(archived_projects.keys()):
                prev = archived_projects[name].get("prev_maturity", "unknown")
                desc = name_to_desc.get(name, "")
                desc_line = f" - {desc[:128]}..." if len(desc) > 128 else (f" - {desc}" if desc else "")
                print(f"   • {name} [{prev} → archived]{desc_line}")

        print(f"{'='*50}\n")

    content = generate_markdown(categorized, foundation_name, foundation_title, landscape_site_url)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
