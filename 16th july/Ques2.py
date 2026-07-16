# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum = num1 + num2 + num3

if num1 == num2 == num3:
    print("Result:", 3 * sum)
else:
    print("Result:", sum)