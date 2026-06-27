from datetime import datetime

APACHE_PROJECTS = "## Apache Projects"
Incubating_Mark = "Incubating"
Attic_Mark = "Attic"

PMC = "pmc"
NAME = "name"
ZH_NAME = "zh_name"
ZH_DESCRIPTION = "zh_description"
DESCRIPTION = "description"

LANDSCAPE_URL = "https://projects.apache.org/"

# project is a dict with key，中间表示形式，Apache 和 README.md 都需要转换成该形式
# {'annotator': {
# 'name': 'Apache Annotator',
# 'zh_name': '注释',
# 'zh_description': '...',
# 'description': 'Apache Annotator is a collaborative community for creating annotation ...',
# 'pmc': 'incubator'
# }

def update_projects(old, new):
    for key, new_project in new.items():
        old_project = old.get(key)
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

    today = datetime.now().strftime('%Y-%m-%d')

    header_lines = []
    header_lines.append("<!-- 此文件由程序自动生成，请勿手动修改 -->")
    header_lines.append("")
    header_lines.append("# Apache Projects")
    header_lines.append("")
    header_lines.append(f"> 数据来源: [Apache Projects]({LANDSCAPE_URL})")
    header_lines.append(">")
    header_lines.append(f"> 更新时间: {today}")
    header_lines.append("")
    header_lines.append("项目统计")
    header_lines.append("")
    header_lines.append("| 状态 | 数量 |")
    header_lines.append("|------|------|")
    header_lines.append(f"| [Graduated](#graduated) | {len(graduated_projects)} |")
    header_lines.append(f"| [Incubating](#incubating) | {len(incubating_projects)} |")
    header_lines.append(f"| [Attic](#attic) | {len(attic_projects)} |")
    header_lines.append(f"| **总计** | **{len(sorted_projects)}** |")
    header_lines.append("")

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(header_lines))
        file.write("---\n\n")
        file.write("## Graduated\n\n")
        for project in graduated_projects:
            write_project(file, project)
        file.write("## Incubating\n\n")
        for project in incubating_projects:
            write_project(file, project, "[{}]".format(Incubating_Mark))
        file.write("## Attic\n\n")
        for project in attic_projects:
            write_project(file, project, "[{}]".format(Attic_Mark))


def write_project(file_out, project, suffix=""):
    # 使用 original_name 显示，如果没有则使用 name
    display_name = project.get("original_name") or project[NAME]
    name = "### " + display_name + suffix
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
        # skip header until '## Graduated'
        line = file.readline()
        while not line.startswith("## "):
            line = file.readline()
        # skip empty line
        file.readline()

        while 1:
            name = file.readline()
            if not name:
                break
            # skip '## Incubating' and '## Attic'
            if name.startswith("## "):
                file.readline()
                continue
            name = name.strip()
            file.readline()
            description = file.readline().strip()
            file.readline()
            zh_description = file.readline().strip()
            file.readline()
            project = read_project(name, description, zh_description)

            # 使用大写作为 key
            upper_name = project[NAME].upper()
            projects[upper_name] = project

    return projects
