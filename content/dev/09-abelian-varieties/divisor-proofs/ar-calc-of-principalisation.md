---
id: ar-calc-of-principalisation
title: The rules of arithmetic intersection, from principalisation
kind: theorem
decl: GlobalTheory.MixHt.arCalc_of_principalisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArCalcOfPrincipalisation
covers: 683
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ArCalc}$, seven rules of arithmetic intersection theory, from principalisation of ideals. It is the first of the three statements in the proof of [the arithmetic Hilbert-Samuel formula from principalisation](/entry/arith-hilbert-samuel-of-principalisation/). It has three more users, among them [the ample counting limit](/entry/ample-hs-of-principalisation/). The proof is one line: it takes the first half of a conjunction, so the theorem is a pass-through.

## Statement

Let $\mathrm{Princ}$ be principalisation, as in [the parent entry](/entry/arith-hilbert-samuel-of-principalisation/). In each rule, $X \to \operatorname{Spec} k$ is an arithmetic variety of dimension $D+1$ (the predicate `IsArithVar p D`: $X$ is integral, projective and flat over an order $k$ in a number field), and the line bundles are hermitian. $\mathrm{ArCalc}$ is the conjunction of:

- `ArExists`: each hermitian line bundle has an arithmetic height function on the points of $X$, and each finite family has an arithmetic intersection functional $\Phi$ and a geometric one;
- `ArChange`: the trivial bundle with the weight $u$ (a smooth function at each complex place) meets $D$ copies of a tensor combination $\overline{L}$ of the family in $\tfrac12 \sum_\sigma \int u_\sigma\, c_1(\overline{L})^D$ (the Lean `chInt`);
- `ArShift`: a constant shift $t$ of the metric of $\overline{L}$ adds $(D+1)\, t \deg L$ to the self-intersection;
- `ArMix`: for a rational section $r$ of $\overline{M}$, the number $\overline{M} \cdot \overline{L}^D$ is the sum of the heights of the components of $\operatorname{div} r$, weighted by multiplicity, minus an archimedean integral of $\log \|r\|$;
- `ArProj`: the projection formula for a dominant map of arithmetic varieties of the same dimension, with the degree of the map as factor;
- `ArIso`: invariance under isometries and compatibility with tensor products;
- `ArMetric`: a change of the metric of $\overline{M}$ by $u$ adds the same term $\tfrac12 \sum_\sigma \int u_\sigma\, c_1(\overline{L})^D$.

The rules have the shape of the arithmetic intersection theory of Bost, Gillet and Soulé (J. Amer. Math. Soc. 7, 1994). We have not unfolded `IsArFun`, `IsArithHeight` or `chInt`.

**Theorem.** $\mathrm{Princ}$ implies $\mathrm{ArCalc}$.

## Proof

Two analytic statements come from $\mathrm{Princ}$:

1. `ArchInteg`, from `T.archLogNormChernIntegrable_of_principalisation`: the predicate `ArchIntegrable` holds for each rational section. We have not unfolded it; by its name, the archimedean integrals converge.
2. `ArchRecip`, from [`T.archLogNormReciprocity_of_principalisation`](/entry/arch-log-norm-reciprocity-of-principalisation/): a reciprocity law for the archimedean terms of two sections $s$, $t$ with no common divisor, proved in [`archRecip_of_principalisation`](/entry/arch-recip-of-principalisation/).

Then `T.arithIntersectionCalculus_cycleHeights_of_analytic`, a renaming of `MixHt.arCalc_cycleHeights_of_analytic`, gives $\mathrm{ArCalc} \wedge \mathrm{CycleHeights}$, and the theorem keeps the first half. The real work is in the lemmas that `MixHt.arCalc_cycleHeights_of_analytic` applies, which we have not opened.

## In the Lean code

The theorem is in [ArCalcOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArCalcOfPrincipalisation.lean#L12). `ArCalc` and its seven parts are in [EqOfIsometricTrivShift.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/EqOfIsometricTrivShift.lean#L161). `ArchInteg` and `ArchRecip` are in [IsAmbOfIsArithVar.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsAmbOfIsArithVar.lean#L110). The second half, `CycleHeights`, is proved and dropped. `ArCalc` is in the namespace `Published`, but here it is proved.
