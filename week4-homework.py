### QUESTION 1
## define function that returns average of 3 numbers
#
# def average_of_three(num1, num2, num3):
#     '''Returns the average of three numbers passed as parameters'''
#     return (num1 + num2 + num3) / 3
#
# print(average_of_three(7, 5, 9))
# print(average_of_three(6, 6, 7))
#
### QUESTION 2
## reorganize average_of_three() and try running
#
# print(average_of_three(7, 5, 9))
# print(average_of_three(6, 6, 7))
#
# def average_of_three(num1, num2, num3):
#     '''Returns the average of three numbers passed as parameters'''
#     return (num1 + num2 + num3) / 3
#
## This program will NOT run because the function average_of_three is called before definition.
#
### QUESTION 3
## try printing local variable and try running
#
# def average_of_three(num1, num2, num3):
#     '''Returns the average of three numbers passed as parameters'''
#     return (num1 + num2 + num3) / 3
#
# print(average_of_three(7, 5, 9))
# print(average_of_three(6, 6, 7))
# print (num1)
#
## This program will NOT run because num1 is not defined globally, so Python will not know what num1 is referencing in the global scope.
#
### QUESTION 4
## create a function that calculates a dog's age into human years

def dog_years_to_human(dog_age):
    '''Take parameter dog_age and convert it into human years'''
    return 24 + (dog_age - 2) * 4

print(f"5 dog years is equivalent to {dog_years_to_human(5)} human years")
print(f"11 dog years is equivalent to {dog_years_to_human(11)} human years\n")

### QUESTION 5
## create a function that calculates the value of a car

def evaluate_car(purchase_price, years_after_purchase, car_nationality):
    '''Calcualates value of a car given purchase price, years after purchase, and car nationality. Accepted nationalities: german, japanese and italian. Assumes percentage change is based only on the principal, and does not compound per year'''
    # map of car nationality to percentage change per year
    car_nationality_map = {"german": -.05, "japanese": -.07, "italian": .05}
    # if input is not valid
    if car_nationality not in car_nationality_map:
        print("Error: only nationalities german, japanese, and italian are accepted")
        return 0
    # calculate amount changed per year
    amount_changed_per_year = purchase_price * car_nationality_map[car_nationality]
    # calculate car value
    return round(purchase_price + (amount_changed_per_year * years_after_purchase), 10)

print(f"The value of a $5000 german car will be ${evaluate_car(5000, 5, 'german')} after 5 years\n")

### QUESTION 6
## create a function that converts dogs age to humans years and return the result

def dog_years_to_human(dog_age):
    '''Take parameter dog_age and convert it into human years'''
    return 24 + (dog_age - 2) * 4

print("Dogs Age Calculator:")
dogs_name = input("What is your dogs name: ")
dogs_age = int(input("How old is your dog: "))
print(f"\nYour dog {dogs_name} is {dog_years_to_human(dogs_age)} human years old.\n")

### QUESTION 7
## create a function to calculate the price of an ice cream cone

def price_for_ice_cream_cone(scoops):
    '''Calculates cost of ice cream cone based on Price = number of scoops x $1.15 + $2.25'''
    return scoops * 1.15 + 2.25

print("Ice Cream Cone Price Calculator:")
scoops = int(input("How many scoops would you like: "))
print(f"\nA {scoops}-scoop ice cream cone will cost ${price_for_ice_cream_cone(scoops)}")