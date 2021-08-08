from collections import defaultdict
import random
import string


class Grafo(object):

    def __init__(self):
        self.adj = defaultdict(set)
        self.n_nos = 0
        self.ciclos = 0
        self.n_contaminados = 0
        self.contaminados = []
        # self.adj = [[] for _ in range(10)]

    def set_nnos(self, n):
        self.n_nos = n

    def gerar_arestas(self):
        nos = list(string.ascii_uppercase)
        qtd_nos = random.randint(2, 26)
        self.set_nnos(qtd_nos)
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
        return visitados

    def retorna_grafo(self):
        arestas = self.gerar_arestas()
        self.adiciona_arestas(arestas)
        nos = self.get_nos()
        lista_adja = self.adj
        busca = self.dfs(lista_adja, 'A')
        if len(busca) != len(nos):
            self.adj = defaultdict(set)
            self.retorna_grafo()
        # print("NOS")
        # print(nos)
        # print("VISITAS")
        # print("ADJS")
        # print(lista_adja)
        # print(valores)
           

    def adiciona_contagio(self, u):
        self.contaminados.append(u)
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
        self.contaminados = []
        self.n_contaminados = 0
        self.adiciona_contagio('A')

    def calcula_ciclos_sem_vacina(self):
        print(self.adj)
        self.adiciona_contagio('A')
        print()
        
        while (self.n_contaminados != self.n_nos):
            self.contamina_2()
        print("Sem vacina: ","Número contaminados:", self.n_contaminados, "Ciclos:", self.ciclos)
    
    def calcula_ciclos_com_vacina(self):
        print()
        self.zerar_dados()
        while (self.n_contaminados != self.n_nos):
            self.contamina_1()
        print("Com vacina: ","Número contaminados:", self.n_contaminados, "Ciclos:", self.ciclos)
    

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]

if __name__ in "__main__":
    grafo = Grafo()
    grafo.retorna_grafo()

    grafo.calcula_ciclos_sem_vacina()
    grafo.calcula_ciclos_com_vacina()
