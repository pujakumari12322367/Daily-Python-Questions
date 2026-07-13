# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5

n = input("Enter a number: ")

n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)

result = n1 + n2 + n3

print("Result:", result)