---
id: exists-finite-type-scheme-representing-polarized-homs
title: Homomorphisms that respect polarizations form a scheme of finite type, over an affine noetherian base
kind: theorem
decl: GlobalTheory.T.exists_finiteType_scheme_representing_polarizedHoms
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteTypeSchemeRepresentingPolarizedHomsStatement
covers: 402
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the representability over an affine base](/entry/exists-hom-fix-rep-finite-type/). It is a second name of that theorem, with the same statement. [The representability over a locally noetherian base](/entry/hom-fix-finite-type/) applies it to each affine open $\operatorname{Spec}\Gamma(S, U)$ of $S$ and glues the results.

## Statement

Let $R$ be a noetherian ring and $S = \operatorname{Spec} R$. Let $A$ and $B$ be abelian schemes over $S$. Let $L$ on $A$ and $M$ on $B$ be line bundles, each given by an open cover and a cocycle of transition units, each rigidified along the unit section, and each relatively ample in the sense of the Lean predicate `Out.RelAmple`.

**Theorem.** There is a scheme $H$ with a map $\pi \colon H \to S$ that is quasi-compact, separated and locally of finite type, and that represents the functor
$$T \mapsto \{\Phi \colon A_T \to B_T \text{ a homomorphism} : \Phi^* M_T \cong L_T\}$$
on schemes $T$ over $S$.

The objects in this statement are defined in [the entry of the affine theorem](/entry/exists-hom-fix-rep-finite-type/).

## Proof

The proof is `exact GlobalTheory.HomFixAff.exists_homFixRep_finiteType`. The real content is in that theorem and below it.

## In the Lean code

The theorem is in [ExistsFiniteTypeSchemeRepresentingPolarizedHomsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteTypeSchemeRepresentingPolarizedHomsStatement.lean#L11). The proof is a `first | exact … | …` combinator that closes the goal with the theorem of the same statement. The conclusion is `∃ R : HomFixRep A B L M, QuasiCompact R.π ∧ IsSeparated R.π ∧ LocallyOfFiniteType R.π`.

The hypotheses `[IsCommMonObj A]` and `[IsCommMonObj B]` repeat the field `comm` of `IsAbelianScheme`.
