# file for general functions used across the programme

# check a list for duplicates
def check_list_for_duplicates(item, listed_items):
    # make sure a list is present
    if type(listed_items) is not list:
        return

    # return if list is empty
    if len(listed_items) == 0:
        return

    # return true if number in list else return false
    if item in listed_items:
        return True

    return False


# selection sort to sort a list of numbers
def selection_sort(listed_items):
    # get length of list
    list_length = len(listed_items)

    # check if a list is passed in
    if type(listed_items) is not list:
        return

    # check if the list is empty
    if list_length == 0:
        return

    # if list is not empty and more than 1 item
    if list_length > 1:
        for i in range(0, list_length - 1):
            minimum = i
            for j in range(i + 1, list_length):
                if listed_items[j] < listed_items[minimum]:
                    minimum = j
            if minimum != i:
                listed_items[i], listed_items[minimum] = listed_items[minimum], listed_items[i]

    return listed_items


# get amount of matched numbers from two lists
def get_amount_of_matched_numbers(list1, list2):
    counter = 0

    # check if lists present
    if type(list1) is not list or type(list2) is not list:
        return

    # check if lists empty
    if len(list1) == 0 or len(list2) == 0:
        return

    for i in range(len(list1)):
        if list1[i] in list2:
            counter += 1

    return counter


# get prize based on numbers matched, amount of numbers = amount of numbers in original lists
def get_prize(matched_numbers, prizes):
    # check if prizes is a list
    if type(prizes) is not list:
        return

    # check if prizes list is empty
    if len(prizes) == 0:
        return

    if matched_numbers == 0 or matched_numbers == 1:
        return 0

    # sort prize values in ascending order
    sorted_prizes = selection_sort(prizes)

    prize = sorted_prizes[matched_numbers - 2]
    return prize
