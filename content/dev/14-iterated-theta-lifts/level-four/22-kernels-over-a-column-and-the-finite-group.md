---
title: Kernels over a column and the finite group
decls:
  - GlobalTheory.Mem.Col2.KerRat.kernelsOver_of_ok
  - GlobalTheory.T.exists_finite_group_goodSet_levels_characters
  - GlobalTheory.Mem.R3.Grp.grp_levels_exist
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernels over a column and the finite group

Two more inputs of [the nonempty hypotheses at unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) are proved in this section. The first is about one column of the construction: the kernel maps of its chain of theta lifts are the matrix kernels of the true theta data, the kernels and the period are rational, and the period of a column form against a row form is the image of a finite period. The second is about the finite group of the auxiliary places: it is identified with the group of the level data, and its good set of characters, its idempotent and its level characters have values in the small coefficient field $K_s$.

### Kernels over a column

Let $B$ be a base with coefficient field $L_L$ and embedding $\mathrm{emb}_L : L_L \to \mathbb{C}$, and let $X$ be pre-base data with primes $\mathrm{Pr}(X)$. Let $I$ be column input over $B$ and $l$ a column lift of $I$, with $m$ steps. For a word $u$ and an index $a$ of $I$, the lift gives a chain of theta lifts with kernel maps $K(i, c, c')$ between the representatives $c$ at step $i$ and $c'$ at step $i + 1$, a family of forms with embeddings $\mathrm{emb}(i)$, and a period datum. Let $\theta_a$ be the true theta datum of $(I, u, a)$ at step $m - 2$, and let $\mathrm{ev}(i)$ be the evaluation at step $i$.

**Definition 1.22.1 (Kernels over a column).** Assume that $I$ is good. The kernels are over the column at $(u, a)$ if the following seven conditions hold.

1. For $i + 2 < m$, the kernel map $K(i, c, c')$ applied to $\mathrm{ev}(i)(x)$ is $\mathrm{ev}(i + 1)$ of the matrix kernel of $\theta_a$ at $i$ for $c$, $c'$ and $x$.
2. At $i = m - 2$, the kernel map is the first coupled kernel of $\theta_a$.
3. At $i = m - 1$, for each $q$ equal to the representative $c'$, the kernel map takes $\mathrm{ev}(x)$ to $\mathrm{ev}(y)$, where $y$ is the top degree kernel of $\theta_a$ at $c$ and $q$.
4. At $i = m - 1$, if $c'$ is the tilde point of a row point $d$, the kernel map takes $\mathrm{ev}(x)$ to $\mathrm{ev}(y)$, where $y$ is the second coupled kernel of $\theta_a$ at $c$ and the row of $d$.
5. The kernels of the family of forms are rational at each $i < m$.
6. The period of the family is rational.
7. The set of indices $b$ of the last step is not empty, and for each $b$ there are a $Y_b$ hypothesis, a kernel equivalence, good characters and a good finite datum $\tilde{M}$ such that for all column forms $\varphi$ and row forms $z$,
$$P\big(\mathrm{emb}(0)(\varphi), z\big) = \mathrm{emb}_L\big(\tilde{P}(\mu_b(\varphi), z)\big).$$

Here $P$ is the period of the column against the row, $\tilde{P}$ is the finite period of $\tilde{M}$, and $\mu_b(\varphi)$ is the column multiplicity vector of $\varphi$ at $b$.

**Theorem 1.22.2 (Kernels over a column).** Let $I$ be good with jets in the column, let $u$ be a word and $a$ an index. Assume that the characters of $\theta_a$ are good, and that for each $i < m$ the ambient datum satisfies the local hypothesis and the smoothness hypothesis of the steps $N(i)$ and $N(i + 1)$. Then the kernels are over the column at $(u, a)$.

Lean: `GlobalTheory.Mem.Col2.KerRat.kernelsOver_of_ok`.

*Proof.* Step 1. For each $i < m$ the kernels of the lift are read at $i$ by the true kernels. This uses that $I$ is good, the jets, and the two hypotheses of the steps $N(i)$ and $N(i + 1)$. Step 2. For each $i < m$ the true kernels hit their target at $i$. This uses that $I$ is good and that the characters of $\theta_a$ are good. Step 3. For $i + 2 < m$, the true kernel at $i$ is the matrix kernel, so Step 1 gives condition 1. Step 4. At the penultimate step, the true kernel is the first coupled kernel, and Step 1 gives condition 2. Step 5. At the last step, the true kernel is the top degree kernel up to a cast of the representative, and Step 1 gives condition 3. Step 6. If $c'$ is the tilde point of $d$, then the top degree kernel at $c'$ is the second coupled kernel at the row of $d$, by the tame frame of the characters. With Step 5 this gives condition 4. Step 7. A kernel that is read and hits its target has a rational form at each embedding of the family, which is condition 5. Step 8. The weights of the built chain are good at each embedding, so the lower forms of the period have rational forms, which is condition 6. Step 9. The index of the last step is unique, so the set of $b$ is not empty. For each $b$ the $Y_b$ hypothesis, the kernel equivalence, the good characters and the good datum $\tilde{M}$ exist, and the comparison of the column period with the finite period, from Steps 1 and 2, gives the formula of condition 7. $\square$

### The finite group of the auxiliary places

Let $X$ be a stage over a base $B$ with pre-base data $p_x$, let $G_c$ be the finite group of $X$, and let $I$ be column input over $B$. Let $U$ be a set of indices and $L$ level and character data for the tuples of $(I, U)$, with places $P_g$. Write $G_0(P_g)$ for the product over $v \in P_g$ of the groups $\mathrm{GL}_r(k_v)$, and $G_0$ for the finite group of the datum, with its idempotent $e_0$ in the group algebra $\mathbb{C}[G_0]$.

**Definition 1.22.3 (Placewise identity).** A group isomorphism $e_G : G_c \cong G_0(P_g)$ is a placewise identity if $e_G(g)_v = g_v$ for each $g \in G_c$ and each place $v$ that is both in $P_g$ and a place of $G_c$.

**Definition 1.22.4 (Good set of characters).** Let $e_R : G_c \cong G_0$ be a group isomorphism and $X_g$ a finite set of functions $G_c \to L_L$. Then $X_g$ is good for $e_R$ if two conditions hold. First, $\chi \in X_g$ if and only if $\chi$ is an absolutely irreducible character and
$$\sum_{g \in G_c} e_0(e_R(g))\, \mathrm{emb}_L(\chi(g)) = \mathrm{emb}_L(\chi(1)).$$
Second, $\mathrm{emb}_L$ of the coefficient of the idempotent of $X_g$ at $g$ is $e_0(e_R(g))$, for each $g$.

The first condition determines $X_g$, so a good set for $e_R$ is unique if it exists. The group condition on $I$ says three things: the places of $G_c$ are the places $P_{g,w}(k, v)$ of the datum, through a bijection with the level divisibility; $e_0$ is idempotent; and $e_0$ is central in $\mathbb{C}[G_0]$.

**Lemma 1.22.5 (Central coefficients).** Let $G$ be a group and $e \in \mathbb{C}[G]$ central. Then $e(k g k^{-1}) = e(g)$ for all $k$ and $g$.

*Proof.* Compare the coefficients at $k g$ of $\delta_k e$ and $e \delta_k$. The first is $e(g)$ and the second is $e(k g k^{-1})$. $\square$

**Corollary 1.22.6.** If $X_g$ is good for $e_R$ and $e_0$ is central, then the coefficients of the idempotent of $X_g$ are constant on the conjugacy classes of $G_c$.

*Proof.* Since $\mathrm{emb}_L$ is injective, it is sufficient to compare the images. They are $e_0(e_R(a b a^{-1}))$ and $e_0(e_R(b))$, and $e_R(a b a^{-1})$ is a conjugate of $e_R(b)$. The lemma gives the equality. $\square$

**Theorem 1.22.7 (Finite group, good set and levels).** Let $I$ be good, let the fields of $B$ be good, assume the group condition on $I$, and let $L$ be the level data of $(I, U)$. Then there are group isomorphisms $e_G : G_c \cong G_0(P_g)$ and $c_G : G_0(P_g) \cong G_0$, and a finite set $X_g$, with the following properties.

1. $e_G$ is a placewise identity.
2. $X_g$ is good for $c_G \circ e_G$.
3. The levels and characters of the first two columns are compatible with the generic character through $c_G \circ e_G$.
4. The coefficients of the idempotent of $X_g$ and the values of the first column character are in $K_s$.
5. For each trace datum $\mathrm{tr}$, the family of rows $A(X, I, U, X_g, \mathrm{tr})$ has an idempotent with class functions as coefficients, and its levels are the levels of $L$ through $e_G$ at the second level of the base face.
6. For each trace datum there is a bijection $p$ from the pairs $(k, v)$ of the datum to $P_g$, with field isomorphisms $\mathbb{Z}/g_k \cong k_{p(k, v)}$, such that $p(k, v) = P_{g,w}(k, v)$, the level of $L$ is divisible at $(k, p(k, v))$, and $e_G(g)_{p(k, v)}$ is the base change of $(c_G e_G(g))_{(k, v)}$ along the field isomorphism.

Lean: `GlobalTheory.T.exists_finite_group_goodSet_levels_characters` (also `GlobalTheory.Mem.R3.Grp.grp_levels_exist`, the proof).

*Proof.* Step 1. The finite group of $I$ has an identification with the group of the fixed places: this gives $e_G$, $c_G$, the bijection $p$ and the field isomorphisms, with properties 1 and 6. Step 2. For the isomorphism $c_G \circ e_G$ there is a good set $X_g$ whose idempotent has coefficients in $K_s$. This gives property 2 and the first half of property 4. Step 3. The column levels give the compatibility of property 3, from Step 1 and the level data. Step 4. The upper unipotent generic character has values in the integers of $K_s$, which gives the second half of property 4. Step 5. For each trace datum, the corollary on central coefficients, with $e_0$ central by the group condition, gives the class function property. The levels of the base face are the symmetric levels of $L$ through $e_G$, by the column face levels, which gives property 5. $\square$

**Remark 1.22.8 (Formalization).** The structure `KernelsOver` is at [KernelsOverOfFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/KernelsOverOfFamily.lean#L183) and the theorem at line 256. Its fields are `mat`, `cp1`, `top`, `cp2`, `krat`, `prat` and `period`. The matrix kernels, the coupled kernels, the top degree kernel, the evaluation `evT`, the rationality conditions `KRat` and `PRat`, the period `PtilCol` and the finite period `PtilFF` are not unfolded here; the definition above gives them by name only. The same file has two variants, `kernelsOver_of_thHyp` at line 292 and `kernelsOver_of_family` at line 299, which get the hypotheses on the characters and the steps from theta hypotheses or from the family laws. The statement of the second theorem is at [ExistsFiniteGroupGoodSetLevelsCharactersStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsFiniteGroupGoodSetLevelsCharactersStatement.lean#L9) and is proved by `first | exact` with `grp_levels_exist` ([ExistsFiniteGroupGoodSetLevelsCharacters.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsFiniteGroupGoodSetLevelsCharacters.lean#L29)). The central coefficient lemma is `coeff_conj_of_central` at line 17 of that file and the corollary is `idemOf_coeff_conj` at line 23. The steps of the proof are statements of the form `GlobalTheory.T.*` that we have not opened. The definitions `IsPlacewiseIdentity`, `GoodSet` and `GrpAt` are in [IsAbsIrrCharCompIff.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsAbsIrrCharCompIff.lean#L220), and the uniqueness of a good set is `GoodSet.unique` in that file. The levels `Seed.LevelsL` and the tie `PsiPPTie` are not unfolded.
