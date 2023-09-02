def a_to_pow_b(a: int, b: int):
    if b == 0:
        return 1
    return a * a_to_pow_b(a, b - 1)

print(a_to_pow_b(2, 3))