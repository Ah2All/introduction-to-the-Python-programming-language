#str
str1 = "Hello, world!"
str2 = 'It is a nice day.'

#more then one line
txt = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


a = "Alireza "
b = "Allahyarian"
print(a+b)


#metod 
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





