---
id: exists-classify-affine
title: A Siegel family classifies principal objects over affine schemes
kind: theorem
decl: GlobalTheory.SiegFamAll.exists_classify_affine
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyExistsUniqueClassifyScheme
covers: 547
status: drafted
drafted_by: writer@claude
---
This lemma proves that a Siegel family classifies each principal Siegel object over an affine scheme $\operatorname{Spec} R$, with no condition on $R$. It reduces to a noetherian ring and applies [the noetherian case](/entry/siegel-family-classifies-noetherian/). Its one user is [the classification over all schemes](/entry/exists-unique-classify/), which covers a scheme by affine opens, applies this lemma on each, glues, and adds uniqueness.

## Statement

Let $B_n = \mathbb{Z}[\zeta_n, 1/n] \subset \mathbb{C}$ with $\zeta_n = e^{2\pi i/n}$. Siegel objects $c = (A, P, \lambda)$ of genus $g$ and level $n$ over a scheme $S \to \operatorname{Spec} B_n$, and principal objects, are as in [the representability entry](/entry/sd-rep-of-coprime/). Write $c \cong f^*c'$ when $c$ is the pullback of $c'$ along $f$: there is a map $A \to A'$ over $f$ that makes $A$ the fibre product, carries $P$ to $P'$ and $\lambda$ to $\lambda'$.

A *Siegel family* of genus $g$ and level $n$ (the Lean structure `SFam`) is:

- a scheme $X$ with $s \colon X \to \operatorname{Spec} B_n$, smooth of relative dimension $g(g+1)/2$ and quasi-projective;
- a principal Siegel object $u$ over $X$;
- (*reduced case*) if $S$ is reduced and the points of $S$ over the generic point of $\operatorname{Spec} B_n$ are dense, then each principal $c$ over $S$ is $f^*u$ for some $f \colon S \to X$ over $B_n$;
- (*local injectivity*) if $R$ is a local ring and $x, y \colon \operatorname{Spec} R \to X$ have $sx = sy$ and $c \cong x^*u$, $c \cong y^*u$ for one $c$, then $x = y$.

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family. Let $R$ be a ring, $t \colon \operatorname{Spec} R \to \operatorname{Spec} B_n$, and $c$ a principal Siegel object over $t$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = t$ and $c \cong f^*u$.

## Proof

1. Write $t = \operatorname{Spec} \beta$ for a ring map $\beta \colon B_n \to R$ (`SiegelRingChange.exists_spMap`).
2. `principalSiegel_descends_finiteType_subring` gives a subring $R_0 \subset R$ of finite type over $\mathbb{Z}$ that contains $\beta(B_n)$, and a principal object $c_0$ over $R_0$ with $c \cong c_0 \otimes_{R_0} R$. We have not opened its proof.
3. $R_0$ is noetherian by the Hilbert basis theorem (`Algebra.FiniteType.isNoetherianRing`).
4. [The noetherian case](/entry/siegel-family-classifies-noetherian/) gives $f_0 \colon \operatorname{Spec} R_0 \to X$ over $B_n$ with $c_0 \cong f_0^*u$.
5. Let $f$ be $\operatorname{Spec} R \to \operatorname{Spec} R_0$ followed by $f_0$. Pullbacks compose (`TChart.AbLevel.siegPB_trans`), so $c \cong f^*u$. The base condition $sf = t$ is bookkeeping.

## In the Lean code

The lemma is in [SiegelFamilyExistsUniqueClassifyScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyExistsUniqueClassifyScheme.lean#L18). `SFam` is in [IsSeparatedOfIsQProjOver.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSeparatedOfIsQProjOver.lean#L18), `SiegPre`, `SiegPre.Principal` and `SiegPB` in [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L16), and $B_n$ is `cycAway n` in [SiegelToroidalIntegral.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/SiegelToroidalIntegral.lean#L16).

The lemmas it calls:

- `GlobalTheory.SiegelRingChange.exists_spMap`;
- `GlobalTheory.T.principalSiegel_descends_finiteType_subring`, a statement form;
- `GlobalTheory.T.siegelFamily_classifies_noetherian`;
- `GlobalTheory.TChart.AbLevel.siegPB_trans`, in [ExistsLevelAbelianLocusToroidalChart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLevelAbelianLocusToroidalChart.lean#L89).

The hypothesis $g \geq 1$ is only passed to the noetherian case. The conclusion has no uniqueness; the parent gets it from `siegelFamily_classifyingMap_unique`.
