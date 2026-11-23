---
id: self-dual-hermitian-lattice-mass-bounds
title: The mass of self-dual lattices with a given trace, statement form
kind: theorem
decl: GlobalTheory.T.selfDual_hermitianLattice_mass_bounds
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SelfDualHermitianLatticeMassBoundsStatement
covers: 317
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`mass_bounds`](/entry/mass-bounds/). Its only user is [`mass_trace`](/entry/mass-trace/), which applies it to the span of the two frames. The content is in [`mass_bounds`](/entry/mass-bounds/).

## Statement

**Theorem.** Let $h$ be a nondegenerate Hermitian form on $E^n$ over an unramified quadratic algebra $E$ of a local field $F$, with a self-dual lattice $\Lambda_s$. Let $x$ be $m$ vectors with invertible Gram matrix, $Y$ their span, and $\Lambda_0$ a lattice. If $n \ge 2m + 3$, there is $\kappa > 0$ such that for every $A \in \mathrm{GL}_m(E)$ with $G(xA^{-1})$ integral,

$$\tfrac{\kappa}{2}\, q^{-(n-m) v_A} \le \sigma(M_A) \le 2\kappa\, q^{-(n-m) v_A}.$$

Here $M_A$ is the $\mathcal{O}$-span of $xA^{-1}$, $v_A$ the valuation of $\det A \cdot c(\det A)$, and $\sigma(M)$ the weighted number of self-dual lattices $\Lambda$ with $\Lambda \cap Y = M$, up to the isometries that fix $Y$ (`sigMass`). All objects are defined in [the entry for `mass_bounds`](/entry/mass-bounds/).

## Proof

The proof is the term `GlobalTheory.HL.Unfold.mass_bounds`. There is nothing else.

## In the Lean code

The theorem is at [SelfDualHermitianLatticeMassBoundsStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SelfDualHermitianLatticeMassBoundsStatement.lean#L10). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits.
