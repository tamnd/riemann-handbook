---
title: Siegel domains
decls:
  - GlobalTheory.CompanionTheory.RedCov.step
  - GlobalTheory.CompanionTheory.RedCov.hasRed_all
  - GlobalTheory.CompanionTheory.RedCov.cov_main
  - GlobalTheory.T.unitary_siegel_domain_exists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Siegel domains

This section proves the main theorem of reduction theory for a unitary group over a CM field: the rational translates of one Siegel set cover the adelic group. It is the unitary case of the theorem of Borel and Harish-Chandra; see [arithmetic subgroups and Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets). The proof is an induction on the Witt index. A vector of nearly minimal height plays the role of the first basis vector of a reduced basis, and the rest of the space is a unitary space of smaller Witt index. The covering is an input of the [Siegel package](/entry/siegel-core/) of the chapter on finiteness, and so of everything in this volume that cuts a quotient into a compact part and cusps. We keep the notation of the previous two sections: $E/F$ is a CM extension, $J$ a nondegenerate Hermitian matrix, $(X, Y)$ a Witt frame of rank $r$, and $P$, $P^1$ the minimal parabolic and its norm-one part.

**Definition 3.3.1 (Split torus).** A split torus for the frame $(X, Y)$ is a continuous homomorphism $a : \mathbb{R}^r \to G(\mathbb{A})$ such that, for every $s \in \mathbb{R}^r$:

1. $a(s)$ is an archimedean point;
2. $a(s) x_i = e^{s_i} x_i$ and $a(s) y_i = e^{-s_i} y_i$ for each $i$, at every archimedean place;
3. $a(s)$ is the identity on the anisotropic complement $V_0$.

Such a torus exists for every frame. It is the group $A$ of the classical theory, written additively through the logarithm.

**Definition 3.3.2 (Cone and Siegel set).** For $c > 0$ let
$$A_c = \{ t \in \mathbb{R}^r : t_i > 0, \ c\, t_{i+1} \le t_i \text{ for } i < r, \ c \le t_r \}.$$
For a set $\Omega \subseteq G(\mathbb{A})$, a constant $c > 0$ and a subgroup $K$, the Siegel set $\mathfrak{S}(\Omega, c, K)$ is the set of products $p\, a\, k$ where $p \in \Omega$, $k \in K$, and $a$ is an archimedean point that acts on $X$ by $\operatorname{diag}(t)$, on $Y$ by $\operatorname{diag}(t)^{-1}$ and trivially on $V_0$, for some $t \in A_c$.

The cone says that the torus part goes to infinity only in the direction where $x_1$ becomes short. In the classical picture for $\mathrm{SL}_2(\mathbb{Z})$, the cone is the half-line $y \ge c$ in the upper half-plane.

**Definition 3.3.3 (Nearly minimal vector).** Let $g \in G(\mathbb{A})$ and let $\operatorname{ht}_g$ be the height of the [previous section](/entry/min-par-one-cocompact/). A vector $v \in E^n$ is nearly minimal for $g$ if $v \neq 0$, $h(v, v) = 0$, and
$$\operatorname{ht}_g(v) \le 2 \operatorname{ht}_g(u)$$
for every nonzero isotropic $u \in E^n$.

**Definition 3.3.4 (Reduction property).** The frame $(X, Y)$ has the reduction property if for every split torus $a$ there are a compact set $C$ and a constant $c > 0$ such that every $g \in G(\mathbb{A})$ can be written
$$g = \gamma\, q\, a(s)\, \kappa, \qquad \gamma \in G(F), \ q \in P^1, \ (e^{s_1}, \dots, e^{s_r}) \in A_c, \ \kappa \in C.$$

The reduction property is a covering by sets $G(F) P^1 a(\text{cone}) C$. The compact $C$ is not yet a group, and $P^1$ is not yet compact. The [last theorem](/entry/cov-main/) of the section repairs both.

We take the following facts as given. Let $(X, Y)$ have rank $r + 1$ and let $a$ be a split torus for it.

- (Full Iwasawa decomposition.) There is a compact subgroup $K$ with $G(\mathbb{A}) = PK$.
- (Rank reduction.) There are a Hermitian matrix $J'$ on a space of smaller dimension, a Witt frame $(X', Y')$ of rank $r$ for $J'$ and a continuous homomorphism $\iota : G'(\mathbb{A}) \to G(\mathbb{A})$ with the following properties. It maps rational points to rational points and $P'^1$ into $P^1$. It fixes $x_1$. For each split torus $a'$ of $(X', Y')$, $\iota(a'(s')) = a(0, s')$. The elements $a(s_1, 0)$ commute with the image of $\iota$. Every $p \in P$ is $q_0\, a(s_1, 0)\, \iota(g')$ with $q_0 \in P^1$, such that $\iota(h)^{-1} q_0\, \iota(h) \in P^1$ for all $h$. Here $J'$ is the form on the orthogonal complement of $x_1$ and $y_1$.
- (Existence of nearly minimal vectors.) Every $g$ has a nearly minimal vector.
- (Witt's theorem over $F$.) For every nonzero isotropic $v \in E^n$ there is $\gamma \in G(F)$ with $\gamma x_1 = v$.
- (Rational parabolic elements.) If $\delta \in G(F) \cap P$, then $\delta(e x_1) = x_1$ for some $e \in E^\times$.
- (Height bounds.) For compact sets $\Omega \subseteq P^1$ and $C$ there are $M_1, M_2 > 0$ such that, if $\omega \in \Omega$, $\kappa \in C$ and some multiple $e x_1$ with $e \neq 0$ is nearly minimal for $\omega\, a(s)\, \kappa$, then
$$e^{-s_1} \le M_1 \quad \text{and} \quad e^{s_2} \le M_2\, e^{s_1}.$$

The height bounds are the heart of reduction theory. The height of $x_1$ at $\omega a(s) \kappa$ is about $e^{-s_1}$, and the height of $x_2$ is about $e^{-s_2}$. If $x_1$ is nearly minimal, then $e^{-s_1}$ is bounded by a Hermite constant, and $e^{-s_1}$ is at most a constant times $e^{-s_2}$.

**Lemma 3.3.5 (Induction step).** Assume that every Witt frame of rank $r$, for every nondegenerate Hermitian matrix over $E$, has the reduction property. Then every Witt frame of rank $r + 1$ has the reduction property.

Lean: `GlobalTheory.CompanionTheory.RedCov.step`.

*Proof.* Let $(X, Y)$ have rank $r + 1$ and let $a$ be a split torus. Take $K$ from the full Iwasawa decomposition, and $\iota$, $J'$, $(X', Y')$ from rank reduction. Choose a split torus $a'$ for $(X', Y')$. The induction hypothesis gives $C'$ and $c'$ for $a'$. Take $\Omega$ from the [theorem on the norm-one parabolic](/entry/min-par-one-cocompact/). Put $C = \iota(C')\, K$, which is compact. Take $M_1, M_2$ from the height bounds for $\Omega$ and $C$, and set
$$c = \min(c', M_1^{-1}, M_2^{-1}).$$
Let $g \in G(\mathbb{A})$. Choose a nearly minimal vector $v$ for $g$ and a rational $\gamma_1$ with $\gamma_1 x_1 = v$. Write $\gamma_1^{-1} g = pk$ with $p \in P$ and $k \in K$, and then $p = q_0\, a(s_1, 0)\, \iota(g')$. The induction hypothesis gives
$$g' = \gamma'\, q'\, a'(s')\, \kappa', \qquad \gamma' \in G'(F), \ q' \in P'^1, \ \kappa' \in C'.$$
Since $a(s_1, 0)$ commutes with the image of $\iota$ and $\iota(a'(s')) = a(0, s')$, we get, with $S = (s_1, s')$,
$$\gamma_1^{-1} g = q_0\, \iota(\gamma')\, \iota(q')\, a(S)\, \iota(\kappa')\, k.$$
The element $Q = \iota(\gamma')^{-1} q_0\, \iota(\gamma')\, \iota(q')$ lies in $P^1$. Write $Q = \delta \omega$ with $\delta$ rational in $P$ and $\omega \in \Omega$. Then
$$g = \bigl(\gamma_1\, \iota(\gamma')\, \delta\bigr) \cdot \omega\, a(S) \cdot \bigl(\iota(\kappa') k\bigr),$$
with the first factor rational and the last in $C$. It remains to show that $e^S$ lies in the cone $A_c$.

The vector $x_1$ is fixed by $\iota(\gamma')$, so $\gamma_1 \iota(\gamma') x_1 = v$. Pick $e \neq 0$ with $\delta(e x_1) = x_1$. The height is invariant under rational translation, so $e x_1$ is nearly minimal for $\omega\, a(S)\, \iota(\kappa') k$. The height bounds give $e^{-S_1} \le M_1$ and $e^{S_2} \le M_2 e^{S_1}$. So $c\, e^{S_2} \le e^{S_1}$, and if $r = 0$ then $c \le e^{S_1}$. The other inequalities of the cone involve only $s'$; they hold with $c'$ by the induction hypothesis, and so with $c \le c'$. $\square$

**Proposition 3.3.6 (Reduction in every rank).** Every Witt frame of every rank, for every nondegenerate Hermitian matrix over a CM extension, has the reduction property.

Lean: `GlobalTheory.CompanionTheory.RedCov.hasRed_all`.

*Proof.* Induction on the rank $r$. For $r = 0$ the torus is trivial, the cone is the one point of $\mathbb{R}^0$, and $g = 1 \cdot g \cdot a(0) \cdot 1$ with $C = \{1\}$. The [induction step](/entry/red-cov-step/) gives rank $r + 1$ from rank $r$. $\square$

**Theorem 3.3.7 (Siegel domains for unitary groups).** Let $E/F$ be a CM extension, $J$ Hermitian and nondegenerate, and $(X, Y)$ a Witt frame of rank $r$. Let $K$ be a compact subgroup of $G(\mathbb{A})$ with $G(\mathbb{A}) = PK$, in good position for $(X, Y)$. Then there are a compact set $\Omega \subseteq P^1$ and a constant $c > 0$ such that
$$G(\mathbb{A}) = G(F)\, \mathfrak{S}(\Omega, c, K).$$

Lean: `GlobalTheory.CompanionTheory.RedCov.cov_main` (also `GlobalTheory.T.unitary_siegel_domain_exists`, a second name).

*Proof.* Choose a split torus $a$. By the [proposition](/entry/has-red-all/), there are $C$ and $c$ with $G(\mathbb{A}) = G(F) P^1 a(\log A_c) C$. Take $\Omega$ from the [theorem on the norm-one parabolic](/entry/min-par-one-cocompact/).

There is a continuous homomorphism $\tau : P \to \mathbb{R}^r$ with $\tau(a(s)) = s$, $\tau = 0$ on $P^1$, and $p\, a(\tau(p))^{-1} \in P^1$ for all $p \in P$. It records the logarithms of the absolute values of the diagonal entries. The set $(CK) \cap P$ is compact, because $P$ is closed. So $|\tau_i| \le B$ on it, for some $B \ge 0$.

Let $g = \gamma\, q\, a(s)\, \kappa$ as in the reduction property. Write $\kappa = pk$ with $p \in P$ and $k \in K$. Then $p = \kappa k^{-1} \in (CK) \cap P$, so $u = \tau(p)$ has $|u_i| \le B$. Put $p_1 = p\, a(u)^{-1} \in P^1$. Since $a(s)$ normalizes $P^1$,
$$g = \gamma\, \bigl(q\, a(s) p_1 a(s)^{-1}\bigr)\, a(s + u)\, k,$$
and the middle factor lies in $P^1$. Write it as $\delta \omega$ with $\delta$ rational and $\omega \in \Omega$. Then $g = (\gamma \delta)\, \omega\, a(s + u)\, k$. Finally, $e^{s+u}$ lies in the cone $A_{c e^{-2B}}$: each coordinate moves by a factor between $e^{-B}$ and $e^{B}$, so each ratio $e^{s_i + u_i}/e^{s_{i+1}+u_{i+1}}$ moves by at least $e^{-2B}$, and the last coordinate by at least $e^{-B} \ge e^{-2B}$. $\square$

**Remark 3.3.8 (Formalization).** The good position hypothesis of the theorem is not used: it is bound to `_` in [UnitarySiegelDomainExists.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitarySiegelDomainExists.lean#L203). The induction step does not use the given $K$ either; it takes its own compact group from `GlobalTheory.T.unitary_adelic_iwasawa` (line 77). The given facts are statements of the form `GlobalTheory.T.*`: `witt_frame_reduce_rank`, `exists_near_minimal_vector`, `rational_unitary_sends_isotropic`, `minimal_parabolic_scales_isotropic`, `reduction_theory_height_bound` and `reduction_theory_lower_bound`. The bound $e^{s_2} \le M_2 e^{s_1}$ concerns the coordinate of index $1$ (counting from $0$); it is used only when the rank is at least $2$.
