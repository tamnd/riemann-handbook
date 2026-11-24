---
title: The tensor product theorem
decls:
  - GroundTheory.Automorphic.AdelicGLn.nonempty_tensorDecomposition
  - GroundTheory.Automorphic.AutomorphicForm.nonempty_adelicDecomposition
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The tensor product theorem

An irreducible admissible representation of an adelic group is a restricted tensor product of local representations. This is the tensor product theorem of Flath. This section proves it for $\mathrm{GL}_n$ over a number field, first for the finite adeles and then for $(\mathfrak{g}, K_\infty) \times \mathrm{GL}_n(\mathbb{A}_f)$-modules. The local components are what the local theory of this chapter (Sections 1 to 4) applies to. The result is used in the proof of [Theorem](/entry/loc-iff/). For automorphic representations and their factorization, see [automorphic representations](/learn/automorphic-forms/#automorphic-representations).

### Restricted tensor products

Let $K$ be a number field. For a finite place $v$ let $K_v$ be the completion, $\mathcal{O}_v$ its ring of integers and $K_v^\circ = \mathrm{GL}_n(\mathcal{O}_v)$. The group $\mathrm{GL}_n(\mathbb{A}_f)$ is the restricted product of the $\mathrm{GL}_n(K_v)$ with respect to the $K_v^\circ$. A representation $\sigma$ of $\mathrm{GL}_n(K_v)$ on $W$ is *smooth* if each vector has an open stabilizer, and *admissible* if it is smooth and the fixed vectors $W^U$ of each open compact subgroup $U$ form a finite-dimensional space. See [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups).

**Definition 4.9.1 (Restricted tensor product).** Let $(\pi_v, W_v)$ be representations of $\mathrm{GL}_n(K_v)$ for all finite $v$, and let $\xi_v \in W_v$ be vectors such that, for all but finitely many $v$, $\xi_v$ is nonzero and fixed by $K_v^\circ$. The *restricted tensor product* $\bigotimes'_v (\pi_v, \xi_v)$ is the span of the pure tensors $\bigotimes_v x_v$ with $x_v = \xi_v$ for all but finitely many $v$. The group $\mathrm{GL}_n(\mathbb{A}_f)$ acts place by place.

The action is defined because an element $g$ of the restricted product has $g_v \in K_v^\circ$ for almost all $v$, and $g_v$ fixes $\xi_v$ at those $v$.

**Definition 4.9.2 (Tensor decomposition).** A *tensor decomposition* of a representation $\rho$ of $\mathrm{GL}_n(\mathbb{A}_f)$ is a family $(\pi_v, W_v, \xi_v)$ as above, with each $\pi_v$ admissible and irreducible, together with an isomorphism of $\rho$ with $\bigotimes'_v(\pi_v, \xi_v)$.

### The finite adeles

The key local input is the following.

**Lemma 4.9.3 (Spherical vectors).** Let $\sigma$ be a smooth irreducible representation of $\mathrm{GL}_n(K_v)$ with a nonzero $K_v^\circ$-fixed vector. Then the space of $K_v^\circ$-fixed vectors has dimension $1$.

Lean: `GroundTheory.Automorphic.Spherical.finrank_fixedVectors_eq_one`.

*Proof.* The spherical Hecke algebra acts on the fixed vectors, and by irreducibility it acts through a character, given by a Satake parameter of $\sigma$. A second fixed vector would give a second spherical function with the same Hecke eigenvalues, so it is proportional to the first. See [unramified representations](/learn/representations/#unramified-representations). $\square$

So in every case the space of $K_v^\circ$-fixed vectors of a smooth irreducible representation has dimension at most $1$.

**Theorem 4.9.4 (Tensor product theorem, finite adeles).** Let $\rho$ be an admissible irreducible representation of $\mathrm{GL}_n(\mathbb{A}_f)$ on a complex vector space. Then $\rho$ has a tensor decomposition.

Lean: `GroundTheory.Automorphic.AdelicGLn.nonempty_tensorDecomposition`.

*Proof.* There is a group isomorphism of $\mathrm{GL}_n(\mathbb{A}_f)$ with the restricted product of the groups $\mathrm{GL}_n(K_v)$. Composition with it keeps $\rho$ admissible and irreducible. We apply the abstract tensor product theorem for restricted products: if $\rho$ is an admissible irreducible representation of a restricted product of groups $G_v$ with respect to open compact subgroups $K_v^\circ$, and if for almost all $v$ each smooth irreducible representation of $G_v$ has at most a one-dimensional space of $K_v^\circ$-fixed vectors, then $\rho$ is a restricted tensor product of admissible irreducible representations. The hypothesis holds at every $v$ by the lemma. Composing back with the isomorphism gives the tensor decomposition. $\square$

The abstract theorem is proved as in Flath. For a finite set $T$ of places and $U$ small, $\rho^U$ is a finite-dimensional irreducible module for the tensor product of the Hecke algebras at $T$; such a module is a tensor product of irreducible modules. The one-dimensional spaces at the places outside $T$ make these finite tensor products compatible as $T$ grows.

### The adelic group

Let $\mathfrak{g}$ be the complexified Lie algebra of $\mathrm{GL}_n(K \otimes \mathbb{R})$ and $K_\infty$ a maximal compact subgroup. A $(\mathfrak{g}, K_\infty) \times \mathrm{GL}_n(\mathbb{A}_f)$-module is a complex vector space with compatible actions of $\mathfrak{g}$, $K_\infty$ and $\mathrm{GL}_n(\mathbb{A}_f)$; the space of $K$-finite smooth automorphic forms is the main example ([automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups)).

**Theorem 4.9.5 (Tensor product theorem).** Let $M$ be an irreducible admissible $(\mathfrak{g}, K_\infty) \times \mathrm{GL}_n(\mathbb{A}_f)$-module. Then there are:

1. an irreducible $K_\infty$-admissible $(\mathfrak{g}, K_\infty)$-module $\pi_\infty$ and an irreducible admissible representation $\pi_f$ of $\mathrm{GL}_n(\mathbb{A}_f)$, with an isomorphism $M \cong \pi_\infty \otimes \pi_f$;
2. a tensor decomposition of $\pi_f$.

Lean: `GroundTheory.Automorphic.AutomorphicForm.nonempty_adelicDecomposition`.

*Proof.* An irreducible admissible module for a product of this form is the tensor product of an irreducible module of each factor: the space of $K_\infty$-types of a fixed type and $U$-fixed vectors is finite-dimensional and irreducible under the two Hecke algebras, so it splits, and these pieces fit together. This gives part 1. Part 2 is the tensor product theorem for the finite adeles applied to $\pi_f$. $\square$

The factors are unique up to isomorphism. If $M \cong \pi_\infty \otimes \pi_f \cong \pi'_\infty \otimes \pi'_f$, then $\pi_\infty \cong \pi'_\infty$, and the local components $\pi_v$ and $\pi'_v$ of the two tensor decompositions are isomorphic for each finite $v$. The same theorem holds for a cuspidal automorphic representation, since its space is an irreducible admissible module of this kind.

**Remark 4.9.6 (Formalization).** The splitting of part 1 is a separate theorem, `GKLModule.nonempty_decomposition` ([GKMain.lean](lean:GroundTheory/AutomorphicForms/TensorProductTheorem/GKMain.lean#L88)); we have not unfolded its proof, and the sketch above follows the classical argument. The abstract restricted product theorem is `RestrictedTensor.exists_equiv_restrictedTensorRep`, also not unfolded. The bound on fixed vectors is proved at every place, though only almost all places are needed ([GeneralLinearIntegers.lean](lean:GroundTheory/AutomorphicForms/TensorProductTheorem/GeneralLinearIntegers.lean#L184)). The spherical lemma is at [Satake.lean](lean:GroundTheory/AutomorphicForms/Satake.lean#L232); its proof goes through the existence of a Satake parameter. The uniqueness statements are `AdelicDecomposition.nonempty_equiv_arch` and `AdelicDecomposition.nonempty_equiv_local`.
