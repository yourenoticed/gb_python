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


def count_elms_more_than_prev(numbers: list) -> int:
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1
    return count
        
        
def in_case_user_wants_to_create_list_themselves():
    amount_of_nums = input_number("Enter amount of values you want to insert")
    user_numbers = create_list_of_ints(amount_of_nums)
    print(count_elms_more_than_prev(user_numbers))


def main(numbers: list[int]):
    print(count_elms_more_than_prev(numbers))
    
    
# in_case_user_wants_to_create_list_themselves()

# if doesn't just put values in "numbers":

# numbers = [0, -1, 5, 2, 3]    
# main(numbers)