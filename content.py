APACHE_PROJECTS = "## Apache Projects"
Incubating_Mark = "Incubating"
Attic_Mark = "Attic"

header = """
# Open Source Project

{}

""".format(APACHE_PROJECTS)

PMC = "pmc"
NAME = "name"
ZH_NAME = "zh_name"
ZH_DESCRIPTION = "zh_description"
DESCRIPTION = "description"

# project is a dict with key，中间表示形式，Apache 和 README.md 都需要转换成该形式
# {'annotator': {
# 'name': 'Apache Annotator',
# 'zh_name': '注释',
# 'zh_description': '...',
# 'description': 'Apache Annotator is a collaborative community for creating annotation ...',
# 'pmc': 'incubator'
# }

def update_projects(old, new):
    for name in new:
        new_project = new[name]
        old_project = old.get(name)
        if old_project is not None:
            new_project[ZH_DESCRIPTION] = old_project[ZH_DESCRIPTION]
            if new_project.get(DESCRIPTION).strip() == "":
                new_project[DESCRIPTION] = old_project[DESCRIPTION]
            # zh_name may not exist
            if old_project.get(ZH_NAME) is not None:
                new_project[ZH_NAME] = old_project[ZH_NAME]


def generate_md(projects, filename="README.md"):
    sorted_projects = sorted(projects.items(), key=lambda d: str.upper(d[1][NAME]))

    incubating_projects = []
    attic_projects = []
    graduated_projects = []

    for project in sorted_projects:
        pmc = project[1][PMC]
        if pmc == "incubator":
            incubating_projects.append(project[1])
        elif pmc == "attic":
            attic_projects.append(project[1])
        else:
            graduated_projects.append(project[1])

    with open(filename, "w", encoding="utf-8") as file:
        file.write(header)
        for project in graduated_projects:
            write_project(file, project)
        for project in incubating_projects:
            write_project(file, project, "[{}]".format(Incubating_Mark))
        for project in attic_projects:
            write_project(file, project, "[{}]".format(Attic_Mark))


def write_project(file_out, project, suffix=""):
    name = "### " + project[NAME] + suffix
    if project.get(ZH_NAME) is not None:
        name = name + "[" + project.get(ZH_NAME) + "]"

    # 描述信息里可能会包含 '\n'，将其进行拼接
    splits = str.split(project[DESCRIPTION], "\n")
    r_splits = [str.lstrip(s) for s in splits]
    description = str.join(" ", r_splits)

    file_out.write(name + "\n\n")
    file_out.write("Description: " + description + "\n\n")

    zh_description = project.get(ZH_DESCRIPTION)
    if zh_description is None:
        file_out.write("介绍: " + description + "\n\n")
    else:
        file_out.write("介绍: " + zh_description + "\n\n")


def read_project(name, description, zh_description):
    project = {}
    # name: Celeborn[Incubating][外部统一Shuffle]
    # name: HugeGraph[Incubating]
    # name: Yetus[软件库集合]
    # name: Yetus
    splits = name.split("[")
    status = ""
    zh_name = ""
    if len(splits) > 1:
        flag = splits[1].removesuffix("]")
        if flag == Incubating_Mark:
            status = "incubator"
        elif flag == Attic_Mark:
            status = "attic"
        else:
            # handle format like "Yetus[软件库集合]"
            zh_name = flag
            status = ""
    if len(splits) > 2:
        zh_name = splits[2].removesuffix("]")

    project[NAME] = splits[0].removeprefix("###").strip()
    if zh_name != "":
        project[ZH_NAME] = zh_name
    project[DESCRIPTION] = description.split(":", 1)[1].strip()
    project[ZH_DESCRIPTION] = zh_description.split(":", 1)[1].strip()
    project[PMC] = status

    return project


def read_md():
    # name: Tajo(Attic)()
    # Description:
    # 介绍:
    projects = {}
    with open("README.md", "r", encoding="utf-8") as file:
        # skip header until Apache projects
        line = file.readline()
        while not line.startswith(APACHE_PROJECTS):
            line = file.readline()
        # skip empty line
        file.readline()

        while 1:
            name = file.readline()
            if not name:
                break
            name = name.strip()
            file.readline()
            description = file.readline().strip()
            file.readline()
            zh_description = file.readline().strip()
            file.readline()
            project = read_project(name, description, zh_description)

            projects[project[NAME]] = project

    return projects