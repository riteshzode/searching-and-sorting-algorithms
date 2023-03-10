def merge_sort(lst, low, high):
    if low < high:
        mid = low + (high - low) // 2
        # mid = (high + low) // 2

        merge_sort(lst, low, mid)
        merge_sort(lst, mid + 1, high)

        merge(lst, low, mid, high)
        # inplace
        # return lst  # return


def merge(lst, l, m, h):
    # created both lists
    left_list = lst[l:m + 1]
    right_list = lst[m + 1: h + 1]
    i = j = 0
    k = l

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
