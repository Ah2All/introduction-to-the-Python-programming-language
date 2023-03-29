primes = [2, 3, 5, 7]

numbers = list(range(1, 6))

# ----------------------------------------------------------------- #

my_list = [1, 2, 3] #append
my_list.append(4)
print(my_list) # خروجی: [1, 2, 3, 4]

my_list = [1, 2, 3] 
my_list.extend([4, 5])
print(my_list) # خروجی: [1, 2, 3, 4, 5]

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list) # خروجی: [1, 4, 2, 3]

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list) # خروجی: [1, 3]

my_list = [1, 2, 3]
popped = my_list.pop()
print(popped) # خروجی: 3
print(my_list) # خروجی: [1, 2]

my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list) # خروجی: [1, 2, 3, 4, 5]

# ----------------------------------------------------------------- #

numbers = [] # ایجاد یک لیست خالی

# دریافت ۵ عدد از کاربر و ذخیره آن‌ها در لیست

num = int(input("Enter a number: "))
numbers.append(num)

# محاسبه مجموع عناصر لیست
total = sum(numbers)

# چاپ مجموع عناصر لیست
print("The sum of the numbers is:", total)

# ----------------------------------------------------------------- #

names = [] # ایجاد یک لیست خالی

# دریافت ۵ نام از کاربر و ذخیره آن‌ها در لیست
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

# چاپ تمامی نام‌های ذخیره شده در لیست
print("The names are:")
for name in names:
    print(name)

