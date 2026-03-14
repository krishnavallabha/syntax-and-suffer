# What the Graph Knows — Applications of BFS and DFS

---

## 1. Beyond Reachability

BFS and DFS both answer the basic question: **can we get from u to v?**

But they also reveal much deeper structure about the graph. This file covers the main applications tested in PDSA.

---

## 2. Connected Components (Undirected Graphs)

An undirected graph is **connected** if every vertex can reach every other. If not, it breaks into **connected components** — maximal subsets of vertices that are internally connected.

**Algorithm:**

1. Assign `component[v] = -1` for all vertices
2. Set `compid = 0`
3. While any unvisited vertex remains:
   - Find the smallest unvisited vertex
   - Run BFS/DFS from it
   - Label all visited vertices with `compid`
   - Increment `compid`

Each run of BFS/DFS from a new starting vertex discovers exactly one connected component.

**Example:**

```
Graph: {0-1-2}  {3-4}  {5}

Component 0: {0, 1, 2}
Component 1: {3, 4}
Component 2: {5}
```

**Complexity:** O(n + m) — each vertex and edge is processed once total across all BFS/DFS calls.

---

## 3. Cycle Detection

A **cycle** is a walk that starts and ends at the same vertex without repeating any edge.

A **simple cycle** only repeats the start/end vertex — all others appear once.

A graph is **acyclic** if it contains no cycles.

### In Undirected Graphs

Run BFS or DFS. If any **non-tree edge** is found (an edge leading to an already-visited vertex that is not the parent), a cycle exists.

```
A —— B —— C —— A    ← cycle detected when C tries to visit A (already visited)
```

### In Directed Graphs

Run DFS and compute pre/post numbers. A cycle exists if and only if a **back edge** is found.

| Edge type | Creates cycle? |
|-----------|---------------|
| Tree edge | No |
| Forward edge | No |
| Cross edge | No |
| **Back edge** | **Yes** |

**How to spot a back edge:** edge (u, v) is a back edge if v was entered before u and has not yet exited — i.e., pre[v] < pre[u] and post[v] > post[u].

---

## 4. Strongly Connected Components (Directed Graphs)

In a directed graph, two vertices u and v are **strongly connected** if there is a path from u to v **and** a path from v to u.

A **strongly connected component (SCC)** is a maximal set of vertices that are all pairwise strongly connected.

Every directed graph can be decomposed into SCCs. The SCCs form a DAG when collapsed into single nodes (the **condensation graph**).

**Computing SCCs:** DFS numbering (specifically post-order) can be used to identify SCCs efficiently. The standard algorithm is **Kosaraju's algorithm** — two DFS passes, one on the original graph and one on the reversed graph.

---

## 5. Articulation Points and Bridges

These are advanced applications of DFS numbering:

- **Articulation point (cut vertex):** a vertex whose removal disconnects the graph
- **Bridge (cut edge):** an edge whose removal disconnects the graph

Both can be identified in O(n + m) using DFS by tracking the earliest ancestor reachable from each subtree.

> These are typically mentioned as awareness topics in PDSA — know the definitions but detailed proofs are usually not required.

---

## 6. DFS Numbering Summary

Pre and post numbers enable classification of all graph edges and reveal structure that simple visited/unvisited tracking cannot.

| Property | How to detect using pre/post |
|----------|------------------------------|
| Tree / forward edge | [pre[v], post[v]] ⊆ [pre[u], post[u]] |
| Back edge | [pre[u], post[u]] ⊆ [pre[v], post[v]] |
| Cross edge | Intervals disjoint |
| Cycle exists | Any back edge found |
| Topological order | Sort vertices by decreasing post number |

---

## Exam Quick-Fire

**Q: How do you find connected components?**
Run BFS/DFS repeatedly from unvisited vertices, incrementing a component ID each time

**Q: How does BFS/DFS detect a cycle in an undirected graph?**
If a non-tree edge to an already-visited (non-parent) vertex is found

**Q: In a directed graph, which edge type indicates a cycle?**
Back edge — identified when post[v] > post[u] for edge (u, v)

**Q: What is a strongly connected component?**
A maximal set of vertices where every vertex can reach every other vertex

**Q: What is the condensation of a directed graph?**
The DAG formed by collapsing each SCC into a single node

**Q: Complexity of finding connected components?**
O(n + m) with adjacency list
