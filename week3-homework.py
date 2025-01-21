### QUESTION 1
## input variable user_name, then output result
user_name = input("Enter your name: ")
print("Hello " + user_name)

### QUESTION 2
## input variable user_age, then output their age in 5 years
user_age = input("\nEnter your age: ")
# print(user_age + 5) this will give an error because user_age is a string, and you cannot add an integer (5) to a string
print("You will be " + str(int(user_age) + 5) + " in 5 years")

### QUESTION 3
## input variable user_age_addition, then output their age after age addition
user_age_addition = input("\nHow many years should be added to your age: ")
                                                           # convert both variables to integers, then convert the added result into a string
print("In " + user_age_addition + " years, you will be " + str(int(user_age) + int(user_age_addition)) + " years old")

### QUESTION 4
## input variable user_hours_worked and variable user_hourly_wage, and convert both into floats
user_hours_worked = float(input("\nEnter the number of hours worked: "))

# put the $ in the question so users would not try to add it themselves
user_hourly_wage = float(input("Enter your hourly wage: $"))

### QUESTION 5
## calculate and output users weekly paycheck (round to 6 digits)
print("Your gross income this week is $" + str(round((user_hours_worked * user_hourly_wage), 6)))
## calculate and output users annual salary
print("Your gross annual pay will be $" + str((user_hours_worked * user_hourly_wage) * 50))