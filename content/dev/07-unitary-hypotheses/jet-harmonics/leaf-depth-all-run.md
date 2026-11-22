---
id: leaf-depth-all-run
title: The four depth bounds at the places of a leaf
kind: theorem
decl: GlobalTheory.RunDepth.leafDepth_all_run
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.LeafDepthAllRun
covers: 4842
status: drafted
drafted_by: writer@claude
---
This theorem bounds the normalized depths of a leaf object at four kinds of places: the good places, the places over $q_1$ and $d$, over the small primes, and over $g_1$ and $g_2$. Its hypotheses are three local statements about formal groups. Its one user, [`leafDepth_all_record`](/entry/leaf-depth-all-record/), proves these three statements and gets the four bounds for the leaf objects of a record. That result goes to [`geoSt_of_pageSt_alt`](/entry/geo-st-of-page-st-alt/), in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $K$ be a number field with an involution, and let $O$ be a leaf object over $K$ (the structure `OnObj`). It has a finite set $T_w$ of finite places of $K$, an index set $J$, real constants ($C, k, m, f, T, Y, \dots$), weights $\theta(l), a(l)$, and bad primes: $g_1, g_2, q_1, d$ and a finite set $s_m$. For a place $w$ let $\ell(w)$ be its residue characteristic and $\bar w$ its conjugate place. The depth is $e_0(w,j) = (E(w,j) - v_w(\sigma(w,j)))/e_w$, with $e_w = v_w(\ell(w))$. Let $N$ be a numerical datum with reals $F_0(w,j)$.

The conclusion has four parts.

1. `LeafDepthGood`: $\theta(l) \ge 0$ and $a(l) \ge 0$ for all $l$; for each finite set $Q$ of primes, $\sum_{p \in Q} \theta(p) \log p \le C/k$ and $T \sum_{p \in Q} a(p) \log p \le C m b$; and for $w \in T_w$ with $\ell = \ell(w)$ not bad and each $j$: if $\ell \le Y$ then $e_0(w,j)$ and $e_0(\bar w,j)$ are at most $F_0(w,j) + a_E(j,\ell) + 1$, and if $\ell > Y$ then $e_0(w,j) = e_0(\bar w,j) = 0 \le F_0(w,j)$. Here $a_E(j,\ell) = A_1(j)/\ell + A_{kw}(j)\theta(\ell) + T a(\ell)$, plus $A_{kw}(j)/\ell^2$ when $\ell > X_2$.
2. `LeafDepthRam`: for $\ell(w) \in \{q_1, d\}$, both depths are at most $s_B(j) + T + 1$; $F_0(w,j) = 0$ if $\ell(w) = q_1$, and $-2fkb' \le F_0(w,j) \le 0$ if $\ell(w) = d$.
3. `LeafDepth2`: for $\ell(w) \in s_m$, both depths are at most $s_C(j) + T + 1$, and $F_0(w,j) = 0$.
4. `LeafDepthLevel`: for $\ell(w) \in \{g_1, g_2\}$, $e_0(w,j) \le 2T - n(w,j)$, $e_0(\bar w,j) \le 2T - n(\bar w,j)$, and $n(w,j) + n(\bar w,j) = -2F_0(w,j)$.

**Theorem.** Assume `AvFSt p`, `HTFSt p` and `UpFSt p` for all primes $p$. Then there is $C_0$ such that the following holds. Let $D$ be a datum with size data $L$, parameters `Pm`, `Tp`, a core $T$ with `LawsM T`, and let $O$, $N$, $\iota \colon J \to \mathbb{N}$ be as above. Assume that $O$ is tied to $D$ (`RunTie`: the bad primes, the constants, $\theta$, $a = 0$ and the depths of $O$ are those of $D$), that `LeafPage O` and `LeafSizes O` hold (positivity, primality and distinctness of the bad primes, size relations), that $F_0$ is the content of $D$ (`ContentEqualsDatumContent`), and that $x \ge 3$, $k b' \le b$, $C_0 \le C$, $10 \le C_{nW}$ and $3 \le x^{e_z/5}$. Then all four parts hold.

The three hypotheses concern a formal group law $F$ with a chart on a commutative group scheme over a complete local domain. `HTFSt` says that the linear terms of finitely many characters of $F$ span the tangent module up to a factor $c$ with $|c|^{p-1} \le |p|$. `AvFSt` and `UpFSt` bound the cokernel of the character map on eigenspaces of an order. [The entry for `goodPrime_packages`](/entry/good-prime-packages/) states `UpFSt` in full.

## Proof

Part 1 and $C_0$ come from [`depthTable_goodPrimes_of_chartForm`](/entry/depth-table-good-primes-of-chart-form/), which uses `UpFSt` only. Parts 2, 3 and 4 come from `leafDepthRam_run`, `leafDepth2_run` and `leafDepthLevel_run`. Only `leafDepth2_run` uses `AvFSt` and `HTFSt`; the other two use no chart statement. The rest is bookkeeping.

## In the Lean code

The theorem is in [LeafDepthAllRun.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/LeafDepthAllRun.lean#L13). The lemmas it calls:

- `GlobalTheory.T.depthTable_goodPrimes_of_chartForm`;
- `GlobalTheory.RunDepth.leafDepthRam_run` in [KLeSubOneOfLt.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/KLeSubOneOfLt.lean#L26);
- `GlobalTheory.RunDepth.leafDepth2_run` in [LeafDepth2Run.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/LeafDepth2Run.lean#L13);
- `GlobalTheory.RunDepth.leafDepthLevel_run` in [LeafDepthLevelRun.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/LeafDepthLevelRun.lean#L18).

The hypotheses $C_0 \le C$, $10 \le C_{nW}$ and $3 \le x^{e_z/5}$ go only to part 1. The four `Leaf…` predicates are in [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L305), and the three chart statements in [StChartF.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PlaceDivisors/StChartF.lean#L133). We have not unfolded `LawsM`, `ParamsT`, `numOf` beyond its fields, or the depth data `depOf`.

Some field names of `RunTie` in [CmQuadraticFormEqAlternatingForm.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/CmQuadraticFormEqAlternatingForm.lean#L40) do not match their statements: `jets_eq_fact` says $g_1 = $ `D.host.g 0`, `cmQuadraticForm_eq_alternatingForm` says $q_1 = $ `D.host.q`, and `depthNumbers_threshold_eq` says $X_2 = $ `L.sc.X'' D.R.n`. The file name has the same mismatch. The field `ad_eq` sets $a = 0$, so under `RunTie` the second sum in part 1 is $0$.
