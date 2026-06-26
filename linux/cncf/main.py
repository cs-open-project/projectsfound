#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# 从 linux/cncf/main.py 往上级到项目根目录
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(root_dir, 'linux'))

from common.main_base import run_foundation


LANDSCAPE_URL = "https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml"
LANDSCAPE_SITE_URL = "https://landscape.cncf.io/"
FOUNDATION_NAME = "CNCF"
FOUNDATION_TITLE = "# CNCF Projects"
CHANGELOG_TITLE = "CNCF 项目历史"


def main():
    run_foundation(
        landscape_url=LANDSCAPE_URL,
        foundation_name=FOUNDATION_NAME,
        foundation_title=FOUNDATION_TITLE,
        changelog_title=CHANGELOG_TITLE,
        base_dir=os.path.dirname(__file__),
        landscape_site_url=LANDSCAPE_SITE_URL,
    )


if __name__ == "__main__":
    main()
