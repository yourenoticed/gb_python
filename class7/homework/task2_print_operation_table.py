def print_operation_table(operation, rows_num = 6, cols_num = 6):
    for i in range(1, rows_num + 1):
        line = list()
        for k in range(1, cols_num + 1):
            line.append(operation(i, k))
        print(*line, sep="\t")
        
print_operation_table(lambda x, y: x * y)
        