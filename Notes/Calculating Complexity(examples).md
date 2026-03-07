# Calculating Complexity — Examples

---

## How to Analyse Any Algorithm

1. Identify the **input size** n
2. Find the **loops** (or recursive calls)
3. Identify the **basic operation** inside
4. **Count** how many times it runs
5. Drop constants and lower-order terms

---

## Example 1 — Find Maximum Element

```python
def maxElement(L):
    maxval = L[0]
    for i in range(len(L)):
        if L[i] > maxval:
            maxval = L[i]
    return maxval
```

- Input size: `n = len(L)`
- One loop running **n times**
- Basic operation: `L[i] > maxval` (1 comparison per iteration)

**T(n) = n → O(n) — Linear time**

---

## Example 2 — Check Duplicates

```python
def noDuplicates(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] == L[j]:
                return False
    return True
```

- Input size: `n = len(L)`
- Two nested loops
- Outer loop: i = 0 → n-1
- Inner loop: j = i+1 → n-1

Number of comparisons:

```
(n-1) + (n-2) + ... + 1 = n(n-1)/2
```

This is the sum of an arithmetic series. The formula is always:

> **1 + 2 + ... + (n-1) = n(n-1)/2**

**T(n) = n(n-1)/2 → O(n²) — Quadratic time**

| Case | Condition | Complexity |
|------|-----------|------------|
| Best | Duplicate found at start | O(1) |
| Worst | No duplicates at all | O(n²) |

We always report **worst case**.

---

## Example 3 — Matrix Multiplication

```python
for i in range(m):
    for j in range(p):
        for k in range(n):
            c[i][j] += A[i][k] * B[k][j]
```

- Matrix A is `m × n`, Matrix B is `n × p`, result is `m × p`
- Three nested loops running m, p, and n times respectively

**T(n) = m × p × n → O(mnp)**

Special case — square matrices (m = n = p):

**O(n³) — Cubic time**

> Note: More advanced algorithms (like Strassen's) can reduce this below O(n³), but O(n³) is the classical result.

---

## Example 4 — Number of Bits

```python
def numberOfBits(n):
    count = 1
    while n > 1:
        count += 1
        n = n // 2
    return count
```

Each iteration halves n:

```
n → n/2 → n/4 → n/8 → ... → 1
```

How many times can we halve before reaching 1? Exactly **log₂n** times.

**Example:** n = 16

```
16 → 8 → 4 → 2 → 1    (4 steps = log₂16)
```

**T(n) = O(log n) — Logarithmic time**

> For number problems, input size is the **number of digits**, not the value itself. A number n has log₁₀n digits. This algorithm is effectively linear in the number of digits.

---

## Example 5 — Towers of Hanoi

**Problem:** Move n disks from peg A to peg C using peg B.

**Rules:**
- Only one disk at a time
- A larger disk can never sit on a smaller one

**Recursive structure:**
1. Move n-1 disks out of the way
2. Move the largest disk
3. Move n-1 disks back on top

**Recurrence:**

```
M(n) = 2·M(n-1) + 1
M(1) = 1
```

**Expanding the recurrence:**

```
M(n) = 2M(n-1) + 1
     = 2(2M(n-2) + 1) + 1  =  4M(n-2) + 3
     = 4(2M(n-3) + 1) + 3  =  8M(n-3) + 7
```

General pattern after k steps:

```
M(n) = 2^k · M(n-k) + (2^k - 1)
```

Set k = n-1, so M(1) = 1:

```
M(n) = 2^(n-1) + (2^(n-1) - 1) = 2^n - 1
```

**T(n) = 2ⁿ - 1 → O(2ⁿ) — Exponential time**

> This is not just theoretically slow. For n = 64 disks, at 1 move per second it would take roughly 585 billion years. No hardware improvement can fix exponential complexity.

---

## Summary

| Problem | Complexity | Type |
|---------|------------|------|
| Find maximum | O(n) | Linear |
| Check duplicates | O(n²) | Quadratic |
| Matrix multiplication | O(n³) | Cubic |
| Bit counting | O(log n) | Logarithmic |
| Towers of Hanoi | O(2ⁿ) | Exponential |

---

## Quick Reference — Spotting Complexity from Code

| Code Pattern | Complexity |
|--------------|------------|
| Single loop over n | O(n) |
| Two nested loops over n | O(n²) |
| Three nested loops over n | O(n³) |
| Halving input each step | O(log n) |
| Loop + halving (e.g. merge sort) | O(n log n) |
| Two recursive calls on full problem | O(2ⁿ) |
