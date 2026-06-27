#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# 更新所有项目

BASE_DIR=$(cd "$(dirname "$0")/../" && pwd)

echo "========================================"
echo " Starting All Projects Update"
echo "========================================"
echo ""

# Apache
bash "${BASE_DIR}/bin/run_single.sh" "Apache" "cd apache && python main.py"
APACHE_EXIT=$?

# CNCF
bash "${BASE_DIR}/bin/run_single.sh" "CNCF" "cd linux/cncf && python main.py"
CNCF_EXIT=$?

# LF AI & Data
bash "${BASE_DIR}/bin/run_single.sh" "LF AI & Data" "cd linux/lfai && python main.py"
LFAI_EXIT=$?

# 汇总
echo "========================================"
echo " Summary"
echo "========================================"

if [ $APACHE_EXIT -eq 0 ]; then
    echo "  Apache:        ✅ OK"
else
    echo "  Apache:        ❌ FAILED"
fi

if [ $CNCF_EXIT -eq 0 ]; then
    echo "  CNCF:          ✅ OK"
else
    echo "  CNCF:          ❌ FAILED"
fi

if [ $LFAI_EXIT -eq 0 ]; then
    echo "  LF AI & Data:  ✅ OK"
else
    echo "  LF AI & Data:  ❌ FAILED"
fi

echo "========================================"
echo "All done."
