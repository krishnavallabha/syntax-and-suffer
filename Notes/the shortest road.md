# The Shortest Road — Dijkstra & Bellman-Ford

---

## 1. Weighted Graphs

In a weighted graph, each edge carries a **cost, distance, or time**:

```
G = (V, E),  W : E → R
```

BFS finds shortest paths by **number of edges**. In a weighted graph we want the path with **minimum total weight** — which may not have the fewest edges.

```
Path A → B → C   weights: 1 + 1 = 2
Path A → C        weight: 5

Fewer edges (1) but heavier. Minimum weight path uses 2 edges.
```

**Adjacency matrix:** store the weight at A[i][j] instead of just 0/1. Use ∞ if no edge exists.

**Adjacency list:** store pairs (neighbour, weight) instead of just neighbour.

---

## 2. Types of Shortest Path Problems

| Problem | Goal |
|---------|------|
| Single source | Shortest path from one fixed vertex to all others |
| All pairs | Shortest path between every pair of vertices |

Real examples: factory to all retail outlets (single source), optimal routes between all cities (all pairs).

---

## 3. Negative Edge Weights

Negative weights can be meaningful (e.g. a road where you profit by driving it). They are allowed **as long as there are no negative cycles**.

A **negative cycle** is a cycle whose total weight is negative. Traversing it repeatedly would keep decreasing the path cost indefinitely — shortest path becomes undefined.

> **Rule:** Negative edge weights are fine. Negative cycles are not.

---

## 4. Dijkstra's Algorithm

Handles graphs with **non-negative edge weights only**.

### Intuition — The Burning Oil Depot

Imagine vertices are oil depots connected by pipelines. Set fire to the source depot. Fire travels at uniform speed along each pipeline (proportional to edge weight). The first unburnt depot to catch fire is the nearest one. The second is the next nearest. Continue until all depots have burnt.

Each time a new vertex "burns", update the expected burn time of its neighbours.

### Algorithm

**Initialise:**
- `visited[v] = False` for all v
- `distance[v] = ∞` for all v
- `distance[source] = 0`

**Repeat n times:**
1. Find the unvisited vertex `nextv` with minimum `distance`
2. Mark `visited[nextv] = True`
3. For each neighbour `v` of `nextv`:
   - `distance[v] = min(distance[v], distance[nextv] + weight(nextv, v))`

### Why It Works (Greedy Correctness)

By induction, assume all burnt vertices have their true shortest distance.

When the next vertex `v` is chosen (minimum distance unvisited), its distance cannot be improved later — any alternative path would have to pass through another unvisited vertex, which has distance ≥ distance[v] (since we always pick the minimum), and all edge weights are non-negative.

> **This argument breaks down with negative edges** — a later vertex could provide a cheaper path back, invalidating the frozen distance.

### Complexity

| Representation | Complexity | Bottleneck |
|----------------|------------|------------|
| Adjacency Matrix | O(n²) | Finding min-distance vertex: O(n) per iteration × n iterations |
| Adjacency List | O(n²) | Same bottleneck — finding the minimum is still O(n) |

> With adjacency lists, distance updates cost O(m) total, but finding the minimum unvisited vertex each iteration still costs O(n). A priority queue (min-heap) improves this to **O((n + m) log n)** — covered later.

---

## 5. Bellman-Ford Algorithm

Handles graphs with **negative edge weights** (but no negative cycles).

### Key Insight

Every shortest path uses at most **n-1 edges** (a path with n or more edges must revisit a vertex, forming a cycle — which can only make things worse if there are no negative cycles).

Every prefix of a shortest path is itself a shortest path. So:
- After 1 round of updates: all shortest paths using ≤ 1 edge are correct
- After 2 rounds: all shortest paths using ≤ 2 edges are correct
- After n-1 rounds: all shortest paths are correct

### Algorithm

**Initialise:**
- `distance[source] = 0`
- `distance[v] = ∞` for all other v

**Repeat n-1 times:**
- For every edge (u, v) in the graph:
  - `distance[v] = min(distance[v], distance[u] + weight(u, v))`

**Detect negative cycles:** Run one more (nth) iteration. If any distance still decreases, a negative cycle exists.

### Complexity

| Representation | Complexity | Why |
|----------------|------------|-----|
| Adjacency Matrix | O(n³) | n-1 outer iterations × O(n²) to scan all edges |
| Adjacency List | O(mn) | n-1 outer iterations × O(m) to scan all edges |

---

## 6. Dijkstra vs Bellman-Ford

| Feature | Dijkstra | Bellman-Ford |
|---------|----------|--------------|
| Negative edges | Not allowed | Allowed |
| Negative cycles | Not detected | Detected |
| Complexity (list) | O(n²) | O(mn) |
| Strategy | Greedy | Iterative relaxation |
| Correctness | Greedy induction | n-1 rounds guarantee |

> Dijkstra is faster when all weights are non-negative. Bellman-Ford is more general but slower.

---

## Exam Quick-Fire

**Q: Why can't Dijkstra handle negative edge weights?**
Once a vertex is marked visited, its distance is frozen. A negative edge could later provide a cheaper path, invalidating the frozen value.

**Q: How does Bellman-Ford detect a negative cycle?**
Run an extra nth iteration. If any distance decreases, a negative cycle exists.

**Q: What is the complexity of Dijkstra with adjacency matrix?**
O(n²)

**Q: What is the complexity of Bellman-Ford with adjacency list?**
O(mn)

**Q: Why does Bellman-Ford run exactly n-1 iterations?**
The longest possible shortest path has n-1 edges. After n-1 rounds, all such paths have stabilised.
