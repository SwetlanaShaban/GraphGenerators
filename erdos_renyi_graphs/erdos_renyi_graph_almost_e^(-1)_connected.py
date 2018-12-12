import networkx as nx
import math


if __name__ == '__main__':
    n = int(input())
    G = nx.erdos_renyi_graph(n, math.log(n) / n)
    f = open(
        'erdos_renyi_graph_almost_e^(-1)_connected/erdos_renyi_graph_almost_e^(-1)_connected' +
        str(n) +
        '.txt',
        'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
    print(nx.is_connected(G))
