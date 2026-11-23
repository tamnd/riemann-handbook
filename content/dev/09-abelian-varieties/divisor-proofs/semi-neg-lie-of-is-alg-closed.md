---
id: semi-neg-lie-of-is-alg-closed
title: Seminegativity of the Lie algebra over an algebraically closed field, by adelic matrices
kind: theorem
decl: GlobalTheory.Nef.semiNeg_lie_of_isAlgClosed
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LieSheafSemiAbelianSemiNegOfIsAlgClosed
covers: 423
status: drafted
drafted_by: writer@claude
---
This theorem proves that the Lie algebra of a semi-abelian scheme over a curve is seminegative, when the base field is algebraically closed of characteristic $0$. The second name [lieSheaf_semiAbelian_semiNeg_of_isAlgClosed](/entry/lie-sheaf-semi-abelian-semi-neg-of-is-alg-closed/) passes it to [the case over any field](/entry/semi-abelian-lie-seminegative/). The proof describes a vector bundle by an adelic family of transition matrices and bounds the degree by a bound on the degrees of lines.

## Statement

Let $k$ be an algebraically closed field of characteristic $0$, let $C$ be a smooth projective geometrically connected curve over $k$, and let $G$ be a semi-abelian group scheme over $C$. Let $W$ be a vector bundle of rank $r$ on $C$ with a monomorphism $W \to \mathrm{Lie}\,G$. Then $\deg \det W \leq 0$.

The terms are defined in [the entry for the general case](/entry/semi-abelian-lie-seminegative/).

## Proof

Let $K$ be the function field of $C$. A *place* $v$ of $K/k$ is a surjective discrete valuation of $K$ that is trivial on $k$ (`Place`), with $\operatorname{ord}_v$ its order. A family $g = (g_v)$ of matrices in $M_r(K)$ is *admitted* if each $\det g_v \neq 0$ and $g_v \in \mathrm{GL}_r(\mathcal{O}_v)$ for almost all $v$. Its degree is $\deg g = \sum_v \operatorname{ord}_v \det g_v$.

1. `exists_isGenOver` gives the generic point $x \colon \operatorname{Spec} K \to C$.
2. `exists_genericFrame_and_localFrames_allPlaces` gives a nonempty open $V_0$, a frame $s$ of $W$ on $V_0$ and an admitted family $g$. At each place $v$, the matrix $g_v$ writes $s$ in a local frame of $W$ near the centre of $v$, read at $x$ (`LocFrame`).
3. `lie_subsheaf_lines_degree_nonpos` uses $W \subset \mathrm{Lie}\,G$ and the semi-abelian hypothesis. It gives `LinesLE g 0`: for each finite extension $E/K$, each map $\rho$ from the places of $E$ to the places of $K$ that restricts valuations, and each nonzero $w \in E^r$,
$$\sum_{p} \operatorname{ordVec}_p\bigl(g_{\rho(p)}\, w\bigr) \leq 0 \cdot [E:K],$$
where $\operatorname{ordVec}_p$ is the order of a vector (the least order of its entries). By the names, the left side is the degree of the line in $W$ spanned by $w$ after base change to $E$. We have not checked the sign convention.
4. `isFunctionFieldOfOneVariable_of_genericPointOfCurve` shows that $K$ is finite over $k(t)$ for some transcendental $t$. Then `adelicMatrixFamilyDegree_le_rank_mul_line_bound` with $b = 0$ gives $\deg g \leq r \cdot 0 = 0$.
5. `detDegree_nonpos_of_adelicDegree_nonpos` turns $\deg g \leq 0$ into $\deg \det W \leq 0$.

The geometry of $G$ enters only in step 3. Steps 4 and 5 are about vector bundles on curves.

## In the Lean code

The theorem is at [LieSheafSemiAbelianSemiNegOfIsAlgClosed.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieSheafSemiAbelianSemiNegOfIsAlgClosed.lean#L27). `Place`, `admitted`, `deg` and `LinesLE` are in [IsAdmissibleIntegralBasisChangeOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsAdmissibleIntegralBasisChangeOne.lean#L15), and `IsGenOver` and `LocFrame` in [IsRatPath.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsRatPath.lean#L61).

The lemmas it calls, each a second name of a theorem in `GlobalTheory.Nef`:

- `exists_genericFrame_and_localFrames_allPlaces` (`exists_frame_locFrames`);
- `lie_subsheaf_lines_degree_nonpos` (`linesLE_zero_of_sub_lie`);
- `isFunctionFieldOfOneVariable_of_genericPointOfCurve` (`CurveFF.isFF_of_isGenOver`);
- `adelicMatrixFamilyDegree_le_rank_mul_line_bound` (`deg_le_rank_mul_of_linesLE`);
- `detDegree_nonpos_of_adelicDegree_nonpos` (`interNum_det_nonpos_of_deg_nonpos`).

We have read their statements, not their proofs. We have not unfolded `IsFrame`. The bound of step 4 holds for any $b$; here only $b = 0$ is used.
