# import built-in modules and functions
import random

# import user-defined modules and functions
from general_functions import check_list_for_duplicates, selection_sort


# generate and return a random number
def get_random_number(starting_number, ending_number):
    number = random.randint(starting_number, ending_number)
    return number


# generate a list of random numbers without duplicates
def generate_random_numbers_list(amount_of_numbers, starting_number, ending_number):
    random_numbers = []

    i = 1
    while i <= amount_of_numbers:
        number = get_random_number(starting_number, ending_number)

        is_duplicated = check_list_for_duplicates(number, random_numbers)

        if is_duplicated:
            continue

        i += 1
        random_numbers.append(number)

    random_number_list = selection_sort(random_numbers)
    return random_number_list
