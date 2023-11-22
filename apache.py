import json
from urllib import request


def splitStr(content):
    datas = str.split(content, ",")
    trim = [k.lstrip() for k in datas]
    return trim


def getIncubatingProjects(url):
    response = request.urlopen(url)
    data = response.read()

    incubatings = json.loads(data)
    incub_projects = {}

    for id in incubatings:
        project = incubatings[id]
        name = str.removesuffix(project["name"], " (Incubating)")

        # Since podlings（incubating） are loaded first, DOAPs take precedence
        incub_projects["incubator-" + id] = {
            "name": name,
            "description": project["description"],
            "pmc": project["pmc"]
        }
    return incub_projects


def getProjects(url):
    response = request.urlopen(url)
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
    response = request.urlopen(url)
    data = response.read()

    jsonData = json.loads(data)
    for id in non_exist:
        project = non_exist.get(id)
        source = jsonData.get(id)
        if source is not None:
            project["description"] = source["description"]
        else:
            project["description"] = ""


def getCommittees(url):
    response = request.urlopen(url)
    data = response.read()

    committees = {}
    # list
    jsonData = json.loads(data)
    for committee in jsonData:
        committees[committee["id"]] = committee["name"]

    return committees
