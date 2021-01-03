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
        # get first number
        for i in range(0, list_length - 1):
            # set minimum to lowest number
            minimum = i
            # get second number
            for j in range(i + 1, list_length):
                # if j is more, set minimum to j
                if listed_items[j] < listed_items[minimum]:
                    minimum = j
            # if minimum is not i, switch number positions
            if minimum != i:
                listed_items[i], listed_items[minimum] = listed_items[minimum], listed_items[i]

    # return sorted list
    return listed_items


# get amount of matched numbers from two lists
def get_amount_of_matched_numbers(list1, list2):
    # initialise counter
    counter = 0

    # check if lists present
    if type(list1) is not list or type(list2) is not list:
        return

    # check if lists empty
    if len(list1) == 0 or len(list2) == 0:
        return

    # iterate through list1 and add to counter if item is in list2
    for i in range(len(list1)):
        if list1[i] in list2:
            counter += 1

    # return the counter as amount of matched numbers
    return counter


# get prize based on numbers matched, amount of numbers = amount of numbers in original lists
def get_prize(matched_numbers, prizes):
    # check if prizes is a list
    if type(prizes) is not list:
        return

    # check if prizes list is empty
    if len(prizes) == 0:
        return

    # return 0 if no numbers or 1 number matched
    if matched_numbers == 0 or matched_numbers == 1:
        return 0

    # sort prize values in ascending order
    sorted_prizes = selection_sort(prizes)

    # get relevant prize and return it
    prize = sorted_prizes[matched_numbers - 2]
    return prize
