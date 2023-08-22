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


def find_closest_to_sought(numbers: list[int], sought: int) -> int:
    diffs = dict()
    for value in numbers:
        diffs[value] = abs(value - sought)
    
    closest_to_sought = numbers[0]
    min_diff = diffs[closest_to_sought]
    
    for key in diffs:
        if min_diff > diffs[key]:
            min_diff = diffs[key]
            closest_to_sought = key
            
    return closest_to_sought


def main():
    amount_of_nums = input_number("Enter amount of numbers you want to insert: ")
    user_numbers = create_list_of_ints(amount_of_nums)
    sought = input_number("Enter a number to compare with: ")
    print(find_closest_to_sought(user_numbers, sought))

    
main()