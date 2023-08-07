# Class

Python中的类是一种数据结构，它将数据和操作数据的方法组合在一起。类的实例是类的具体对象，它具有类定义的行为。类实例化后，可以使用其属性和方法。

类体现了oop(面向对象编程)的思想，面向对象编程的核心思想是将数据和操作数据的方法组合在一起，这样能够更加方便地对数据进行操作。

## 面向对象编程

在Python中，万物皆对象\
在Python中，一切皆对象，包括整数、浮点数、字符串、列表、元组、字典、函数、模块、类等等，这些都是对象，它们都有自己的属性和方法。\
在Python中，对象是通过类来创建的，类是对象的抽象，对象是类的具体实例。

例如，我们在生活中创建一个类，我们说有一种人，他聪明、善良、勤奋、有责任心，这些就是这种人的属性，我们把这种人叫做“好人”，这就是一个类的定义。\
当我们说有一个人，他叫张三，他是一个好人，他聪明、善良、勤奋、有责任心，这就是一个对象的定义，张三就是这个类的一个具体实例。

在下文中，对象为obj，属性为attr，方法为method。

## 类的定义

类的定义使用关键字class，后面紧跟类名，类名通常采用驼峰命名法，紧接着是圆括号，圆括号中是类的父类，如果没有父类，可以省略圆括号。类的定义后面是冒号，冒号后面是类的主体，类的主体中可以定义属性和方法。

```python
# 一个最简单的类的定义
class ClassName():
    # class body
```

接下来，我们引入例子来说明类的定义。

```python
# 有这么一种好人
class GoodMan():
    # 这种好人的属性
    attr = ['聪明', '善良', '勤奋', '有责任心']
    # 这种好人的方法
    def method(self):
        print('这种人是好人')
```

## 类的实例化

上文中，我们定义了一个类，这个类是一种好人，这种好人有一些属性和方法，但是我们并没有具体的好人，我们只是定义了一种好人，那么我们该如何创建一个具体的好人呢？\

我们可以通过类来创建一个具体的对象，这个对象就是类的实例，类的实例化使用类名后面跟圆括号，圆括号中是类的参数，如果没有参数，可以省略圆括号。

```python
# 类的实例化
zhangsan = GoodMan()  # 创建一个具体的好人张三
print(zs.attr)      # 打印这个好人的属性
zs.method()         # 调用这个好人的方法
```

```
result:

```python
['聪明', '善良', '勤奋', '有责任心']
这种人是好人
```

张三就是一个具体的obj，聪明、善良、勤奋、有责任心就是张三的attr，我们可以通过obj.attr来访问对象的属性。还可以通过obj.method()来调用对象的方法。

## 类的初始化

类的初始化是类的一个特殊方法，类的初始化方法是__init__()，类的初始化方法在类的实例化时自动调用，类的初始化方法可以接收参数，参数可以用来初始化类的属性。

```python
# 类的初始化
class GoodMan():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def method(self):
        print('这种人是好人')
```

```python
# 类的实例化
zhangsan = GoodMan('张三', 18)
print(zhangsan.name)
print(zhangsan.age)
```

```
result:

```python
张三
18
```

\_\_init\_\_()是一种特殊的方法，它在类的实例化时自动调用，它的第一个参数是self，self代表类的实例，self后面的参数是类的参数，类的参数可以用来初始化类的属性。在之后的Special Method中，我们会详细介绍和它类似的特殊方法。

self在此处代表的是类的实例，即zhangsan = GoodMan('张三', 18)后的zhangsan

学习过C++的朋友可能会对类的初始化有所了解，C++中的类的初始化是通过构造函数来实现的，Python中的类的初始化是通过__init__()方法来实现的。而self在Python中的作用和this在C++中的作用是类似的，都是代表类的实例。

以下举一个例子

```c++
// C++中的类的初始化
class GoodMan {
public:
    GoodMan(string name, int age) {
        this->name = name;
        this->age = age;
    }
    void method() {
        cout << "这种人是好人" << endl;
    }
private:
    string name;
    int age;
}
```

## 类的方法

类的方法是类的行为，类的方法可以通过类名和实例名来访问，类的方法可以接收参数，参数可以用来初始化类的属性，类的方法可以调用类的属性。

```python
# 类的方法
class GoodMan():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method(self):
        print('这种人是好人')

    def print_name(self):
        print(self.name)
```

```python
# 类的实例化
zhangsan = GoodMan('张三', 18)
zhangsan.method()
zhangsan.print_name()
```

```
result:

```python
这种人是好人
张三
```

### From Function to Method

在Python中，函数和方法是有区别的，函数是独立的，方法是依附于类的，方法是类的行为，方法可以调用类的属性，函数不能调用类的属性。\
且Method的第一个参数大多是self，self代表类的实例，self后面的参数是类的参数，类的参数可以用来初始化类的属性。

```python
# 函数
def function():
    print('function')
```

```python
# 方法
class ClassName():
    def method(self):
        print('method')
```

```python
# 函数的调用
function()
```

```python
# 方法的调用
cn = ClassName()
cn.method()
```

```python
result:

function
method
```


## 类的属性

类的属性是类的特征，类的属性可以是任意类型的数据，包括整数、浮点数、字符串、列表、元组、字典、函数、模块、类等等。

类的属性可以分为两种，一种是类属性，一种是实例属性。

### 类属性

类属性是类的所有实例共有的属性，类属性可以通过类名和实例名来访问，类属性的值可以通过类名和实例名来修改。

```python
# 类属性
class ClassName():
    attr = 'class attr'
    def method(self):
        print('method')
```

```python
# 类属性的访问
print(ClassName.attr)
cn = ClassName()
print(cn.attr)
```
```python
result:
class attr
class attr
```

```python
# 类属性的修改
ClassName.attr = 'new class attr'
print(ClassName.attr)
cn.attr = 'new class attr'
print(cn.attr)
```
```python
result:
new class attr
new class attr
```

### 实例属性

实例属性是类的实例独有的属性，实例属性只能通过实例名来访问，实例属性的值只能通过实例名来修改。

```python
# 实例属性
class ClassName():
    def __init__(self):
        self.attr = 'instance attr'

    def method(self, attr):
        self.attr = attr
        print(self.attr)
```

```python
# 实例属性的访问
cn = ClassName()
print(cn.attr)
```
```python
result:
instance attr
```

```python
# 实例属性的修改
cn.attr = 'new instance attr'
print(cn.attr)
cn.method('new instance attr')
```
```python
result:
new instance attr
new instance attr
```

如果你认为所有实例的某个attribute都应该是一样的，那么你应该使用类属性。\
如果你认为每个实例的某个attribute都应该是不同的，那么你应该使用实例属性。


## 类的继承

类的继承是类的一种特性，类的继承使用关键字class，后面紧跟类名，类名后面紧跟圆括号，圆括号中是父类的类名，如果没有父类，可以省略圆括号。类的继承后面是冒号，冒号后面是类的主体，类的主体中可以定义属性和方法。

```python
# 类的继承
class Father():

    character = 'irascible'     # 父亲性格暴躁

    def __init__(self):
        self.iq = 100

    def printf(self):
        print('i am a typist')  # 父亲是个打字员


class Son(Father):

    def __init__(self):
        self.iq = 50

    def fire(self):
        print('i am a soldier')  # 儿子是个士兵
```

```python
# 类的实例化
f = Father()
s = Son()
```

```python
# 类的属性的访问
print(f.character)
print(s.character)  # 子类继承父类的属性
```

```python
result:
irascible
irascible       # 儿子也性格暴躁
```

```python
# 类的方法的调用
f.printf()
s.printf()      # 子类继承父类的方法，即使在子类中没有定义
```

```python
result:
i am a typist
i am a typist   # 儿子不仅是个士兵，也可以是个打字员
```

```python
# 类的属性的修改
Father.character = 'gentle'     # 修改父类的属性
print(f.character)
print(s.character)
```
```python
result:
gentle
gentle      # 儿子也变温柔了
# 注意是在实例化之后修改的，说明类的属性是类的所有实例共有的属性
```

```python
# 类的方法的修改
Father.printf = lambda self: print('i am a teacher')  # 修改父类的方法
f.printf()
s.printf()
```
```python
result:
i am a teacher
i am a teacher     # 儿子也变成了老师

# 注意是在实例化之后修改的，说明类的方法是类的所有实例共有的方法
```

```python
# 类的属性的增加
Father.new_attr = 'new attr'    # 增加父类的属性
print(f.new_attr)
print(s.new_attr)
```
```python
result:
new attr
new attr    # 儿子也有了新属性
# 注意是在实例化之后增加的，说明类的属性是类的所有实例共有的属性
```

```python
# 类的方法的增加
Father.new_method = lambda self: print('new method')  # 增加父类的方法
f.new_method()
s.new_method()
```
```python
result:
new method
new method  # 儿子也有了新方法
# 注意是在实例化之后增加的，说明类的方法是类的所有实例共有的方法
```

```python
# 类的属性的删除
del Father.new_attr     # 删除父类的属性
print(f.new_attr)
print(s.new_attr)
```
```python
result:
AttributeError: 'Father' object has no attribute 'new_attr'
AttributeError: 'Son' object has no attribute 'new_attr'
# 儿子也没有了属性
```

```python
# 类的方法的删除
del Father.new_method   # 删除父类的方法
f.new_method()
s.new_method()
```
```python
result:
AttributeError: 'Father' object has no attribute 'new_method'
AttributeError: 'Son' object has no attribute 'new_method'
# 儿子也没有了方法
```


## 类的多继承

类的多继承是类的一种特性，类的多继承使用关键字class，后面紧跟类名，类名后面紧跟圆括号，圆括号中是父类的类名，如果没有父类，可以省略圆括号，如果有多个父类，可以用逗号隔开。类的多继承后面是冒号，冒号后面是类的主体，类的主体中可以定义属性和方法。

```python
# 类的多继承
class Father():

    character = 'irascible'     # 父亲性格暴躁

    def __init__(self):
        self.iq = 100

    def printf(self):
        print('i am a typist')  # 父亲是个打字员


class Mother():
    
    character = 'gentle'        # 母亲性格温柔

    def __init__(self):
        self.iq = 120

    def printf(self):
        print('i am a singer')   # 母亲是个歌手


class Son(Father, Mother):
    
    def __init__(self):
        self.iq = 50

    def fire(self):
        print('i am a soldier')  # 儿子是个士兵
```
    
```python
# 类的实例化
f = Father()
m = Mother()
s = Son()
```

```python
# 类的属性的访问
print(f.character)
print(m.character)
print(s.character)  # 子类继承父类的属性
```

```python
result:

irascible
gentle
irascible
```

```python
# 类的方法的调用
f.printf()
m.printf()
s.printf()      # 子类继承父类的方法，即使在子类中没有定义
```

```python
result:

i am a typist
i am a singer
i am a typist   # 儿子不仅是个士兵，也可以是个打字员
```

可以发现，当类的多继承时，如果多个父类中有相同的属性或方法，子类会继承第一个父类的属性或方法。


## 类的私有属性和私有方法

类的私有属性和私有方法是类的一种特性，类的私有属性和私有方法使用双下划线开头，双下划线开头的属性和方法只能在类的内部访问，类的外部无法访问。

```python
# 类的私有属性和私有方法
class ClassName():
    __attr = 'private attr'
    def __method(self):
        print('private method')
```

```python
# 类的实例化
cn = ClassName()
```

```python
# 类的私有属性的访问
print(cn.__attr)
```
```python
result:

AttributeError: 'ClassName' object has no attribute '__attr'
```

```python
# 类的私有方法的调用
cn.__method()
```
```python
result:

AttributeError: 'ClassName' object has no attribute '__method'
```

## int、str、list等基本数据类型中的类

在Python中，int、str、list等基本数据类型也是类，它们都是object的子类，它们都有自己的属性和方法。

上文中提到的"str".split()，和本文中的调用Method的方法是一样的，"str"就是str类的一个实例，split()就是str类的一个方法。




