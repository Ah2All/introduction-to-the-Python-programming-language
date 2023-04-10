## 🔹The topics we discuss in this chapter:

- variable
- Data Type
   - (string, integers, bool, float) 
   - Data Structures(List, Tuple, Dictionaries, set)
- Convert data types to each other

</br>

## 💎Concept of Variable
> In Python, a variable is a name that refers to a value. It is used to store and manipulate data. When you create a variable in Python, you must choose a name for it, assign it a value, and declare its data type (although in most cases, Python automatically detects the data type based on the assigned value).

**⭕️ It is like a container into which we pour something and then use it**

### 🔻How to define a variable in Python🔻
To define a variable in Python, we first specify the variable name and then use the equal sign (=) to assign the desired value to the variable. For example:

```python:
name = "John"
age = 30
height = 1.75
```
In this example, three variables named name, age, and height are defined, and they point to the values "John", 30, and 1.75, respectively. These values can be strings, integers or floats, or even other data types.

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
