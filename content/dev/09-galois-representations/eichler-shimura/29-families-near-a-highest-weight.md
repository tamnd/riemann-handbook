---
title: Families near a highest weight
decls:
  - UpperTheory.Gal.Wt.famEx_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Families near a highest weight

This section builds the families of automorphic forms that Section 30 uses to move the weight at $v'$. Let $f$ be an algebraic form fixed by $K'$ and $\tau$ an embedding over $v'$. For every dominant weight $\nu$, we find a family of forms that behaves like a matrix coefficient of the representation of highest weight $\nu$ at $\tau$, up to a defect $d$ that does not depend on $\nu$, and that is $\ell$-adically close to $f$. The method twists $f$ by the $\ell$-adic avatar of the component at $\tau$ and cuts the level into small pieces. The result is [the theorem on families](/entry/fam-ex-holds/).

We keep the notation of Sections 25 and 28. For an embedding $\tau : E \to \mathbb{C}$, we say $\tau$ *lies over* a place $v$ if $\lVert \iota^{-1} \tau(x) \rVert < 1$ for all $x \in v$, and $\tau$ *lies over the pair* of $v$ if $\tau$ or $\tau \circ c$ lies over $v$, with $c$ the complex conjugation of $E$. Let $c_\tau : G \to \mathrm{GL}_a(\mathbb{C})$ be the component at the infinite place of $\tau$, read through $\tau$, and $G_\tau \subset G_\infty$ the elements with trivial component at the other infinite places. A *weight family* $\lambda$ assigns a dominant weight $\lambda_\tau$ of $\mathrm{GL}_a$ to each $\tau$. Its *size* is $\lvert \lambda \rvert = \sum_\tau \sum_k \lvert \lambda_{\tau, k} \rvert$, and its *size over* a place $u$, written $\lvert \lambda \rvert_u$, is the same sum over the $\tau$ that lie over the pair of $u$. Each automorphic space $U$ has a weight at each $\tau$, and this weight is unique. For $K \subset G_f$, $U$ is *of type $(\lambda, K)$* if it is automorphic, has weight $\lambda_\tau$ at each $\tau$, and has a nonzero vector fixed by $K$. For a weight family $\lambda$, let $W_\lambda$ be the weight with family $\lambda$. An element of $G_w$ has trivial component at each place apart from $w$.

For a dominant weight $\nu$, let $\nabla_\nu$ be the representation of $\mathrm{GL}_a(\mathbb{C})$ of highest weight $\nu$, realized in polynomials in the entries of an $a \times a$ matrix, and $e_\nu$ its highest weight vector. Put $\chi_\nu(b) = \prod_i b_{ii}^{\nu_i}$ and $\delta_\nu(h)$ the value at the identity matrix of $h \cdot e_\nu$, for $h \in \mathrm{GL}_a(\mathbb{C})$. Write $\psi_\nu(k) = \nu_0 + \cdots + \nu_{k-1}$. Let $t_k(z) = \mathrm{diag}(z, \dots, z, 1, \dots, 1)$, with $k$ entries $z$, for $z$ on the unit circle. A *circle* of rank $k$ at $\tau$ is a map $z \mapsto x(z) \in G_\tau$ with $c_\tau(x(z)) = t_k(z)$. Let $\mathcal{E}_{\leq s}$ and $\mathcal{E}_{\geq s}$ be the spans of the functions $z \mapsto z^m$ on the circle with $m \leq s$, and with $m \geq s$.

**Definition 3.30.1 (Family near $\nu$).** Let $\tau$ be an embedding, $W$ a weight, $K \subset G$, $\nu$ a dominant weight and $d \geq 0$. A *family near $\nu$ at $\tau$* of level $K$ and defect $d$ is a map $B$ that sends $y_1, y_2 \in \mathrm{GL}_a(\mathbb{C})$ to a linear map $B(y_1, y_2)$ from $V_W$ to functions on $G$, such that:

1. each $B(y_1, y_2)(v)$ is an automorphic form fixed by $K$, and all of them lie in one finite dimensional space;
2. $R(x) B(y_1, y_2)(v) = B(c_\tau(x) y_1, c_\tau(x) y_2)(W(x) v)$ for $x \in G_\infty$;
3. $B(y_1 b, y_2) = \chi_\nu(b) B(y_1, y_2)$ for upper triangular $b$;
4. for each circle $x$ of rank $k$ at $\tau$, the function $z \mapsto B(t_k(z) y_1, t_k(z) y_2)(W(x(z)) v)(g)$ lies in $\mathcal{E}_{\leq \psi_\nu(k) + d}$, and $z \mapsto B(1, t_k(z) y_2)(W(x(z)) v)(g)$ lies in $\mathcal{E}_{\geq -d}$.

Lean: `UpperTheory.Gal.Wt.Fam` (also `UpperTheory.Gal.Wt.delta`, `UpperTheory.Gal.Wt.tor`, `UpperTheory.Gal.Wt.ExpLe`, `UpperTheory.Gal.Wt.ExpGe`).

Conditions 3 and 4 say that $B$ looks like a matrix coefficient of $\nabla_\nu$ in $y_1$, up to the defect $d$. A matrix $h$ is *integral* if $h$ and $h^{-1}$ have entries with $\lVert \iota^{-1}(\cdot) \rVert \leq 1$, and *$\varepsilon$-near $1$* if each entry of $h - 1$ has $\lVert \iota^{-1}(\cdot) \rVert \leq \varepsilon$.

**Proposition 3.30.2 (Inputs on families).** Let $a \geq 1$.

1. *Neat levels.* Let $w_0, v', K, K_v, K'$ be as in the theorem below, and $f$ an algebraic form fixed by $K'$. There is a level $C \supset K$ such that $\gamma g = g c x$ with $\gamma$ rational, $c \in C$, $x \in G_\infty$ forces $c = 1$; $c_{v'}(C) \subset \mathrm{GL}_a(\mathcal{O}_{v'})$; and $f$ is fixed by $C \cap c_{v'}^{-1}(K_v)$.
2. *Splitting.* For a subgroup $C \subset G_f$ with the property of item 1 on $\gamma g = g c x$, there is $L : G \to C$ with $L(\gamma g) = L(g)$ for rational $\gamma$, $L(gc) = L(g) c$ for $c \in C$ and $L(gx) = L(g)$ for $x \in G_\infty$.
3. *Twists.* Let $C$ be a level and $L$ as in item 2. For an algebraic form $f$ and $c \in C$ there is an algebraic form $F$ fixed by $C$ with $F(v)(g) = f(v)(g L(g)^{-1} c)$. If every algebraic form is bounded on $b : G \times X \to V_W$, there is $R > 0$ with $\lVert \iota^{-1} f(b(g, i))(g L(g)^{-1} c) \rVert \leq R$ for all $c, g, i$.
4. *The $\ell$-adic embedding.* For $\tau$ over $v'$ there is a homomorphism $\kappa : G \to \mathrm{GL}_a(\mathbb{C})$ with $\kappa(\gamma) = c_\tau(\gamma)$ for rational $\gamma$, $\kappa = 1$ on $G_\infty$, $\kappa(g) = 1$ if and only if $c_{v'}(g) = 1$, entries that are continuous for $\iota^{-1}$, and $\kappa(g)$ integral when $c_{v'}(g) \in \mathrm{GL}_a(\mathcal{O}_{v'})$.
5. *Pieces.* Let $\Gamma$ be a compact group, $\varphi : \Gamma \to \mathrm{GL}_a(\mathbb{C})$ a homomorphism with integral values and $\iota^{-1}$-continuous entries, $\Gamma' \supset \ker \varphi$ an open subgroup and $\varepsilon > 0$. There are finitely many $c_q \in \Gamma$ and polynomials $P_q$ in the matrix entries such that for each $g$ some $q_0$ has $c_{q_0}^{-1} g \in \Gamma'$, $\varphi(c_{q_0}^{-1} g)$ $\varepsilon$-near $1$, $\lVert \iota^{-1}(P_{q_0}(\varphi g) - 1) \rVert \leq \varepsilon$ and $\lVert \iota^{-1} P_q(\varphi g) \rVert \leq \varepsilon$ for $q \neq q_0$.
6. *Coefficients.* For integral $h$, $\lVert \iota^{-1} \delta_\nu(h) \rVert \leq 1$, and if $h$ is $\varepsilon$-near $1$ then $\lVert \iota^{-1}(\delta_\nu(h) - 1) \rVert \leq \varepsilon$.
7. *Construction.* Let $C$ be a level and $n : G \to \mathrm{GL}_a(\mathbb{C})$ with $n(\gamma g) = n(g)$ for rational $\gamma$, $n(gc) = n(g)$ for $c \in C$ and $n(gx) = n(g) c_\tau(x)$ for $x \in G_\infty$. Let $f_q$ be finitely many algebraic forms fixed by $C$, and $P_q$ polynomials. There is $d$ such that for all $\nu$ and $X_q \in \mathrm{GL}_a(\mathbb{C})$ the map
$$B(y_1, y_2)(v)(g) = \sum_q P_q(n(g) y_2)\, \delta_\nu(X_q n(g) y_1)\, f_q(v)(g)$$
is a family near $\nu$ at $\tau$ of level $C$ and defect $d$.

Lean: `UpperTheory.Gal.Wt.neatLev_holds` (also `UpperTheory.Gal.Wt.ellC_holds`, `UpperTheory.Gal.Wt.twist_holds`, `UpperTheory.Gal.Wt.twistBd_holds`, `UpperTheory.Gal.Wt.ladic_weight_embedding_over_place`, `UpperTheory.Gal.Wt.pieces_holds`, `UpperTheory.Gal.Wt.deltaNear_holds`, `UpperTheory.Gal.Wt.famOf_holds`).

These facts are proved elsewhere in the development, and we take them as given. Item 4 is the $\ell$-adic avatar of $c_\tau$: on rational points it is $c_\tau$, but it is continuous in the $\ell$-adic topology and sees only the component at $v'$.

**Theorem 3.30.3 (Families).** Let $a \geq 1$, let $w_0 \mid \ell$ and $v'$ be split places that are apart, $K$ a level away from $w_0$ that contains each $x \in G_{v'}$ with $c_{v'}(x) \in \mathrm{GL}_a(\mathcal{O}_{v'})$, $K_v \subset \mathrm{GL}_a(E_{v'})$ open, and $K' = \{x \in K : c_{v'}(x) \in K_v\}$. Let $W$ be a weight, $f$ an algebraic form of weight $W$ fixed by $K'$, $\tau$ an embedding over $v'$, and $b : G \times X \to V_W$ a map on which every algebraic form is bounded. For each $\varepsilon > 0$ there are $d \geq 0$ and $M : G \to \mathrm{GL}_a(\mathbb{C})$ with $M(gh) = M(g)$ for $h \in G_f$ with $c_{v'}(h) = 1$, such that for every dominant $\nu$ there is a family $B$ near $\nu$ at $\tau$ of level $K$ and defect $d$ with
$$\lVert \iota^{-1}\bigl(f(b(g, i))(g) - B(M g, M g)(b(g, i))(g)\bigr) \rVert \leq \varepsilon \quad \text{for all } g, i.$$

Lean: `UpperTheory.Gal.Wt.famEx_holds` (also `UpperTheory.Gal.Wt.famEx_of`, `UpperTheory.Gal.Wt.FamEx`).

*Proof.* Item 1 gives a neat level $C \supset K$, item 2 a map $L$, item 3 a bound $R$, and item 4 a homomorphism $\kappa$. Let $\varphi = \kappa|_C$; it has integral values since $c_{v'}(C) \subset \mathrm{GL}_a(\mathcal{O}_{v'})$. Its kernel lies in $\Gamma' = C \cap c_{v'}^{-1}(K_v)$, since $\kappa(c) = 1$ forces $c_{v'}(c) = 1$. Item 5 with $\Gamma'$ and $\varepsilon / R$ gives $c_q$ and $P_q$, and item 3 gives forms $F_q$ fixed by $C$ with $F_q(v)(g) = f(v)(g L(g)^{-1} c_q)$. Put $M(g) = c_\tau(g)^{-1} \kappa(g)$ and $n(g) = \kappa(L(g)) M(g)^{-1}$. For $h \in G_f$ with $c_{v'}(h) = 1$, $c_\tau(h) = 1$ and $\kappa(h) = 1$, so $M(gh) = M(g)$. The map $n$ has the three properties of item 7: for rational $\gamma$, $\kappa(\gamma) = c_\tau(\gamma)$ cancels; for $c \in C$, $L(gc) = L(g) c$ and $c_\tau(c) = 1$; for $x \in G_\infty$, $\kappa(x) = 1$. Item 7 gives $d$, and with $X_q = \kappa(c_q)^{-1}$ a family $B$ of level $C$, hence of level $K$.

Fix $g, i$ and take $q_0$ for $L(g)$ from item 5. Since $c_{q_0}^{-1} L(g) \in \Gamma'$ fixes $f$, $f(b(g,i))(g) = F_{q_0}(b(g,i))(g)$. As $n(g) M(g) = \kappa(L(g))$, the difference in the theorem is
$$\sum_q \bigl(\delta_{q q_0} - P_q(\kappa(L g))\, \delta_\nu(\kappa(c_q^{-1} L g))\bigr) F_q(b(g,i))(g).$$
Each $F_q$ term has $\lVert \iota^{-1}(\cdot) \rVert \leq R$. For $q \neq q_0$ the bracket is at most $\varepsilon / R$ by items 5 and 6. For $q = q_0$ write $1 - P\delta = -((P - 1)\delta + (\delta - 1))$; both terms are at most $\varepsilon / R$, since $\kappa(c_{q_0}^{-1} L g)$ is $\varepsilon / R$-near $1$. The ultrametric inequality bounds the sum by $\varepsilon$. $\square$

**Remark 3.30.4 (Formalization).** The theorem, [DeltaNear.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/WeightCharacters/DeltaNear.lean#L175), does not ask that $v'$ lie above $\ell$; only the weight change statement of Section 30 does. The name `ladic_weight_embedding_over_place` at [LadicWeightEmbeddingOverPlace.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/WeightCharacters/LadicWeightEmbeddingOverPlace.lean#L61) is a second name of `ladic_weight_at_embedding_over_place`. We read the proof of the theorem in full, but only the statements of the items of the proposition, and we did not unfold the definitions of $\nabla_\nu$, its action, or the highest weight vector.
