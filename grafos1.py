from collections import defaultdict
import random
import string


class Grafo(object):

    def __init__(self):
        self.adj = defaultdict(set)

    def gerar_arestas(self):
        nos = list(string.ascii_uppercase)
        qtd_nos = random.randint(2, 26)
        # print(qtd_nos)
        max_arestas = random.randint(qtd_nos-1, (qtd_nos*(qtd_nos-1))//2)
        # print(max_arestas)
        arestas = []
        # print(nos)
        for n in range(max_arestas):
            while True:
                v = nos[random.randint(0, qtd_nos-1)]
                u = nos[random.randint(0, qtd_nos-1)]
                if v != u and tuple((v, u)) not in arestas:
                    arestas.append(tuple((v,u)))
                    break
        return arestas

    def get_nos(self):
        return list(self.adj.keys())

    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def dfs(self, grafo, vertice):
        visitados = list()
        def dfs_recursiva(grafo, vertice):
            visitados.append(vertice)
            # print(visitados)
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    dfs_recursiva(grafo, vizinho)
        dfs_recursiva(grafo, vertice)

    def retorna_grafo(self):
        arestas = self.gerar_arestas()
        grafo.adiciona_arestas(arestas)
        nos = self.get_nos()
        lista_adja = self.adj
        # print("NOS")
        # print(nos)
        # print("VISITAS")
        self.dfs(lista_adja, 'A')
        # print("ADJS")
        # print(lista_adja)
        # print(valores)

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]

if __name__ in "__main__":
    grafo = Grafo()
    grafo.retorna_grafo()