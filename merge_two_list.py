a = [1, 2, 3, None, None]
b = [4, 5, 3]


def get_longest_list(list_a, list_b):
    if len(list_a) > len(list_b):
        return len(list_a)
    else:
        return len(list_b)


def get_merged_list(list_a, list_b):
    count = get_longest_list(list_a, list_b)
    solutions=[]
    for i in range(count):
        try:
            solutions.append(list_a[i])
        except IndexError:
            pass
        try:
            solutions.append(list_b[i])
        except IndexError:
            pass
    return solutions


def remove_none(a_list):
    new_list = []
    for i in a_list:
        if i != None :
            new_list.append(i)
    return new_list


print(remove_none(get_merged_list(a,b)))