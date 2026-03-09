# Chains, Piles & Pipes — Linked Lists, Stacks, Queues & Hash Tables

---

## Part 1 — Linked Lists

### Structure

A linked list is a chain of nodes. Each node holds a value and a pointer to the next node.

```
Head
 ↓
[5 | *] → [10 | *] → [15 | *] → None
```

An empty list is a single node with value = None and next = None.

### Core Operations

**Append (add to end)**

Traverse the entire list to find the last node, then attach a new node.

```
5 → 10 → 15         append 20
5 → 10 → 15 → 20
```

Cost: O(n) — must walk the whole chain.

**Insert at head**

The head node cannot simply be replaced (other parts of the program hold a reference to it). Instead:

1. Create a new node
2. Swap values between the new node and the head
3. Relink the pointers

```
Original:  [5] → [10] → [15]
Insert 2:  [2] → [5]  → [10] → [15]
```

Cost: O(1) — no traversal needed.

**Delete a value**

To remove a node, we must update the *previous* node's pointer to skip over it. This means we look one node ahead while traversing.

```
5 → 10 → 15 → 20     delete 15
5 → 10 → 20
```

Special case: deleting the head — copy the next node's value into the head, then skip the next node.

Cost: O(n) — must find the node first.

### Complexity Summary

| Operation | Complexity |
|-----------|------------|
| Access element | O(n) |
| Append | O(n) |
| Insert at head | O(1) |
| Delete | O(n) |

### Why Linked Lists Matter

Many important data structures are built from linked lists:
- Stacks and Queues
- Adjacency lists in graphs
- Hash table chaining (see Part 4)

---

## Part 2 — Stacks

### Concept

A stack follows **LIFO — Last In, First Out**.

Think of a stack of plates. You always add and remove from the top.

```
push(5)   push(10)   push(20)

    TOP
     ↓
    [20]
    [10]
    [5]

pop() → removes 20
```

### Operations

| Operation | Action |
|-----------|--------|
| push(x) | Add element to top |
| pop() | Remove and return top element |
| peek() | View top element without removing |
| isempty() | Check if stack is empty |

### Complexity

All stack operations are **O(1)** because everything happens at one end (the top of the list, which is the last index in a Python list).

### Applications

**Parentheses / bracket matching**

Push every opening bracket. When a closing bracket is found, pop and check if they match.

```
Input: ((a + b) * (c - d))

Push (    →  stack: [( ]
Push (    →  stack: [(, (]
See  )    →  pop (  → matched
Push (    →  stack: [(, (]
See  )    →  pop (  → matched
See  )    →  pop (  → matched
Stack empty → all matched ✓
```

**Function call stack**

Every time a function is called, the program pushes its context (local variables, return address) onto the call stack. When the function returns, it is popped off. This is why infinite recursion causes a "stack overflow".

**Undo / Redo**

Each action is pushed onto a stack. Ctrl+Z pops the last action and reverses it.

**DFS (Depth-First Search)**

Graph traversal uses a stack to track which node to visit next (covered in Week 4).

---

## Part 3 — Queues

### Concept

A queue follows **FIFO — First In, First Out**.

Think of a line at a ticket counter. The first person in line is the first served.

```
enqueue(5)   enqueue(10)   enqueue(20)

Front → [5] → [10] → [20] ← Rear

dequeue() → removes 5
```

### Operations

| Operation | Action |
|-----------|--------|
| enqueue(x) | Add element to rear |
| dequeue() | Remove element from front |
| front() | View front element |
| isempty() | Check if queue is empty |

### The Problem with List-Based Queues

Using `list.pop(0)` to dequeue requires shifting every remaining element one position left — O(n).

The solution is Python's `collections.deque` (double-ended queue), which supports O(1) operations at both ends.

```python
from collections import deque

q = deque()
q.append(10)      # enqueue — O(1)
q.popleft()       # dequeue — O(1)
```

### Complexity (with deque)

| Operation | Complexity |
|-----------|------------|
| enqueue | O(1) |
| dequeue | O(1) |
| front | O(1) |

### Applications

**BFS (Breadth-First Search)**

Graph traversal visits nodes level by level, using a queue to track the next node to process (covered in Week 4).

**CPU Scheduling**

Operating systems process tasks in arrival order using queues.

**Printer spooling**

Print jobs are queued and processed in submission order.

---

## Stack vs Queue

| Feature | Stack | Queue |
|---------|-------|-------|
| Rule | LIFO | FIFO |
| Insert at | Top | Rear |
| Remove from | Top | Front |
| Graph use | DFS | BFS |
| Real example | Browser back button | Printer queue |

---

## Part 4 — Hash Tables & Python Dictionaries

### The Problem

Searching through a list is O(n). We want **O(1) lookup** regardless of how many items are stored.

### The Idea: Hash Tables

A hash table converts a key into an array index using a **hash function**:

```
key → hash(key) → array index → value
```

Example:

```
hash("cat") = 2   →   array[2] = "meow"
hash("dog") = 5   →   array[5] = "woof"
```

Lookup is O(1) because array access by index is O(1).

### Collisions

Two different keys may hash to the same index:

```
hash("cat") = 2
hash("bat") = 2   ← collision
```

Two standard strategies to handle this:

**1. Chaining (Open Hashing)**

Each slot holds a linked list of all key-value pairs that hash there.

```
index 2 → [("cat", "meow"), ("bat", "squeak")]
```

Lookup traverses the short list at that slot. Average case stays O(1) if the hash function distributes keys evenly.

**2. Open Addressing (Closed Hashing)**

If a slot is occupied, probe the next available slot:

```
index 2 → full
index 3 → free → insert here
```

Common probing strategies: linear probing (try 2, 3, 4, ...) or quadratic probing.

### Python Dictionaries

Python's `dict` is implemented as a hash table with open addressing.

```python
student = {"name": "Rahul", "marks": 92}
student["name"]   # O(1)
```

**Keys must be immutable** (int, string, tuple). Mutable keys (lists, dicts) are forbidden because if the key changes, its hash changes, and the dictionary loses track of the value.

### Dictionary Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case O(n) occurs when many keys collide repeatedly, which is rare with a good hash function.

---

## Full Complexity Reference

| Structure | Access | Insert | Delete | Notes |
|-----------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | Index-based |
| Linked List | O(n) | O(1) at head | O(n) | Pointer-based |
| Stack | O(1) top only | O(1) | O(1) | LIFO |
| Queue | O(1) front only | O(1) | O(1) | FIFO, use deque |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | Key-value |

---

## Exam Quick-Fire

**Q: LIFO structure?** Stack

**Q: FIFO structure?** Queue

**Q: DFS uses which structure?** Stack

**Q: BFS uses which structure?** Queue

**Q: Why can't lists be dictionary keys?** Lists are mutable — their hash value could change, breaking the dictionary's internal structure

**Q: Queue with Python list — why is deque better?** `list.pop(0)` is O(n) due to shifting. `deque.popleft()` is O(1).

**Q: Hash table worst case and why?** O(n) — if all keys collide into the same slot, lookup degrades to scanning a linked list of length n.
