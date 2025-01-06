#==================
# PROBLEM 1
#==================
pet_type = "dog"
pet_name = "Taner"

print(f"I have a {pet_type}, his name is {pet_name}. \n")

#==================
# PROBLEM 2
#==================
first_name = input("What is your first name: ")
current_age = int(input("What is your current age: "))
yearly_savings = int(input("What is your yearly savings: "))

print(f"\nHello {first_name}! You are currently {current_age} years old")
print(f"In 10 years, you will be {current_age + 10}")
print(f"If you save {yearly_savings} each year, in five years you will have saved {yearly_savings * 5}")
print(f"Your average monthly savings is {yearly_savings / 12} \n")

#==================
# PROBLEM 3
#==================
import calendar
from datetime import datetime

# Get month number from datetime
month_number = datetime.now().month
# Based on the month number, get the name of the month from calendar
month_name = calendar.month_name[month_number]
# Get the total days in the month through calendar
days_in_month = calendar.monthrange(datetime.now().year, month_number)[1]
# Calculate the total seconds in the month by multiplying the days in a month by 24 hours, by 60 minutes, by 60 seconds
seconds_in_month = days_in_month * 24 * 60 * 60

print(f"The number of seconds in {month_name} is {seconds_in_month}.  \n")

#==================
# PROBLEM 4
#==================
eggs = int(input("Enter the number of eggs: "))

print(f"\nThis makes {eggs // 12} dozen eggs with {eggs % 12} left over.")
