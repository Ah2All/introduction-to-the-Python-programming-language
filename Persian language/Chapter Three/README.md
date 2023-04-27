## 🔹موضوعاتی که در این فصل بحث می کنیم:

- [مفهوم متغیر](#مفهوم-متغیر)

   - [نحوه تعریف متغیر در پایتون](#نحوه-تعریف-متغیر-در-پایتون)
   - [قوانین برای متغیرهای پایتون](-قوانین-برای-متغیرهای-پایتون)
   
- [انواع داده ها در پایتون](#-انواع-داده-پایتون)

   - (ا[string](#-رشته-ها-در-پایتون), [integers](#-اعداد-در-پایتون), [bool](#-بولین), [float](#-اعداد-در-پایتون)) 
   - مجموعه داده ها ([List](#-لیست-ها), [Tuple](#-تاپل), [Dictionaries](#-دیکشنری-ها), [set](#-مجموعه))
   
- [تبدیل انواع داده ها به یک دیگر](#تبدیل-انواع-داده-ها-به-یکدیگر)

</br>

## 💎مفهوم متغیر
> در پایتون، متغیر نامی است که به یک مقدار اشاره دارد. برای ذخیره و دستکاری داده ها استفاده می شود. هنگامی که متغیری را در پایتون ایجاد می کنید، باید نامی برای آن انتخاب کنید، به آن مقدار اختصاص دهید و نوع داده آن را اعلام کنید (اگرچه در بیشتر موارد، پایتون به طور خودکار نوع داده را بر اساس مقدار اختصاص داده شده تشخیص می دهد).

**⭕️ مانند ظرفی است که در آن چیزی می ریزیم و بعد از آن استفاده می کنیم**

</br>

#

### 🔻نحوه تعریف متغیر در پایتون🔻
برای تعریف متغیر در پایتون ابتدا نام متغیر را مشخص می کنیم و سپس با استفاده از علامت مساوی (=) مقدار مورد نظر را به متغیر اختصاص می دهیم. مثلا:

```python:
name = "John"
age = 30
height = 1.75
```

#
</br>

### ♨️ قوانین برای متغیرهای پایتون:
- نام متغیر باید با یک حرف یا کاراکتر زیرخط شروع شود
- نام متغیر نمی تواند با عدد شروع شود
- نام متغیر فقط می تواند شامل کاراکترهای عددی و زیرخط باشد (A-z، 0-9 و _ )
- نام متغیرها به حروف بزرگ و کوچک حساس هستند (سن، سن و AGE سه متغیر متفاوت هستند)
- نام متغیر نمی تواند هیچ یک از کلمات کلیدی پایتون باشد.

مثلا:
```python:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```
نام متغیرهای غیرقانونی:
```python:
2myvar = "John"
my-var = "John"
my var = "John"
```
#
### 💢 متغیرهای پایتون - چندین مقدار اختصاص دهید
#### 🔹متغیرهای چندگانه
پایتون به شما این امکان را می دهد که در یک خط به چندین متغیر مقادیر اختصاص دهید:
```python:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
#### 🔹یک مقدار به چند متغیر
و می توانید یک مقدار را به چندین متغیر در یک خط اختصاص دهید:
```python:
x = y = z = "Orange"
print(x)
print(y)
print(z)
```
### 💢خروجی متغییر
#### 🔹خروجی متغییر ها
تابع print() Python اغلب برای خروجی متغیرها استفاده می شود.
```python:
x = "Python is awesome"
print(x)
```
خروجی :
```python:
Python is awesome
```
در تابع print() شما چندین متغیر را که با کاما از هم جدا شده اند، خروجی می دهید:
```python:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```
خروجی :
```python:
Python is awesome
```
همچنین می توانید از عملگر + برای خروجی چندین متغیر استفاده کنید:
```python:
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
```
خروجی :
```python:
Python is awesome
```
**🛑 به کاراکتر Space بعد از "Python" و "is" توجه کنید، بدون آنها نتیجه "Pythonisawesome" خواهد بود.**

برای اعداد، کاراکتر + به عنوان یک عملگر ریاضی عمل می کند:
```python:
x = 5
y = 10
print(x + y)
```
خروجی :
```python:
15
```
مثال :
```python
name = "John"
message = "Hello, " + name + "!"
print(message) # Output: Hello, John!
```
</br>

***

</br>

## 💎 انواع داده پایتون
> در پایتون، یک نوع داده به نوع مقداری که یک متغیر در خود نگه می دارد اشاره دارد. پایتون چندین نوع داده داخلی دارد از جمله:

- Integers (int): اعداد کامل بدون اعشار
- Floating-point numbers (float): اعداد با اعشار
- Strings (str): دنباله ترتیب کاراکترهای محصور شده در نقل قول (تک یا دوتایی)
- Booleans (bool): مقادیر درست یا غلط برای عملیات منطقی
- Lists (list):  مجموعه مرتب شده و قابل تغییر ا مقادیر 
- Tuples (tuple): مجموعه‌ای مرتب و تغییرناپذیر از مقادیر 
- Sets (set): مجموعه نامرتب و قابل تغییر از مقادیر منحصر به فرد محصور 
- Dictionaries (dict): مجموعه‌ای از جفت‌های کلید-مقدار.

**انواع داده ها مهم هستند زیرا نوع عملیاتی را که می توانیم روی یک متغیر انجام دهیم، نحوه رفتار آن در موقعیت های خاص و نحوه ذخیره آن در حافظه را تعیین می کنند.**
</br>

#

</br>

### 📌 رشته ها در پایتون 
> رشته‌ها در پایتون توسط یک علامت نقل قول یا دو علامت نقل قول احاطه شده‌اند.
**'hello' مثل این هست  "hello".**
مثال:
```python
print("Hello")
print('Hello')
```
خروجی :
```python:
Hello
Hello
```
#### 🔹رشته را به یک متغیر اختصاص دهید
تخصیص یک رشته به یک متغیر با نام متغیر و به دنبال آن علامت مساوی و رشته انجام می شود:
مثال:
```python:
a = "Hello"
print(a)
```
خروجی :
```python:
Hello
```
#### 🔹رشته های چند خطی
با استفاده از سه نقل قول می توانید یک رشته چند خطی را به یک متغیر اختصاص دهید:
مثال:
```python:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#or 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
خروجی :
```python:
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

#### 💢 برش رشته ها
با استفاده از نحو slice می توانید طیف وسیعی از کاراکترها را برگردانید.
برای برگرداندن بخشی از رشته، شاخص شروع و اندیس پایان را که با یک دو نقطه از هم جدا شده اند، مشخص کنید.
مثال:
```python:
b = "Hello, World!"
print(b[2:5])
```
خروجی :
```python:
llo
```
**⭕️نکته: کاراکتر اول دارای شاخص 0 است.**

#### 💢 رشته ها را اصلاح کنید
پایتون مجموعه ای از متدهای داخلی دارد که می توانید روی رشته ها استفاده کنید.
Example:
```python:
string = "python is amazing"
print(string.capitalize()) #capitalize():
# Output: "Python is amazing"

string = "python is amazing"
print(string.upper())
# Output: "PYTHON IS AMAZING"

string = "PYTHON IS AMAZING"
print(string.lower())
# Output: "python is amazing"

string = "Python, is, amazing"
lst = string.split(",")
print(lst)
# Output: ['Python', ' is', ' amazing']

string = "Python is amazing"
new_string = string.replace("Python", "Java")
print(new_string)
# Output: "Java is amazing"

string = "PYTHON IS AMAZING"
print(len(string))
# Output: 17
```
**⭕️[String Methods](https://www.w3schools.com/python/python_strings_methods.asp)⭕️**

Example :
```python:
a = "Alireza "
b = "Allahyarian"
print(a+b)
```

Output :
```python:
Alireza Allahyarian
```

#

### 📌 اعداد در پایتون 
سه نوع عددی در پایتون وجود دارد:

- int
- float
- complex

مثال :
```python:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```
#### 💢 اعداد صحیح 
عدد صحیح، یک عدد کامل، مثبت یا منفی، بدون اعشار، با طول نامحدود است.

مثال :
```python:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

خروجی :
```python:
<class 'int'>
<class 'int'>
<class 'int'>
```

▫️ یک مثال کمی کاربردی تر:
```python:
# Define a value of type int and assign a value to it
age = 30
print(age)

# Perform arithmetic operations using int changes
year_born = 2023 - age
print("you in the year", year_born, "you are born")
```
خروجی :
```python:
you in the year 1,993 you are born
```

#### 💢 اعداد اعشاری 
اعداداعشاری یک عدد مثبت یا منفی است که شامل یک یا چند اعشار است.

مثال :
```python:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

خروجی :
```python:
<class 'float'>
<class 'float'>
<class 'float'>
```

#### 💢 اعداد مختلط 
اعداد مختلط با یک "j" به عنوان قسمت خیالی نوشته می شوند:

مثال :
```python:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

خروجی :
```python:
<class 'complex'>
<class 'complex'>
<class 'complex'>
```

#

### 📌 بولین
اBoolean یکی از دو مقدار True یا False را نشان می دهد.

##### 🔹مقادیر بولی
در برنامه نویسی اغلب باید بدانید که آیا یک عبارت True یا False است.

شما می توانید هر عبارتی را در پایتون ارزیابی کنید و یکی از دو پاسخ درست یا غلط را دریافت کنید.

وقتی دو مقدار را با هم مقایسه می کنید، عبارت مورد ارزیابی قرار می گیرد و پایتون پاسخ بولی را برمی گرداند:

مثال :
```python:
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

مثال :
```python:
True
False
False
```

#

### 📌 ساختارهای داده (فهرست، تاپل، دیکشنری، مجموعه)

#### 💢 لیست ها
لیست ها برای ذخیره چندین مورد در یک متغیر استفاده می شوند.

لیست ها یکی از 4 نوع داده داخلی در پایتون هستند که برای ذخیره مجموعه داده ها استفاده می شوند، 3 نوع دیگر Tuple، Set و Dictionary هستند که همه با کیفیت ها و کاربردهای متفاوتی هستند.

لیست ها با استفاده از براکت ایجاد می شوند:

مثال :
```python:
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

مثال :
```python:
['apple', 'banana', 'cherry']
```

دسترسی به آیتم یک لیست:
مثال :
```python:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]))
```
خروجی :
```python:
banana
```
**⭕️ اولین مورد دارای شاخص 0 است.**

**⭕️ نمایه سازی منفی یعنی شروع از انتها -1 به آخرین مورد، -2 به دومین مورد آخر و غیره اشاره دارد.**

محدوده شاخص ها:
> می‌توانید با تعیین مکان شروع و پایان محدوده، محدوده‌ای از شاخص‌ها را مشخص کنید.


مثال :
```python:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```
خروجی :
```python:
['cherry', 'orange', 'kiwi']
```

🔶 تغییر موارد لیست:
> برای تغییر مقدار یک مورد خاص، به شماره فهرست مراجعه کنید

مثال :
```python:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
خروجی :
```python:
['apple', 'blackcurrant', 'cherry']
```

🔶 محدوده ای از مقادیر آیتم ها را تغییر دهید
> برای تغییر مقدار اقلام در یک محدوده خاص، لیستی با مقادیر جدید تعریف کنید و به محدوده اعداد فهرستی که می خواهید مقادیر جدید را درج کنید مراجعه کنید.

مثال :
```python:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```
خروجی :
```python:
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```

🔶 موارد را درج کنید
> برای درج یک آیتم لیست جدید، بدون جایگزینی هیچ یک از مقادیر موجود، می توانیم از متد insert() استفاده کنیم.
مثال :
```python:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```
خروجی :
```python:
['apple', 'banana', 'watermelon', 'cherry']
```
**⭕️ در نتیجه مثال بالا، لیست اکنون شامل 4 مورد خواهد بود**

🔶 List Methods
```python:
my_list = [ 1 , 2 , 3 ] #append
my_list.append(4)
print(my_list) # Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list) # Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list) # Output: [1, 4, 2, 3]

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list) # output: [1, 3]

my_list = [1, 2, 3]
popped = my_list.pop()
print(popped) # Output: 3
print(my_list) # output: [1, 2]

my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list) # Output: [1, 2, 3, 4, 5]
```

#### 💢 دیکشنری ها
دیکشنری ها برای ذخیره مقادیر داده در جفت کلید:مقدار استفاده می شوند.
دیکشنری مجموعه ای است که سفارش داده شده*، قابل تغییر است و اجازه تکرار ندارد.

مثال :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
خروجی :
```python:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

🔶 آیتم های دیکشنری 
> آیتم های دیکشنری مرتب، قابل تغییر هستند و اجازه تکرار ندارند.
> آیتم های دیکشنری به صورت جفت کلید: ارزش ارائه می شوند و می توان با استفاده از نام کلید به آنها اشاره کرد.

مثال :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
مثال :
```python:
Ford
```

**⭕️ دیکشنری ها قابل تغییر هستند، به این معنی که بعد از ایجاد دیکشنری می توانیم موارد را تغییر دهیم، اضافه یا حذف کنیم.**

تکراری مجاز نیست
> دیکشنری نمی تواند دو مورد با یک کلید داشته باشد:

مثال :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```
خروجی :
```python:
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

🔶 سازنده dict().
> همچنین می توان از سازنده dict() برای ساخت دیکشنری استفاده کرد.
مثال :
```python:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
خروجی :
```python:
{'name': 'John', 'age': 36, 'country': 'Norway'}
```

🔶 تغییر مقدار
> می توانید مقدار یک مورد خاص را با مراجعه به نام کلید آن تغییر دهید:

مثال :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```
مثال :
```python:
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
```

🔶 Dictionary Methods

Example :
```python:
# clear(): clear all dictionary items
d = {1: 'red', 2: 'blue', 3: 'green'}
d.clear()
print(d)   # Output: {}


#copy(): Copy a dictionary
d = {1: 'red', 2: 'blue', 3: 'green'}
d1 = d.copy()
print(d1)   # Output: {1: 'red', 2: 'blue', 3: 'green'}


#get(): Gets the value corresponding to a key, returning the default value if the key does not exist.
d = {1: 'red', 2: 'blue', 3: 'green'}
print(d.get(1))    # Output: 'red'
print(d.get(4, 'No color'))  # Output: 'No color'


#items(): return all items of the dictionary
d = {1: 'red', 2: 'blue', 3: 'green'}
print(d.items())    # Output: dict_items([(1, 'red'), (2, 'blue'), (3, 'green')])


#keys(): return all keys of the dictionary
d = {1: 'red', 2: 'blue', 3: 'green'}
print(d.keys())    # Output: dict_keys([1, 2, 3])


#values(): return all dictionary values
d = {1: 'red', 2: 'blue', 3: 'green'}
print(d.values())    # Output: dict_values(['red', 'blue', 'green'])


#pop(): remove an item from the dictionary using the corresponding key
d = {1: 'red', 2: 'blue', 3: 'green'}
d.pop(2)
print(d)    # Output: {1: 'red', 3: 'green'}


#update(): update the dictionary by adding another dictionary
d = {1: 'red', 2: 'blue', 3: 'green'}
d1 = {4: 'yellow'}
d.update(d1)
print(d)    # Output: {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow'}
```

#### 💢 مجموعه
مجموعه ها برای ذخیره چندین آیتم در یک متغیر استفاده می شوند.
یکی از 4 نوع داده داخلی در پایتون است که برای ذخیره مجموعه داده ها استفاده می شود، 3 نوع دیگر List، Tuple و Dictionary هستند که همگی با کیفیت ها و کاربردهای متفاوتی هستند.

**⭕️ موارد تنظیم شده غیر قابل تغییر هستند، اما می توانید موارد را حذف کرده و موارد جدید اضافه کنید**

مثال :
```python:
thisset = {"apple", "banana", "cherry"}
print(thisset)
```
خروجی :
```python:
{'banana', 'cherry', 'apple'}
```

- موارد مجموعه نامرتب، غیرقابل تغییر هستند و اجازه مقادیر تکراری را نمی دهند.
- بدون ترتیب به این معنی است که آیتم های یک مجموعه دارای ترتیب تعریف شده ای نیستند.
- آیتم های مجموعه می توانند هر بار که از آنها استفاده می کنید با ترتیب متفاوتی ظاهر شوند و نمی توان با فهرست یا کلید به آنها اشاره کرد.

🔶 به موارد مجموعه دسترسی داشته باشید
> نمی توانید با مراجعه به فهرست یا کلید به موارد موجود در یک مجموعه دسترسی پیدا کنید.
مثال :
```python:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```
خروجی :
```python:
banana
cherry
apple
```

مثال :
```python:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
```
خروجی :
```python:
True
```

🔶 سازنده () set
> همچنین می توان از سازنده set() برای ساخت مجموعه استفاده کرد.

مثال :
```python:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
```
خروجی :
```python:
{'banana', 'apple', 'cherry'}
```

🔶 Set Methods : 

Example :
```python:
# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}

# Intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2)) # Output: {3}

# Difference of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2)) # Output: {1, 2}
```

**⭕️[Set Methods](https://www.w3schools.com/python/python_sets_methods.asp)⭕️**


#### 💢 تاپل
تاپل ها برای ذخیره چندین آیتم در یک متغیر استفاده می شوند.
تاپل یکی از 4 نوع داده داخلی در پایتون است که برای ذخیره مجموعه داده ها استفاده می شود، 3 نوع دیگر List، Set و Dictionary هستند که همگی با کیفیت ها و کاربردهای متفاوتی هستند.
تاپل مجموعه‌ای است منظم و غیرقابل تغییر.

مثال :
```python:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```
خروجی :
```python:
('apple', 'banana', 'cherry')
```

🔶 سفارش داد
> وقتی می گوییم تاپل ها مرتب می شوند به این معنی است که موارد دارای ترتیب مشخصی هستند و ترتیب آن تغییر نمی کند.

🔶 غیر قابل تغییر
> تاپل ها غیر قابل تغییر هستند، به این معنی که پس از ایجاد تاپل نمی توانیم موارد را تغییر، اضافه یا حذف کنیم.

🔶 تکراری را مجاز کنید
> از آنجایی که تاپل ها ایندکس شده اند، می توانند مواردی با همان مقدار داشته باشند:

مثال :
```python:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```
خروجی :
```python:
('apple', 'banana', 'cherry', 'apple', 'cherry')
```

🔶 سازنده () tuple
> همچنین می توان از سازنده ()tuple برای ساخت یک تاپل استفاده کرد.

مثال :
```python:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```
خروجی :
```python:
('apple', 'banana', 'cherry')
```

🔶 به موارد تاپل دسترسی پیدا کنید
> در تاپل ها، دسترسی به آیتم ها دقیقاً مانند لیست ها است

🔶 تاپل ها را به روز کنید
> هنگامی که یک تاپل ایجاد می شود، نمی توانید مقادیر آن را تغییر دهید. تاپل ها غیرقابل تغییر یا تغییر ناپذیر هستند که به آن نیز گفته می شود.
> اما راه حلی وجود دارد. شما می توانید تاپل را به یک لیست تبدیل کنید، لیست را تغییر دهید، و لیست را دوباره به یک تاپل تبدیل کنید.

مثال :
```python:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```
خروجی :
```python:
("apple", "kiwi", "cherry")
```

**⭕️اگر می‌خواهید روی تاپل‌ها عملیات انجام دهید، می‌توانید تاپل را به لیست تبدیل کنید، لیست را تغییر دهید و لیست را دوباره به تاپل تبدیل کنید. ⭕️**

🔶 به تاپل بپیوندید
> برای پیوستن به دو یا چند تاپل می توانید از عملگر + استفاده کنید:

مثال :
```python:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```
خروجی :
```python:
('a', 'b', 'c', 1, 2, 3)
```

🔶 ضرب تاپل
> اگر می خواهید محتوای یک تاپل را چندین بار ضرب کنید، می توانید از عملگر * استفاده کنید:

مثال :
```python:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```
خروجی :
```python:
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

🔶 Tuple Methods

Example :
```python:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x) #output = 2


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x) #output = 3
```

***

## 💎تبدیل انواع داده ها به یکدیگر
گاهی اوقات، ممکن است نیاز به انجام تبدیل بین انواع داخلی داشته باشید. برای تبدیل بین انواع، شما به سادگی از نام نوع به عنوان یک تابع استفاده می کنید.

#### 🔶 عملکرد و توضیحات

| Function | Description |
| ----------- | ----------- |
| int(x) | Converts x to an integer. base specifies the base if x is a string. |
| float(x) | Converts x to a floating-point number. |
| complex(x) | Creates a complex number. |
| str(x) | Converts object x to a string representation. |
| tuple(s) | Converts s to a tuple. |
| list(s) | Converts s to a list. |
| set(s) | Converts s to a set. |
| dict(d) | Creates a dictionary. d must be a sequence of (key,value) tuples. |


Example :
```python:
# Converting a string to an integer:
x = "123"
y = int(x)
print(y)  # Output: 123

# Converting a string to a float:
x = "3.14"
y = float(x)
print(y)  # Output: 3.14

# Converting an integer to a string:
x = 123
y = str(x)
print(y)  # Output: "123"

# Converting a float to a string:
x = 3.14
y = str(x)
print(y)  # Output: "3.14"

# Converting a boolean to an integer:
x = True
y = int(x)
print(y)  # Output: 1

# Converting an integer to a boolean:
x = 0
y = bool(x)
print(y)  # Output: False

# Converting a string to a boolean:
x = "True"
y = bool(x)
print(y)  # Output: True

# Converting a list to a tuple:
x = [1, 2, 3]
y = tuple(x)
print(y)  # Output: (1, 2, 3)

# Converting a tuple to a list:
x = (1, 2, 3)
y = list(x)
print(y)  # Output: [1, 2, 3]
```

### 🖊 the writer : Alireza Allahyarian - [Website](http://microhex.info/) - [linkedin](https://www.linkedin.com/in/alireza-allahyarian-658658258/)- [GitHub](https://github.com/graymicro) - [Tlegeram](https://t.me/graycubeteam) 

#### **[♦️license by gray cube team♦️](graycubeteam.github.io)**
