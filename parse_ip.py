texte = """this is an IP adress 192.168.0.1/16 and
here is another one 112.432.67.12/32 ! """


def get_ip_from_text(a_text):
    solutions = []
    splitted_text = a_text.split()
    for words in splitted_text:
        try:
            adress, network = words.split('/')
            a, b, c, d = adress.split('.')
            solutions.append((a, b, c, d, network))
        except ValueError:
            pass
    return solutions


print(get_ip_from_text(texte))
