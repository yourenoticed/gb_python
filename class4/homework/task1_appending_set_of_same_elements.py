list_1 = list()
amount_1 = int(input("Enter amount of elements you want to input into the first list: "))

for _ in range(amount_1):
    list_1.append(int(input("Enter a value: ")))

list_2 = list()    
amount_2 = int(input("Enter amount of elements you want to input into the second list: "))

for _ in range(amount_2):
    list_2.append(int(input("Enter a value: ")))

list_1 = set(list_1)
list_2 = set(list_2)

result_list = list(list_1.intersection(list_2))
result_list.sort()

print(result_list)