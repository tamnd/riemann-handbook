---
id: count-e-prime-alt
title: The count of eigenforms in a Hida family
kind: theorem
decl: UpperTheory.V.Z.Desc.V0.countE'_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.CountE
covers: 343
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{CountEAlt}$. It is a pass-through. [The multiplicity comparison](/entry/num-jedense-threshold-cases/) uses it to get $\mathrm{ZEqDimEAlt}$.

## Statement

**Theorem.** $\mathrm{CountEAlt}$ holds.

$\mathrm{CountEAlt}$ says: assume $\mathrm{HypothesesH'}$, $\mathrm{Mult}$ and $\mathrm{CompOf}$. Let $l$ be a prime, $L$ a CM field, $s$ a Hida setting with a level $V$, $1 \le n \le 4$ and $\lambda$ a weight. Then there is a number $a_0$ with this property. Take a type $\tau_0$, a weight $\theta$ and a point $x$ (`IsSpec`), a level $K$ and Hecke eigenvalues of absolute value 1, such that the space of forms `zPart` is not zero and each piece that meets it is irreducible. Then there are a cuspidal $\pi$ of $\mathrm{GL}_n$ over $L$, a form $\sigma$ on the unitary group and local components $C$ of $\pi$ such that, for each $a$, the dimension of the $a$-part of `zPart` is $a_0$ times the rank of the $a$-part of the invariants of $C$.

## Proof

The proof applies `count_e_of_sph_same_at_same_bc_dims` to twelve named lemmas: `WtEx`, `Decomp`, `ZDecE`, `ZEq`, `SphSameAlt`, `AtSameAlt`, `BcOfAlt`, `YDimE`, `CompsEx`, `Slope`, `Ord1Alt` and `EigPi`. It takes $a_0$ from $\mathrm{Mult}$.

## In the Lean code

The theorem is in [CountE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CountE.lean#L21). The lemma is in [TCountE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TCountE.lean#L147), and $\mathrm{CountEAlt}$ is in [ZEqDimE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ZEqDimE.lean#L43).

The lemma does not use its fourth input `ZEq` or its ninth input `CompsEx`: its `intro` discards both. The lemma `zEq` still enters through `zDecE`.
