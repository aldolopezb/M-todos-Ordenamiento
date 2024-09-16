import numpy as np
import matplotlib.pyplot as plt

def objective_function(schedule):
    
    num_machines = len(schedule)
    times = [sum(task) for task in zip(*schedule)]
    return max(times)

def generate_neighbor(schedule):
    
    new_schedule = [machine[:] for machine in schedule]
    num_machines = len(new_schedule)
    
    # Seleccionar dos máquinas aleatorias
    machine1, machine2 = np.random.choice(num_machines, 2, replace=False)
    
    # Seleccionar una tarea aleatoria en cada máquina
    task1_idx = np.random.randint(len(new_schedule[machine1]))
    task2_idx = np.random.randint(len(new_schedule[machine2]))
    
    # Intercambiar tareas entre las dos máquinas
    new_schedule[machine1][task1_idx], new_schedule[machine2][task2_idx] = \
        new_schedule[machine2][task2_idx], new_schedule[machine1][task1_idx]
    
    return new_schedule

def tabu_search(initial_schedule, iterations, tabu_size):
   
    current_schedule = initial_schedule
    best_schedule = current_schedule
    best_objective = objective_function(best_schedule)
    
    tabu_list = []
    
    for _ in range(iterations):
        neighbors = [generate_neighbor(current_schedule) for _ in range(10)]
        neighbors = [n for n in neighbors if n not in tabu_list]
        
        if not neighbors:
            break
        
        neighbor = min(neighbors, key=objective_function)
        neighbor_objective = objective_function(neighbor)
        
        if neighbor_objective < best_objective:
            best_schedule = neighbor
            best_objective = neighbor_objective
        
        tabu_list.append(neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        current_schedule = neighbor
    
    return best_schedule, best_objective

def plot_schedule(schedule):
   
    num_machines = len(schedule)
    colors = plt.cm.viridis(np.linspace(0, 1, num_machines))  # Genera colores únicos para cada máquina
    plt.figure(figsize=(10, 6))
    
    for i, (machine, color) in enumerate(zip(schedule, colors)):
        start = 0
        for j, task in enumerate(machine):
            plt.barh(i, task, left=start, color=color, edgecolor='black', label=f'Máquina {i + 1}' if j == 0 else "")
            start += task
            plt.text(start - task / 2, i, f'T{j + 1}', va='center', ha='center', color='black')
    
    plt.xlabel('Tiempo')
    plt.ylabel('Máquinas')
    plt.title('Asignación de Tareas a Máquinas')
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.grid(True)
    plt.show()

def main():
    # Ejemplo de asignación inicial de tareas a máquinas
    initial_schedule = [
        [3, 2, 4],  # Tareas en la Máquina 1
        [5, 3],     # Tareas en la Máquina 2
        [2, 6]      # Tareas en la Máquina 3
    ]
    
    # Parámetros del algoritmo
    iterations = 100
    tabu_size = 10
    
    # Ejecutar búsqueda Tabú
    best_schedule, best_objective = tabu_search(initial_schedule, iterations, tabu_size)
    
    # Mostrar resultados
    print(f"Mejor asignación encontrada: {best_schedule}")
    print(f"Tiempo total de producción: {best_objective}")
    
    # Graficar la mejor asignación
    plot_schedule(best_schedule)

if __name__ == "__main__":
    main()


'''La planificación de producción en el código se centra en asignar tareas 
a máquinas para minimizar el tiempo máximo de trabajo y la gráfica 
proporciona una representación visual de cómo se realiza esta asignación.'''

'''La longitud de la barra indica el tiempo total que cada máquina está ocupada, 
y la gráfica ayuda a visualizar cómo se distribuyen las tareas entre las 
máquinas para lograr una producción equilibrada.'''