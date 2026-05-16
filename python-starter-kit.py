print("\nHello, King Boo speaking...\nThis is going to be a long python file!\nI hope you enjoy the ride!")

from datetime import datetime, timedelta

# date calculations
print("\n==== DATE CALCULATIONS ====")
current_date = datetime.now()
print("Today is " + str(current_date))

one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday was: " + str(yesterday))

one_week = timedelta(weeks=1)
last_week = current_date - one_week
print("Last week was: " + str(last_week))

# date formatting
print("\n==== DATE FORMATTING ====")
print("Today's month: " + str(current_date.month))
print("Today's day: " + str(current_date.day))
print("Today's year: " + str(current_date.year))
print("Today's hour: " + str(current_date.hour) + " o'clock!")
print("Today's minute: " + str(current_date.minute) + " minute(s) in!")
print("Today's second: " + str(current_date.second) + " second(s) in!")
bday = input("Please enter your birthday (mm/dd/yyyy): ")
print("You entered: " + str(bday))
formatted_bday = datetime.strptime(bday, "%m/%d/%Y")
print("Your validated bday is: " + str(formatted_bday))
print("Week before your bday: " + str(formatted_bday - one_week))

# error handling
print("\n==== ERROR HANDLING ====")
x = 32
y = 54
z = 0
if x < y:
    print(str(x) + " is less than " + str(y))
try:
    print(x / z)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero.")
else:
    print("Something else went wrong.")
finally:
    print("This is our cleanup code.")