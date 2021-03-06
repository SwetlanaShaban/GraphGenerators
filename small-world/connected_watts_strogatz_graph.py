import networkx as nx

if __name__ == '__main__':
    n = int(input())
    G = nx.connected_watts_strogatz_graph(n, 4, 0.5)
    f = open(
        'connected_watts_strogatz_graph/connected_watts_strogatz_graph_' +
        str(n) +
        '.txt',
        'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
