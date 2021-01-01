# get user age through input
def get_user_age():
    age = int(input("Please enter your age: "))
    return age


# determine user eligibility/whether they are 18yrs or older
def is_older_than_18(age):
    return True if age >= 18 else False
