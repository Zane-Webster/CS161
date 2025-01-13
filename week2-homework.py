########## USING BIN/HEX IN PYTHON
### QUESTION 1
## set variable x, and print out it's value in dec, binary and hex
# x = 31
#
# print (x, bin(x), hex(x))
#
### QUESTION 2
## set variable x to a float instead of int
# x = 1.825
#
# print (x, bin(x), hex(x))
## received an error due to bin() and hex() requiring an integer as the input

### QUESTION 3
# set variables to bin and hex values
# y = 0b1011
# z = 0xA3
#
# print(y, z)
#
### QUESTION 4
## seems to be a typo. this question is a repeat of question 3
#
### QUESTION 5
## output the sum of decimal x, binary y and hexadecimal z
# w = x + y + z
# print ('the sum is: ', w)
#
########## COMPRESSION
def percentage_of_comp(p_original_size, p_dictionary_size, p_compressed_size):
    return round(1 - ((p_compressed_size + p_dictionary_size) / p_original_size), 4) * 100

original_text_size = int(input("Enter the size of the original text: "))
dictionary_size = int(input("Enter the size of the dictionary: "))
compressed_size = int(input("Enter the size of the compressed text: "))

print(f"Compressed text size: {compressed_size}\n"
      f"     Dictionary size: {dictionary_size}\n"
      f"               Total: {compressed_size + dictionary_size}\n"
      f"  Original text size: {original_text_size}\n"
      f"         Compression: {percentage_of_comp(original_text_size, dictionary_size, compressed_size)}%")