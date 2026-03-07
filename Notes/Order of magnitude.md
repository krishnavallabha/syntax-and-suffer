# Orders of Magnitude & Asymptotic Notation

---

## 1. Orders of Magnitude

When comparing algorithms, we care about **how fast they grow**, not exact values.

**Example:** t₁(n) = n² vs t₂(n) = 5000n

| n | n² | 5000n |
|---|-----|-------|
| 10 | 100 | 50,000 |
| 50 | 2,500 | 250,000 |
| 10,000 | 100,000,000 | 50,000,000 |

For small n, n² looks smaller. But eventually **n² grows faster and wins**.

The crossover point (~5000) is irrelevant for asymptotic analysis. We only care about long-term behaviour.

---

## 2. Ignore Constant Factors

t(n) = 3n and t(n) = 100n are **both O(n)**.

Even if one is 100× slower, the order of growth is the same. Constants are dropped.

---

## 3. Asymptotic Complexity

"Asymptotic" means: what happens as **n → ∞**?

We ignore small inputs and focus only on the growth trend.

| n | n | n² |
|---|---|-----|
| 10 | 10 | 100 |
| 100 | 100 | 10,000 |
| 1000 | 1,000 | 1,000,000 |

For large n, O(n²) becomes impractical.

---

## 4. Typical Complexity Classes

Ordered from **fastest to slowest growing:**

| Complexity | Name |
|------------|------|
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(n³) | Cubic |
| O(2ⁿ) | Exponential |

**Growth example at n = 1000:**

| Function | Value |
|----------|-------|
| log n | 10 |
| n | 1,000 |
| n log n | 10,000 |
| n² | 1,000,000 |
| 2ⁿ | impossible |

---

## 5. Measuring Running Time

We do **not** measure seconds (machines differ). We count **basic operations:**
- comparisons
- assignments
- swaps
- arithmetic

**Example:** `if a < b` counts as 1 comparison.

**Swap example:** both methods below are O(1) since constants are ignored.
```
(x, y) = (y, x)          # 1 operation
t = x; x = y; y = t      # 3 assignments
```

---

## 6. What Counts as Input Size?

| Problem | Input size |
|---------|------------|
| Sorting | n = number of elements |
| Graph | V = vertices, E = edges |
| Searching | n = size of list |
| Primality (is n prime?) | number of **digits** = log₁₀(n) |

> For numeric problems, input size is the number of digits, not the value itself. Arithmetic is done digit by digit.

---

## 7. Worst Case Analysis

Algorithm performance depends on input arrangement.

**Example: Linear search in [8, 3, 5, 1, 9]**
- Search for 8 → found immediately → O(1)
- Search for 7 → scan whole array → O(n)

**Why not average case?** It requires knowing the probability distribution of inputs, which is hard to determine.

**Worst case** is preferred because it gives a **guarantee**.

> Merge sort worst case: O(n log n). No matter the input, it will never exceed this.

---

## 8. Big-O — Upper Bound

**Definition:** f(x) = O(g(x)) if there exist constants c and x₀ such that:

```
f(x) ≤ c · g(x)    for all x ≥ x₀
```

Think of Big-O as a **ceiling** on growth rate.

### Proof Example: f(n) = 100n + 5 is O(n)

For n ≥ 5:
```
100n + 5 ≤ 100n + n = 101n
```
Choose c = 101, n₀ = 5. Done.

> Note: Big-O is not unique. Any valid c and n₀ work.

### Key Rule: Highest Term Dominates

f(n) = 100 + 20n + 5 → **O(n)**  
f(n) = n² + n → **O(n²)**

Drop all lower-order terms and constants.

### Why n² is NOT O(n)

If n² = O(n), then n² ≤ cn, so n ≤ c. But n grows forever, so this eventually fails. Therefore **n² ∉ O(n)**.

---

## 9. Addition Rule for Big-O

If f₁(n) = O(g₁(n)) and f₂(n) = O(g₂(n)), then:

```
f₁(n) + f₂(n) = O(max(g₁(n), g₂(n)))
```

The **largest term dominates**.

**Algorithm phases example:**
- Phase A: O(n)
- Phase B: O(n²)
- Total: O(n + n²) = **O(n²)**

---

## 10. Big-Ω — Lower Bound

**Definition:** f(x) = Ω(g(x)) if there exist constants c and x₀ such that:

```
f(x) ≥ c · g(x)    for all x ≥ x₀
```

Big-Ω gives a **minimum** growth rate.

**Example:** f(n) = n³ = Ω(n²) because n³ ≥ n² for all n ≥ 1.

**Important:** Comparison-based sorting requires **Ω(n log n)** comparisons. No algorithm can do better. This is why merge sort and heap sort both achieve O(n log n).

---

## 11. Big-Θ — Tight Bound

**Definition:** f(x) = Θ(g(x)) if:

```
c₁ · g(x) ≤ f(x) ≤ c₂ · g(x)
```

Θ means g(x) is **both** the upper and lower bound. The growth rate is exactly that order.

**Example:** f(n) = n(n-1)/2 = n²/2 - n/2

- Upper bound: f(n) ≤ ½ n²
- Lower bound: f(n) ≥ ¼ n²

So c₁ = ¼, c₂ = ½ → **f(n) = Θ(n²)**

---

## 12. Summary Table

| Symbol | Meaning | Analogy |
|--------|---------|---------|
| O(g(n)) | Upper bound | ≤ |
| Ω(g(n)) | Lower bound | ≥ |
| Θ(g(n)) | Exact bound | = |

| Function | Big-O | Big-Ω | Big-Θ |
|----------|-------|-------|-------|
| n² + 3n | O(n²) | Ω(n²) | Θ(n²) |
| 100n | O(n) | Ω(n) | Θ(n) |
| n³ | O(n³) | Ω(n³) | Θ(n³) |

---

## 13. Common Exam Questions

**Q: What is O of 5n² + 3n?**  
A: **O(n²)**

**Q: Algorithm has phases n² and n log n. Total?**  
A: **O(n²)**

**Q: Nested loop — for i in range(n): for j in range(n):**  
A: **Θ(n²)**

---

## Key Takeaways

1. Running time depends on input size n
2. Measure basic operations, not seconds
3. Ignore constant factors
4. Focus on order of growth
5. Analyse worst case behaviour
6. The dominant term always wins
