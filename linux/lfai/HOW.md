# LF AI & Data 项目获取说明

## 数据来源

项目数据从 [LF AI & Data Landscape](https://github.com/lfai/lfai-landscape) 获取：

- Landscape 数据：https://raw.githubusercontent.com/lfai/lfai-landscape/master/landscape.yml

## 项目状态区分

LF AI & Data 项目通过 maturity 字段区分状态：

| 状态 | maturity 值 | 说明 |
|------|-------------|------|
| Graduated | `graduated` | 正式毕业项目 |
| Incubating | `incubating` | 孵化中的项目 |
| Sandbox | `sandbox` | 沙箱项目 |
| Archived | `archived` | 已归档的项目 |

## 项目变迁记录

LF AI & Data 项目变更包括：

- **New**: 新增到某个状态的项目
- **Incubating**: 从 Sandbox 晋级到 Incubating
- **Graduated**: 从 Incubating 升级到 Graduated
- **Archived**: 变为 Archived 状态

## 项目描述获取

LF AI & Data 的 landscape.yml 数据中的项目大多没有 `description` 字段，因此需要通过额外方式获取项目描述。

### 描述优先级

生成 README 时，项目描述按以下优先级获取（取最长的有效描述）：

1. **landscape 数据中的 description** - landscape.yml 中自带的描述（大多数项目为空）
2. **extra.summary_use_case** - landscape 数据中的备用描述字段
3. **extra.summary_business_use_case** - landscape 数据中的备用描述字段
4. **本地描述缓存** - `lfai_github_descriptions.json` 中维护的项目描述（主要来源）

### 描述缓存文件

`lfai_github_descriptions.json` 是一个 JSON 文件，key 为大写的项目名称，value 为项目描述。

示例格式：
```json
{
  "ONNX": "Open Neural Network Exchange - open format for representing machine learning models",
  "MILVUS": "High-performance vector database built for scale..."
}
```

### 补全描述的方法

如果需要为新项目补全描述，可以通过以下方式获取：

| 方法 | 说明 |
|------|------|
| GitHub API | 通过 `https://api.github.com/repos/{owner}/{repo}` 获取仓库 description 字段 |
| GitHub README | 从仓库的 README.md 中提取第一段有意义的描述文本 |
| 项目官网 | 访问项目 homepage 提取简介 |
| 网页搜索 | 通过搜索引擎搜索项目名称获取官方描述 |

### 更新描述的步骤

1. 编辑 `lfai_github_descriptions.json`，添加或修改对应项目的描述
2. 运行 `python main.py`，程序会自动加载缓存并使用缓存中的描述

### 相关脚本

- `fetch_github_desc.py` - 通过 GitHub API 批量获取项目描述（匿名 API 有每小时 60 次限制）
- `fetch_readme_desc.py` - 通过 GitHub README 原始文件批量提取项目描述（无频率限制）
- `clean_descriptions.py` - 清理描述文本中的 badge、链接标记、HTML 标签等

## 运行方式

```bash
cd linux/lfai
python main.py
```

## 生成文件

- `README.md` - 所有 LF AI & Data 项目列表，按 Graduated / Incubating / Sandbox / Archived 分组
- `CHANGELOG_PROJECTS.md` - 项目变更历史
- `lfai_github_descriptions.json` - 项目描述缓存（可手动维护）
