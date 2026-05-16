# mini bday calculator
from datetime import datetime, timedelta

# enter bday
bday_input = input("When is your birthday? (mm/dd/yyyy)")
# reformat bday
bday_date = datetime.strptime(bday_input, "%d/%m/%Y")
# create time change
time_change = timedelta(days=3)
# calculate new bday
new_bday = bday_date - time_change

print(new_bday)