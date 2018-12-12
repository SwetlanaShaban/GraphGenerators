import networkx as nx
import numpy as np

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    G = nx.Graph()
    G.add_edge(0, 0)
    for i in range(2, k * n + 1):
        prob = [val / (2 * i - 1) for (_, val) in G.degree()]
        prob.append(1 / (2 * i - 1))
        node = np.random.choice(i, 1, p=prob)[0]
        G.add_edge(i - 1, node)
    H = nx.empty_graph(n)
    for i in range(n):
        edges_to_add = ((int(u / k), int(v / k))
                        for (u, v) in G.edges(range(i, k * (i + 1))))
        H.add_edges_from(edges_to_add)
    f = open('bollobas_riordan/bollobas_riordan' + str(n) + '.txt', 'w')
    f.write(str(n) + ' ' + str(H.number_of_edges()) + '\n')
    for i, j in H.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
    print(nx.is_connected(H))
