# Module

Module在Python中是一个非常重要的概念，它是Python组织代码的基本方式，也是Python代码**重用**的基本方式。

## 模块的定义

模块是一个包含所有定义的函数和变量的文件，其后缀名是`.py`。模块可以被别的程序引入，以使用该模块中的函数等功能。

## 模块的导入

假设当前文件树如下

```bash

D:py.
├── main.py
├── module1.py
└── module
    ├── __init__.py
    └── module2.py
```

当前文件为`main.py`，`module1.py`和`module2.py`都是模块文件，`module`是一个包，`__init__.py`是一个空文件，用于告诉Python这个目录是一个Python的包。

Python的`import`语句用于导入模块，语法如下：

```python
import module_name
```

或者

```python
from module_name import function_name
```

或者

```python
from module_name import *
```

### 模块的搜索路径

当解释器遇到`import`语句，如果模块在当前的搜索路径就会被导入。

搜索路径是一个解释器会先进行搜索的所有目录的列表。如下：

```python
import sys
print(sys.path)
```

### 模块的内置属性

每个模块都有一些内置的属性，可以通过`dir()`函数来查看，如下：

```python
import sys
print(dir(sys))
```

### 模块的`__name__`属性

一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用`__name__`属性来使该程序块仅在该模块自身运行时执行。

```python
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
```

该属性较为重要，如不理解，请先按固定格式在每一个模块中添加该属性，然后再进行学习。\
它的作用大多是用于测试模块。

例如如上的文件树，我们在module1.py中添加如下代码
```python
# module1.py
def func1():
    print('func1() in module1.py')

def func2():
    print('func2() in module1.py')

func1()

if __name__ == '__main__':
    func2()
```
接下来在main.py中添加如下代码
```python
# main.py
import module1
```

运行main.py，输出如下
```bash
func1() in module1.py
```

在`import module1`时，`module1.py`中的`func1()`被执行，但因为`__name__`属性的值是`module1`，而不是`__main__`，因此`func2()`没有被执行。


### alias 别名

我们可以给模块起一个别名，例如如下代码

```python
import module1 as m1
```

### from...import 语句

Python的`from`语句让我们从模块中导入一个指定的部分到当前命名空间中，语法如下：

```python
from module_name import function_name
```

可以让我们只导入一个模块中的某个部分


## 路径导入

假设当前文件树如下

```bash
d:/root.
├── src
│   ├── main.py
│   ├── module1.py
│   └── folder
│       ├── __init__.py
│       ├── module2.py
│       └── utils
│           ├── __init__.py
│           └── module3.py
└── module
    ├── __init__.py
    └── module4.py
```



### 绝对路径导入

绝对路径导入是指从根目录开始导入模块，例如如下代码

```python
# main.py
import module.module4
import src.module1
import src.folder.module2
import src.folder.utils.module3
```

如果要导入的模块位于根目录外，例如`d:/other/module.py`，则需要将根目录添加到搜索路径中，例如如下代码

```python
# main.py
import sys
sys.path.append('d:/other')
import module
```

### 相对路径导入

相对路径导入是指从当前目录开始导入模块，例如如下代码

```python
# main.py
from . import module1
from .folder import module2
from .folder.utils import module3
from .. import module4
```

单独一个`.`表示当前目录，`..`表示上一级目录，以此类推。

如果要导入的模块位于当前目录外，例如`d:/other/module.py`，则需要将根目录添加到搜索路径中，例如如下代码

```python
# main.py
import sys
sys.path.append('d:/other')
from module import module
```
