running_list = []
def fibo(counter, previous_num, current_num, desired_counter):
    if counter == desired_counter:
        return running_list
    else:
        new_sum = current_num + previous_num
        previous_num = current_num
        current_num = new_sum
        running_list.append(current_num)
        return fibo(counter + 1, previous_num, current_num, desired_counter)

desired_counter = input("How many numbers would you like displayed? ")
print(fibo(1, 0, 1, 8))