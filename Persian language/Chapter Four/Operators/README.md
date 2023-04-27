## 🔹موضوعاتی که در این فصل مورد بحث قرار می‌دهیم:

- [عملگرهای حسابی](#-عملگرهای-حسابی)
- [عملگرهای مقایسه](#-عملگرهای-مقایسه)
- [عملگرهای واگذاری](#-عملگرهای-واگذاری)
- [عملگرهای منطقی](#-عملگرهای-منطقی)
- [عملگرهای عضویت](#-عملگرهای-عضویت)
- [عملگرهای هویت](#-عملگرهای-هویت)

***

## 💎مفهوم اپراتورها
> عملگرها برای انجام عملیات روی متغیرها و مقادیر استفاده می شوند.

</br>

### 💢 عملگرهای حسابی
> عملگرهای حسابی با مقادیر عددی برای انجام عملیات ریاضی رایج استفاده می شوند

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

### 💢 عملگرهای مقایسه
> عملگرهای مقایسه برای مقایسه دو مقدار استفاده می شوند
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

### 💢 عملگرهای واگذاری
> عملگرهای انتساب برای تخصیص مقادیر به متغیرها استفاده می شوند

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

### 💢 عملگرهای منطقی
> عملگرهای منطقی برای ترکیب عبارات شرطی استفاده می شوند

```python:
x = 10
y = 5

print(x > 5 and y < 10) # True
print(x > 5 or y > 10) # True
print(not(x == y)) # True
```

*** 

### 💢 عملگرهای عضویت
> عملگرهای عضویت برای آزمایش اینکه آیا دنباله ای در یک شی ارائه شده است استفاده می شود

```python:
x = ["apple", "banana"]
print("banana" in x) # True
print("cherry" not in x) # True
```

*** 

### 💢 عملگرهای هویت
> عملگرهای هویت برای مقایسه اشیاء استفاده می‌شوند، نه اگر برابر باشند، بلکه اگر در واقع یک شی با مکان حافظه یکسان باشند.

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
