from collections import defaultdict
import random
import string


class Grafo(object):

    def __init__(self):
        self.adj = defaultdict(set)
        self.n_nos = 0
        self.ciclos = 0
        self.n_contaminados = 0
        self.contaminados = {}
        # self.adj = [[] for _ in range(10)]

    def set_nnos(self, n):
        self.n_nos = n

    def gerar_arestas(self):
        qtd_nos = 200
        self.set_nnos(qtd_nos)
        print(qtd_nos)
        max_arestas = random.randint(qtd_nos-1, (qtd_nos*(qtd_nos-1))//2)
        print(max_arestas)
        arestas = []
        # print(nos)
        for n in range(max_arestas):
            while True:
                v = random.randint(0, qtd_nos-1)
                u = random.randint(0, qtd_nos-1)
                if v != u and tuple((v, u)) not in arestas:
                    arestas.append(tuple((v,u)))
                    break
        # print(arestas)
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
        self.adj[v].add(u)

    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def adiciona_contagio(self, u):
        self.contaminados[u] = 'Contaminado'
        self.n_contaminados += 1

    def contamina_2(self):        
        for n in self.contaminados.copy():
            contagio = 0
            for m in self.adj[n]:
                if m not in self.contaminados:
                    self.adiciona_contagio(m)
                    contagio += 1
                if contagio == 2:
                    break
        self.ciclos += 1

    def contamina_1(self):        
        for n in self.contaminados.copy():
            for m in self.adj[n]:
                if m not in self.contaminados:
                    self.adiciona_contagio(m)
                    break;
        self.ciclos += 1
    
    def zerar_dados(self):
        self.ciclos = 0
        self.contaminados = {}
        self.n_contaminados = 0
        self.adiciona_contagio(1)

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]

if __name__ in "__main__":
    grafo = Grafo()
    
    grafo.adiciona_arestas(grafo.gerar_arestas())
    grafo.adiciona_contagio(1)
    print()
    
    #print(grafo.adj)
    while (grafo.n_contaminados != grafo.n_nos):
        grafo.contamina_2()
    print("Sem vacina: ","Número contaminados:", grafo.n_contaminados, "Ciclos:", grafo.ciclos)
    #
    print()
    grafo.zerar_dados()
    while (grafo.n_contaminados != grafo.n_nos):
        grafo.contamina_1()
    print("Com vacina: ","Número contaminados:", grafo.n_contaminados, "Ciclos:", grafo.ciclos)
    
    #print(grafo.get_vertices())
    #print(grafo.get_arestas())
    #print(grafo.existe_aresta('A', 'B'), grafo.existe_aresta('E', 'C'))