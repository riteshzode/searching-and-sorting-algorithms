# Approach 1

def merge_sort(lst):
    if len(lst) > 1:

        mid = len(lst) // 2

        left_list = lst[:mid]
        right_list = lst[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        # we can also create merge function outside
        # merge(lst, left_list, right_list) # check the merge.py file

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

# Approach 2

# This is a simple merge function

# def merge(lst, left_list, right_list):
#     # we can also create merge function by below code
#
#     i = j = k = 0
#
#     while i < len(left_list) and j < len(right_list):
#
#         if left_list[i] < right_list[j]:
#             lst[k] = left_list[i]
#             i += 1
#         else:
#             lst[k] = right_list[j]
#             j += 1
#         k += 1
#
#     while i < len(left_list):
#         lst[k] = left_list[i]
#         i += 1
#         k += 1
#
#     while j < len(right_list):
#         lst[k] = right_list[j]
#         j += 1
#         k += 1
