# . Given a string, return a "rotated right" version where the last n chars are moved to the start. The 
# string length will be at least 2.
# right2("Hello",2) → "loHel" 
# right2("java",3) → "avaj"
# right2("Hi",3) → "Hi"
a=input("Enter string:")
l=len(a)

b=int(input("Enter the terms to replace"))
x=l-b
c=a[x:]
d=a[:x]
print(c+d)