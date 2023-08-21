def how_long_will_the_ride_take(kms_per_day: int, total_kms: int):
    return int((total_kms - 1) / kms_per_day + 1)

print(how_long_will_the_ride_take(700, 700))