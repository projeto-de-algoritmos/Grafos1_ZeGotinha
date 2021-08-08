from collections import defaultdict
import random
import string


class Grafo(object):

    def __init__(self):
        self.adj = defaultdict(set)
        # self.adj = [[] for _ in range(10)]

    def gerar_arestas(self):
        nos = list(string.ascii_uppercase)
        qtd_nos = random.randint(2, 26)
        print(qtd_nos)
        max_arestas = random.randint(qtd_nos-1, (qtd_nos*(qtd_nos-1))//2)
        print(max_arestas)
        arestas = []
        print(nos)
        for n in range(max_arestas):
            while True:
                v = nos[random.randint(0, qtd_nos-1)]
                u = nos[random.randint(0, qtd_nos-1)]
                if v != u and tuple((v, u)) not in arestas:
                    arestas.append(tuple((v,u)))
                    break
        print(arestas)
        return arestas


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
    grafo = Grafo()
    grafo.adiciona_arestas(grafo.gerar_arestas())
    print(grafo.adj)
    #print(grafo.get_vertices())
    #print(grafo.get_arestas())
    #print(grafo.existe_aresta('A', 'B'), grafo.existe_aresta('E', 'C'))