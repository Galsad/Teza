import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from tqdm import tqdm
import pprint
import collections

def random_diamnod_chain(n = 40):
    G = nx.DiGraph()
    i = 0
    while i < n:
        G.add_edge(i, i+1)
        G.add_edge(i, i + 2)
        G.add_edge(i + 1, i + 3)
        G.add_edge(i + 2, i + 3)
        i += 3
    return G


def delete_random_edges(G):
    edges_to_remove = []
    for edge in G.edges():
        a = random.randint(0, 2)
        if a == 0:
            edges_to_remove.append(edge)

    for edge in edges_to_remove:
        G.remove_edge(*edge)

    return G


def full_chain(size = 20):
    G = nx.DiGraph()
    for i in range(size):
        for j in range(i, size):
            G.add_edge(i, j, prob = 1./size)
            # weights[(i, j)] = 1./(size - i)
            # weights[(i, j)] = 1. / (size)
            # weights[(i, j)] = 1. / ( size**(0.5) * (j - i + 1) )
            # weights[(i, j)] = 1. / (j - i + 1)

    # nx.set_edge_attributes(G, weights, 'prob')
    return G


def delete_random_edges_full_chain(G):
    edges_to_remove = []
    thresholds = np.random.uniform(0, 1, (len(G.nodes()), len(G.nodes())))
    for i in range(len(G.nodes())):
        for j in range(i, len(G.nodes())):
            if thresholds[i][j] > G[i][j]['prob']:
                edges_to_remove.append((i,j))

    for edge in edges_to_remove:
        G.remove_edge(*edge)

    return G


def block_graph(n=32):
    '''
    cteates a graph with n**2 + 1 nodes. there are n layers which each contains n nodes, all nodes are connected to
    each other and have a probability of 1/n.
    :param n:
    :return:
    '''
    G = nx.DiGraph()
    for i in range(n):
        G.add_edge((0,0), (1, i), prob=1./n, a=0)

    # i represents layer and j and k represents nodes in each layer
    for i in range(1, n):
        for j in range(n):
            for k in range(n):
                G.add_edge((i, j), (i+1, k), prob=1./n**(1.14), a=0)

    return G


def delete_edges_from_block_graph(G):
    edges_to_remove = []
    for edge in G.edges():
        G[edge[0]][edge[1]]['a'] = np.random.uniform(0, 1)
        if G[edge[0]][edge[1]]['a'] > G[edge[0]][edge[1]]['prob']:
            edges_to_remove.append(edge)

    for edge in edges_to_remove:
        G.remove_edge(*edge)

    return G


if __name__ == '__main__':
    Es = []
    for i in tqdm(range(1000)):
        # G = full_chain(128)
        # G = nx.fast_gnp_random_graph(500, 0.0009, directed=True)
        G = block_graph(n=180)
        G1 = delete_edges_from_block_graph(G)
        Es.append(len(nx.weakly_connected_components(G1).next()))
    print Es
    print np.average(Es)**2, np.var(Es)
    C = collections.Counter(Es)
    labels, values = zip(*C.items())
    indexes = np.arange(len(labels))
    width=1
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()