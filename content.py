APACHE_PROJECTS = "## Apache Projects"
Incubating_Mark = "Incubating"
Attic_Mark = "Attic"

header = """
# Open Source Project

{}

""".format(APACHE_PROJECTS)


# project is a dict with key
# {'incubator-annotator': {
# 'name': 'Apache Annotator',
# 'description': 'Apache Annotator is a collaborative community for creating annotation ...',
# 'pmc': 'incubator'
# }
def generate_md(projects, filename="README.md"):
    sorted_projects = sorted(projects.items(), key=lambda d: str.upper(d[1]["name"]))

    incubating_projects = []
    attic_projects = []
    graduated_projects = []

    for project in sorted_projects:
        pmc = project[1]["pmc"]
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
            write_project(file, project, "[]{}]".format(Attic_Mark))


def write_project(file_out, project, suffix=""):
    name = "### " + str.removeprefix(project["name"], "Apache ") + suffix
    splits = str.split(project["description"], "\n")
    r_splits = [str.lstrip(s) for s in splits]
    description = str.join(" ", r_splits)

    file_out.write(name + "\n\n")
    file_out.write("Description: " + description + "\n\n")

    zh_description = project.get("zh-description")
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
            status = "attic-"
        else:
            # handle format like "Yetus[软件库集合]"
            zh_name = flag
            status = ""
    if len(splits) > 2:
        zh_name = splits[2].removesuffix("]")

    project["name"] = splits[0].removeprefix("###").strip()
    if zh_name != "":
        project["zh_name"] = zh_name
    project["description"] = description.split(":", 2)[1]
    project["zh_description"] = zh_description.split(":", 2)[1]
    project["pmc"] = status

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

            projects[project["name"]] = project

    return projects