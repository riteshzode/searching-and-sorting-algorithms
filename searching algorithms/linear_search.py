def linear_search(list, value):

    for i in range(len(list)):
        if list[i] == value:
            return i  # return index

    return -1


def verify(answer):
    if answer != -1:
        return f"The answer is in index {answer}"
    else:
        return "The answer is not is list"


# with open("../inputs/numbers/unsorted/10000.txt") as f:
#     x = list(map(int, f.readlines()))
#
# y = linear_search(x, 9229)
# print(f"index No : {y}")
