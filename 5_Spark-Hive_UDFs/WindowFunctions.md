# :rocket: [Windowing and Analytics Functions][1] :facepunch:
---
```
df1 = spark.range(5).withColumn('a', lit(8))
df2 = spark.range(5, 10).withColumn('a', lit(88))
df = df1.union(df2)

+---+---+
| id|  a|
+---+---+
|  0|  8|
|  1|  8|
|  2|  8|
|  3|  8|
|  4|  8|
|  5| 88|
|  6| 88|
|  7| 88|
|  8| 88|
|  9| 88|
+---+---+
```
---
## RankingFunctions
- ROW_NUMBER
```
row_number() OVER(PARTITION BY xx ORDER BY xx)
row_number().over(Window.partitionBy("xx").orderBy("xx"))
```
- RANK: 排名相等留下空位(1,2,2,4,5)
- DENSE_RANK: 排名相等不留空位(1,2,2,3,4)
- PERCENT_RANK: 分位数分布
- NTILE: ntile(n): 1/n比例切割
```
df.withColumn('new',expr("ntile(5) OVER(PARTITION BY a ORDER BY id) ")).show()

+---+---+---+
| id|  a|new|
+---+---+---+
|  5| 88|  1|
|  6| 88|  2|
|  7| 88|  3|
|  8| 88|  4|
|  9| 88|  5|
|  0|  8|  1|
|  1|  8|  2|
|  2|  8|  3|
|  3|  8|  4|
|  4|  8|  5|
+---+---+---+
```
---
```
df.withColumn('new',expr("id - mean(id) OVER() ")).show()
+---+---+----+
| id|  a| new|
+---+---+----+
|  0|  8|-4.5|
|  1|  8|-3.5|
|  2|  8|-2.5|
|  3|  8|-1.5|
|  4|  8|-0.5|
|  5| 88| 0.5|
|  6| 88| 1.5|
|  7| 88| 2.5|
|  8| 88| 3.5|
|  9| 88| 4.5|
+---+---+----+

df.withColumn('new',expr("mean(id) OVER(PARTITION BY a) ")).show()
+---+---+---+
| id|  a|new|
+---+---+---+
|  5| 88|7.0|
|  6| 88|7.0|
|  7| 88|7.0|
|  8| 88|7.0|
|  9| 88|7.0|
|  0|  8|2.0|
|  1|  8|2.0|
|  2|  8|2.0|
|  3|  8|2.0|
|  4|  8|2.0|
+---+---+---+
```
[1]: https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics
