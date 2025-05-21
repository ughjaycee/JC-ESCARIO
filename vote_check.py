# vote_check.py
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible to vote!")
else:
    print(f"{name}, you are not eligible to vote yet.")
