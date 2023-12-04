# 获取所有的 committees，有的 apache 项目共用一个 committee （如 apache commons 存在多个链接），incubating 项目都属于一个 Incubator committee
import logging

import apache
import content

committees = apache.getCommittees("https://projects.apache.org/json/foundation/committees.json")
logging.info("get committees")

# 获取所有的 incubator 项目
incubatings = apache.getIncubatingProjects("https://projects.apache.org/json/foundation/podlings.json")
logging.info("get incubating projects")

# 这里可能会有 incubating 的项目，其 pmc 为 incubator
projects = apache.getProjects("https://projects.apache.org/json/foundation/projects.json")
logging.info("get graduated projects")

all = {}
all.update(incubatings)
all.update(projects)
# no DOAP file written by the PMC: creating default content
non_exist = apache.handlerNoDOAPProjects(committees, all)
logging.info("handle no doap projects")

# 从 incubating 项目历史中，获取 描述信息
apache.updateNonExistDescription("https://projects.apache.org/json/foundation/podlings-history.json", non_exist)
logging.info("update no doap projects")
all.update(non_exist)

existed_projects = content.read_md()

fp = open("CHANGELOG_PROJECTS.md", "a", encoding="utf-8")

hasNew = False
for key in all:
    project_name = str.removeprefix(all[key]["name"], "Apache").strip()
    pmc = all[key]["pmc"]
    if existed_projects.get(project_name) is None:
        print("project_name {} is new", project_name)
        hasNew = True
        fp.write("- New Project: {}, Description: {}, PMC: {}\n\n".format(project_name, all[key]["description"], all[key]["pmc"]))
        continue

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
    content.generate_md(all)

