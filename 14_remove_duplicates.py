# VERSION ONE - SETS
def remove_duplicates_set(input_list):
    return list(set(input_list))

print(remove_duplicates_set([1, 2, 2, 3, 4, 5, 5]))


# VERSION TWO - FOR LOOP (Modify existing list)
# define the function:
def remove_duplicates_loop_one(input_list):
    # sort the list
    input_list.sort()
    # create temp_item variable
    temp_item = ''
    # loop through items in the list
    for item in input_list:
        if item == temp_item:
            input_list.remove(item)
        temp_item = item
    return input_list

print(remove_duplicates_loop_one([1, 2, 2, 3, 4, 5, 5]))


# VERSION THREE - FOR LOOP (Create new list)
def remove_duplicates_loop_two(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

print(remove_duplicates_loop_two([1, 2, 2, 3, 4, 5, 5]))