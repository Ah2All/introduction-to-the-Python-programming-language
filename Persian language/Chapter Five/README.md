## 🔹موضوعاتی که در این فصل بحث می کنیم:

- [دستورات شرطی (if, else, elif)](#مفهوم-دستورات-شرطی)
- [حلقه ها در پایتون (for, while)](#مفهوم-حلقه-ها-در-پایتون)
- [تابع ها در پایتون ](#concept-of-functions)

***

## 💎مفهوم دستورات شرطی
> عبارات شرطی در پایتون به شما امکان می دهد کدی را مشخص کنید که باید طبق شرایط خاصی اجرا شود. یک دستور شرطی ممکن است یک شرط واحد یا ترکیبی از چند شرط باشد.

### ⭕️ پایتون از شرایط منطقی معمول ریاضیات پشتیبانی می کند:

- برابر است با: a == b
- برابر نیست: a != b
- کمتر از: a < ب
- کمتر یا مساوی با: a <= b
- بزرگتر از: a > b
- بزرگتر یا مساوی با: a >= b
- این شرایط را می توان به روش های مختلفی مورد استفاده قرار داد، معمولاً در «عبارات if» و حلقه ها.

### 💢 استفاده از دستور if :
> برای استفاده از دستور if از کلمه کلیدی if استفاده می‌کنیم 

Example:
```python:
a = 33
b = 200
if b > a:
  print("b is greater than a")
```
Output :
```python:
b is greater than a
```

</br> 


### 💢 دستور Elif :
> کلمه کلیدی elif روشی است که پایتون می گوید: «اگر شرایط قبلی درست نبود، این شرط را امتحان کنید».

Example:
```python:
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
Output :
```python:
a and b are equal
```

</br> 

### 💢 دستور Else :
> کلمه کلیدی else هر چیزی را که تحت شرایط قبلی قرار نگرفته است را می گیرد.

Example:
```python:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
Output :
```python:
a is greater than b
```

***

## 💎مفهوم حلقه ها در پایتون
> حلقه ها در پایتون یکی از ابزارهای اساسی و قدرتمندی هستند که برای تکرار بر روی یک بلوک کد به طور مکرر بر اساس شرایط خاص یا دنباله ای از داده ها استفاده می شود. دو نوع حلقه در پایتون وجود دارد

### 💢 حلقه For :
> حلقه for زمانی استفاده می شود که بخواهیم روی یک دنباله (لیست، تاپل، رشته یا هر شیء قابل تکرار دیگری) تکرار کنیم و بلوک عبارات یا کد را برای هر عنصر دنباله اجرا کنیم. حلقه تا رسیدن به آخرین عنصر در دنباله ادامه می یابد.

با حلقه for می‌توانیم مجموعه‌ای از دستورات را، یک بار برای هر آیتم در یک لیست، تاپل، مجموعه و غیره اجرا کنیم.

Example:
```python:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
Output :
```python:
apple
banana
cherry
```

#### 🔶 دستور break
> با دستور break می‌توانیم حلقه را قبل از اینکه تمام آیتم‌ها را حلقه کند متوقف کنیم:

Example:
```python:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```
Output :
```python:
apple
banana
```

#### 🔶 تابع range().
> برای حلقه زدن مجموعه ای از کدها به تعداد مشخص، می توانیم از تابع range() استفاده کنیم.
تابع range() دنباله‌ای از اعداد را برمی‌گرداند که به طور پیش‌فرض از 0 شروع می‌شود و به صورت پیش‌فرض 1 افزایش می‌یابد و به یک عدد مشخص ختم می‌شود.
Example:

```python:
for x in range(6):
  print(x)
```
Output :
```python:
0
1
2
3
4
5
```

#### 🔶 ه else در For Loop
> کلمه کلیدی else در یک حلقه for، بلوکی از کد را مشخص می کند که باید پس از اتمام حلقه اجرا شود:

Example:
```python:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```
Output :
```python:
0
1
2
3
4
5
Finally finished!
```

### 💢 حلقه while :
> حلقه while زمانی استفاده می شود که بخواهیم یک دستور را در حالی که شرط داده شده درست است تکرار کنیم. حلقه تا زمانی که شرط نادرست شود ادامه می یابد.


Example:
```python:
i = 1
while i < 6:
  print(i)
  i += 1
```
Output :
```python:
1
2
3
4
5
```

#### 🔶 دستور break 
> با دستور break می توانیم حلقه را متوقف کنیم حتی اگر شرط while درست باشد:

Example:
```python:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```
Output :
```python:
1
2
3
```


#### 🔶 ه Else در while Loop
> با دستور else می‌توانیم یک بلوک کد را یکبار اجرا کنیم، زمانی که شرط دیگر درست نیست:

Example:
```python:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```
Output :
```python:
1
2
3
4
5
i is no longer less than 6
```

***

## 💎مفهوم توابع
> یک تابع یک بلوک از کد است که فقط زمانی اجرا می شود که فراخوانی شود. شما می توانید داده ها را که به عنوان پارامتر شناخته می شوند، به یک تابع منتقل کنید. یک تابع می تواند در نتیجه داده ها را برگرداند.

Example:
```python:
def my_function():
  print("Hello from a function")
```
#### 🔶 فراخواندن یک تابع 
Example:
```python:
def my_function():
  print("Hello from a function")

my_function()
```
Output :
```python:
Hello from a function
```

### 🖊 the writer : Alireza Allahyarian - [Website](http://microhex.info/) - [linkedin](https://www.linkedin.com/in/alireza-allahyarian-658658258/)- [GitHub](https://github.com/graymicro) - [Tlegeram](https://t.me/graycubeteam) 

#### **[♦️license by gray cube team♦️](graycubeteam.github.io)**
