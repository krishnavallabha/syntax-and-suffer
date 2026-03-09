# The Memory Game — Arrays vs Linked Lists

---

## 1. What is a Sequence?

A sequence is an **ordered collection of values** that supports operations like:

- access element A[i]
- insert values
- delete values
- swap elements
- search

There are two fundamental ways to store a sequence in memory:

```
1. Arrays        — contiguous memory
2. Linked Lists  — scattered nodes connected by pointers
```

The choice between them is one of the most important decisions in algorithm design. Each has a completely different performance profile.

---

## 2. Arrays

Elements are stored in **contiguous (adjacent) memory blocks**.

```
Address 1000 → 10
Address 1004 → 20
Address 1008 → 30
Address 1012 → 40
```

Because the spacing between elements is fixed, we can compute any element's address directly:

```
Address(A[i]) = base_address + i × element_size
```

This is called **random access** — we jump straight to any index in O(1).

### Advantages

**Fast access:** A[i] is always O(1) regardless of i.

**Cache friendly:** Contiguous memory means the CPU cache loads nearby elements together, making repeated access very fast in practice.

**Binary search works well:** Jumping to the midpoint is instant.

### Disadvantages

**Insertion is expensive:** Inserting at index i requires shifting all elements after i one position to the right.

```
Insert 25 at index 2:

Before:  [10, 20, 30, 40]
Shift:   [10, 20, __, 30, 40]
Insert:  [10, 20, 25, 30, 40]
```

Cost: O(n)

**Fixed size:** Traditional arrays must declare size upfront. Resizing requires allocating new memory and copying everything over.

---

## 3. Linked Lists

Elements are stored as **nodes** scattered anywhere in memory, connected by pointers.

```
Head
 ↓
[10 | *] → [20 | *] → [30 | *] → None
```

Each node contains:
- a **value**
- a **pointer** to the next node

Memory is not contiguous. Nodes can be at completely different addresses.

### Advantages

**Flexible size:** Nodes are allocated on demand. No need to declare size in advance.

**Fast insertion/deletion (at a known node):** Just update the pointers. No shifting required.

```
Insert 25 between 20 and 30:

Before:  10 → 20 → 30 → 40
After:   10 → 20 → 25 → 30 → 40
```

Only two pointer updates needed → O(1)

### Disadvantages

**Slow access:** To reach A[i], you must follow the chain from the head.

```
Find A[3]:  Head → 10 → 20 → 30 → 40
```

Cost: O(i), worst case O(n)

**No binary search:** Jumping to the midpoint requires traversing n/2 nodes — O(n). Binary search loses its advantage entirely.

**Extra memory:** Every node stores a pointer in addition to its value.

---

## 4. Operation Comparison

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access A[i] | O(1) | O(n) |
| Insert at known position | O(n) | O(1) |
| Delete at known position | O(n) | O(1) |
| Swap A[i], A[j] | O(1) | O(n) |
| Search (unsorted) | O(n) | O(n) |
| Binary Search | O(log n) | O(n) |

### Why swapping is O(n) in linked lists

In an array: `A[i], A[j] = A[j], A[i]` — direct index access, O(1).

In a linked list: you must **find both nodes first** by traversing from the head. Finding them costs O(n), even if the swap itself is just pointer manipulation.

---

## 5. The Binary Search Problem

Binary search computes the midpoint at each step:

```
mid = (low + high) // 2
access A[mid]
```

With an **array**, A[mid] is O(1). Total complexity: O(log n).

With a **linked list**, reaching the midpoint requires traversing n/2 nodes — O(n) per step.

```
Binary search + array       →  O(log n)
Binary search + linked list →  O(n log n)  ← worse than linear search
```

> This is why binary search is only ever used with arrays.

---

## 6. Python Lists — Not What the Name Suggests

Despite the name, **Python lists are dynamic arrays**, not linked lists.

- Stored in contiguous memory
- Support O(1) random access via L[i]
- Resize automatically when full

### How Python lists grow

When the array fills up:

1. Allocate a larger array (roughly double the size)
2. Copy all elements over — O(n)
3. Discard the old array

Growth sequence: 4 → 8 → 16 → 32 → ...

Resizing is expensive but happens rarely. The **amortized cost** of append works out to O(1).

| Operation | Complexity |
|-----------|------------|
| L[i] access | O(1) |
| append | O(1) amortized |
| insert at index i | O(n) |
| delete at index i | O(n) |
| pop from end | O(1) |

---

## 7. NumPy Arrays

NumPy provides **true fixed-type arrays** built for numerical computing.

```python
import numpy as np
A = np.array([10, 20, 30, 40])
```

**Why NumPy is faster than Python lists:**
- All elements are the same type (no type-checking overhead)
- Stored in contiguous memory like a C array
- Operations are implemented in optimised C code
- Supports **vectorised operations** — apply an operation to the whole array without a Python loop

```python
# Without NumPy:
result = [x * 3 for x in L]       # Python loop, slow

# With NumPy:
result = A * 3                      # C-level operation, fast
```

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| Element types | mixed | same type only |
| Speed | slower | much faster |
| Matrix operations | manual loops | built-in |
| Memory | more overhead | compact |
| Best for | general use | numerical computing |

---

## 8. Full Summary

### Choose an Array when:
- You need fast access by index
- You are doing binary search
- Data size is known or mostly stable

### Choose a Linked List when:
- You need frequent insertions or deletions in the middle
- Data size is unpredictable
- You do not need random access

---

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory layout | contiguous | scattered |
| Access | O(1) | O(n) |
| Insert / Delete | O(n) | O(1) |
| Binary Search | O(log n) | unusable |
| Cache performance | good | poor |
| Size flexibility | fixed (or costly resize) | dynamic |
