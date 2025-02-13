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