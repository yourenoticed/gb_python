def find_min_max(amount_of_watermelons: int):
    weight = input_number("Enter weight of a watermelon: ")            
    min_weight = weight
    max_weight = weight
    
    for _ in range(1, amount_of_watermelons):
        weight = input_number("Enter weight of a watermelon: ")
        
        if weight > max_weight:
            max_weight = weight
        
        if weight < min_weight:
            min_weight = weight
        
    return min_weight, max_weight


def input_number(msg: str) -> int:
    while True:
        weight = input(msg)
        if weight.isdigit():
            weight = int(weight)
            return weight
    
        else:
            print("Please, enter a number.")

    
def main():
    amount = input_number("Enter amount of watermelons: ")
    print(find_min_max(amount))

    
main()