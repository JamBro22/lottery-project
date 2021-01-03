# import user-defined modules
from general_functions import check_list_for_duplicates


# get user age through input
def get_user_age():
    try:
        age = int(input("Please enter your age: "))
        return age
    except ValueError:
        print("Must be a number")
        return get_user_age()


# determine user eligibility/whether they are 18yrs or older
def is_older_than_18(age):
    try:
        return True if age >= 18 else False
    except TypeError:
        print("Must be a number")
        age = get_user_age()
        return is_older_than_18(age)


# return a list of non-duplicated user chosen numbers
def get_user_numbers():
    user_numbers = []

    i = 1
    while i <= 6:
        try:
            number = int(input("Please enter a number from 1 to 49: "))

            is_duplicated = check_list_for_duplicates(number, user_numbers)

            if is_duplicated:
                print("Number already chosen")
                continue

            if 1 > number or number > 49:
                print("Number must be from 1 to 49")
                continue

            i += 1
            user_numbers.append(number)
        except ValueError:
            print("Must be a number")
            continue

    user_numbers.sort()
    return user_numbers

