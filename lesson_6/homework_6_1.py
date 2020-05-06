# You are given a list in list_1 variable, write a swap_first_last function to return a new list with
# the first and the last elements of the list swapped.
list_1 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]


def swap_first_last(array_1):
    result = array_1.copy()
    result[0], result[-1] = result[-1], result[0]
    return result


result_1 = swap_first_last(list_1)
print(result_1)

# You are given a list in list_2 variable, write a reverse_list function which creates a new list in reversed order.
list_2 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]


def reverse_list(array_2):
    result = array_2.copy()
    result.reverse()
    return result


result_2 = reverse_list(list_2)
print(result_2)

# Create a list which contains only number items and save it to the list_3 variable. Then write multiply_list_items
# function to multiply all the items in a list.
list_3 = [1, 11, 5, 3, 8]


def multiply_list_items(array_3):
    result = 1
    for item in array_3:
        result *= item
    return result


result_3 = multiply_list_items(list_3)
print(result_3)

# Create a list which contains only number items and save it to the list_4 variable. Then write a smallest_item_list
# function to get the smallest number from a list
list_4 = [10, 2, 5, 5, 18]


# def smallest_item_list(array_4):
#     min_1 = min(array_4)
#     return min_1


def smallest_item_list(array_4):
    min_1 = array_4[0]
    for item in array_4:
        if item < min_1:
            min_1 = item
    return min_1


result_4 = smallest_item_list(list_4)
print(result_4)

# Given a list in list_5 variable, write a remove_duplicates_list function to remove duplicates from a list.
list_5 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]


def remove_duplicates_list(array_5):
    result = []
    for item in array_5:
        if not item in result:
            result.append(item)
    return result


result_5 = remove_duplicates_list(list_5)
print(result_5)

# You are given a list in list_6 variable. Enter an integer number and save it to number_1 variable,
# write a longer_words_list function which will return the list of words that are longer than number_1
# from a given list of words.
number_1 = 8
list_6 = ['On', 'it', 'differed', 'repeated', 'wandered', 'required', 'in.', 'Then', 'girl', 'neat', 'why', 'yet',
          'knew', 'rose', 'spot.', 'Moreover', 'property', 'we', 'he', 'kindness', 'greatest', 'be', 'oh', 'striking',
          'laughter.', 'In', 'me', 'he', 'at', 'collecting', 'affronting', 'principles', 'apartments.', 'Has',
          'visitor',
          'law', 'attacks', 'pretend', 'you', 'calling', 'own', 'excited', 'painted.', 'Contented', 'attending',
          'smallness', 'it', 'oh', 'ye', 'unwilling.', 'Turned', 'favour', 'man', 'two', 'but', 'lovers.', 'Suffer',
          'should', 'if', 'waited', 'common', 'person', 'little', 'oh.', 'Improved', 'civility', 'graceful', 'few',
          'smallest', 'screened', 'settling.', 'Likely', 'active', 'her', 'warmly', 'has.']


def longer_words_list(array_6, number1):
    result = []
    for item in array_6:
        if len(item) > number1:
            result.append(item)
    return result


result_6 = longer_words_list(list_6, number_1)
print(result_6)

# Given two lists in list_7 and list_8 variables. Write a function find_item_lists that takes two lists and returns
# True if they have at least one common member.
list_7 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]
list_8 = ['asdasd', True, 8, False, 94, 'Hello world', None, range(1, 11), 100, 1]


def find_item_lists(array_7, array_8):
    result = False
    for item_1 in array_7:
        if item_1 in array_8:
            result = True
    return result


result_7 = find_item_lists(list_7, list_8)
print(result_7)

# You are given a list in list_9 variable. Write a function string_to_list to convert a list of
# characters into a string.
list_9 = ['I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']


def list_to_string(list9):
    result = ''.join(list9)
    return result


result_8 = list_to_string(list_9)
print(result_8)

# Given a list of numbers in list_10 and a number number_2, write count_items_list function which will count number of
# occurrences of x in the given list
list_10 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
number_2 = 3


def count_items_list(array_10, number2):
    result = array_10.count(number2)
    return result


result_9 = count_items_list(list_10, number_2)
print(result_9)

# Given a list of numbers, write a function even_items_list to return new list which include all even numbers in
# given list.
list_11 = [1, 2, 3, 1, 1, 1, 2, 3, 4]


def even_items_list(array_11):
    result = []
    for item in array_11:
        if item % 2 == 0:
            result.append(item)
    return result


result_10 = even_items_list(list_11)
print(result_10)
