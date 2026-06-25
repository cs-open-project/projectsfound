#!/usr/bin/env bash

BASE_DIR=$(cd "$(dirname "$0")/../" && pwd)

usage() {
    echo "Usage: $0 [apache|cncf|all]"
    echo ""
    echo "  apache  - Update Apache projects"
    echo "  cncf    - Update CNCF projects"
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
    cd "${BASE_DIR}/cncf" && python main.py
    echo "CNCF projects updated."
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
    all)
        run_apache
        run_cncf
        ;;
    *)
        usage
        ;;
esac

echo "Done."