# import user-defined modules
from general_functions import check_list_for_duplicates, selection_sort


# get user age through input
def get_user_age():
    try:
        # allow user to input age and return if no exceptions
        age = int(input("Please enter your age: "))
        return age
    except ValueError:
        # account for Value Error and let user know that the chosen value must be a number
        # call function again
        print("Must be a number")
        return get_user_age()


# determine user eligibility/whether they are 18yrs or older
def is_older_than_18(age):
    try:
        return True if age >= 18 else False
    except TypeError:
        # account for type error and let user know the value must be a number
        # call function again
        print("Must be a number")
        age = get_user_age()
        return is_older_than_18(age)


# return a list of non-duplicated user chosen numbers
def get_user_numbers(amount_of_numbers, starting_number, ending_number):
    # initialising empty list
    user_numbers = []

    # loop for a chosen amount of times/ amount of lottery numbers
    i = 1
    while i <= amount_of_numbers:
        try:
            # allow user to choose numbers within a chosen range
            number = int(input("Please enter a number from {} to {}: ".format(starting_number, ending_number)))

            # check if the chosen number is already in the list user_numbers
            is_duplicated = check_list_for_duplicates(number, user_numbers)

            # if the number is in the list, repeat the current loop and get a new number
            if is_duplicated:
                print("Number already chosen")
                continue

            # ensure that the chosen number is within the chosen range, if not, repeat loop to get new number
            if starting_number > number or number > ending_number:
                print("Number must be from {} to {}".format(starting_number, ending_number))
                continue

            # if the number is valid, add to list and loop for a new turn
            i += 1
            user_numbers.append(number)
        except ValueError:
            # account for value error, letting user know the value must be a number, repeat loop
            print("Must be a number")
            continue

    # sort and return list
    user_number_list = selection_sort(user_numbers)
    return user_number_list

