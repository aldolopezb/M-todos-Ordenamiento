import matplotlib.pyplot as plt
import numpy as np

# Definimos el camión como una cuadrícula (ancho, largo)
truck_width = 6
truck_length = 10
truck = np.zeros((truck_length, truck_width))  # Camión vacío (0 significa espacio libre)

# Definimos los muebles como rectángulos (ancho, alto)
furniture = [
    {"name": "Sofa", "width": 3, "height": 2},
    {"name": "Mesa", "width": 2, "height": 2},
    {"name": "Silla", "width": 1, "height": 1},
    {"name": "Estante", "width": 2, "height": 3},
    {"name": "Cama", "width": 4, "height": 2},
    {"name": "Refrigerador", "width": 1, "height": 2}
]

# Función para verificar si el mueble cabe en la posición dada
def can_place(truck, furniture, x, y):
    for i in range(furniture['height']):
        for j in range(furniture['width']):
            if x + i >= truck.shape[0] or y + j >= truck.shape[1] or truck[x + i][y + j] != 0:
                return False
    return True

# Función para colocar el mueble en el camión
def place_furniture(truck, furniture, x, y, furniture_id):
    for i in range(furniture['height']):
        for j in range(furniture['width']):
            truck[x + i][y + j] = furniture_id

# Función para eliminar el mueble (cuando se retrocede)
def remove_furniture(truck, furniture, x, y):
    for i in range(furniture['height']):
        for j in range(furniture['width']):
            truck[x + i][y + j] = 0

# Función de Búsqueda Vuelta Atrás para colocar todos los muebles
def backtrack(truck, furniture_list, index):
    if index == len(furniture_list):
        return True  # Todos los muebles están colocados
    
    furniture = furniture_list[index]
    for x in range(truck.shape[0]):
        for y in range(truck.shape[1]):
            if can_place(truck, furniture, x, y):
                place_furniture(truck, furniture, x, y, index + 1)
                
                if backtrack(truck, furniture_list, index + 1):
                    return True  # Solución encontrada
                
                remove_furniture(truck, furniture, x, y)  # Retroceder
    
    return False  # No se puede colocar este mueble en ninguna posición

# Ejecutamos la Búsqueda Vuelta Atrás
backtrack(truck, furniture, 0)

# Graficamos el resultado
def plot_truck(truck):
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(truck, cmap="Pastel1", origin="upper")

    # Configuración de la cuadrícula
    ax.set_xticks(np.arange(truck_width) - 0.5, minor=True)
    ax.set_yticks(np.arange(truck_length) - 0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=2)
    ax.tick_params(axis='both', which='both', length=0)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)

    # Añadir leyenda fuera de la gráfica
    for i, furn in enumerate(furniture):
        ax.text(truck_width + 1, i, f"{i+1}: {furn['name']}", 
                verticalalignment='center', horizontalalignment='left', fontsize=12, fontweight='bold')

    # Ajustar límites
    ax.set_xlim(-0.5, truck_width - 0.5)
    ax.set_ylim(truck_length - 0.5, -0.5)
    plt.subplots_adjust(right=0.7)  # Ajustar el margen derecho para dar espacio a la leyenda

    plt.show()

plot_truck(truck)


# El algoritmo sigue buscando dónde pueden colocarse los muebles sin que sobrepasen los límites del camión de mudanza.
# Podemos cambiar el ejemplo reduciendo el area del camión por un area de 6 x 5 para ver cómo es que el método 
# cámbia el acomodo para que quepa mejor la carga en el area designada.