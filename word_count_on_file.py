

def get_dict(a_file):
    word_count_dict = {}
    pokemon_file = open(a_file, "r+")
    for word in pokemon_file.read().split():
        if word not in word_count_dict:
            word_count_dict[word.lower()] = word_count_dict.get(word.lower(), 0) + 1
    return word_count_dict


def order_dict(a_dict):
    sorted_word_count_dict = [sorted(((v, k) for k, v in a_dict.items()), reverse=True)]
    return sorted_word_count_dict


def value_from_dict(a_dict, my_value):
    number_of_value = a_dict.get(my_value, 0)
    return number_of_value


if __name__ == "__main__":
    my_dict = get_dict("pokemon.txt")
    my_order_dict = order_dict(my_dict)
    nb_of_value = value_from_dict(my_dict, 'you')
    print(nb_of_value)
