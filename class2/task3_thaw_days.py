def thaw_days(days_amount: int):
    longest_thaw_streak = 0
    curr_thaw_streak = 0
    for _ in range(days_amount):
        while True:
            temperature = input("Enter temperature in Celcius: ")
            if temperature[0] == '-' and temperature[1:].isdigit():
                temperature = int(temperature)
                break
        
            if temperature.isdigit():
                temperature = int(temperature)
                break
                
            else:
                print("Please, enter a number.")
        
        if temperature > 0:
            curr_thaw_streak += 1
        
        else:
            if longest_thaw_streak < curr_thaw_streak:
                longest_thaw_streak = curr_thaw_streak
                curr_thaw_streak = 0
                
    return longest_thaw_streak

def main():
    while True:
        days_amount = input("Enter amount of days: ")
        if days_amount.isdigit():
            days_amount = int(days_amount)
            break
        
        else:
            print("Please, enter a number")

    print(thaw_days(days_amount))

main()