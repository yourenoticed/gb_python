def find_fibonacci_index(n: int) -> int:
    """ if n == 0:
        return 1
    if n == 1:
        return 2 """
    
    fib_1 = 0
    fib_2 = 1
    index = 2
    while n > fib_2:
        temp = fib_2
        fib_2 += fib_1
        fib_1 = temp
        index += 1
        
    if n == fib_2:
        return index
    
    return -1

print(find_fibonacci_index(8))