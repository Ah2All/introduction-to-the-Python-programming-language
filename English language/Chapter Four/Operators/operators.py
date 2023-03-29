# ---------- Arithmetic operators -----------#

x = 10
y = 5

print(x + y) # 15
print(x - y) # 5
print(x * y) # 50
print(x / y) # 2.0
print(x % y) # 0
print(x ** y) # 100000
print(x // y) # 2


# ---------- comparison operators -----------#
x = 10
y = 5

print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False



# ---------- Assignment operators -----------#

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



# ---------- logical operators -----------#

x = 10
y = 5

print(x > 5 and y < 10) # True
print(x > 5 or y > 10) # True
print(not(x == y)) # True


# ---------- membership operators -----------#

x = ["apple", "banana"]
print("banana" in x) # True
print("cherry" not in x) # True



# ---------- Identity operators -----------#

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
