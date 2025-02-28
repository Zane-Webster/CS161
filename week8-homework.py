### QUESTION 1
## have user enter the same string twice, first in lower case, then in upper case, if they match, return "Stop shouting please!"
q1_lower = input("Enter a phrase in lowercase: ")
q1_upper = input("Enter the same phrase in uppercase: ")

# if q1_lower matches q1_upper when converted to uppercase, tell user to stop shouting
if q1_lower.upper() == q1_upper:
    print("Stop shouting please! \n")

### QUESTION 2
## take user input string, return number of unique vowels

q2_str = input("Enter a string: ")

# store vowels in an array, and create a set to count unique vowels
vowels = ['a','e','i','o','u']
unique_vowels = set()

# iterate through string, if letter is vowel, add to unique vowels set
for i in range(len(q2_str)):
    if q2_str[i].lower() in vowels:
        unique_vowels.add(q2_str[i])

print(f"{q2_str} has {len(unique_vowels)} unique vowel(s) in it \n")

### QUESTION 3
## take 2 strings, and return which string comes first in alphabetical order

q3_str1 = input("Enter a string: ")
q3_str2 = input("Enter a different string: ")

# using relational operators, print which string comes first alphabetically
if q3_str1 < q3_str2:
    print(f"{q3_str1} comes before {q3_str2} \n")
if q3_str1 > q3_str2:
    print(f"{q3_str2} comes before {q3_str1} \n")
if q3_str1 == q3_str2:
    print(f"{q3_str1} is the same as {q3_str2} \n")

### QUESTION 4
## have user input email, have them repeat email, if they match say "Thank you!, else make them try again

def enter_email():
    email = input("Enter your email: ")
    # if second email matches, say thank you and exit
    if input("Enter your email again: ") == email:
        print("Thank you! \n")
    # otherwise, call enter_email() again until it matches
    else:
        print("The two inputs did not match. Try again \n")
        enter_email()

enter_email()

### QUESTION 5
## make an iterative and recursive function that will calculate the factorial of a number. measure using time package
import time

def iterative_factorial(n):
    # if user enters 0 or negative number, return 0
    if n <= 0:
        return 0
    total = 1
    # iterate through range 2 to n+1, multiplying the previous total with the current iteration. start on 2 because total is already 1 and multiplying by 1 doesn't do anything
    for i in range(2, n+1):
        total = total * i
    return total

def recursive_factorial(n, total=1):
    # if user enters 0 or negative number, return 0
    if n <= 0:
        return 0
    # if n is greater than 1, multiply the current total by n
    if n > 1:
        total = total * n
    # otherwise, if n is 1, return the total
    else:
        return total

    # recursively call function, subtracting 1 from n
    return recursive_factorial(n-1, total)

q5_number = int(input("Enter a number: "))

# get start time
start = time.perf_counter_ns()
# run number iteratively
iterative_factorial(q5_number)
# get stop time
stop = time.perf_counter_ns()

# measure iterative time
iterative_time = stop - start

# get start time
start = time.perf_counter_ns()
# run number recursively
recursive_factorial(q5_number)
# get stop time
stop = time.perf_counter_ns()

# measure recursion time
recursive_time = stop - start

print(f"Calculating {q5_number}! takes: \n{iterative_time} nanoseconds iteratively \n{recursive_time} nanoseconds recursively \n")

### RESULTS
# 3! takes: 4200ns iteratively, 2000ns recursively
# 10! takes: 4900ns iteratively, 3100ns recursively
# 25! takes: 5900ns iteratively, 19900ns recursively
#
# from these results we see that with smaller inputs, recursion is faster than iteration
# but with larger inputs, iteration is faster than recursion
###
