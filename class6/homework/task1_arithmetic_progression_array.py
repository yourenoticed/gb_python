from numbers_input import number_input as num
                
                
def create_list_with_arithmetic_progression(start, difference, quantity) -> list:
    result_list = list()
    curr_num = start
    
    for _ in range(quantity):
        result_list.append(curr_num)
        curr_num += difference    
   
    return result_list

# if list is not going to contain integers only:
def create_list_with_int_arithmetic_progression(start: int, difference: int, quantity: int) -> list[int]:
    return [x for x in range(start, start + difference * quantity, difference)]

    
def main_any_numbers():
    print("\nWelcome to list creation tool!")
    start_value = num.input_any_number("Enter beginning value of arithmetic progression")
    diff = num.input_any_number("Enter difference of arithmetic progression")
    amount = num.input_positive_int("Enter amount of elements in list")
    
    user_list = create_list_with_arithmetic_progression(start_value, diff, amount)
    print(*user_list)
    return

def main():
    print("\nWelcome to list creation tool!")
    start_value = num.input_int("Enter beginning value of arithmetic progression")
    diff = num.input_int("Enter difference of arithmetic progression")
    amount = num.input_positive_int("Enter amount of elements in list")
    
    user_list = create_list_with_int_arithmetic_progression(start_value, diff, amount)
    print(*user_list)
    return

main_any_numbers()