---
title: Classification over all schemes
decls:
  - GlobalTheory.SiegelNoeth.classify_noetherian
  - GlobalTheory.T.siegelFamily_classifies_noetherian
  - GlobalTheory.SiegFamAll.exists_classify_affine
  - GlobalTheory.SiegFamAll.existsUnique_classify
  - GlobalTheory.T.siegelFamily_existsUnique_classify_scheme
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Classification over all schemes

This section completes the classification. Let $F = (X, s, u)$ be a Siegel family of genus $h \geq 1$ and odd level $M \geq 3$. The previous section shows that $F$ classifies every principal Siegel object over a noetherian local ring. Here we pass to noetherian rings by spreading out from the local rings, to all rings by writing a ring as a union of subrings of finite type over $\mathbb{Z}$, and to all schemes by gluing on an affine open cover. The result is that $(X, u)$ is a fine moduli scheme for principal Siegel objects of genus $h$ and level $M$ over $B_M$. The method of limits is that of EGA IV$_3$, §8. For the moduli schemes of Volume 1 see [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures).

### Inputs

We use the following results. We state them as we use them. For a ring $R$ and $r \in R$ we write $R_r$ for the localization at the powers of $r$, and $R_{\mathfrak{p}}$ for the localization at a prime $\mathfrak{p}$.

1. (Locality.) Let $c$ be a principal Siegel object over $s' : S \to \operatorname{Spec} B_M$. Suppose that every point of $S$ has an open neighbourhood $V$ such that $F$ classifies a pullback of $c$ to $V$. Then $F$ classifies $c$.
2. (Spreading out from a prime.) Let $R$ be noetherian, $\beta : B_M \to R$, $c$ a principal Siegel object over $\operatorname{Spec} R$, and $\mathfrak{p}$ a prime of $R$. Suppose that $F$ classifies every Siegel object over $R_{\mathfrak{p}}$ with a map to $c$. Then there is $r \notin \mathfrak{p}$ such that $F$ classifies every Siegel object over $R_r$ with a map to $c$.
3. (Descent to finite type.) Let $R$ be a ring, $\beta : B_M \to R$, and $c$ a principal Siegel object over $\operatorname{Spec} R$. Then there are a subring $R_0 \subseteq R$ of finite type over $\mathbb{Z}$ that contains $\beta(B_M)$ and a principal Siegel object $c_0$ over $\operatorname{Spec} R_0$ with a map $c \to c_0$ over the inclusion.
4. (Uniqueness of classifying maps.) This is result 3 of the previous section: two maps $f, f' : S \to X$ over $B_M$ with maps $c \to u$ over $f$ and over $f'$ are equal.
5. (Pullbacks and composition.) Pullbacks of principal Siegel objects exist and are principal, and maps of Siegel objects compose. These are results 1 and 2 of the section on small extensions.

Result 1 holds because the classifying maps on the open sets agree on the overlaps by result 4, so they glue to a map $S \to X$, and the maps of Siegel objects glue with them. Result 2 uses that $X$ is locally of finite presentation over $B_M$, so that a map from $\operatorname{Spec} R_{\mathfrak{p}} = \varprojlim_{r \notin \mathfrak{p}} \operatorname{Spec} R_r$ to $X$ comes from some $\operatorname{Spec} R_r$ (EGA IV$_3$, Théorème 8.8.2), and the same for the abelian scheme, the line bundle and the level structure. Result 3 is the same argument for the filtered union of the subrings of finite type of $R$.

### Noetherian rings and all rings

**Theorem 8.6.1 (Classification over noetherian rings).** Let $R$ be a [[noetherian|0670T59HGE]] ring with a map $\beta : B_M \to R$. Then $F$ classifies every principal Siegel object over $\operatorname{Spec} R$.

Lean: `GlobalTheory.SiegelNoeth.classify_noetherian` (also `GlobalTheory.T.siegelFamily_classifies_noetherian`).

*Proof.* Let $c$ be principal over $\operatorname{Spec} R$. We use result 1. Let $x = \mathfrak{p}$ be a point of $\operatorname{Spec} R$. The ring $R_{\mathfrak{p}}$ is a noetherian local ring. Every Siegel object $c'$ over $R_{\mathfrak{p}}$ with a map $c' \to c$ is principal by result 5, so the [theorem on noetherian local rings](/entry/exists-point-of-principal/) shows that $F$ classifies $c'$. Result 2 gives $r \notin \mathfrak{p}$ such that $F$ classifies every Siegel object over $R_r$ with a map to $c$. Let $c_V$ be a pullback of $c$ to $\operatorname{Spec} R_r$, which exists by result 5. Then $F$ classifies $c_V$. The map $\operatorname{Spec} R_r \to \operatorname{Spec} R$ is an open immersion with image the basic open set $D(r)$, and $x \in D(r)$ since $r \notin \mathfrak{p}$. So the hypothesis of result 1 holds, and $F$ classifies $c$. $\square$

**Lemma 8.6.2 (Classification over affine schemes).** Let $R$ be a ring and $t : \operatorname{Spec} R \to \operatorname{Spec} B_M$. Then $F$ classifies every principal Siegel object over $t$.

Lean: `GlobalTheory.SiegFamAll.exists_classify_affine`.

*Proof.* The map $t$ is $\operatorname{Spec} \beta$ for a ring map $\beta : B_M \to R$. Let $d$ be a principal Siegel object over $t$. Result 3 gives a subring $R_0 \subseteq R$ of finite type over $\mathbb{Z}$, a map $\beta_0 : B_M \to R_0$ with $\beta = \iota \beta_0$ for the inclusion $\iota : R_0 \to R$, and a principal Siegel object $c_0$ over $R_0$ with a map $d \to c_0$ over $\operatorname{Spec} \iota$. By the Hilbert basis theorem, $R_0$ is noetherian. The theorem above gives $f_0 : \operatorname{Spec} R_0 \to X$ over $B_M$ with a map $c_0 \to u$ over $f_0$. Let $f = f_0 \operatorname{Spec} \iota$. Then $s f = \operatorname{Spec}(\beta_0) \operatorname{Spec}(\iota) = \operatorname{Spec}(\iota \beta_0) = t$, and the composite of $d \to c_0$ and $c_0 \to u$ is a map $d \to u$ over $f$. $\square$

### All schemes

**Theorem 8.6.3 (Siegel families are fine moduli schemes).** Let $h \geq 1$, let $M \geq 3$ be odd, and let $F = (X, s, u)$ be a Siegel family of genus $h$ and level $M$. Let $S$ be a scheme with a map $s' : S \to \operatorname{Spec} B_M$, and let $c$ be a principal Siegel object over $s'$. Then there is a unique map $f : S \to X$ with $s f = s'$ such that there is a map $c \to u$ over $f$.

Lean: `GlobalTheory.SiegFamAll.existsUnique_classify` (also `GlobalTheory.T.siegelFamily_existsUnique_classify_scheme`).

*Proof.* Existence. We use result 1. Let $x \in S$ and let $j : \operatorname{Spec} A \to S$ be the open immersion of an affine open of a fixed affine open cover that contains $x$. Result 5 gives a pullback $c_V$ of $c$ along $j$, over $s' j$, and $c_V$ is principal. The lemma on affine schemes shows that $F$ classifies $c_V$. So result 1 gives $f$. Uniqueness follows from result 4. $\square$

In other words, the functor that sends a scheme $S$ over $B_M$ to the set of isomorphism classes of principal Siegel objects over $S$ is represented by $X$, with universal object $u$. The uniqueness of the classifying map holds without the hypothesis that $c$ is principal, since result 4 does not use it; only the existence needs it.

The two properties in the definition of a Siegel family are much weaker than this theorem. Property 1 asks for classification only over reduced schemes in which the characteristic $0$ points are dense, and property 2 asks for uniqueness only over local rings. The previous sections lift these two properties to all schemes. The smoothness of $s$ enters in the small extension theorem.

**Remark 8.6.4 (Formalization).** The descent to finite type (result 3) does not use the hypothesis $h \geq 1$, which appears only in the other results: [SiegelFamilyExistsUniqueClassifyScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyExistsUniqueClassifyScheme.lean#L18). The open cover is the standard affine open cover of $S$ chosen in Mathlib, and uniqueness is one call to result 4: [SiegelFamilyExistsUniqueClassifyScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyExistsUniqueClassifyScheme.lean#L28). The noetherian case defines two helpers on $\operatorname{Spec}$ of compositions and identities that the file on complete local rings repeats: [SiegelFamilyClassifiesNoetherian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherian.lean#L16). The open immersion $\operatorname{Spec} R_r \to \operatorname{Spec} R$ and its image $D(r)$ come from Mathlib: [SiegelFamilyClassifiesNoetherian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherian.lean#L24). We read the statements of results 1 to 5, not their proofs; the explanations of results 1 to 3 above are ours.
