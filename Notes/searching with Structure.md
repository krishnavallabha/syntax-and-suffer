# Searching with Structure — Binary Search Trees

---

## 1. The Problem with Static Structures

A sorted array supports O(log n) binary search, but inserting or deleting an element costs O(n) due to shifting.

A **Binary Search Tree (BST)** maintains sorted order dynamically — supporting search, insert, and delete all in O(height) time, with no shifting required.

---

## 2. The BST Property

For every node with value v:

```
All values in the LEFT subtree  <  v
All values in the RIGHT subtree  >  v
```

No duplicate values. This property holds recursively at every node.

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

An **in-order traversal** (left → root → right) always yields values in **sorted ascending order**.

---

## 3. Find — O(height)

Compare v with the current node:
- If equal → found
- If v < current → go left
- If v > current → go right
- If empty node → not in tree

At each step we eliminate one subtree. In a balanced tree this halves the search space.

---

## 4. Insert — O(height)

Run Find(v). Insert at the exact position where Find would fail (the empty node where the search ends).

```
Insert 5 into the tree above:
→ 5 < 8, go left
→ 5 > 3, go right
→ 5 < 6, go left
→ 5 > 4, go right
→ empty node → insert 5 here
```

---

## 5. Delete — O(height)

Three cases depending on the node being deleted:

**Case 1 — Leaf node:** Simply remove it (replace with empty node). No restructuring needed.

**Case 2 — One child:** Promote the single child subtree up into the deleted node's position.

**Case 3 — Two children:** This is the tricky case.
- Find the **in-order predecessor** — the maximum value in the left subtree (rightmost node of the left subtree)
- Replace the deleted node's value with this predecessor value
- Delete the predecessor from the left subtree (it has no right child, so this reduces to Case 1 or 2)

```
Delete 8 from the tree:
→ two children
→ in-order predecessor = max of left subtree = 7
→ replace 8 with 7
→ delete 7 from its original position (it was a leaf)
```

---

## 6. Minimum and Maximum

- **Minimum:** Follow left pointers all the way down — leftmost node
- **Maximum:** Follow right pointers all the way down — rightmost node

Both are O(height).

---

## 7. Complexity

All operations (find, insert, delete, min, max) walk down a single path from root to a node.

**Cost = O(height)**

| Tree shape | Height | Operation cost |
|------------|--------|----------------|
| Balanced | O(log n) | O(log n) |
| Unbalanced (worst case) | O(n) | O(n) |

**The worst case:** Inserting elements in sorted order (e.g. 1, 2, 3, 4, 5) produces a tree that degenerates into a linked list — all nodes chain to the right, height = n.

```
1
 \
  2
   \
    3
     \
      4
```

To guarantee O(log n) performance, we need **balanced BSTs** — trees that automatically rebalance on insert and delete. Examples include AVL trees and Red-Black trees (covered separately if needed).

---

## 8. BST vs Sorted Array vs Heap

| Structure | Search | Insert | Delete | Sorted output |
|-----------|--------|--------|--------|---------------|
| Sorted array | O(log n) | O(n) | O(n) | O(1) (already sorted) |
| Heap | O(n) | O(log n) | O(log n) | O(n log n) |
| Balanced BST | O(log n) | O(log n) | O(log n) | O(n) in-order |

A BST gives the best of both worlds for dynamic data — fast search AND fast updates.

---

## Exam Quick-Fire

**Q: State the BST property.**
For every node v: all values in the left subtree < v, all values in the right subtree > v

**Q: What traversal prints a BST in sorted order?**
In-order traversal (left → root → right)

**Q: How do you delete a node with two children?**
Replace it with its in-order predecessor (max of left subtree), then delete that predecessor

**Q: Why can a BST degrade to O(n) operations?**
If elements are inserted in sorted order, the tree becomes a linked list with height n

**Q: What is the height of a balanced BST with n nodes?**
O(log n)

**Q: How do you find the minimum of a BST?**
Follow left pointers to the leftmost node
