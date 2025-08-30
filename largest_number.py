num_list = [1,8,14,16,18,24]
def largest_number(num_list,max_num):
    if num_list == 1:
        return num_list
    max_num = largest_number(num_list[0:])
    if num_list >= max_num:
        return num_list[0]
    else:
        return max_num