# merge two sorted array / list
# Approach 1

def merge_two_sorted_list_1(left_list, right_list):
    # we can also create merge function by below code
    temp = []  # using empty list and appending afterwords

    i = j = 0

    while i < len(left_list) and j < len(right_list):

        if left_list[i] < right_list[j]:
            temp.append(left_list[i])
            i += 1
        else:
            temp.append(right_list[j])
            j += 1

    while i < len(left_list):
        temp.append(left_list[i])
        i += 1

    while j < len(right_list):
        temp.append(right_list[j])
        j += 1

    return temp


# Approach 2

def merge_two_sorted_list_2(left_list, right_list):
    # we can also create merge function by below code
    lst = [0] * (len(left_list) + len(right_list))  # create a list by adding length og both list only containing zero

    i = j = k = 0

    while i < len(left_list) and j < len(right_list):

        if left_list[i] < right_list[j]:
            lst[k] = left_list[i]
            i += 1
        else:
            lst[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        lst[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        lst[k] = right_list[j]
        j += 1
        k += 1

    return lst

#
# l = [6, 7, 8, 9, 10]
# v = [1, 2, 3, 4, 5]
#
# x = merge(l, v)
#
# print(x)
