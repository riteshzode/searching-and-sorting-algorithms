# this is also a famous algorithm name quickselect
# Approach 1
# increase i than swap

def partition1(lst: list, low: int, high: int):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]  # swap i with j

    lst[i + 1], lst[high] = lst[high], lst[i + 1]  # swap i + 1 with pivot ie high
    return i + 1

    # it will give correct index of pivot value
    # all value less than pivot on left side
    # all value greater than pivot on right side

# Approach 2
# swap than increase i

def partition2(lst: list, low: int, high: int):
    pivot = lst[high]
    i = low

    for j in range(low, high):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]  # swap i with j
            i += 1

    lst[i], lst[high] = lst[high], lst[i]  # swap i with pivot ie high
    return i
