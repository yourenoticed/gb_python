def is_prime(num: int) -> bool:
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True

for n in range(1, 100):
    print(f"{n} {is_prime(n)}")