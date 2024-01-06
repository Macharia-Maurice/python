import database
# database.delete_record('12')
# database.add_one_record('june','may','may@gmail')
# items=[
#     ('june','may','may@gmail'),
#     ('solly', 'march', 'march@gmail')
# ]
# database.add_many_records(items)
# database.show_all()

person_x=database.search_by_id('10')
print(person_x)