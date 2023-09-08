from numbers_input import number_input as num

def count_elements_with_less_adjacent_values(arr: list) -> int:
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1
    return count


def main():
    amount = num.input_positive_int("Enter amount of numbers you want to input")
    user_list = list()
    for _ in range(amount):
        user_list.append(num.input_any_number("Enter a number"))
        
    count_elms = count_elements_with_less_adjacent_values(user_list)
    print(count_elms)