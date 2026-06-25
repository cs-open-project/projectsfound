# -*- coding: utf-8 -*-

import json
import yaml
import requests
from datetime import datetime
from typing import Dict, List, Any

LANDSCAPE_URL = "https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml"

MATURITY_MAP = {
    "graduated": "Graduated",
    "incubating": "Incubating",
    "sandbox": "Sandbox",
    "archived": "Archived",
}


def fetch_landscape_data() -> Dict[str, Any]:
    """从 GitHub 获取 CNCF Landscape 数据"""
    response = requests.get(LANDSCAPE_URL, timeout=60)
    response.raise_for_status()
    data = yaml.safe_load(response.text)
    return data


def process_projects(landscape_data: Dict) -> Dict[str, Dict[str, List[Dict]]]:
    """解析并分类所有项目"""
    categorized = {
        "graduated": {},
        "incubating": {},
        "sandbox": {},
        "archived": {},
    }

    landscape = landscape_data.get("landscape", [])

    for category_data in landscape:
        if not category_data:
            continue
        category_name = category_data.get("name", "Unknown")
        subcategories = category_data.get("subcategories") or []

        for subcategory_data in subcategories:
            if not subcategory_data:
                continue
            subcategory_name = subcategory_data.get("name", "Unknown")
            items = subcategory_data.get("items") or []

            for item in items:
                if not item:
                    continue

                maturity = _get_maturity(item)
                if not maturity:
                    continue

                project_info = _extract_project_info(item, category_name, subcategory_name)

                if category_name not in categorized[maturity]:
                    categorized[maturity][category_name] = {}
                if subcategory_name not in categorized[maturity][category_name]:
                    categorized[maturity][category_name][subcategory_name] = []
                categorized[maturity][category_name][subcategory_name].append(project_info)

    return categorized


def count_projects(categorized: Dict) -> Dict[str, int]:
    """统计每个成熟度的项目数量"""
    counts = {}
    for maturity in ["graduated", "incubating", "sandbox", "archived"]:
        count = 0
        cats = categorized.get(maturity, {})
        for cat_name, subcats in cats.items():
            for subcat_name, projects in subcats.items():
                if isinstance(projects, list):
                    count += len(projects)
                elif isinstance(projects, dict):
                    for key, projs in projects.items():
                        if isinstance(projs, list):
                            count += len(projs)
        counts[maturity] = count
    return counts


def _get_maturity(item: Dict) -> str:
    """从 project 字段获取项目成熟度

    project 字段的取值：
    - sandbox: 沙箱项目
    - incubating: 孵化中项目
    - graduated: 毕业项目
    - archived: 已归档项目

    如果没有 project 字段，返回 None（表示不是 CNCF 项目）
    """
    project = item.get("project")
    if project in ["sandbox", "incubating", "graduated", "archived"]:
        return project
    return None


def _extract_project_info(item: Dict, category: str, subcategory: str) -> Dict:
    """提取项目的基本信息：名称、描述、链接、分类等"""
    name = item.get("name", "Unknown")
    homepage_url = item.get("homepage_url", "")
    repo_url = item.get("repo_url", "")
    extra = item.get("extra") or {}

    # 优先使用 item.description，其次用 summary_use_case，最后用 summary_business_use_case
    description = item.get("description", "") or ""
    if not description:
        description = extra.get("summary_use_case", "") or ""
    if not description:
        description = extra.get("summary_business_use_case", "") or ""

    return {
        "name": name,
        "description": description,
        "homepage_url": homepage_url,
        "repo_url": repo_url,
        "category": category,
        "subcategory": subcategory,
        "graduated_date": extra.get("graduated", ""),
        "incubating_date": extra.get("incubating", ""),
        "archived_date": extra.get("archived", ""),
    }


def generate_markdown(categorized: Dict) -> str:
    """生成 Markdown 格式的项目列表，按成熟度 → 分类 → 子分类层级展示"""
    lines = []

    counts = count_projects(categorized)
    total = sum(counts.values())

    # 文件头部：自动生成声明、标题、数据来源、更新时间
    lines.append("<!-- 此文件由程序自动生成，请勿手动修改 -->")
    lines.append("")
    lines.append("# CNCF Projects")
    lines.append("")
    lines.append(f"> 数据来源: [CNCF Landscape](https://landscape.cncf.io/)")
    lines.append(f"> 更新时间: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    # 统计概览表格，带锚点跳转到对应章节
    lines.append("## 项目统计")
    lines.append("")
    lines.append("| 状态 | 数量 |")
    lines.append("|------|------|")
    for maturity in ["graduated", "incubating", "sandbox", "archived"]:
        count = counts.get(maturity, 0)
        lines.append(f"| [{MATURITY_MAP[maturity]}](#{MATURITY_MAP[maturity].lower()}) | {count} |")
    lines.append(f"| **总计** | **{total}** |")
    lines.append("")

    # 按成熟度分组展示项目
    section_num = 1
    for maturity in ["graduated", "incubating", "sandbox", "archived"]:
        categories = categorized.get(maturity, {})
        if not categories:
            continue

        maturity_count = counts.get(maturity, 0)
        lines.append("---")
        lines.append("")
        lines.append(f"## {MATURITY_MAP[maturity]} ({maturity_count})")
        lines.append("")

        # 按分类展示
        for cat_name in sorted(categories.keys()):
            subcats = categories[cat_name]
            cat_count = 0
            for subcat_name, projects in subcats.items():
                if isinstance(projects, list):
                    cat_count += len(projects)

            lines.append(f"### {cat_name} ({cat_count})")
            lines.append("")

            # 按子分类展示项目列表
            for subcat_name in sorted(subcats.keys()):
                projects = subcats[subcat_name]
                if not projects:
                    continue
                lines.append(f"#### {subcat_name}")
                lines.append("")

                # 项目按名称字母排序
                for proj in sorted(projects, key=lambda x: x["name"].lower()):
                    proj_name = proj["name"]
                    # 有主页链接则加超链接
                    if proj.get("homepage_url"):
                        name_display = f"[{proj_name}]({proj['homepage_url']})"
                    else:
                        name_display = proj_name

                    desc = proj.get("description", "") or ""
                    if desc:
                        desc = desc.replace("\n", " ").strip()
                        lines.append(f"- **{name_display}** — {desc}")
                    else:
                        lines.append(f"- **{name_display}**")

                lines.append("")

        section_num += 1

    lines.append("---")
    lines.append("")
    lines.append("Data source: [CNCF Landscape](https://landscape.cncf.io/)")
    lines.append(f"Updated: {datetime.now().strftime('%Y-%m-%d')}")

    return "\n".join(lines)
