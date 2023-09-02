def input_number(msg: str):
    while True:
        num = input(msg)
        if num.isdigit():
            num = int(num)
            return num

def max_to_min(arr: list):
    max_num = max(arr)
    min_num = min(arr)
    for i in range(len(arr)):
        if arr[i] == max_num:
            arr[i] = min_num

def main():            
    amount = input_number("Enter amount of grades you want to input: ")
    grades = [] # list()

    for _ in range(amount):
        user_input = input_number("Enter a grade: ")
        grades.append(user_input)

    max_to_min(grades)
