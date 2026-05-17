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

# conditionals
print("\n==== CONDITIONALS ====")
print("Welcome to your math/personality quiz. Please answer all questions and aim for an A+!\nYours truly, King Boo")
x = input("Please choose an x value: ")
y = input("Please choose an y value: ")
z = input("Please choose an z value: ")
pi = 3.14
question1 = "What is " + str(x) + " * " + str(y) + "? "
question2 = "Do you like Minecraft? "
question3 = "What is (" + str(pi) + " - " + str(z) + ")/(" + str(x) + ")? "
question4 = "Do you like computers? "
question5 = "How many questions were in this quiz? "
secret_question = "Hello, what's your name? "

null = input("Please press enter to continue:")
name = input(secret_question)
print("Thank you for sharing! Next question!")
answer1 = input(question1)
answer2 = input(question2)
answer3 = input(question3)
answer4 = input(question4)
answer5 = input(question5)
null = input("AWESOME! Now let's see your results! Please press enter:")
point1 = 0
point2 = 0
point3 = 0
point4 = 0
point5 = 0
point6 = 0

if float(answer1) == int(x) * int(y):
    point1 = 1
else:
    pass

if answer2 == "yes":
    point2 = 1
else:
    pass

if float(answer3) == (int(pi) - int(z)) / int(x):
    point3 = 1
else:
    pass

if answer4 == "yes":
    point4 = 1
else:
    pass

if int(answer5) == 6:
    point5 = 1
else:
    pass
   
average = ((point1 + point2 + point3 + point4 + point5 + point6) / 6) * 100
print(average)