---
id: arith-hilbert-samuel-of-principalisation
title: The arithmetic Hilbert-Samuel formula for nef bundles, from principalisation
kind: theorem
decl: GlobalTheory.arithHilbertSamuel_of_principalisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArithHilbertSamuelOfPrincipalisation
covers: 1772
status: drafted
drafted_by: writer@claude
---
This theorem proves the arithmetic Hilbert-Samuel formula for a nef hermitian line bundle, $\mathrm{ArithHilbertSamuel}$, from principalisation of ideals in characteristic zero. Its only caller is [the literature form of the formula](/entry/arith-hilbert-samuel-of-literature/), which fills the field `q9` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). The hypothesis is not open: it is proved in the code as `principalisation_closed`. Below this theorem are 1,772 declarations.

## Statement

Let $\mathrm{Princ}$ be the statement `Principalisation`. Let $k$ be a field of characteristic $0$, let $Y$ be an integral scheme, smooth of relative dimension $d$ and projective over $k$, and let $I$ be a nonzero ideal sheaf on $Y$. Then there is $s \colon Y' \to Y$ with $Y'$ integral, smooth of relative dimension $d$ and projective over $k$, such that $s$ is a sequence of smooth blow-ups over the support of $I$ (the predicate `IsSmoothBlowupSeq`, which we have not unfolded), $s$ is an isomorphism over the complement of the support, $s^{-1} I$ is an effective Cartier divisor, and its support has simple normal crossings. This is principalisation of ideals, as proved by Hironaka (Ann. of Math. 79, 1964).

**Theorem.** $\mathrm{Princ}$ implies $\mathrm{ArithHilbertSamuel}$.

$\mathrm{ArithHilbertSamuel}$ is stated in full in [the parent entry](/entry/arith-hilbert-samuel-of-literature/). In short: let $X$ be an arithmetic variety of dimension $D+1$, let $\overline{L}$, $\overline{N}$ be hermitian line bundles on $X$, and let $\overline{L}$ be nef with arithmetic self-intersection $a$. Let $\widehat{H}^0_m$ be the set of sections of $\overline{L}^m \otimes \overline{N}$ of sup norm at most $1$ at each complex place. Then $\widehat{H}^0_m$ is finite for large $m$, and

$$\log \# \widehat{H}^0_m = \frac{a}{(D+1)!}\, m^{D+1} + o(m^{D+1}).$$

## Proof

The proof derives three statements from $\mathrm{Princ}$ and then passes from ample to nef.

1. **Arithmetic intersection calculus.** `MixHt.arCalc_of_principalisation` gives `ArCalc`, a conjunction of seven rules (`ArExists`, `ArChange`, `ArShift`, `ArMix`, `ArProj`, `ArIso`, `ArMetric`) that we have not unfolded. It is the first half of `T.arithIntersectionCalculus_cycleHeights_of_analytic`, applied to two analytic facts that come from $\mathrm{Princ}$: integrability of the Chern forms of log norms and a reciprocity law (`T.archLogNormChernIntegrable_of_principalisation`, `T.archLogNormReciprocity_of_principalisation`).
2. **The ample case.** `T.ampleArithHilbertSamuel_of_principalisation` gives `AmpleHS`. Let $L$ be ample with a semipositive metric and self-intersection $a$, inside a pair $P$ of hermitian bundles (the structure `Pair`, not unfolded). Then there is $t_0$ such that for $t \geq t_0$ a counting function `P.lc m 1 (exp (t m))`, divided by $m^{D+1}$, tends to $(a + (D+1)\, t\, g)/(D+1)!$, where $g$ is a geometric degree `gdeg P.L D`. The proof uses $\mathrm{Princ}$ directly in `T.arithHilbertSamuel_smallSections_change_of_metric`, and through `ArCalc`.
3. **Pull-back.** `SemiPullAll.semiPull_of_principalisation` gives `SemiPull`: the pull-back of a semipositive hermitian line bundle along a morphism of arithmetic varieties over the same base is semipositive. The proof uses $\mathrm{Princ}$ to get a birational, generically smooth model of $X$ (`GenRes.exists_birational_genSmooth`).

Then `T.arithHilbertSamuel_nef_of_ample`, which is `HSNef.arithHilbertSamuel_of_ampleHS`, gives the formula. Finiteness holds for every $m$, by `T.finite_smallSec_hermitian_line_bundle_arith_variety`. For each $c > 0$, an upper bound `T.arith_nef_volume_upper_bound` (from all three statements) and a lower bound `T.arithHilbertSamuel_lowerBound_semiPos_nefOnFibres` (from `ArCalc` and `AmpleHS`) give, for large $m$, that $\log \# \widehat{H}^0_m$ is within $c\, m^{D+1}$ of $a\, m^{D+1}/(D+1)!$. We have not opened the statements of the two bounds.

## In the Lean code

The theorem is in [ArithHilbertSamuelOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelOfPrincipalisation.lean#L11). Its proof is one term:

```
fun h => T.arithHilbertSamuel_nef_of_ample (MixHt.arCalc_of_principalisation h)
  (T.ampleArithHilbertSamuel_of_principalisation h) (SemiPullAll.semiPull_of_principalisation h)
```

The lemmas:

- `HSNef.arithHilbertSamuel_of_ampleHS` in [ArithHilbertSamuelNefOfAmple.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelNefOfAmple.lean#L16);
- `HSNef.ampleHS_of_principalisation` in [AmpleArithHilbertSamuelOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AmpleArithHilbertSamuelOfPrincipalisation.lean#L26);
- `SemiPullAll.semiPull_of_principalisation` in [SemiPullOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiPullOfPrincipalisation.lean#L35);
- `MixHt.arCalc_of_principalisation` in [ArCalcOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArCalcOfPrincipalisation.lean#L12).

`Principalisation` is in [GeometricallyConnectedOfIsIsoRestrict.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/GeometricallyConnectedOfIsIsoRestrict.lean#L118), and `AmpleHS` and `SemiPull` are in [SmallFam.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SmallFam.lean#L69).

The statements `T.arithHilbertSamuel_nef_of_ample` and `T.ampleArithHilbertSamuel_of_principalisation` are restatements: each is a `first | exact ...` tactic that applies the `HSNef` lemma of the same type. The lower bound does not use `SemiPull`.
