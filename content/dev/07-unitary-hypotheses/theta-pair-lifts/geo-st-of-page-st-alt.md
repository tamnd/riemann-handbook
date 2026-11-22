---
id: geo-st-of-page-st-alt
title: The lattice and depth conditions of a record object, from its page conditions
kind: theorem
decl: GlobalTheory.BigOn.geoSt_of_pageSt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.GeoStOfPageSt
covers: 5131
status: drafted
drafted_by: writer@claude
---
This theorem proves the "geometric statement" about the record objects of a family from their "page statement". It is an input of [`ontoX_of_hypotheses_alt_alt`](/entry/onto-x-of-hypotheses-alt-alt/), half of branch 2 of the [unitary hypotheses node](/proof/unitary-hypotheses/). There `pageSt_alt` proves the page statement. Below this theorem are 5,131 declarations, 4,843 of them below [`leafDepth_all_record`](/entry/leaf-depth-all-record/).

## Statement

Both sides have the form `ForallRecordObjects Q`. This says: for small $\varepsilon$ and each large family in `FamHyp` (in the sense of [`Closed`](/step/closed-def/)), there is $c_0$ such that, for each constant record $c = (C, C_{b1}, C_{b2})$ with $C \ge c_0$, $C_{b1} \ge 14$ and $C_{b2} \ge 66C + 4$, there is $x_0$ such that $Q(O)$ holds at all $x \ge x_0$, all points $p$ with the point conditions and `More p`, all pairs of runs $r$ and all objects $O$ recorded at $p$ along $r$ (`RecAt`).

An object $O$ (`OnObj`) carries, for each index $j$, a representation $\rho_j$ of a finite group $P$ on $K^{n_j}$, a subgroup $U$, a character $\psi$, lattices $M_j$, lattices $\Theta_v, \Theta^K_v, \Theta^0_v$ and exponents $e_0(v,j)$ at each finite place $v$, and real constants.

**Theorem.** The page statement implies the geometric statement.

The page statement has nine facts: `LeafPage` (the constants are at least 1, $f \ge 8$, $g_1, g_2, q_1, d$ are four distinct primes outside a finite set $s_m$), `LeafSizes`, `LeafX`, `LeafBad`, `LeafLevelSq`, `LeafYBound`, the equation $O.b = b$ for the size data, $E_{1u} \ge 0$, and a formula for the error constant. The geometric statement asks:

1. `LeafSup`: each $M_j$ is a full lattice, stable under $\rho_j(P)$;
2. `LeafSpan`, `LeafLemmaS`, `LeafData`: at each twisted place $w$ and at its conjugate $\bar w$, $\Theta_v$ and $\Theta^K_v$ are full lattices, $\Theta_v \subseteq M_j$ is $P$-stable and lies in $\sigma \Theta^K_v$ with $\sigma \ne 0$, and $\Theta^0_v$ is finitely generated, lies in the $(U,\psi)$-eigenspace and contains $|U|$ times the cut of $\Theta^K_v$;
3. `HasIndexBound`: lattices $\Theta^1_v$ and constants bound the index of $M_j \cap W$ over $\Theta^1_v \cap W$ for each subspace $W$;
4. four depth conditions: bounds on $e_0(w,j)$ and $e_0(\bar w, j)$ at twisted places $w$, one for each kind of residue characteristic ($q_1$ or $d$; in $s_m$; $g_1$ or $g_2$; all others).

## Proof

1. `runsHold_of_ties` gives $C_K, x_a$ and `RunsHold` for runs that satisfy the core ties and a numerical condition `PageNum` at $x_a$.
2. `leaves_sup_span_data` gives $x_b$ and facts 1 and 2 from `RunsHold`, `PageNum` at $x_b$ and group and tuple conditions.
3. `leafDepth_all_record` gives $C_d$ and the four depth conditions from `LeafPage`, `LeafSizes` and size conditions on $x$.
4. `runNumericalConditions_hold_along_family`, at $x_a$ and at $x_b$, gives `PageNum` and the size conditions eventually along the family.

The proof joins the page statement with step 4 and takes the largest constants. At a point, `links2_of_single_index_twisted` gives the group and tuple conditions. Then `hasIndexBound_of_runs` gives fact 3 from `RunsHold`, `LeafSup`, `LeafSpan` and $O.b = b$. Step 3 also needs the content equality `indefinitePoint_splitPartContent_eq_forcedContent`.

## In the Lean code

The theorem is in [GeoStOfPageSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeoStOfPageSt.lean#L21). The two statements are in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L37). The leaf predicates are in [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L241), and `HasIndexBound` is in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L77). We have not unfolded `FamHyp`, `RecAt`, `RunsHold` or `PageNum`.

- The proof uses only `LeafPage`, `LeafSizes` and $O.b = b$ of the nine page facts. It drops the other six at line 34.
- The section `Comparison₂` (lines 17 to 20) is empty: it declares variables and nothing else.
- `GlobalTheory.T.geoSt_of_pageSt'` in GeoStOfPageStStatement.lean (line 13) is a copy of this theorem.
