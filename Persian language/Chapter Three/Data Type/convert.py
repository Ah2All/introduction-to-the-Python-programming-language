num = 123
str_num = str(num)
print(type(str_num)) # <class 'str'>


str_num = "456"
num = int(str_num)
print(type(num)) # <class 'int'>


float_num = 3.14
int_num = int(float_num)
print(type(int_num)) # <class 'int'>


int_num = 42
float_num = float(int_num)
print(type(float_num)) # <class 'float'>


int_num = 0
is_true = bool(int_num)
print(type(is_true)) # <class 'bool'>

is_true = True
int_num = int(is_true)
print(type(int_num)) # <class 'int'>


my_string = "Hello, World!"
my_list = list(my_string)
print(my_list) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']


my_list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
my_string = ''.join(my_list)
print(my_string) # 'Hello, World!'


my_tuple = ('apple', 'banana', 'cherry')
my_list = list(my_tuple)
print(my_list) # ['apple', 'banana', 'cherry']


my_list = ['apple', 'banana', 'cherry']
my_tuple = tuple(my_list)
print(my_tuple) # ('apple', 'banana', 'cherry')


my_string = '{"name": "John", "age": 30, "city": "New York"}'
my_dict = dict(my_string)
print(my_dict) # {'{': None, '"': None, 'n': None, 'a': None, 'm': None, 'e': None, ...


my_dict = {"name": "John", "age": 30, "city": "New York"}
my_string = str(my_dict)
print(my_string) # "{'name': 'John', 'age': 30, 'city': 'New York'}"


str_list = ["3", "5", "7", "9"]
num_list = [int(x) for x in str_list]
print(num_list) # [3, 5, 7, 9]


num_list = [1, 2, 3, 4, 5]
str_list = [str(x) for x in num_list]
print(str_list) # ['1', '2', '3', '4', '5']
