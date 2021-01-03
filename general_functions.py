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
