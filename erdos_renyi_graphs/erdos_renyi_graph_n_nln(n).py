import networkx as nx
import math

if __name__ == '__main__':
    n = int(input())
    G = nx.gnm_random_graph(n, n * math.log(n))
    f = open(
        'erdos_renyi_graph_n_nln(n)/erdos_renyi_graph_n_nln(n)' +
        str(n) +
        '.txt',
        'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
    print(nx.is_connected(G))
