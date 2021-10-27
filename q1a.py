'''Create a program to compare three numbers and find the bigger numbers. [topics covered: identified, variable, types, operator, if statement]'''

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if (num1 >= num2) and (num1 >= num3):
   bigger = num1
elif (num2 >= num1) and (num2 >= num3):
   bigger = num2
else:
   bigger = num3
print("The largest number is", bigger)