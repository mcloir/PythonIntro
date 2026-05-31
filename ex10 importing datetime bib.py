from datetime import datetime, date

now = datetime.now()
print(now)
today = date.today()
print(today)
print(today.year, today.month, today.day)
wasborndate = date(1980, 5, 15)
age = today.year - wasborndate.year
print(age)
