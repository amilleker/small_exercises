array = [["A","B"],["A","C"],["B","D"],["B","C"],["R","M"], ["S"],["P"], ["A"]]
# Write a function that creates a dictionary of how many friends each person has.
# People can have 0 to many friends. However, there won't be repeat relationships like [A,B] and [B,A]
# and neither will there be more than 2 people in a relationship


def get_number_friends(raw_list):
    my_dict = {}
    cleaned_list = []
    for i in raw_list:
        if len(i) == 2:
            cleaned_list.append(i)
    for j in cleaned_list:
        my_dict[j[0]] = my_dict.get(j[0], 0) + 1
        my_dict[j[1]] = my_dict.get(j[1], 0) + 1
    print(my_dict)


print(get_number_friends(array))


