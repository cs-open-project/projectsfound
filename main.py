import time

import apache
import content


def distinguish(existed_projects, all_projects):
    new_projects = {}
    graduate_projects = {}
    attic_projects = {}
    for key in all_projects:
        project_name = all_projects[key]["name"]
        pmc = all_projects[key]["pmc"]
        if existed_projects.get(project_name) is None:
            new_projects[key] = all_projects[key]
            continue

        previous_pmc = existed_projects.get(project_name)["pmc"]
        # 项目退役
        if previous_pmc != "attic" and pmc == "attic":
            attic_projects[key] = all_projects[key]
        # 项目毕业
        if previous_pmc == "incubator" and pmc != previous_pmc:
            graduate_projects[key] = all_projects[key]

    # 处理之前存在，但现在不存在的项目
    for key in existed_projects:
        project_name = existed_projects[key]["name"]
        if all_projects.get(project_name) is None:
            all_projects[key] = existed_projects[key]

    return new_projects, graduate_projects, attic_projects


def generate_changelog(new_projects, graduate_projects, attic_projects):
    if len(new_projects) == 0 and len(attic_projects) == 0 and len(graduate_projects) == 0:
        return
    with open("CHANGELOG_PROJECTS.md", "a", encoding="utf-8") as fp:
        fp.write(time.strftime('%Y-%m-%d\n\n', time.localtime()))
        for name in new_projects:
            fp.write("- Project New: {}\n\n".format(name))
        for name in graduate_projects:
            fp.write("- Project Graduated: {}\n\n".format(name))
        for name in attic_projects:
            fp.write("- Project Attic: {}\n\n".format(name))


def generate_readme(existed_projects, all_projects):
    if len(new_projects) == 0 and len(attic_projects) == 0 and len(graduate_projects) == 0:
        return

    if len(new_projects) != 0:
        print("new projects:" + str.join(",", new_projects.keys()))
    if len(graduate_projects) != 0:
        print("graduated projects:" + str.join(",", graduate_projects.keys()))
    if len(attic_projects) != 0:
        print("attic projects:" + str.join(",", attic_projects.keys()))
    content.update_projects(existed_projects, all_projects)
    content.generate_md(all_projects)


all_projects = apache.getApacheProjects()
existed_projects = content.read_md()
new_projects, graduate_projects, attic_projects = distinguish(existed_projects, all_projects)

generate_changelog(new_projects, graduate_projects, attic_projects)
generate_readme(existed_projects, all_projects)
