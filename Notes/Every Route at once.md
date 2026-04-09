# Every Route at Once — Floyd-Warshall

---

## 1. All Pairs Shortest Paths

Instead of one fixed source, find the shortest path **between every pair of vertices**.

**Brute force approach:** Run Dijkstra or Bellman-Ford from each vertex.

- Dijkstra from every vertex: O(n³) with adjacency matrix
- Bellman-Ford from every vertex: O(mn²)

Floyd-Warshall achieves **O(n³)** with a cleaner, simpler structure — and handles negative edge weights (no negative cycles).

---

## 2. The Core Idea

Define **SP[i][j][k]** = length of the shortest path from i to j using only vertices {0, 1, ..., k-1} as **intermediate** vertices (i and j themselves are not restricted).

Build up the solution by gradually allowing more intermediate vertices.

**Base case (k = 0):** No intermediate vertices allowed. The only path from i to j is a direct edge.

```
SP[i][j][0] = W(i, j)     if edge exists
SP[i][j][0] = ∞           if no edge
```

**Recurrence:** When we allow vertex k as an intermediate:

```
SP[i][j][k] = min(
    SP[i][j][k-1],                    ← don't use k
    SP[i][k][k-1] + SP[k][j][k-1]    ← go through k
)
```

Either the best path from i to j ignoring k is still best, or it is better to go through k.

**Final answer:** SP[i][j][n] = shortest path between every pair using all vertices as potential intermediates.

---

## 3. Connection to Warshall's Algorithm

Warshall's algorithm computes **transitive closure** — whether any path exists from i to j:

```
B[i][j][k] = 1  if there is any path from i to j using {0,...,k-1} as intermediates
```

Floyd-Warshall is the same structure but tracking **shortest distance** instead of just reachability.

---

## 4. Implementation Notes

A naive implementation stores an n × n × (n+1) matrix — O(n³) space.

**Space optimisation:** At each step k, SP[i][j][k] only depends on SP values from step k-1. We can maintain **two n × n slices** — the current and previous — and copy between them. This reduces space to **O(n²)**.

---

## 5. Complexity

| | Value |
|--|-------|
| Time | O(n³) — three nested loops over n vertices |
| Space (full) | O(n³) |
| Space (optimised) | O(n²) |

Works with negative edge weights. If a negative cycle exists, SP[i][i] will become negative for some vertex i (a path from i back to i with negative total cost).

---

## 6. Comparison of All Shortest Path Algorithms

| Algorithm | Type | Negative edges | Complexity | Notes |
|-----------|------|----------------|------------|-------|
| BFS | Single source | No (unweighted) | O(n + m) | Counts edges, not weights |
| Dijkstra | Single source | No | O(n²) | Greedy, fast |
| Bellman-Ford | Single source | Yes | O(mn) | Detects negative cycles |
| Floyd-Warshall | All pairs | Yes | O(n³) | Clean DP structure |

---

## Exam Quick-Fire

**Q: What does SP[i][j][k] represent in Floyd-Warshall?**
The shortest path from i to j using only vertices {0, 1, ..., k-1} as intermediates

**Q: What is the recurrence in Floyd-Warshall?**
SP[i][j][k] = min(SP[i][j][k-1], SP[i][k][k-1] + SP[k][j][k-1])

**Q: What is the time complexity of Floyd-Warshall?**
O(n³)

**Q: How can you detect a negative cycle using Floyd-Warshall?**
Check the diagonal — if SP[i][i] < 0 for any i, a negative cycle exists

**Q: What is the space-optimised version of Floyd-Warshall?**
O(n²) — maintain only two n × n slices at a time instead of the full n³ matrix
