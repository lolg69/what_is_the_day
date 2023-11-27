import datetime
from datetime import date

today = date.today()

if today.weekday() == 0:
    print("Eat eggs today and remember to eat poha")
elif today.weekday() == 1:
    print("Eat oats and create music")
elif today.weekday() == 2:
    print("Remember to read today")
elif today.weekday() == 3:
    print("My god only one one day to go then saturday")
elif today.weekday() == 4:
    print("Lyf set")
elif today.weekday() == 5:
    print("Watch ninga hattori")
else:
    print("Watch doremon")
x = datetime.datetime.now()
print(x)