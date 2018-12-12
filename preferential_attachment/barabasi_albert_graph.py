import networkx as nx
import numpy as np

if __name__ == '__main__':
    n = int(input())
    G = nx.Graph()
    G.add_edge(0, 1)
    for i in range(2, n):
        p = [val / (2 * G.size()) for (_, val) in G.degree()]
        nodes = np.nonzero(np.random.binomial(1, p, len(G)))[0]
        G.add_node(i)
        G.add_edges_from([(i, node) for node in nodes])
    print(nx.is_connected(G))
    f = open(
        'barabasi_albert_graph/barabasi_albert_graph' +
        str(n) +
        '.txt',
        'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
