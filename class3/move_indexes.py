def create_list(n: int) -> list:
    user_inputs = list()
    for _ in range(n):
        user_input = input("Enter a value: ")
        user_inputs.append(user_input)
    return user_inputs


def input_number(msg: str) -> int:
    while True:
        user_input = input(msg)
        if user_input.isdigit():
            user_input = int(user_input)
            return user_input
    
        else:
            print("Please, enter a number.")
            

def in_case_user_wants_to_create_list_themselves():
    amount_of_nums = input_number("Enter amount of values you want to insert")
    user_numbers = create_list(amount_of_nums)
    print()
    shift = input_number("Enter the shift amount")
    print(move_values(user_numbers, shift))


def move_values(numbers: list, shift: int):
    for _ in range(shift % len(numbers)):
        numbers.insert(0, numbers[-1])
        numbers.pop()

def main(numbers: list[int]):
    move_values(numbers, 4)
    print(numbers)
    
# in_case_user_wants_to_create_list_themselves()

# if the user doesn't wanna do it, put values in "values":

# values = [5, 3, 4, 2, 6, 8, 1, 2, 3]
# main(values)