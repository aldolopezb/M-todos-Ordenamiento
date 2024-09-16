import heapq
import matplotlib.pyplot as plt
import networkx as nx

def heuristic(a, b):
    """
    Calcula la distancia heurística entre dos puntos usando la distancia Manhattan.
    
    Args:
    - a (tuple): Coordenada del punto A (x1, y1).
    - b (tuple): Coordenada del punto B (x2, y2).
    
    Returns:
    - int: Distancia heurística entre los puntos A y B.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(graph, start, goal):
    """
    Implementa el algoritmo A* para encontrar el camino más corto en un grafo.
    
    Args:
    - graph (networkx.Graph): El grafo en el que se realiza la búsqueda.
    - start (tuple): Nodo de inicio.
    - goal (tuple): Nodo objetivo.
    
    Returns:
    - dict: Diccionario que mapea cada nodo al nodo desde el cual fue alcanzado por primera vez.
    - dict: Diccionario que mapea cada nodo al costo total desde el nodo de inicio hasta ese nodo.
    """
    # Cola de prioridad para los nodos a explorar, ordenada por prioridad
    queue = []
    # Inserta el nodo de inicio en la cola con prioridad 0
    heapq.heappush(queue, (0, start))
    # Diccionario para rastrear el nodo desde el cual llegamos a cada nodo
    came_from = {start: None}
    # Diccionario para rastrear el costo total desde el nodo de inicio a cada nodo
    cost_so_far = {start: 0}

    while queue:
        # Extrae el nodo con la prioridad más alta (menor valor de f)
        current = heapq.heappop(queue)[1]

        # Si el nodo actual es el objetivo, terminamos
        if current == goal:
            break

        # Explora los nodos vecinos
        for next in graph.neighbors(current):
            # Calcula el costo para llegar al nodo vecino
            new_cost = cost_so_far[current] + graph[current][next]['weight']
            # Si el nodo vecino no ha sido visitado o encontramos un camino más corto
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                # Actualiza el costo y el nodo desde el cual llegamos
                cost_so_far[next] = new_cost
                # Calcula la prioridad como la suma del costo y la heurística
                priority = new_cost + heuristic(goal, next)
                # Inserta el nodo vecino en la cola con la nueva prioridad
                heapq.heappush(queue, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    """
    Reconstruye el camino desde el nodo de inicio hasta el objetivo utilizando el diccionario came_from.
    
    Args:
    - came_from (dict): Diccionario que mapea cada nodo al nodo desde el cual fue alcanzado por primera vez.
    - start (tuple): Nodo de inicio.
    - goal (tuple): Nodo objetivo.
    
    Returns:
    - list: Lista de nodos en el camino desde el inicio hasta el objetivo.
    """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Crear un grafo de ejemplo (una cuadrícula 5x5)
G = nx.grid_2d_graph(5, 5)
# Establecer el peso de cada arista como 1
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = 1

# Definir los nodos de inicio y objetivo
start, goal = (0, 0), (4, 4)
# Ejecutar la búsqueda A*
came_from, cost_so_far = a_star_search(G, start, goal)
# Reconstruir el camino encontrado
path = reconstruct_path(came_from, start, goal)

# Graficar el grafo y el camino encontrado
# Establecer la posición de los nodos en el gráfico
pos = {node: node for node in G.nodes()}
# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
# Dibujar los bordes del camino encontrado en rojo
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
# Mostrar el gráfico
plt.show()


''' La visualización muestra el camino encontrado por el algoritmo A*. 
Dado que la cuadrícula es simple y los costos son uniformes, el camino 
más corto en términos de costo y heurística es generalmente el más 
directo.'''