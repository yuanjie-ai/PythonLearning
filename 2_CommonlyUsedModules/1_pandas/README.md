<h1 align = "center">:rocket: pandas :facepunch:</h1>

---
## 日期
```python
pd.to_datetime(df2.head()['ALTDATE']).diff()

0         NaT
1   -396 days
2    485 days
3   -516 days
4     31 days
Name: ALTDATE, dtype: timedelta64[ns]

# to day
pd.to_datetime(df2.head()['ALTDATE']).diff()/np.timedelta64(1, 'D')
pd.to_datetime(df2.head()['ALTDATE']).diff().astype('timedelta64[D]')

0      NaN
1   -396.0
2    485.0
3   -516.0
4     31.0
Name: ALTDATE, dtype: float64

```
## query
```
 df.query('x < 3')
 df[df.x < 3]
```
encoding='latin1'
