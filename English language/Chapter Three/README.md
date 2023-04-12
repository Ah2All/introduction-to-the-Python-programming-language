## 🔹The topics we discuss in this chapter:

- [Concept of Variable](#concept-of-variable)

   - [How to define a variable in Python](#how-to-define-a-variable-in-python)
   - [Rules for Python variables](#%EF%B8%8F-rules-for-python-variables)
   
- [Python Data Types](#-python-data-types)

   - ([string](#-python-strings), [integers](#-python-numbers), [bool](#-python-booleans), [float](#-python-numbers)) 
   - Data Structures([List](#-lists), [Tuple](#-tuples), [Dictionaries](#-dictionaries), [set](#-set))
   
- [Convert data types to each other]()

</br>

## 💎Concept of Variable
> In Python, a variable is a name that refers to a value. It is used to store and manipulate data. When you create a variable in Python, you must choose a name for it, assign it a value, and declare its data type (although in most cases, Python automatically detects the data type based on the assigned value).

**⭕️ It is like a container into which we pour something and then use it**

</br>

#

### 🔻How to define a variable in Python🔻
To define a variable in Python, we first specify the variable name and then use the equal sign (=) to assign the desired value to the variable. For example:

```python:
name = "John"
age = 30
height = 1.75
```
In this example, three variables named name, age, and height are defined, and they point to the values "John", 30, and 1.75, respectively. These values can be strings, integers or floats, or even other data types.
#
</br>

### ♨️ Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

For example:
```python:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```
Illegal variable names:
```python:
2myvar = "John"
my-var = "John"
my var = "John"
```
#
### 💢 Python Variables - Assign Multiple Values
#### 🔹Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
```python:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
#### 🔹One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
```python:
x = y = z = "Orange"
print(x)
print(y)
print(z)
```
### 💢 Python - Output Variables
#### 🔹Output Variables
The Python print() function is often used to output variables.
```python:
x = "Python is awesome"
print(x)
```
Output :
```python:
Python is awesome
```
In the print() function, you output multiple variables, separated by a comma:
```python:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```
Output :
```python:
Python is awesome
```
You can also use the + operator to output multiple variables:
```python:
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
```
Output :
```python:
Python is awesome
```
**🛑 Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".**

For numbers, the + character works as a mathematical operator:
```python:
x = 5
y = 10
print(x + y)
```
Output :
```python:
15
```
Example :
```python
name = "John"
message = "Hello, " + name + "!"
print(message) # Output: Hello, John!
```
</br>

***

</br>

## 💎 Python Data Types
> In Python, a data type refers to the type of value that a variable holds. Python has several built-in data types including:

- Integers (int): Whole numbers without decimal points
- Floating-point numbers (float): Numbers with decimal points
- Strings (str): Ordered sequence of characters enclosed in quotes (single or double)
- Booleans (bool): True or False values used for logical operations
- Lists (list): Ordered, mutable collection of values enclosed in square brackets
- Tuples (tuple): Ordered, immutable collection of values enclosed in parentheses
- Sets (set): Unordered, mutable collection of unique values enclosed in curly braces
- Dictionaries (dict): Collection of key-value pairs enclosed in curly braces with colons separating the keys and values.

**Data types are important because they determine the type of operations we can perform on a variable, how it behaves in certain situations, and how it is stored in memory.**
</br>

#

</br>

### 📌 Python Strings
> Strings in python are surrounded by either single quotation marks, or double quotation marks. 
**'hello' is the same as "hello".**
Example:
```python
print("Hello")
print('Hello')
```
Output :
```python:
Hello
Hello
```
#### 🔹Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
Example:
```python:
a = "Hello"
print(a)
```
Output :
```python:
Hello
```
#### 🔹Multiline Strings
You can assign a multiline string to a variable by using three quotes:
Example:
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
Output :
```python:
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

#### 💢 Slicing Strings
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
Example:
```python:
b = "Hello, World!"
print(b[2:5])
```
Output :
```python:
llo
```
**⭕️Note: The first character has index 0.**

#### 💢 Modify Strings
Python has a set of built-in methods that you can use on strings.
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

### 📌 Python Numbers
There are three numeric types in Python:

- int
- float
- complex

Example :
```python:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```
#### 💢 Integer
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Example :
```python:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

Output :
```python:
<class 'int'>
<class 'int'>
<class 'int'>
```

▫️ A slightly more practical example:
```python:
# Define a value of type int and assign a value to it
age = 30
print(age)

# Perform arithmetic operations using int changes
year_born = 2023 - age
print("you in the year", year_born, "you are born")
```
Output :
```python:
you in the year 1,993 you are born
```

#### 💢 Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Example :
```python:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Output :
```python:
<class 'float'>
<class 'float'>
<class 'float'>
```

#### 💢 Complex
Complex numbers are written with a "j" as the imaginary part:

Example :
```python:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

Output :
```python:
<class 'complex'>
<class 'complex'>
<class 'complex'>
```

#

### 📌 Python Booleans
Booleans represent one of two values: True or False.

##### 🔹Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

Example :
```python:
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

Output :
```python:
True
False
False
```

#

### 📌 Data Structures(List, Tuple, Dictionaries, set)

#### 💢 Lists
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

Example :
```python:
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

Output :
```python:
['apple', 'banana', 'cherry']
```

Access Items:
Example :
```python:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]))
```
Output :
```python:
banana
```
**⭕️ The first item has index 0.**

**⭕️ Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc..**

Range of Indexes: 
> You can specify a range of indexes by specifying where to start and where to end the range.


Example :
```python:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```
Output :
```python:
['cherry', 'orange', 'kiwi']
```

🔶 Change List Items: 
> To change the value of a specific item, refer to the index number

Example :
```python:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
Output :
```python:
['apple', 'blackcurrant', 'cherry']
```

🔶 Change a Range of Item Values
> To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values

Example :
```python:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```
Output :
```python:
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```

🔶 Insert Items
> To insert a new list item, without replacing any of the existing values, we can use the insert() method.

Example :
```python:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```
Output :
```python:
['apple', 'banana', 'watermelon', 'cherry']
```
**⭕️ As a result of the example above, the list will now contain 4 items**

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

#### 💢 Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Example :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
Output :
```python:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

🔶 Dictionary Items
> Dictionary items are ordered, changeable, and does not allow duplicates.
> Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Example :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
Output :
```python:
Ford
```

**⭕️ Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.**

🔶 Duplicates Not Allowed
> Dictionaries cannot have two items with the same key:

Example :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```
Output :
```python:
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

🔶 The dict() Constructor
> It is also possible to use the dict() constructor to make a dictionary.

Example :
```python:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
Output :
```python:
{'name': 'John', 'age': 36, 'country': 'Norway'}
```

🔶 Change Values
> You can change the value of a specific item by referring to its key name:

Example :
```python:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```
Output :
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

#### 💢 Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

**⭕️ Set items are unchangeable, but you can remove items and add new items**

Example :
```python:
thisset = {"apple", "banana", "cherry"}
print(thisset)
```
Output :
```python:
{'banana', 'cherry', 'apple'}
```

- Set items are unordered, unchangeable, and do not allow duplicate values.
- Unordered means that the items in a set do not have a defined order.
- Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

🔶 Access Set Items
> You cannot access items in a set by referring to an index or a key.

Example :
```python:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```
Output :
```python:
banana
cherry
apple
```

Example :
```python:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
```
Output :
```python:
True
```

🔶 The set() Constructor
> It is also possible to use the set() constructor to make a set.

Example :
```python:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
```
Output :
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


#### 💢 Tuples
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.

Example :
```python:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```
Output :
```python:
('apple', 'banana', 'cherry')
```

🔶 Ordered
> When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

🔶 Unchangeable
> Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

🔶 Allow Duplicates
> Since tuples are indexed, they can have items with the same value:

Example :
```python:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```
Output :
```python:
('apple', 'banana', 'cherry', 'apple', 'cherry')
```

🔶 The tuple() Constructor
> It is also possible to use the tuple() constructor to make a tuple.

Example :
```python:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```
Output :
```python:
('apple', 'banana', 'cherry')
```

🔶 Access Tuple Items
> In tuples, access to items is exactly like lists 

🔶 Update Tuples
> Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
> But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Example :
```python:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```
Output :
```python:
("apple", "kiwi", "cherry")
```

**⭕️If you want to perform operations on tuples You can convert the tuple to a list, modify the list, and convert the list back to a tuple. ⭕️**

🔶 Join Tuples
> To join two or more tuples you can use the + operator:

Example :
```python:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```
Output :
```python:
('a', 'b', 'c', 1, 2, 3)
```

🔶 Multiply Tuples
> If you want to multiply the content of a tuple a given number of times, you can use the * operator:

Example :
```python:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```
Output :
```python:
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

🔶 Tuple Methods
> Python has two built-in methods that you can use on tuples.

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

## 💎Convert data types to each other
Sometimes, you may need to perform conversions between the built-in types. To convert between types, you simply use the type name as a function.

#### 🔶 Function & Description

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
