---
id: exists-sum
title: The Hecke sum over a reduced ring is a trace
kind: theorem
decl: GlobalTheory.HeckeEx.exists_sum
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.HeckeTransformOfPointLaws
covers: 372
status: drafted
drafted_by: writer@claude
---
This lemma is step 2 of [the Hecke transform of a section](/entry/sec-transform/). Over a reduced ring $R$, the sum of a section over the Hecke kernels is defined only at geometric points. The lemma finds one element $v \in R$ that has these sums as its values. The element is a trace along the Hecke correspondence.

## Statement

Let $1 \le p + q$, let $(\mathfrak{P}, p)$ be admitted, and assume `TotalAt`: every Hecke kernel at a geometric point has a target point. Let $f$ be a section of weight $(a, n)$, let $R$ be a reduced $c.F$-algebra, and let $y$ be a framed point over $R$. Then there is $v \in R$ such that
$$\varphi(v) = \sum_C \mathrm{term}(f, z, C)$$
for every algebraically closed $\Omega$, every $\varphi : R \to \Omega$ over $c.F$, and every framed point $z$ over $\Omega$ that is the base change of $y$ along $\varphi$. The terms are those of the parent entry.

## Proof

1. `heckeInFamilies` gives a Hecke correspondence $Z$ over the moduli space whose first projection $\pi_1$ is finite and étale.
2. Pull $Z$ back along $y$. `exists_finiteEtale_algebra_pullback_affine` gives a finite étale $R$-algebra $B$ with this pullback as spectrum. $B$ is reduced, by `isReduced_algebra_of_smooth_of_isReduced`.
3. Base change $y$ to $B$. `exists_term` gives $b \in B$ whose value at each geometric point of $B$ is the term of $f$ at the matching kernel.
4. `exists_trace_eq_finsum_geometric_points_etale` gives $v \in R$ with $\varphi(v) = \sum_\chi \chi(b)$, where $\chi$ runs over the maps $B \to \Omega$ that extend $\varphi$. For a finite étale algebra this is the trace of $b$, but the Lean statement asks only for some $v$ with this property.
5. The maps $\chi$ are in bijection with the points of $Z$ over $z$, and so with the Hecke kernels $C$ (`exists_equiv_heckeKernelScheme_points_heckeKernels`). The sums agree term by term.

## In the Lean code

The lemma is on [line 194 of HeckeTransformOfPointLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeTransformOfPointLaws.lean#L194). The helper `exists_term` is on line 137 and `term` on line 44. The trace lemma is a second name for `EtaleTraceGeom.exists_trace_eq_finsum` ([ExistsTraceEqFinsumGeometricPointsEtaleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsTraceEqFinsumGeometricPointsEtaleStatement.lean#L9)). `heckeInFamilies` is in [HeckeInFamilies.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/HeckeInFamilies.lean#L20). We have not opened the proofs of these lemmas.

The sum is a `finsum`. It is $0$ when the set of kernels is infinite, but here it is in bijection with the maps $\chi$ from the finite $R$-algebra $B$, which are finitely many. The hypothesis $1 \le p + q$ is used only by `heckeInFamilies`.
