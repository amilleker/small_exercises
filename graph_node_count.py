graph = [('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'),
         ('b', 'c'), ('b', 'e'), ('e', 'c'), ('e', 'b'), ('d', 'c')]

def get_nodes_count(a_graph_list):
    graph_dict = {}
    for i in a_graph_list:
        graph_dict[i[0]] = graph_dict.get(i[0], 0) + 1
        graph_dict[i[1]] = graph_dict.get(i[1], 0) + 1
    for j in graph_dict:
        graph_dict[j] = int(graph_dict[j]/2)
    return(graph_dict)


print(get_nodes_count(graph))