from numbers_input import number_input as num

def count_same_pairs(arr: list) -> int:
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
    
    return count


def main():
    amount = num.input_positive_int("Enter amount of numbers you want to input")
    user_list = list()
    for _ in range(amount):
        user_list.append(num.input_any_number("Enter a number"))
    
    count = count_same_pairs(user_list)
    print(f'\n{user_list}\nAmount of pairs with the same value: {count}')
    
main()
    
    
    