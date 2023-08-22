def find_unique_values_in_list_of_dicts(list_of_dicts: list[dict]) -> list:
    unique_values = list()

    for dictionary in list_of_dicts:
        for key in dictionary:
            if dictionary[key] not in unique_values:
                unique_values.append(dictionary[key])
    
    return unique_values

            
values = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
    {"VIII": "S007"},
        ]


print(find_unique_values_in_list_of_dicts(values))