# The Minimal Web — Prim's & Kruskal's Algorithms

---

## 1. Spanning Trees

A **spanning tree** of a connected graph G = (V, E) is a subgraph that:
- Connects **all vertices**
- Contains **no cycles**
- Has exactly **n-1 edges**

Three equivalent ways to define a tree on n vertices — any two imply the third:
1. Connected and acyclic
2. Connected and has n-1 edges
3. Acyclic and has n-1 edges

**Key facts:**
- Adding any edge to a spanning tree **creates a cycle**
- Removing any edge from a spanning tree **disconnects the graph**
- Every pair of vertices is connected by **exactly one path** in a tree

---

## 2. Minimum Cost Spanning Tree (MCST)

In a weighted graph, each spanning tree has a total cost (sum of its edge weights).

A **Minimum Cost Spanning Tree (MCST)** is the spanning tree with the lowest total weight.

**Applications:** cheapest cable/pipe network connecting all nodes, minimum cost road restoration, cheapest network backbone.

> If all edge weights are distinct, the MCST is unique. If weights repeat, multiple MCSTs may exist.

---

## 3. The Minimum Separator Lemma

This lemma is the foundation of correctness for both Prim's and Kruskal's algorithms.

**Lemma:** Partition the vertices V into two non-empty sets U and W = V \ U. Let e = (u, w) be the **minimum cost edge** crossing from U to W. Then **every MCST must include e**.

**Proof sketch:** Suppose an MCST T does not include e. T is connected, so it has some path from u to w — this path must cross from U to W via some other edge f. Since e is the minimum crossing edge, cost(e) < cost(f). Replace f with e to get a cheaper spanning tree, contradicting T being minimum.

---

## 4. Prim's Algorithm

**Strategy:** Grow the MCST one vertex at a time, starting from any vertex.

At each step, add the **minimum cost edge** that connects a tree vertex to a non-tree vertex.

### Algorithm

**Initialise:**
- `visited[v] = False`, `distance[v] = ∞` for all v
- Start at vertex 0: `visited[0] = True`
- Set `distance[v]` = weight of edge (0, v) for all neighbours v of 0

**Repeat n-1 times:**
1. Find unvisited vertex `nextv` with minimum `distance`
2. Mark `visited[nextv] = True`
3. Add edge to tree
4. Update `distance[v]` for each unvisited neighbour v of `nextv`:
   - `distance[v] = min(distance[v], weight(nextv, v))`

### Example

```
Start at vertex 0.

Step 1: nearest unvisited vertex → add it and its edge
Step 2: nearest unvisited vertex from the growing tree → add
Step 3: continue until all vertices are in the tree
```

### Why It Works

At every step, the newly added edge is the minimum crossing edge between the current tree vertices (TV) and the rest (V \ TV). By the Minimum Separator Lemma, this edge must belong to the MCST.

### Complexity

| Implementation | Complexity | Bottleneck |
|----------------|------------|------------|
| Naive (scan all edges each step) | O(mn) | Scanning all edges to find next vertex |
| Track nearest neighbour per vertex | O(n²) | Scanning unvisited vertices for minimum distance |

> Like Dijkstra, the bottleneck is finding the minimum distance unvisited vertex. A priority queue improves this to **O((n + m) log n)**.

**Key difference from Dijkstra:** Dijkstra updates `distance[v] = distance[nextv] + edge_weight`. Prim's updates `distance[v] = edge_weight` alone — we track the cheapest edge to the tree, not the full path distance.

---

## 5. Kruskal's Algorithm

**Strategy:** Build the MCST bottom-up. Process all edges in ascending order of cost and add each one unless it would create a cycle.

### Algorithm

**Initialise:**
- Each vertex is its own component: `component[v] = v`
- Sort all edges by weight: e₀, e₁, ..., eₘ₋₁
- `TE = []` (tree edges so far)

**For each edge (u, v) in sorted order:**
- If `component[u] ≠ component[v]`:
  - Add (u, v) to TE
  - Merge the two components (all vertices in u's component now join v's component)
- If `component[u] == component[v]`: skip (would create a cycle)

**Stop** when n-1 edges have been added.

### Example

```
Edges sorted: (1,3,w=4), (2,4,w=5), (0,1,w=6), (0,3,w=7), (1,2,w=8)

Add (1,3): merges components {1} and {3}  →  TE = [(1,3)]
Add (2,4): merges {2} and {4}             →  TE = [(1,3),(2,4)]
Add (0,1): merges {0} and {1,3}           →  TE = [(1,3),(2,4),(0,1)]
Skip (0,3): 0 and 3 already in same component
Add (1,2): merges {0,1,3} and {2,4}       →  TE = [...,(1,2)]
Done — n-1 = 4 edges added.
```

### Why It Works

When edge e = (u, v) is processed, u and v are in different components. These components form a partition U and W = V \ U of the vertices. Since edges are processed in ascending order, e is the minimum cost edge crossing this partition. By the Minimum Separator Lemma, e must be in the MCST.

### Complexity

| Step | Cost |
|------|------|
| Sorting edges | O(m log m) = O(m log n) since m ≤ n² |
| Naive component merging | O(n) per merge × n merges = O(n²) |
| Total (naive) | O(n²) |
| With Union-Find data structure | O(m log n) |

**The bottleneck** is tracking and merging components. The naive approach — scan all vertices to relabel a component — costs O(n) per merge. A **Union-Find** (disjoint set) data structure reduces this to near O(1) per operation, bringing total complexity to **O(m log n)**.

---

## 6. Prim's vs Kruskal's

| Feature | Prim's | Kruskal's |
|---------|--------|-----------|
| Strategy | Grow one tree from a vertex | Merge components bottom-up |
| Processes | Vertices | Edges |
| Best for | Dense graphs (m ≈ n²) | Sparse graphs (m << n²) |
| Requires sorting | No | Yes — sort all edges |
| Complexity (basic) | O(n²) | O(n²) naive, O(m log n) with Union-Find |
| Correctness basis | Minimum Separator Lemma | Minimum Separator Lemma |

Both algorithms are **greedy** and both rely on the same Minimum Separator Lemma for correctness.

---

## Exam Quick-Fire

**Q: How many edges does a spanning tree on n vertices have?**
Exactly n-1

**Q: State the Minimum Separator Lemma.**
If V is partitioned into U and W, the minimum cost edge crossing from U to W must be in every MCST.

**Q: What is the key difference in the distance update between Prim's and Dijkstra?**
Dijkstra: distance[v] = distance[nextv] + edge_weight (full path cost). Prim's: distance[v] = edge_weight only (cheapest edge to the tree).

**Q: How does Kruskal's avoid cycles?**
By checking whether both endpoints are in the same component before adding an edge. Same component = cycle.

**Q: What data structure speeds up Kruskal's component merging?**
Union-Find (disjoint set), reducing total complexity to O(m log n)

**Q: If all edge weights are equal, is the MCST unique?**
No — any spanning tree would be minimum, and there are many spanning trees.
