import networkx as nx

if __name__ == '__main__':
    n = int(input())
    G = nx.gnm_random_graph(n, 10)
    f = open(
        'erdos_renyi_graph_n_10n/erdos_renyi_graph_n_10n' +
        str(n) +
        '.txt',
        'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
    print(nx.is_connected(G))
