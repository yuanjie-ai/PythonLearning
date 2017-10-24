<h1 align = "center">:rocket: 节假日筛选 :facepunch:</h1>

---
- lunardate: 阳历转农历
- chinese_calendar
```
import datetime
from chinese_calendar.utils import is_workday, is_holiday
march_first = datetime.date(2017, 5, 1)
print(is_workday(march_first))  # False
print(is_holiday(march_first))  # True
```
