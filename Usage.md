# 使用文档

自动生成 Apache 项目介绍信息，并根据类型进行分组（Active/Incubating/Retired）
```python
# 需要 python 3.9 以上的版本
python main.py
```

- 可以修改中文描述`介绍:`，修改后会保存，下次更新时也不会覆盖，但英文描述会被覆盖；

TODO
- 有些[apache项目](https://projects.apache.org/projects.html?name)在官方会有多个项目列表，
如 Fluo 包含了Apache Fluo,Apache Fluo Recipes,Apache Fluo YARN