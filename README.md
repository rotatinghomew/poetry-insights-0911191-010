# 流动诗词课堂服务缺口与选点方案复核

本项目保存流动课堂排期所需的合成学校班级、可达时窗、场次容量、预约及服务规则，均使用 UTF-8 CSV。空字段表示记录未提供。

## 数据

- `data/schools.csv`：班级人数、服务优先级及确认状态。
- `data/travel_windows.csv`：学校至场馆的分时到达区间。
- `data/sessions.csv`：地点、场次、席位、人员及开放时间。
- `data/reservations.csv`：班级已确认和候补席位。
- `data/rules.csv`：重点区域底线、保护席位及释放时点。

## 环境与验证

需要 Python 3.11 或更新版本；项目仅使用 Python 标准库。可用 `python3 -m unittest discover -s tests -v` 检查 CSV 结构与本地资料完整性。
