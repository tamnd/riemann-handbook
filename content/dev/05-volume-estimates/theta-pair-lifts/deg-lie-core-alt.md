---
id: deg-lie-core-alt
title: The Lie degree of a rational point at the last level
kind: theorem
decl: GlobalTheory.DefCoreLie.degLie_core_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DegLieCore
covers: 532
status: drafted
drafted_by: writer@claude
---
This theorem computes the Lie degree of a rational point on a component of the moduli space at the last level: it is $-\mathrm{flatDegVal}$, a multiple of the log period of a Kronecker character. Its only user is its renaming [degLie_eq_neg_flatDegVal_at_last_index](/entry/deg-lie-eq-neg-flat-deg-val-at-last-index/), which [flat sections at the last level](/entry/flat-exists-at-core-alt/) uses to fix the degree of each flat section. Below this theorem are 532 declarations.

## Statement

Use the point $p$, the level $i$ and the notation of [flat sections at the last level](/entry/flat-exists-at-core-alt/). Let $X$ be the moduli space at level $i + 1$ over the coefficient field $F$, and let $(p_i, q_i)$ be the signature of its datum. A *point datum* $P$ on a component $Z$ (`PtData`) is an $F$-rational point $y_0$ that lies only on $Z$, with a frame matrix $B_w(\tau)$ at each finite place $w$ of $F$ (equal to $1$ at almost all $w$) and a matrix $X_\sigma(\tau)$ at each embedding $\sigma$ of $F$. Its *Lie degree* at $\tau$ is

$$\deg_{\mathrm{Lie}} P(\tau) = \sum_w v_w\bigl(\det B_w(\tau)\bigr)\,\ell_w - \frac{1}{[F:\mathbb{Q}]}\sum_\sigma \log\bigl|\det X_\sigma(\tau)\bigr|,$$

where the weights $\ell_w$ satisfy $\sum_w v_w(n)\,\ell_w = \log n$ for each integer $n \ge 1$ (`sum_vAdd_nat`). This is `degLie`, through `detDeg` and `lineDeg`. Let

$$\mathrm{flatDegVal} = \frac{p_i - q_i}{2}\log\Omega + q_i\bigl(\log d - \mathrm{lrd}(E)\bigr).$$

**Theorem.** Let $p$ satisfy `RowsTAlt`, let $i + 1 = m$, and assume `GramAt`, `WtNum`, `HostNum` and `FnAlgClosed` at level $i + 1$. Then for each component $Z$, each point datum $P$ on $Z$ and each $\tau \in \Psi$, $\deg_{\mathrm{Lie}} P(\tau) = -\mathrm{flatDegVal}$.

## Proof

1. `finite_nonempty_components_and_dict_mem_dom` gives the definite case `DefCase`, in particular $q_i = 0$ and $p_i \ge 1$. `laws_core` gives the laws `Laws` of the uniformizations.
2. `logPeriod_eq_kroneckerCharacter_logPeriod_of_host` gives a Kronecker character $\chi$ modulo $d$ with $\operatorname{Re}\log\Omega(E, \chi) = \log\Omega$, where $\log\Omega(E,\chi) = \gamma + \log(2\pi / \mathrm{rd}(E)) - L'(1,\chi)/L(1,\chi)$ and $\mathrm{rd}(E)$ is the root discriminant.
3. `frameDeg_def`, fed with `cmObject_definite_lieEigenLattice_degree_difference`, gives `FrameDeg`: each archimedean section on $Z$ at $\tau$ has degree $\tfrac{p_i - q_i}{2}\operatorname{Re}\log\Omega(E,\chi)$. Its proof picks a CM point of good reduction on $Z$ and compares the degrees of two eigenlattices of the CM object.
4. `nonempty_flatSec` gives a flat section $s$ on $Z$ at $\tau$. Step 3 applies to its frame.
5. `degree_dualDetLie_eq_neg_flatSection_degree` gives $\deg_{\mathrm{Lie}} P(\tau) = -\deg s$. With steps 3 and 4 this is $-\mathrm{flatDegVal}$.

The rest is bookkeeping.

## In the Lean code

The theorem is at [DegLieCore.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DegLieCore.lean#L16). It calls `GlobalTheory.T.finite_nonempty_components_and_dict_mem_dom`, `GlobalTheory.LawsCore.laws_core`, `GlobalTheory.T.logPeriod_eq_kroneckerCharacter_logPeriod_of_host`, `frameDeg_def`, `GlobalTheory.T.cmObject_definite_lieEigenLattice_degree_difference`, `GlobalTheory.FlatLine.Definite.nonempty_flatSec` and `GlobalTheory.T.degree_dualDetLie_eq_neg_flatSection_degree`.

- The proof is a copy of `degLie_core` in [ComponentPointLastIndex.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComponentPointLastIndex.lean#L47). That theorem assumes `RowsT` instead of `RowsTAlt` and gets `DefCase` from `deformation_case_finite_components`.
- The hypotheses `RowsTAlt`, `GramAt`, `WtNum` and `HostNum` are used only by the first lemma.
- Since $q_i = 0$, the value is $\tfrac{p_i}{2}\log\Omega$. The statement keeps the general form of `flatDegVal`.
- We have not unfolded `FlatSec`, `ArchSec`, the CM objects of step 3, or the proof of `cmObject_definite_lieEigenLattice_degree_difference`.
