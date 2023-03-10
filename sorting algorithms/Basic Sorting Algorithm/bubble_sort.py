
def bubble_sort(lst):
    for i in range(len(lst)):
        is_sorted = True
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_sorted = False
        if is_sorted:
            return


# two ways to run for loop in bubble sort
# n = 5
# for i in range(n-1): # we can use n or n-1
#     print(n-1-i)
#
# for i in range(n-1, 0, -1):
#     print(i)
