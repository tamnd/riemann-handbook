---
id: mass-trace
title: The mass of self-dual lattices over a frame lattice
kind: theorem
decl: GlobalTheory.HL.FrameMass.mass_trace
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SelfDualHermitianLatticeMassOfTrace
covers: 332
status: drafted
drafted_by: writer@claude
---
This theorem applies the local bound [`mass_bounds`](/entry/mass-bounds/) to the space spanned by the two frames of a record `Frames`. It gives one constant $\kappa$ that works for all frame classes at once. Its statement form is [`selfDualHermitianLattice_mass_of_trace`](/entry/self-dual-hermitian-lattice-mass-of-trace/), which has two users below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

## Statement

The local field $F$, the algebra $E$, $q$, $\mathcal{O}$, the frames record $S$ with Hermitian form $h$ on $V = E^{k+2r+1}$, the frames $f, f'$ and the groups $N, N'$ are as in [the entry for `amp_le_mass`](/entry/amp-le-mass/) and [the entry for `mass_bounds`](/entry/mass-bounds/). The frame $f$ is $r + 1$ vectors, and so is $f'$. Let $\mathrm{ME}$ be the $E$-span of $f$ and $f'$ ($2r + 2$ vectors), and $H_0$ the group of isometries of $V$ that fix $\mathrm{ME}$ pointwise. For a lattice $\hat M \subseteq \mathrm{ME}$, `massSig` is the sum $\sigma(\hat M)$ of [`mass_bounds`](/entry/mass-bounds/) for $Y = \mathrm{ME}$, with $\Lambda_0 = \mathcal{O}^{k+2r+1}$.

A *frame class* (`IsCls`) is a set $C$ of pairs of $(r+1)$-tuples: those obtained from $(nf, n'f')$, for fixed $n \in N$, $n' \in N'$, by integral upper unitriangular matrices that agree modulo $\theta$ (`frameCls`), where $\theta \in \{1, \varpi\}$ is fixed by $S$. For a pair $p = (g, g')$ let $M(p)$ be the $\mathcal{O}$-span of the $g_b$ and of the $\theta^{-1}(g'_b - g_b)$ (`Mof`).

**Theorem.** Let $k \ge 2r + 6$, and suppose that $h$ has a self-dual lattice. Then there is $\kappa > 0$ such that for each frame class $C$, each $p \in C$ and each lattice $\hat M$ with $M(p) \subseteq \hat M \subseteq \mathrm{ME}$ and $h(\hat M, \hat M) \subseteq \mathcal{O}$,

$$\tfrac{\kappa}{2}\, [\hat M : M(p)]^{-(k-1)} \le \sigma(\hat M) \le 2\kappa\, [\hat M : M(p)]^{-(k-1)}.$$

## Proof

1. `FrameTuple.main` gives a tuple $x$ of $2r + 2$ vectors with invertible Gram matrix and span $\mathrm{ME}$. It also says that $H_0$ is the group $U_{\mathrm{ME}}$ of [`mass_bounds`](/entry/mass-bounds/), that `massSig` is `sigMass` with $\Lambda_0 = \mathcal{O}^{k+2r+1}$, and that each $p$ in a class has $M(p) = \mathcal{O}\text{-span}(xB)$ for a matrix $B$ with $\det B \cdot c(\det B) = 1$.
2. [`selfDual_hermitianLattice_mass_bounds`](/entry/self-dual-hermitian-lattice-mass-bounds/) with $m = 2r + 2$ and $n = k + 2r + 1$ gives $\kappa$. Its condition $n \ge 2m + 3$ is $k \ge 2r + 6$.
3. Fix $C$, $p$ and $\hat M$, and put $y = xB$. `exists_basis_overlattice` gives an integral matrix $A$ with invertible determinant and $\hat M = \mathcal{O}\text{-span}(yA^{-1})$. `index_rmul` gives $[\hat M : M(p)] = q^{v}$, with $v \ge 0$ the valuation of $\det A \cdot c(\det A)$.
4. Apply step 2 to $AB^{-1}$. Then $x(AB^{-1})^{-1} = yA^{-1}$, the norm of $\det(AB^{-1})$ is that of $\det A$, and $G(yA^{-1})$ is integral because $h$ is integral on $\hat M$. As $n - m = k - 1$, the factor $q^{-(n-m)v}$ is $[\hat M : M(p)]^{-(k-1)}$.

The rest is matrix bookkeeping: `gram_rmul`, `det_cT` and `span_rmul`, in the same file.

## In the Lean code

The theorem is in [SelfDualHermitianLatticeMassOfTrace.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SelfDualHermitianLatticeMassOfTrace.lean#L84), and `massSig`, `Mof`, `IsCls` in [ComplementReferenceCompactSubgroup.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean#L137). The statement has no trace map. In this name and in `trace_partition`, the "trace" of a lattice $\Lambda$ seems to be $\Lambda \cap Y$, here $\Lambda \cap \mathrm{ME}$ (`sat`). The self-dual lattice of the hypothesis is used only as $\Lambda_s$ in step 2. The users `total_le_generic` and `share_le` call this theorem with $k \ge 4r + 7$.
