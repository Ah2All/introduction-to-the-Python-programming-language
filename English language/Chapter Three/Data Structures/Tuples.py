names = [] # ایجاد یک لیست خالی

# دریافت ۵ نام از کاربر و ذخیره آن‌ها در لیست
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
    mytuple = tuple(names)

# چاپ تمامی نام‌های ذخیره شده در لیست
print("The names are:")
for name in names:
    print(name)

print(mytuple)


# تعریف یک tuple جدید
person = ("John", "Doe", 27, "123-456-7890")

# دسترسی به اطلاعات در یک tuple با استفاده از indexing
print("Name:", person[0], person[1])
print("Age:", person[2])
print("Phone:", person[3])