n=int(input("Enter the value of n:"))
dct={}
for i in range(n):
    a=int(input("Enter the radious of the circle:"))
    b=a*2*3.14
    dct.update({a:b})
print(dct)