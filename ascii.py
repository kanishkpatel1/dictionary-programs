# Create first dictionary name ‘ASC_Value’ in python using loop in which keys are alphabets (Lower 
# case letters) and values are their corresponding ASCII code. Print the final dictionary items in 
# separated lines. Also read your first name and calculate your ASCII score (add ASCII code of each 
# character of your name) using that dictionary ASC_Value.
a={}
n=list(input("Enter your name:"))
print(n)
for i in range(1,27):
    ch=96+i
    b=chr(ch)
    for j in range(1,27):
            a.update({b:ch})
sum=0
for i in range (len(n)):
    
     b=n.pop()
     sum=sum+a.get(b)

print(a)
print(sum)