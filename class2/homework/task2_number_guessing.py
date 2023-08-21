def guess_number(sum:int, multiplication: int):
    for i in range(1001):
        for j in range(1001):
            if i + j == sum and i * j == multiplication:
                return i, j
    print("There is either no such numbers or they're bigger than 1000")

print(guess_number(5, 6))