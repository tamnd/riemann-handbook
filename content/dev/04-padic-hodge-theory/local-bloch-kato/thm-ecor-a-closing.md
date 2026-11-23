---
id: thm-ecor-a-closing
title: The local lifting theorem and its corollary for all data
kind: theorem
decl: GlobalTheory.ThmECorA.closing
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremECorollaryAClosingAllData
covers: 1797
status: drafted
drafted_by: writer@claude
---
This theorem proves two local results on crystalline lattices for every datum: a lifting theorem for finite cocycles along a surjection of lattices, with an explicit exponent, and a bound on the cokernel of the map on $H^1_f$. It takes three literature hypotheses of local [[Galois cohomology|9MPCZ3EAJM]]. Its user is its [second name](/entry/theorem-e-corollary-a-closing-all-data/), which [the fifteen local bounds along a family](/entry/nlink-close-main-alt-alt/) calls.

## Statement

Fix a prime $\ell$, finite extensions $K$ and $L$ of $\mathbb{Q}_\ell$ with $\mathcal{O}$ the integers of $L$, and $n$ embeddings of the maximal unramified subfield of $K$ into $L$. Let $f \colon T_1 \to T_2$ be a surjection of lattices in continuous crystalline representations of $G_K$. Say that $f$ *lifts with exponent* $e$ if for each Bloch-Kato finite cocycle $c$ of $T_2$, the cocycle $\ell^e c$ is the image of a finite cocycle of $T_1$ plus a coboundary.

**Theorem.** Assume `BlochKatoLocal`, local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK`. Then there is a real $C_0$ such that for each datum $D$ (with local data $HW$, $F$, $Cm$ over it):

1. (`Conclusion1 D 800`) If $\ell \ge 5$ and the embeddings meet a condition on letters, then each such $f$ whose Hodge-Tate weights lie in windows of a given shape lifts with an exponent $e$, an explicit function of the windows. Also, for all such parameters, $e \le 800 \left( \frac{h}{(\ell - 1)^{j+1}} + g \cdot m + \log_\ell h \right)$, where $h$ bounds the weights, $j$ is a cut length, $g$ is a size parameter of the windows and $m$ is the largest arc length.
2. (`Conclusion2 D C₂`, for each $C_2 \ge C_0$) If $\ell \ge 11$ and the same letter condition holds, then for each such $f$ with $T_2$ of rank $r$ and with weights in windows, the cokernel of $H^1_f(T_1) \to H^1_f(T_2)$ has length at most $C_2 (n+1) r$ times an explicit expression in the window sizes that has a term divided by $(\ell-1)^{j+1}$.

## Proof

Take $C_0$ to be `localCorollaryConstant`. Fix $D$, $HW$, $F$, $Cm$. The proof collects five inputs:

- `Per.DdREqDcris.record_caseA`: the statement `DdREqDcris` for unramified $K$;
- `Decompl.fontaine_and_decompletion` and `T.fontaine_fullFaithful_exact_psi`: two statements whose names refer to Fontaine's functor and to decompletion;
- `WachUnit.unitGen_exists`: a unit generator of the Wach module for $\ell \ge 5$;
- `T.localLifting_theoremE_hypotheses_admitted`: the 16 local hypotheses `WachCoordinates.admitted` with constant 10. This is the only place where the three literature hypotheses enter.

Then `Ln03.local_corollary_of_de_rham`, applied with $E_1 = 800$ and $E_2 = C_0$, gives part 1. Applied with $E_2 = C_2 \ge C_0$, it gives part 2.

## In the Lean code

The theorem is in [TheoremECorollaryAClosingAllData.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremECorollaryAClosingAllData.lean#L17). The two conclusions are `LiftingTheoremLocalTheory` and `LocalCorollaryLifting` in [WachCoordinates.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L287). We have not unfolded the letter condition, the window shapes, the full bound in part 2, or the inputs of the proof.

- `Conclusion1 D C` and `Conclusion2 D C` depend only on the local theory `D.loc`. The quantifiers over $HW$, $F$ and $Cm$ only ask that such data exist.
- The bound on $e$ in part 1 (`ThmEBound 800`) is a numeric inequality. It does not depend on $D$.
- $C_0$ is `localCorollaryConstant`, defined in [LocalCorollaryConstant.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalCorollaryConstant.lean#L9) by `Classical.choose`. So the Lean code gives no value for $C_0$.
