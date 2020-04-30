# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write function counter, which will count how many times your character is included in your string

string_1 = 'Kids want to go back to school'
char_1 = 'o'

def counter(string, char):
    return string.count(char)

result_1 = counter(string_1, char_1)
print(result_1)


# Enter a random number and save it in variable number_1. Then create a function number_multiplication
# that will multiply all the digits together and return the result.

number_1 = 137
def number_multiplication(number):
    index = 0
    result = 1
    num_string = str(number)
    length = len(num_string)
    while index < length:
        result *= int(num_string[index])
        index += 1
    return result

result_2 = number_multiplication(number_1)
print(result_2)

# number_1 = 137
# def number_multiplication(number):
#     result = 1
#     for char in str(number):
#         result *= int(char)
#     return result
#
# result_2 = number_multiplication(number_1)
# print(result_2)


# Enter a random number and save it in variable number_2. Then create function number_reverse which will return
# a number with digits of number_1 in reverse order

number_2 = 123456789
def number_reverse(number):
    num_string = str(number)
    index = len(num_string)
    result = ''
    while index > 0:
        result += num_string[index-1]
        index -= 1
    return int(result)

result_3 = number_reverse(number_2)
print(result_3)
