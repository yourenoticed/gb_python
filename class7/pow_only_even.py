li = [1, 2, 3, 5, 8, 15, 23, 38]
filt = lambda x: x % 2 == 0
result_list = list(zip(filter(filt, li), map(lambda x: x * x, filter(filt, li))))
print(result_list)