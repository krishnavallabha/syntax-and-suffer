# 🧠 Syntax & Suffer — A DSA Learning Journal

> *"First, solve the problem. Then, write the code."* — John Johnson

A personal repository documenting my Data Structures & Algorithms journey — combining college coursework (PDSA), LeetCode/Neetcode grinding, and the occasional existential crisis over a DP problem.

Built with Python. Fueled by curiosity (and caffeine).

---

## 👤 About Me

Hi, I’m K! I spend most of my time thinking about uncertainty, probabilities, and why models are wrong but still useful.
I’m really into Bayesian machine learning and research-heavy ML problems.
Long term, I want to work where math, markets, and machine learning collide.

---

## 🗂️ Structure

```
syntax-and-suffer/
├── README.md
├── arrays/
│   ├── notes.md          # Theory, derivations, patterns
│   └── *.py              # LeetCode / Neetcode solutions
├── strings/
├── linked_lists/
├── stacks_queues/
├── binary_search/
├── sliding_window/
├── two_pointers/
├── recursion/
├── trees/
├── graphs/
├── dynamic_programming/
└── sorting/
```

Each topic folder contains:
- `notes.md` — concept explanations, complexity derivations, patterns, and ML analogies where applicable
- `.py` solution files named after the problem (e.g. `two_sum.py`, `lru_cache.py`)

---

## 📒 Notes Format

Each `notes.md` follows this template:

```markdown
## Topic

### Key Concepts

### Complexity Derivations (Time & Space)

### Common Patterns

### ML Analogies (where applicable)

### Problems Solved
| Problem | Platform | Difficulty | Link |
|---------|----------|------------|------|
```

---

## 📊 Progress Tracker

| Topic | Status | Problems Solved |
|-------|--------|----------------|
| Arrays | 🔄 In Progress | 0 |
| Strings | ⏳ Not Started | 0 |
| Linked Lists | ⏳ Not Started | 0 |
| Stacks & Queues | ⏳ Not Started | 0 |
| Binary Search | ⏳ Not Started | 0 |
| Sliding Window | ⏳ Not Started | 0 |
| Two Pointers | ⏳ Not Started | 0 |
| Recursion | ⏳ Not Started | 0 |
| Trees | ⏳ Not Started | 0 |
| Graphs | ⏳ Not Started | 0 |
| Dynamic Programming | ⏳ Not Started | 0 |
| Sorting | ⏳ Not Started | 0 |

---

## 🗺️ Roadmap

Following a mix of **Neetcode 150** and **PDSA college curriculum** (they overlap more than you'd think).

**Phase 1 — Foundations**
- [ ] Arrays & Strings
- [ ] Two Pointers & Sliding Window
- [ ] Binary Search

**Phase 2 — Core Structures**
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees & BSTs

**Phase 3 — Advanced**
- [ ] Graphs (BFS/DFS)
- [ ] Recursion & Backtracking
- [ ] Dynamic Programming

**Phase 4 — Sorting & Misc**
- [ ] Sorting Algorithms with derivations
- [ ] Heaps, Tries, Intervals

---

## ⚡ Solution File Format

Every solution file follows this structure:

```python
"""
Problem: Two Sum
Platform: LeetCode #1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Approach: Hash map for O(n) lookup
Time: O(n) | Space: O(n)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

---

## 🔗 Resources

- [Neetcode 150](https://neetcode.io/practice) — primary problem set
- [Neetcode YouTube](https://www.youtube.com/@NeetCode) — video explanations
- [LeetCode](https://leetcode.com) — problem platform
- [Visualgo](https://visualgo.net) — algorithm visualizations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com) — complexity reference

---

## 📅 Started

February 27, 2025 — Day 1 of many.

---

*If you stumbled here — good luck on your own grind. May your recursion always have a base case.* 🫡
