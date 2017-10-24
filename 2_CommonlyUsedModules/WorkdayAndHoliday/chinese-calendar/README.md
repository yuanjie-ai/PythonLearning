<h1 align = "center">:rocket: 节假日 :facepunch:</h1>

---
```
import datetime
from chinese_calendar.utils import is_workday, is_holiday
march_first = datetime.date(2017, 5, 1)
print(is_workday(march_first))  # False
print(is_holiday(march_first))  # True
```
