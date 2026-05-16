# date formatting
from datetime import datetime

# store the current date in a variable
date = datetime.now()

# individually print the data
print("The month is: " + str(date.month))
print("The day is: " + str(date.day))
print("The year is: " + str(date.year))