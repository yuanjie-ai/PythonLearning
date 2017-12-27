<h1 align = "center">:rocket: 更好用的时间模块 :facepunch:</h1>

---
## 创建时间
- pendulum.create
- pendulum.create_from_timestamp(time.time(), 'local')

## 加减
```python
from datetime import timedelta # days
p.add_timedelta(timedelta(10))
p.subtract_timedelta(timedelta(10))
p.add() # 推荐
p.subtract() 
str(p.diff(p.add(1))) # pendulum对象作差
```
## 年月日时分秒
> p = pendulum.create_from_timestamp(time.time(), 'local')
- p.second
- p.second_(1)
- p.seconds_since_midnight(): 距离0点多少秒
- p.seconds_until_end_of_day(): 距离24点多少秒
- p.minute
- p.minute(1)
- p.hour
- p.hour_(1)
- p.day
- p.day_of_week
- p.day_of_year
- p.days_in_month


- p.date()
- p.day_(1): 时间平移到当月某天
- p.yesterday()
- p.today()
- p.tomorrow()

- p.day_of_week: p.isoweekday()
- p.week_of_month
- p.week_of_year
- p.weekday()
- p.is_weekday(): 1-5
- p.is_weekend(): [6, 0] 默认也可以自定义
- p.is_monday()
- p.is_tuesday()
- p.is_wednesday()
- p.is_thursday()
- p.is_friday()
- p.is_saturday()
- p.is_sunday()

- p.month
- p.month_(1): 时间平移到当年某月
- p.year
- p.year_(2016)

## time格式
- p.ctime()
- p.time()
- p.timetz()
- p.timestamp()
- p.int_timestamp()
- p.float_timestamp()
- p.timestamp_(p.timestamp()): 时间戳转换成Pendulum对象
- p.fromtimestamp(p.timestamp()): 时间戳转换成Pendulum对象
- p.timetuple()
- p.utctimetuple()

## 时区
- pendulum.timezones
- p.astimezone(tz=None): 时间转换到tz时区
- p.in_timezone('Asia/Shanghai')
- p.get_timezone()
- p.timezone
- p.timezone_
- p.timezone_name

## string
- p.to_time_string()
- p.to_date_string()
- p.to_datetime_string()

- p.to_atom_string()
- p.to_cookie_string()
- p.to_day_datetime_string()

- p.to_formatted_date_string()
- p.to_iso8601_string()
- p.to_rfc1036_string()
- p.to_rfc1123_string()
- p.to_rfc2822_string()
- p.to_rfc3339_string()
- p.to_rfc822_string()
- p.to_rfc850_string()
- p.to_rss_string()
- p.to_w3c_string()

# Pendulum格式
- p.set_to_string_format('%Y-%m-%d')
- p.reset_to_string_format()
