# Set Method

通过`print(dir(set))`可以查看set的所有方法

set的内置方法可以方便我们对集合进行操作

### add()

`add()`方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作

```python
set_ = {'a', 'b', 'c'}
set_.add('d')   # {'a', 'b', 'c', 'd'}
set_.add('a')   # {'a', 'b', 'c', 'd'}
```

- param: object: 要添加的元素
- return: None

### clear()

`clear()`方法用于移除集合中的所有元素

```python
set_ = {'a', 'b', 'c'}
set_.clear()   # set()
```

- param: None
- return: None

### copy()

`copy()`方法用于拷贝一个集合

```python
set_ = {'a', 'b', 'c'}
set_copy = set_.copy()    # {'a', 'b', 'c'}
```

- param: None
- return: set

### difference()

`difference()`方法用于返回多个集合的差集

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}
set_1.difference(set_2)    # {'c'}
```

- param: set: 要比较的集合
- return: set

### difference_update()

`difference_update()`方法用于移除集合中的元素，该元素在指定的集合也存在

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}
set_1.difference_update(set_2)    # {'c'}
print(set_1)    # {'c'}
```

- param: set: 要比较的集合
- return: None

### discard()

`discard()`方法用于移除指定的集合元素

```python
set_ = {'a', 'b', 'c'}
set_.discard('a')   # {'b', 'c'}
```

- param: object: 要移除的元素
- return: None

### intersection()

`intersection()`方法用于返回集合的交集

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}
set_1.intersection(set_2)    # {'a', 'b'}
```

- param: set: 要比较的集合
- return: set

### intersection_update()

`intersection_update()`方法用于获取两个或更多集合中都重叠的元素，即计算交集

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}

set_1.intersection_update(set_2)    # {'a', 'b'}
print(set_1)    # {'a', 'b'}
```

- param: set: 要比较的集合
- return: None

### isdisjoint()

`isdisjoint()`方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}

set_1.isdisjoint(set_2)    # False  
# set_1 和 set_2 有相同的元素 a 和 b，因此返回 False
```

- param: set: 要比较的集合
- return: bool

### issubset()

`issubset()`方法用于判断指定集合是否为该方法参数集合的子集

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'c', 'd'}
set_3 = {'a', 'b', 'e'}

set_1.issubset(set_2)    # True
set_1.issubset(set_3)    # False
```

- param: set: 要比较的集合
- return: bool

### issuperset()

`issuperset()`方法用于判断该方法的参数集合是否为指定集合的子集

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'c', 'd'}
set_3 = {'a', 'b', 'e'}

set_2.issuperset(set_1)    # True
set_3.issuperset(set_1)    # False
```

- param: set: 要比较的集合
- return: bool

### pop()

`pop()`方法用于随机移除一个元素

```python
set_ = {'a', 'b', 'c'}
get = set_.pop()   
print(get)    # c
print(set_)   # {'a', 'b'}
```

- param: None
- return: object

### remove()

`remove()`方法用于移除集合中的指定元素

```python
set_ = {'a', 'b', 'c'}
set_.remove('a')   # {'b', 'c'}
```

- param: object: 要移除的元素
- return: None

### symmetric_difference()

`symmetric_difference()`方法用于返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}

set_1.symmetric_difference(set_2)    # {'c', 'd'}
```

- param: set: 要比较的集合
- return: set

### symmetric_difference_update()

`symmetric_difference_update()`方法用于获取两个集合中不重复的元素集合，即会移除两个集合中都存在的元素

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}

set_1.symmetric_difference_update(set_2)    # {'c', 'd'}
print(set_1)    # {'c', 'd'}
```

- param: set: 要比较的集合
- return: None

### union()

`union()`方法用于返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}

set_1.union(set_2)    # {'a', 'b', 'c', 'd'}
```

- param: set: 要比较的集合
- return: set

### update()

`update()`方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略

```python
set_1 = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'd'}

set_1.update(set_2)    # {'a', 'b', 'c', 'd'}
print(set_1)    # {'a', 'b', 'c', 'd'}
```

- param: set: 要比较的集合
- return: None



