# Float Method

通过`print(dir(float))`可以查看float的所有方法

float的内置方法可以方便我们对浮点数进行操作

### as_integer_ratio()

`as_integer_ratio()`方法用于将浮点数转化为分数

```python
float_ = 0.5
float_.as_integer_ratio()   # (1, 2)
```

- param: None
- return: tuple

### is_integer()

`is_integer()`方法用于判断浮点数是否为整数

```python
float_ = 0.5
float_.is_integer()   # False
```

- param: None
- return: bool

### hex()

`hex()`方法用于将浮点数转化为十六进制数

```python
float_ = 0.5
float_.hex()   # '0x1.0000000000000p-1'
```

- param: None
- return: str

### fromhex()

`fromhex()`方法用于将十六进制数转化为浮点数

```python
float_ = 0.5
float_.fromhex('0x1.0000000000000p-1')   # 0.5
```

- param: None
- return: float

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
from fractions import Fraction

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

