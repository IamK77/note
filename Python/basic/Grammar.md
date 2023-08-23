# Grammar

## variable

变量的本质就是要在内存的某个位置开辟空间，用来保存数据；

### variable name

变量名的命名规则：

- 变量名只能是字母、数字或下划线的任意组合
- 变量名的第一个字符不能是数字
- keyword关键字不能声明为变量名
- 变量名区分大小写

```python
x = 1   # 将1赋值给变量x
y = 2   # 将2赋值给变量y
z = x + y   # 将x+y的结果赋值给变量z
z_1 = z + 1 # 将z+1的结果赋值给变量z_1
z_1 = z_1 + 1   # 将z_1+1的结果赋值给变量z_1
_z = 1  # 变量名可以以下划线开头


```

- 驼峰命名法
  - 大驼峰：每个单词的首字母都大写，例如：MyName
  - 小驼峰：第一个单词首字母小写，其他单词首字母大写，例如：myName

- 蛇形命名法
  - 单词之间用下划线连接，例如：my_name

### variable use

变量的使用：

```python
var_int = 1 # 变量可以是整型
var_string = "String" # 变量可以是字符串
var_func = lambda x: x+1    # 变量可以是函数
var_cls = MyClass()    # 变量可以是类
var_list = [1,2,3]  # 变量可以是列表
var_tuple = (1,2,3) # 变量可以是元组
var_dict = {"key": "value"} # 变量可以是字典
var_set = {1,2,3}   # 变量可以是集合
...
```

在python中，我们更多的使用蛇形命名法来命名变量，且以此对变量进行分类，例如：

```python
int_1 = 1
int_2 = 2
str_1 = "String"
str_2 = "String"
func_1 = lambda x: x+1
func_2 = lambda x: x+2
cls_1 = MyClass()
cls_2 = MyClass()
```

以下进行一个简单的赋值打印

print在python中是一个函数，用来打印输出，它是一个内置函数，不需要导入

```python
hello = "Hello World!"
print(hello)
```

result:

```python
Hello World!
```

## data type

### int

整型，python中的整型是没有大小限制的，可以是一个无限大的整数

```python
a = 1
b = 2
c = a + b
print(c)
```

result:

```python
3
```

### float

浮点型，python中的浮点型也是没有大小限制的，可以是一个无限大的浮点数

```python
a = 1.1
b = 2.2
c = a + b
print(c)
```

result:

```python
3.3000000000000003      # 为什么不等于3.3呢？浮点数的精度问题，如何解决留到下文讲解
```

### bool

布尔型，python中的布尔型只有两个值，True和False，可以和数字相加

```python
a = True
b = False
c = a + 1
d = b + 1
print(c)
print(d)
```

result:

```python
2
1
```

### str

字符串，python中的字符串可以使用单引号或者双引号，也可以使用三引号，三引号可以换行

```python
a = "Hello World!"
b = 'Hello World!'
c = """Hello
World!"""
print(a)
print(b)
print(c)
```

result:

```python
Hello World!
Hello World!
Hello
World!
```

### list

列表，python中的列表是一个有序的集合，可以随时添加和删除其中的元素

**列表从0开始索引**

```python
a = [1,2,3]
a[0]    # 1
a[1]    # 2
a[2]    # 3
```

```python
a = [1,2,3]
b = ["a","b","c"]
c = [1,"a",True]
print(a)
print(b)
print(c)
print(a[0])
print(a[1])
print(a[10])
```

result:

```python
[1, 2, 3]
['a', 'b', 'c']
[1, 'a', True]
1
2
Traceback (most recent call last):
  File "D:/Python/basic/basic_grammar.py", line 9, in <module>
    print(a[10])
IndexError: list index out of range     # 索引超出范围,抛出错误,列表中没有第10个元素
```

### tuple

元组，python中的元组和列表类似，但是元组一旦初始化就不能修改

```python
a = (1,2,3)
b = ("a","b","c")
c = (1,"a",True)
print(a)
print(b)
print(c)
```

result:

```python
(1, 2, 3)
('a', 'b', 'c')
(1, 'a', True)
```

### dict

字典，python中的字典是另一种可变容器模型，且可存储任意类型对象，使用键值对存储数据，可以随时添加和删除其中的元素

键必须是唯一的，但值则不必

```python
a = {"key1": "value1", "key2": "value2"}
b = {}
print(a)
```

result:

```python
{'key1': 'value1', 'key2': 'value2'}
```

### set

集合，python中的集合是一个无序的不重复元素序列，可以随时添加和删除其中的元素

```python
a = {1,2,3}
b = set()   # 创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典的
print(a)
```

result:

```python
{1, 2, 3}
```

### type

内置函数type可以查看变量的类型

```python
a = 1
b = 1.1
c = True
d = "Hello World!"
e = [1,2,3]
f = (1,2,3)
g = {"key1": "value1", "key2": "value2"}
h = {1,2,3}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
```

result:

```python
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'set'>
```

## operator

### arithmetic operator

算术运算符

```python
a = 1
b = 2
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** b
i = a // b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
```

result:

```python
3  # 加
-1  # 减
2   # 乘
0.5 # 除
1   # 取余  1/2=0...1
1   # 幂    1^2=1   即1的2次方
0   # 取整  1/2=0.5 取整为0，结果向下取整 例如1.7取整为1，-1.7取整为-2
```

### comparison operator

比较运算符

返回值为bool型的数据

```python
a = 1
b = 2
c = a > b
d = a < b
e = a == b
f = a != b
g = a >= b
h = a <= b
print(c)
...
print(h)
```

result:

```python
False   # 大于
True    # 小于
False   # 等于
True    # 不等于
False   # 大于等于
True    # 小于等于
```

注意此处的等于，python中的等于是==，而=是赋值
```python
a = 1   # 将1赋值给变量a
a == 1  # 判断a是否等于1
```

### assignment operator

赋值运算符

```python
a = 1
c = 3
c += a  # c = c + a
print(c)
c -= a  # c = c - a
print(c)
c *= a  # c = c * a
print(c)
c /= a  # c = c / a
print(c)
```

result:

```python
4
2
3
3.0
```

### logical operator

逻辑运算符

返回值为bool型的数据

```python
a = True
b = False
c = a and b    # 与     两个都为真才为真
d = a or b     # 或     一个为真就为真
e = not a      # 非     取反
print(c)
print(d)
print(e)
```

result:

```python
False
True
False
```

### membership operator

成员运算符

返回值为bool型的数据

```python
a = [1,2,3]
b = 1
c = 4
d = b in a  # 判断b是否在a中
e = c not in a  # 判断c是否不在a中
print(d)
print(e)
```

result:

```python
True
True
```

### identity operator

身份运算符

返回值为bool型的数据

```python
a = 1
b = 1
c = 2
d = a is b  # 判断a是否是b
e = a is not c  # 判断a是否不是c
print(d)
print(e)
```

result:

```python
True
True
```

## control flow

### if

if语句用来判断一个条件是否成立，如果成立则执行if下面的代码，如果不成立则不执行

```python
a = 1
if a == 1:
    print("a == 1")
```

result:

```python
a == 1
```

### if else

if else语句用来判断一个条件是否成立，如果成立则执行if下面的代码，如果不成立则执行else下面的代码

```python
a = 2
if a == 1:
    print("a == 1")
else:
    print("a != 1")
```

result:

```python
a != 1
```

### if elif else

if elif else语句用来判断多个条件是否成立，如果成立则执行if下面的代码，如果不成立则判断elif下面的代码，如果elif成立则执行elif下面的代码，如果elif不成立则执行else下面的代码

```python
a = 2
if a == 1:
    print("a == 1")
elif a == 2:
    print("a == 2")
else:
    print("a != 1 and a != 2")
```

result:

```python
a == 2
```

### for

for循环用来遍历一个可迭代对象itarable，例如列表、元组、字典、字符串等

```python
for i in [1,2,3]:
    print(i)
```

result:

```python
1
2
3
```

code1:
```python
for _ in "hello":
    print("world")
```

result:

```python
world
world
world
world
world
```

code2:
```python
for i in {"key1": "value1", "key2": "value2"}:
    print(i)
```

result:

```python
key1
key2
```

code3:
```python
for i in {"key1": "value1", "key2": "value2"}.values():
    print(i)
```

result:

```python
value1
value2
```

code4:
```python
for i in {"key1": "value1", "key2": "value2"}.items():
    print(i)
```

result:

```python
('key1', 'value1')
('key2', 'value2')
```

### while

while循环用来判断一个条件是否成立，如果成立则执行while下面的代码，如果不成立则不执行

```python
a = 1
while a < 3:
    print(a)
    a += 1
```

result:

```python
1
2
# 当a=3时，a<3不成立，循环结束
```

### break

break用来跳出循环

```python
a = 1
while True:
    print(a)
    a += 1
    if a == 3:
        break
```

result:

```python
1
2
# 当a=3时，a==3成立，跳出循环
```

### continue

continue用来跳过本次循环，继续下一次循环

```python
a = 1
while a < 3:
    a += 1
    if a == 2:
        continue
    print(a)
```

result:

```python
3
# 当a=1时，进入循环后a += 1，a==2成立，跳过本次循环，继续下一次循环
```

### pass

pass用来占位，不做任何操作

```python
def func():
    pass
```

## function

在python中，函数是一段可以重复使用的代码块，可以接受参数，也可以返回值，参数经过一定逻辑后，返回一个结果

func的完整结构如下

```python
def func_name(param1: param1_type, param2: param2_type, ..., param9: int = 1) -> result_type:
    """
    some description
    param1: param1_description
    param2: param2_description
    ...
    return: result_description
    """
    # do something
    return result

func_name(arg1, arg2, ...)
```

- func_name: 函数名，命名规则同变量名
- param1: 参数1，命名规则同变量名
- param1_type: 参数1的类型，可以是int、str、bool、list、tuple、dict、set等
- param1_description: 参数1的描述，可以是任意字符串
- param2: 参数2，命名规则同变量名
- ...
- result_type: 返回值的类型，可以是int、str、bool、list、tuple、dict、set等
- result_description: 返回值的描述，可以是任意字符串

完整的func结构太过复杂，我们先来看一个简单的func

```python
def func(a, b = 1):
    """
    在这这个函数中，param_type和result_type都是可以省略的，因为python是动态语言，不需要指定类型
    在这里面a和b是形参，形参就是在定义函数时，括号中的参数，形参只有在函数内部有效
    b = 1是默认参数，如果调用函数时没有传入b的值，则b的值为1
    如果传入了b的值，则b的值为传入的值
    默认参数必须在位置参数后面
    """
    return a + b

print(func(1, 2))   # 3
```

### parameter

参数分为两种，一种是位置参数，一种是关键字参数

位置参数必须在关键字参数前面

```python
def func(a, b, c):
    return a + b + c

print(func(1, 2, 3))    # 6
# 此处均为位置参数，1赋值给a，2赋值给b，3赋值给c
print(func(1, c = 3, b = 2))    # 6
# 此处位置参数为1，关键字参数为c = 3, b = 2
print(func(a = 1, b = 2, c = 3))    # 6
# 此处关键字参数为a = 1, b = 2, c = 3
print(func(a = 1, c = 3, b = 2))    # 6
# 此处关键字参数为a = 1, c = 3, b = 2
```

### default parameter

默认参数必须在位置参数后面

```python
def func(a, b = 1):
    return a + b

print(func(1))  # 2
# 此处位置参数为1，b没有传值，b的值为默认值1
print(func(1, 2))   # 3
# 此处位置参数为1，b传值为2，b的值为传入的值2
```

### variable parameter

可变参数可以接受任意数量的参数，可变参数必须在位置参数和默认参数后面

```python
def func(a, *args):
    """
    *args是可变参数，可以接受任意数量的参数，接受到的参数会被组装成一个元组
    """
    print(a)
    print(args)

func(1, 2, 3, 4, 5)
```

result:

```python
1
(2, 3, 4, 5)
```

### keyword parameter

关键字参数可以接受任意数量的参数，关键字参数必须在位置参数和默认参数后面

```python
def func(a, **kwargs):
    """
    **kwargs是关键字参数，可以接受任意数量的参数，接受到的参数会被组装成一个字典
    """
    print(a)
    print(kwargs)

func(1, b = 2, c = 3, d = 4, e = 5)
```

result:

```python
1
{'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

### unpack parameter

解包参数，将一个列表或者元组解包成位置参数，将一个字典解包成关键字参数

```python
def func(a, b, c):
    print(a)
    print(b)
    print(c)

func(*[1,2,3])
```

result:

```python
1
2
3
```

```python
def func(a, b, c):
    print(a)
    print(b)
    print(c)

func(**{"a": 1, "b": 2, "c": 3})
```

result:

```python
# 同上
```

### lambda

lambda表达式用来创建一个匿名函数，lambda表达式的完整结构如下

```python
lambda param1, param2, ..., param9: result
```

- param1: 参数1，命名规则同变量名
- param2: 参数2，命名规则同变量名
- ...
- result: 返回值，可以是任意类型

```python
func = lambda a, b: a + b
print(func(1, 2))
```

result:

```python
3
```










