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
> Loops in Python are one of the basic and powerful tools used to iterate over a block of code repeatedly based on certain conditions or sequence of data. There are two types of loops in Python

### 💢 For Loops :
> For loop is used when we want to iterate over a sequence (list, tuple, string, or any other iterable object) and execute the block of statements or code for each element of the sequence. The loop continues till the last element in the sequence is reached.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

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

#### 🔶 The break Statement
> With the break statement we can stop the loop before it has looped through all the items:

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

#### 🔶 The range() Function
> To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
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

#### 🔶 Else in For Loop
> The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

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

### 💢 For Loops :
> While loop is used when we want to repeat a statement while the given condition is true. The loop continues till the condition becomes false.


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

#### 🔶 The break Statement
> With the break statement we can stop the loop even if the while condition is true:

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


#### 🔶 Else in For Loop
> With the else statement we can run a block of code once when the condition no longer is true:

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
