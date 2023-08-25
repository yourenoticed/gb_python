user_input = [
    {'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, 
    {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, 
    {'VIII': 'S007'}  
]

my_set = set()
for dictionary in user_input:
    
    for value in dictionary.values():
        my_set.add(value)
    
print(my_set)