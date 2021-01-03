# add lottery data to file
def add_data_to_file(file_name, mode, list_of_data):
    # make sure file name is a string
    if type(file_name) is not str or type(mode) is not str:
        return

    # make sure param is list
    if type(list_of_data) is not list:
        return

    # check if list is empty
    if len(list_of_data) == 0:
        return

    # open text file
    with open(file_name, mode) as receipt:
        try:
            # iterate through the list of data and write each item to a file
            for item in range(len(list_of_data)):
                receipt.write(list_of_data[item] + "\n")
        finally:
            receipt.close()
