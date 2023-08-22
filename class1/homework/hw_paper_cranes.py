n = 6

def find_amount(n):
    answers = tuple()
    answers += (str(n // 6), )
    answers += (str(n // 6 * 4), )
    answers += (str(n // 6), )
    return answers

answer = " ".join(find_amount(n))
print(answer)