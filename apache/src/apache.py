import json
import logging
from urllib import request
import ssl

# 创建一个SSL上下文对象
context = ssl.create_default_context()
# 忽略SSL证书验证
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

def splitStr(content):
    datas = str.split(content, ",")
    trim = [k.lstrip() for k in datas]
    return trim


def getIncubatingProjects(url):
    response = request.urlopen(url, context=context)
    data = response.read()

    incubatings = json.loads(data)
    incub_projects = {}

    for id in incubatings:
        project = incubatings[id]
        name = str.removesuffix(project["name"], " (Incubating)")

        # Since podlings（incubating） are loaded first, DOAPs take precedence
        # 因为 projects 里也会有 incubator 的项目，所以必须统一格式
        incub_projects["incubator-" + id] = {
            "name": name,
            "description": project["description"],
            "pmc": project["pmc"]
        }
    return incub_projects


def getProjects(url):
    response = request.urlopen(url, context=context)
    data = response.read()
    jsonData = json.loads(data)

    allProjects = {}

    for id in jsonData:
        project = jsonData[id]
        name = project["name"]
        description = project.get("description")
        if description is None:
            description = project.get("shortdesc")
        if description is None:
            description = ""
        allProjects[id] = {
            "name": name,
            "description": description,
            "pmc": project["pmc"]
        }

    return allProjects


def handlerNoDOAPProjects(committees, existProjects):
    projectPmcs = {}
    for id in existProjects:
        project = existProjects[id]
        projectPmcs[project["pmc"]] = project

    projects = {}
    for committee_id in committees:
        committee_name = committees[committee_id]
        if projectPmcs.get(committee_id) is None and committee_id != "attic":
            projects[committee_id] = {
                "name": committee_name,
                "pmc": committee_id
            }

    return projects


def updateNonExistDescription(url, non_exist):
    response = request.urlopen(url, context=context)
    data = response.read()

    jsonData = json.loads(data)
    for id in non_exist:
        project = non_exist.get(id)
        source = jsonData.get(id)
        if source is not None:
            project["description"] = source["description"]
        else:
            project["description"] = ""


# 获取所有的 committees，有的 apache 项目共用一个 committee （如 apache commons 存在多个链接），incubating 项目都属于一个 Incubator committee
def getCommittees(url):
    response = request.urlopen(url, context=context)
    data = response.read()

    committees = {}
    # list
    jsonData = json.loads(data)
    for committee in jsonData:
        committees[committee["id"]] = committee["name"]

    return committees


def getApacheProjects():
    committees = getCommittees("https://projects.apache.org/json/foundation/committees.json")
    logging.info("get committees")

    # 获取所有的 incubator 项目
    incubatings = getIncubatingProjects("https://projects.apache.org/json/foundation/podlings.json")
    logging.info("get incubating projects")

    # 这里可能会有 incubating 的项目，其 pmc 为 incubator，项目名为 incubator-xxx
    projects = getProjects("https://projects.apache.org/json/foundation/projects.json")
    logging.info("get graduated projects")

    all_projects = {}
    all_projects.update(incubatings)
    all_projects.update(projects)
    # no DOAP file written by the PMC: creating default content
    non_exist = handlerNoDOAPProjects(committees, all_projects)
    logging.info("handle no doap projects")

    # 从 incubating 项目历史中，获取 描述信息
    updateNonExistDescription("https://projects.apache.org/json/foundation/podlings-history.json", non_exist)
    logging.info("update no doap projects")
    all_projects.update(non_exist)

    # 按全大写名称去重，保留 description 更长的
    upper_to_name = {}  # 全大写名称 -> 原始名称
    upper_to_project = {}  # 全大写名称 -> 项目信息

    for name in all_projects:
        project = all_projects[name]
        format_name = str.removeprefix(project["name"], "Apache").strip()
        upper_name = format_name.upper()

        # 如果已存在同名项目，选择 description 更长的
        if upper_name in upper_to_project:
            existing_desc = upper_to_project[upper_name]["description"] or ""
            new_desc = project["description"] or ""
            if len(new_desc) > len(existing_desc):
                upper_to_project[upper_name] = project
                upper_to_name[upper_name] = format_name
        else:
            upper_to_project[upper_name] = project
            upper_to_name[upper_name] = format_name

    # 转换为最终格式，key 和 name 都使用大写
    format_projects = {}
    for upper_name in upper_to_project:
        project = upper_to_project[upper_name]
        project["name"] = upper_name
        project["original_name"] = upper_to_name[upper_name]
        format_projects[upper_name] = project

    return format_projects
