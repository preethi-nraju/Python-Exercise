'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.[Topic cover: function]'''

def year():
    name = input("What is your name: ")
    age = int(input("How old are you: "))
    return 100 - age + 2021
print("The person turn 100 years in " + str(year()))