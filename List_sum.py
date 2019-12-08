liste_to_look = [1, 5, 6, 2, 3, 3, 10, 12, 2, 8]
wanted_sum = 8

#sorted(set(liste_to_look))

def get_two_numbers(wanted_sum, liste_to_look):
    head_of_list = 0
    solutions = []
    for i in liste_to_look:
        head_of_list += 1
        for j in liste_to_look[head_of_list:]:
            print(i+j-wanted_sum)
            if int(i)+int(j) == int(wanted_sum) :
                solutions.append((i,j))
    print(solutions)

get_two_numbers(wanted_sum, liste_to_look)