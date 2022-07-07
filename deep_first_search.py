
# A entrada do algortimo será um dicionário que atuará como uma lista de adjacência

graph = {
    'V1' : ['V2','V3'],
    'V2' : ['V4', 'V5'],
    'V3' : ['V6'],
    'V4' : [],
    'V5' : ['V6'],
    'V6' : []
}

visited = set() #irá acompanhar os nós visitados

#Função que percorrerá o grafo:
def deep_first_search(visited, graph, node):
    if node not in visited: #1. verifica se o vértice ainda não foi visitado, se sim, ele será adicionado em visited
        print (node)
        visited.add(node)
        for neighbour in graph[node]: # Para cada vizinho do nó atual, a função é chamada novamente
            deep_first_search(visited, graph, neighbour)

print("Pecorrendo o grafo")
deep_first_search(visited, graph, 'V1')
