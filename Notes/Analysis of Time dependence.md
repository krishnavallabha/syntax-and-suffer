# Algorithm Analysis Notes

---

## Performance Measurement

Two main sources of interest:
- **Running time** — how long the algorithm takes
- **Space** — memory usage

> We typically focus on **time** over space.

**Why not just upgrade hardware?**
- Processing power is fixed for given hardware
- Hardware upgrades have limited practical impact

---

## Time Complexity

Running time depends on **input size n**.

Instead of measuring exact seconds, we count **basic operations**.

| Function | Type |
|----------|------|
| t(n) = n | Linear |
| t(n) = n² | Quadratic |
| t(n) = n log₂n | Divide-and-conquer |

---

## Understanding log₂n

log₂(n) = k means n = 2^k

**How many times can you divide n by 2 before reaching 1?**

```
1024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1
                     10 steps  →  log₂(1024) = 10
```

| n | log₂n |
|---|-------|
| 1,024 | 10 |
| 1,000,000 | ≈ 20 |

log grows **very slowly** — that's why O(n log n) algorithms are so powerful.

---

## Example 1 — Duplicate Card Detection (SIM / Aadhaar / Bank IDs)

**Problem:** Find if any two cards belong to the same person.

### ❌ Naive Algorithm — O(n²)

Compare every pair:

```
1 vs 2,  1 vs 3,  1 vs 4
2 vs 3,  2 vs 4
3 vs 4
```

Total comparisons = n(n−1)/2 ≈ **n²**

### ✅ Clever Algorithm — O(n log n)

1. **Sort** the cards → duplicates end up adjacent
2. **Compare only neighbours**

```
A100, A102, A102, A105
             ^^^^ found!
```

Sorting costs n log₂n, which is far cheaper than n².

---

## Example 2 — Video Game Closest Pair Detection

**Problem:** Game engine must find the closest pair of objects (bullets, enemies, players, obstacles) every frame.

### ❌ Naive Algorithm — O(n²)

Compare every pair of objects.

With **n = 100,000 objects:**

```
n² = (10⁵)² = 10¹⁰ = 10 billion operations

At 10M ops/sec (Python):
10,000,000,000 ÷ 10,000,000 = 1000 seconds = 16.7 minutes
```

**Completely unusable.** Games need millisecond responses.

### ✅ Clever Algorithm — O(n log n)

Uses **divide and conquer** / spatial partitioning.

```
n log₂n = 100,000 × 17 = 1,700,000 operations
```

### Comparison

| Algorithm | Operations |
|-----------|------------|
| Naive O(n²) | 10,000,000,000 |
| Clever O(n log n) | 1,700,000 |
| **Difference** | **~6,000× faster** |

*(Note: 4K console = 4000×2000 = 8M pixels — O(n²) is simply not viable at this scale)*

---

## Key Takeaway

> **Algorithm efficiency matters more than hardware speed.**
> A powerful machine cannot save a bad algorithm.

### Complexity Growth (slowest → fastest growing)

| Complexity | Growth Rate |
|------------|-------------|
| O(n) | Linear ✅ |
| O(n log n) | Fast ✅ |
| O(n²) | Slow ⚠️ |
| O(2ⁿ) | Impossible ❌ |
