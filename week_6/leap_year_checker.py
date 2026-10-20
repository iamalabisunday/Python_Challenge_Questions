def leap_year(year: int) -> str:
    try:
        numb = int(year)
    except ValueError:
        return "Error"
    
    if numb % 4 == 0 and numb % 100 != 0 or numb % 400 == 0:
        return f"{numb} is a leap year"
    else:
        return f"{numb} is not a leap year"
    
    
year = input("Input: ")
    
print(leap_year(year))