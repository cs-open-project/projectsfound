#!/usr/bin/env bash

BASE_DIR=$(cd "$(dirname "$0")/../" && pwd)

usage() {
    echo "Usage: $0 [apache|cncf|lfai|all]"
    echo ""
    echo "  apache  - Update Apache projects"
    echo "  cncf    - Update CNCF projects (Linux Foundation)"
    echo "  lfai    - Update LF AI & Data projects (Linux Foundation)"
    echo "  all     - Update all projects (default)"
    exit 1
}

run_apache() {
    echo "=============================="
    echo " Updating Apache Projects"
    echo "=============================="
    cd "${BASE_DIR}/apache" && python main.py
    echo "Apache projects updated."
    echo ""
}

run_cncf() {
    echo "=============================="
    echo " Updating CNCF Projects"
    echo "=============================="
    cd "${BASE_DIR}/linux/cncf" && python main.py
    echo "CNCF projects updated."
    echo ""
}

run_lfai() {
    echo "=============================="
    echo " Updating LF AI & Data Projects"
    echo "=============================="
    cd "${BASE_DIR}/linux/lfai" && python main.py
    echo "LF AI & Data projects updated."
    echo ""
}

TARGET="${1:-all}"

case "$TARGET" in
    apache)
        run_apache
        ;;
    cncf)
        run_cncf
        ;;
    lfai)
        run_lfai
        ;;
    all)
        run_apache
        run_cncf
        run_lfai
        ;;
    *)
        usage
        ;;
esac

echo "Done."
