---
title: Local norms of ratios
decls:
  - GlobalTheory.LocTriv.ratio_local_norm_dpair
  - GlobalTheory.T.definitePairs_ratio_locally_rational_times_norm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local norms of ratios

Fix a definite pair $P_1$ with irreducible polynomial. Every definite pair $P$ with the same $\gamma$ and the same $c$ gives a ratio $\beta_P \beta_1^{-1}$. This ratio lies in the [[centralizer|02YYV36BFM]] of $\gamma$, which is a number field $L$ with an involution $c$. This section proves the local part of the finiteness argument of the next section. If the pairs $P$ have trivializations whose images lie in one compact set, then at almost all primes $\ell$ the ratio is a scalar times a norm $y\, c(y)$ from $\mathbb{Q}_\ell \otimes L$. The global count of such ratios modulo rational scalars and norms is then finite. That step is done in the [finiteness of classes in a compact set](/entry/finite-of-compact/).

We keep the unitary datum $\mathsf{G}$ and the notation of the first section. A prime means a prime number $\ell$, and $\mathbb{Q}_\ell$ is the $\ell$-adic field ([completions](/learn/number-fields/#places-and-completions)).

### The centralizer field

The next result is an input. It is proved in the formal development by the theory of the algebra $F[X]/(P_\gamma)$.

**Theorem 6.2.1 (Centralizer of an element of maximal degree).** Let $\gamma \in C^\times$ with $P_\gamma$ irreducible of degree $n$. Then there are a [[number field|MWBDFS2KJ5]] $L$ that is an $F$-algebra and an injective $F$-algebra map $j \colon L \to C$ such that $z \in C$ commutes with $\gamma$ if and only if $z = j(e)$ for some $e \in L$.

Lean: `GlobalTheory.CentIrr.centralizer_unit_eq_field`.

*Proof.* This is proved in the development from the algebra $F[X]/(P_\gamma)$ and the map that sends $X$ to $\gamma$; we take it as an input. $\square$

**Theorem 6.2.2 (Centralizer field).** Let $\beta, \gamma \in C^\times$ and $c_0 \in \mathbb{Q}^\times$ with $\beta^* = \beta$ and $\gamma \beta \gamma^* = c_0 \beta$. Assume that $P_\gamma$ is irreducible of degree $n$. Then there are a number field $L$, an injective $\mathbb{Q}$-algebra map $\iota \colon L \to C$ and a $\mathbb{Q}$-algebra map $c \colon L \to L$ with these properties:

1. $z \in C$ commutes with $\gamma$ if and only if $z = \iota(w)$ for some $w \in L$;
2. $\iota(c(x)) = \beta\, \iota(x)^* \beta^{-1}$ for all $x \in L$;
3. $c(c(x)) = x$ for all $x \in L$.

Lean: `GlobalTheory.T.exists_numberField_involution_similitudeCentralizer` (also `GlobalTheory.CentSim.centraliser_field_involution`).

*Proof.* Take $L$ and $\iota = j$ from the last theorem. Let $z$ commute with $\gamma$. From $\gamma \beta \gamma^* = c_0 \beta$ we get $\gamma \beta = c_0 \beta (\gamma^*)^{-1}$ and $\beta^{-1} \gamma = c_0 (\gamma^*)^{-1} \beta^{-1}$. Since $z^*$ commutes with $(\gamma^*)^{-1}$, a direct computation gives that $\beta z^* \beta^{-1}$ commutes with $\gamma$. So $\beta \iota(x)^* \beta^{-1} = \iota(c(x))$ for a unique $c(x) \in L$. The map $c$ is additive and sends $1$ to $1$. It is multiplicative because $x \mapsto x^*$ reverses products and $L$ is commutative. From $\beta^* = \beta$ we get $\beta (\beta \iota(x)^* \beta^{-1})^* \beta^{-1} = \iota(x)$, so $c \circ c$ is the identity, by injectivity of $\iota$. $\square$

### Integrality at a prime

Fix a $\mathbb{Q}$-basis $b$ of $C$ and a $\mathbb{Q}$-basis $b_L$ of $L$. For a prime $\ell$, an element of $\mathbb{Q}_\ell \otimes_{\mathbb{Q}} C$ is *$\ell$-integral* if its coordinates in the basis $1 \otimes b$ lie in $\mathbb{Z}_\ell$. The same definition with $b_L$ applies to $\mathbb{Q}_\ell \otimes_{\mathbb{Q}} L$. For $\ell \neq p$ and $g \in \mathbb{A}^p \otimes C$ we write $g_\ell$ for the image of $g$ in $\mathbb{Q}_\ell \otimes C$, and the same for $\mathbb{A}^p$. An algebra map $c \colon L \to L$ acts on $\mathbb{Q}_\ell \otimes L$ by $1 \otimes c$, and we keep the name $c$. The same holds for $\iota$.

The next five results are inputs. They are proved in other parts of the development, and each proof below says only this.

**Theorem 6.2.3 (Compact sets are integral almost everywhere).** Let $\Omega \subseteq G(\mathbb{A}^p)$ be [[compact|0TVJZYB6SH]]. Then for all but finitely many primes $\ell \neq p$, every $(g, \nu) \in \Omega$ has $g_\ell$ and $g_\ell^{-1}$ $\ell$-integral and $\nu_\ell, \nu_\ell^{-1} \in \mathbb{Z}_\ell$.

Lean: `GlobalTheory.OrbFinAf.cptInt`.

*Proof.* This is proved in the development from the continuity of the coordinate maps on $\mathbb{A}^p \otimes C$; we take it as an input. $\square$

**Theorem 6.2.4 (Products and the involution).** Let $C$ be a finite dimensional $\mathbb{Q}$-algebra, $x \mapsto x^*$ a ring map from $C$ to the opposite ring of $C$, and $b$ a $\mathbb{Q}$-basis of $C$. There is a finite set $S$ of primes such that for $\ell \notin S$ the product of two $\ell$-integral elements is $\ell$-integral, and $y^*$ is $\ell$-integral when $y$ is.

Lean: `GlobalTheory.T.eventually_adic_integral_span_closed_mul_star`.

*Proof.* This is an input from the development. $\square$

**Theorem 6.2.5 (Integral conjugators).** Let $\gamma \in C^\times$ with $P_\gamma$ separable of degree $n$. Let $L$ be a number field and $\iota \colon L \to C$ an injective $\mathbb{Q}$-algebra map whose image is the centralizer of $\gamma$. There is a finite set $S$ of primes such that for $\ell \notin S$ the following holds. If $X, X' \in (\mathbb{Q}_\ell \otimes C)^\times$ and $X \gamma X^{-1}$, $X' \gamma X'^{-1}$ are $\ell$-integral, then there is $m \in (\mathbb{Q}_\ell \otimes L)^\times$ such that $X \iota(m) X'^{-1}$ and $X' \iota(m^{-1}) X^{-1}$ are $\ell$-integral.

Lean: `GlobalTheory.T.eventually_integral_conjugators_differ_by_centralizer`.

*Proof.* This is an input from the development. $\square$

**Theorem 6.2.6 (Twisted integral elements).** Let $C$ be a finite dimensional $\mathbb{Q}$-algebra with a basis $b$, $L$ a number field with a basis $b_L$, and $\iota \colon L \to C$ an injective $\mathbb{Q}$-algebra map. There is a finite set $S$ of primes such that for $\ell \notin S$, all $X \in (\mathbb{Q}_\ell \otimes C)^\times$ and all $E \in \mathbb{Q}_\ell \otimes L$: if $X \iota(E) X^{-1}$ is $\ell$-integral, then $E$ is $\ell$-integral.

Lean: `GlobalTheory.T.almost_all_places_twisted_unit_integral`.

*Proof.* This is an input from the development. $\square$

**Theorem 6.2.7 (Fixed units are norms).** Let $L$ be a number field and $c \colon L \to L$ a $\mathbb{Q}$-algebra map with $c \circ c = \mathrm{id}$ and $c \neq \mathrm{id}$. There is a finite set $S$ of primes such that for $\ell \notin S$ the following holds. If $e \in (\mathbb{Q}_\ell \otimes L)^\times$ has $c(e) = e$ and $e, e^{-1}$ are $\ell$-integral, then $e = y\, c(y)$ for some $y \in (\mathbb{Q}_\ell \otimes L)^\times$.

Lean: `GlobalTheory.T.fixed_unit_eq_norm_almost_all_places`.

*Proof.* This is an input from the development. $\square$

The last tool is an identity in any ring.

**Lemma 6.2.8 (Self-dual identity).** Let $R$ be a commutative ring, $A$ an $R$-algebra and $B$ a commutative $R$-algebra. Let $\iota \colon B \to A$ be a ring map with $\iota(r) = r$ for $r \in R$, $x \mapsto x^\sigma$ a ring map from $A$ to the opposite ring of $A$, and $c \colon B \to B$ a ring map. Let $\beta_1, X, X_1 \in A^\times$, $t, t_1 \in R^\times$, $a' \in B$ and $m \in B^\times$. Assume
$$\iota(c(m)) = \beta_1\, \iota(m)^\sigma \beta_1^{-1}, \qquad X \iota(a') \beta_1 X^\sigma = t, \qquad X_1 \beta_1 X_1^\sigma = t_1.$$
Let $u = X \iota(m) X_1^{-1}$ and $E = t^{-1} t_1\, a'\, m^{-1} c(m^{-1})$. Then $u \cdot X_1 \iota(E) X_1^{-1} \cdot u^\sigma = 1$.

Lean: `GlobalTheory.LocTriv.selfDual_conj_eq_one`.

*Proof.* From $X_1 \beta_1 X_1^\sigma = t_1$ we get $X_1^{-1} (X_1^{-1})^\sigma = t_1^{-1} \beta_1$, since $(X_1^{-1})^\sigma$ is the inverse of $X_1^\sigma$. The first assumption gives $\beta_1 \iota(m)^\sigma = \iota(c(m)) \beta_1$. Hence
$$\begin{aligned} u\, X_1 \iota(E) X_1^{-1}\, u^\sigma &= X \iota(m) \iota(E)\, X_1^{-1} (X_1^{-1})^\sigma\, \iota(m)^\sigma X^\sigma \\ &= t_1^{-1}\, X\, \iota(m E\, c(m))\, \beta_1 X^\sigma. \end{aligned}$$
Since $B$ is commutative, $m E c(m) = t^{-1} t_1 a'$. So the product is $t^{-1} X \iota(a') \beta_1 X^\sigma = t^{-1} t = 1$. $\square$

### The ratio theorem

**Theorem 6.2.9 (Ratios are local norms up to scalars).** Let $\Omega \subseteq G(\mathbb{A}^p)$ be compact and $P_1 = (\beta_1, \gamma_1, c_1)$ a definite pair. Let $L$ be a number field, $\iota \colon L \to C$ an injective $\mathbb{Q}$-algebra map and $c \colon L \to L$ a $\mathbb{Q}$-algebra map. Assume that $z \in C$ commutes with $\gamma_1$ if and only if $z \in \iota(L)$, and that $\iota(c(x)) = \beta_1 \iota(x)^* \beta_1^{-1}$ for all $x$. Then there is a finite set $S$ of primes with the following property. Let $P$ be a definite pair with $\gamma_P = \gamma_1$ and $c_P = c_1$, and with a trivialization $(x, t)$ such that $(x \gamma_P x^{-1}, c_P) \in \Omega$. Let $a \in L$ with $\iota(a) = \beta_P \beta_1^{-1}$. Then for each prime $\ell \notin S$ there are $r \in \mathbb{Q}_\ell^\times$ and $y \in (\mathbb{Q}_\ell \otimes L)^\times$ with
$$1 \otimes a = r\, y\, c(y).$$

Lean: `GlobalTheory.T.definitePairs_ratio_locally_rational_times_norm` (also `GlobalTheory.LocTriv.ratio_local_norm_dpair`).

*Proof.* First, $c \circ c = \mathrm{id}$. Indeed, $\iota(c(c(x))) = \beta_1 (\beta_1 \iota(x)^* \beta_1^{-1})^* \beta_1^{-1} = \iota(x)$ by $\beta_1^* = \beta_1$, and $\iota$ is injective. Second, $c \neq \mathrm{id}$. Take an embedding $\tau$ of $F$ and $f \in E$ with $\operatorname{Im} \tau(f) \neq 0$. Then the complex conjugate $\bar f$ of $f$ in the CM field $F$ is not $f$. Since $f$ is central, $f = \iota(w)$ for some $w$, and $\iota(c(w)) = \beta_1 f^* \beta_1^{-1} = \bar f$, so $c(w) \neq w$.

Fix a trivialization $(x_1, t_1)$ of $P_1$. Let $S$ be the union of $\{p\}$ and of these six finite sets: the set of the theorem on compact sets for $\Omega$; the same for the one point $(x_1 \gamma_1 x_1^{-1}, c_1)$; the sets of the theorems on products, on integral conjugators for $\gamma_1$, on twisted integral elements, and on fixed units for $c$.

Let $P$, $(x, t)$, $a$ and $\ell \notin S$ be as in the statement. Let $X = x_\ell$, $X_1 = (x_1)_\ell$, $T = t_\ell$ and $T_1 = (t_1)_\ell$. The $\ell$-components of $x \gamma_1 x^{-1}$ and $x_1 \gamma_1 x_1^{-1}$ are $X \gamma_1 X^{-1}$ and $X_1 \gamma_1 X_1^{-1}$, and they are $\ell$-integral by the choice of $S$. The theorem on integral conjugators gives $m \in (\mathbb{Q}_\ell \otimes L)^\times$ such that $u = X \iota(m) X_1^{-1}$ and $u^{-1} = X_1 \iota(m^{-1}) X^{-1}$ are $\ell$-integral.

Since $\iota(a) \beta_1 = \beta_P$, the trivializations give $X \iota(a) \beta_1 X^* = T$ and $X_1 \beta_1 X_1^* = T_1$. The second condition on $c$ gives $\iota(c(m)) = \beta_1 \iota(m)^* \beta_1^{-1}$. Let $E = T^{-1} T_1\, a\, m^{-1} c(m^{-1})$, a unit of $\mathbb{Q}_\ell \otimes L$, and $W = X_1 \iota(E) X_1^{-1}$. The self-dual identity gives $u W u^* = 1$, so
$$W = u^{-1} (u^{-1})^*, \qquad W^{-1} = X_1 \iota(E^{-1}) X_1^{-1} = u^* u.$$
Both are $\ell$-integral by the theorem on products. The theorem on twisted integral elements then gives that $E$ and $E^{-1}$ are $\ell$-integral.

Next, $c(a) = a$. Indeed, $\iota(c(a)) = \beta_1 (\beta_P \beta_1^{-1})^* \beta_1^{-1} = \beta_1 \beta_1^{-1} \beta_P \beta_1^{-1} = \iota(a)$, by $\beta_1^* = \beta_1$ and $\beta_P^* = \beta_P$. Since $c$ fixes scalars and $c \circ c = \mathrm{id}$, we get $c(E) = T^{-1} T_1\, a\, c(m^{-1})\, m^{-1} = E$. The theorem on fixed units gives $y_0$ with $E = y_0\, c(y_0)$. Then
$$1 \otimes a = T T_1^{-1}\, m\, c(m)\, E = T T_1^{-1}\, (m y_0)\, c(m y_0).$$
Take $r = T T_1^{-1}$ and $y = m y_0$. $\square$

The hypothesis $c_P = c_1$ is not used in the proof. The next section applies the theorem with $L$, $\iota$ and $c$ from the theorem on the centralizer field.

**Remark 6.2.10 (Formalization).** In [DefinitePairsRatioLocallyRationalTimesNorm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DefinitePairsRatioLocallyRationalTimesNorm.lean#L18) the primes are the height one primes of $\mathbb{Z}$, and $\ell$-integrality is the predicate `GlobalTheory.AdicSpan.IsIntB` for the bases `Module.finBasis`. The theorem does not assume $c \circ c = \mathrm{id}$; it proves it at line 31, and it proves $c \neq \mathrm{id}$ at line 34 from the subfield $E$ of the datum. The hypothesis $c_P = c_1$ is introduced at line 57 and is never used. The name of the theorem says "locally rational times norm", but the scalar $r$ is in $\mathbb{Q}_\ell^\times$, not in $\mathbb{Q}^\times$. The public statement is a wrapper with the same statement. Four of the five inputs on integrality are also wrappers, of `GlobalTheory.AdicSpan.isIntB_mul_star_eventually`, `GlobalTheory.LatStep.lattice_step`, `GlobalTheory.LocIntSpan.isIntB_of_isIntB_conj` and `GlobalTheory.LocNorm.unit_fixed_is_norm`; `GlobalTheory.OrbFinAf.cptInt` has its own proof. We opened their statements, not their proofs. The theorem on twisted integral elements has one finite set $S$ for all units $X$ at once. This is a strong form, and we did not check its proof. The theorem on the centralizer field is a wrapper of `GlobalTheory.CentSim.centraliser_field_involution`, whose proof we read.
