import matplotlib.pyplot as plt
import numpy as np

def interpolation_search(arr, target):
    """
    Realiza una búsqueda por interpolación para encontrar el índice del valor objetivo en un arreglo ordenado.
    
    Args:
    - arr (list of int): Arreglo ordenado en el que se realiza la búsqueda.
    - target (int): Valor a buscar en el arreglo.
    
    Returns:
    - int: Índice del valor objetivo en el arreglo, o -1 si no se encuentra.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        # Evitar división por cero
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            else:
                return -1
        
        # Estimación de la posición
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        
        # Verificar si la posición estimada contiene el objetivo
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

def plot_inventory(arr, target_index):
    """
    Grafica el inventario de productos y marca el producto buscado.
    
    Args:
    - arr (list of int): Arreglo ordenado de IDs de productos.
    - target_index (int): Índice del producto buscado en el arreglo.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(arr, 'bo-', label='IDs de Productos', markersize=10)
    
    # Marca el producto buscado
    if target_index != -1:
        plt.plot(target_index, arr[target_index], 'ro', markersize=12, label='Producto Buscado')
    
    plt.xlabel('Índice')
    plt.ylabel('ID del Producto')
    plt.title('Inventario de Productos')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Crear un inventario de productos
    product_ids = [1001, 1003, 1005, 1007, 1009, 1011, 1013, 1015, 1017, 1019]

    # Solicitar al usuario el ID del producto a buscar
    try:
        target_id = int(input("Ingrese el ID del producto que está buscando: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    # Buscar el ID del producto usando búsqueda por interpolación
    target_index = interpolation_search(product_ids, target_id)

    # Mostrar el resultado
    if target_index != -1:
        print(f"Producto con ID {target_id} encontrado en el índice {target_index}.")
    else:
        print(f"Producto con ID {target_id} no encontrado.")

    # Graficar el inventario y el producto buscado
    plot_inventory(product_ids, target_index)

if __name__ == "__main__":
    main()

'''En un almacén, tenemos una lista ordenada de productos por su número de 
identificación (ID) y necesitamos encontrar un producto específico'''