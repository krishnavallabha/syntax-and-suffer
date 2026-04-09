# The Priority Line — Heaps & Priority Queues

---

## 1. The Problem

A **priority queue** maintains a collection of items with priorities and supports:

| Operation | Meaning |
|-----------|---------|
| `insert(x)` | Add a new item |
| `delete_max()` | Remove and return the item with the highest priority |

**Applications:** job schedulers, Dijkstra's algorithm, Prim's algorithm, heap sort.

---

## 2. Why Not a Simple List?

| Structure | insert | delete_max | n operations |
|-----------|--------|------------|--------------|
| Unsorted list | O(1) | O(n) — scan all | O(n²) |
| Sorted list | O(n) — find position | O(1) | O(n²) |
| √N × √N array | O(√N) | O(√N) | O(N√N) |
| **Heap** | **O(log N)** | **O(log N)** | **O(N log N)** |

We need something better than O(n²) for n operations.

---

## 3. Binary Trees — Background

A **binary tree** is a rooted tree where each node has at most two children (left and right).

- **Leaf node:** no children
- **Height:** number of levels
- A binary tree with k full levels has 2⁰ + 2¹ + ... + 2^(k-1) = 2^k - 1 nodes
- A tree with N nodes has at most **1 + log N levels** (height = O(log N))

---

## 4. The Heap

A **heap** is a binary tree with two structural properties:

**1. Shape property:** Filled level by level, left to right. All levels are completely filled except possibly the last, which is filled from the left.

**2. Heap property (max-heap):** The value at each node is **≥** the values of both its children.

```
        90
       /  \
      80   70
     / \   /
    60  50 40
```

The root always holds the **maximum value** — by the heap property, no child can be larger than its parent, so the maximum propagates to the root.

A **min-heap** inverts the condition: each node is ≤ its children. The root holds the minimum.

---

## 5. Heap as an Array

A heap can be stored compactly as a flat array, numbered top-to-bottom, left-to-right:

```
H = [h₀, h₁, h₂, h₃, h₄, h₅, ...]

Children of H[i]:   H[2i+1]  and  H[2i+2]
Parent of H[i]:     H[(i-1)//2]    (for i > 0)
```

No pointers needed. This is both space-efficient and cache-friendly.

---

## 6. insert() — O(log N)

1. Add the new element at the **end** of the array (next available position at the bottom level)
2. **Bubble up:** Compare with parent. If larger than parent, swap. Repeat until heap property is restored.

```
Insert 85 into heap:

Add at end → [..., 85]
85 > parent(60) → swap
85 > parent(80) → swap
85 < parent(90) → stop
```

At most O(log N) swaps — one per level from leaf to root.

---

## 7. delete_max() — O(log N)

1. The maximum is always at the **root** — record it
2. Move the **last element** (rightmost at lowest level) to the root
3. Remove the last position (shrink heap by 1)
4. **Bubble down (heapify down):** Compare root with its children. Swap with the larger child if it is greater. Repeat until heap property is restored.

```
Remove root (90):

Move last element to root → [85, 80, 70, 60, 50, 40]
85 > children → already heap property satisfied (example)
```

At most O(log N) swaps — one per level from root to leaf.

---

## 8. heapify() — Building a Heap in O(N)

**Naive approach:** Insert each of N elements one by one → O(N log N).

**Better approach:** Start with the raw array. The second half (indices ≥ N//2) are all leaf nodes — they already satisfy the heap property trivially. Work backwards from the middle, applying bubble-down at each node.

**Why O(N)?** The cost analysis:

```
Level k from bottom has N/2^(k+1) nodes, each needs at most k swaps.

Total = N/4 × 1 + N/8 × 2 + N/16 × 3 + ...  =  O(N)
```

Nodes near the bottom (most of them) only need a few swaps. The sum converges to O(N).

> This is better than inserting one by one. heapify() builds a heap in **O(N)** regardless of the input.

---

## 9. Heap Sort — O(N log N) in-place

Use the heap structure to sort a list without extra memory:

1. **heapify()** the array — O(N)
2. Repeat N times:
   - Call **delete_max()** — O(log N) — this removes the largest element
   - Store it at the **end** of the current heap (the freed slot after shrinking)

After N deletions, the array is sorted in ascending order, entirely in-place.

**Total: O(N) + N × O(log N) = O(N log N)**

---

## 10. Heaps in Dijkstra's Algorithm

Dijkstra's bottleneck is: **find the unvisited vertex with minimum distance** — O(n) naively.

With a min-heap of (distance, vertex) pairs:
- `delete_min()` gives the next vertex in O(log n)
- When a neighbour's distance is updated, the heap value must change — this requires **updating a value inside the heap**, which is not a standard operation

To support updates, maintain extra pointers mapping vertices to their heap positions. With this extension, each update costs O(log n).

| Algorithm version | Complexity |
|-------------------|------------|
| Dijkstra, naive find-min | O(n²) |
| Dijkstra, with min-heap | O((m + n) log n) |

---

## 11. Complexity Summary

| Operation | Complexity |
|-----------|------------|
| insert | O(log N) |
| delete_max / delete_min | O(log N) |
| heapify (build heap) | O(N) |
| heap sort | O(N log N) |

---

## Exam Quick-Fire

**Q: What two properties define a heap?**
Shape property (filled left-to-right) and heap property (parent ≥ children for max-heap)

**Q: Where is the maximum always found in a max-heap?**
At the root

**Q: What are the children of H[i] in an array-based heap?**
H[2i+1] and H[2i+2]

**Q: Why is heapify() O(N) and not O(N log N)?**
Most nodes are near the bottom and need only a few swaps. The weighted sum of work per level converges to O(N).

**Q: Why can't we directly use a heap in Dijkstra without modification?**
Updating a distance inside the heap is not a standard heap operation — extra pointers are needed to locate and update internal nodes

**Q: What is the complexity of Dijkstra with a min-heap?**
O((m + n) log n)
