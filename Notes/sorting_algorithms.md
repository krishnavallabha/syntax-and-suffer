# Sorting Algorithms

---

## 1. Selection Sort

**Idea:** Find the minimum element in the unsorted portion and place it at the correct position. Repeat for each position.

**Example:**

```
[8, 3, 5, 2]
 → find min (2) → swap to front  →  [2, 3, 5, 8]
 → find min of remaining (3) → already in place
 → done
```

**Complexity Analysis:**

Inner loop runs (n-1) + (n-2) + ... + 1 times:

```
T(n) = n(n-1)/2
```

| Case | Complexity |
|------|------------|
| Best | O(n²) |
| Worst | O(n²) |

> Selection sort **always scans the full remaining list** regardless of input. Best and worst case are identical.

---

## 2. Insertion Sort

**Idea:** Build a sorted sublist from left to right. For each new element, insert it into the correct position within the already-sorted portion.

**Example:**

```
[7, 4, 5, 2]
 →  [7]
 →  [4, 7]         (4 inserted before 7)
 →  [4, 5, 7]      (5 inserted between 4 and 7)
 →  [2, 4, 5, 7]   (2 inserted at front)
```

**Complexity Analysis:**

- Worst case: list is reverse sorted. Every new element must travel all the way to the front.

```
T(n) = 1 + 2 + 3 + ... + (n-1) = n(n-1)/2
```

- Best case: list is already sorted. Each element is compared once and stays in place.

```
T(n) = n
```

| Case | Complexity |
|------|------------|
| Best | O(n) |
| Worst | O(n²) |

> Insertion sort is efficient for **nearly sorted data**. It is the preferred choice for small or almost-sorted lists.

---

## 3. Bubble Sort

**Idea:** Repeatedly compare and swap adjacent elements if they are out of order. After each full pass, the largest unsorted element "bubbles" to its correct position at the end.

**Example:**

```
[5, 1, 4, 2]
 pass 1 → [1, 4, 2, 5]
 pass 2 → [1, 2, 4, 5]
 pass 3 → no swaps, done
```

**Complexity Analysis:**

Each pass does (n-1), (n-2), ... comparisons:

```
T(n) = n(n-1)/2
```

Optimised version: if a full pass produces no swaps, the list is sorted and the algorithm stops early.

| Case | Complexity |
|------|------------|
| Best (optimised) | O(n) |
| Worst | O(n²) |

> Bubble sort is primarily educational. It is rarely used in practice due to its high constant factors compared to insertion sort.

---

## 4. Merge Sort

**Idea (Divide and Conquer):**
1. Split the list in half
2. Recursively sort both halves
3. Merge the two sorted halves into one sorted list

**Example:**

```
[8, 3, 5, 2]
 → split →  [8, 3]  |  [5, 2]
 → sort  →  [3, 8]  |  [2, 5]
 → merge →  [2, 3, 5, 8]
```

**Merging two sorted lists:** Compare the front elements of each half, take the smaller one, and repeat until both halves are exhausted. This takes O(n) time.

**Recurrence:**

```
T(n) = 2T(n/2) + n
```

- 2T(n/2): sort two halves
- n: merge step

**Solving the recurrence:**

At each level of recursion, n elements are processed. There are log₂n levels (since we halve each time).

```
Total = n × log₂n
```

| Case | Complexity | Space |
|------|------------|-------|
| Best | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

> Merge sort is **stable** and always O(n log n) regardless of input. The downside is it requires O(n) extra space for the temporary arrays.

---

## 5. Quick Sort

**Idea:**
1. Choose a **pivot** element
2. Partition: move all elements smaller than pivot to the left, all larger to the right
3. Recursively sort the left and right partitions

**Example:**

```
[8, 3, 5, 2]   pivot = 8

left  = [3, 5, 2]   (less than 8)
right = []           (greater than 8)

→ sort [3, 5, 2] with pivot = 3
   left = [2], right = [5]
   → [2, 3, 5]

→ final: [2, 3, 5, 8]
```

**Complexity Analysis:**

- Best/Average case: pivot divides list roughly in half each time.

```
T(n) = 2T(n/2) + n  →  O(n log n)
```

- Worst case: pivot is always the smallest or largest element (e.g. already sorted list with first element as pivot). One partition has n-1 elements, the other has 0.

```
T(n) = T(n-1) + n  →  O(n²)
```

| Case | Complexity | Space |
|------|------------|-------|
| Best / Average | O(n log n) | O(log n) |
| Worst | O(n²) | O(n) |

> Quick sort is the **fastest in practice** due to small constants and good cache performance, despite its O(n²) worst case. The worst case is avoided by choosing a good pivot (e.g. random pivot or median-of-three).

---

## 6. Heap Sort

**Idea:** Uses a **binary max-heap** — a tree where every parent is larger than its children. The root is always the maximum element.

**Steps:**
1. Build a max-heap from the list: O(n)
2. Repeatedly extract the maximum (root) and place it at the end: O(n log n)

**Why log n per extraction?** After removing the root, the heap must be repaired ("heapify"), which travels down the height of the tree. Height of a heap with n elements = log₂n.

```
Total = O(n) + O(n log n) = O(n log n)
```

| Case | Complexity | Space |
|------|------------|-------|
| Best | O(n log n) | O(1) |
| Worst | O(n log n) | O(1) |

> Heap sort is **in-place** (no extra memory) and always O(n log n). However, it is slower than merge sort and quick sort in practice due to poor cache behaviour.

---

## Full Comparison

| Algorithm | Best | Worst | Space | Notes |
|-----------|------|-------|-------|-------|
| Selection Sort | O(n²) | O(n²) | O(1) | Always same regardless of input |
| Insertion Sort | O(n) | O(n²) | O(1) | Fast on nearly sorted data |
| Bubble Sort | O(n) | O(n²) | O(1) | Mostly educational |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Stable, consistent |
| Quick Sort | O(n log n) | O(n²) | O(log n) | Fastest in practice |
| Heap Sort | O(n log n) | O(n log n) | O(1) | In-place, consistent |

---

## When to Use Which

| Situation | Best Choice |
|-----------|-------------|
| Small list | Insertion Sort |
| Nearly sorted data | Insertion Sort |
| Large data, stability needed | Merge Sort |
| Large data, speed needed | Quick Sort |
| Large data, no extra memory | Heap Sort |

---

## Key Exam Facts

**Q: Which algorithm has identical best and worst case?**
Selection Sort and Merge Sort and Heap Sort (all O(n²) or all O(n log n) regardless)

**Q: Which O(n²) algorithm can run in O(n)?**
Insertion Sort and Bubble Sort (when data is already sorted)

**Q: Quick sort worst case and when does it occur?**
O(n²) — when pivot is always the minimum or maximum (e.g. sorted list + first element pivot)

**Q: Why is merge sort O(n log n)?**
log n levels of recursion × O(n) merge at each level

**Q: Which sorting algorithm uses extra O(n) space?**
Merge Sort (all others listed here are O(1) or O(log n))
