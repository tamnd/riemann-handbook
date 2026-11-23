---
title: The reduced case by normalization and pinching
decls:
  - GlobalTheory.T.hasProperSmoothDualRepresentative_noetherianInduction
  - GlobalTheory.DualConStep.step
  - GlobalTheory.T.hasRepresentingScheme_pinchedBase
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The reduced case by normalization and pinching

Let $R$ be a reduced ring of finite type over $\mathbb{Z}$ and $A$ an abelian scheme over $\mathrm{Spec}\, R$. This section constructs a good representative of the dual of $A$ over $\mathrm{Spec}\, R$, under two assumptions: some affine open set of $A$ meets every fibre, and representatives exist over $\mathrm{Spec}\, R/J$ for each ideal $J \neq 0$ (Theorem (Reduced case)). The idea is to replace $R$ by its normalization. Over a normal domain an abelian scheme with such an affine open set has a relatively ample line bundle, so the last section applies. The normalization is a finite product of normal domains, and $\mathrm{Spec}\, R$ is obtained from it and from $\mathrm{Spec}\, R/\mathfrak{c}$, where $\mathfrak{c}$ is the conductor, by pinching. The theorem is the main step of the noetherian induction in the next section.

**Definition 1.4.1 (Conductor).** Let $R \to R'$ be a homomorphism of rings. The *conductor* of $R'$ over $R$ is the ideal
$$\mathfrak{c} = \{x \in R : \text{for each } r \in R' \text{ there is } y \in R \text{ with } y = x r \text{ in } R'\}.$$

If $R \to R'$ is injective, $\mathfrak{c}$ is the largest ideal of $R$ that is also an ideal of $R'$. For $R = \mathbb{Z}[2i]$ and $R' = \mathbb{Z}[i]$ it is $2\mathbb{Z}[i]$. In general $\mathfrak{c} R' \subseteq \mathfrak{c}$, in this sense: for $x \in \mathfrak{c}$ and $r \in R'$ there is $y \in \mathfrak{c}$ with $y = x r$ in $R'$. Indeed, take $y$ with $y = x r$; for $r' \in R'$, an element $z \in R$ with $z = x (r r')$ in $R'$ shows that $y r' = z$ lies in the image of $R$.

**Theorem 1.4.2 (Pinching).** Let $R$ be a noetherian ring and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$. Let $R'$ be a finite $R$-algebra with $R \to R'$ injective, and let $\mathfrak{c}$ be an ideal of $R$ such that for each $x \in \mathfrak{c}$ and $r \in R'$ there is $y \in \mathfrak{c}$ with $y = x r$ in $R'$. Suppose that $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec}\, R')$ and $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/\mathfrak{c})$ hold. Then $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$ holds.

Lean: `GlobalTheory.T.hasRepresentingScheme_pinchedBase` (a second name of `GlobalTheory.Pinch.hasRep_pinched`).

The proof is in a later section, at [Theorem 1.4.2](/entry/has-rep-pinched/). Under its hypotheses $\mathfrak{c}$ is an ideal of $R'$ that lies in $R$, and $R$ is the fibre product of $R'$ and $R/\mathfrak{c}$ over $R'/\mathfrak{c}$. So $\mathrm{Spec}\, R$ is obtained from $\mathrm{Spec}\, R'$ by pinching $\mathrm{Spec}\, R'/\mathfrak{c}$ onto $\mathrm{Spec}\, R/\mathfrak{c}$, and the theorem says that representatives over the two pieces give one over $\mathrm{Spec}\, R$.

We also use four facts.

1. (Ample bundles over normal domains.) Let $D$ be a noetherian normal domain and $A$ an abelian scheme over $\mathrm{Spec}\, D$. Suppose that some affine open set $V$ of $A$ meets every fibre of $A \to \mathrm{Spec}\, D$. Then $A$ has a relatively ample line bundle.
2. (Normalization.) Let $R$ be a nonzero reduced ring of finite type over $\mathbb{Z}$. Then there are normal domains $D_1, \dots, D_n$, each a finite $R$-algebra, such that $R \to \prod_i D_i$ is injective, and an element $a \neq 0$ of $R$ with $a \prod_i D_i \subseteq R$.
3. (Products.) Let $D_1, \dots, D_n$ be $R$-algebras. If $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec}\, D_i)$ holds for each $i$, then $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec} \prod_i D_i)$ holds.
4. (Empty base.) If $S'$ is empty, then $\mathrm{Rep}^{\mathrm{af}}_g(A, S')$ holds.

Fact 2 comes from the normalization of $R$: a ring of finite type over $\mathbb{Z}$ is excellent, so its normalization is finite over it (A. Grothendieck, *Éléments de géométrie algébrique IV*, Part 2, Publ. Math. IHÉS 24, Scholie 7.8.3). For reduced $R$ the normalization is the product of the normalizations of $R/\mathfrak{p}$ over the minimal primes $\mathfrak{p}$. Fact 3 holds because $\mathrm{Spec} \prod_i D_i$ is the disjoint union of the $\mathrm{Spec}\, D_i$. Fact 4 holds with the empty representative.

**Theorem 1.4.3 (Reduced case).** Let $R$ be a reduced ring of finite type over $\mathbb{Z}$ and $A$ an abelian scheme over $\mathrm{Spec}\, R$ that is smooth of relative dimension $g$. Let $V$ be an affine open set of $A$ that meets every fibre of $A \to \mathrm{Spec}\, R$. Suppose that $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$ holds for each ideal $J \neq 0$ of $R$. Then $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$ holds.

Lean: `GlobalTheory.DualConStep.step` (also `GlobalTheory.T.hasProperSmoothDualRepresentative_noetherianInduction`, a second name).

*Proof.* The ring $R$ is noetherian, by the Hilbert basis theorem. If $R = 0$, then $\mathrm{Spec}\, R$ is empty, and fact 4 gives a representative. So let $R \neq 0$.

Step 1: one normal domain. Let $D$ be a noetherian normal domain with an $R$-algebra structure. We show $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec}\, D)$. Let $A_D = A \times_R D$. It is an abelian scheme over $D$, smooth of relative dimension $g$. The map $A_D \to A$ is affine, as a base change of the affine map $\mathrm{Spec}\, D \to \mathrm{Spec}\, R$, so the preimage $V_D$ of $V$ is an affine open set of $A_D$. It meets every fibre: for $s \in \mathrm{Spec}\, D$ with image $s_0 \in \mathrm{Spec}\, R$, choose $x \in V$ over $s_0$; some point of $A_D$ maps to $x$ and to $s$. By fact 1, $A_D$ has a relatively ample line bundle. By [Theorem 1.3.2](/entry/has-rep-af-of-rel-ample/) (Dual from an ample bundle), $\mathrm{Rep}^{\mathrm{af}}_g(A_D, \mathrm{Spec}\, D)$ holds. By Lemma (Change of base), part (a), $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec}\, D)$ holds.

Step 2: the normalization. Take $D_1, \dots, D_n$ and $a$ from fact 2, and put $R' = \prod_i D_i$. Each $D_i$ is finite over the noetherian ring $R$, so it is noetherian. Step 1 and fact 3 give $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec}\, R')$. The ring $R'$ is a finite $R$-algebra, as a finite product of finite $R$-algebras, and $R \to R'$ is injective.

Step 3: pinching. Let $\mathfrak{c}$ be the conductor of $R'$ over $R$. It contains $a$, so $\mathfrak{c} \neq 0$. By the hypothesis, $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/\mathfrak{c})$ holds. By the remark after the definition of the conductor, $\mathfrak{c}$ satisfies the condition of the pinching theorem. So the pinching theorem gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$. $\square$

**Remark 1.4.4 (Formalization).** Facts 1 to 4 are `GlobalTheory.T.exists_relAmple_of_affineOpen_meets_fibres`, `GlobalTheory.T.reduced_finiteType_int_exists_finite_prod_normalDomains_nonzero_conductor`, `GlobalTheory.T.hasProperSmoothDualRep_of_finite_product_algebras` and `GlobalTheory.T.hasProperSmoothDualRepresentativeFinAffine_of_isEmpty`; they are cited by their statements, and the sentences on why they hold are not read from proofs. Fact 2 asks that $D_i$ be a domain, integrally closed and finite over $R$; it does not say that $\prod_i D_i$ is the normalization. Fact 3 has no hypothesis on the $D_i$. Step 1 is `GlobalTheory.DualConStep.hasRepAF_factor`, the conductor is `GlobalTheory.DualConStep.conductor`, and the remark after its definition is `GlobalTheory.DualConStep.conductor_mul`. The two names `GlobalTheory.DualConStep.step` and `GlobalTheory.DualCon.Step.step` (the theorem of the next section) differ by one dot. The second name of this theorem ends in `noetherianInduction`, and the second name of the next one ends in `noetherian_induction`; this theorem is the reduced case, not the induction. The second names of this theorem and of the pinching theorem are closed by a `first` list under `set_option maxHeartbeats 1000000`.
