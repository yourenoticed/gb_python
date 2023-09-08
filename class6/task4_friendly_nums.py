def find_friendly_nums(control_num: int) -> list[int]:
    result = list()
    for num1 in range(control_num - 1):
        div_sum_1 = 0
        for div in range(1, num1):
            if num1 % div == 0:
                div_sum_1 += div
        
        div_sum_2 = 0
        for num2 in range(num1 + 1, control_num):
            for div in range(1, num2):
                if num2 % div == 0:
                    div_sum_2 += div
        
        if div_sum_1 == div_sum_2:
            result.append([])
                