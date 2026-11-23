---
id: exists-secs-of-int-fam
title: Sections on the generic fibre with a given theta expansion at every trait
kind: theorem
decl: GlobalTheory.Mum.exists_secs_of_intFam
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSecsOfIntFam
covers: 461
status: drafted
drafted_by: writer@claude
---
This theorem gives, for a labelled cover, sections on the generic fibre with a prescribed theta expansion along every trait. It is step 3 of [`secs_exists`](/entry/secs-exists/). Its proof applies `SecsDesc.assemble` to three lemmas, which hold the content.

## Statement

Let $R$, $D$ and a labelled cover $C$ of $D$ be as in [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/), with `Base R`. Let $L$ be the line bundle of $C$, $A$ its generic fibre and $n$ its odd prime.

An integral family of degree $k$ (`IntFam 𝔪 D k`) is a family of sections $f(\alpha)$ on the abelian part of $D$, one for each character $\alpha \in X$, such that for each $e$ only finitely many $f(\alpha)$ fail to vanish on the $e$-th thickening of the closed fibre.

A trait datum $T$ (`Trait C W`) is a complete discrete valuation ring $W$ over $R$, a lift $\operatorname{Spec} W \to S$, and a uniformisation of the pullback of $G$ by the pullback of $D$, compatible with the labels. For a section $s$ of $L^k$ on $A$, `T.Exp a b s F` says: there is a section $\sigma$ over $W$ with $\sigma = a\, s$ on the generic fibre, and $\sigma = b\, \sigma'$, where $\sigma'$ is a section on the uniformised group with expansion coefficients from $F$ (`ExpandsAt`, not unfolded here).

**Theorem.**

1. There is $j_0$ such that for each $j \geq j_0$ there is a map $\Phi$ from integral families of degree $n^j$ to sections of $L^{n^j}$ on $A$ with: for each trait $T$ there is a unit $u$ of $W$ with `T.Exp 1 u (Φ F) F` for all $F$.
2. For each integral family $F_1$ of degree 1 there is a section $\theta$ of $L$ on $A$ with: for each trait $T$ there is a unit $u$ with `T.Exp 1 u θ F₁`.

## Proof

`SecsDesc.assemble` proves the theorem from three statements:

- `exists_map_thetaExpansion_all_traits`: for each $j$, a $\Phi$ with `T.Exp a b (Φ F) F` for some nonzero $a, b \in W$;
- `exists_origin_normalisation_unit_at_traits`: for $k \geq k_0$, such a $\Phi$ can be replaced by one with $a = 1$ and $b$ a unit;
- `exists_thetaSection_normalised_unit_at_traits`: for odd $m$, a normalised $\Phi$ in degree $m^2$ gives a normalised $\theta$ in degree 1.

For part 1, take $j_0 = k_0$; then $n^j \geq j \geq k_0$, and the first two statements give a normalised $\Phi$. For part 2, take $m = n^{k_0}$, which is odd, so $m^2 = n^{2k_0}$ is covered by part 1. The third statement gives $\theta$.

## In the Lean code

The theorem is in [ExistsSecsOfIntFam.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSecsOfIntFam.lean#L14). Its proof is one term: `SecsDesc.assemble` in [ImportsTailRest.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailRest.lean#L13), applied to the three statements above. We read the statements of the three lemmas, not their proofs. `IntFam` and `Trait` are in [ExistsLeadOfUnif.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsLeadOfUnif.lean#L49).

The file name `ImportsTailRest.lean` says nothing of its content.
