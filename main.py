
# 获取所有的 committees，有的 apache 项目共用一个 committee （如 apache commons 存在多个链接），incubating 项目都属于一个 Incubator committee
from apache import getCommittees, getIncubatingProjects, handlerNoDOAPProjects, getProjects, updateNonExistDescription

committees = getCommittees("https://projects.apache.org/json/foundation/committees.json")

# 获取所有的 incubator 项目
incubatings = getIncubatingProjects("https://projects.apache.org/json/foundation/podlings.json")
# 这里可能会有 incubating 的项目，其 pmc 为 incubator
projects = getProjects("https://projects.apache.org/json/foundation/projects.json")

all = {}
all.update(incubatings)
all.update(projects)
# no DOAP file written by the PMC: creating default content
non_exist = handlerNoDOAPProjects(committees, all)

# 从 incubating 项目历史中，获取 描述信息
updateNonExistDescription("https://projects.apache.org/json/foundation/podlings-history.json", non_exist)
all.update(non_exist)