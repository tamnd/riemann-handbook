---
id: full-intersection-tower-i8-identity
title: The antisymmetry of the height defect on a good tower (statement form)
kind: theorem
decl: GlobalTheory.T.full_intersection_tower_I8_identity
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.FullIntersectionTowerI8IdentityStatement
covers: 1620
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`full_intersection_tower_I8_relation`](/entry/full-intersection-tower-i8-relation/), and its proof applies that theorem. The real content is in [`good_tower_antisymmetry_of`](/entry/good-tower-antisymmetry-of/). Its user is [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/), which needs the property `I8` of a good tower.

## Statement

Use the notation of [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/). For a weight $\lambda$, a component $c$ and $B \geq 2$, let
$$D_{B,c}(\lambda) = \mathrm{PP}_{B,c}(L_\lambda^{d+1}) - \mathrm{vol}(c)\, h_{\mathrm{Fl}}(L_\lambda^{d+1}),$$
where $h_{\mathrm{Fl}}$ is the arithmetic intersection number on the flag variety, with sign $(-1)^{\deg}$.

**Theorem.** Assume `CmpSt`, $\mathrm{Given}$ and `Out.WeilSt`. Let $T$ be a root tower for $N = p + q$ with a good origin $o$ that has `Extra`, let $II$ be a full intersection system, and let $p, q \geq 1$. Then for each $\tau \in \Psi$ and each $a$ with $a + 1 \neq j$,
$$D_{B,c}(s_{\tau,a}\lambda) = -D_{B,c}(\lambda),$$
where $s_{\tau,a}$ swaps the entries $a$ and $a+1$ of $\lambda$ at $\tau$. These swaps generate the Weyl group of the Levi subgroup $\mathrm{GL}_j \times \mathrm{GL}_{N-j}$ in each factor.

## Proof

Apply `full_intersection_tower_I8_relation`.

## In the Lean code

The theorem is in [FullIntersectionTowerI8IdentityStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/FullIntersectionTowerI8IdentityStatement.lean#L20). The proof is `first | exact @… | exact … | (intros; apply … <;> assumption)`, as in the other statement files of this chapter. `import Mathlib` and the import of `CmpSt` each appear twice. `I8` is in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L108). The remark on the Levi subgroup is our reading of the condition $b = a + 1 \neq j$.
