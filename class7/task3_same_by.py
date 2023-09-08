def same_by(characteristic, objects) -> bool:
    result_list = list(map(characteristic, objects))
    checked_val = result_list[0]
    for value in result_list:
        if value != checked_val:
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')