students={
    'Maurice':"Cs",
    'Daniel':'financial Eng',
    'Cynthia':'Actuarial Sc',
    'Ann':'Medicine PSY',
    'Peter':'Medicine'
}

# print out the whole dictionary including the curly braces
print(students)

# print out only the keys
for student in students:
    print(student)

# printing out keys with their values
for student in students:
    print(student,'>>',students[student],)