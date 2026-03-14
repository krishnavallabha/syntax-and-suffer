# Level by Level — Breadth First Search

---

## 1. The Core Idea

BFS explores a graph **level by level** — first all vertices one step away from the source, then two steps away, then three, and so on.

```
Source → level 1 neighbours → level 2 neighbours → ...
```

Think of it as a ripple spreading outward from a stone dropped in water.

**Key rules:**
- Each vertex is visited **at most once**
- Visited but unexplored vertices are stored in a **queue (FIFO)**
- When a vertex is dequeued, all its unvisited neighbours are enqueued

---

## 2. Algorithm

**Initialise:**
- Set `visited[v] = False` for all vertices
- Set `visited[source] = True`
- Enqueue the source

**Repeat until queue is empty:**
1. Dequeue vertex j
2. For each neighbour k of j:
   - If `visited[k] == False`:
     - Set `visited[k] = True`
     - Enqueue k

---

## 3. Example Trace

BFS from vertex 0 in graph: 0→1, 0→4, 1→2, 2→0

```
Queue: [0]         visited: {0}

Dequeue 0 → neighbours 1, 4
Queue: [1, 4]      visited: {0, 1, 4}

Dequeue 1 → neighbour 2
Queue: [4, 2]      visited: {0, 1, 4, 2}

Dequeue 4 → no unvisited neighbours
Dequeue 2 → neighbour 0 (already visited)

Queue empty → done
```

---

## 4. Recording Paths (Parent Array)

To reconstruct the actual path from source to any reachable vertex, track **how each vertex was discovered**:

```
parent[k] = j    (vertex k was found while exploring j)
```

To find the path from source to vertex k:

```
k → parent[k] → parent[parent[k]] → ... → source
```

Follow parent links backwards until you reach the source.

---

## 5. Recording Distances (Level Array)

BFS naturally discovers vertices in order of distance. Instead of a boolean `visited`, maintain `level[v]`:

```
level[source] = 0
level[k] = level[j] + 1    (when k is discovered from j)
```

`level[v]` gives the **shortest path distance** from source to v, measured in number of edges.

Unvisited vertices are initialised to -1. A vertex with level == -1 has not been reached.

> This is why BFS finds shortest paths — it always visits closer vertices before farther ones.

---

## 6. Complexity

Each vertex is enqueued and dequeued **exactly once**.

| Representation | Complexity | Why |
|----------------|------------|-----|
| Adjacency Matrix | O(n²) | Exploring vertex i scans all n entries of row i |
| Adjacency List | O(n + m) | Exploring vertex i only looks at its actual neighbours |

> When m << n², the adjacency list version is dramatically faster. This is why m and n are kept as separate parameters.

---

## 7. Summary

| Feature | BFS |
|---------|-----|
| Data structure | Queue (FIFO) |
| Order of exploration | Level by level |
| Finds shortest path? | Yes (by number of edges) |
| Complexity (matrix) | O(n²) |
| Complexity (list) | O(n + m) |

---

## Exam Quick-Fire

**Q: What data structure does BFS use?**
Queue — FIFO

**Q: Does BFS find shortest paths?**
Yes — shortest in terms of number of edges

**Q: Why is BFS O(n + m) with adjacency lists?**
Each vertex is processed once (O(n)) and each edge is examined once (O(m))

**Q: What does level[v] represent?**
The shortest path distance (in edges) from the source to v

**Q: How do you recover the actual path after BFS?**
Follow parent[] links from destination back to source
