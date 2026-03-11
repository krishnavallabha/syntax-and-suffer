# Everything is Connected — Introduction to Graphs

---

## 1. What is a Graph?

A graph is a mathematical structure for representing **relationships between objects**.

Formally:

```
G = (V, E)

V = set of vertices (nodes)
E = set of edges (connections)
```

Example:

```
V = {A, B, C, D}
E = {(A,B), (B,C), (C,D)}

A —— B —— C —— D
```

- **Vertices** represent entities
- **Edges** represent relationships between them

---

## 2. Directed vs Undirected Graphs

### Directed Graph

Edges have a **direction**. An edge (u, v) means u → v, but v → u may not exist.

```
A → B → C
```

Real examples: web page links, flight routes, course prerequisites, teacher-course assignments

### Undirected Graph

Edges have **no direction**. An edge (u, v) means u ↔ v — the relationship goes both ways.

```
A —— B —— C
```

Real examples: friendships, road networks, collaboration graphs

> The key test: if A relates to B, does B necessarily relate to A?
> Yes → undirected. No → directed.

---

## 3. Paths, Walks and Reachability

### Path

A **path** is a sequence of vertices where each consecutive pair is connected by an edge, and **no vertex is repeated**.

```
A → B → C → D
```

Formally: v₁, v₂, ..., vₖ such that (vᵢ, vᵢ₊₁) ∈ E for all i.

### Walk

A **walk** is like a path but **vertices may repeat**.

```
A → B → C → B → D    (B appears twice — valid walk, not a valid path)
```

### Reachability

Vertex v is **reachable** from u if there exists a path from u to v.

```
Madurai → Chennai → Delhi
```

Delhi is reachable from Madurai.

### Connected Graph

A graph is **connected** if every vertex can reach every other vertex.

---

## 4. Classic Graph Problems

### Graph Coloring

Assign a colour to each vertex such that **no two adjacent vertices share the same colour**.

```
Coloring function:  c : V → C
Constraint:  if (u, v) ∈ E  then  c(u) ≠ c(v)
```

Real example: map colouring — neighbouring regions must have different colours.

```
A —— B
|    |
C —— D

A=red, B=blue, C=blue, D=red   ✓
```

> **Four Colour Theorem:** Any planar map can be coloured using at most **4 colours**. This was one of the first major theorems proved with computer assistance (1976).

---

### Vertex Cover

Select the **minimum set of vertices** such that every edge in the graph has at least one endpoint in the set.

Real example: placing security cameras at corridor intersections to cover every corridor.

```
A —— B —— C

Vertex cover: {B}
B covers edge (A,B) and edge (B,C)
```

The goal is always to find the **minimum** vertex cover — using as few vertices as possible.

---

### Independent Set

A set of vertices such that **no two vertices in the set share an edge**.

Opposite of vertex cover.

```
A —— B —— C

Independent set: {A, C}
A and C are not connected to each other ✓
```

> There is a deep mathematical connection between vertex cover and independent set: if S is a vertex cover of G, then V − S is an independent set, and vice versa.

---

### Matching

A set of edges where **no two edges share a vertex**.

```
A —— B
C —— D

Matching: {(A,B), (C,D)}
Every vertex appears at most once ✓
```

**Perfect Matching:** every vertex in the graph is part of exactly one matched edge.

Real example: matching job applicants to positions, matching students to dorms.

---

## 5. Summary

### Core Definitions

| Term | Meaning |
|------|---------|
| Vertex | An object / entity |
| Edge | A relationship between two vertices |
| Directed graph | Edges have direction (one-way) |
| Undirected graph | Edges are symmetric (two-way) |
| Path | Sequence of connected vertices, no repeats |
| Walk | Sequence of connected vertices, repeats allowed |
| Reachability | A path exists from u to v |
| Connected | Every vertex can reach every other vertex |

### Classic Problems

| Problem | Goal |
|---------|------|
| Graph Coloring | Colour vertices so no two neighbours share a colour |
| Vertex Cover | Fewest vertices that touch every edge |
| Independent Set | Largest set of vertices with no shared edges |
| Matching | Largest set of edges with no shared vertices |

---

## 6. Common Exam Questions

**Q: What is the difference between a path and a walk?**
A path visits each vertex at most once. A walk can revisit vertices.

**Q: What does it mean for a graph to be connected?**
Every vertex is reachable from every other vertex.

**Q: What is the Four Colour Theorem?**
Any planar graph (map) can be coloured with at most 4 colours such that no adjacent vertices share a colour.

**Q: What is the relationship between vertex cover and independent set?**
They are complements — if S is a vertex cover, then V − S is an independent set.

**Q: Give a real-world example of a directed graph.**
Web pages (links go one way), flight routes, Twitter follows.

**Q: Give a real-world example of an undirected graph.**
Facebook friendships, road maps, co-authorship networks.

---

## 7. Where Graphs Show Up

- **Social networks** — vertices are people, edges are friendships or follows
- **Google Maps** — vertices are locations, edges are roads with weights (distances)
- **Internet routing** — vertices are routers, edges are connections
- **Recommendation systems** — edges connect users to products they liked
- **Compilers** — dependency graphs determine build order
