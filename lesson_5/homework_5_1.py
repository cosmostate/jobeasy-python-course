# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which returns
# value that is equal to your name three times

name_1 = 'Ulyana'

def print_name_three_times(name):
    return name * 3

result_1 = print_name_three_times(name_1)
print(result_1)


# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable

name_2 = 'Ulyana'
number_1 = 3

def print_name_number_times(number, name):
    return name * number

result_2 = print_name_number_times(number_1, name_2)
print(result_2)

# Enter a random string, which includes only digits. Write function sum_digits which find a sum of digits in this string

string_number_1 = '482901645'

def sum_digits(string):
    result = 0
    for char in string:
        result += int(char)
    return result

result_3 = sum_digits(string_number_1)
print(result_3)


# Create function which sums up all even numbers between 2 and 100 (include 100)

def sum_even_numbers():
    result = 0
    for number in range(2, 101, 2):
        result += number
    return result

result_4 = sum_even_numbers()
print(result_4)
