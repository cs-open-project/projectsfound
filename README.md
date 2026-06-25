# Open Source Projects Found

自动化获取主流开源基金会的所有项目，并生成格式统一的项目列表。

## 支持的基金会

| 基金会 | 项目数量 | 说明 |
|--------|----------|------|
| [Apache Software Foundation](./apache/) | 400+ | 包含 Top-Level Projects 和 Incubating 项目 |
| [Cloud Native Computing Foundation](./cncf/) | 250+ | 包含 Graduated、Incubating、Sandbox 项目 |

## 项目列表

- **[Apache 项目列表](./apache/README.md)** - Apache 软件基金会所有开源项目
- **[CNCF 项目列表](./cncf/README.md)** - 云原生计算基金会所有开源项目

## 快速开始

```bash
# Apache 项目
python apache/main.py

# CNCF 项目
python cncf/main.py
```

## 环境要求

- Python 3.8+
- requests
- PyYAML

```bash
pip install requests PyYAML
```

## 数据来源

- Apache: [projects.apache.org](https://projects.apache.org/)
- CNCF: [github.com/cncf/landscape](https://github.com/cncf/landscape)

## License

[Apache License 2.0](./LICENSE)
