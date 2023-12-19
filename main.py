
import apache
import content

all_projects = apache.getApacheProjects()

existed_projects = content.read_md()

fp = open("CHANGELOG_PROJECTS.md", "a", encoding="utf-8")

hasNew = False
for key in all_projects:
    project_name = str.removeprefix(all_projects[key]["name"], "Apache").strip()
    pmc = all_projects[key]["pmc"]
    if existed_projects.get(project_name) is None:
        print("project_name {} is new".format(project_name))
        hasNew = True
        fp.write("- New Project: {}, Description: {}, PMC: {}\n\n".format(project_name, all_projects[key]["description"], all_projects[key]["pmc"]))
        continue

    # TODO 处理 incubator 项目直接 attic 的事情
    previous_pmc = existed_projects.get(project_name)["pmc"]
    # 项目毕业
    if previous_pmc == "incubator" and pmc != previous_pmc:
        hasNew = True
        fp.write("- Project Graduated: {}\n\n".format(project_name))
    # 项目退役
    if previous_pmc != "attic" and pmc == "attic":
        hasNew = True
        fp.write("- Project Attic: {}\n\n".format(project_name))

fp.close()

if hasNew:
    print("projects has new information, re-generate README.md")
    content.update_projects(existed_projects, all_projects)
    content.generate_md(all_projects)

