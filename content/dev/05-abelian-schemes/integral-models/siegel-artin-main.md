---
id: siegel-artin-main
title: Principal Siegel objects over local Artinian rings are classified
kind: theorem
decl: GlobalTheory.SiegelArtin.main
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelPointLiftsToArtinian
covers: 373
status: drafted
drafted_by: writer@claude
---
This theorem proves that a family of Siegel objects with a few local properties classifies every principal object over a local Artinian base. The proof is an induction on length, with [the lift over a small extension](/entry/classified-of-small/) as the step. [Its statement form](/entry/siegel-point-lifts-to-artinian/) repeats it for [the classification over complete noetherian local rings](/entry/classified-of-complete/).

## Statement

Let $n \geq 3$ be odd and $B_n = \mathbb{Z}[\zeta_n, 1/n] \subset \mathbb{C}$. Siegel objects of genus $g$ and level $n$, and principal ones, are as in [the representability of Siegel moduli](/entry/sd-rep-of-coprime/). An object $c$ over $S'$ *is the pullback of* an object $u$ over $S$ along $f \colon S' \to S$ if there is a map $A_c \to A_u$ over $f$ that makes $A_c$ the pullback group scheme, that carries the line bundle of $u$ on $A_u \times A_u$ to that of $c$ up to isomorphism, and that carries the level structure of $c$ to that of $u$.

A *family* of genus $g$ and level $n$ is a scheme $X$ with a map $s \colon X \to \operatorname{Spec} B_n$ and a principal Siegel object $u$ over $X$, such that:

- $s$ is smooth of relative dimension $g(g+1)/2$ and quasi-projective;
- each principal object over a reduced scheme $S$, whose points over the generic point of $\operatorname{Spec} B_n$ are dense, is the pullback of $u$ along some map $S \to X$ over $B_n$;
- for a local ring $R$, two maps $\operatorname{Spec} R \to X$ over $B_n$ along which the same object is the pullback of $u$ are equal.

**Theorem.** Let $g \geq 1$, $n \geq 3$ odd, and $(X, s, u)$ a family of genus $g$ and level $n$. Let $C$ be a local Artinian ring, $\beta \colon B_n \to C$ a ring map, and $c$ a principal Siegel object over $\operatorname{Spec} C$. Then there is $f \colon \operatorname{Spec} C \to X$ with $s \circ f = \operatorname{Spec}\beta$ such that $c$ is the pullback of $u$ along $f$.

## Proof

Strong induction on the length $N$ of $C$ as a $C$-module. This length is finite since $C$ is Artinian.

1. If the maximal ideal $\mathfrak{m}$ is $0$, then $C$ is a field. `GlobalTheory.T.siegel_family_classifies_principal_any_field` gives $f$.
2. If $\mathfrak{m} \neq 0$, `exists_socle` gives $e \neq 0$ in $\mathfrak{m}$ with $\mathfrak{m} e = 0$. Take $k$ least with $\mathfrak{m}^k = 0$; then $k \geq 2$, and $e$ is any nonzero element of $\mathfrak{m}^{k-1}$.
3. The ideal $(e)$ is nonzero, so $C/(e)$ has length less than $N$.
4. [The lift over a small extension](/entry/exists-sieg-pb-lift-of-quotient-lift/) reduces the claim for $c$ to this: each pullback $c_0$ of $c$ to $C/(e)$ is classified by a map $\operatorname{Spec} C/(e) \to X$.
5. `GlobalTheory.siegPre_pullback` says that a pullback of a principal object is principal. So $c_0$ is principal, and the induction hypothesis for $C/(e)$ gives its map.

The rest is bookkeeping on lengths.

## In the Lean code

The theorem is in [SiegelPointLiftsToArtinian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelPointLiftsToArtinian.lean#L47). The family is the structure `SFam` in [IsSeparatedOfIsQProjOver.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSeparatedOfIsQProjOver.lean#L18), with the fields `smooth`, `qproj`, `univ`, `princ`, `rep` and `inj`. "Is the pullback" is `SiegPB` in [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L50); we have not unfolded `IsGrpPullback` inside it. `exists_socle` is in the same file, proved in full. `GlobalTheory.siegPre_pullback` is in [SiegelObjectPullbackExistsAndPrincipal.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/SiegelObjectPullbackExistsAndPrincipal.lean#L106). `GlobalTheory.T.siegel_family_classifies_principal_any_field` is a statement form whose proof we have not opened.

The step lemma does not need $e \neq 0$; the induction needs it only to make the length drop.
