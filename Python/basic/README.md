# Preface

[目录](/README.md)

## About Python

Python是一种计算机程序设计语言。它是一种oop(面向对象)的动态类型语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。

与其他一些语言不同的是，Python是一种解释型语言，解释型语言在执行时不需要编译为机器码或者字节码，可以直接由解释器读取源代码（类似于我们人类读取自然语言一样），并执行程序。

而其他一些语言，如C、C++、Java等，都是编译型语言，编译型语言在执行前需要一个专门的编译过程，将源代码编译为一个binary(二进制)文件，然后再执行这个binary文件。

Python的编程范式支持多种，包括面向对象编程、命令式编程、函数式编程、面向切面编程等。Python拥有一个庞大的标准库，提供了各种各样的工具，涵盖了网络、文件、GUI、数据库、图形、XML等，还有大量的第三方库。

Python的语法简洁优雅，由于其面向对象的特性，Python的语法更符合人类直觉。

这使得Python在开发速度上有很大的优势，但是在执行速度上却不如编译型语言。

## About Python Standard and Python Interpreter

了解C++的人可能知道，随C++的发展，C++的标准也在不断更新，有C++11，C++14，C++17等等多个标准。而C++的编译器是根据C++标准来实现的，不同的编译器如gcc、clang、msvc等，对C++标准的支持程度也不同。C++的标准规定了C++的语法、语义、标准库等等，编译器则是根据标准对源代码进行编译，生成可执行文件。

Python的标准和Python的解释器也是类似的，Python的标准规定了Python的语法、语义、标准库等等，Python的解释器则是根据标准对源代码进行解释，执行程序。但是Python的标准是根据cPython的实现来制定的，cPython是Python的官方解释器，Python的标准库也是根据cPython的实现来制定的。除此之外，还有其他的Python解释器，如Jython、IronPython、PyPy等，这些解释器也是根据cPython的实现来实现的，但是它们的标准库可能不同于cPython的标准库。

## About Python Version

Python的标准版本有Python2和Python3，Python2和Python3的语法、语义、标准库等等都有一些不同，Python3是Python的未来，Python2已经不再更新，Python3的标准库也更加完善。

目前Python3.x的常用子版本有Python3.6、Python3.7、Python3.8，Python3.9，Python3.10，Python3.11

Python3.11仍处于beta阶段，Python3.10是目前最新的稳定版本，推荐使用的Python版本是3.10、3.9。

## About Anaconda

Anaconda是一个Python发行版，包含了Python解释器、Python标准库、conda包管理器、conda环境管理器、conda虚拟环境管理器、conda包及其依赖项等等。

为什么使用Anaconda？

- 当开发项目时，需要测试在不同的Python版本下的运行情况，使用Anaconda可以方便地切换Python版本，方便开发者进行测试。
- 当使用第三方库时，可能会遇到版本冲突的问题，即库1依赖库2的某版本使用，而库3依赖库2的另一版本使用，当程序运行时，可能会导致运行错误，使用Anaconda可以方便地创建虚拟环境，避免版本冲突。
- 使用Anaconda可以避免三方库过于臃肿

## About Python IDE

IDE是集成开发环境的缩写，IDE是一种软件，可以集成编辑器、编译器、调试器、自动补全、自动格式化、自动重构、自动部署等等功能，提高开发效率。

常用的Python IDE有PyCharm、VSCode、Spyder、Jupyter Notebook、Jupyter Lab等等。

## About Python Package

Python Package是Python的包，包含了Python的源代码、Python的标准库、Python的第三方库、Python的解释器等等。

Python Package的安装方式有多种，包括pip、conda、源码编译等等。

安装第三方库：

```bash
pip install package_name
```

使用国内镜像源提高下载速度：

```bash
pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple
```

卸载第三方库：

```bash
pip uninstall package_name
```

查看已安装的第三方库：

```bash
pip list
```

查看已安装的第三方库的版本：

```bash
pip list -v
```

查看已安装的第三方库的详细信息：

```bash
pip show package_name
```

## Error

当Python解释器在执行程序时，如果遇到错误，会抛出异常，coding过程中，我们经常会遇到各种各样的错误，如语法错误、语义错误、运行时错误等等。当遇到异常时，Python解释器会打印出异常信息，异常信息包含了异常类型、异常信息、异常发生的位置等等。\
此时锁定异常发生的位置，阅读代码，查找错误，才是解决问题的关键。如果判断不出错误的原因，可以将代码逐步注释，逐步调试，找到错误的原因。或者复制异常信息，bing一下

\
\
\
\
传送门: [basic](Grammar.md)
