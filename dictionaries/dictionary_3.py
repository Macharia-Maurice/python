students=[
    {'name':'Hermione', 'house':'Gryffindor', 'patronus':'Otter'},
    {'name':'Harry', 'house':'Gryffindor', 'patronus':'Stag'},
    {'name':'Ron', 'house':'Gryffindor', 'patronus':'Jack Russell terrier'},
    {'name':'Draco', 'house':'Slytherin', 'patronus':None},
]
#  printing individual values
print(students[0]['name'])

# printing keys and values
for i in range(len(students)):
    if i!=0 :
        print("")

    for student in students[i]:
        if student!='patronus':
         print(student, students[i][student], sep=':', end=', ')
        else:print(student, students[i][student], sep=':', end='.')