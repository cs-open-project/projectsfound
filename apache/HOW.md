# Apache 项目获取说明

## 数据来源

项目数据从 [Apache Projects](https://projects.apache.org/) 获取，包括：

- **Committees**: https://projects.apache.org/json/foundation/committees.json
- **Projects**: https://projects.apache.org/json/foundation/projects.json
- **Podlings (Incubating)**: https://projects.apache.org/json/foundation/podlings.json
- **Podlings History**: https://projects.apache.org/json/foundation/podlings-history.json

## 项目状态区分

Apache 项目通过 `pmc` 字段区分状态：

| 状态 | pmc 值 | 说明 |
|------|--------|------|
| Graduated | 非 `incubator` / `attic` | 正式毕业项目 |
| Incubating | `incubator` | 孵化中的项目 |
| Attic | `attic` | 已退役的项目 |

## 运行方式

```bash
cd apache
python main.py
```

## 生成文件

- `README.md` - 所有 Apache 项目列表，按 Graduated / Incubating / Attic 分组
- `CHANGELOG_PROJECTS.md` - 项目变更历史，记录新增、毕业、退役的项目
