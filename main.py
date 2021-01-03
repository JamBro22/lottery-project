# import built-in modules and functions
import sys

# import user-defined modules and functions
from user_functions import get_user_age, is_older_than_18, get_user_numbers
from random_numbers import generate_random_numbers_list


# call all functions in main
def main():
    # display welcome message
    welcome_message = "\nWelcome to Ithuba National Lottery\n"
    print(welcome_message)

    # step 1: get user age
    user_age = get_user_age()

    # step 2: determine whether user is old enough to play (>=18)
    is_old_enough = is_older_than_18(user_age)

    if not is_old_enough:
        message_for_ineligible_players = """
You are not eligible to play Ithuba National Lottery. Players must be 18 years or older
        """
        sys.exit(message_for_ineligible_players)

    # step 3: if old enough, allow user to pick numbers and add to user number list without duplicates
    print("\nYou are eligible to play Ithuba National Lottery.\n")
    # allow user to add 6 numbers from 1 to 49
    user_number_list = get_user_numbers(6, 1, 49)
    print(user_number_list)

    # step 4: generate a list of random numbers without duplicates
    # generates 6 random numbers from 1 to 49
    random_numbers_list = generate_random_numbers_list(6, 1, 49)
    print(random_numbers_list)

    # step 5: compare user number list to randomly generated list and return amount of matched numbers
    # step 6: display both lists, the amount of numbers matched and the prize won
    # step 7: write results to text file, along with prize categories


# run only from main file
if __name__ == "__main__":
    main()
