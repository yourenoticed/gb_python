def tables_needed(amount_of_groups: int):
    groups = list()
    for group_num in range(amount_of_groups):
        while True:
            user_input = input(f"Enter amount of students in {group_num + 1} group: ")
            if user_input.isdigit():
                groups.append(int(user_input))
                break
            else:
                print("Enter an integer number")
            
    tables = 0
    for students in groups:
        tables += (students - 1) // 2 + 1
        
    return tables

print(tables_needed(3))