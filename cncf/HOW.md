# CNCF 项目获取说明

## 数据来源

项目数据从 [CNCF Landscape](https://github.com/cncf/landscape) 获取：

- Landscape 数据：https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml

## 项目状态区分

CNCF 项目通过 maturity 字段区分状态：

| 状态 | maturity 值 | 说明 |
|------|-------------|------|
| Graduated | `graduated` | 正式毕业项目 |
| Incubating | `incubating` | 孵化中的项目 |
| Sandbox | `sandbox` | 沙箱项目 |
| Archived | `archived` | 已归档的项目 |

## 项目变迁记录

CNCF 项目变更包括：

- **New**: 新增到某个状态的项目
- **Graduated**: 从 Incubating 升级到 Graduated
- **Archived**: 变为 Archived 状态

## 运行方式

```bash
cd cncf
python main.py
```

## 生成文件

- `README.md` - 所有 CNCF 项目列表，按 Graduated / Incubating / Sandbox / Archived 分组
- `CHANGELOG_PROJECTS.md` - 项目变更历史
