---
id: branching-interlacing-pairs
title: Branching maps for interlacing weights
kind: theorem
decl: Formalism.L2.DIV.BrJ.branching_interlacing_pairs
module: Formalism.LocalToGlobal.Divisibility.BrJoint
covers: 701
status: drafted
drafted_by: writer@claude
---
This theorem proves `Conclusion6` of the namespace `PrimeDegreeVariant` with no hypothesis. It is a pass-through. It calls [`gTLower_of`](/entry/g-tlower-of/) with the proved duality `factDelDualNabla`. The content is in that theorem and in [the general branching theorem](/entry/wgl-g-tlower-of/). It lies below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

## Statement

Let $N = n + 1$. Let $\lambda$ be a dominant weight of $\mathrm{GL}_N$ and $\sigma$ one of $\mathrm{GL}_n$. They interlace (`Interlace`) if $\lambda_{i+1} \le \sigma_i \le \lambda_i$ for $1 \le i \le n$. This is the interlacing condition of the branching rule from $\mathrm{GL}_N$ to $\mathrm{GL}_{n}$ (Goodman and Wallach, *Symmetry, Representations, and Invariants*, Chapter 8).

`Branch` asks, with the spaces $\nabla(\lambda)$, $\Delta(\lambda)$ and the Fock pairing as in [`gTLower_of`](/entry/g-tlower-of/), for an explicit nonzero integer $c$ with an explicit bound, an explicit nonzero product $\xi$ of powers of minors, and two linear maps $\iota : \nabla(\sigma) \to \nabla(\lambda)$ and $\beta : \Delta(\lambda) \to \Delta(\sigma)$. Both maps are integral, equivariant for $\mathrm{GL}_n \subset \mathrm{GL}_N$, scale by $a^{|\lambda| - |\sigma|}$ under $\mathrm{diag}(1, \dots, 1, a)$, and are bounded in the Fock norm. Also $\iota$ sends the extremal vector to $c\,\xi$, $\beta \ne 0$, and $\langle \iota s, f \rangle_\lambda = \langle s, \beta f \rangle_\sigma$.

**Theorem.** If $\lambda$ and $\sigma$ interlace, then `Branch` holds.

## Proof

The proof is one line: `gTLower_of factDelDualNabla n N h lam sg hI`.

## In the Lean code

The theorem is in [BrJoint.lean](lean:Formalism/LocalToGlobal/Divisibility/BrJoint.lean#L13). The statement is in [PrimeDegreeVariant.lean](lean:Formalism/SharpRestriction/Divisibility/PrimeDegreeVariant.lean#L104), and `factDelDualNabla` in [FactDelDualNabla.lean](lean:Formalism/LocalRingCardinality/FactDelDualNabla.lean#L75).

Odd points:

- `gTLower_of` returns `PI.GTLower`, and Lean accepts it as `PrimeDegreeVariant.Conclusion6`. The two files define `Interlace`, `Branch` and the maps twice, with the same content.
- A second theorem with the same short name, in the namespace `UnusedSlot33` ([BranchingInterlacingPairs.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/BranchingInterlacingPairs.lean#L53)), proves an unrelated statement about a datum `D` and a scale.
