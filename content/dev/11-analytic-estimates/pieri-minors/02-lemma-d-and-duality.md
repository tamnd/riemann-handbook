---
title: Lemma D for Weyl modules and its dual form
decls:
  - Formalism.CohomologicalDescent.LR.real_of_skeleton
  - Formalism.CohomologicalDescent.LR.real_of_pieri
  - Formalism.CohomologicalDescent.Down.hG
  - Formalism.CohomologicalDescent.LD.lastGradedOfGradedAlone
  - Formalism.CohomologicalDescent.LD.last_graded_of_graded_alone
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lemma D for Weyl modules and its dual form

This section proves Lemma D. Let $\nu = (w^p, \lambda_2)$ be a dominant weight of $\mathrm{GL}_{p+q}$ whose first $p$ entries are equal to $w$. If the dual Weyl module $\nabla(\lambda_2)$ of $\mathrm{GL}_q$ sits inside the Weyl module $\Delta(\lambda_2)$ after multiplication by $l^{e}$ in all weights of small depth, then $\nabla(\nu)$ sits inside $\Delta(\nu)$ after multiplication by $l^{e + v_l(D_n)}$ in the weights of depth $n$. The proof applies the [depth skeleton](/entry/depth-skeleton-third-form-holds/) of Section 1 to the rational Weyl module. A duality of Weyl modules, given by the cofactor matrix, then moves the result from the first block to the last block. The last block form is used in Section 3 to remove rows one at a time, and through it in the lattice inclusions of Section 4.

We use [polynomials on matrices](/learn/combinatorics/#polynomials-on-matrices), [minors and determinant identities](/learn/combinatorics/#minors-and-determinant-identities) and [highest weights and branching](/learn/representations/#highest-weights-and-branching).

**Definition 4.2.1 (Integral Weyl modules and the exponent of a weight).** Let $r \geq 1$ and let $\mathbb{Z}[x] = \mathbb{Z}[x_{ij} : 0 \leq i, j < r]$, with $\mathrm{GL}_r$ acting on rows. For a weight $\nu \in \mathbb{N}^r$, let $\nabla(\nu) \subseteq \mathbb{Z}[x]$ be the dual Weyl module of highest weight $\nu$ (spanned by products of leading minors in its rational form) and let $\Delta(\nu)$ be the Weyl module, the submodule generated from the highest weight vector by divided powers. For $\mu \in \mathbb{N}^r$, let $\nabla(\nu)_\mu$ be the part of $\nabla(\nu)$ that is homogeneous of row degree $\mu$. Let $l$ be a prime number and $e \in \mathbb{N}$. We write $\mathrm{Exp}_l(\nu, \mu) \leq e$ if for every $x \in \nabla(\nu)_\mu$ there is an integer $m$ prime to $l$ with $m\, l^e x \in \Delta(\nu)$.

So $\mathrm{Exp}_l(\nu, \mu) \leq e$ says that the $l$-part of the index of $\Delta(\nu)_\mu$ in $\nabla(\nu)_\mu$ is killed by $l^e$. For $r = 2$, $\nu = (w, y)$ and $\mu = (w - i, y + i)$, the module $\nabla(\nu)_\mu$ has rank one, and $c$ times its generator lies in $\Delta(\nu)$ exactly when $\binom{w - y}{i}$ divides $c$.

**Definition 4.2.2 (Block weights and depth).** For $p, q, w \in \mathbb{N}$ and $\kappa \in \mathbb{N}^q$, put $(w^p, \kappa) = (w, \dots, w, \kappa(0), \dots, \kappa(q-1)) \in \mathbb{N}^{p+q}$ and $(\kappa, w^p) \in \mathbb{N}^{q+p}$. A weight $\mu \in \mathbb{N}^{p+q}$ has *depth* $i$ if $\sum_{a < p} \mu(a) + i = p w$; a weight $\mu \in \mathbb{N}^{q+p}$ has *last depth* $i$ if the sum of its last $p$ entries is $p w + i$. For $\xi \in \mathbb{Z}^r$ and $\lambda, \mu \in \mathbb{N}^r$, put $d_\xi(\lambda, \mu) = \sum_a \xi(a)(\lambda(a) - \mu(a))$.

The depth counts how many boxes move from the first block to the second. For a non-increasing $\xi$ the number $d_\xi(\lambda, \mu)$ measures how far $\mu$ lies below $\lambda$ in the dominance order, weighted by $\xi$.

**Theorem 4.2.3 (Lemma D, graded form).** Let $l$ be a prime number, $p, q, w \in \mathbb{N}$, $\lambda_2 \in \mathbb{N}^q$ non-increasing with $\lambda_2(b) \leq w$ for all $b$, and $\xi \in \mathbb{Z}^{p+q}$ non-increasing. Let $i' \in \mathbb{Z}$ and $e \in \mathbb{N}$, and assume that $\mathrm{Exp}_l(\lambda_2, \mu_2) \leq e$ for every $\mu_2 \in \mathbb{N}^q$ with $d_\xi((w^p, \lambda_2), (w^p, \mu_2)) \leq i'$. Then for every $i \in \mathbb{N}$ and every $\mu \in \mathbb{N}^{p+q}$ of depth $i$ with $d_\xi((w^p, \lambda_2), \mu) \leq i'$,
$$\mathrm{Exp}_l\bigl((w^p, \lambda_2), \mu\bigr) \leq e + v_l\bigl(D_n(p, w, i, \lambda_2)\bigr).$$

The proof needs two facts about the rational module $V = \nabla_{\mathbb{Q}}((w^p, \lambda_2))$. The operators $E_{ab}$ are the polarization operators $\sum_s x_{as}\, \partial / \partial x_{bs}$, and $W \subseteq V$ is the space of vectors killed by the $E_{\alpha b}$ ($\alpha < p \leq b$) on which $E_{\alpha \beta}$ acts by $\delta_{\alpha\beta} w$. This is a depth setting in the sense of [Section 4.1.8](/entry/depth-skeleton-third-form-holds/), with the Fock pairing divided by the square norm of the highest weight vector as the form $B$.

**Proposition 4.2.4 (Pieri decomposition over $\mathbb{Q}$).** For all $p, q, w$, every non-increasing $\lambda_2 \in \mathbb{N}^q$ with $\lambda_2 \leq w$, and every $n$, the path spaces of $T_n(W)$ for the shapes $\tau \geq \lambda_2$ span $T_n(W)$.

Lean: `Formalism.CohomologicalDescent.LPR.pieri_real_form`.

*Proof.* The space $W$ is finite dimensional. It carries a positive definite form for which $E_{b b'}$ is adjoint to $E_{b' b}$, and it is generated by the highest weight vector as a module over $\mathfrak{gl}_q$. These are the hypotheses of the [Pieri rule](/learn/combinatorics/#the-pieri-and-littlewood-richardson-rules) for $\mathfrak{gl}_q$ (I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I, §5): tensoring an irreducible module of highest weight $\kappa$ with the standard representation gives the irreducible modules of highest weights $\kappa + e_b$ that are non-increasing. Applied $n$ times, starting from $\lambda_2$, this splits $T_n(W)$ into the joint eigenspaces of the partial Casimir operators along paths of shapes, which are the path spaces. $\square$

**Proposition 4.2.5 (Column vanishing).** Under the same hypotheses, if some column of $\tau/\lambda_2$ has more than $p$ boxes, then the symmetrization map kills the path space of $\tau$ in $T_n(W)$.

Lean: `Formalism.CohomologicalDescent.ColumnMinorsFromPieri.columns_real_of_pieri_real`.

*Proof.* This is deduced from the Pieri decomposition by a combinatorial argument on paths. It exchanges two steps of a path that add boxes in the same column, which acts on tensors by a transposition of factors, and it uses that the symmetrization is invariant under such transpositions. We do not reproduce the combinatorics. $\square$

**Theorem 4.2.6 (Lemma D from the skeleton).** Assume the Pieri decomposition and the column vanishing for all $p, q, w, \lambda_2, n$. Then Lemma D in its graded form holds.

Lean: `Formalism.CohomologicalDescent.LR.real_of_skeleton` (also `Formalism.CohomologicalDescent.LR.real_of_pieri`, the same result with the two identities on coefficients of words supplied).

*Proof.* Fix the data of Lemma D and an element $x \in \nabla((w^p, \lambda_2))_\mu$. Take $O = \mathbb{Z}_{(l)}$, $K = \mathbb{Q}$ and the depth setting $(V, W, B)$ above. Let $L \subseteq W$ be the $\mathbb{Z}_{(l)}$-span of the vectors obtained from the highest weight vector by words of divided powers $E_{b b'}^{(k)}$ with $b, b'$ in the second block; it is stable under the $E_{b b'}$. We check the third inputs of the skeleton. The form is contragredient and nondegenerate, and $V$ is generated by $W$. The Pieri and column conditions are the hypotheses. Put $\xi^\sharp(\kappa) = \sum_a \xi(a) \kappa(a)$; since $\xi$ is non-increasing, $\xi^\sharp(e_\alpha - e_b) \geq 0$ for $\alpha$ in the first block and $b$ in the second. For item 7, the coefficient of a polynomial of column weight $\nu$ on a lower triangular monomial is the value at the identity matrix of a word of polarization operators applied to it (the identity on coefficients of words). This reduces item 7 to the hypothesis $\mathrm{Exp}_l(\lambda_2, \mu_2) \leq e$ for the weights $\mu_2$ of the second block with $d_\xi \leq i'$. The image of $x$ lies in $\Delta(L)^\vee$, has weight $\mu$, and satisfies $\sum_{a < p} \mu(a) + i = p w$ and $\xi^\sharp(\lambda - \mu) = d_\xi((w^p, \lambda_2), \mu) \leq i'$. The [third form of the skeleton](/entry/depth-skeleton-third-form-holds/) gives $l^N x \in \Delta(L)$ with $N = e + v_l(D_n(p, w, i, \lambda_2))$. Finally $\Delta(L)$ lies in the $\mathbb{Z}_{(l)}$-span of $\Delta((w^p, \lambda_2))$, which gives an integer $m$ prime to $l$ with $m\, l^N x \in \Delta((w^p, \lambda_2))$. $\square$

**Theorem 4.2.7 (Lemma D).** Lemma D in its graded form holds for all $l, p, q, w, \lambda_2, \xi$ as in its statement.

Lean: `Formalism.CohomologicalDescent.Down.hG`.

*Proof.* This is [Lemma D from the skeleton](/entry/real-of-pieri/) applied to the Pieri decomposition over $\mathbb{Q}$ and to the column vanishing, which follows from it. $\square$

For $\xi = 0$ the condition on $d_\xi$ is empty, and Lemma D says: if $\mathrm{Exp}_l(\lambda_2, \mu_2) \leq e$ for all $\mu_2$, then $\mathrm{Exp}_l((w^p, \lambda_2), \mu) \leq e + v_l(D_n(p, w, i, \lambda_2))$ for all $\mu$ of depth $i$.

**Definition 4.2.8 (Dual weight).** For $M \in \mathbb{N}$ and $\kappa \in \mathbb{N}^r$, put $\kappa^{*}(a) = M - \kappa(r - 1 - a)$. If $\kappa \leq M$, then $(\kappa^{*})^{*} = \kappa$, $\kappa^* \leq M$, and $\kappa^*$ is non-increasing when $\kappa$ is.

The dual weight is the highest weight of $\nabla(\kappa)^\vee \otimes \det^M$. The cofactor map $\mathrm{cof}$ sends $x_{ij}$ to the entry $(r - 1 - j, r - 1 - i)$ of the adjugate of the generic matrix $X$. It realizes this duality on polynomials.

**Proposition 4.2.9 (Exponent duality).** Let $l$ be a prime number, $\nu, \mu \in \mathbb{N}^r$ with $\nu$ non-increasing, and $\nu, \mu \leq M$. Then $\mathrm{Exp}_l(\nu, \mu) \leq e$ if and only if $\mathrm{Exp}_l(\nu^*, \mu^*) \leq e$.

Lean: `Formalism.CohomologicalDescent.LD.expDual`.

*Proof.* By symmetry and $(\nu^*)^* = \nu$ it is enough to show one direction. Let $x \in \nabla(\nu)_\mu$ be nonzero; its total degree is $\sum_a \nu(a) = \sum_a \mu(a)$. Four facts about the cofactor map are used. (1) There is $g \in \nabla(\nu^*)$ with $\det(X)^{\sum \nu}\, g = \det(X)^M \mathrm{cof}(x)$, and the same holds for $\Delta$. (2) This $g$ has row weight $\mu^*$. (3) $\mathrm{cof}(\det X) = \det(X)^{r-1}$. (4) For $x$ homogeneous of degree $N$, $\det(X)^N \mathrm{cof}(\mathrm{cof}(x)) = \det(X)^{(r-1)N} x$. Assume $\mathrm{Exp}_l(\nu^*, \mu^*) \leq e$. Then $m\, l^e g \in \Delta(\nu^*)$ for some $m$ prime to $l$, and (1) for $\Delta$ gives $y \in \Delta(\nu)$ with $\det(X)^{\sum \nu^*}\, y = \det(X)^M \mathrm{cof}(m l^e g)$. Applying $\mathrm{cof}$ to (1) and using (3), (4) and $\sum \nu^* + \sum \nu = r M$, both $y$ and $m l^e x$ satisfy the same equation after multiplication by a power of $\det(X)$. Since $\mathbb{Z}[x]$ is a domain, $y = m l^e x$. $\square$

**Theorem 4.2.10 (Lemma D for the last block).** Assume Lemma D in its graded form. Let $l$ be a prime number, $p, q, w, M \in \mathbb{N}$, $\lambda_2 \in \mathbb{N}^q$ non-increasing with $w \leq \lambda_2(b) \leq M$ for all $b$, and $\xi \in \mathbb{Z}^{q+p}$ non-increasing. Let $i' \in \mathbb{Z}$, $e \in \mathbb{N}$, and assume $\mathrm{Exp}_l(\lambda_2, \mu_2) \leq e$ for every $\mu_2$ with $d_\xi((\lambda_2, w^p), (\mu_2, w^p)) \leq i'$. Then for every $i$ and every $\mu \in \mathbb{N}^{q+p}$ of last depth $i$ with $d_\xi((\lambda_2, w^p), \mu) \leq i'$,
$$\mathrm{Exp}_l\bigl((\lambda_2, w^p), \mu\bigr) \leq e + v_l\bigl(D_n(p, M - w, i, \lambda_2^*)\bigr), \qquad \lambda_2^*(b) = M - \lambda_2(q - 1 - b).$$

Lean: `Formalism.CohomologicalDescent.LD.lastGradedOfGradedAlone` (also `Formalism.CohomologicalDescent.LD.last_graded_of_graded_alone`, a second name).

*Proof.* First let $q \geq 1$. Then $w \leq \lambda_2(0) \leq M$. It is enough to treat a nonzero $x \in \nabla((\lambda_2, w^p))_\mu$; then $\mu \leq M$, because a weight of $\nabla(\nu)$ is bounded by $\nu(0)$. By exponent duality it is enough to bound $\mathrm{Exp}_l$ of the dual weights. The dual of $(\lambda_2, w^p)$ is $((M - w)^p, \lambda_2^*)$, and $\mu$ of last depth $i$ goes to $\mu^*$ of depth $i$ for the scalar $M - w$. Put $\xi'(a) = -\xi(p + q - 1 - a)$, which is non-increasing; then $d_{\xi'}(\nu^*, \mu^*) = d_\xi(\nu, \mu)$. The hypothesis on $\lambda_2$ moves to $\lambda_2^*$ by exponent duality in rank $q$. Lemma D (hypothesis of the theorem) for $(p, q, M - w, \lambda_2^*, \xi')$ now gives the bound, and exponent duality moves it back. If $q = 0$, then $\lambda_2$ is empty, the shapes have no rows, $D_n = 1$, and the claim follows in the same way with $M$ replaced by $\max(M, w)$. $\square$

**Remark 4.2.11 (Formalization).** In [RealOfSkeleton.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/RealOfSkeleton.lean#L46), the hypothesis that a $\mathbb{Q}$-polynomial in $\nabla$ with integral lower triangular coefficients is integral is taken as an argument and never used; the second result supplies it anyway. Down.hG is a theorem whose name reads like that of a local hypothesis. In HighestWeightProdLeadingMinors.lean, last_graded_of_graded_alone (line 1075) is a second name of lastGradedOfGradedAlone (line 1061), and lines 1063 to 1074 add twelve more such names. We did not unfold the definitions of the integral modules $\nabla$ and $\Delta$; the rank two remark uses the input statement on exact divisors in rank two. The argument of the column vanishing is summarized from the list of lemmas that its proof combines (in LemmaDSkeletonFour.lean); we did not open them. The proof of item 7 in Lemma D from the skeleton is a lemma that we did not open in detail.
