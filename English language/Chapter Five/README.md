## 🔹The topics we discuss in this chapter:

- [Conditional commands (if, else, elif)](#-arithmetic-operators)
- [Loops in Python (for, while)](#-comparison-operators)
- [Functions](#-assignment-operators)

***

## 💎Concept of Conditional commands
> Conditional statements in Python allow you to specify code that should be executed according to certain conditions. A conditional statement may be a single condition or a combination of several conditions.

### ⭕️ Python supports the usual logical conditions from mathematics:

- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b
- These conditions can be used in several ways, most commonly in "if statements" and loops.

### 💢 if statement :
> An "if statement" is written by using the if keyword.

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

### 💢 Elif :
> The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"

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

### 💢 Elif :
> The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"

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

### 💢 Else :
> The else keyword catches anything which isn't caught by the preceding conditions.

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

## 💎Concept of Loops in Python
> Conditional statements in Python allow you to specify code that should be executed according to ce
