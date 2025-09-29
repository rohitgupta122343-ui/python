from datetime import date

date1 = date(2025, 5, 17)
date2 = date(2026, 1, 1)

if date1 < date2:
    print("Earlier date:", date1)
else:
    print("Earlier date:", date2)
