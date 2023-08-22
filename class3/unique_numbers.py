def count_unique_numbers(numbers: list[int]) -> int:
    unique_numbers = list()
    amount = 0
    for value in numbers:
        if value not in unique_numbers:
            unique_numbers.append(value)
            amount += 1
    return amount


def input_number(msg: str) -> int:
    while True:
        user_input = input(msg)
        if user_input.isdigit():
            user_input = int(user_input)
            return user_input
    
        else:
            print("Please, enter a number.")
            

def create_list_of_ints(n: int) -> list[int]:
    user_inputs = list()
    for _ in range(n):
        user_input = input_number("Enter a number: ")
        user_inputs.append(user_input)
    return user_inputs


def in_case_user_wants_to_create_list_themselves():
    amount_of_nums = input_number("Enter amount of numbers you want to insert: ")
    user_numbers = create_list_of_ints(amount_of_nums)
    print(count_unique_numbers(user_numbers))


def main(numbers: list[int]):   
    print(count_unique_numbers(numbers))


# in_case_user_wants_to_create_list_themselves()

# if doesn't just put values in "numbers":

# numbers = [1, 2, 3, 4, 5, 5]
# main(numbers)