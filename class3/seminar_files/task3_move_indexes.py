def move_indexes(numbers: list, k: int):
    for _ in range(k % len(numbers)):
        numbers.insert(0, numbers.pop())
        
my_list = [1, 2, 3, 4, 5, 6]
move_indexes(my_list, 3)
print(my_list)