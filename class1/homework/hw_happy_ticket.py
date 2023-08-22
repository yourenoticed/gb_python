def is_happy(n: int):
    length = len(str(n))
    sum_1, sum_2 = 0, 0
    for _ in range (length // 2):
        sum_1 += n % 10
        n //= 10
    for _ in range (length // 2):
        sum_2 += n % 10
        n //= 10
        
    if sum_1 == sum_2:
        return "yes"
    return "no"

print(is_happy(52343))