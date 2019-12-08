texte = "Je m'appelle Arnaud. Comme tous les Arnaud, j'aime le chocolat, la praline et le boudin."


def get_dicts(a_texte):
    words_dict = {}
    new_texte = []
    for i in texte.split():
        cleaned_i = ""
        for char in i:
            if char in '.,':
                char = ''
            cleaned_i += char
        new_texte.append(cleaned_i)
    for j in new_texte:
        words_dict[j] = + words_dict.get(j, 0) + 1
    return words_dict


def get_ordered_list(a_dict):
    my_list = sorted(((v, k) for k, v in a_dict.items()), reverse=True)
    return my_list


print(get_ordered_list(get_dicts(texte)))
