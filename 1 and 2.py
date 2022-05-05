#getkeys['name','age']
a={'name':'kanishk','age':18,'location':'U.P','country':'Indian'}
c={key:a[key] for key in ['name','age']} #get keys and create new dictionary
print(c)

b={key:a[key] for key in a.keys()-['name','age']} #this is for delete set of keys from dictionary
print(b)