## 🔹The topics we discuss in this chapter:

- [Concept of Variable](#concept-of-variable)

   - [How to define a variable in Python](#how-to-define-a-variable-in-python)
   - [Rules for Python variables](#%EF%B8%8F-rules-for-python-variables)
   
- [Python Data Types](#-python-data-types)

   - (string, integers, bool, float) 
   - Data Structures(List, Tuple, Dictionaries, set)
   
- Convert data types to each other

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
