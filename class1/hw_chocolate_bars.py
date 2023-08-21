def can_break_chocolate_bars(a: int, b: int, amount_of_bars: int):
    if amount_of_bars >= min(a, b) and\
    amount_of_bars <= a * b:
        return "yes"
    return "no"

print(can_break_chocolate_bars(3, 2, 4))