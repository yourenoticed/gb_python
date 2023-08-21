def is_year_leap(year: int):
    if year % 100 == 0 and year % 400 != 0:
        return "no"
    elif year % 4 == 0:
        return "yes"
    
for year in range(1600, 2008, 4):
    print(f"{year} {is_year_leap(year)}")