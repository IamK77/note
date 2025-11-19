# Decorator

## Basic Decorator

### func as a parameter

在python中，函数也是一个对象，可以赋值给一个变量，也可以作为参数传递给另一个函数

```python
def double(x):
    return x * 2
# 等价于 double = lambda x: x * 2
# double和变量名一样，没有什么不同
```

```python
def double(x):
    return x * 2

def calc_number(func, x):
     print(func(x))

calc_number(double, 5)
```

result:

```python
10
```

### func as a return value

同样的，函数也可以作为返回值返回

```python
def get_multiple_func(n):

    def multiple(x):
        return x * n

    return multiple

get_double = get_multiple_func(2)
'''
get_multiple_func(2)返回multiple
get_double = get_multiple_func(2) = multiple(2)
此时的multiple定义为

def multiple(x):
    return x * 2

get_double 和 multiple 等价
'''
print(get_double(5))
'''
等价于
print(multiple(5))
'''
```

result:

```python
10
```

### decorator

在上面的例子中，我们定义了一个函数，用来计算一个数的2倍，然后我们又定义了一个函数，用来计算一个数的3倍，这样的函数还可以继续定义下去，但是这样的代码会有很多重复的部分，我们可以使用装饰器来简化这样的代码

```python
def dec(f):
    return 1

@dec
def double(x):
    return x * 2

print(double(5))

'''
等价于 double = dec(double)
'''
```

result:

```python
1
```

接下来举一个复杂一点的例子，我们定义一个装饰器，用来计算函数的运行时间

```python
import time

def timer(func):

    def wrapper(x):
        start_time = time.time()
        ret = func(x)
        print(f"Time used: {time.time() - start_time}")
        return ret

    return wrapper

@timer
def my_func(x):
    time.sleep(x)

@timer
def double(x):
    return x * 2

my_func(2)
'''
my_func = timer(my_func)(2) = wrapper(2)
此时的wrapper定义为
def wrapper(x):
    start_time = time.time()
    ret = my_func(x)
    print(f"Time used: {time.time() - start_time}")
    return ret

my_func 和 wrapper 等价
最终执行的代码为
def wrapper():
    start_time = time.time()
    ret = time.sleep(2)
    print(f"Time used: {time.time() - start_time}")
'''
print(double(5))
'''
double = timer(double)(5) = wrapper(5)
此时的wrapper定义为
def wrapper(x):
    start_time = time.time()
    ret = double(x)
    print(f"Time used: {time.time() - start_time}")
    return ret
最终执行的代码为
def wrapper():
    start_time = time.time()
    ret = 5 * 2
    print(f"Time used: {time.time() - start_time}")
    return ret
print(ret)
'''

```

result:

```python
Time used: 2.000000238418579
Time used: 0.0
10
```

### decorator more parameters

上面的例子中，我们定义了一个装饰器，但是这个装饰器只能用来装饰没有参数的函数，如果我们想要装饰有参数的函数，我们需要对装饰器进行改造

```python
import time

def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print(f"Time used: {time.time() - start_time}")
        return ret

    return wrapper

@timer
def my_func(x):
    time.sleep(x)

@timer
def add(x, y):
    return x + y

print(add(1, 2))
'''
add = timer(add)(1, 2) = wrapper(1, 2)

def wrapper(*args, **kwargs):
    start_time = time.time()
    ret = add(1, 2)
    print(f"Time used: {time.time() - start_time}")
    return ret

print(ret)
'''
```

result:

```python
Time used: 0.0
3
```

### decorator with parameters

现在我们来写一个带参数的装饰器，这个装饰器可以接受一个参数，用来指定函数的运行次数

```python
import time

def timer(iteration):

    def inner(func):

        def wrapper(*args, **kwargs):
            start_time = time.time()
            for _ in range(iteration):
                ret = func(*args, **kwargs)
            print(f"Time used: {time.time() - start_time}")
            return ret

        return wrapper

    return inner

@timer(3)
def double(x):
    return x * 2

print(double(5))
'''
double = timer(3)(double)(5) = inner(double)(5) = wrapper(5)

def wrapper(*args, **kwargs):
    start_time = time.time()
    for _ in range(3):
        ret = double(5)
    print(f"Time used: {time.time() - start_time}")
    return ret

print(ret)
'''
```

result:

```python
Time used: 0.0
10
```
