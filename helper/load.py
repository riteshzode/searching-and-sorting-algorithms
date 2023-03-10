def load_string(filename):
    """if the input is string file use load_string"""
    list1 = []
    with open(f"{filename}", mode="r") as f1:
        for i in f1.readlines():
            list1.append(i.strip())

    return list1


def load_integer(filename):
    """if the input is integer file use load_integer"""

    list2 = []
    with open(f"{filename}", mode="r") as f1:
        for i in f1.readlines():
            list2.append(int(i))

    return list2
