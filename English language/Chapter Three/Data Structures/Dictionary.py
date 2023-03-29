# Build a dictionary
my_dict = {'name': 'Maryam', 'age': 25, 'country': 'Iran'}

# Access dictionary elements using keys
print(my_dict['name'])   # output: Maryam
print(my_dict['age'])    # output: 25

# Change the value of a key in the dictionary
my_dict['age'] = 30
print(my_dict['age'])    # output: 30

# Add a new key-value pair to the dictionary
my_dict['profession'] = 'Engineer'
print(my_dict)
# output: {'name': 'Maryam', 'age': 30, 'country': 'Iran', 'profession': 'Engineer'}

# ----------------------------------------------------------------- #

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

# ----------------------------------------------------------------- #

text = "In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available."
text = text.lower()
words = text.split(" ")

word_count = {}

for word in words:
    count = word_count.get(word, 0)
    word_count[word] = count + 1

print(word_count)
