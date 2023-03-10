import random


def check_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def bogo_sort(list):
    while not check_sorted(list):
        random.shuffle(list)
    return
