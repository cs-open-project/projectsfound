#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# 单个项目执行、提交并发送钉钉通知

BASE_DIR=$(cd "$(dirname "$0")/../" && pwd)

usage() {
    echo "Usage: $0 <project_name> <run_command>"
    echo ""
    echo "  project_name  - 项目名称（apache/cncf/lfai）"
    echo "  run_command   - 执行命令（如 'cd linux/cncf && python main.py'）"
    exit 1
}

if [ $# -lt 2 ]; then
    usage
fi

PROJECT_NAME="$1"
shift
RUN_COMMAND="$@"

cd "$BASE_DIR"

# 钉钉通知配置
DINGTALK_WEBHOOK="${DINGTALK_WEBHOOK:-}"

# 发送钉钉通知（markdown 格式）
send_dingtalk() {
    local title="$1"
    local text="$2"
    if [ -z "$DINGTALK_WEBHOOK" ]; then
        echo "DINGTALK_WEBHOOK not set, skip notification"
        return 1
    fi

    PAYLOAD=$(cat <<ENDJSON
{
    "msgtype": "markdown",
    "markdown": {
        "title": "${title}",
        "text": "${text}"
    }
}
ENDJSON
)

    curl -s -X POST "$DINGTALK_WEBHOOK" \
        -H 'Content-Type: application/json' \
        -d "$PAYLOAD" \
        > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "DingTalk notification sent."
    else
        echo "Failed to send DingTalk notification."
    fi
}

# 检查是否有 git 变更
has_changes() {
    git status --porcelain | grep -q .
}

# 执行命令，捕获输出
echo "=============================="
echo " Running: ${PROJECT_NAME}"
echo "=============================="

OUTPUT_FILE=$(mktemp)
bash -c "$RUN_COMMAND" > "$OUTPUT_FILE" 2>&1
EXIT_CODE=$?

# 打印输出
cat "$OUTPUT_FILE"

if [ $EXIT_CODE -ne 0 ]; then
    # 情形 1: 执行失败
    echo "${PROJECT_NAME} failed with exit code ${EXIT_CODE}."

    LAST_LINES=$(tail -20 "$OUTPUT_FILE" | sed 's/"/\\"/g' | sed 's/\n/\\n/g')
    NOTIFY_TITLE="[ProjectsFound] ${PROJECT_NAME} 执行失败"
    NOTIFY_TEXT="### ❌ ${PROJECT_NAME} 执行失败

**Exit code**: \`${EXIT_CODE}\`

**Last output**:
\`\`\`
${LAST_LINES}
\`\`\`

---
*ProjectsFound*"
    send_dingtalk "$NOTIFY_TITLE" "$NOTIFY_TEXT"

    rm -f "$OUTPUT_FILE"
    exit $EXIT_CODE
fi

# 检查输出中是否有项目变更（包含"项目变更"分隔线表示有变更打印）
if grep -q "项目变更" "$OUTPUT_FILE"; then
    # 情形 3: 执行成功且有项目变更
    CHANGE_TYPE="Project Update"
    NOTIFY_TITLE="[ProjectsFound] ${PROJECT_NAME} 项目更新"

    # 提取项目变更部分，转换为 markdown
    CHANGE_MD=$(sed -n '/项目变更/,/====/p' "$OUTPUT_FILE" \
        | sed 's/"/\\"/g' \
        | sed '/^[=]*$/d' \
        | sed 's/🆕 新增项目/#### 🆕 新增项目/g' \
        | sed 's/🎓 毕业升级/#### 🎓 毕业升级/g' \
        | sed 's/🔄 孵化晋级/#### 🔄 孵化晋级/g' \
        | sed 's/📁 已归档/#### 📁 已归档/g' \
        | sed 's/^   • /- /g')
else
    # 情形 2: 执行成功但无项目变更（可能有描述更新或无更新）
    # 检查是否有 git 变更
    if has_changes; then
        CHANGE_TYPE="Description Update"
        NOTIFY_TITLE="[ProjectsFound] ${PROJECT_NAME} 描述更新"
        CHANGE_MD="描述内容有更新"
    else
        # 没有任何变更，跳过提交和通知
        echo "${PROJECT_NAME}: no changes."
        rm -f "$OUTPUT_FILE"
        exit 0
    fi
fi

rm -f "$OUTPUT_FILE"

# Git 提交
echo ""
echo "Committing ${PROJECT_NAME} changes..."
git add -A

STATS=$(git diff --cached --stat)
SHORT_STATS=$(echo "$STATS" | tail -1)

COMMIT_MSG="[${PROJECT_NAME}] ${CHANGE_TYPE}: $(date '+%Y-%m-%d %H:%M:%S')

${SHORT_STATS}"
git commit -m "$COMMIT_MSG"

echo "Committed: ${COMMIT_MSG}"

# 推送
echo "Pushing to remote..."
git push

# 发送通知
NOTIFY_TEXT="### 📝 ${NOTIFY_TITLE}

**更新时间**: $(date '+%Y-%m-%d %H:%M:%S')

**变更统计**: \`${SHORT_STATS}\`

---

${CHANGE_MD}

---
*ProjectsFound*"
send_dingtalk "$NOTIFY_TITLE" "$NOTIFY_TEXT"

echo "${PROJECT_NAME} done."
echo ""
