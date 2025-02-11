### QUESTION 1
## using a while loop, take user input and count down from the number given
from functools import partial

def blast_off(start_n):
    '''Takes parameter positive integer "start number".
       Function then prints number, and subtracts one (counting down) until the number reaches 0, at which point it will print "blastoff!"'''

    # if number is greater than 0, subtract one and call function recursively
    while start_n > 0:
        print(start_n)
        start_n -= 1
    # if number is equal to 0, then blastoff!
    print('blastoff!\n')

user_number = int(input("Enter a positive integer: "))
blast_off(user_number)

### QUESTION 2
## modify the function above to print if a number is even or odd

def blast_off_with_parity(start_n):
    '''Takes parameter positive integer "start number".
       Function then prints number, and subtracts one (counting down) until the number reaches 0, at which point it will print "blastoff!".
       Prints whether the integer is even or odd at each step.'''

    parity = ""

    # if number is greater than 0, subtract one and call function recursively
    while start_n > 0:
        # if number is divisible by 2, parity is even
        if start_n % 2 == 0:
            parity = "Even"
        # else, parity is odd
        else:
            parity = "Odd"
        print(f"{start_n} is {parity}")
        start_n -= 1
    # if number is equal to 0, then blastoff!
    print('blastoff!\n')

blast_off_with_parity(user_number)

### QUESTION 3
## modify the function above to allow the user to change the subtraction amount

def blast_off_with_custom_decrease(start_n, decrease):
    '''Takes parameter positive integer "start number".
       Takes parameter positive integer "decrease".
       Function then prints number, and subtracts the decrease amount (counting down) until the number reaches 0, at which point it will print "blastoff!".
       Prints whether the integer is even or odd at each step.'''

    parity = ""

    # if number is greater than 0, subtract one and call function recursively
    while start_n > 0:
        # if number is divisible by 2, parity is even
        if start_n % 2 == 0:
            parity = "Even"
        # else, parity is odd
        else:
            parity = "Odd"
        print(f"{start_n} is {parity}")
        start_n -= decrease
    # if number is equal to 0, then blastoff!
    else:
        print('blastoff!\n')

user_decrease_amount = int(input("Enter how much you want the countdown to decrease by each step: "))
blast_off_with_custom_decrease(user_number, user_decrease_amount)

### QUESTION 4.1
## using a while loop, take user string until string is less than 5 characters

user_string = input("Enter a word: ")
string_length = len(user_string)
print(f"{user_string} has {string_length} letters")

while (string_length >= 5):
    user_string = input("Enter a word: ")
    string_length = len(user_string)
    print(f"{user_string} has {string_length} letters")

print("Goodbye\n")

### QUESTION 4.2
## repeat step 4.1, adding a counter that calls the user a loser if they try 5 times and don't enter a word less than 5 characters

user_string = input("Attempt 1 | Enter a word: ")
string_length = len(user_string)
print(f"{user_string} has {string_length} letters")

user_attempts = 1
exit_message = "Goodbye"

while (string_length >= 5):
    user_attempts += 1
    if user_attempts > 5:
        exit_message = "Loser!"
        break
    string_length = len(input(f"Attempt {user_attempts} | Enter a word: "))
    print(f"{user_string} has {string_length} letters")

print(f"{exit_message}\n")

### QUESTION 5
## create a while loop that counts from 10 to 100 in dec, bin and hex
q5_number = 10
while q5_number <= 100:
    print(f"{q5_number} | {bin(q5_number)} | {hex(q5_number)}")
    q5_number += 1

### QUESTION 6
## create two functions to print stars equal to the input amount, decreasing by one and printing the amount of stars. one function iteratively, one function recursively

def iterative_triangle_printer(start_n):
    '''Takes parameter positive integer "start number".
       Prints stars equal to the number, then decreases by one and repeats.
       Uses iteration'''
    for i in reversed(range(start_n+1)):
        print("*" * i)
        i -= 1

def recursive_triangle_printer(start_n):
    '''Takes parameter positive integer "start number".
       Prints stars equal to the number, then decreases by one and repeats.
       Uses recursion'''
    if start_n > 0:
        print("*" * start_n)
        start_n -= 1
        recursive_triangle_printer(start_n)

q6_user_number = int(input("\nEnter a positive integer: "))
iterative_triangle_printer(q6_user_number)
recursive_triangle_printer(q6_user_number)

### EXTRA CREDIT 1
## write a recursive function that takes a positive integer and returns the sum of it's digits

import math

def sum_of_digits(number, total=0):
    '''Takes parameter number, then adds the sum of its digits'''
    # marks the digit breaks (2 digits, 3 digits, 4 digits, 5 digits, etc.)
    digit_breaks = [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]

    # gets the length of the current number, and subtracts by 2 to get the current highest digit break
    # e.g. if number == 1000, then length of number is 4, so to match the digit_breaks array, you subtract by 2 to get current highest digit break, which is the second index of the array
    current_digit_break = len(str(number))-2

    # if the current digit break is -1, that means the number is now single digit. add the last single digit number to the total, print the number and end recursion by returning the function
    if current_digit_break == -1:
        total += number
        print(f"Sum of digits is {total}")
        return

    # take the number, divide by the current digit break, and floor it to get the isolated digit value, then add to total
    # e.g. if number == 1234, divide by digit break (1000), to get 1.234, then floor to get 1 and add to total
    total += math.floor(number / digit_breaks[current_digit_break])

    # subtract number by the same math above, but multiply by the current digit break to get the proper digit break
    # e.g. if number == 3234, do the same math to get 3, then multiply by digit break (1000) to get 3000, and subtract this from the current number to get 234
    number -= math.floor(number / digit_breaks[current_digit_break]) * digit_breaks[current_digit_break]

    # call function recursively until the if statement above stops the function
    sum_of_digits(number, total)

ec1_number = int(input("\nEnter a positive integer: "))
sum_of_digits(ec1_number)

### EXTRA CREDIT 2
## write a recursive function that takes a strings and returns whether that string is a palindrome

def is_palindrome(string):
    '''Takes parameter string, and returns whether string is a palindrome'''
    # if the string is one letter or zero letters, then the string is a palindrome
    if len(string) < 2:
        return True

    # if the first and last characters match, slice the first and last characters and call recursively
    if string[0] == string[-1]:
        # slice the first letter
        string = string[1:]
        # slice the last letter
        string = string[:-1]
        # return the current string
        return is_palindrome(string)

    # if not under 2 letters, and not matching first and last letters, return false
    return False

ec2_input = input("\nEnter a string: ")
ec2_input_is_palidrome = is_palindrome(ec2_input)
if ec2_input_is_palidrome:
    print(f"Yes, {ec2_input} is a palindrome")
else:
    print(f"No, {ec2_input} is not a palindrome")
