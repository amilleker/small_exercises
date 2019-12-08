list = [3, [4, [4, 5]], 2, [5, 6], 0]
dict = "{3, {4, {4, 5}}, 2, {5, 6}, 0}"


def flatten_list(a_list):
    flat_list = []
    for sublist in a_list:
        try:
            for value in sublist:
                flat_list.append(value)
        except TypeError:
            flat_list.append(sublist)
    return flat_list

def flatten_list2(a_list):
    flat_list = [item for sublist in a_list for item in sublist]
    return flat_list


print(flatten_list2(list))