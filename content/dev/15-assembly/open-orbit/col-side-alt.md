---
id: col-side-alt
title: The column side of a geometric family
kind: theorem
decl: GlobalTheory.Fam.colSide_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ColSide
covers: 3232
status: drafted
drafted_by: writer@claude
---
Given a geometric family $a$, family constants $k$ and a good row choice, this theorem builds a column choice and two tuples, $w_0$ and its rescaling $w$, with some twenty conditions. Through the relay [`true_geometry_family_invariance_alt`](/entry/true-geometry-family-invariance-alt/), [the family conditions from the package conditions](/entry/fam-all-q-of-all-true-alt/) uses it for each $k$.

## Statement

Assume `DiscreteSeriesCover` and `HarishChandraModules`. Let $W$ be a real package over $D$ = `I.rec7 l Z` with `AllFamilyConditions W`, and let $m$ = `D.R.m` be the top level. Let $a$ be a geometric family for $W$ and a word $u$ (`GeometricFamily`: a geometry $g$, commuting data $v$, local data, a bottom datum and constants $c_0$). Assume `a.Is`, `a.True`, and that the top matrix $i_A$ of $g$ at level $m$ is the identity. Let $k$ be family constants for $a$ (`FamilyConstants`: residue units $\varepsilon$, bilinear operations, exponents and scalars). Let a row choice be given, one good row for each index $t$, all of the same shape.

**Theorem.** There are a column choice $\mathrm{col}$, tuples $w_0(t)$ and $w(t)$, and local families $F(t)$ such that:

1. `FamilyColumnCondition`: there is $c_0$ with `PinX` for $g$, and for each $t$ a twist datum on which the column is pinned (`PinChL`) and a top datum (`PinTopL`);
2. `ColumnOutputCondition k w₀ w F`. Its main fields: the family is `ColOK`; $F(t)$ pins $w_0(t)$; $w(t)$ has the same $Q$, $e_Q$, $c_Q$, $F_Y$, $F_T$ as $w_0(t)$; $w(t)$ satisfies the place laws `QLaw`, `QLast` and `QFin`; the level, rational vector and chart at zero conditions hold; the scalars of $w(t)$ match $k$, the row and the column; and the coefficients $c_K$, $c_P$ at $t$ and at the base point $\mu_0$ are in `UnitRatio`: some power of their ratio is a nonzero rational number whose primes lie under `Q t`.

## Proof

1. The rows and `a.Is` give `RowOK`. Then `famCh_is_and_tuples_is_of_colOK` shows that the commuting datum of $g$ is good.
2. `exists_quadratic_extension_reads_of_true` gives, for each $t$, quadratic extension data $J(t)$. From $i_A = 1$, `true_geometry_row_pair_relation_alt_alt_alt` gives constants $C_j \neq 0$ and, for each $t$, roots of unity $s$, $\rho$ and scalars $\zeta$. Two more lemmas give volumes $V_j, V_T \neq 0$ and the kernels.
3. For $j < m$, `true_geometry_twist_local_value_alt` and `finComb3` give a finite combination $dd$ equal to the composite of $d_Q$, $d_G$ and $d_T$. `true_geometry_joint_twist_relation_alt` gives the operators $S'$.
4. At level $m$ each $J(t)$ has exactly one character $\beta_0(t)$: the count is a product of ones.
5. The column is `columnChoiceOfCoefficients` with $c_K = V_j C_j c_0(j) \rho_t(j)$ and $c_P = V_T \sum_\beta s_t(m, \beta)$. Then $F$ = `familyOfRowColumnChoices`, $w_0(t)$ is the pinned tuple, and $w(t) = \mathrm{resc}(w_0(t), s_t)$.
6. The field `laws` comes from [`true_geometry_family_final_alt`](/entry/true-geometry-family-final-alt/). The fields `lev`, `vec`, `atQ`, `e` and `zero` come from `true_geometry_quadratic_twist_level_alt`, `true_geometry_joint_twist_identity_alt`, `true_geometry_joint_twist_value_alt`, `true_geometry_joint_twist_data_alt` and `true_geometry_joint_twist_bound_alt`, and `stabK` from `chainKernel_preserves_ramifiedForms_liveCharts`. For `cK` and `cP`: if $x$, $y$ are roots of unity and $c \neq 0$, then $(cx/cy)^{n_1 n_2} = 1$, so `unitRatio_laws` gives `UnitRatio`. By step 4, the sum in $c_P$ has one term.

## In the Lean code

The theorem is in [ColSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ColSide.lean#L35). The conditions are in [FamilyConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamilyConstants.lean#L37) and [FamCol.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamCol.lean#L26).

The two named hypotheses are only passed on, in steps 1 and 6. Step 1 uses `trivialColumnChoice`, a column with no characters, since the commuting datum depends only on $g$. The fields `FT` and `FX` hold by `Set.mem_univ`: the spaces $F_T$ and $F_X$ of these tuples are everything, so those conditions in the place laws are empty. A parallel copy for `RealPack`, `GlobalTheory.Fam.colSide`, is in [TrueGeometryFamilyInvariance.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyInvariance.lean#L53).
