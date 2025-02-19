### QUESTION 1
## input user low n and high n, then print all even numbers between the user inputs

q1_user_low = int(input("Enter the lower number: "))
q1_user_high = int(input("Enter the higher number: "))

q1_even_numbers = []
# iterate over range of user numbers, adding one to the high to make sure we include the high number
for i in range(q1_user_low, q1_user_high+1):
    # if the current number is divisible by 2, it is even, add it to array
    if i % 2 == 0:
        q1_even_numbers.append(i)

print(f"The even numbers between {q1_user_low} and {q1_user_high} are: {q1_even_numbers}\n")

### QUESTION 2
## iterate to find all factors of user number

q2_num = int(input("Enter a positive integer: "))

q2_factors = []
# iterate from 1 to the user input, add one to the high to include user input
for i in range(1, q2_num+1):
    # if the user input is divisible by i, it is a factor
    if q2_num % i == 0:
        q2_factors.append(i)

print(f"The factors of {q2_num} are: {q2_factors}\n")

### QUESTION 3
## given array alphabet, take user input and add index of each letter in name

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

q3_name = input("Enter your name: ")

q3_total = 0
# for each letter in the users name, find the index at which each value lies
for i in range(len(q3_name)):
    if q3_name[i] in alphabet:
        # add the index to the total
        q3_total += alphabet.index(q3_name[i])

print(f"{q3_total}\n")

### QUESTION 4
## use recursion to print squares of all integers from 1->user input, e.g. input = 4, return 1, 2, 9, 16

def recursive_square(n, i=1):
    '''
    prints squares up to of number input (e.g. n = 4, return 1,2,9,16)
    :param n: max limit of squares
    :param i: internal int that tracks current number
    '''

    # print current square
    print(i*i)

    # if i == n, exit function
    if i == n:
        return

    # otherwise, call recursion, adding 1 to i
    recursive_square(n, i + 1)

q4_max_number = int(input("Enter a positive integer: "))

if q4_max_number > 0:
    recursive_square(q4_max_number)

print('\n')

### QUESTION 5
## create a teepee sort, where highest number is in the center. left side should contain increasing odd numbers, right side should contain decreasing even numbers

def teepee_sort(array):
    '''
    creates array with highest number in the center, with odd numbers increasing on left and even numbers decreasing on right
    :param array: unsorted array
    :return: teepee sorted array
    '''

    # create arrays for even numbers and odd numbers
    even_array = []
    odd_array = []

    # find the highest number in the array
    highest_number = max(array)

    # remove the highest number as to not sort it
    array.remove(highest_number)

    # sort all numbers in array into even and odd
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_array.append(array[i])
            continue
        odd_array.append(array[i])

    # sort the odd array increasing
    odd_array.sort()

    # sort the even array decreasing
    even_array.sort(reverse=True)

    # return odd array first (* unpacks array), then highest number, then even array
    return [*odd_array, highest_number, *even_array]

q5_array = [12, 43, 22, 34, 2, 21, 3, 33, 81]

print(f"{teepee_sort(q5_array)} \n")

### QUESTION 6
## given an arrangement of the digits 0-9, find the next highest arrangement

def next_highest(n):
    '''
    Takes a number with the digits 0-9 exactly once in any order, and returns the next highest number that can be created with the same 10 digits
    :param n: a number with numbers 0-9 exactly once in any order
    :return: the next highest number
    '''

    # turn the number into an array of digits by converting to string, then getting length
    array_of_n = [int(x) for x in str(n)]

    # get last digit index of the array
    last_index = len(array_of_n) - 1

    # find the pivot, where the
    def find_pivot(p_array_of_n, p_last_index):
        # if the last index is 0, there is no higher number
        if p_last_index == 0:
            return -1

        # see if the digit to the left of the current last_index is less than the last_index, if it is, it's the highest number
        if p_array_of_n[p_last_index - 1] < p_array_of_n[p_last_index]:
            return p_last_index - 1

        # recursively call until pivot is found
        return find_pivot(p_array_of_n, p_last_index - 1)

    pivot = find_pivot(array_of_n, last_index)

    # if no pivot is found, the number is the highest it can be (9876543210)
    if pivot == -1:
        return "NO HIGHER NUMBER FOUND"

    # find the smallest digit to the right of the pivot
    def find_successor(p_array_of_n, pivot, p_last_index):
        # if the last index is greater than the pivot, return the last index
        if p_array_of_n[p_last_index] > p_array_of_n[pivot]:
            return p_last_index

        # recursively call until successor is found
        return find_successor(p_array_of_n, pivot, p_last_index - 1)

    successor = find_successor(array_of_n, pivot, last_index)

    # swap the pivot and the successor
    array_of_n[pivot], array_of_n[successor] = array_of_n[successor], array_of_n[pivot]

    # reserve everything after the successor
    def reverse(array_of_n, start, end):
        if start < end:
            array_of_n[start], array_of_n[end] = array_of_n[end], array_of_n[start]
            reverse(array_of_n, start + 1, end - 1)

    # reverse the end of the number
    reverse(array_of_n, pivot + 1, last_index)

    # recombine into int by using strings
    return int("".join(map(str, array_of_n)))

q6_number = int(input("Enter a positive integer with all digits 0-9 each used exactly once: "))

print(f"The next highest number after {q6_number} is {next_highest(q6_number)} \n")