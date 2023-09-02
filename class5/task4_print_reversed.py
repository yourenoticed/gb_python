def print_reversed(amount: int):
    if amount == 0:
        return ""
    num = input("Enter a number: ")
    return f"{print_reversed(amount - 1)} {num}".strip()


print(print_reversed(5))