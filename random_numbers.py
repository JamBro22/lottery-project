# import built-in modules and functions
import random

# import user-defined modules and functions
from general_functions import check_list_for_duplicates, selection_sort


# generate and return a random number between a chosen range
def get_random_number(starting_number, ending_number):
    number = random.randint(starting_number, ending_number)
    return number


# generate a list of random numbers without duplicates
def generate_random_numbers_list(amount_of_numbers, starting_number, ending_number):
    # initialising empty list
    random_numbers = []

    # loop for chosen amount and add randomly generated number to random_numbers list
    i = 1
    while i <= amount_of_numbers:
        number = get_random_number(starting_number, ending_number)

        # check for random_numbers list duplicates
        is_duplicated = check_list_for_duplicates(number, random_numbers)

        # if list contains duplicate, repeat this loop and generate new number
        if is_duplicated:
            continue

        # when there are no duplicates, loop for a new turn and add number to list
        i += 1
        random_numbers.append(number)

    # sort list in ascending order and return
    random_number_list = selection_sort(random_numbers)
    return random_number_list
