def bellman_ford(vertices, edges, source):
    # Step 1: Initialize distances
    dist = [float('inf')] * vertices
    dist[source] = 0

    # Step 2: Relax edges (V - 1) times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative weight cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "Negative weight cycle detected"

    return dist
