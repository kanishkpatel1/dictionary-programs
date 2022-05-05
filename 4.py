# create a dictionary of fabonacci series
#Ex-----> {1:0,2:1,3:1,4:2,5:3}
x={}
n=int(input("Enter the value of n: "))
a,b=0,1
for i in range(1,n+1):
    
    x.update({i:a})
    a,b=b,a+b
    
print(x) 