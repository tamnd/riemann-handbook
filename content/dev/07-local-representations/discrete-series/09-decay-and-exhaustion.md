---
title: Decay along paths and the exhaustion of the discrete series
decls:
  - CompanionTheory.RgExh.Dec.J.exhaustion_labels
  - CompanionTheory.RgExh.Dec.L.back_of_inputs
  - CompanionTheory.RgExh.Dec.L.back_of_lineFormula
  - CompanionTheory.RgExh.Dec.L.backward_of_line_formula
  - CompanionTheory.RgExh.Dec.decay_estimate
  - CompanionTheory.RgExh.Fin.exhaustion_finite_length
  - CompanionTheory.RgExh.dsExhaust
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Decay along paths and the exhaustion of the discrete series

This section proves that every irreducible square integrable unitary representation of $U(p,q)$ is a discrete series with a Harish-Chandra parameter, in the sense of the lowest $K$-type. The proof moves the Harish-Chandra module along a path of steps, as in [Theorem 3.8.7](/entry/hecke-algebra-exhaustion/). It shows that the end of a long path still embeds into $L^2(U(p,q))$, and then counts parameters. The result is used in the step [EveryCharacter from the literature](/step/every-character-of-literature/).

Background: [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees), [asymptotics of matrix coefficients](/learn/real-groups/#asymptotics-of-matrix-coefficients), [[unitary representation|74BPYJNZTM]], [[Harish-Chandra module|2MKHH636C3]].

We keep the notation of the previous section: $\mathfrak{gl}_n$-modules, characters, steps $\operatorname{st}(X, z)$, paths with labels $\operatorname{end}(\chi)$, good paths, $c_n = (n-1)/2$, $\rho_c$, $\rho_n$, $\Lambda(\mu) = \mu + \rho_n - \rho_c$, and algebraic discrete series. Let $G_\varepsilon = \{g : g^*Jg = J\}$ with $J = \operatorname{diag}(\varepsilon)$ and $\mathfrak{g}_\varepsilon$ its Lie algebra. We say that the *shift of characters* holds if, for all $X$, $\chi$ and $s$, a module with character $\chi$ has a step $\operatorname{st}(X, \chi_s)$ with character $\chi + e_s$.

### Harish-Chandra modules and $L^2$ embeddings

**Definition 3.9.1 (Harish-Chandra module of $\sigma$).** Let $\sigma$ be a representation of $G_\varepsilon$ on a Hilbert space $H$. A *Harish-Chandra module* of $\sigma$ is a subspace $D \subseteq H$ with operators $E_{ab}$ on $D$ such that: $D$ is the space of $K$-finite vectors; $\frac{d}{dt}\sigma(\exp tY)v|_{t=0} = \sum_{a,b} Y_{ab}E_{ab}v$ for $Y \in \mathfrak{g}_\varepsilon$ and $v \in D$; the $E_{ab}$ satisfy the relations of $\mathfrak{gl}_n$, are unitary for $\varepsilon$ and are locally $K$-finite; and every $K$-type of $\sigma$ contains a nonzero $K$-highest vector of $D$ of the same weight.

**Definition 3.9.2 ($L^2$ embedding).** A $\mathfrak{gl}_n$-module $X$ has an *$L^2$ embedding* if for every nonzero $u \in X$ there is a linear map $c$ from $X$ to the smooth vectors of the right regular representation $R$ of $G_\varepsilon$ on $L^2(G_\varepsilon)$ with $c(u) \neq 0$ and $c(E_{ab}x) = dR(E_{ab})c(x)$ for all $a, b, x$.

**Definition 3.9.3 (Far labels).** Let $B \in \mathbb{R}$. The labels $\chi'$ are *$B$-far from* $\chi$ if for all disjoint sets $I, I'$ of indices with $|I| = |I'|$ and $\operatorname{Re}(\sum_I \chi - \sum_{I'}\chi) < 0$ we have $\operatorname{Re}(\sum_I \chi' - \sum_{I'}\chi') < -B$.

### Gradings and line integrals

A *grading* is an $A \in \mathfrak{g}_\varepsilon$ with $A^* = A$, $A^3 = A$ and $A \neq 0$. Let $V_A$ be the image of $\frac12(A^2 - A)$ and $W_A$ the kernel of $\frac12(A^2 + A)$. Let $P_A$ be the subgroup of $g \in G_\varepsilon$ with $gV_A = V_A$ and $gW_A = W_A$. Let $j_A = \operatorname{tr}\frac12(A^2 + A)$ and $\rho_A = j_A(n - j_A)$. A *parabolic Haar measure* for $A$ is the image in $G_\varepsilon$ of a Haar measure on $P_A$. Put $a_t = \exp(tA)$.

For a function $f$ on matrices, $s \in \mathbb{R}$ and $x \in G_\varepsilon$, put
$$\ell_s(f, x) = \int_0^\infty |f(x a_t)|^2 e^{-2st}\, dt \in [0, \infty].$$
Let $(f_i)$ be a family of linear maps from a space $V$ to functions. A vector $u \in V$ satisfies the *line condition at $s$* for $(f_i)$, $A$ and a measure $\mu$ if for every $i$, $\ell_s(f_i(u), x) < \infty$ for $\mu$-almost every $x$.

For the representation $\sigma$, the *base coefficients* are $c_\xi(u)(g) = \langle \xi, \sigma(g)u\rangle$. If $c$ is a linear map from $X$ to functions and $j$ is an index, the *step coefficient* on $\operatorname{st}(X, z) \subseteq X^n$ is
$$c^{(j)}(u)(g) = \sum_i g_{ji}\, c(u_i)(g).$$
Along a path $s_1, \dots, s_k$ and a list $j_1, j_2, \dots$ of indices, apply this at each stage, with $j_m$ at stage $m$ (and $s_m$ if the list is too short). Starting from $c_\xi$ with $\xi \in D$, this gives the *path coefficients* $c_{\xi, j}$ on $\operatorname{path}(X)$.

### The three steps of the decay argument

**Theorem 3.9.4 (Labels).** Assume the shift of characters. For every $n$ there is $B$ with the following property. Let $\sigma$ be a unitary representation of $G_\varepsilon$ on a Hilbert space with a Harish-Chandra module $X$ of character $\chi$, and take a good path whose labels $\operatorname{end}(\chi)$ are $B$-far from $\chi$. Let $A$ be a grading and $\mu$ a parabolic Haar measure for $A$. If every $u \in X$ satisfies the line condition at $-\rho_A$ for the base coefficients $(c_\xi)_{\xi \in D}$, then every $u \in \operatorname{path}(X)$ satisfies the line condition at $-\rho_A - 1$ for the path coefficients.

Lean: `CompanionTheory.RgExh.Dec.J.exhaustion_labels`

*Proof.* The theorem is derived from ten statements: local finiteness of a filtration, a decomposition of the tensor product along a step, a transport rule, a filtration and an induction for coefficient families, a base family, a start case, a degree bound, a basis of graded eigenvectors, and a tracking of labels. We did not open these statements or the argument that combines them. $\square$

**Definition 3.9.5 (Line formula).** The *line formula* holds if for every grading $A$, every Haar measure $\nu$ on $P_A$ and every continuous $\tau : G_\varepsilon \to \mathbb{R}$ with $\tau(y) = \tau(x) + t$ whenever $x, y \in P_A$ and $y = x a_t$, there is $\kappa \in (0, \infty)$ such that for every measurable $F \geq 0$ with $F(gk) = F(g)$ for $k \in K$,
$$\int_{G_\varepsilon} F\, dg = \kappa \int_{\{x \in P_A : \tau(x) \in [0,1)\}} \int_{\mathbb{R}} F(x a_t)\, e^{2\rho_A t}\, dt\, d\nu(x).$$

**Definition 3.9.6 (Polynomial reduction).** Let $\mathfrak{n}_A$ be the set of $Y_1 + Y_2$ with $[A, Y_1] = -Y_1$ and $[A, Y_2] = -2Y_2$, and for a matrix $Y$ let $Y \cdot u = \sum_{a,b} Y_{ab}E_{ab}u$. The *polynomial reduction* holds if for every module $X$ with a character and every grading $A$ there is a monic polynomial $p$ such that for every $u$, $p(A\cdot)u = \sum_k Y_k \cdot v_k$ for finitely many $Y_k \in \mathfrak{n}_A$ and $v_k \in X$.

**Definition 3.9.7 (Backward statement).** The *backward statement* says: assume the shift of characters; let $\sigma$ be a unitary square integrable representation on a Hilbert space with a Harish-Chandra module $X$ of character $\chi$, and take a path. If for every grading $A$ and every parabolic Haar measure $\mu$ for $A$, every $u \in \operatorname{path}(X)$ satisfies the line condition at $-\rho_A - 1$ for the path coefficients, then $\operatorname{path}(X)$ has an $L^2$ embedding.

**Proposition 3.9.8 (Backward statement from its inputs).** If the line formula and the polynomial reduction hold, then the backward statement holds.

Lean: `CompanionTheory.RgExh.Dec.L.back_of_inputs`

*Proof.* The backward statement is an assembly of eleven inputs: the line formula, the polynomial reduction, an absolute $L^2$ bound, a geometric statement on gradings, the existence of Haar measures on $P_A$, a right and a left rule for nilpotent elements, a statement on $K$-types on the right, a growth bound, a packing statement, and the assembly itself. The proof inserts the two given inputs and the other nine. We did not open the nine other inputs. $\square$

**Proposition 3.9.9 (Backward statement from the line formula).** If the line formula holds, then the backward statement holds.

Lean: `CompanionTheory.RgExh.Dec.L.back_of_lineFormula`

*Proof.* The polynomial reduction holds by a separate theorem. Apply [Proposition 3.9.8](/entry/back-of-inputs/). $\square$

**Theorem 3.9.10 (Backward statement).** The backward statement holds.

Lean: `CompanionTheory.RgExh.Dec.L.backward_of_line_formula`

*Proof.* The line formula holds by a separate theorem, which derives it from a Fubini statement, a list of facts on lines and an equality of parabolic subgroups. We did not open these three statements. Apply [Proposition 3.9.9](/entry/back-of-line-formula/). $\square$

**Theorem 3.9.11 (Decay along far paths).** Assume the shift of characters. For every $n$ there is $B$ with the following property. Let $\sigma$ be an irreducible square integrable unitary representation of $G_\varepsilon$ on a Hilbert space, with a Harish-Chandra module $X$ of character $\chi$. For every good path whose labels $\operatorname{end}(\chi)$ are $B$-far from $\chi$, the module $\operatorname{path}(X)$ has an $L^2$ embedding.

Lean: `CompanionTheory.RgExh.Dec.decay_estimate`

*Proof.* Take $B$ from [Theorem 3.9.4](/entry/exhaustion-labels/). A start statement says that for $\sigma$ unitary and square integrable, every $u \in X$ satisfies the line condition at $-\rho_A$ for all base coefficients $c_\xi$, $\xi \in H$, for every grading $A$ and every parabolic Haar measure. So the hypothesis of the theorem on labels holds, and it gives the line condition at $-\rho_A - 1$ for the path coefficients. [Theorem 3.9.10](/entry/backward-of-line-formula/) then gives the $L^2$ embedding. $\square$

### Exhaustion

**Definition 3.9.12 (Discrete series with parameter $\mu$).** A representation $\sigma$ of $G_\varepsilon$ on a Hilbert space $H$ is a *discrete series with parameter $\mu$* if $H \neq 0$, $\sigma$ is unitary, strongly continuous, irreducible and square integrable, the $K$-type of highest weight $\Lambda(\mu)$ occurs in $\sigma$, and $\|\Lambda(\mu) + 2\rho_c\| \leq \|\nu + 2\rho_c\|$ for every highest weight $\nu$ of a $K$-type of $\sigma$.

**Theorem 3.9.13 (Exhaustion from the four inputs).** Assume the shift of characters, the conclusion of [Theorem 3.8.7](/entry/hecke-algebra-exhaustion/), the conclusion of [Theorem 3.9.11](/entry/decay-estimate/) and the conclusion of [Theorem 3.8.9](/entry/far-regular-exhaustion/). Let $\sigma$ be an irreducible square integrable unitary representation of $G_\varepsilon$ on a Hilbert space $H \neq 0$. Then there are a Harish-Chandra parameter $\mu$ and a permutation $s$ with $s(a) < s(b)$ whenever $a < b$ and $\varepsilon_{s(a)} = \varepsilon_{s(b)}$, such that $g \mapsto \sigma\bigl((g_{s^{-1}(a)s^{-1}(b)})_{a,b}\bigr)$ is a discrete series with parameter $\mu$ for the sign vector $\varepsilon \circ s$.

Lean: `CompanionTheory.RgExh.Fin.exhaustion_finite_length`

*Proof.* The proof uses fifteen further statements, which we name by content when they are used. The *end data* of a module $M$ along the path is a pair $d = (s', \mu')$ such that $\operatorname{path}(M)$ is isomorphic to a unitary, locally $K$-finite, simple module that is an algebraic discrete series with data $d$.

First, $\sigma$ has a Harish-Chandra module $X$, and $X$ is simple, has integral weights and has a scalar character $\chi$. Take $B$ from the decay theorem. A path statement gives $C$ and $\delta > 0$ for $(\chi, B)$. Take $N_0$ from the far regular theorem for $(C, \delta)$. The path statement then gives a good path that uses every index, whose labels are $B$-far from $\chi$, and whose end labels satisfy the gap and size bounds of the far regular theorem for some $N \geq N_0$.

Key claim: if $\sigma'$ is irreducible, square integrable and unitary with a Harish-Chandra module $X'$ that is simple, has integral weights and has scalar character $\chi$, then the path is simple, $\operatorname{path}(X')$ has scalar character $\operatorname{end}(\chi)$, and $X'$ has end data $(s', \mu')$ with $\mu'$ a permutation of $\operatorname{end}(\chi)$. Indeed, the decay theorem gives an $L^2$ embedding of $\operatorname{path}(X')$. The shift of characters gives the character $\operatorname{end}(\chi)$, and a module with an $L^2$ embedding and a character has that character as a scalar character. The theorem on paths makes the path and $\operatorname{path}(X')$ simple. A module with an $L^2$ embedding that is simple is isomorphic to a unitary module. Steps keep local finiteness and integral weights, and isomorphisms keep all the properties used. The far regular theorem gives an algebraic discrete series structure $(s', \mu')$. A last statement says that $\mu'$ is then a permutation of the scalar character.

Apply the key claim to $X$, with end data $d_0$. So the entries of $\operatorname{end}(\chi)$ are distinct reals in $c_n + \mathbb{Z}$. Since $\operatorname{end}(\chi) - \chi \in \mathbb{N}^n$, the same holds for the reality and integrality of $\chi$, and since the path is simple and uses every index, the entries of $\chi$ are also distinct. A counting statement gives two finite sets $\mathcal{A}$ and $\mathcal{A}'$ of the same size: the pairs $(s, \mu)$ with $\mu$ a Harish-Chandra parameter, $s$ order preserving on each sign class, and $\mu$ a permutation of $\chi$ (for $\mathcal{A}$) or of $\operatorname{end}(\chi)$ (for $\mathcal{A}'$).

For $d \in \mathcal{A}$, an existence statement gives an irreducible square integrable unitary $\sigma_d$ whose Harish-Chandra modules $M_d$ are algebraic discrete series with data $d$ and satisfy a cone condition on their $K$-highest weights. Since $\mu$ is a permutation of the character of $M_d$ and of $\chi$, and $P_\chi$ does not change under permutation, $M_d$ has scalar character $\chi$. The key claim gives end data $e(d) \in \mathcal{A}'$. The map $e$ is injective. If $e(d_1) = e(d_2)$, a uniqueness statement for algebraic discrete series with the same data gives $\operatorname{path}(M_{d_1}) \cong \operatorname{path}(M_{d_2})$, and part 3 of the theorem on paths gives $M_{d_1} \cong M_{d_2}$. Then $M_{d_1}$ is an algebraic discrete series with data $d_1$ and $d_2$ and satisfies the cone condition for $d_1$, and a uniqueness statement for data gives $d_1 = d_2$. Since $|\mathcal{A}| = |\mathcal{A}'|$, $e$ is onto, so $d_0 = e(d)$ for some $d \in \mathcal{A}$. As before, $X \cong M_d$, so $X$ is an algebraic discrete series with data $d = (s, \mu)$. A final statement turns this into the claim for $\sigma$. $\square$

**Theorem 3.9.14 (Exhaustion of the discrete series).** Let $\sigma$ be an irreducible square integrable unitary representation of $G_\varepsilon \cong U(p,q)$ on a Hilbert space $H \neq 0$. Then there are a Harish-Chandra parameter $\mu$ and a permutation $s$ as in the previous theorem such that $\sigma$, renumbered by $s$, is a discrete series with parameter $\mu$ for $\varepsilon \circ s$.

Lean: `CompanionTheory.RgExh.dsExhaust`

*Proof.* Apply [Theorem 3.9.13](/entry/exhaustion-finite-length/). The shift of characters holds by a separate statement. The other three inputs are [Theorem 3.8.7](/entry/hecke-algebra-exhaustion/), [Theorem 3.9.11](/entry/decay-estimate/) (with the shift of characters) and [Theorem 3.8.9](/entry/far-regular-exhaustion/). $\square$

This is the exhaustion half of Harish-Chandra's classification of the discrete series: every discrete series representation has a regular integral Harish-Chandra parameter. The parametrization through the lowest $K$-type $\Lambda(\mu)$ is the one of Hecht-Schmid and Schmid (see the notes at the end of the chapter).

**Remark 3.9.15 (Formalization).** Four of these theorems take the shift of characters as a hypothesis inside the statement, and the final theorem passes the same proof of it twice ([DsExhaust.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/DsExhaust.lean#L14)). The assembly behind the backward statement also receives it twice ([BackOf.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/BackOf.lean#L7)). The decay theorem assumes irreducibility, but its proof does not use it ([DecayOf.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/DecayOf.lean#L7)). The polynomial reduction is proved by trying three forms of one term in turn. The right regular representation in the $L^2$ embedding is defined by a choice, with the identity as a fallback value. We opened the statements of all inputs named above and the proof of the exhaustion theorem from its inputs, but not the proofs of the inputs, the assembly or the start statement.
