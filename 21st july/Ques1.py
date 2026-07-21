# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

# Accept a string from the user
text = input("Enter a string: ")

# Check if the string starts with "Is"
if text.startswith("Is"):
    print("Result:", text)
else:
    print("Result: Is " + text)