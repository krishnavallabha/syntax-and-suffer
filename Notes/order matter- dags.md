# Order Matters — DAGs, Topological Sort & Longest Paths

---

## 1. Directed Acyclic Graphs (DAGs)

A **DAG** is a directed graph with **no directed cycles**.

```
G = (V, E),  directed,  no cycle exists
```

DAGs naturally model **dependency relationships** — situations where some tasks must be completed before others can begin.

**Real examples:**
- Course prerequisites (must pass Maths before taking Algorithms)
- Build systems (compile module A before module B)
- Project scheduling (lay conduits before plastering walls)
- Recipe steps (chop vegetables before cooking)

In a DAG, if there is a path from i to j, there is **no path back** from j to i.

---

## 2. Topological Sort

A **topological ordering** of a DAG is a linear arrangement of all vertices such that for every edge (i, j), vertex i appears **before** j in the list.

```
If i → j exists, then i comes before j in the ordering.
```

This represents a **valid schedule** — every task is listed after all its dependencies.

**Key facts:**
- A topological sort exists **if and only if** the graph is a DAG (no cycles)
- A graph with a cycle cannot be topologically sorted — circular dependencies have no valid start
- There may be **multiple valid** topological orderings

---

## 3. Algorithm — Topological Sort

The algorithm is based on a simple observation:

> **Every DAG has at least one vertex with indegree 0** (no incoming edges — no dependencies).

**Proof:** Start at any vertex and follow edges backwards. After n steps we must revisit a vertex, creating a cycle — but DAGs have no cycles. So we must reach a vertex with no incoming edges within n steps.

**Algorithm (Kahn's algorithm):**

1. Compute `indegree[v]` for all vertices
2. Enqueue all vertices with `indegree = 0`
3. While queue is not empty:
   - Dequeue vertex j, add to result list
   - For each neighbour k of j:
     - Decrement `indegree[k]`
     - If `indegree[k]` becomes 0, enqueue k
4. Return result list

Each time a vertex is listed and removed, its outgoing edges are deleted. The remaining graph is still a DAG, so a new vertex with indegree 0 will always emerge (if any remain).

**Example:**

```
Tasks: A → B → D
       A → C → D

indegree: A=0, B=1, C=1, D=2

Step 1: List A (indegree 0) → B and C become indegree 0
Step 2: List B → D becomes indegree 1
Step 3: List C → D becomes indegree 0
Step 4: List D

Valid ordering: A, B, C, D  (or A, C, B, D)
```

---

## 4. Complexity — Topological Sort

| Implementation | Complexity | Reason |
|----------------|------------|--------|
| Adjacency Matrix | O(n²) | Scanning columns to compute indegrees: O(n²). Finding next zero-indegree vertex: O(n) per step × n steps |
| Adjacency List | O(n + m) | Computing indegrees by scanning lists: O(m). Queue operations and indegree updates: O(n + m) total |

---

## 5. Longest Path in a DAG

**Problem:** Given a DAG where each edge represents a task or time unit, find the longest path from any source.

**Why this matters:** In project scheduling, the longest path is the **critical path** — the minimum time needed to complete all tasks. You cannot do better no matter how much you parallelise.

**Key insight:** Process vertices in **topological order**. When computing the longest path to vertex k, all predecessors of k have already been processed.

**Algorithm:**

1. Initialise `lpath[v] = 0` for all v
2. Run topological sort
3. When vertex j is dequeued:
   - For each neighbour k of j:
     - Update: `lpath[k] = max(lpath[k], lpath[j] + 1)`
     - Decrement indegree; if 0, enqueue k

This is computed **in parallel with topological sort** — no extra pass needed.

**Example:**

```
A → B → D
A → C → D

lpath[A] = 0
lpath[B] = 1  (from A)
lpath[C] = 1  (from A)
lpath[D] = 2  (from B or C, both give 2)

Longest path = 2
```

**Complexity:** O(n + m) with adjacency list — same as topological sort.

---

## 6. Longest Paths in General Graphs

In a DAG, longest paths are easy because topological order guarantees predecessors are processed first.

In a general directed graph (with cycles), this guarantee breaks down. No efficient algorithm is known — the problem is **NP-hard** in general. The only known approach is exhaustive enumeration of all paths.

This is one of the fundamental differences between DAGs and general graphs.

---

## 7. Summary

| Concept | Key Point |
|---------|-----------|
| DAG | Directed graph, no cycles |
| Topological sort | Linear order respecting all dependencies |
| Existence condition | Possible iff graph is a DAG |
| Multiple orderings | Usually yes — depends on structure |
| Critical observation | Every DAG has a vertex with indegree 0 |
| Longest path in DAG | Computed in O(n + m) alongside topological sort |
| Longest path in general graph | NP-hard — no efficient algorithm known |

---

## Exam Quick-Fire

**Q: What is a DAG?**
A directed graph with no directed cycles

**Q: When does a topological sort exist?**
If and only if the graph is a DAG

**Q: Why does every DAG have a vertex with indegree 0?**
If every vertex had indegree > 0, following edges backward would force a cycle, contradicting the DAG property

**Q: Complexity of topological sort with adjacency list?**
O(n + m)

**Q: What is the longest path in a DAG used for in scheduling?**
It gives the critical path — the minimum total time regardless of parallelisation

**Q: Why can't we compute longest paths efficiently in general graphs?**
Cycles mean there is no topological order, and the problem becomes NP-hard
