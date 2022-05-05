# Programe whose key is perfect no and value is strong number 
lst1=[]
# code for generate perfect  number in range
for i in range(1,10000):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        lst1.append(i)
  
lst2=[]
# code for generate strong number in range
for k in range(1,100000):
        temp=k
        suma=0
        while(k!=0):
            r=k%10
            fact=1
            
            for i in range(1,r+1):
                fact=fact*i
            suma+=fact
            k=k//10
        if(temp==suma):
            lst2.append(suma)
    
print(lst1)
print(lst2)
c=zip(lst1,lst2)
d=dict(c)
print(d)
  