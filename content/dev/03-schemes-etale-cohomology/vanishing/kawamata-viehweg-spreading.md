---
id: kawamata-viehweg-spreading
title: Kawamata-Viehweg vanishing on a fibre of a model of finite type, second name
kind: theorem
decl: GlobalTheory.T.kawamata_viehweg_spreading
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.KawamataViehwegSpreadingStatement
covers: 522
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`vanishing_charZero_fibre_of_finiteType`](/entry/vanishing-char-zero-fibre-of-finite-type/). It has the same statement, and its proof only calls that theorem. [`vanishing_ample_snc_charZero`](/entry/vanishing-ample-snc-char-zero/) calls it after it spreads its data out over a ring of finite type. The content is in `vanishing_charZero_fibre_of_finiteType`. Below this theorem are 522 declarations.

## Statement

Let $R$ be a commutative ring of finite type over $\mathbb{Z}$ and $\varphi \colon R \to k$ an injective map to a field of characteristic $0$. Let $f \colon X \to \operatorname{Spec} R$ be smooth of relative dimension $d$ and proper, and $\pi \colon X' = X \times_R k \to X$ the base change. Let $L_1, \dots, L_s$ with sections $\sigma_i$ be a relative snc family over $R$ (see [`vanishing_ample_snc_charZero`](/entry/vanishing-ample-snc-char-zero/)), $K$ the canonical bundle of $X/R$, and $M$, $A$ line bundles on $X$ with $\pi^* A$ ample on $X'$. Let $r > 0$ and $0 \leq b_i < r$ with

$$r[M] = r[K] + \sum_i b_i [L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$

Then $H^q(X', \pi^* M) = 0$ for all $q > 0$.

## Proof

The proof is `vanishing_charZero_fibre_of_finiteType` applied to the same arguments.

## In the Lean code

The theorem is in [KawamataViehwegSpreadingStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegSpreadingStatement.lean#L12). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with the name `GlobalTheory.vanishing_charZero_fibre_of_finiteType` in each branch. The two statements are identical. The only use of this name is in [KawamataViehwegVanishing.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegVanishing.lean#L44).
