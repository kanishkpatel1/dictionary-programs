#change the value in nested dictionary
employee_details={
    'Employee1':{
        'name':'bob',
        'age':45,
        'profession':'writer',
        'city':'varanasi'
    },
    'Employee2':{
        'name':'kanishk',
        'age':18,
        'profession':'coder',
        'city':'kannauj'
    },
        'Employee3':{
        'name':'rahul',
        'age':19,
        'profession':'hacker',
        'city':'gopalganj'
    }

}
employee_details['Employee3']['name']='prince' #this will edit name
print(employee_details)