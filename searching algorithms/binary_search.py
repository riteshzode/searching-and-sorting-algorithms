# iterative method

def binary_search_iterative(lst, target):
    """ This is binary search function """
    left = 0
    right = len(lst) - 1

    while left <= right:

        mid = left + (right - left) // 2
        # mid = right + left //2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# recursive method


def binary_search_recursive(lst, left, right, target):
    """ This is binary search function """

    if left > right:
        return -1

    mid = left + (right - left) // 2
    # mid = right + left //2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, left, mid - 1, target)
    else:
        return binary_search_recursive(lst, mid + 1, right, target)


# verify function

def verify(answer):
    if answer != -1:
        return f"The answer is in index {answer}"
    else:
        return "The answer is not is list"


# with open("../inputs/numbers/sorted/10000.txt") as f:
#     x = list(map(int, f.readlines()))
#
# y = binary_search_recursive(x, 0, len(x) - 1, 2)
# print(f"index No : {y}")

