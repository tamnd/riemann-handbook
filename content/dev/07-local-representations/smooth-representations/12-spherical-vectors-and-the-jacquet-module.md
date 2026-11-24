---
title: Spherical vectors and the Jacquet module
decls:
  - GlobalTheory.T.satake_power_nonvanishing
  - GlobalTheory.CompanionTheory.SatPow.satPowNonvan
  - GlobalTheory.T.unitary_jacquet_nonzero
  - GlobalTheory.CompanionTheory.JacSph.jacNeU
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Spherical vectors and the Jacquet module

Let $\rho$ be an unramified representation of the unitary group $G$ of the previous two sections, with Satake parameter $\alpha$. This section proves that the spherical vector of $\rho$ does not lie in the kernel of the map to the Jacquet module for the Borel subgroup. By Frobenius reciprocity this gives an embedding of $\rho$ into a principal series, and the swap and inverse reductions then move its parameters into a fixed order. Both steps serve [Theorem 7.3.4 of Volume 8](/entry/extreme-u/). The main tool is a nonvanishing statement for the Satake transform of the powers of one strictly dominant double coset. The argument is that of Casselman: a vector in the kernel of the Jacquet map is killed by a power of an Iwahori Hecke operator. For background see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Hecke operators and Satake parameters

We keep the unramified setting and the notation $L$, $\sigma$, $\varpi$, $q$, $G$, $K$, $B$, $N$, $m = \lfloor n/2 \rfloor$, $\chi_\alpha$, $I(\alpha)$ of Section 10. For $a \in \mathbb{Z}^m$ let $t_a$ be the diagonal matrix with entry $\varpi^{a_i}$ in place $i$ and $\varpi^{-a_i}$ in place $n + 1 - i$, for $1 \leq i \leq m$, and $1$ elsewhere.

**Definition 1.12.1 (Hecke algebra).** The *Hecke algebra* $\mathcal{H}$ is the space of functions $h \colon G \to \mathbb{C}$ that are invariant under $K$ on both sides and vanish outside finitely many double cosets $KgK$. For $g \in G$ let $\mathbf{1}_{KgK} \in \mathcal{H}$ be the indicator function of $KgK$. For a representation $\rho$ of $G$ on $V$, $h \in \mathcal{H}$ and $x \in V$ put
$$h \cdot x = \sum_{c \in G/K} h(c)\,\rho(c)x,$$
a finite sum when $x \in V^K$ (the sum is over representatives $c$; it does not depend on them).

**Definition 1.12.2 (Satake transform).** For $h \in \mathcal{H}$ and $\alpha \in \mathbb{C}^m$ put
$$S(h, \alpha) = \sum_{a \in \mathbb{Z}^m}\ \prod_{i=1}^m \alpha_i^{a_i}\,q^{-a_i(n+1-2i)} \sum_{\substack{c \in G/K \\ c \in t_a N K}} h(c).$$

This is the classical Satake transform. The inner sum is the integral of $h$ over the coset $t_aN$, and the factor $q^{-a_i(n+1-2i)}$ comes from the square root of the modulus character of $B$.

**Definition 1.12.3 (Satake vector).** Let $\rho$ be a representation of $G$ on $V$ and $\alpha \in (\mathbb{C}^\times)^m$. A vector $x \in V$ is a *Satake vector with parameter $\alpha$* if $x \neq 0$, $x \in V^K$, and $h \cdot x = S(h, \alpha)\,x$ for all $h \in \mathcal{H}$. We say that $\rho$ *has Satake parameter $\alpha$* if $V^K \neq 0$ and every nonzero $x \in V^K$ is a Satake vector with parameter $\alpha$.

**Definition 1.12.4 (Strictly dominant).** A diagonal $t \in G$ is *strictly dominant* if $\mathrm{ord}(t_{jj}) < \mathrm{ord}(t_{ii})$ whenever $i < j$.

**Definition 1.12.5 (Jacquet kernel).** For a representation $\rho$ of $G$ on $V$ let $V(N)$ be the span of the vectors $\rho(u)v - v$ with $u \in N$ and $v \in V$. The quotient $V/V(N)$ is the Jacquet module for $B$.

### The Satake transform of dominant powers

**Theorem 1.12.6 (Nonvanishing of Satake powers).** Assume the unramified setting. Let $\alpha \in (\mathbb{C}^\times)^m$, let $t \in G$ be diagonal and strictly dominant, and let $j_0 \geq 0$. Then there is $j \geq j_0$ with $S(\mathbf{1}_{Kt^jK}, \alpha) \neq 0$.

Lean: `GlobalTheory.CompanionTheory.SatPow.satPowNonvan` (also `GlobalTheory.T.satake_power_nonvanishing`, the same statement).

We take the following facts as given; they are proved elsewhere in the development. Let $I \subseteq K$ be the Iwahori subgroup. A *permutation element* is an element $w \in G$ with the pattern of a permutation $\pi$ of $\{1, \dots, n\}$; it is determined by $\pi$. For strictly dominant $t$, each $\pi$ has a weight $\mathrm{wt}_t(\pi) \in \mathbb{Z}$.

**Theorem 1.12.7 (Inputs on the Iwahori subgroup).** Assume the unramified setting and let $t$ be diagonal and strictly dominant.

- (i) $K$ is open and compact, $I \leq K$, and $K/I$ is finite.
- (ii) There is a finite set $R \subseteq I$ with $1 \in R$ such that every $\iota \in I$ has exactly one $r \in R$ with $t^{-1}r^{-1}\iota\,t \in I$, and $t^k r t^{-k} \in K$ for all $r \in R$ and $k \geq 0$.
- (iii) Every $g \in G$ is $b\,w\,\iota$ with $b \in B$, $w$ a permutation element and $\iota \in I$.
- (iv) Let $w$ and $w'$ be permutation elements for $\pi$ and $\pi'$, let $r \in I$, and let $w\,r\,t = b\,w'\,\iota$ with $b \in B$ and $\iota \in I$. Then either $\mathrm{wt}_t(\pi') < \mathrm{wt}_t(\pi)$, or $\pi' = \pi$ and $b$ has the same diagonal orders as $w t w^{-1}$.
- (v) There is a right $K$-invariant $\varphi_0 \in I(\alpha)$ with $\varphi_0(1) = 1$ and, for all $h \in \mathcal{H}$, $\sum_{c \in G/K} h(c)\varphi_0(c) = S(h, \alpha)$.
- (vi) Put $A\varphi(g) = \sum_{r \in R}\varphi(grt)$. For each $j$ there is an integer $M > 0$ such that for every right $K$-invariant $\psi$,
$$\sum_{c \in K/I}(A^j\psi)(c) = M\sum_{x \in G/K}\mathbf{1}_{Kt^jK}(x)\,\psi(x).$$

Fact (vi) says that $A$ is the Iwahori Hecke operator of $ItI$, and that the $j$-th power of $ItI$ is $It^jI$ (this is where (ii) is used), which meets $Kt^jK$ with a fixed multiplicity.

*Proof of the theorem.* Let $W$ be the space of $\varphi \in I(\alpha)$ that are right invariant under $I$. By (iii), $\varphi \in W$ is determined by its values on the finitely many permutation elements, so $W$ is finite-dimensional.

*Step 1: $A$ preserves $W$.* Left $B$-equivariance of $A\varphi$ is clear. For right $I$-invariance, let $\iota \in I$. For each $r \in R$, (ii) gives $r' \in R$ with $t^{-1}r'^{-1}\iota r\,t \in I$, and $r \mapsto r'$ is injective, hence a bijection of $R$. Then $\varphi(g\iota rt) = \varphi(gr't)$, so $A\varphi(g\iota) = A\varphi(g)$.

*Step 2: $A$ is injective on $W$.* Let $\varphi \in W$ be nonzero with $A\varphi = 0$. By (iii), $\varphi(w) \neq 0$ for some permutation element $w$. Take such $w$, for a permutation $\pi$, with $\mathrm{wt}_t(\pi)$ least. Put $x = \chi_\alpha(wtw^{-1})\varphi(w)$. Note that $wtw^{-1}$ is diagonal, so $x \neq 0$, and $\varphi(w \cdot 1 \cdot t) = \varphi(wtw^{-1}\,w) = x$. For $r \in R$ write $wrt = bw'\iota$ by (iii). By (iv), either the weight drops, and then $\varphi(w') = 0$ by minimality, so $\varphi(wrt) = 0$; or $w' = w$ and $\chi_\alpha(b) = \chi_\alpha(wtw^{-1})$, so $\varphi(wrt) = x$. Hence $0 = A\varphi(w) = e\,x$, where $e \geq 1$ counts the $r$ of the second kind, and $r = 1$ is one of them. This is a contradiction.

*Step 3: a functional.* Let $l(\varphi) = \sum_{c \in K/I}\varphi(c)$ on $W$. The function $\varphi_0$ of (v) lies in $W$, and $l(\varphi_0) = |K/I| \neq 0$, as $\varphi_0 = 1$ on $K$.

*Step 4: conclusion.* Suppose $S(\mathbf{1}_{Kt^jK}, \alpha) = 0$ for all $j \geq j_0$. By (v) and (vi), $l(A^j\varphi_0) = M \cdot S(\mathbf{1}_{Kt^jK}, \alpha) = 0$ for $j \geq j_0$. As $A$ is injective on the finite-dimensional $W$, it is invertible, and by the theorem of Cayley and Hamilton $A^{-j_0}$ is a polynomial $p(A)$. So $\varphi_0 = p(A)A^{j_0}\varphi_0$ is a combination of the $A^j\varphi_0$ with $j \geq j_0$, and $l(\varphi_0) = 0$. This contradicts Step 3. $\square$

### The spherical vector is not in the Jacquet kernel

**Theorem 1.12.8 (Spherical vectors survive in the Jacquet module).** Assume the unramified setting. Let $\rho$ be an irreducible admissible representation of $G$ on $V$ with Satake parameter $\alpha \in (\mathbb{C}^\times)^m$. Then there is $y \in V$ with $y \notin V(N)$ and $\rho(k)y - y \in V(N)$ for every diagonal $k \in K$.

Lean: `GlobalTheory.CompanionTheory.JacSph.jacNeU` (also `GlobalTheory.T.unitary_jacquet_nonzero`, the same statement).

We take the following facts as given. The first three are proved elsewhere in the development; the fourth is a theorem of Casselman.

**Theorem 1.12.9 (Inputs on Iwahori fixed vectors).** Assume the unramified setting, and let $\rho$ be a smooth representation of $G$ on $V$.

- (i) There is a diagonal strictly dominant $t_0 \in G$. It contracts $I \cap N$ under conjugation and expands $I \cap \bar N$, where $\bar N$ is the lower unipotent group.
- (ii) There is a linear operator $U$ on $V^I$ with $f(\rho(t_0)v) = f(Uv)$ for every $v \in V^I$ and every linear form $f$ on $V$ invariant under $I$. Then also $f(\rho(t_0^j)v) = f(U^jv)$ for all $j$.
- (iii) For $v \in V^K$ with $v \neq 0$ there is a linear form $l$ on $V$, invariant under $K$, with $l(v) = 1$.
- (iv) If $v \in V^I$ lies in $V(N)$, then $U^{j_0}v = 0$ for some $j_0$.

Fact (iv) is the key lemma of Casselman: the kernel of the Jacquet map on $V^I$ is the generalized kernel of the dominant Iwahori Hecke operator. Fact (iii) comes from averaging over the compact group $K$.

*Proof.* Let $v_0$ be a Satake vector with parameter $\alpha$, and put $y = v_0$. As $v_0 \in V^K$, $\rho(k)y - y = 0$ for every $k \in K$, so the second claim holds.

Suppose $v_0 \in V(N)$. As $I \leq K$, $v_0 \in V^I$. By (iv), $U^{j_0}v_0 = 0$ for some $j_0$. Let $l$ be the form of (iii) with $l(v_0) = 1$. By the theorem on Satake powers there is $j \geq j_0$ with $S(\mathbf{1}_{Kt_0^jK}, \alpha) \neq 0$. By (ii), applied to $l$, which is invariant under $I$,
$$l(\rho(t_0^j)v_0) = l(U^jv_0) = 0.$$
On the other side, $v_0$ is a Satake vector, so $\mathbf{1}_{Kt_0^jK} \cdot v_0 = S(\mathbf{1}_{Kt_0^jK}, \alpha)v_0$. The left side is the sum of $\rho(c)v_0$ over the $d$ cosets $c \in Kt_0^jK/K$, and $d$ is finite because $K$ is open and compact. Each $c$ is $k\,t_0^j$ with $k \in K$, and $l$ is $K$-invariant, so applying $l$ gives
$$d \cdot l(\rho(t_0^j)v_0) = S(\mathbf{1}_{Kt_0^jK}, \alpha)\,l(v_0) = S(\mathbf{1}_{Kt_0^jK}, \alpha).$$
The left side is $0$ and the right side is not. This is a contradiction, so $v_0 \notin V(N)$. $\square$

The theorem gives a nonzero vector in the Jacquet module $V/V(N)$ on which the compact part of the torus acts trivially. Frobenius reciprocity then gives a nonzero $G$-map from $V$ into an unramified principal series, which is injective as $V$ is irreducible. This is the starting point of [Theorem 7.3.4 of Volume 8](/entry/extreme-u/).

**Remark 1.12.10 (Formalization).** The statements `SatPowNonvan` and `JacNeU` are in [SatPowNonvan.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/UnitaryExtremality/SatPowNonvan.lean#L32). The Satake transform is `SatU` and $t_a$ is `tMat`, in [StatementF.lean](lean:Formalism/SatakeDualWeyl/StatementF.lean#L50); its index runs from $0$, with the exponent $n - 1 - 2i$. The abstract core of the first proof is `abs_main` (L49 of [SatakePowerNonvanishing.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SatakePowerNonvanishing.lean#L49)), with `aOp_inj` and `finiteDimensional_iwFix`. In the second theorem, irreducibility of $\rho$ is assumed but not used, and of admissibility only smoothness (`hadm.1`) is used ([UnitaryJacquetNonzero.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitaryJacquetNonzero.lean#L33)). The witness is the spherical vector, so the condition on diagonal $k$ holds for all $k \in K$. We have not unfolded the weight `permWt`.
