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


def count_number(numbers: list[int], sought: int) -> int:
    count = 0
    for value in numbers:
        if value == sought:
            count += 1
    return count


def main():
    amount_of_nums = input_number("Enter amount of numbers you want to insert: ")
    user_numbers = create_list_of_ints(amount_of_nums)
    sought = input_number("Enter a number you want to count: ")
    print(count_number(user_numbers, sought))

    
main()