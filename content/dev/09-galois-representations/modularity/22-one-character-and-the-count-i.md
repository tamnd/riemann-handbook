---
title: One character and the count I
decls:
  - oneChar_unramU
  - UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy
  - UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy
status: drafted
drafted_by: writer@claude-opus-5-5
---
## One character and the count I

This section proves the count I of Step 4 of section 1. The count I is different in form from the other counts: it bounds a sum over all primes $l$ in case I. Its core is a bound for one character. Let $K$ be an imaginary CM field of degree two and $\sigma \in G_K$. If no admissible three-dimensional representation of $G_K$ has the trace $t = \Psi(\sigma) + 1 + \Psi(\sigma)^{-1}$ of the reducible point at $\sigma$, then the length of case I for $\psi$ is finite and bounded by the valuations of the trace differences at $\sigma$. A theorem of the literature on the number of such representations then turns the bounds for one character into the count I. The proof of the one character bound follows the main count in rank four of section 17, with a universal deformation ring of rank three in place of the symplectic family.

We keep the notation of case I. Let $N \ge 1$, $e \ge 1$, $\psi$ a Dirichlet character modulo $N$ with values in $\mathcal{O}$, and $\Psi = \chi_{\mathrm{cyc}}^{e} \psi$. Let $K$ be a CM field with $[K : \mathbb{Q}] = 2$ and quadratic character $\eta$. A good datum for $(K, l, e, \psi)$ is a set of conditions on $l$ (among them that $l$ is odd), on $\psi$ and on $K$ that put $\psi$ in case I. We write $V_{\mathrm{len}}$ for the length of case I, with value $\infty$ when the module is not of finite length, and $V_n$ for the normalized length.

**Definition 8.22.1 (Admissible representation of case I).** Let $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$. A continuous $\rho \colon G_K \to \mathrm{GL}_3(\overline{\mathbb{Q}}_l)$ is admissible for $(\iota, e, N)$ if it is either a three-dimensional unitary representation that is automorphic through $\iota$, of weight given by $e$ and level dividing $N$, or the sum of a character and a two-dimensional automorphic representation of conductor dividing $N |d_K|$, where $d_K$ is the discriminant of $K$.

The two kinds are the two shapes that a point of the deformation ring of the reducible point can take: an irreducible point (type I) or a point that contains a two-dimensional piece (type II).

**Theorem 8.22.2 (One character bound).** Assume the cohomology inputs, the lemmas M, M' and P, Kato's vanishing for two twists, rigidity in the first and in the second case, admissibility of points of type I, and the automorphy of unramified representations. Let $K$, $l$, $e$, $\psi$ be as above with a good datum, $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$, $\sigma \in G_K$ and

$$t = \Psi(\sigma) + 1 + \Psi(\sigma)^{-1}.$$

Suppose that no admissible $\rho$ has $\operatorname{tr} \rho(\sigma) = t$. Then $V_{\mathrm{len}}$ is finite, and there is a finite set $X$ of admissible representations, pairwise non-isomorphic, with

$$V_n \le 2 \sum_{\rho \in X} v_l\bigl(\operatorname{tr} \rho(\sigma) - t\bigr).$$

Lean: `UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy` (also `oneChar_unramU`, the same statement for $\mathcal{O}$ unramified over $\mathbb{Z}_l$).

*Proof.* We first reduce to the case where $\mathcal{O}$ is unramified over $\mathbb{Z}_l$. The lengths $V_{\mathrm{len}}$ and $V_n$ do not depend on the coefficient ring, so we may replace $\mathcal{O}$ by the ring generated over $\mathbb{Z}_l$ by the values of $\psi$, which is unramified because the order of $\psi$ is prime to $l$ in case I.

Now let $\mathcal{O}$ be unramified. The good datum gives a deformation datum $D$ over $K$, with characters $\eta$ and $\Psi$ and a complex conjugation. The automorphy of unramified representations gives a marked element $g_1$, finiteness at the end, and the automorphy of the points of type I and of the two-dimensional pieces of points of type II. The cohomology inputs give local conditions, a universal ring $S$ of rank three with mark $g_1$, and, with the lemma P, a model $M$ of $D$. Each point $f$ of $S$ is a representation of $G_{\mathbb{Q}}$ with a multiplier for $\eta$, and its restriction $\rho_f$ to $G_K$ is three-dimensional. Since $\eta(\sigma) = 1$, the trace of the residual point at $\sigma$ is $t$, so the trace difference at $\sigma$ is

$$\operatorname{tr} \rho_f(\sigma) - t.$$

Each point $f$ with the two-point condition is of type I or of type II. A point of type I is admissible by the admissibility of points of type I and the automorphy of type I points. A point of type II is admissible by the automorphy of its two-dimensional piece and the modular extensions of type II. So by hypothesis no trace difference vanishes. The upper bound for models, with the lemma M, finiteness at the end and the point hypothesis (which comes from Kato's vanishing for two twists and the two rigidity statements), gives a finite set $T$ of points and the bound of the length of $M$ by twice the sum of the valuations of the trace differences over $T$. The lemma M' compares $V_{\mathrm{len}}$ with the length of $M$. Two points of $T$ with isomorphic restrictions to $G_K$ are equal, by the shape of two-point representations, so $X = \{\rho_f : f \in T\}$ has the required property. Since the length is monotone, the bound for $M$ gives the bound for $V_n$. $\square$

The proof is the same as that of the [Theorem 8.17.7](/entry/main-big/) in rank four: a finite set of points at which the trace differences do not vanish, and a model whose length is bounded by their valuations. The difference is in the input. In rank four the nonvanishing comes from a Frobenius element at a small prime. Here it is a hypothesis on $\sigma$, and the count I below chooses $\sigma$.

**Theorem 8.22.3 (Count I).** Assume the extended hypotheses, Lemma K, Kato's vanishing for two twists and the automorphy of unramified representations. Then the count I holds.

Lean: `UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy`.

*Proof.* The extended hypotheses and Lemma K give the cohomology inputs. The lemmas M, M' and P are proved in the algebraic part of the chapter. Rigidity in the first case comes from the cohomology inputs, the adjoint lifting theorem of section 16 and the end statement for unlinked points, which comes from the [Theorem 8.20.7](/entry/linked-unl-e-alt/) of section 20. Rigidity in the second case comes from the cohomology inputs and the adjoint lifting theorem. Admissibility of points of type I comes from the cohomology inputs and the same end statement. So the [Theorem 8.22.2](/entry/one-char-u-of-kato-two-w-rig-adm-i-automorphy/) on one character applies. The classical part of the extended hypotheses gives a bound on the number of admissible three-dimensional unitary representations of given weight and level. With this bound, the one character bound gives a property of the primes of case I: for each $\chi$ there is $C$ such that for each $\psi$ the number of primes $l$ in case I where an admissible representation has trace $t$ is controlled, and the remaining primes satisfy the one character bound. This is the corollary of the counting statement, and it gives the count I. $\square$

**Remark 8.22.4 (Formalization).** The unramified case is the private theorem `oneChar_unramU` in the root namespace ([FOneCharU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean#L19)), and a second private `oneChar_unramU` is in [OneCharU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/WeightInfinitesimalCharacters/OneCharU.lean#L12). The private helpers `exists_unram` and `gd_chHom` also appear twice under the same names. The one character statement is `OneCharU` ([AdmissibleUnitaryThreePoint.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/WeightInfinitesimalCharacters/AdmissibleUnitaryThreePoint.lean#L116)). We have not unfolded the admissibility predicates `Adm3U_s` and `Adm2A`, the good datum `GD`, the lengths `Vlen` and `Vn`, the model, or the statements `propGK` and `corGK` that turn one character bounds into the count; our description of the last step reads their names and inputs. The count I computes `unlEnd3E (linkedUnlE_alt hH)` at [LinkedUnlE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L51), as the count V does at line 57.
