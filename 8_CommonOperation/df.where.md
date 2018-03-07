## NaN入库转化None
```python
df.where(df.notnull(), None)
```
