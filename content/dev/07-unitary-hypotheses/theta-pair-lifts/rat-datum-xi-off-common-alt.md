---
id: rat-datum-xi-off-common-alt
title: A rational datum for the off part of the twisted function
kind: theorem
decl: GlobalTheory.Fam.ratDatum_xiOff_common_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RatDatumXiOffCommon
covers: 307
status: drafted
drafted_by: writer@claude
---
For a geometric family with top matrix $1$, this theorem finds constants $C_j \neq 0$ and shows that $C_j$ times the off part $\xi^{\mathrm{off}}_j$ of the twisted function of any quadratic extension datum is a rational datum for the vacuum of level $j$. The constants do not depend on $t$ or on the datum. Through the restatement [`true_geometry_row_pair_relation_alt_alt`](/entry/true-geometry-row-pair-relation-alt-alt/), [`dat_exists`](/entry/dat-exists/) uses it to build the full datum `J.Dat`, which [the column side of a geometric family](/entry/col-side-alt/) uses in step 2.

## Statement

Let $W$, $u$ and the geometric family $a$ be as in [the column side](/entry/col-side-alt/), with `AllFamilyConditions W`, `a.Is`, `a.True`, and the top matrix $i_A$ of $a.g$ at level $m$ equal to the identity. A quadratic extension datum $J$ for $a$ and $t$ (`QuadraticExtensionData`) has a twist datum $J.A$, places $\mathrm{pl}_1, \dots, \mathrm{pl}_r$ in the set `Q t`, a local datum `QExt` at each of them, and maps $\iota_j$ from tuples of local characters to the characters $\mathrm{Ch}_0(j)$ of $J.A$. `J.Reads` is a list of 17 compatibility conditions.

Let $\xi_j(\alpha, \gamma)$ be the twisted function `J.A.xi` on matrices $z$ over $E$. `xi_eq_xiOff_mul` splits it as $\xi^{\mathrm{off}}_j \cdot \prod_{P \notin v_G} \xi_P$, where $\xi^{\mathrm{off}}_j$ is an archimedean factor `phiT` times the local factors $\xi_P$ at the bad primes $P \in v_G$.

For a finitely supported $c$ on adelic matrices, $\mathrm{comb}(c) f = \sum_x c(x)\, h(x) f$, with $h$ the Heisenberg action. `IsRatDatum e Ξ f₀ f` means: there is $\Phi$ on adelic matrices, supported on the $e$-part of $k^{-1}\Lambda$ and invariant under the $e$-part of $k\Lambda$ for some $k > 0$ ($\Lambda$ the standard lattice), with $\Phi(e\gamma) = \Xi(\gamma)$ for rational $\gamma$, such that each place model at $e$ that sends the lattice indicator to $f_0$ sends $\Phi$ to $f$.

**Theorem.** There are $C_j \neq 0$ ($j < m$) such that for each $t$, each $J$ with `J.Reads`, each sum $e$ of local idempotents on $v_T(u) \cup v_G$ (`IsIdemSum`), each $j < m$ and all $\alpha$, $\gamma$:

$$\mathrm{IsRatDatum}\bigl(e,\; C_j\, \xi^{\mathrm{off}}_j(\iota\alpha, \iota\gamma),\; \mathrm{vac}_j,\; \mathrm{comb}(d_G(j))\, \mathrm{comb}(d_T(j))\, \mathrm{vac}_j\bigr).$$

## Proof

1. `true_geometry_row_pair_symmetry_alt` gives $C'_j \neq 0$ and, for each local group $n$ of $a$, a function $\Xi_n$ that is a local factor (`IsLocFac`) at the place $\mathrm{pl}(n)$ for the combination $c_g(n, j)$, with $\prod_{P \in v_G} \xi_P = C'_j \prod_n \Xi_n$. Put $C_j = (C'_j)^{-1}$.
2. `true_geometry_twist_reduction_alt`: the factor `phiT` is a rational datum on $v_T(u)$ for $\mathrm{vac}_j$ and $\mathrm{comb}(d_T(j))\,\mathrm{vac}_j$.
3. `true_geometry_chain_descent_alt` says that these two functions are theta functions and that $\mathrm{vac}_j$ is a lattice vacuum. The lattices of level $j$ and $j+1$ are self-dual and equal to the integral vectors. The places $\mathrm{pl}(n)$ list $v_G$ without repetition, and `type_primes_disjoint'` gives $v_T(u) \cap v_G = \emptyset$.
4. `rationalDatum_foldr_local_combinations` adds the local factors $\Xi_n$ at the places of $v_G$ to the datum of step 2. The field `gpin.dG` of `a.Is` identifies the iterated combination with $\mathrm{comb}(d_G(j))$.
5. By step 1, $C_j \xi^{\mathrm{off}}_j = \mathrm{phiT} \cdot \prod_n \Xi_n$. The rest is field arithmetic.

## In the Lean code

The theorem is at [RatDatumXiOffCommon.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RatDatumXiOffCommon.lean#L22). `IsRatDatum` is in [IsRatDatum.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsRatDatum.lean#L26), `xiOff` in [XiEqXiOffMul.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/XiEqXiOffMul.lean#L106), and `QuadraticExtensionData` in [QuadraticExtensionData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/QuadraticExtensionData.lean#L23). The lemmas it calls:

- `true_geometry_row_pair_symmetry_alt`, `true_geometry_chain_descent_alt`, `true_geometry_twist_reduction_alt`, `type_primes_disjoint'`;
- `rationalDatum_foldr_local_combinations`, the gluing step.

We have not unfolded `IsLocFac`, the place models or `QExt`. `QExt` holds a tame character, unramified characters, coset representatives and local combinations; we have not checked how it relates to a quadratic extension. The hypothesis `J.Reads` is only passed to the two lemmas of steps 1 and 2.
