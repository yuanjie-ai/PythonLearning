# :rocket: UDF :facepunch:
---

## List(spark array)
- 列表去重顺序不变
```
listUnique = lambda x: sorted(list(set(x)), key=x.index)
```
- 列表相减顺序不变
```
listSub = lambda a,b: [a[i] for i in np.where([i not in b for i in a])[0]]
```
- 列表一列裂变成多列
```
def listExplode(df,colname='name'):
    n = len(df.select(colname).first()[0])
    names = df.columns + [col(colname)[i].name(colname+str(i)) for i in range(n)]
    return df.select(names)
    
df = spark.createDataFrame([[[1,2,3]]], ['a'])
listExplode(df, 'a').show()
+---------+---+---+---+
|        a| a0| a1| a2|
+---------+---+---+---+
|[1, 2, 3]|  1|  2|  3|
+---------+---+---+---+
```
---
## colToList
> df为一列
- 取列前几行
```
def takeN(df, n=5):
    return np.array(df.take(n)).flatten().tolist()

df = spark.range(10)
takeN(df)
[0, 1, 2, 3, 4]
```
- 将整列转换成列表
```
def colToList(df):
    return takeN(df.select(collect_list(df.columns[0])), n=1)

colToList(df)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```