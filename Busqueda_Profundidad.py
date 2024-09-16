import networkx as nx
import matplotlib.pyplot as plt

# Definimos el grafo que simula empresas, departamentos y roles
grafo_empresas = {
    'Empresa A': ['Depto 1', 'Depto 2'],
    'Depto 1': ['Rol 1.1', 'Rol 1.2'],
    'Depto 2': ['Rol 2.1', 'Rol 2.2'],
    'Rol 1.1': [],
    'Rol 1.2': [],
    'Rol 2.1': [],
    'Rol 2.2': [],
    
    'Empresa B': ['Depto 3', 'Depto 4'],
    'Depto 3': ['Rol 3.1', 'Rol 3.2'],
    'Depto 4': ['Rol 4.1', 'Rol 4.2'],
    'Rol 3.1': [],
    'Rol 3.2': [],
    'Rol 4.1': [],
    'Rol 4.2': [],

    'Empresa C': ['Depto 5', 'Depto 6'],
    'Depto 5': ['Rol 5.1', 'Rol 5.2'],
    'Depto 6': ['Rol 6.1', 'Rol 6.2'],
    'Rol 5.1': [],
    'Rol 5.2': [],
    'Rol 6.1': [],
    'Rol 6.2': [],
}

# Implementamos DFS para explorar las oportunidades laborales en las empresas
def dfs(graph, node, visited):
    if node not in visited:
        print(f'Explorando {node}')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Ejecutar DFS desde la primera empresa
visited = set()
inicio = 'Empresa A'
dfs(grafo_empresas, inicio, visited)

# Crear el grafo para visualizarlo
G = nx.DiGraph()

# Añadimos nodos y bordes al grafo
for node, neighbors in grafo_empresas.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Definir colores para los nodos
color_map = []
for node in G.nodes():
    if "Empresa" in node:
        color_map.append('skyblue')  # Color para empresas (nodos principales)
    elif "Depto" in node:
        color_map.append('lightgreen')  # Color para departamentos (nodos secundarios)
    else:
        color_map.append('lightcoral')  # Color para roles (nodos terciarios)

# Dibujamos el grafo con los colores especificados
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=color_map, font_size=10, node_size=3000, arrows=True)
plt.title("Búsqueda de Empleo usando DFS con colores personalizados", size=15)
plt.show()


'''Si tenemos una lista de empresas que nos interesan. Para cada empresa, exploramos primero todas las vacantes disponibles 
dentro de un departamento (como ingeniería, venatas, marketing, etc.), luego, si ninguna vacante es adecuada, 
pasamos al siguiente departamento, y finalmente, cuando hayamos agotado todas las oportunidades dentro de esa empresa, 
nos muevemos a la siguiente empresa en tu lista.'''