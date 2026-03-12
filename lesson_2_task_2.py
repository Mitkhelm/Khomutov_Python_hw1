def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"
num = int(2028)
result = is_year_leap(num)
print(f"год {num}: {result}")
