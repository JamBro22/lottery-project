# file for common functions used across the programme

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
