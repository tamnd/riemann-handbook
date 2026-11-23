---
title: Products of short rules and theta rules
decls:
  - GlobalTheory.ShortTimesTheta.mul_mem_span
  - GlobalTheory.ShortTimesTheta.short_mul_theta_mem_span
  - GlobalTheory.FormTies.productsShort_rec
  - GlobalTheory.FormTies.leaves_sup_span_lemmaS_of_formTieK
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Products of short rules and theta rules

This section proves that the product of a short rule and a theta rule on a unitary moduli space is an integral combination of short rules. By induction, products of a short rule with any number of theta rules stay in the integral span of short rules. The result gives the three lattice conditions at the leaves of the indefinite tree: the modules of cusp forms, of theta products and of short products are lattices, they are stable under the level group, and the module of theta products lies in a scaled copy of the module of short products. These conditions are used in the [leaf data of Volume 15](/entry/leaves-sup-span-data/).

### Rules, theta rules and short rules

We use the unitary moduli spaces of the earlier chapters of this volume without repeating their construction. Let $E$ be a CM field with a host datum, let $D_w$ be a Hermitian datum of signature $(p, q)$ with lattice $\Lambda_w$, let $l$ be a level of odd modulus $M \geq 3$, let $X$ be the moduli space of level $l$, and let $c$ be a coefficient datum with field $F_c$. A *rule* is a compatible family of values at the frame points of $X$ over all $F_c$-algebras. Rules form an $F_c$-algebra. A *weight* $a$ assigns a natural number to each pair of an embedding $\tau : E \to \mathbb{C}$ and an index $i$. For a weight $a$ and $n \geq 0$ the rules of weight $a$ in $n$ columns form an $F_c$-space $\mathrm{sec}(a, n)$.

**Definition 4.4.1.** A *theta rule* of weight $a$ in $n$ columns is a rule $f$ for which there are columns $x \in \Lambda_w^n$ and a harmonic polynomial $P$ of weight $a$ in $n$ columns such that the value of $f$ at every frame point is the theta value of $P$ at the columns $x$.

A *covering datum* $\delta$ in $n$ columns consists of an integer $p_\delta$, an ideal $I$ of $\mathcal{O}_E$, a second level $l_2$ whose modulus is a multiple of $M$, a moduli space $X_2$ of level $l_2$ with a map to $X$, a coefficient datum $c_2$ with an isomorphism $F_{c_2} \cong F_c$, and a function $\varphi_\delta$ on $(\Lambda_w / l_2)^n$ with values in $F_c$. Changing only $\varphi_\delta$ to a function $\varphi'$ in $n'$ columns gives a covering datum in $n'$ columns, written $\delta[\varphi']$.

**Definition 4.4.2.** A *short rule* of weight $a$ in $n$ columns for $\delta$ is a rule $f \in \mathrm{sec}(a, n)$ for which there are a unimodular Hermitian lattice $\Lambda$ of rank $n$, trivial at the bad primes and at the modulus of $l_2$, an integer $N$ adapted to $\Lambda$ and $l_2$, admissible columns $x_0 \in \Lambda_w^n$, and a harmonic polynomial $P$ of weight $a$ for $\Lambda$, with the following property. At every frame point $y$ of $X$ over an algebraically closed field and every point $y_2$ of $X_2$ over $y$, the value of $f$ at $y$ is the value of a fixed rule $c_\delta$ at $y_2$ times the short theta value of $(\Lambda, N, x_0, P)$ at $y_2$. The short value is the average over $(\Lambda_w/l_2)^n$ of the theta values of $P$ weighted by $\varphi_\delta$ and normalized by a nonzero constant $\beta(\Lambda)$.

### One factor

**Lemma 4.4.3 (one theta factor, general form).** Let $\delta$ be a covering datum in $n$ columns of level type, with the harmonic structures at both levels, and let $m \geq 0$. Let $\zeta \in F_c$ be a root of unity and let $\varphi'$ be the function on $(\Lambda_w/l_2)^{n+m}$ given by
$$\varphi'(q) = \zeta\, \varphi_\delta(q_1, \dots, q_n) \cdot \begin{cases} c_I^m & \text{if } q_{n+1}, \dots, q_{n+m} \in I \Lambda_w, \\ 0 & \text{otherwise.} \end{cases}$$
Here $c_I$ is the order of $\Lambda_w / I \Lambda_w$. Assume that $n = n_V$ implies $m = 0$, and that every unimodular lattice $\Lambda$ that is trivial at the bad primes has a nonzero normalizing constant $\beta(\Lambda)$ with the expected ideal and absolute values. Let $a, a'$ be weights, and assume that every short datum of weight $a + a'$ in $n + m$ columns for $\delta[\varphi']$ has a unique short value and a short rule. Let $g$ be a short rule of weight $a$ in $n$ columns for $\delta$, and let $f$ be a theta rule of weight $a'$ in $m$ columns. Then $g f$ lies in the $\mathcal{O}_{F_c}$-span of the short rules of weight $a + a'$ in $n + m$ columns for $\delta[\varphi']$.

Lean: `GlobalTheory.ShortTimesTheta.mul_mem_span`.

*Proof.* Let $g$ come from $(\Lambda, N, x_0, P')$ and $f$ from $(x, P)$. Put $\Lambda' = \Lambda \oplus \mathcal{O}_E^m$, the block sum with the standard unimodular lattice. The block product $P' \otimes P$ is a harmonic polynomial of weight $a + a'$ for $\Lambda'$. For each $x' \in (\Lambda_w / l)^m$ the columns $(x_0, x')$ are admissible, so the hypothesis gives a short rule $F_{x'}$ for $(\Lambda', N, (x_0, x'), P' \otimes P)$. The normalizing constants satisfy $\beta(\Lambda') = \zeta' \beta(\Lambda)$ for a root of unity $\zeta'$. Let $\zeta_M$ be the root of unity of the level pairing and put $c(x') = \zeta' \zeta^{-1} \zeta_M^{-\langle x', p_\delta x \rangle}$. These numbers are algebraic integers. We claim
$$g f = \sum_{x'} c(x') F_{x'}.$$
Two rules are equal if their values agree at every frame point over every algebraically closed field. At such a point, the value of $f$ is a theta value at the columns $x$. It equals a short value at level $l_2$ with the weight that is concentrated at the class of $p_\delta x$. The short value of the block product is the product of the two short values. A character sum over $(\Lambda_w/l)^m$ writes the concentrated weight as a combination of characters, and the definition of $\varphi'$ turns this into the sum over $x'$. So the values agree. Each $c(x')$ is integral, so $g f$ lies in the span. $\square$

**Proposition 4.4.4 (short times theta).** Let $T$ be a tower of moduli data for $D$ with the projective laws and the short laws, let $j$ be an index in the range of $D$, and assume that all covering data of $T$ at $j$ differ only in their function $\varphi$, and that the level $l_2$ of the covering datum in $0$ columns has $A = 1$. Assume the chart independence statement. Let $w, w_L$ be weights at $j$ with $r \leq n(w)$, where $r$ is the rank of $D$, and such that $n(w) = n_V$ implies $n(w_L) = 0$. Then for every short rule $g$ of weight $w$ and every theta rule $f$ of weight $w_L$ of $T$ at $j$, the product $g f$ lies in the $\mathcal{O}_{F_c}$-span of the short rules of weight $w + w_L$.

Lean: `GlobalTheory.ShortTimesTheta.short_mul_theta_mem_span`.

*Proof.* If $X$ has no frame point over any algebraically closed field, then $g f = 0$, which lies in the span. Otherwise fix such a point $y$. The covering data in $n(w)$ and in $n(w) + n(w_L)$ columns are $\delta[\varphi_0]$ and $\delta[\varphi']$ for the same $\delta$. The signature satisfies $p + q = r \geq 1$. The cover characters of the two covering data agree, because a cover character is unique once a point $y_2$ over $y$ exists. Then the comparison of coefficients in more columns gives a root of unity $\zeta$ with $\varphi'$ of the form of the lemma. The short laws of $T$ give the normalizing constants and the short rules in $n(w) + n(w_L)$ columns. The lemma applies. $\square$

### Many factors and the leaves

For weights $\kappa, w_L, w_F$ and $T_n \geq 0$, the *theta products* are the sum of three modules: $T_n$-fold products of theta rules of weight $w_L$ times short rules of weight $w_F$; $(T_n - \dim Y)$-fold products of theta rules times short rules of weight $w_F + (\dim Y) w_L$; and the short rules of weight $\kappa$. Here $\dim Y$ depends on $D$ and $j$.

**Corollary 4.4.5 (products of short rules).** Under the hypotheses of the proposition, let $\kappa, w_L, w_F$ be weights and $T_n \geq 0$, with $w_F = \kappa - T_n w_L$ in each entry, $n(\kappa) = n(w_F) + T_n\, n(w_L)$, $\dim Y \leq T_n$, $r \leq n(w_F)$ and $n(\kappa) = n_V$. Then the theta products lie in the module of short rules of weight $\kappa$.

Lean: `GlobalTheory.FormTies.productsShort_rec`.

*Proof.* Apply the proposition once for each theta factor, by induction on the number of factors. Each step keeps the number of columns at least $r$. $\square$

**Theorem 4.4.6 (lattices at the leaves).** Assume the chart independence statement. Let $O$ be a leaf object over a number field $K$ for indefinite data $S$, with a finite group $P$ acting. Assume that for every place $v$ of $K$ and every index $i$ there are a full tower $T$ with the projective laws, an index $j$, an integer $p > 0$ and an identification $z$ of the coordinates of $O$ at $i$ with cusp forms of weight $\kappa$ at $j$, such that: the lattice, the action, the theta products, the scalar and the short products of $O$ at $(v, i)$ are the images under $z$ of the corresponding objects of $T$; the action of $P$ comes from the level group; $T$ has the full laws; the character $\xi$ is trivial on the determinants of the theta group; all covering data at $j$ differ only in $\varphi$; and the lattice, span and second harmonic conditions hold at $j$. Then:
1. for every $i$, the module $O.M_i$ is a lattice and is stable under $P$;
2. for every place $w$ of the twisted set of $S$, and for $\bar w$, the modules $O.\Theta_{w,i}$ and $O.\Theta^K_{w,i}$ are lattices;
3. for the same places, $O.\Theta_{w,i} \subseteq O.M_i$, the module $O.\Theta_{w,i}$ is stable under $P$, the scalar $\sigma_{w,i}$ is nonzero, and $O.\Theta_{w,i} \subseteq \sigma_{w,i} \cdot O.\Theta^K_{w,i}$.

Here a lattice is a finitely generated $\mathcal{O}_K$-module that spans the whole coordinate space over $K$.

Lean: `GlobalTheory.FormTies.leaves_sup_span_lemmaS_of_formTieK`.

*Proof.* Fix $v$ and $i$ and take the data of the hypothesis. The weights $\kappa, w_L, w_F$ of the run satisfy the four conditions of the corollary. The module of short theta rules of weight $w_F$ is finitely generated, and the corollary shows that the theta products lie in the short products. So the tie of $O$ with $T$ holds in the form that contains the theta products. Three lemmas then give the three claims at $(v, i)$: the lattice and its stability under the level action, the lattice property of the two theta modules, and the inclusions with the scalar $\sigma$, where the level action preserves the theta products because $\xi$ is trivial on the determinants. Claims 2 and 3 follow by applying this at $w$ and at $\bar w$. Claim 1 does not depend on the place, so we apply it at any one place $v_0$ of $K$. $\square$

**Remark 4.4.7 (Formalization).** The general lemma and the proposition are in one module, [ShortMulThetaMemSpan.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ShortMulThetaMemSpan.lean#L243). The corollary is one application of a recursion lemma to the proposition. The objects $O.M_i$, $O.\Theta_{w,i}$, $O.\Theta^K_{w,i}$ and $\sigma_{w,i}$ are the components of the leaf object.
