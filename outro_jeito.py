import networkx as nx 
import matplotlib.pyplot as plt

# Pergunta para o usuário quais são os vértices do grafo
# Por exemplo: entrando com "abcd" irá criar 4 vértices: 'a','b','c','d'
vertices=list(input("Entre com as sequência de vértices: " ))
print('Muito obrigado, os vértices ficaram assim: ',vertices)

# Para cada vértice, pergunta quais são seus vizinhos
arestas=[]
for vertice in vertices:
    vizinhos=list(input("Quais os vizinhos de "+vertice+" ? "))
    for vizinho in vizinhos:
      aresta=(vertice,vizinho)
      arestas.append(aresta)
print('Muito obrigado, as arestas ficaram assim: ',arestas)
# Cria um grafo vazio
G = nx.Graph()

# Coloca os vértices e arestas no grafo G
G.add_nodes_from(grafo[0])
G.add_edges_from(grafo[1])
nx.draw(G, pos=nx.spring_layout(G), with_labels = True, edge_color='r', node_color = ['blue'], arrows=True,arrowstyle = '-|>',
        arrowsize =  15)
plt.show()
