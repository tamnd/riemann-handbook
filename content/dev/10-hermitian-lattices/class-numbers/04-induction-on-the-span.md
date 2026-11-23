---
title: Induction on the span
decls:
  - GlobalTheory.ClassFin.cf_of_isQGroup
  - GlobalTheory.T.finiteAdelicDoubleCosets_of_rational_SL_subgroup
  - GlobalTheory.T.hasFiniteAdelicDoubleCosets_of_blockDiagPart_image
  - GlobalTheory.ClassFin.cf_of_cf_blk_image
  - GlobalTheory.ClassFin.PolySection.exists_section
  - GlobalTheory.T.exists_rat_idempotent_blockDiagPart_kills_span
  - GlobalTheory.T.isAutStableSLMatrixGroup_image_blockDiagPart
  - GlobalTheory.T.ratZariskiClosure_of_autStable_SL_group
  - GlobalTheory.T.finrank_span_blockDiagPart_image_lt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Induction on the span

This section removes the hypothesis of complete reducibility. A rational group that is not completely reducible fixes a rational flag $W \subset \mathbb{C}^I$, and its block-diagonal part for this flag is a smaller rational group. The kernel of the passage to the block-diagonal part is a vector group, and a polynomial section splits it. Class finiteness lifts from the block-diagonal part to the group, by clearing denominators in the vector group. An induction on the dimension of the linear span of the group then proves that every rational group has finite class number over every adelic pair. This is the main theorem of the chapter over $\mathbb{Q}$.

### The block-diagonal part

Let $e \in M_I(\mathbb{Q})$ be an idempotent, $e^2 = e$, and $W = e\,\mathbb{C}^I$. A matrix $g$ is *block upper triangular for $e$* if $(1 - e) g e = 0$, that is, if $gW \subseteq W$. The *block-diagonal part* of a matrix $g$ over a $\mathbb{Q}$-algebra is
$$\beta_e(g) = e g e + (1 - e) g (1 - e).$$

In a basis adapted to $\mathbb{C}^I = W \oplus (1 - e)\mathbb{C}^I$, a block upper triangular $g$ is $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$ and $\beta_e(g) = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix}$. So $\beta_e$ is linear, and it is multiplicative on block upper triangular matrices, with $\beta_e(1) = 1$ and $\det \beta_e(g) = \det g$. For a set $\Gamma$ we write $\beta_e(\Gamma)$ for its image.

**Lemma 1.4.1 (A rational flag).** Let $\Gamma$ be a Galois-stable group that is not completely reducible. Then there are an idempotent $e \in M_I(\mathbb{Q})$ such that every $g \in \Gamma$ is block upper triangular for $e$, and a nonzero matrix $a$ in the complex span of $\Gamma$ with $\beta_e(a) = 0$.

Lean: `GlobalTheory.T.exists_rat_idempotent_blockDiagPart_kills_span`.

*Proof.* Let $A \subseteq M_I(\mathbb{C})$ be the complex span of $\Gamma$. It is an algebra, since $\Gamma$ is closed under products, and it is stable under the automorphisms of $\mathbb{C}$. The $\Gamma$-stable subspaces of $\mathbb{C}^I$ are the $A$-submodules. If $A$ were semisimple, every $A$-module would be semisimple and $\Gamma$ would be completely reducible. So the radical $J$ of $A$ is not zero. It is stable under $\operatorname{Aut}(\mathbb{C})$, and it is nilpotent. Let $W = J\,\mathbb{C}^I$, and let $a \neq 0$ lie in the last nonzero power of $J$. Then $W$ is $\Gamma$-stable and $\operatorname{Aut}(\mathbb{C})$-stable, $a\,\mathbb{C}^I \subseteq W$ and $aW = 0$. A subspace of $\mathbb{C}^I$ that is stable under $\operatorname{Aut}(\mathbb{C})$ has a basis of rational vectors. Complete it by rational vectors to a basis of $\mathbb{C}^I$, and let $e$ be the projection onto $W$ along their span. Then $e$ is rational, $(1 - e)ge = 0$ for $g \in \Gamma$, $ae = 0$ since $aW = 0$, and $(1 - e)a = 0$ since $a$ maps into $W$. So $\beta_e(a) = 0$. $\square$

**Lemma 1.4.2 (The block-diagonal image).** Let $\Gamma$ be a Galois-stable group and $e \in M_I(\mathbb{Q})$ an idempotent such that every $g \in \Gamma$ is block upper triangular for $e$. Then $\beta_e(\Gamma)$ is a Galois-stable group.

Lean: `GlobalTheory.T.isAutStableSLMatrixGroup_image_blockDiagPart`.

*Proof.* The map $\beta_e$ is multiplicative on $\Gamma$ and preserves $1$ and the determinant, so $\beta_e(\Gamma)$ is a group of matrices of determinant $1$, and $\operatorname{adj}(\beta_e(g)) = \beta_e(g)^{-1} = \beta_e(g^{-1})$. Since $e$ is rational, $\sigma(\beta_e(g)) = \beta_e(\sigma(g))$ for $\sigma \in \operatorname{Aut}(\mathbb{C})$. $\square$

**Lemma 1.4.3 (Rational closure).** Let $\Gamma$ be a Galois-stable group. Then $\Gamma(\mathbb{C})$ is a rational group, $\mathfrak{a}(\Gamma(\mathbb{C})) = \mathfrak{a}(\Gamma)$, and $\Gamma(\mathbb{C})$ and $\Gamma$ have the same complex span.

Lean: `GlobalTheory.T.ratZariskiClosure_of_autStable_SL_group`.

*Proof.* Since $\Gamma \subseteq \Gamma(\mathbb{C})$ and every $f \in \mathfrak{a}(\Gamma)$ vanishes on $\Gamma(\mathbb{C})$, the two rational ideals agree. So $\Gamma(\mathbb{C})(\mathbb{C}) = \Gamma(\mathbb{C})$. By the lemma on points of the first section with $R = \mathbb{C}$, the set $\Gamma(\mathbb{C})$ contains $1$, is closed under products and adjugates, and has determinant $1$. It is stable under $\operatorname{Aut}(\mathbb{C})$, since the equations $f \in \mathfrak{a}(\Gamma)$ have rational coefficients. For the span: the span of $\Gamma$ is stable under $\operatorname{Aut}(\mathbb{C})$, so it is the zero set of the rational linear forms that vanish on it. Such a form lies in $\mathfrak{a}(\Gamma)$, so it vanishes on $\Gamma(\mathbb{C})$. $\square$

**Lemma 1.4.4 (The span drops).** Let $\Gamma \subseteq M_I(\mathbb{C})$, $e \in M_I(\mathbb{Q})$, and let $a \neq 0$ in the span of $\Gamma$ with $\beta_e(a) = 0$. Then the span of $\beta_e(\Gamma)$ has smaller dimension than the span of $\Gamma$.

Lean: `GlobalTheory.T.finrank_span_blockDiagPart_image_lt`.

*Proof.* Since $\beta_e$ is linear, the span of $\beta_e(\Gamma)$ is the image of the span of $\Gamma$ under $\beta_e$. The restriction of $\beta_e$ to the span of $\Gamma$ has $a$ in its kernel, so its image has smaller dimension by the rank-nullity theorem. $\square$

### A polynomial section

For rational numbers $c = (c_{ij, kl})$ let $L_c(X)_{ij} = \sum_{k, l} c_{ij, kl} X_{kl}$, a $\mathbb{Q}$-linear map of $M_I(A)$ to itself for every $\mathbb{Q}$-algebra $A$.

**Lemma 1.4.5 (Polynomial section).** Let $\Gamma$ be a rational group and $e \in M_I(\mathbb{Q})$ an idempotent such that every $g \in \Gamma$ is block upper triangular for $e$. Let $\Gamma' = \beta_e(\Gamma)$. Then there are rational numbers $c$ and polynomials $b_{ij} \in \mathbb{Q}[x]$ such that for every commutative $\mathbb{Q}$-algebra $R$:

1. $1 + L_c(X) \in \Gamma(R)$ for every $X \in M_I(R)$;
2. $L_c(X) L_c(Y) = 0$ for all $X, Y$;
3. every $y \in \Gamma(R)$ with $\beta_e(y) = 1$ is $1 + L_c(X)$ for some $X$;
4. every $x \in \Gamma(R)$ is block upper triangular for $e$, and $\beta_e(x) \in \Gamma'(R)$;
5. for every $y \in \Gamma'(R)$ the matrix $\sigma(y) = (b_{ij}(y))$ lies in $\Gamma(R)$ and $\beta_e(\sigma(y)) = y$.

Lean: `GlobalTheory.ClassFin.PolySection.exists_section`.

So $\Gamma(R)$ is an extension of $\Gamma'(R)$ by the vector group $\{1 + L_c(X)\}$, split by a map $\sigma$ given by rational polynomials. Each matrix $L_c(X)$ satisfies $eL_c(X)(1 - e) = L_c(X)$, so it lies in the upper right block, and part 2 follows from $(1 - e)e = 0$. We use the lemma without a full proof. Its proof first finds $c$ and $b$ with the five properties for $R = \mathbb{C}$ and $\Gamma$ in place of $\Gamma(R)$. Each property is a polynomial identity with rational coefficients, or says that a polynomial map with rational coefficients sends $\Gamma$ into a set of points. Such a statement carries over from $\Gamma$ to $\Gamma(R)$: if a rational polynomial $f$ vanishes on $\Gamma$, then it vanishes on $\Gamma(R)$ by definition.

### Clearing denominators

**Lemma 1.4.6 (Classes of bounded denominator).** Let $(R, R_0)$ be an adelic pair, and $S \subseteq M_I(R)$ a set that contains $1$, is closed under products and adjugates, and has determinant $1$. Let $N \geq 1$ be an integer. Then there is a finite set $F \subseteq S$ such that every $w \in S$ with $Nw$ integral is $w = tp$ with $t \in F$ and $p \in S$ integral.

*Proof.* Let $\delta = |I| - 1$ and $L = N^{\delta + 1}$. Let $w \in S$ with $Nw$ integral. By part 1 of the lemma on elementary properties, $Nw_{ij} = z_{ij} + La_{ij}$ with $z_{ij} \in \mathbb{Z}$ and $a_{ij} \in R_0$. The class of $w$ is the matrix $(z_{ij} \bmod L)$ in $M_I(\mathbb{Z}/L)$. There are finitely many classes. For each class that occurs, choose one $t \in S$ in it, and let $F$ be the set of these. If $w$ and $t$ have the same class, then $Nw - Nt$ has entries in $L R_0$. Since $N$ is invertible in $R$, this gives $w = t + N^\delta E$ with $E$ integral. Then
$$p = t^{-1} w = \operatorname{adj}(t)\, w = 1 + N^\delta \operatorname{adj}(t)\, E = 1 + \operatorname{adj}(Nt)\, E,$$
since the adjugate is homogeneous of degree $\delta$. As $Nt$ is integral, so is $\operatorname{adj}(Nt)$, and $p$ is integral. Also $p \in S$ and $w = tp$. $\square$

**Theorem 1.4.7 (Lifting through the block-diagonal part).** Let $\Gamma$ be a rational group, $e \in M_I(\mathbb{Q})$ an idempotent such that every $g \in \Gamma$ is block upper triangular for $e$, and $(R, R_0)$ an adelic pair. If $\beta_e(\Gamma)$ has finite class number over $(R, R_0)$, then so has $\Gamma$.

Lean: `GlobalTheory.T.hasFiniteAdelicDoubleCosets_of_blockDiagPart_image` (also `GlobalTheory.ClassFin.cf_of_cf_blk_image`, a second name).

*Proof.* Let $\Gamma' = \beta_e(\Gamma)$, let $T'$ be a finite set for $\Gamma'$, and take $c$, $b$ and $\sigma$ from the lemma on the polynomial section. Let $x \in \Gamma(R)$. By part 4, $\beta_e(x) \in \Gamma'(R)$, so $\beta_e(x) = \gamma_0 s u$ with $\gamma_0 \in \Gamma'(\mathbb{Q})$, $s \in T'$ and $u \in \Gamma'(R)$ integral. The matrix $\sigma(\gamma_0)$ is rational and lies in $\Gamma(\mathbb{Q})$ by part 5 with $R = \mathbb{Q}$. Since $\beta_e$ is multiplicative on $\Gamma(R)$, the matrix $n = \sigma(s)^{-1} \sigma(\gamma_0)^{-1} x\, \sigma(u)^{-1} \in \Gamma(R)$ has $\beta_e(n) = s^{-1}\gamma_0^{-1}\beta_e(x)u^{-1} = 1$. So does $m = \sigma(s)\, n\, \sigma(s)^{-1}$, so $m = 1 + L_c(Y)$ by part 3, and
$$x = \sigma(\gamma_0)\, m\, \sigma(s)\, \sigma(u).$$
By part 2 of the lemma on elementary properties, there is an integer $K \geq 1$ such that $K c_{ij, kl} \in \mathbb{Z}$ for all indices and $K\sigma(s)$ and $K\sigma(s)^{-1}$ are integral for all $s \in T'$. It depends only on $T'$ and $c$. By condition 2 of an adelic pair, applied to each entry, $Y = q + K^3 Y_0$ with $q \in M_I(\mathbb{Q})$ and $Y_0$ integral. By part 2,
$$1 + L_c(Y) = (1 + L_c(q))(1 + L_c(K^3 Y_0)).$$
Let $\gamma = \sigma(\gamma_0)(1 + L_c(q))$. It lies in $\Gamma(\mathbb{Q})$ by part 1. Let
$$v = \sigma(s)^{-1}(1 + L_c(K^3 Y_0))\,\sigma(s) = 1 + (K\sigma(s)^{-1})\, L_{Kc}(Y_0)\, (K\sigma(s)).$$
It is integral and lies in $\Gamma(R)$, and $x = \gamma\, \sigma(s)\, v\, \sigma(u)$. Let $N \geq 1$ be a common denominator of the coefficients of the polynomials $b_{ij}$. Since $u$ is integral, $N\sigma(u)$ is integral, so $w = v\sigma(u) \in \Gamma(R)$ has $Nw$ integral. The lemma on classes of bounded denominator, for $S = \Gamma(R)$, gives a finite $F \subseteq \Gamma(R)$, depending only on $N$, with $w = tp$, $t \in F$ and $p \in \Gamma(R)$ integral. So $x = \gamma\,(\sigma(s) t)\, p$, and $T = \{ \sigma(s) t : s \in T', t \in F \}$ is a finite subset of $\Gamma(R)$ that works for every $x$. $\square$

### The theorem over $\mathbb{Q}$

**Theorem 1.4.8 (Class finiteness over an adelic pair).** Let $\Gamma \subseteq M_I(\mathbb{C})$ be a rational group and $(R, R_0)$ an adelic pair. Then $\Gamma$ has finite class number over $(R, R_0)$: there is a finite set $T \subseteq \Gamma(R)$ with $\Gamma(R) = \Gamma(\mathbb{Q})\, T\, (\Gamma(R) \cap M_I(R_0))$.

Lean: `GlobalTheory.ClassFin.cf_of_isQGroup` (also `GlobalTheory.T.finiteAdelicDoubleCosets_of_rational_SL_subgroup`, a second name).

*Proof.* We use induction on the dimension $n$ of the complex span of $\Gamma$, for all rational groups and all adelic pairs at once. If $\Gamma$ is completely reducible, this is the [theorem of the completely reducible case](/entry/cf-of-ss/). If not, the lemma on a rational flag gives $e$ and $a$. Let $\Gamma' = \beta_e(\Gamma)$. It is a Galois-stable group by the lemma on the block-diagonal image. By the lemma on rational closure, $\Gamma'(\mathbb{C})$ is a rational group with the rational ideal and the span of $\Gamma'$. By the lemma on the span, this span has dimension less than $n$. So $\Gamma'(\mathbb{C})$ has finite class number by induction. Class finiteness depends only on the rational ideal, so $\Gamma'$ has finite class number. The theorem on lifting through the block-diagonal part gives the result for $\Gamma$. $\square$

**Remark 1.4.9 (Formalization).** The lemma on classes of bounded denominator is the private lemma `exists_finset_integral_classes` of [HasFiniteAdelicDoubleCosetsOfBlockDiagPartImage.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/HasFiniteAdelicDoubleCosetsOfBlockDiagPartImage.lean#L111), and the dependence of class finiteness on the rational ideal is `GlobalTheory.ClassFin.cf_congr_of_vanI_eq`. The lemma on a rational flag is proved from `GlobalTheory.T.invariant_subspace_not_semisimple` and `GlobalTheory.T.exists_rat_idempotent_of_autStable_subspace`; we have opened their statements, not their proofs, and the argument with the radical of the span is ours. The polynomial section comes from `GlobalTheory.T.exists_polynomial_section_blockDiagonal_map`, whose proof we have not unfolded. The induction runs on the dimension of the span of $\Gamma$ in $M_I(\mathbb{C})$, not on the dimension of the group. The theorem on lifting asks for class finiteness of the image $\beta_e(\Gamma)$ itself, not of its rational closure. The second name of the main theorem is a wrapper proved by `first | exact ...` under `set_option maxHeartbeats 1000000`.
