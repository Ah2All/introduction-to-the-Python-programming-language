## 🔹The topics we discuss in this chapter:

- [عملگرهای حسابی](#-arithmetic-operators)
- [عملگرهای مقایسه](#-comparison-operators)
- [عملگرهای واگذاری](#-assignment-operators)
- [عملگرهای منطقی](#-logical-operators)
- [عملگرهای عضویت](#-membership-operators)
- [عملگرهای هویت](#-identity-operators)

***

## 💎مفهوم اپراتورها
> عملگرها برای انجام عملیات روی متغیرها و مقادیر استفاده می شوند.

</br>

### 💢 Arithmetic operators
> Arithmetic operators are used with numeric values to perform common mathematical operations

```python:
x = 10
y = 5

print(x + y) # 15
print(x - y) # 5
print(x * y) # 50
print(x / y) # 2.0
print(x % y) # 0
print(x ** y) # 100000
print(x // y) # 2
```

*** 

### 💢 comparison operators
> Comparison operators are used to compare two values

```python:
x = 10
y = 5

print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False
```

*** 

### 💢 Assignment operators
> Assignment operators are used to assign values to variables

```python:
x = 5
x += 3
print(x) # output: 8

x = 5
x -= 3
print(x) # output: 2

x = 5
x *= 3
print(x) # output: 15

x = 6
x /= 3
print(x) # output: 2.0

x = 7
x %= 3
print(x) # output: 1

x = 7
x //= 3
print(x) # output: 2

x = 2
x **= 3
print(x) # output: 8
```

*** 

### 💢 logical operators
> Logical operators are used to combine conditional statements

```python:
x = 10
y = 5

print(x > 5 and y < 10) # True
print(x > 5 or y > 10) # True
print(not(x == y)) # True
```

*** 

### 💢 membership operators
> Membership operators are used to test if a sequence is presented in an object

```python:
x = ["apple", "banana"]
print("banana" in x) # True
print("cherry" not in x) # True
```

*** 

### 💢 Identity operators
> Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

```python:
# is a comparison with the operator
a = [1, 2, 3]
b = a
print(b is a)   # Output: True

c = [1, 2, 3]
print(c is a)   # Output: False

# compares the absence with the not operator
d = "Hello"
e = "World"
print(d is not e)   # Output: True

f = "Hello"
print(d is not f)   # Output: False
```

### 🖊 the writer : Alireza Allahyarian - [Website](http://microhex.info/) - [linkedin](https://www.linkedin.com/in/alireza-allahyarian-658658258/)- [GitHub](https://github.com/graymicro) - [Tlegeram](https://t.me/graycubeteam) 

#### **[♦️license by gray cube team♦️](graycubeteam.github.io)**
