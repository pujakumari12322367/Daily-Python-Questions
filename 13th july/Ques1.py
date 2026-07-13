# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

num = int(input("Enter a number: "))

if num <= 17:
    difference = 17 - num
else:
    difference = 2 * abs(num - 17)

print("Result:", difference)