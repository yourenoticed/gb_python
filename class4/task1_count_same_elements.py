user_input = "a a a b c a a d c d d"
list_input = user_input.split()
values = [] # list()

for i in range(len(list_input)):
    if list_input[i] not in values:
        values.append(list_input[i])
    else:
        values.append(list_input[i])
        list_input[i] += f"_{values.count(list_input[i]) - 1}"      

print(" ".join(list_input))