from numbers_input import number_input as num

def filter_indexes(arr: list, range_start, range_end) -> list[int]:
    indexes = list()
    for i, val in enumerate(arr):
        if val >= range_start and val <= range_end:
            indexes.append(i)
    return indexes


def main():
    amount = num.input_positive_int("Enter amount of values you want to input")
    array = list()
    
    for _ in range(amount):
        array.append(num.input_any_number("Enter a value"))    
    
    start = num.input_any_number("\nEnter filter start range")
    end = num.input_any_number("Enter filter end range")
    filtered_ind = filter_indexes(array, start, end)
    
    print(filtered_ind)
    
main()