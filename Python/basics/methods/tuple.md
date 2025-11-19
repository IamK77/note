# Tuple Method

通过`print(dir(tuple))`可以查看tuple的所有方法

tuple的内置方法可以方便我们对元组进行操作

### count()

`count()`方法用于统计某个元素在元组中出现的次数

```python
tuple_ = ('a', 'b', 'c', 'a', 'b', 'c')
tuple_.count('a')    # 2
```

- param: object
- return: int

### index()

`index()`方法用于从元组中找出某个值第一个匹配项的索引位置

```python
tuple_ = ('a', 'b', 'c', 'a', 'b', 'c')
tuple_.index('a')    # 0
```

- param: object
- return: int
