import calendar

year = 2025
month = 9

weekday = calendar.weekday(year, month, 1)
print("First day is:", calendar.day_name[weekday])
