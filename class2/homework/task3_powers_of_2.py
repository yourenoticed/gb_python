def input_number(msg: str) -> int:
    while True:
        user_input = input(msg)
        if user_input.isdigit():
            return int(user_input)
    
        else:
            print("Please, enter a number.")


def print_all_powers_of_2_to_n(n: int):
    k = 0
    
    while 2 ** k <= n:
        print(2 ** k)
        k += 1
    

def main():
    limit = input_number("Enter a limit number: ")
    print_all_powers_of_2_to_n(limit)
    
    
main()