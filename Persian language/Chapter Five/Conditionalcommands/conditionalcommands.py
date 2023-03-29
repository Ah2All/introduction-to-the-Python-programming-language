

#syn

# if condition1:
#     code to execute if condition1 is True
# elif condition2:
#     code to execute if condition1 is False, but condition2 is True
# else:
#     code to execute if neither condition is True







age = 21
if age < 18:
    print("You are not old enough to vote yet.")
elif age < 21:
    print("You can vote, but you cannot buy alcohol.")
else:
    print("You can vote and buy alcohol.")


num = 5

if num >= 0:
    print("The number is positive")
else:
    print("The number is negative")



name = input("What is your name? ")

if name == "Saeed":
    print("Hello, Saeed!")
else:
    print("Hello, "+name+".")
