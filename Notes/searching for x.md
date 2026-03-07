# Searching Algorithms

---

## 1. Linear Search

- Works on **sorted or unsorted** lists
- Scan one element at a time until found

**Example:** Search v = 9 in [3, 8, 1, 9, 5]

```
3 → no   8 → no   1 → no   9 → yes
```

| Case | Condition | Complexity |
|------|-----------|------------|
| Best | Element is first | O(1) |
| Worst | Element not in list | O(n) |

---

## 2. Binary Search

- Requires a **sorted** list
- Check the middle element, eliminate half, repeat

**Example:** Search v = 13 in [2, 4, 7, 9, 13, 18, 25]

```
middle = 9  →  13 > 9  →  search right half
middle = 18 →  13 < 18 →  search left half
middle = 13 →  found
```

Each step halves the list: n → n/2 → n/4 → ... → 1

Number of steps = log₂n

**Complexity: O(log n)**

---

## 3. Jump Search

- Requires a **sorted** list
- Jump ahead in fixed blocks of size **√n**, then do linear search inside the block

**Example:** Search v = 21 in a list of n = 16, block size = √16 = 4

```
Step 1 — Jump through blocks:
index 0  → 1
index 4  → 9
index 8  → 17
index 12 → 25  ← exceeded target, stop

Step 2 — Linear search in previous block [17, 19, 21, 23]:
17 → no   19 → no   21 → yes
```

- Jumps taken: √n
- Linear search inside block: √n
- Total: **O(√n)**

---

## 4. Exponential Search

- Used for **sorted lists of unknown or very large size**
- Double the search range until the target is exceeded, then apply binary search

**Example:** Search v = 18 in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

```
Check index 1  → 4
Check index 2  → 6
Check index 4  → 10
Check index 8  → 18  ← found range

Apply binary search within that range.
```

- Finding the range: O(log n)
- Binary search within range: O(log n)
- Total: **O(log n)**

---

## 5. Interpolation Search

- Improvement on binary search for **uniformly distributed** data
- Instead of always checking the middle, it **estimates** where the value likely is

**Formula:**

```
pos = low + [(v - A[low]) / (A[high] - A[low])] × (high - low)
```

**Example:** Search v = 70 in [10, 20, 30, 40, 50, 60, 70, 80, 90]

Binary search would check index 4 (value 50) first. Interpolation search predicts the position is near index 6 and jumps straight there.

| Case | Complexity |
|------|------------|
| Best / Average | O(log log n) |
| Worst | O(n) |

> Worst case happens when data is **not** uniformly distributed — the position estimate keeps missing badly.

---

## Full Comparison

| Algorithm | Works on | Complexity |
|-----------|----------|------------|
| Linear Search | Unsorted or sorted | O(n) |
| Binary Search | Sorted | O(log n) |
| Jump Search | Sorted | O(√n) |
| Exponential Search | Sorted, large/unknown size | O(log n) |
| Interpolation Search | Sorted, uniform data | O(log log n) avg |

---

## Which to Use?

| Situation | Best Choice |
|-----------|-------------|
| Unsorted list | Linear Search |
| Sorted list | Binary Search |
| Uniformly distributed values | Interpolation Search |
| Unknown or very large size | Exponential Search |

---

## Exam Questions

**Q: Which search works on unsorted lists?**
Linear Search

**Q: Which search halves the search space each step?**
Binary Search

**Q: Jump search complexity?**
O(√n)

**Q: Binary search complexity?**
O(log n)

**Q: Interpolation search best case?**
O(log log n)

**Q: When does interpolation search degrade to O(n)?**
When data is not uniformly distributed

---

## Memory Trick

| Algorithm | Core Idea |
|-----------|-----------|
| Linear | Check every element |
| Binary | Divide list in half |
| Jump | Jump √n blocks |
| Exponential | Double the range |
| Interpolation | Predict the position |
