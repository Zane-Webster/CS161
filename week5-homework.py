### QUESTION 1
## Create a function to return if number is divisible by 5
def divisible_by_five(n):
    ''' Take in number n, determines if divisible by 5, and returns "is" or "is not"'''
    if n % 5 == 0:
        return "is"
    return "is not"

user_number = int(input("Enter a number: "))
print(f"{user_number} {divisible_by_five(user_number)} evenly divisible by 5\n")

### QUESTION 2.1
## Create a dictionary, and use if/elif/else to search by state name to get capital
capitals_by_state = {
    "Oregon": "Salem",
    "California": "Sacramento",
    "Washington": "Olympia",
    "Idaho": "Boise",
    "Montana": "Helena",
    "Nevada": "Carson City"
}

user_state = input("Enter a state: ")

# if user_state in capitals_by_state:
#   print(capitals_by_state[user_state])

# It hurts me to write this like this, but I understand it's to learn if/elif/else

if user_state == "Oregon":
    print(capitals_by_state[user_state])
elif user_state == "California":
    print(capitals_by_state[user_state])
elif user_state == "Washington":
    print(capitals_by_state[user_state])
elif user_state == "Idaho":
    print(capitals_by_state[user_state])
elif user_state == "Montana":
    print(capitals_by_state[user_state])
elif user_state == "Nevada":
    print(capitals_by_state[user_state])
else:
    print("I don't know that state")

### QUESTION 2.2
## Repeat 2.1, but use match case instead of if/elif/else

user_state = input("Enter a state: ")

match user_state:
    case "Oregon":
        print(capitals_by_state[user_state])
    case "California":
        print(capitals_by_state[user_state])
    case "Washington":
        print(capitals_by_state[user_state])
    case "Idaho":
        print(capitals_by_state[user_state])
    case "Montana":
        print(capitals_by_state[user_state])
    case "Nevada":
        print(capitals_by_state[user_state])
    case _:
        print("I don't know that state")

### QUESTION 4
## Create a function that uses elif to set price for public pool entrance

def pool_admission_price(age):
    '''Takes input age, and returns how much pool admission would be according to that age'''
    # If age less than 0, return with error -1
    if age < 0:
        return -1
    # If age younger than 2, return free. $0
    elif age < 2:
        return 0
    # If age between 2 and 11, return $3
    elif age < 12:
        return 3
    # If age between 12 and 60, return $6
    elif age < 61:
        return 6
    # If age over 60, return $4
    else:
        return 4

user_age = int(input("\nEnter age: "))
print(f"The price for the pool at age {user_age} is ${pool_admission_price(user_age)}")

### QUESTION 5
## Determine how many times the string "160" appears in HTML code for coccbobcat.com
import requests
cocc_html_request = requests.get("http://www.coccbobcat.com/")
cocc_html_request_160_occurrences = cocc_html_request.text.count("160")
print(f"The substring '160' appears {cocc_html_request_160_occurrences} times in the HTML source code of http://www.coccbobcat.com/\n")

### QUESTION 6
## Determine the number of processes running on your system and print the result
import psutil

process_count = len(psutil.pids())
print(f"Number of processes running: {process_count}")