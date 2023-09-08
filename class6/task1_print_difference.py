from numbers_input import number_input as num

def find_difference(arr1: list, arr2: list) -> list:
    diff_list = list()
    for value in arr1:
        if value not in arr1:
            diff_list.append(value)
            
    return diff_list


def main():
    amount1 = num.input_positive_int("Enter amount of elements you want to put in 1st array")
    arr1 = list()
    for _ in range(amount1):
        arr1.append(input("Enter a value: "))
        # not making a value an int because it makes more sense and more usable
        
    amount2 = num.input_positive_int("Enter amount of elements you want to put in 2nd array")    
    arr2 = list()
    for _ in range(amount2):
        arr2.append(input("Enter a value: "))
        
    print(f'\narr1: {arr1}')
    print(f'arr2: {arr2}')
    
    difference = find_difference(arr1, arr2)
    print(f'Difference list: {difference}')