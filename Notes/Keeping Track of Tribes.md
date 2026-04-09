# Keeping Track of Tribes — Union-Find

---

## 1. The Problem

Kruskal's algorithm needs to efficiently answer two questions at every step:

1. Are vertices u and v in the **same component**?
2. If not, **merge** their components.

This is the **Union-Find** (or Disjoint Set Union) problem.

---

## 2. Operations

| Operation | Meaning |
|-----------|---------|
| `MakeUnionFind(S)` | Initialise — each element is its own singleton component |
| `Find(v)` | Return the component containing v |
| `Union(u, v)` | Merge the components of u and v |

---

## 3. Naive Implementation

Use a single array `Component` where `Component[i]` = the label of i's component.

**MakeUnionFind:** Set `Component[i] = i` for all i.

**Find(i):** Return `Component[i]` — O(1).

**Union(i, j):** Find the old component label, scan the entire array, relabel all members of i's component to j's label — **O(n)**.

| Operation | Complexity |
|-----------|------------|
| MakeUnionFind | O(n) |
| Find | O(1) |
| Union | O(n) |
| m Union operations | O(mn) |

For Kruskal's with m edges, this gives O(mn) — too slow.

---

## 4. Improved Implementation — Members List

Add a `Members[c]` list for each component c (the list of all vertices in that component) and `Size[c]` to track component size.

**Union(i, j):** Instead of scanning all n vertices, only scan `Members[c_old]` and relabel just those — cost is **O(Size[c_old])** instead of O(n).

**The key optimisation — always merge smaller into larger:**

When merging, always relabel the **smaller** component into the larger one.

**Why this helps:** Every time a vertex is relabelled, its component at least **doubles in size** (since we merged smaller into larger). A component can only double log n times before it reaches size n. Therefore, each vertex is relabelled **at most O(log n)** times across all operations.

**Amortised analysis:**
- m Union operations touch at most 2m vertex-relabellings total
- Each relabelling costs O(1)
- Over all m operations: **O(m log n)** total, so **O(log n) amortised per Union**

| Operation | Complexity |
|-----------|------------|
| MakeUnionFind | O(n) |
| Find | O(1) |
| Union (amortised) | O(log n) |
| m Union operations | O(m log n) |

---

## 5. Kruskal's with Union-Find

| Step | Cost |
|------|------|
| Sort edges | O(m log m) = O(m log n) since m ≤ n² |
| n-1 Union operations | O(n log n) amortised |
| m Find operations | O(m) |
| **Total** | **O((m + n) log n)** |

> With an even more advanced Union-Find using trees (union by rank + path compression), Union becomes effectively O(1) amortised, but O(log n) is sufficient for this course.

---

## Exam Quick-Fire

**Q: What two operations must Union-Find support?**
Find(v) — return component of v; Union(u, v) — merge their components

**Q: Why is naive Union O(n)?**
Must scan all n vertices to relabel the old component

**Q: What optimisation reduces Union to O(log n) amortised?**
Always merge the smaller component into the larger one

**Q: Why does each vertex get relabelled at most O(log n) times?**
Each relabelling at least doubles the component size — a component can only double O(log n) times before reaching size n

**Q: What is the overall complexity of Kruskal's with efficient Union-Find?**
O((m + n) log n)
