---
id: p-from-aut
title: Automorphy of the Taylor-Wiles data gives the support properties of the Hecke ideal
kind: theorem
decl: UpperTheory.V.Pa.pFromAut
module: Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.AutomorphicDetection.PfromAut
covers: 920
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{PfromAut}$ of the patching argument in the [main fork](/proof/vwin/). It is a pass-through: the proof is one call to `pFromAut_of` with six proved inputs. The real content is in `pFromAut_of`, its lemma `chain_of`, and the six inputs.

## Statement

Let $s$ be a Hida setting over a CM field $L$, $V_0$ a level with $S' = S$, $\mathcal{O}$ a coefficient ring that is a discrete valuation ring, $n \ge 1$, $r$ a residual datum, $B$ its universal ordinary determinant ring and $J$ an ideal of $B$.

**Theorem.** Assume the cohomology package $\mathrm{CohP}$. Suppose that `LocCFT` holds, that $\varepsilon(g) \not\equiv 1 \bmod l$ for some $g \in G_0$, and that $J$ satisfies `HasAut`: each Taylor-Wiles group with `TWPl` carries a Taylor-Wiles automorphic datum for $J$. Then:

1. `P1core`: if $x$ is a point of type I with the conditions `N1`, `N3`, `N4` and $J \subseteq \ker f_x$, then $J$ lies in each prime below $\ker f_x$;
2. `P3core`: let $x_0, \dots, x_h$ be points of type E with `N1`, `N3`, `N4`, where $x_{i-1}$ and $x_i$ lie on a common thick prime. If a stable prime that contains $J$ lies below $\ker f_{x_0}$, then $J$ lies in each stable or thick prime below $\ker f_{x_h}$.

A prime is stable if the determinant of $B$ over its residue field comes from an absolutely irreducible representation. It is thick if it is not stable and the quotient `E0kap` of the group algebra is not semisimple.

## Proof

The proof is `pFromAut_of norm choice arPl b1Ar b2Ar raw`. Here `norm` proves `Norm` and uses [`Pa.core`](/entry/pa-core/). `choice` proves `Choice`, `arPl` gives Taylor-Wiles places (`ArPl`), `b1Ar` proves `FirstOrderDualArithmeticBound`, `b2Ar` proves `TaylorWilesObstructionBound` and `raw` proves `Raw`. `pFromAut_of` calls `chain_of` and reads off both parts. We have not unfolded the six statements.

## In the Lean code

The theorem is in [PfromAut.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/PfromAut.lean#L9). $\mathrm{PfromAut}$ and `HasAut` are in [TaylorWilesObstructionBound.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/TaylorWilesObstructionBound.lean#L147), `P1core` and `P3core` in [UniversalOrdinaryDeterminantRing.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/WeilGroupCharacters/UniversalOrdinaryDeterminantRing.lean#L284), and `pFromAut_of` in [PFromAutOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ChebotarevFamilies/PFromAutOf.lean#L116). The case $h = 0$ of `P3core` is `P2core`, by `P3core.p2`.
