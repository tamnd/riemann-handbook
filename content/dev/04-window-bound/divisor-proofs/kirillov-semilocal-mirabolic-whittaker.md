---
id: kirillov-semilocal-mirabolic-whittaker
title: The semi-local Kirillov bump, from a Whittaker function that is not zero on the mirabolic subgroup
kind: theorem
decl: GlobalTheory.T.kirillov_semilocal_mirabolic_whittaker
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KirillovSemilocalMirabolicWhittakerStatement
covers: 367
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the assembly of the semi-local Kirillov bump](/entry/kirillov-semilocal/). [The semi-local Kirillov bump](/entry/kirillov-semilocal-bump/) calls it after it has moved a nonzero value of the Whittaker function into the mirabolic subgroup.

## Statement

The statement of [the semi-local Kirillov bump](/entry/kirillov-semilocal-bump/), with the same $E$, $S$, $G_S$, $P_S$, $b$ and conditions 1 to 4 on $b$, and with one change in the hypothesis on $\varphi \in \pi$: there is $p \in P_S$ with $W_\varphi(p) \ne 0$. The conclusion is the same: there is $F$ in the span $\mathcal{M}(\pi)$ with $W_F = b$ on $P_S$, right invariant under an open subgroup of $\mathrm{GL}_{m+1}(\mathbb{A}_f)$, and with the right invariances and Whittaker relations of $\varphi$ under each $t$ that is trivial at infinity and at $S$.

The hypothesis is stronger than the one of the bump theorem, because $P_S \subset G_S$.

## Proof

The proof is `exact MirSemi.kirillov_semilocal`. See [the assembly](/entry/kirillov-semilocal/).

## In the Lean code

The theorem is in [KirillovSemilocalMirabolicWhittakerStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemilocalMirabolicWhittakerStatement.lean#L8). The proof is a `first` combinator around `exact`. The statement writes the smoothness as `ContDiffOn ℝ ((⊤ : ℕ∞) : WithTop ℕ∞)`, where the bump theorem writes `ContDiffOn ℝ ∞`. These are the same. It names the variable of clause 3 `k`, where the bump theorem names it `t`.
