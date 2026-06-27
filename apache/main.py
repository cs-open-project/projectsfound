#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import apache
import content


def distinguish(existed_projects, all_projects):
    new_projects = {}
    graduate_projects = {}
    attic_projects = {}
    
    for key, proj in all_projects.items():
        pmc = proj["pmc"]
        if key not in existed_projects:
            new_projects[key] = proj
            continue

        previous_pmc = existed_projects[key]["pmc"]
        # 项目退役
        if previous_pmc != "attic" and pmc == "attic":
            attic_projects[key] = proj
        # 项目毕业
        if previous_pmc == "incubator" and pmc != previous_pmc:
            graduate_projects[key] = proj

    # 处理之前存在，但现在不存在的项目
    for key, proj in existed_projects.items():
        if key not in all_projects:
            all_projects[key] = proj

    return new_projects, graduate_projects, attic_projects


def generate_changelog(new_projects, graduate_projects, attic_projects):
    has_changes = (len(new_projects) > 0 or len(graduate_projects) > 0 or len(attic_projects) > 0)

    if not has_changes:
        return

    if new_projects:
        print(f"\n🆕 新增项目 ({len(new_projects)}):")
        for key, proj in sorted(new_projects.items()):
            name = proj.get("original_name") or key
            desc = proj.get("description") or ""
            desc_line = f" - {desc[:256]}..." if len(desc) > 256 else (f" - {desc}" if desc else "")
            print(f"   • {name}{desc_line}")

    if graduate_projects:
        print(f"\n🎓 毕业升级 ({len(graduate_projects)}):")
        for key, proj in sorted(graduate_projects.items()):
            name = proj.get("original_name") or key
            desc = proj.get("description") or ""
            desc_line = f" - {desc[:256]}..." if len(desc) > 256 else (f" - {desc}" if desc else "")
            print(f"   • {name}{desc_line}")

    if attic_projects:
        print(f"\n📁 已归档 ({len(attic_projects)}):")
        for key, proj in sorted(attic_projects.items()):
            name = proj.get("original_name") or key
            desc = proj.get("description") or ""
            desc_line = f" - {desc[:256]}..." if len(desc) > 256 else (f" - {desc}" if desc else "")
            print(f"   • {name}{desc_line}")

    changelog_path = "CHANGELOG_PROJECTS.md"
    header = """<!-- 此文件由程序自动生成，请勿手动修改 -->

# 项目历史

"""

    new_entry_lines = []
    new_entry_lines.append(time.strftime('%Y-%m-%d\n\n', time.localtime()))
    for key, proj in new_projects.items():
        name = proj.get("original_name") or key
        new_entry_lines.append("- Project New: {}\n\n".format(name))
    for key, proj in graduate_projects.items():
        name = proj.get("original_name") or key
        new_entry_lines.append("- Project Graduated: {}\n\n".format(name))
    for key, proj in attic_projects.items():
        name = proj.get("original_name") or key
        new_entry_lines.append("- Project Attic: {}\n\n".format(name))

    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
        # 跳过 header（4行：注释、空行、标题、空行）
        existing_content = "".join(lines[4:])
        with open(changelog_path, "w", encoding="utf-8") as fp:
            fp.write(header)
            fp.writelines(new_entry_lines)
            fp.write(existing_content)
    else:
        with open(changelog_path, "w", encoding="utf-8") as fp:
            fp.write(header)
            fp.writelines(new_entry_lines)


def generate_readme(existed_projects, all_projects):
    content.update_projects(existed_projects, all_projects)
    content.generate_md(all_projects)


existed_projects = content.read_md()
all_projects = apache.getApacheProjects()
new_projects, graduate_projects, attic_projects = distinguish(existed_projects, all_projects)

generate_changelog(new_projects, graduate_projects, attic_projects)
generate_readme(existed_projects, all_projects)
