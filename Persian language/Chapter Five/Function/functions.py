import random

def guess_number(num):
    secret_num = random.randint(0, 100)
    if num == secret_num:
        print("Congratulations! You guessed the number!")
    elif num > secret_num:
        print("Too high! Try again.")
        guess_number(int(input("Enter a number: ")))
    else:
        print("Too low! Try again.")
        guess_number(int(input("Enter a number: ")))

guess_number(int(input("Enter a number: ")))

