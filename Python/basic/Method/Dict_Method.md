# Dict Method

通过`print(dir(dict))`可以查看dict的所有方法

dict的内置方法可以方便我们对字典进行操作

### clear()

`clear()`方法用于删除字典内所有元素

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.clear()   # {}
```

- param: None
- return: None

### copy()

`copy()`方法用于返回一个字典的浅复制

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_copy = dict_.copy()    # {'a': 1, 'b': 2, 'c': 3}
```

- param: None
- return: dict

### fromkeys()

`fromkeys()`方法用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值

```python
dict_ = dict.fromkeys(['a', 'b', 'c'], 1)    # {'a': 1, 'b': 1, 'c': 1}
example = dict.fromkeys([1, 2, 3], ['1', '2', '3'])    
# {1: ['1', '2', '3'], 2: ['1', '2', '3'], 3: ['1', '2', '3']}
```

- param: seq: 字典的键; 
- param: value: 字典的值
- return: dict

### get()

`get()`方法用于返回指定键的值，如果值不在字典中返回默认值

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.get('a')  # 1
dict_.get('d')  # None
dict_.get('d', 4)   # 4
print(dict_)    # {'a': 1, 'b': 2, 'c': 3}  .get('d', 4)后字典不变
```

- param: key: 字典中要查找的键
- param: default: 如果指定键的值不存在时，返回该默认值
- return: value

### items()

`items()`方法用于以列表返回可遍历的(键, 值) 元组数组

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.items()   # dict_items([('a', 1), ('b', 2), ('c', 3)])
for _ in dict_.items():
    print(_)    # ('a', 1) ('b', 2) ('c', 3)
```

- param: None
- return: list

### keys()

`keys()`方法用于返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有键

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.keys()    # dict_keys(['a', 'b', 'c'])
print(list(dict_.keys())[2])    # c
for _ in dict_.keys():
    print(_)    # a b c
```

- param: None
- return: iterator

### pop()

`pop()`方法用于删除字典给定键 key 所对应的值，返回值为被删除的值

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.pop('a')  # 1
print(dict_)    # {'b': 2, 'c': 3}
```

- param: key: 要删除的键值
- return: value

### popitem()

`popitem()`方法用于随机返回并删除字典中的一对键和值

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.popitem() # ('c', 3)
print(dict_)    # {'a': 1, 'b': 2}
```

- param: None
- return: tuple

### setdefault()

`setdefault()`方法和get()方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.setdefault('d', 4)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_.setdefault('a', 4)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

- param: key: 要查找的键值
- param: default: 如果指定键的值不存在时，返回该默认值
- return: value

### update()

`update()`方法用于修改字典中的值

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.update({'a': 4, 'd': 5})  # {'a': 4, 'b': 2, 'c': 3, 'd': 5}
```

- param: dict: 添加到指定字典dict_中的字典
- return: None

### values()

`values()`方法用于返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值

```python
dict_ = {'a': 1, 'b': 2, 'c': 3}
dict_.values()  # dict_values([1, 2, 3])
print(list(dict_.values())[2])  # 3
for _ in dict_.values():
    print(_)    # 1 2 3
```

- param: None
- return: iterator

### dict()

`dict()`方法用于创建一个字典

```python
dict_ = dict([('a', 1), ('b', 2), ('c', 3)])    # {'a': 1, 'b': 2, 'c': 3}
```

- param: iterable: 可迭代对象
- return: dict

