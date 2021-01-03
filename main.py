# import built-in modules and functions
import sys
from datetime import date

# import user-defined modules and functions
from user_functions import get_user_age, is_older_than_18, get_user_numbers
from random_numbers import generate_random_numbers_list
from general_functions import get_amount_of_matched_numbers, get_prize
from file_handling import add_data_to_file


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
    user_numbers = "Your numbers are: {}".format(user_number_list)
    print(user_numbers)

    # step 4: generate a list of random numbers without duplicates
    # generates 6 random numbers from 1 to 49
    random_numbers_list = generate_random_numbers_list(6, 1, 49)
    random_numbers = "The lotto results are: {}".format(random_numbers_list)
    print(random_numbers)

    # step 5: compare user number list to randomly generated list and return amount of matched numbers
    matched_numbers = get_amount_of_matched_numbers(user_number_list, random_numbers_list)
    matched_amount = "You have matched {} number[s]".format(matched_numbers)
    print(matched_amount)

    # step 6: display both lists, the amount of numbers matched and the prize won
    prize = get_prize(matched_numbers, [10000000, 8584, 2384, 100.50, 20])
    prize_amount = "You have won R{}".format(prize)
    print(prize_amount)

    # step 7: write results to text file
    date_today = str(date.today())
    add_data_to_file("lottery_results.txt", "a", [date_today, user_numbers, random_numbers, matched_amount, prize_amount])


# run only from main file
if __name__ == "__main__":
    main()
