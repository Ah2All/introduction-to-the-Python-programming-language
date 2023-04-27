## 🔹The topics we discuss in this chapter:

-  What Is Object-Oriented Programming in Python?
-  Class in Python


## 💎What Is Object-Oriented Programming in Python?

### 💢 Concept Object-Oriented Programming
Object-oriented programming is a programming paradigm in which programs are designed and implemented as collections of objects. Each object has specific properties and behaviors that are defined as methods. By using object-oriented programming, you can design programs that are modular and extensible. In other words, by using objects and their relationships, you can design programs that are easily adaptable and changeable in the future.For example, suppose you want to design a program for managing a library. In object-oriented programming, a library object is defined with properties such as a name, address, opening and closing times, and behaviors such as adding books, deleting books, and searching for books. Similarly, a book object is defined with properties such as a name, author, and publication year, and behaviors such as displaying book information and editing book information. Then, using these objects, you can design your library program.

### 💢 Object-Oriented Programming in python
Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.

Another common programming paradigm is procedural programming, which structures a program like a recipe in that it provides a set of steps, in the form of functions and code blocks, that flow sequentially in order to complete a task.

The key takeaway is that objects are at the center of object-oriented programming in Python, not only representing the data, as in procedural programming, but in the overall structure of the program as well.


## 💎 Python Classes and Objects

- Python is an object oriented programming language.
- Almost everything in Python is an object, with its properties and methods.
- A Class is like an object constructor, or a "blueprint" for creating objects.

### 💢 Create a Class:
```python:
class MyClass:
  x = 5
```

### 💢 Create Object:
```python:
p1 = MyClass()
print(p1.x)
```

### 💢 The __init__() Function:
> All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```python:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

### 💢 Object Methods
> Objects can also contain methods. Methods in objects are functions that belong to the object.

```python:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

### 💢 The self Parameter
> The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

```python:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```

### 🖊 the writer : Alireza Allahyarian - [Website](http://microhex.info/) - [linkedin](https://www.linkedin.com/in/alireza-allahyarian-658658258/)- [GitHub](https://github.com/graymicro) - [Tlegeram](https://t.me/graycubeteam) 

#### **[♦️license by gray cube team♦️](graycubeteam.github.io)**
