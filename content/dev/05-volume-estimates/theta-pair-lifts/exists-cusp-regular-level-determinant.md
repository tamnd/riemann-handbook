---
id: exists-cusp-regular-level-determinant
title: A cusp form with a regular level determinant
kind: theorem
decl: GlobalTheory.OrbitSep.exists_cusp_regular_level_determinant
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.ExistsCuspRegularLevelDeterminant
covers: 760
status: drafted
drafted_by: writer@claude
---
This theorem finds, on a good cover of the tower, one cusp form $u$ whose group determinant over a finite group of level automorphisms is not a zero divisor in the ring of modular forms. Its second name is [orbits_separated_by_regular_cusp](/entry/orbits-separated-by-regular-cusp/), which the [covolume bound](/entry/top-covol-g-alt-alt/) reaches through `regular_embeddings_cover_bad_embedding_locus` and `exists_short_integral_vector`. The geometric input is [separate_orbits_by_cusp](/entry/separate-orbits-by-cusp/). Below this theorem are 760 declarations.

## Statement

Let $Y$ be a good cover at level $j$ of a tower `CoreJ` with `LawsJ`, with signature $(p, q)$ at $j$. A *rule* is a function on framed points of the Shimura variety of $Y$, functorial in the coefficient ring (`Rul`). Let $R$ be the ring of rules of some integer weight (`secRing`, the sum of the spaces `secZ e`). A level automorphism $h$ acts on rules by $(h \cdot f)(y) = f(h^{-1} y)$. For a finite group $S$ of level automorphisms and a rule $u$, the *level determinant* is the group determinant

$$\operatorname{levDet}_S(u) = \det\bigl(hg \cdot u\bigr)_{h, g \in S}.$$

**Theorem.** Assume the six published inputs (`PublishedHodgeBundleTheorems`, `GrothendieckDeformation`, `Quoted`, `SiegelToroidalIntegral`, `ToroidalForFanKS`, `SemiAbelianLieSeminegative`). Assume $p, q \ge 1$, $[E:\mathbb{Q}]/2 > 2$, $1 \le j \le m$, $Y$ good for $(e, o)$ with $e \ge 4$, and $r + 1 < g_k$ for both host primes $g_k$. Let $S$ be `grpHR fr` or `grpGHR fr k` for a type frame `fr`. Then there is a cusp form $u$ of weight $c_0 \cdot \lambda_H$ (with $\lambda_H$ the Hodge weight and $c_0$ = `cZero D j`) such that $\operatorname{levDet}_S(u)\, f = 0$ implies $f = 0$ for each $f \in R$.

## Proof

1. `exists_neatPrime_levelAutSubgroup_unipotent` gives an ideal $I$ of norm a prime $g > p + q + 1$, with $g \notin I^2$, that contains the level, such that each element of $S$ is unipotent modulo $I$.
2. The constant $c_0$ is at least $p + q + \binom{d+1}{2} + 1$, with $d$ the dimension (`cZeroN_isLeast`). So [separate_orbits_by_cusp](/entry/separate-orbits-by-cusp/) applies with $s = c_0$. For each connected component $Z$ it gives a complex point $y_Z$ on $Z$ at which cusp forms separate the points $h^{-1} y_Z$ that lie on $Z$.
3. There are finitely many components (`CompFin.finite_comp`). The linear algebra lemma `exists_vector_groupDeterminants_ne_zero` then gives one cusp form $u$ with $\det\bigl(u(g^{-1} h^{-1} y_Z)\bigr)_{h,g} \neq 0$ for every $Z$.
4. Evaluation at $y_Z$ is a ring map, so this determinant is the value of $\operatorname{levDet}_S(u)$ at $y_Z$ (`evR_transl`). The level determinant has an integer weight (`levDet_mem_secZ`). `integerExponentSection_mul_eq_zero_imp_eq_zero` says that such a form, nonzero at a complex point of each component, is not a zero divisor in $R$.

## In the Lean code

The theorem is at [ExistsCuspRegularLevelDeterminant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsCuspRegularLevelDeterminant.lean#L144). `levDet` and `secRing` are in [MemLevEigenIffTransl.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/MemLevEigenIffTransl.lean#L146), and `cZeroN` in [NormNegCmConstantEqAtAllEmbeddings.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NormNegCmConstantEqAtAllEmbeddings.lean#L83).

- The hypothesis $4 \le e$ is never used: the `intro` at line 146 names it `_`.
- `exists_vector_groupDeterminants_ne_zero` and `integerExponentSection_mul_eq_zero_imp_eq_zero` restate `GenericGroupDet.exists_vec_det_ne_zero` and `SecRingNonZeroDiv.eq_zero_of_mul_eq_zero`, whose proofs we have not opened. Nor have we unfolded the subgroups `levelU` and `levelGU` behind `grpHR` and `grpGHR`.
- The name of the second name says "orbits separated"; the statement is about a regular determinant. The orbit separation is in step 2.
