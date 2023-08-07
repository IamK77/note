# List Method

通过`print(dir(list))`可以查看list的所有方法

List的内置方法可以方便我们对列表进行操作

### append()

`append()`方法用于在列表末尾添加新的对象

```python
list_ = ['a', 'b', 'c']
list_.append('d')   # ['a', 'b', 'c', 'd']
```

- param: object: 添加的对象
- return: None

### clear()

`clear()`方法用于清空列表

```python
list_ = ['a', 'b', 'c']
list_.clear()   # []
```

- param: None
- return: None

### copy()

`copy()`方法用于复制列表

```python
list_ = ['a', 'b', 'c']
list_copy = list_.copy()    # ['a', 'b', 'c']
```

- param: None
- return: list

### count()

`count()`方法用于统计某个元素在列表中出现的次数

```python
list_ = ['a', 'b', 'c', 'a', 'b', 'c']
list_.count('a')    # 2
```

- param: object
- return: int

### extend()

`extend()`方法用于在列表末尾一次性追加另一个序列中的多个值

```python
list_ = ['a', 'b', 'c']
list_.extend(['d', 'e', 'f'])   # ['a', 'b', 'c', 'd', 'e', 'f']
```

- param: iterable: 可迭代对象，在基础数据类型中，只有字符串、列表、元组、字典、集合是可迭代对象
- return: None

### index()

`index()`方法用于从列表中找出某个值第一个匹配项的索引位置

```python
list_ = ['a', 'b', 'c']
list_.index('b')    # 1
```

- param: object：查找的对象
- return: int

### insert()

`insert()`方法用于将对象插入到列表中的指定位置

```python
list_ = ['a', 'b', 'c']
list_.insert(1, 'd')    # ['a', 'd', 'b', 'c']
```

- param: index: 插入的位置
- param: object: 插入的对象
- return: None

### pop()

`pop()`方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

```python
list_ = ['a', 'b', 'c']
get = list_.pop()    # ['a', 'b']
print(get)    # c

list_ = ['a', 'b', 'c']
get = list_.pop(1)    # ['a', 'c']
print(get)    # b
```

- param: index
- return: object

### remove()

`remove()`方法用于移除列表中某个值的第一个匹配项

```python
list_ = ['a', 'b', 'c']
list_.remove('b')    # ['a', 'c']
```

- param: object
- return: None

### reverse()

`reverse()`方法用于反向列表中元素

```python
list_ = ['a', 'b', 'c']
list_.reverse()    # ['c', 'b', 'a']
```

- param: None
- return: None

### sort()

`sort()`方法用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数

```python
list_ = ['2', '1', '3']
list_.sort()    # ['1', '2', '3']
# 按照ASCII码排升序

list_ = [['a', 2], ['ab',1], ['abc', 3]]
list_.sort()    # [['a', 2], ['ab', 1], ['abc', 3]]
list_.sort(key=lambda x: x[1])    # [['ab', 1], ['a', 2], ['abc', 3]]
# 传入函数，按照列表中元素的第二个元素进行排序

list_ = [['a', 2], ['ab',1], ['abc', 3]]
list_.sort(reverse=True)    # [['abc', 3], ['a', 2], ['ab', 1]]
# 降序
```

- param: key：指定比较的元素，key=lambda x: x[1]，表示按照列表中元素的第二个元素进行排序
- param: reverse：True为降序，False为升序
- return: None


## Silce

切片操作可以对可迭代对象进行切片操作

### 切片操作

Silce[开始:结束:步长]
- 开始：切片操作开始的位置
- 结束：切片操作结束的位置
- 步长：切片操作的步长



```python
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
list_[1:5:3]    
# 从1开始，即'b'开始，到5结束，即'f'结束，但不包括'f'，步长为3，即每隔两个元素取一个元素
# ['b', 'e']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#   0    1    2    3    4    5    6    7    8    9
#      开始   1    2    3    结束
list_[-1:-9:-2]
# 从-1开始，即'j'开始，到-9结束，即'b'结束，但不包括'b'，步长为-2，即每隔一个元素取一个元素
# ['j', 'h', 'f', 'd']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#  -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
#       结束   1   取    1    取    1    取   1   开始
```


```python
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

list_[1:5]    # ['b', 'c', 'd', 'e']    
# 左闭右开，切片操作从1开始，即'b'开始，到5结束，即'f'结束，但不包括'f'
list_[:5]    # ['a', 'b', 'c', 'd', 'e']
# 从0开始，即'a'开始，到5结束，即'f'结束，但不包括'f'
list_[1:]    # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 从1开始，即'b'开始，到最后结束
list_[:]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 从0开始，即'a'开始，到最后结束
list_[1:5:2]    # ['b', 'd']
# 从1开始，即'b'开始，到5结束，即'f'结束，但不包括'f'，步长为2，即每隔一个元素取一个元素
list_[::-1]    # ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
```






