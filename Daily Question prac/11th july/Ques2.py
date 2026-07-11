# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
filename = input("Enter filename: ")
extension = filename.split(".")
print("Extension:", extension[-1])