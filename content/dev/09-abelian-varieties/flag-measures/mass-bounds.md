---
id: mass-bounds
title: The mass of self-dual lattices with a given trace, up to a factor 2
kind: theorem
decl: GlobalTheory.HL.Unfold.mass_bounds
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SelfDualHermitianLatticeMassBounds
covers: 316
status: drafted
drafted_by: writer@claude
---
Fix a nondegenerate subspace $Y$ of a Hermitian space over a local field. This theorem says that the weighted number of self-dual lattices whose intersection with $Y$ is a given lattice $M$ is, up to a factor $2$, a constant times a power of $q$ that depends on the determinant of the Gram matrix of $M$. Its statement form is [`selfDual_hermitianLattice_mass_bounds`](/entry/self-dual-hermitian-lattice-mass-bounds/), and [`mass_trace`](/entry/mass-trace/) applies it to the frames.

## Statement

Let $F$ be a nonarchimedean local field of characteristic $0$, with a uniformizer $\varpi$ and $q$ elements in its residue field. Let $E$ be an unramified $F$-algebra of rank $2$ with involution $c$ (the record `LocE`), and $\mathcal{O}$ the integral closure of $\mathcal{O}_F$ in $E$. Let $H$ be an invertible $n \times n$ matrix with $c(H)^{T} = H$, and $h(v, w) = \sum_{i,j} v_i H_{ij} c(w_j)$ on $V = E^n$. A lattice $\Lambda$ is *self-dual* if $\Lambda = \{w : h(\Lambda, w) \subseteq \mathcal{O}\}$.

Let $\Lambda_s$ be a self-dual lattice, $x = (x_1, \dots, x_m)$ vectors with invertible Gram matrix $G(x) = (h(x_b, x_a))$, $Y$ their $E$-span, and $\Lambda_0$ any lattice. Let $U_Y$ be the group of isometries of $V$ that fix $Y$ pointwise, and $K_\Lambda$ the stabilizer of $\Lambda$ in $U_Y$. For a lattice $M \subseteq Y$, put

$$\sigma(M) = \sum_{[\Lambda]} \frac{[K_{\Lambda_0} : K_{\Lambda_0} \cap K_\Lambda]}{[K_\Lambda : K_{\Lambda_0} \cap K_\Lambda]},$$

over the $U_Y$-orbits of self-dual $\Lambda$ with $\Lambda \cap Y = M$ (`sigMass`). For $A \in \mathrm{GL}_m(E)$ let $xA^{-1}$ be the tuple $(\sum_i (A^{-1})_{ij} x_i)_j$, $M_A$ its $\mathcal{O}$-span, and $v_A$ the $\varpi$-adic valuation of $\det A \cdot c(\det A)$.

**Theorem.** If $n \ge 2m + 3$, there is $\kappa > 0$ such that for each $A \in \mathrm{GL}_m(E)$ with $G(xA^{-1})$ integral,

$$\tfrac{\kappa}{2}\, q^{-(n-m) v_A} \le \sigma(M_A) \le 2\kappa\, q^{-(n-m) v_A}.$$

## Proof

Write $\mathrm{cont}$ for the volume of a finite union of cosets, with a reference lattice of volume $1$. For $i \ge 1$, let $\mathcal{H}_i$ be the set of matrices $c(B)^{T} G(x) B$ with $B \equiv 1 \bmod \varpi^i$.

1. `mass_eq_const_mul_content` gives $\kappa > 0$ such that, for each self-dual $\Lambda$ and all large $i$, the weight of $\Lambda$ in $\sigma$ times $\mathrm{cont}(\mathcal{H}_i)$ equals $\kappa$ times the content of a $\varpi^i$-neighbourhood of the orbit of $x$ under the isometries that fix $\Lambda$.
2. `trace_partition` gives a finite set $s$ of isometries $g$ with $g\Lambda_s \cap Y = M_A$. Each self-dual $\Lambda$ with $\Lambda \cap Y = M_A$ is $u g \Lambda_s$ for exactly one $g \in s$ and some $u \in U_Y$. For large $i$, the tuples $z$ with $zA^{-1}$ primitive in $\Lambda_s$ and $G(z) \in \mathcal{H}_i$ form the disjoint union over $g \in s$ of the neighbourhoods of the orbits of $g^{-1}x$.
3. So $\sigma(M_A)$ is the finite sum over $g \in s$ (`sigMass_eq_sum`, with `unimodular` for the invariance of the weights).
4. `image_thick` and `tuple_jacobian` move the neighbourhood of step 1 for $g\Lambda_s$ to that of $g^{-1}x$. Summing over $s$ with `cont_biUnion`, $\sigma(M_A)\,\mathrm{cont}(\mathcal{H}_i) = \kappa\,\mathrm{cont}(\text{primitive set})$.
5. `cont_prim_scale` says that, for large $i$, the content of the primitive set is between $\tfrac12$ and $2$ times $q^{-(n-m)v_A}\,\mathrm{cont}(\mathcal{H}_i)$. This is the only use of $n \ge 2m + 3$.
6. `congK_group` gives $\mathrm{cont}(\mathcal{H}_i) > 0$. Divide.

## In the Lean code

The theorem is in [SelfDualHermitianLatticeMassBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SelfDualHermitianLatticeMassBounds.lean#L113), and `sigMass` in [HermLat.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/HermLat.lean#L68). `sigMass_eq_sum` and `image_thick` are in the same file. The constant $\kappa$ depends on $\Lambda_0$, $\Lambda_s$ and $x$, but not on $A$. The matrix $A$ need not be integral. We have not compared the statement with a published local mass formula.
