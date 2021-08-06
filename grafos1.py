from collections import defaultdict

class Grafo(object):

    def __init__(self, arestas):
        self.adj = defaultdict(set)
        # self.adj = [[] for _ in range(10)]
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        return list(self.adj.keys())

    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adiciona_aresta_dupla(u, v)

    def adiciona_aresta_dupla(self, u, v):
        self.adj[u].add(v)

    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]

if __name__ in "__main__":
    arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]

    grafo = Grafo(arestas)
    print(grafo.adj)
    print(grafo.get_vertices())
    print(grafo.get_arestas())
    print(grafo.existe_aresta('A', 'B'), grafo.existe_aresta('E', 'C'))