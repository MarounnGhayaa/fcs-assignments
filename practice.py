#Exercise 1
age = int(input("Enter your age: "))
if age < 5:
    print("The ticket is for free")
elif age < 10:
    print("The ticket costs 5$")
elif age < 18:
    print("The ticket costs 7$")
else:
    print("The ticket costs 10$")

#Exercise 2
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Exercise 3
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")