def sum(a: int, b: int):
    if b == 1:
        return 1
    return a + sum(a, b - 1)

print(sum(2, 5))