'''Create a program to compare three numbers and find the bigger numbers.[topics covered: function]'''

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))
def max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print('The bigger number is: ', num1)
    elif num2 > num1 and num2 > num3:
        print('The bigger number is: ', num2)
    else:
        print('The bigger number is: ', num3)
max(num1,num2,num3);