# 1. Write a program that accepts a comma separated sequence of words as input and prints the words in a 
# comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# Input: without,hello,bag,world 
# Then, the output should be:
# bag,hello,without,world
a=input("Enter the : ").split()
b=" ".join(sorted(a))
print(b)