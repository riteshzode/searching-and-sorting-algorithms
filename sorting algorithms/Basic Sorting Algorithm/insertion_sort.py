
def insertion_sort(lst):
    for i in range(1, len(lst)):
        pivot = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > pivot:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = pivot
