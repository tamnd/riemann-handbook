---
id: charpoly-de-rham-homology-endomorphism-eq-map-ladic
title: The de Rham and l-adic characteristic polynomials agree (statement form)
kind: theorem
decl: GlobalTheory.T.charpoly_deRhamHomology_endomorphism_eq_map_ladic
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CharpolyDeRhamHomologyEndomorphismEqMapLadicStatement
covers: 706
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [GlobalTheory.DeRham.charpoly_push_eq](/entry/charpoly-push-eq/), which has the proof and the same statement. It sits below [the six facts about the Kuga-Sato tower](/entry/kodaira-spencer-of-weight-one/). Its users apply it to the action of an element of $O_F$ on de Rham homology.

## Statement

Use the notation of [charpoly_push_eq](/entry/charpoly-push-eq/): $k$ is algebraically closed, $A$ is an abelian scheme over $k$ with an endomorphism $f$, and $H_1^{\mathrm{dR}}(A)$ (`HdR A`) is the dual of the primitive de Rham classes, with $f_*$ the induced map.

**Theorem.** Let $L$ be a free $\mathbb{Z}$-module of finite rank with $\varphi \in \operatorname{End}(L)$, and $\ell$ a prime that is not $0$ in $k$. Assume that for each $j$ there is a group homomorphism $\mathrm{ev}_j \colon L \to A(k)$ with $\mathrm{ev}_j \circ \varphi = f \circ \mathrm{ev}_j$, kernel $\ell^j L$ and image $A[\ell^j](k)$. If $H_1^{\mathrm{dR}}(A)$ has finite dimension, then $\operatorname{charpoly}(f_*)$ is the image of $\operatorname{charpoly}(\varphi)$ in $k[X]$.

## Proof

The proof is `first | exact @GlobalTheory.DeRham.charpoly_push_eq | ...`. The real steps are in [charpoly_push_eq](/entry/charpoly-push-eq/) and [the algebraically closed case](/entry/charpoly-push-eq-map-charpoly/). The positive characteristic case is [charpoly_deRhamHomology_abelianVariety_charP](/entry/charpoly-de-rham-homology-abelian-variety-char-p/), an alias of [charpoly_push](/entry/charpoly-push/).

## In the Lean code

The theorem is in [CharpolyDeRhamHomologyEndomorphismEqMapLadicStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyEndomorphismEqMapLadicStatement.lean#L8). It has two users: `finrank_quot` in [HarrisTaylorFinrankDeRhamQuotientCharacter.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorFinrankDeRhamQuotientCharacter.lean#L50) and `UpperTheory.Gal.Ord.dims` in [FinrankWPow.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RadicalStalks/FinrankWPow.lean#L125). Both take $f$ to be the action of an element of $O_F$ on the abelian variety of an object. The maps $\mathrm{ev}_j$ need not be compatible as $j$ varies.
