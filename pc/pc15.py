import datetime

# Note the end of the search at 1582, which was the first year of the Gregorian calendar
for year in range(1582, 2007):
    if datetime.date(year, 1, 1).weekday() == 3:
        if str(year).endswith("6"):
            if year % 4 == 0:
                print(year)
