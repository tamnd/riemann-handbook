---
title: Colength at split places
decls:
  - GlobalTheory.ChF.colength_bound_linDat
  - GlobalTheory.T.colength_bound_split_place_linear_data
  - GlobalTheory.ChF.colength_bound_split_place_chart
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Colength at split places

Let $O_E$ act on a formal group $F$ of dimension $d$ over $\mathcal{O}$, and let $\tau : O_E \to \mathcal{O}$ be an embedding. The differentials of the characters of $F$ span a submodule of the cotangent space $\mathcal{O}^d$. Restrict them to the $\tau$-eigenspace of the tangent space. If the restrictions span this eigenspace up to a small colength, then the Hodge-Tate periods of $F$ are close to integral there. This section bounds the colength at the embeddings of a place $w$ of $E$ above $p$ that is split by the involution: $w \neq \bar w$. The bound is in terms of the eigenspace dimension $r_-$ at the conjugate place, the prime $p$ and the discriminant of $w$. We prove it first for a [linear datum](/entry/exists-lin-dat-of-ext-ser/), and then for the formal group of a degenerating abelian scheme with an action of $O_E$. The second form is used directly in the step [every character of the literature](/step/every-character-of-literature/).

We keep the setting of [the previous section](/entry/exists-lin-dat-of-ext-ser/). So $C$ is algebraically closed of characteristic $0$, $\mathcal{O}$ is the ring of integers of $v$, $p$ is not a unit in $\mathcal{O}$, and $\mathcal{O}$ is a $p$-adically complete $\mathbb{Z}_p$-algebra. Now $O_E$ is a Dedekind domain of characteristic $0$ that is free of finite rank over $\mathbb{Z}$, with an involution $a \mapsto a^*$. The main example is the ring of integers of a CM field with complex conjugation. Put $O_e = \mathbb{Z}_p \otimes O_E$ and $\sigma = 1 \otimes {}^*$. Each ring map $\tau : O_E \to \mathcal{O}$ extends to a $\mathbb{Z}_p$-algebra map $\tilde\tau : O_e \to \mathcal{O}$.

### Places, lengths and eigenbases

**Definition 4.5.1 (Place above $p$).** A *place* of $O_E$ above $p$ is a primitive idempotent $e \neq 0$ of $O_e$. It is *split* if $\sigma(e) \neq e$. Its *conjugate* is $\bar e = \sigma(e)$. Put $O_w = eO_e$ and $n = \operatorname{rank}_{\mathbb{Z}_p} O_w$. The *embeddings of $e$* are the ring maps $\tau : O_E \to \mathcal{O}$ with $\tilde\tau(e) = 1$.

The primitive idempotents of $O_e$ correspond to the primes of $O_E$ above $p$, and $O_w$ is the completion at the prime. So the embeddings of $e$ are the embeddings of $O_E$ into $\mathcal{O}$ that are continuous for this prime.

**Definition 4.5.2 (Discriminant exponent).** Let $w$ be a place with $n$ embeddings $\tau_1, \dots, \tau_n$. A real number $\delta$ is a *discriminant exponent* of $w$ if there is a $\mathbb{Z}_p$-basis $b_1, \dots, b_n$ of $O_w$ with
$$v\Bigl(\det\bigl(\tilde\tau_j(b_i)\bigr)_{i,j}^2\Bigr) = v(p)^{n\delta}.$$

The square of the determinant is the discriminant of $O_w$ over $\mathbb{Z}_p$, so $n\delta$ is its $p$-adic valuation, measured in units of $v(p)$. It is $0$ if $w$ is unramified.

**Definition 4.5.3 (Length).** Let $M$ be an $\mathcal{O}$-module and $x \geq 0$ a real number. Then $M$ has *length* $x$ if $M \cong \bigoplus_{i=1}^m \mathcal{O}/c_i\mathcal{O}$ for some $c_1, \dots, c_m \in \mathcal{O}$ with $\prod_i v(c_i) = x$.

So the length is multiplicative and lies in $[0, 1]$. A small length is a large module. A bound $v(p)^\lambda \leq x$ says that $M$ has size at most $\lambda$ in units of $v(p)$.

**Definition 4.5.4 (Eigenbasis).** Let $\rho : O_E \to M_d(\mathcal{O})$ and let $\tau : O_E \to \mathcal{O}$ be a ring map. Vectors $W_1, \dots, W_s \in \mathcal{O}^d$ form a *$\tau$-eigenbasis* of $\rho$ if $\rho(a)W_i = \tau(a)W_i$ for all $i$ and $a$, and each $x \in \mathcal{O}^d$ with $\rho(a)x = \tau(a)x$ for all $a$ is a unique $\mathcal{O}$-combination of the $W_i$. For a covector $u \in \mathcal{O}^d$ put $\mathrm{res}_W(u) = (W_i^{\mathsf T} u)_i \in \mathcal{O}^s$.

So $\mathrm{res}_W(u)$ is the restriction of the linear form $u$ to the $\tau$-eigenspace, in the basis $W$.

### The bound for linear data

**Theorem 4.5.5 (Colength at a split place, linear form).** Let $c_p \in \mathcal{O}$, and let $H$ be a Hodge-Tate datum over $\mathcal{O}$ for $(O_e, \sigma, c_p)$ in a Hodge-Tate setting. Let $(H, A, B, \rho_G, N, s)$ be a linear datum with $s_1, \dots, s_m \in \mathcal{O}^d$. Let $w$ be a place above $p$ with embeddings $\tau_1, \dots, \tau_n$, and let $\delta$ be a discriminant exponent of $w$. Let $r_+, r_- \geq 0$. Assume that for each $j$ the vectors $W_{j,1}, \dots, W_{j,r_+}$ form a $\tau_j$-eigenbasis of $\rho_G$, and that each embedding of $\bar e$ has an eigenbasis of $\rho_G$ with $r_-$ elements. Then there are lengths $x_1, \dots, x_n$ such that $\mathcal{O}^{r_+}/\langle \mathrm{res}_{W_j}(s_k) : k \leq m\rangle$ has length $x_j$ for each $j$, and
$$v(p)^{n r_- \left(\frac{1}{p-1} + \frac{\delta}{2}\right)} \leq \prod_{j=1}^n x_j.$$

Lean: `GlobalTheory.ChF.colength_bound_linDat` (also `GlobalTheory.T.colength_bound_split_place_linear_data`, a second name).

*Proof.* Write $\lambda = v(p)$ and $D = \lambda^{n\delta}$. The proof has six steps.

First, $O_w$ is monogenic: there is $\alpha \in O_e$ such that $e, e\alpha, \dots, e\alpha^{n-1}$ is a $\mathbb{Z}_p$-basis of $O_w$. The values $a_j = \tilde\tau_j(\alpha)$ are distinct, and $v\bigl(\prod_{j \neq j'} (a_j - a_{j'})\bigr) = D$, with $n\delta \geq 0$.

Second, the abelian part has small eigenspaces at the conjugate place. Let $\tau$ be an embedding of $\bar e$. The eigenbasis of $\rho_G$ at $\tau$ has $r_-$ elements, so the $\tau$-eigenspace of $\rho_G$ over $C$ has dimension $r_-$. Since $(A, B)$ is split exact and intertwines $\rho_G$ with $N$ and $\rho_L$, this dimension is the sum of the dimensions for $N$ and for $\rho_L$. So the $\tau$-eigenspace of $\rho_L(1 \otimes \cdot)$ has dimension at most $r_-$.

Third, the Hodge-Tate cokernel. Let $\mathrm{Lie}_e$ be the image of $\rho_L(e)^{\mathsf T}$ in $\mathcal{O}^g$ and $T_{\bar e}$ the image of $\rho(\bar e)$ in $\mathcal{O}^{\mathrm{Ix}}$. The quotient $\mathrm{Lie}_e / H(T_{\bar e}) \cap \mathrm{Lie}_e$ is the cokernel of the Hodge-Tate map from the $\bar e$-part of the Tate module to the $e$-part of the cotangent space. By the second step and the theory of the abelian part, it has a length $c_w$ with $\lambda^{n r_-/(p-1)} \leq c_w$. The exponent $1/(p-1)$ is that of $v(c_p) = v(p)^{1/(p-1)}$ in a Hodge-Tate setting.

Fourth, the generators. Let $\kappa : \mathcal{O}^d \to \mathcal{O}^{n \times r_+}$ be $u \mapsto (\mathrm{res}_{W_j}(u))_j$, and let $M$ be its image. There are $h \leq r_+ + r_-$ vectors $\psi_1, \dots, \psi_h \in \mathcal{O}^d$ such that each $\mathrm{res}_{W_j}(\psi_l)$ lies in the span of the $\mathrm{res}_{W_j}(s_k)$, and such that the Hodge-Tate cokernel maps onto $M/M'$, where $M'$ is spanned by the vectors $(a_j^q \,\mathrm{res}_{W_j}(\psi_l))_j$ for $q < n$ and $l \leq h$.

Fifth, the lattice inequality. The module $M$ is finitely generated and stable under multiplication by $(a_j)_j$, and it maps onto each factor $\mathcal{O}^{r_+}$. So $M/M'$ has a length $c$, and $c_w \leq c$ by the surjection of the fourth step. A lattice inequality over $\mathcal{O}$ then gives lengths $y_j$ of the quotients $\mathcal{O}^{r_+}/\langle \mathrm{res}_{W_j}(\psi_l) \rangle$ with
$$c^2 D^h \leq \Bigl(\prod_j y_j\Bigr)^2 D^{r_+}.$$
Since the span of the $\mathrm{res}_{W_j}(\psi_l)$ is in the span of the $\mathrm{res}_{W_j}(s_k)$, the module of the theorem is a quotient of this one, and its length $x_j$ satisfies $y_j \leq x_j$.

Sixth, the arithmetic. Put $X = \prod_j x_j$. Since $0 < D \leq 1$ and $h \leq r_+ + r_-$, we have $D^{r_+ + r_-} \leq D^h$, so $c^2 D^{r_-} D^{r_+} \leq X^2 D^{r_+}$ and $c^2 D^{r_-} \leq X^2$. With $\lambda^{n r_-/(p-1)} \leq c_w \leq c$ this gives
$$\Bigl(\lambda^{n r_-\left(\frac{1}{p-1} + \frac{\delta}{2}\right)}\Bigr)^2 = \bigl(\lambda^{n r_-/(p-1)}\bigr)^2 D^{r_-} \leq X^2,$$
and the claim follows by taking square roots. $\square$

### The bound for degenerating abelian schemes

Now let $T$ be a complete noetherian local domain of characteristic $0$ in which $p$ is not a unit. Let $G$ be a smooth commutative group scheme over $T$ whose generic fibre is a polarized abelian variety $A$. Assume that $G$ comes with degeneration data $D$: a uniformization over the thickenings $T/I^{k+1}$ of the maximal ideal $I$ by a Raynaud extension of an abelian scheme by a split torus with character group $X$, with a cubical line bundle, as in the theory of Mumford and of Faltings and Chai. Let $x$ be a formal chart of $G$ at the origin, with formal group law $F$ of dimension $d$. Let $O_E$ act on $G$, on the data $D$ and on $A$ compatibly with the uniformization, where $a$ acts on $X$ through $a^*$. Let $O_E$ act on $F$ compatibly with the chart. Let $\iota : T \to \mathcal{O}$ be a local ring map, and write $F^\iota$ and $\rho^\iota(a)$ for the base change of $F$ and the linear part of the action of $a$ over $\mathcal{O}$.

**Theorem 4.5.6 (Colength at a split place, chart form).** In this setting, let $w$ be a place above $p$ with embeddings $\tau_1, \dots, \tau_n$ and a discriminant exponent $\delta$. Let $r_+, r_- \geq 0$. Assume that for each $j$ the vectors $W_{j,1}, \dots, W_{j,r_+}$ form a $\tau_j$-eigenbasis of $\rho^\iota$, and that each embedding of $\bar e$ has an eigenbasis of $\rho^\iota$ with $r_-$ elements. Then there are lengths $x_1, \dots, x_n$ such that for each $j$ there are characters $u_1, \dots, u_m$ of $F^\iota$ with
$$\mathcal{O}^{r_+}/\langle \mathrm{res}_{W_j}(du_k) : k \leq m \rangle \text{ of length } x_j, \qquad v(p)^{n r_- \left(\frac{1}{p-1} + \frac{\delta}{2}\right)} \leq \prod_{j=1}^n x_j.$$

Lean: `GlobalTheory.ChF.colength_bound_split_place_chart`.

*Proof.* We build a linear datum and apply the linear form. The chart $x$ gives a nilpotent chart of $G$ that reads the action of $O_E$. The abelian part of the Raynaud extension has a formal group law $F_B$ of dimension $g$, and each endomorphism of the abelian part is read by power series $\alpha_B(a)$. The uniformization makes $F$ an extension of $F_B$ by $\hat{\mathbb{G}}_m^r$, equivariant for $O_E$ with integral matrices $N(a)$ on the torus part. After base change along $\iota$, the formal group law $F^\iota$ has finite flat $p$-power torsion, by a result on the $p^k$-torsion of $G$. The polarized abelian part gives a Hodge-Tate datum with an invertible matrix $S$ and characters of $F_B^\iota$, as in the hypothesis of [the theorem on split extensions](/entry/exists-lin-dat-of-ext-ser/). That theorem gives a linear datum whose covectors are differentials of characters $u_k$ of $F^\iota$, with $\rho_G = \rho^\iota$. The linear form now gives the lengths $x_j$, with the same characters $u_k$ for each $j$. $\square$

**Remark 4.5.7 (Formalization).** The second name of the linear form is proved by `first | exact @GlobalTheory.ChF.colength_bound_linDat | ...` at [ColengthBoundSplitPlaceLinearDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ColengthBoundSplitPlaceLinearDataStatement.lean#L21), with a raised heartbeat limit at line 19. The chart form is stated as a proposition about a prime $p$. Its proof calls the second names of the linear form and of [the theorem on split extensions](/entry/exists-lin-dat-of-ext-ser/), not the first names. In the chart form the characters are chosen for each $j$ separately, but the proof gives one family for all $j$. The eigenbasis hypotheses for $\rho^\iota$ are stated for the linear parts of the action series, and the proof converts them to eigenbases of $\rho_G$. The six steps of the linear form are results of their own in the development; we have opened their statements, and the third and the fifth are used as given.
