# Go Deep — Depth First Search

---

## 1. The Core Idea

DFS explores a graph by going **as deep as possible** before backtracking.

From the current vertex, immediately move to an unvisited neighbour. If no unvisited neighbours exist, backtrack to the most recently visited vertex that still has unexplored neighbours.

```
Visit → go deeper → go deeper → dead end → backtrack → try next neighbour
```

Suspended vertices are stored in a **stack (LIFO)** — either explicitly, or implicitly via recursion.

---

## 2. Algorithm (Recursive)

DFS is most naturally expressed recursively. The call stack acts as the implicit stack.

**Steps:**
1. Mark current vertex v as visited
2. For each neighbour k of v:
   - If k is not visited:
     - Set `parent[k] = v`
     - Recursively call DFS(k)

**Initialisation** is kept separate — set `visited[v] = False` and `parent[v] = -1` for all vertices before the first call.

---

## 3. Pre and Post Numbers

DFS can record the **order of entry and exit** for each vertex using a counter:

- `pre[v]` — counter value when DFS **first visits** v (entry time)
- `post[v]` — counter value when DFS **finishes exploring** v (exit time)

The counter increments each time a vertex is entered or exited.

**Interval notation:** vertex v "owns" the interval [pre[v], post[v]].

These intervals have a key structural property:

> For any two vertices u and v, their intervals are either **completely nested** or **completely disjoint** — they never partially overlap.

---

## 4. Types of Edges in DFS

When DFS runs on a directed graph, every edge (u, v) falls into exactly one category:

| Edge Type | Meaning | Interval relationship |
|-----------|---------|----------------------|
| Tree edge | v was first discovered via u | [pre[v], post[v]] inside [pre[u], post[u]] |
| Forward edge | u → v, v is a descendant but not direct child | [pre[v], post[v]] inside [pre[u], post[u]] |
| Back edge | u → v, v is an **ancestor** of u | [pre[u], post[u]] inside [pre[v], post[v]] |
| Cross edge | u → v, no ancestor/descendant relationship | Intervals are **disjoint** |

**The critical fact for cycle detection:**

> **Only back edges create cycles.** A directed graph has a cycle if and only if DFS finds a back edge.

---

## 5. Complexity

Same structure as BFS — each vertex is visited and explored exactly once.

| Representation | Complexity | Why |
|----------------|------------|-----|
| Adjacency Matrix | O(n²) | Exploring vertex v scans all n entries of its row |
| Adjacency List | O(n + m) | Only actual neighbours are examined |

---

## 6. BFS vs DFS

| Feature | BFS | DFS |
|---------|-----|-----|
| Data structure | Queue (FIFO) | Stack / Recursion (LIFO) |
| Exploration order | Level by level | Deep first |
| Finds shortest paths? | Yes | No |
| Natural implementation | Iterative | Recursive |
| Complexity (list) | O(n + m) | O(n + m) |
| Used for | Shortest paths, connectivity | Cycle detection, SCCs, topological sort |

---

## Exam Quick-Fire

**Q: What data structure does DFS use?**
Stack — LIFO (implicit via recursion)

**Q: Does DFS find shortest paths?**
No — DFS paths are not guaranteed to be shortest

**Q: Which type of non-tree edge indicates a cycle in a directed graph?**
Back edge only

**Q: How do you identify a back edge using pre/post numbers?**
Edge (u, v) is a back edge if [pre[u], post[u]] is contained inside [pre[v], post[v]] — v was entered before u and exits after u

**Q: What is the complexity of DFS with adjacency list?**
O(n + m)
