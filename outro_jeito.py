import networkx as nx 
import matplotlib.pyplot as plt

# Pergunta para o usuário quais são os vértices do grafo
# Por exemplo: entrando com "abcd" irá criar 4 vértices: 'a','b','c','d'
vertices=list(input("Entre com as sequência de vértices: " ))

# Para cada vértice, pergunta quais são seus vizinhos
arestas=[]
for vertice in vertices:
    vizinhos=list(input("Quais os vizinhos de "+vertice+" ? "))
    for vizinho in vizinhos:
      aresta=(vertice,vizinho)
      arestas.append(aresta)
 
# Apenas junta vertices e arestas em um única estrutura de dados
grafo=(vertices,arestas)
print('Vértices do grafo: ',grafo[0])
print('Arestas do grafo: ',grafo[1])

def totalArestas(grafo):
  return(len(grafo[1]))
  
print('O total de arestas é: ',totalArestas(grafo))

def mostraGraus(grafo):

  # Cria um dicionário de vértice e graus  
  graus = {v:0 for v in grafo[0]}

  for v1,v2 in grafo[1]:
     graus[v1]+=1
     graus[v2]+=1
     
  print('o grau de cada vertice é: ',graus)    
                  
    
mostraGraus(grafo) 

# Cria um grafo vazio
G = nx.Graph()

# Coloca os vértices e arestas no grafo G
G.add_nodes_from(grafo[0])
G.add_edges_from(grafo[1])
nx.draw(G, pos=nx.spring_layout(G), with_labels = True, edge_color='r', node_color = ['blue'], arrows=True,arrowstyle = '<|-|>',
        arrowsize =  15)
plt.show()
