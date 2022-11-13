'''Criar um programa que permite que o usuário entre com os vértices e arestas de um grafo e
mostre diversas propriedades deste gráfico(quanto mais propriedade, mais PIC$, a expectativa
é que mostre ao menos umas 10 propriedades). Entre as propriedades que podem ser apresentadas estão:
grau máximo, grau mínimo, número cromático, raio, diâmetro, perímetro, árvore geradora mínima, etc .
 O programa pode ainda indicar se o grafo é conexo, acíclico, completo, Euleriano, Hamiltoniano, etc
 (isso também são propriedades). O programa deve oferecer ao usuário a possibilidade de abrir grafos
 já prontos que ilustrem algumas destas propriedade.'''

import networkx as nx
import matplotlib.pyplot as plt

class Grafos: 
    
    def __init__(self,vertices):
        #construtor
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        
    def adiciona_aresta_simples(self, u, v, peso):
        #pensando em grafos direcionados simples
        self.grafo[u-1][v-1] = peso
    
    def adiciona_aresta_mult(self, u, v, peso):
        #pensando em grafos múltiplo
        self.grafo[u-1][v-1] += peso
        if u != v:
            self.grafo[v-1][u-1] += peso        

    def adiciona_aresta_sime(self, u, v):
        #pensando em grafos não direcionados, ou de relação simétrica
        self.grafo[u-1][v-1] += 1
        if u != v:
            self.grafo[v-1][u-1] += 1

    def mostra_matriz(self):
        print('A matriz de adjacência é: ')
        for i in range(self.vertices):
            print(self.grafo[i])
    
    def plot_grafo(self):
        #cria um grafo vazio
        G = nx.Graph()

        # Coloca os vértices e arestas no grafo G
        #G.add_node((2,3,4))
    
        G.add_edges_from([(2,3), (2,5), (1,2)])
        nx.draw(G, pos=nx.spring_layout(G), with_labels = True, edge_color='r', node_color = ['blue'], arrows=True,arrowstyle = '-|>',
        arrowsize =  15)
        plt.show()

    def tem_aresta(self,u,v):
        if self.grafo[u-1][v-1] == 0:
            print(f'Não tem aresta entre os vértices {u} e {v}')
        else:
            print(f'Existe {self.grafo[u-1][v-1]} de arestas entre os vértices {u} e {v}')
            
    def eh_euleriano(self):
        contador = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j:
                    grau = grau + 2 * self.grafo[i][j]
                else:
                    grau += self.grafo[i][j]
            if grau % 2 != 0:
                contador += 1
        if contador == 0:
            print('É um grafo euleriano!')
        elif contador == 2:
            print('É um grafo semieuleriano!')
        else:
            print('O grafo não é euleriano e nem semieuleriano!')
        

# tg = str(input('Digite "s" para Grafo Simples ou "m" para Grafo Multiplos" ou "d" para Grafo Simétrico: '))  #tipo de grafo

# v = int(input('Digite a quantidade de Vértices: '))
# g = Grafos(v)
# a = int(input('Digite a quantidade de Arestas: '))

# if tg == 's':
#     for i in range(a):
#         u = int(input('De qual Vértice parte esta Aresta? '))
#         v = int(input('De qual Vértice chega esta Aresta? '))
#         p = int(input('Qual é o peso desta Aresta? '))
#         g.adiciona_aresta_simples(u,v,p)
# elif tg == 'm':
#     for i in range(a):
#         u = int(input('De qual Vértice parte esta Aresta? '))
#         v = int(input('De qual Vértice chega esta Aresta? '))
#         p = int(input('Qual é o peso desta Aresta? '))
#         g.adiciona_aresta_mult(u, v, p)
# elif tg == 'd':
#     for i in range(a):
#         u = int(input('De qual Vértice parte esta Aresta? '))
#         v = int(input('De qual Vértice chega esta Aresta? '))
#         g.adiciona_aresta_sime(u, v)

# g.mostra_matriz()
# g.eh_euleriano()
        
# instanciano objeto
g = Grafos(4)

g.adiciona_aresta_mult(1, 2,5)
g.adiciona_aresta_mult(3, 4,3)
g.adiciona_aresta_mult(2, 3,1)
g.adiciona_aresta_mult(1,4,7)

#g.tem_aresta(2,4)

g.eh_euleriano()
g.tem_aresta(1,4)
g.mostra_matriz()

g.plot_grafo()
