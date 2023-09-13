# Special Method

也叫Magic Method，是一种特殊的方法，它的名字前后都有两个下划线，比如\_\_init\_\_()

## \_\_init\_\_()和\_\_new\_\_()

类的初始化方法，类的初始化方法在类的实例化时自动调用，类的初始化方法可以接收参数，参数可以用来初始化类的属性。

```python
# 类的初始化
class A():
    def __new__(cls):
        print('new')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('init')
        self.name = name
        self.age = age
```

\_\_new\_\_在实际应用中使用不多，此处不再赘述。当你知道何时1使用\_\_new\_\_时，你自然会知道它的作用。

\_\_init\_\_用于初始化类的属性，它的第一个参数是self，self代表类的实例，self后面的参数是类的参数，类的参数可以用来初始化类的属性。

```python
# 类的实例化
zhangsan = A('张三', 18)
# __new__会先于___init__被调用
# obj = __new__(A)
# __init__(obj, '张三', 18)

# result:
new
init
```

## \_\_del\_\_()

类的析构方法，类的析构方法在类的实例被销毁时自动调用，类的析构方法不接收参数。

```python
# 类的析构

class A():
    def __init__(self):
        print('init')

    def __del__(self):
        print('del_')

a = A()
del a

print('end')
```

```python
# result:
init
del_
end
```

C++中的写法:

```c++
class A {
public:
    A() {
        cout << "init" << endl;
    }
    ~A() {
        cout << "del_" << endl;
    }
};

int main() {
    A a;
    return 0;
}
```

```c++
// result:
init
del_
```

## \_\_str\_\_()和\_\_repr\_\_()

类的字符串表示方法，类的字符串表示方法在使用print()函数打印类的实例时自动调用，类的字符串表示方法不接收参数。

```python
# 类的字符串表示

class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name: %s, age: %d' % (self.name, self.age)

    def __repr__(self):
        return 'name: %s, age: %d' % (self.name, self.age)

a = A('张三', 18)
print(a)
```

```python
# result:
name: 张三, age: 18
```

\_\_str\_\_()和\_\_repr\_\_()的区别在于，\_\_str\_\_()在使用print()函数打印类的实例时自动调用，\_\_repr\_\_()在使用repr()函数打印类的实例时自动调用。

```python
# repr()函数

a = A('张三', 18)
print(repr(a))
```

```python
# result:
name: 张三, age: 18
```

通常来说，\_\_str\_\_()和\_\_repr\_\_()的返回值是一样的，但是\_\_str\_\_()的返回值更加友好更易理解，\_\_repr\_\_()的返回值更加准确。当两个同时存在时，使用print会优先调用\_\_str\_\_()，使用repr会优先调用\_\_repr\_\_()。
