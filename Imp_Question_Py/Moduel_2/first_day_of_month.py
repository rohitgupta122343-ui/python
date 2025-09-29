import calendar

month = 9
year = 2025


weekday = calendar.weekday(year, month, 1)
print("First day is:", calendar.day_name[weekday])
