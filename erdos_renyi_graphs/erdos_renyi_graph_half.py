import networkx as nx

if __name__ == '__main__':
    n = int(input())
    G = nx.erdos_renyi_graph(n, 0.5)
    f = open(
        'erdos_renyi_graph_half/erdos_renyi_graph_half_' +
        str(n) +
        '.txt',
        'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
    print(nx.is_connected(G))
