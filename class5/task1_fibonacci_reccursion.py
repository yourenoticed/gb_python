# 1, 1, 2, 3, 5, 8, 13, 21 
def find_nth_fib(n):
    if n in [1, 2]:
        return 1
    return find_nth_fib(n - 1) + find_nth_fib(n - 2)

print(find_nth_fib(8))