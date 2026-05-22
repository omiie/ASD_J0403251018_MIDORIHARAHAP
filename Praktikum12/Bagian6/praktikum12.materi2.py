# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2
# Materi 12 - Graph II : Shortest Path

def bellman_ford(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 

    # Relaksasi berulang 
    for _ in range(len(graph) - 1):  
        for node in graph: 

            for neighbor, weight in graph[node].items():  
                if distances[node] + weight < distances[neighbor]: 

                    distances[neighbor] = distances[node] + weight 
    return distances 