def how_many_carriages_in_train(num_from_head: int, car_num: int):
    if num_from_head == car_num:
        return "Can't count how many carriages there are, not enough information"
    else:
        return num_from_head + car_num - 1 
    
print(how_many_carriages_in_train(3, 3))