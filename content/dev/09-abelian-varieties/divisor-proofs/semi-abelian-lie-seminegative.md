---
id: semi-abelian-lie-seminegative
title: Subbundles of the Lie algebra of a semi-abelian scheme on a curve have degree at most zero
kind: theorem
decl: GlobalTheory.Nef.semiAbelianLieSeminegative
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiAbelianLieSeminegativeBis
covers: 454
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `SemiAbelianLieSeminegative` over any field of characteristic $0$. It reduces the statement to an algebraically closed field by base change. The renaming [from the literature](/entry/semi-abelian-lie-seminegative-of-literature/) gives it to the volume estimate in [EveryCharacter from the literature](/step/every-character-of-literature/). The case of an algebraically closed field is [the next entry](/entry/lie-sheaf-semi-abelian-semi-neg-of-is-alg-closed/), and its proof [semiNeg_lie_of_isAlgClosed](/entry/semi-neg-lie-of-is-alg-closed/) has the real content.

## Statement

Let $k$ be a field of characteristic $0$, and let $C$ be a smooth projective geometrically connected curve over $k$. Call a sheaf of modules $F$ on $C$ *seminegative* (`SemiNeg k F`) if each vector bundle $W$ of rank $r$ with a monomorphism $W \to F$ has $\deg \det W \leq 0$. Here the degree of a line bundle $L$ is the Lean `interNum k O_C ![L]`, which by its definition is $\chi(\mathcal{O}_C) - \chi(L^{-1})$. On a curve this is $\deg L$ by Riemann-Roch.

**Theorem.** Let $G$ be a semi-abelian group scheme over $C$ (`IsSemiAbelian`: commutative, smooth, separated, quasi-compact, geometrically connected, and each geometric fibre is an extension of an abelian variety by a split torus). Then $\mathrm{Lie}\,G$, the dual of the conormal sheaf of the unit section, is seminegative.

## Proof

Let $\bar k$ be an algebraic closure of $k$.

1. `semiNegative_descends_fieldExtension_curve`, applied to $\bar k$, gives a curve $C'$ over $\bar k$ and a map $\pi \colon C' \to C$ such that, for each sheaf $F$ on $C$, if $\pi^* F$ is seminegative over $\bar k$, then $F$ is seminegative over $k$.
2. The base change $G' = G \times_C C'$ is semi-abelian (`IsSemiAbelian.pullback`). By [the algebraically closed case](/entry/lie-sheaf-semi-abelian-semi-neg-of-is-alg-closed/), $\mathrm{Lie}\,G'$ is seminegative.
3. `lieBaseIso` gives $\pi^* \mathrm{Lie}\,G \cong \mathrm{Lie}\,G'$. It needs $C$ integral, which `isIntegral_curve` gives from smoothness and geometric connectedness. `semiNeg_of_iso` moves seminegativity along this isomorphism.

Step 1 then gives the theorem.

## In the Lean code

The theorem is at [SemiAbelianLieSeminegativeBis.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianLieSeminegativeBis.lean#L22). The statement is at [InterNumDetNonposSplitTorus.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/InterNumDetNonposSplitTorus.lean#L23). `SemiNeg` is at [IsIsoFromNormalization.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsIsoFromNormalization.lean#L22), and `lieBaseIso` and `semiNeg_of_iso` are at [SemiAbelianLieSeminegativeOfNeron.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianLieSeminegativeOfNeron.lean#L32).

- The descent lemma holds for every field extension $k \to k'$. It does not ask for characteristic $0$. We have not read its proof, `SemiNegFieldChange.semiNeg_descends_baseChange`.
- In the statement, `IsSemiAbelian G` is an instance argument. In the algebraically closed case it is an explicit hypothesis. This is only a difference of form.
- We do not know a published source for the statement in this form.
