from collections import defaultdict
import random
import string
import matplotlib.pyplot as plt

class Grafo(object):

    def __init__(self):
        self.adj = defaultdict(set)
        self.n_nos = 0
        self.ciclos1 = 0
        self.ciclos2 = 0
        self.n_contaminados = 0
        self.contaminados = []

    def set_nnos(self, n):
        self.n_nos = n

    def gerar_arestas(self):
        nos = list(string.printable)
        qtd_nos = random.randint(2, 100)
        self.set_nnos(qtd_nos)
        max_arestas = random.randint(qtd_nos-1, (qtd_nos*(qtd_nos-1))//2)
        arestas = []
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

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def dfs(self, grafo, vertice):
        visitados = list()
        def dfs_recursiva(grafo, vertice):
            visitados.append(vertice)
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    dfs_recursiva(grafo, vizinho)
        dfs_recursiva(grafo, vertice)
        return visitados
    
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
        self.ciclos2 += 1

    def contamina_1(self):        
        for n in self.contaminados.copy():
            for m in self.adj[n]:
                if m not in self.contaminados:
                    self.adiciona_contagio(m)
                    break;
        self.ciclos1 += 1
    
    def zerar_dados(self):
        self.contaminados = []
        self.n_contaminados = 0
        self.adiciona_contagio('0')

    def calcula_ciclos_sem_vacina(self):
        self.adiciona_contagio('0')
        print()
        
        while (self.n_contaminados != self.n_nos):
            self.contamina_2()
        print("Pessoas NÃO vacinadas: ", self.n_nos, "| Dias necessários para contaminar toda população: ", self.ciclos2 * 7, "dias")
    
    def calcula_ciclos_com_vacina(self):
        print()
        self.zerar_dados()
        while (self.n_contaminados != self.n_nos):
            self.contamina_1()
        print("Pessoas JÁ vacinadas: ", self.n_nos, "| Dias necessários para contaminar toda população: ", 7 * self.ciclos1, "dias")
    
    def plotar_grafico(self):
        populacao = ['Não Vacinada', 'Vacinada']
        ciclos = [self.ciclos2 * 7, self.ciclos1 * 7]

        plt.bar(populacao, ciclos, color = "#8B0000")

        plt.xticks(populacao)
        plt.ylabel("Número de dias")
        plt.xlabel("Estado da população")
        plt.title("Número de dias até uma contaminação completa \nX\n População vacinada e não vacinada")
        plt.axhline(self.ciclos2 * 7, 0, 1, color="#00BFFF", **{'ls':'--', 'lw':5})
        plt.show()

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))
    
    def retorna_grafo(self):
        arestas = self.gerar_arestas()
        self.adiciona_arestas(arestas)
        nos = self.get_nos()
        busca = self.dfs(self.adj, '0')
        if len(busca) != len(nos):
            self.adj = defaultdict(set)
            self.retorna_grafo()
        print("Tamanho do grafo: ", self.__len__())
        grafo.calcula_ciclos_sem_vacina()
        grafo.calcula_ciclos_com_vacina()
        grafo.plotar_grafico()
            
            
if __name__ in "__main__":
    grafo = Grafo()
    grafo.retorna_grafo()
