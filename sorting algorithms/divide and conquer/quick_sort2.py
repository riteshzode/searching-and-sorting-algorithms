
def quicksort(lst):
    if len(lst) < 2:
        return lst

    pivot = lst[len(lst) // 2]
    # pivot = lst[0]  # we can also take 1 value as a pivot

    left = [i for i in lst if i < pivot]
    mid = [i for i in lst if i == pivot]
    right = [i for i in lst if i > pivot]

    return quicksort(left) + mid + quicksort(right)

