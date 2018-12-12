import networkx as nx

if __name__ == '__main__':
    n = int(input())
    G = nx.random_regular_graph(4, n)
    f = open('4-regular_graph/4-regular_graph' + str(n) + '.txt', 'w')
    f.write(str(n) + ' ' + str(G.number_of_edges()) + '\n')
    for i, j in G.edges():
        f.write(str(i) + ' ' + str(j) + '\n')
    print(nx.is_connected(G))
