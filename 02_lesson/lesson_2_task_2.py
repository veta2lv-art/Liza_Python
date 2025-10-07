def is_year_leap(y):
    return True if y % 4 == 0 else False


y = 2023
year = is_year_leap(y)
print("Год", y, ":", year)
