# Str Method

通过python内方法对数据进行基础操作

### 高频使用的方法有

- `len`
- `replace`
- `split`
- `join`
- `strip`
- `format`

其他只需知道有这个方法即可，用到的时候再去查阅文档


### len

len() 方法返回对象（字符、列表、元组等）长度或项目个数。

```python
var_str = "www.google.com"
len(var_str)    # 14
var_list = [1, 2, 3, 4, 5]
len(var_list)   # 5
var_tuple = (1, 2, 3, 4, 5)
len(var_tuple)  # 5
```

- param -- 对象。
- return -- 返回对象长度。

### replace

replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

```python
var_str = "www.google.com"
var_str.replace("o", "O")       # 'www.gOOgle.cOm'
var_str.replace("o", "O", 1)    # 'www.gOogle.com'
```

- param1 -- 指定需要被替换的旧字符串
- param2 -- 新字符串，用于替换old子字符串
- param3 -- 可选字符串, 替换不超过 max 次
- return -- 返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串。


### split

split() 方法通过指定分隔符对字符串进行分割并返回一个列表，默认分隔符为所有空字符，包括空格、换行(\n)、制表符(\t)等。

```python
var_str = "www.google.com"
var_str.split(".")      # ['www', 'google', 'com']
var_str.split(".", 1)   # ['www', 'google.com']
var_str.split("o")      # ['www.g', '', 'gle.c', 'm']

var_str = "my name is tom"
var_str.split()         # ['my', 'name', 'is', 'tom']

var_str = "i\nwill\ndeal\nwith\nit"
var_str.split()         # ['i', 'will', 'deal', 'with', 'it']
```

- param1 -- 分隔符，默认为所有空字符，包括空格、换行(\n)、制表符(\t)等
- param2 -- 分割次数，默认为 -1，即分隔所有

### join

join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

```python
var_list = ['www', 'google', 'com']
".".join(var_list)      # 'www.google.com'
var_list = ['i', 'will', 'deal', 'with', 'it']
" ".join(var_list)      # 'i will deal with it'
```

- param -- 要连接的元素序列
- return -- 返回通过指定字符连接序列中元素后生成的新字符串。

这里的使用方法有些不同，在后面的class中会详细介绍

在这里只需知道使用方法

### strip

strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

```python
var_str = "   www.google.com   "
var_str.strip()         # 'www.google.com'
var_str = "www.google.com"
var_str.strip("w")      # '.google.com'
var_str.strip("moc")    # 'www.google.'
```

- param -- 移除字符串头尾指定的字符序列
- return -- 返回移除字符串头尾指定的字符生成的新字符串。

### find

find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

```python
var_str = "www.google.com"
var_str.find("o")       # 5
var_str.find("o", 4)    # 5
var_str.find("o", 13, 14)  # -1
"i am a handsome boy".find("handsome")  # 7
```

- param1 -- 指定检索的字符串
- param2 -- 指定检索的开始位置，默认为 0，从0开始算起，如果是负数，则从字符串的末尾开始算起。
- param3 -- 指定检索的结束位置，默认为字符串的长度。
- return -- 如果包含子字符串返回开始的索引值，否则返回-1。人话就是第一次出现的位置，如果没有就返回-1

### count

count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

```python
var_str = "www.google.com"
var_str.count("o")      # 3
var_str.count("o", 4)   # 3
var_str.count("o", 13, 14)  # 0
```

- param1 -- 指定检索的字符串
- param2 -- 指定检索的开始位置，默认为 0，从0开始算起，如果是负数，则从字符串的末尾开始算起。
- param3 -- 指定检索的结束位置，默认为字符串的长度。
- return -- 返回子字符串出现的次数

### startswith

startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

```python
var_str = "www.google.com"
var_str.startswith("www")       # True
var_str.startswith("www", 0)    # True
var_str.startswith("www", 1)    # False
var_str.startswith("www", 0, 3) # True
var_str.startswith("www", 0, 4) # False
```

- param1 -- 指定检索的字符串
- param2 -- 指定检索的开始位置，默认为 0，从0开始算起，如果是负数，则从字符串的末尾开始算起。
- param3 -- 指定检索的结束位置，默认为字符串的长度。
- return -- 如果是则返回 True，否则返回 False

### endswith

endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。

```python
var_str = "www.google.com"
var_str.endswith("com")       # True
var_str.endswith("com", 0)    # True
var_str.endswith("com", 1)    # False
var_str.endswith("com", 0, 3) # False
var_str.endswith("com", 0, 4) # True
```

- param1 -- 指定检索的字符串
- param2 -- 指定检索的开始位置，默认为 0，从0开始算起，如果是负数，则从字符串的末尾开始算起。
- param3 -- 指定检索的结束位置，默认为字符串的长度。
- return -- 如果是则返回 True，否则返回 False

### isalpha

isalpha() 方法检测字符串是否只由字母组成。

```python
var_str = "www.google.com"
var_str.isalpha()       # False
var_str = "wwwgooglecom"
var_str.isalpha()       # True
```

- return -- 如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

### isdigit

isdigit() 方法检测字符串是否只由数字组成。

```python
var_str = "www.google.com"
var_str.isdigit()       # False
var_str = "1234567890"
var_str.isdigit()       # True
```

- return -- 如果字符串只包含数字则返回 True 否则返回 False.

### isalnum

isalnum() 方法检测字符串是否由字母和数字组成。

```python
var_str = "www.google.com"
var_str.isalnum()       # False
var_str = "wwwgooglecom"
var_str.isalnum()       # True
var_str = "1234567890"
var_str.isalnum()       # True
```

- return -- 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

### islower

islower() 方法检测字符串是否由小写字母组成。

```python
var_str = "www.google.com"
var_str.islower()       # True
var_str = "wwwgooglecom"
var_str.islower()       # True
var_str = "1234567890"
var_str.islower()       # False
```

- return -- 如果字符串中包含至少一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False

### isupper

isupper() 方法检测字符串是否由大写字母组成。

```python
var_str = "www.google.com"
var_str.isupper()       # False
var_str = "WWWGOOGLECOM"
var_str.isupper()       # True
var_str = "1234567890"
var_str.isupper()       # False
```

- return -- 如果字符串中包含至少一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False

### lower

lower() 方法转换字符串中所有大写字符为小写。

```python
var_str = "www.google.com"
var_str.lower()       # 'www.google.com'
var_str = "WWWGOOGLECOM"
var_str.lower()       # 'wwwgooglecom'
var_str = "1234567890"
var_str.lower()       # '1234567890'
```

- return -- 返回将字符串中所有大写字符转换为小写后生成的字符串。

### upper

upper() 方法将字符串中的小写字母转为大写字母。

```python
var_str = "www.google.com"
var_str.upper()       # 'WWW.GOOGLE.COM'
var_str = "WWWGOOGLECOM"
var_str.upper()       # 'WWWGOOGLECOM'
var_str = "1234567890"
var_str.upper()       # '1234567890'
```

- return -- 返回将字符串中所有大写字符转换为小写后生成的字符串。

### capitalize

capitalize() 方法将字符串的第一个字母变成大写,其他字母变小写。

```python
var_str = "www.google.com"
var_str.capitalize()       # 'Www.google.com'
var_str = "WWWGOOGLECOM"
var_str.capitalize()       # 'Wwwgooglecom'
var_str = "1234567890"
var_str.capitalize()       # '1234567890'
```

- return -- 返回将字符串中所有大写字符转换为小写后生成的字符串。

### title

title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。

```python
var_str = "www.google.com"
var_str.title()       # 'Www.Google.Com'
var_str = "WWWGOOGLECOM"
var_str.title()       # 'Wwwgooglecom'
var_str = "1234567890"
var_str.title()       # '1234567890'
```

- return -- 返回将字符串中所有大写字符转换为小写后生成的字符串。

### swapcase

swapcase() 方法用于对字符串的大小写字母进行转换。

```python
var_str = "www.google.com"
var_str.swapcase()       # 'WWW.GOOGLE.COM'
var_str = "WWWGOOGLECOM"
var_str.swapcase()       # 'wwwgooglecom'
var_str = "1234567890"
var_str.swapcase()       # '1234567890'
```

- return -- 返回将字符串中所有大写字符转换为小写后生成的字符串。

### ljust

ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

```python
var_str = "www.google.com"
var_str.ljust(20)       # 'www.google.com      '
var_str.ljust(20, "1")  # 'www.google.com111111'
var_str.ljust(10)       # 'www.google.com'
```

- param1 -- 指定填充字符串的长度。
- param2 -- 填充的字符，默认为空格。
- return -- 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。

### rjust

rjust() 方法返回一个原字符串右对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

```python
var_str = "www.google.com"
var_str.rjust(20)       # '      www.google.com'
var_str.rjust(20, "1")  # '111111www.google.com'
var_str.rjust(10)       # 'www.google.com'
```

- param1 -- 指定填充字符串的长度。
- param2 -- 填充的字符，默认为空格。
- return -- 返回一个原字符串右对齐,并使用空格填充至指定长度的新字符串。

### center

center() 方法返回一个原字符串居中,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

```python
var_str = "www.google.com"
var_str.center(20)       # '   www.google.com   '
var_str.center(20, "1")  # '111www.google.com111'
var_str.center(10)       # 'www.google.com'
```

- param1 -- 指定填充字符串的长度。
- param2 -- 填充的字符，默认为空格。
- return -- 返回一个原字符串居中,并使用空格填充至指定长度的新字符串。

### lstrip

lstrip() 方法用于截掉字符串左边的空格或指定字符。

```python
var_str = "   www.google.com   "
var_str.lstrip()         # 'www.google.com   '
var_str.lstrip("w")      # '.google.com   '
var_str.lstrip("moc")    # '   www.google.'
```

- param -- 指定截取的字符，默认为空格。
- return -- 返回截掉字符串左边的空格或指定字符后生成的新字符串。

### rstrip

rstrip() 方法用于截掉字符串右边的空格或指定字符。

```python
var_str = "   www.google.com   "
var_str.rstrip()         # '   www.google.com'
var_str.rstrip("w")      # '   www.google.com.'
var_str.rstrip("moc")    # '   www.google'
```

- param -- 指定截取的字符，默认为空格。
- return -- 返回截掉字符串右边的空格或指定字符后生成的新字符串。

### zfill

zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

```python
var_str = "www.google.com"
var_str.zfill(20)       # '000000www.google.com'
var_str.zfill(20, "1")  # '111111www.google.com'
var_str.zfill(10)       # 'www.google.com'
```

- param1 -- 指定字符串的长度。原字符串右对齐，前面填充0。
- param2 -- 填充的字符，默认为空格。
- return -- 返回指定长度的字符串，原字符串右对齐，前面填充0。

### format

format() 方法用于格式化字符串，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 % 。

```python
var_str = "www.google.com"
var_str.format()         # 'www.google.com'
var_str.format("1")      # 'www.google.com'
var_str.format("1", "2") # 'www.google.com'
var_str.format("1", "2", "3")    # 'www.google.com'
```

- param -- 指定截取的字符，默认为空格。
- return -- 返回截掉字符串左右两边的空格或指定字符后生成的新字符串。

在这里展示一下c语言中的格式化输出

```c
#include <stdio.h>

int main()
{
    int a = 10;
    float b = 3.1415926;
    char c = 'a';
    char str[20] = "hello world";
    printf("a = %d\n", a);
    printf("b = %f\n", b);
    printf("c = %c\n", c);
    printf("str = %s\n", str);
    return 0;
}
```

输出结果

```shell
a = 10
b = 3.141593
c = a
str = hello world
```

在python中，新近更新了f-string，可以直接在字符串中使用变量，而不需要使用format()方法

```python
a = 10
b = 3.1415926
c = 'a'
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
```

输出结果

```shell
a = 10
b = 3.1415926
c = a
```

即在字符串前加上f，然后在字符串中使用{}包裹变量即可

### encode

encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。

```python
var_str = "www.google.com"
var_str.encode()         # b'www.google.com'
var_str.encode("utf-8")  # b'www.google.com'
var_str.encode("gbk")    # b'www.google.com'
var_str.encode("gbk", "ignore") # b'www.google.com'
```

- param1 -- 指定编码的格式。
- param2 -- 错误处理方案，默认为 'strict'，意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
- return -- 返回编码后的字符串。

### decode

decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。

```python
var_str = "www.google.com"
var_str.encode()         # b'www.google.com'
var_str.encode("utf-8")  # b'www.google.com'
var_str.encode("gbk")    # b'www.google.com'
var_str.encode("gbk", "ignore") # b'www.google.com'
```

- param1 -- 指定编码的格式。
- param2 -- 错误处理方案，默认为 'strict'，意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
- return -- 返回编码后的字符串。











