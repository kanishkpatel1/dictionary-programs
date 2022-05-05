# . Write a Python program that accepts a hyphen separated sequence of words as input and prints the 
# words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items: green-red-yellow-black-white 
# Expected Result: black-green-red-white-yellow
a=input("Enter the string with hyphen (-):").split("-")
b="-".join(sorted(a))
print(b)