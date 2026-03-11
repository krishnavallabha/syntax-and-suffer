# Mapping the Web — Graph Representation

---

## 1. Why We Need a Representation

A graph G = (V, E) is a mathematical idea. To run algorithms on it, we must store it in memory. The choice of representation directly affects the **speed and memory usage** of every graph algorithm.

There are two standard approaches:

```
1. Adjacency Matrix  — 2D table
2. Adjacency List    — dictionary of neighbour lists
```

---

## 2. Adjacency Matrix

Create an **n × n table** where n = number of vertices.

```
A[i][j] = 1   if edge i → j exists
A[i][j] = 0   otherwise
```

**Example:** V = {0, 1, 2, 3}, edges: 0→1, 0→2, 1→2, 2→0

```
     0  1  2  3
  0 [0, 1, 1, 0]
  1 [0, 0, 1, 0]
  2 [1, 0, 0, 0]
  3 [0, 0, 0, 0]
```

### Undirected Graphs

For undirected graphs, the matrix is **symmetric**:

```
A[i][j] = A[j][i]
```

Edge (0, 1) means both A[0][1] = 1 and A[1][0] = 1. The matrix mirrors across the diagonal.

### Finding Neighbours

To find all neighbours of vertex i, scan row i for all positions where A[i][j] = 1.

Cost: **O(n)** — must check every column regardless of how many neighbours exist.

### Space

The matrix always occupies **O(n²)** space, even if the graph has very few edges. Most cells will be 0 for sparse graphs — wasted space.

---

## 3. Degree of a Vertex

The **degree** of a vertex is the number of edges connected to it.

For **undirected graphs:**

```
degree(v) = number of neighbours of v
```

For **directed graphs**, degree splits into two:

| Term | Meaning |
|------|---------|
| Outdegree | Number of edges **leaving** v |
| Indegree | Number of edges **entering** v |

**Example:**

```
3 → 6 → 5

outdegree(6) = 1   (6 → 5)
indegree(6)  = 1   (3 → 6)
```

In the adjacency matrix:
- **Row i** sum = outdegree of i
- **Column i** sum = indegree of i

---

## 4. Adjacency List

Instead of storing the full n × n table, store **only the actual neighbours** of each vertex.

**Example:**

```
0 → [1, 4]
1 → [2]
2 → [0]
3 → [4, 6]
4 → [0, 3, 7]
```

This is a dictionary where each key is a vertex and each value is a list of its neighbours.

### Space

Only stores edges that actually exist:

```
Space = O(V + E)
```

For a sparse graph where E << n², this is dramatically smaller than O(n²).

### Edge Limits

| Graph type | Maximum edges |
|------------|---------------|
| Undirected | n(n-1) / 2 |
| Directed | n(n-1) |

In practice, most real-world graphs are **sparse** (E << n²): road networks, social networks, the internet. Adjacency lists are almost always preferred.

---

## 5. Reachability Preview

Reachability asks: **can we reach vertex v starting from vertex u?**

The general algorithm idea:

1. Mark the source vertex as visited
2. Mark all its neighbours
3. Repeatedly mark neighbours of already-marked vertices
4. Stop when the target is marked (reachable) or no new vertices can be marked (unreachable)

This is the foundation of both **BFS** and **DFS**, covered next.

---

## 6. Full Comparison

| Operation | Adjacency Matrix | Adjacency List |
|-----------|-----------------|----------------|
| Space | O(n²) | O(V + E) |
| Check if edge (i,j) exists | O(1) | O(deg(i)) |
| Find all neighbours of i | O(n) | O(deg(i)) |
| Add an edge | O(1) | O(1) |
| Best for | Dense graphs | Sparse graphs |

### Edge lookup detail

- **Matrix:** `A[i][j]` — direct index access, always O(1)
- **List:** scan through `AList[i]` until j is found — O(degree(i))

For dense graphs, degree(i) ≈ n, so both are similar. For sparse graphs, degree(i) << n, making the list much faster for neighbour traversal.

---

## 7. When to Use Which

| Situation | Better Choice |
|-----------|---------------|
| Dense graph (many edges) | Adjacency Matrix |
| Sparse graph (few edges) | Adjacency List |
| Frequent "does edge exist?" queries | Adjacency Matrix |
| Frequent "give me all neighbours" queries | Adjacency List |
| Memory is tight | Adjacency List |

> Most graph algorithms (BFS, DFS, Dijkstra) are designed around adjacency lists because real graphs are almost always sparse.

---

## 8. Exam Quick-Fire

**Q: Adjacency matrix space complexity?**
O(n²)

**Q: Adjacency list space complexity?**
O(V + E)

**Q: How to check if edge (i,j) exists in a matrix?**
A[i][j] == 1 → O(1)

**Q: How to check if edge (i,j) exists in a list?**
Scan AList[i] → O(deg(i))

**Q: What is a sparse graph?**
A graph where E << n² — far fewer edges than the theoretical maximum

**Q: For an undirected graph, what property does the adjacency matrix have?**
It is symmetric: A[i][j] = A[j][i]

**Q: What does the row sum of an adjacency matrix represent in a directed graph?**
The outdegree of that vertex
