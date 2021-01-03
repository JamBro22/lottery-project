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
    # user_numbers = []

    i = 1
    while i <= 6:
        number = int(input("Please enter a number from 1 to 49: "))

        if 1 > number or number > 49:
            print("Number must be from 1 to 49")
            continue

        i += 1


get_user_numbers()
