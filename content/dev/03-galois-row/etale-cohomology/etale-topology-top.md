---
id: etale-topology-top
title: Finiteness of étale cohomology of proper schemes over an algebraically closed field
kind: theorem
decl: UpperTheory.Et.EtaleTopology.top
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.EtaleTopology
covers: 2249
status: drafted
drafted_by: writer@claude
---
This theorem proves the finiteness axiom E4 of the étale chapter from 27 other axioms of the chapter and one compatibility of $H^1(\mathbb{G}_m)$ with the Picard group. The theorem [e4](/entry/e4/) supplies the compatibility, and [the finiteness theorem](/entry/etale-finiteness-of-duality/) supplies the 27 axioms. The result goes to [VFin holds](/entry/v-fin-holds/), which needs finite $\ell$-adic cohomology. Below this theorem are 2,249 declarations of the proof.

## Statement

The cohomology is the one of the étale chapter: $H^n(X, F)$ is computed from an injective resolution of $F$ on the big étale site, and $\mathbb{Z}/q(i)$ is the Tate twist.

Let $\mathrm{Pic}$ be the statement: for each commutative ring $A$, there is a group isomorphism $H^1(\operatorname{Spec} A, \mathbb{G}_m) \cong \operatorname{Pic}(A)$.

**Theorem.** Assume $\mathrm{Pic}$. Assume the axioms A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5, D1 to D3 and E1 to E3 of the étale chapter. Let $k$ be an algebraically closed field, $q \neq 0$ an integer invertible in $k$, and $X$ a proper scheme over $k$. Then $H^n(X, \mathbb{Z}/q(i))$ is finite for all $n, i \in \mathbb{Z}$.

This is the finiteness theorem for proper schemes of SGA 4, Exposé XIV (Artin), for constant coefficients $\mathbb{Z}/q(i)$ only.

## Proof

The proof builds 133 facts and calls `LateralTheory.E.E4.goal_of` on 13 of them. That lemma does an induction on the degree $n$. Negative degrees vanish by axiom A9. Fix $n$ and assume finiteness in all degrees below $n$, for all proper $X$.

1. **Kernels.** For a proper surjection $f \colon Y \to X$, Čech descent along $f$ (`LeafDesc`, proved by `curve_etale_descent`) and `LeafSS`, built from a filtration of the Čech complex, show that $\ker(f^* \colon H^n(X) \to H^n(Y))$ is finite.
2. **Curves.** For a proper smooth curve $C$ over an algebraically closed field, $H^1$ and $H^2$ are finite and $H^m = 0$ for $m \geq 3$ (`LeafCurve`). The input is the finiteness of $H^1(\operatorname{Spec} B)$ for Dedekind $B$ of finite type (`LeafKum`). It comes from the finiteness of $B^\times / B^{\times q}$ (`LeafUnits`) and of $\operatorname{Pic}(B)[q]$ (`LeafPic`), with $\mathrm{Pic}$.
3. **Induction on dimension.** Let $X$ be integral. If $\dim X \leq 0$, `LeafPt` applies. Otherwise `LeafGeo` fibres a modification $Y_0 \to X$ by curves over a base $B$ with $\dim B < \dim X$. `LeafKill` gives finite covers $C_2 \to C_1 \to C_0$ of a geometric fibre $C_0$ that kill $H^2(C_0)$ and then $H^1(C_1)$. By `LeafSpec` and `LeafGhost`, a class on $Y_0$ that vanishes over a closed subset $W \subset B$ comes from $H^n(B)$ after pullback to $Y_2$. Finiteness on $B$ and on the preimage of $W$ holds by induction. Step 1 and the exact-sequence lemma `fin_of` then give finiteness for $X$.
4. **General $X$.** `LeafComp` gives a proper surjection onto $X$ from a scheme with finite $H^n$, given finiteness on integral closed subschemes. Step 1 ends the proof.

The rest is bookkeeping.

## In the Lean code

The theorem is in [EtaleTopology.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleTopology.lean#L133). The induction is `goal_of` in [H0TwistOverClosedField.lean](lean:Development/EtaleCohomology/EtaleSheaves/H0TwistOverClosedField.lean#L114). The leaves it uses:

- `UpperTheory.leafH0_holds`: $H^0$ of a point is finite, and $H^0$ of a connected scheme is $H^0$ of the point.
- `UpperTheory.curve_etale_descent`, `curve_picard_of_selmerPicard_of_modelCurve`, `leafCurve_of_leafH0`, `Cb.curve_cohomology_killed_by_finite_cover`, `Cb.geometric_fibre_cohomology_constant`.
- `LateralTheory.E.LeafGeoCut.goal_of`, the end of about 40 lemmas on models of curves and spreading out.
- `LateralTheory.E.LeafGhostCut.goal_of_all`, the end of about 50 lemmas on strictly henselian stalks and on classes killed locally.

The axiom statements are in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L145). The hypothesis $\mathrm{Pic}$ is `GlobalTheory.EtC.DivisorPicardCompatibility`. It is used only once, at [line 166](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleTopology.lean#L166), to supply the Picard input of the Kummer leaf. The name `top` says nothing about the statement. We have not unfolded the leaves below `LeafGhost`.
