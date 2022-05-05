a={'name':'bob','age':'25','place':'bangalore'}
b={key:value for key,value in sorted(a.items(),key=lambda item:item[1],reverse=True)} #sorted in reverse
print(b)
