# Int Method

通过`print(dir(int))`可以查看int的所有方法

int的内置方法可以方便我们对整数进行操作

### conjugate()

`conjugate()`方法用于返回该复数的共轭复数

```python
complex_ = 1 + 2j
complex_.conjugate()   # (1-2j)
```

- param: None
- return: complex

### denominator()

`denominator()`方法用于返回该有理数的分母

```python
from fractions import Fraction

x = Fraction(5, 2)
y = Fraction(3, 4)

print(x.denominator)  # 输出 2
print(y.denominator)  # 输出 4
```

- param: None
- return: int

### numerator()

`numerator()`方法用于返回该有理数的分子

```python
fraction_ = Fraction(1, 2)
fraction_.numerator()   # 1
```

- param: None
- return: int

### imag()

`imag()`方法用于返回该复数的虚部

```python
complex_ = 1 + 2j
complex_.imag()   # 2.0
```

- param: None
- return: float

### real()

`real()`方法用于返回该复数的实部

```python
complex_ = 1 + 2j
complex_.real()   # 1.0
```

- param: None
- return: float

### bit_length()

`bit_length()`方法用于返回该整数的二进制长度

```python
int_ = 10
int_.bit_length()   # 4
```

- param: None
- return: int

### to_bytes()

`to_bytes()`方法用于将整数转换为字节类型

```python
int_ = 10
int_.to_bytes(2, byteorder='big')   # b'\x00\n'
int__ = 20
int__.to_bytes(2, byteorder='little')   # b'\x14\x00'
```

- param: length: 字节长度;
- param: byteorder: 字节顺序
- return: bytes

### from_bytes()

`from_bytes()`方法用于将字节类型转换为整数

```python
bytes_ = b'\x00\n'
int.from_bytes(bytes_, byteorder='big')   # 10
bytes__ = b'\x14\x00'
int.from_bytes(bytes__, byteorder='little')   # 20
```

- param: bytes: 字节;
- param: byteorder: 字节顺序
- return: int





