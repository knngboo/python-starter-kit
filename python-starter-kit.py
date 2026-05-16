# dates

# import function from library
from datetime import datetime, timedelta

# call the datetime function
date = datetime.now()
print("The date is: " + str(date))

# create the change in time
time = timedelta(days=1)

# calculate change in time
date2 = date - time
print("Yesterday was: " + str(date2))