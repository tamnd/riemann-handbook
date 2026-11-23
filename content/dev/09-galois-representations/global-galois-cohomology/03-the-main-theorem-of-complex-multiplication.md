---
title: The main theorem of complex multiplication
decls:
  - GroundTheory.Global.Elliptic.exists_uniformization_level
  - GroundTheory.Global.Elliptic.main_theorem_complexMultiplication
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The main theorem of complex multiplication

This section proves the main theorem of complex multiplication of Shimura. Let $K$ be an imaginary quadratic field and let $E$ be an [[elliptic curve|427N6S6QQW]] over $\mathbb{C}$ with complex multiplication by the ring of integers of $K$. An automorphism $\sigma$ of $\mathbb{C}$ over $K$ acts on $E$ and on its torsion points. The theorem computes this action through an idele $s$ that corresponds to $\sigma$ on the maximal abelian extension of $K$ under the reciprocity law of the previous section. We first prove the theorem on the torsion points of a fixed level $m$, and then pass to all torsion points. The step [EveryCharacter from Row0b](/step/every-character-of-row/) depends on the theorem, through the Galois representations attached to Hecke characters of imaginary quadratic fields.

Background is in [lattices and the Weierstrass function](/learn/elliptic-curves/#lattices-and-the-weierstrass-function), [elliptic curves and the $j$-invariant](/learn/elliptic-curves/#elliptic-curves-and-the-j-invariant), [complex multiplication](/learn/elliptic-curves/#complex-multiplication) and [the main theorem of complex multiplication](/learn/theta-functions-cm/#the-main-theorem-of-complex-multiplication).

### Setting

Throughout, $K$ is a [[number field|MWBDFS2KJ5]] of degree $2$ over $\mathbb{Q}$ that is totally complex, with ring of integers $\mathcal{O}_K$, and with a fixed embedding $K \subseteq \mathbb{C}$. Let $\bar K$ be the algebraic closure of $K$ in $\mathbb{C}$ and $K^{\mathrm{ab}} \subseteq \bar K$ the maximal abelian extension. Write $[\,\cdot\,, K] : C_K \to \operatorname{Gal}(K^{\mathrm{ab}}/K)$ for the Artin map, built from the reciprocity law.

A fractional ideal $\mathfrak{a}$ of $K$ is a lattice in $\mathbb{C}$. An *analytic uniformization* of a Weierstrass curve $E$ over $\mathbb{C}$ with lattice $\Lambda$ is a surjective homomorphism $f : \mathbb{C} \to E(\mathbb{C})$ with kernel $\Lambda$ that is analytic near each point: in affine coordinates away from $\Lambda$, and in the coordinates at infinity near $\Lambda$. So $f$ induces an analytic isomorphism $\mathbb{C}/\Lambda \cong E(\mathbb{C})$, given by the [[Weierstrass function|361NAK68QK]] and its derivative after a change of variables.

An idele $s \in I_K$ acts on fractional ideals: $s\mathfrak{a}$ is the fractional ideal with $\operatorname{ord}_v(s\mathfrak{a}) = \operatorname{ord}_v(s_v) + \operatorname{ord}_v(\mathfrak{a})$ at each finite place $v$. It also acts on quotients. The group $K/\mathfrak{a}$ is the direct sum of the local quotients $K_v/\mathfrak{a}_v$. Multiplication by $s_v$ maps $K_v/\mathfrak{a}_v$ onto $K_v/s_v\mathfrak{a}_v$, and the sum of these maps is an isomorphism of $\mathcal{O}_K$-modules
$$s : K/\mathfrak{a} \xrightarrow{\ \sim\ } K/s\mathfrak{a}.$$
For an automorphism $\sigma$ of $\mathbb{C}$, write $E^\sigma$ for the curve with the coefficients of $E$ moved by $\sigma$, and $P \mapsto P^\sigma$ for the induced map $E(\mathbb{C}) \to E^\sigma(\mathbb{C})$.

### The theorem at a fixed level

**Theorem 2.3.1 (main theorem of complex multiplication, level $m$).** Let $\sigma$ be an automorphism of $\mathbb{C}$ over $K$, and let $s \in I_K$ with $[s, K] = \sigma$ on $K^{\mathrm{ab}}$. Let $\mathfrak{a}$ be a fractional ideal of $K$, let $E$ be an elliptic curve over $\mathbb{C}$, and let $f : \mathbb{C} \to E(\mathbb{C})$ be an analytic uniformization with lattice $\mathfrak{a}$. Let $m \geq 1$. Then there is an analytic uniformization $f' : \mathbb{C} \to E^\sigma(\mathbb{C})$ with lattice $s^{-1}\mathfrak{a}$ such that
$$f'(y) = f(t)^\sigma$$
for all $t, y \in K$ with $mt \in \mathfrak{a}$ and $s^{-1}(t \bmod \mathfrak{a}) = y \bmod s^{-1}\mathfrak{a}$.

Lean: `GroundTheory.Global.Elliptic.exists_uniformization_level`.

*Proof.* We give the steps of the proof.

Step 1: models. The lattice of $E$ is the ideal $\mathfrak{a}$, so $E$ has complex multiplication by $\mathcal{O}_K$, and its [[j-invariant|9538W1K1EX]] $j(E)$ is algebraic over $K$. The field $K(j(E))$ is the Hilbert class field of $K$. Let $M_1$ be a finite extension of $K(j(E))$ over which the $m$-torsion points of a short Weierstrass model of $E$ are defined. Choose a finite Galois extension $L$ of $K$ inside $\mathbb{C}$ that contains $M_1$, the ray class field of $K$ of modulus $m$ and a primitive $12$-th root of unity. Choose $L$ so large that each curve with complex multiplication by $\mathcal{O}_K$ has a short model over $L$, and that any two such curves are isogenous over $L$. Then $E$ is isomorphic over $\mathbb{C}$ to the base change of a short model $A$ over $L$.

Step 2: a Frobenius prime. Let $S$ be the finite set of finite places of $K$ that are bad for the following reasons: they divide $6m$, some curve of Step 1 has bad reduction at a place above them, or the prime classes fail to describe Frobenius on $j$-invariants there. By the Chebotarev density theorem there is a prime $\mathfrak{p} \notin S$ of degree one and a prime $\mathfrak{P}$ of $L$ above $\mathfrak{p}$ such that $\sigma|_L$ is an arithmetic [[Frobenius element|H5145REFMW]] at $\mathfrak{P}$. Since $\mathfrak{p}$ has degree one and does not divide $6$, its norm $p = N\mathfrak{p}$ is a prime with $p \geq 5$.

Step 3: the isogeny. Since $\sigma|_L$ is Frobenius at $\mathfrak{p}$, it acts on the $j$-invariants of the curves of Step 1 as the class of $\mathfrak{p}$. So there is an isogeny $\varphi : A \to A^\sigma$ over $L$ that corresponds to the ideal $\mathfrak{p}^{-1}$. On the analytic side an isogeny is multiplication by a constant, and the constants that give homomorphisms from $A$ to $A^\sigma$ form a scaled copy of the lattice $\mathfrak{p}^{-1}$. The reduction of $\varphi$ modulo $\mathfrak{P}$ is the $p$-th power Frobenius of the reduced curve. Since $\mathfrak{p}$ does not divide $m$, reduction modulo $\mathfrak{P}$ is injective on the $m$-torsion. So $\varphi(P) = P^\sigma$ for each $m$-torsion point $P$ of $A$.

Step 4: the idele. On the ray class field of modulus $m$, both $[s, K]$ and the Frobenius of $\mathfrak{p}$ equal $\sigma$. By the reciprocity law, $s$ is the product of a principal idele $x \in K^\times$, the idele of $\mathfrak{p}$, and an idele that is a unit congruent to $1$ modulo $m$ at each finite place. So the action of $s^{-1}$ on $K/\mathfrak{a}$, restricted to the elements killed by $m$, is the action of $x^{-1}$ times the action of $\mathfrak{p}^{-1}$.

Step 5: conclusion. Compose $f$ with the isogeny of Step 3 and scale by $x$. This gives a uniformization $f'$ of $E^\sigma$ with lattice $s^{-1}\mathfrak{a}$. By Steps 3 and 4 it satisfies $f'(y) = f(t)^\sigma$ for all $t$ with $mt \in \mathfrak{a}$. $\square$

### The theorem at all levels

**Theorem 2.3.2 (main theorem of complex multiplication).** Let $\sigma$, $s$, $\mathfrak{a}$, $E$ and $f$ be as in the previous theorem. Then there is a unique analytic uniformization $f' : \mathbb{C} \to E^\sigma(\mathbb{C})$ with lattice $s^{-1}\mathfrak{a}$ such that
$$f'(y) = f(t)^\sigma$$
for all $t, y \in K$ with $s^{-1}(t \bmod \mathfrak{a}) = y \bmod s^{-1}\mathfrak{a}$.

Lean: `GroundTheory.Global.Elliptic.main_theorem_complexMultiplication`.

So the diagram
$$\begin{array}{ccc} K/\mathfrak{a} & \xrightarrow{\ f\ } & E(\mathbb{C})_{\mathrm{tors}} \\ \downarrow s^{-1} & & \downarrow \sigma \\ K/s^{-1}\mathfrak{a} & \xrightarrow{\ f'\ } & E^\sigma(\mathbb{C})_{\mathrm{tors}} \end{array}$$
commutes. This is the form of Shimura's theorem in Silverman, *Advanced Topics*, Chapter II, Theorem 8.2.

*Proof.* Existence. For each $n \geq 0$, the previous theorem with $m = (n+1)!$ gives a uniformization $F_n$ of $E^\sigma$ with lattice $s^{-1}\mathfrak{a}$ that has the property for all $t$ with $(n+1)!\, t \in \mathfrak{a}$. Fix $F_0$. Two uniformizations with the same lattice differ by an automorphism of $\mathbb{C}/s^{-1}\mathfrak{a}$, that is, by multiplication with a unit of $\mathcal{O}_K$. So $F_n(z) = F_0(\varepsilon_n z)$ for a unit $\varepsilon_n$. The unit group of $\mathcal{O}_K$ is finite, because $K$ is imaginary quadratic. So one unit $\varepsilon$ occurs for infinitely many $n$. Let $f' = F_{n_0}$ for one such $n_0$. Let $t \in K$. Some positive integer $k$ has $kt \in \mathfrak{a}$. Choose $n$ in the infinite set with $n \geq k$. Then $(n+1)!\, t \in \mathfrak{a}$, so $F_n(y) = f(t)^\sigma$. And $F_n = F_{n_0}$, because both are $F_0(\varepsilon\, \cdot)$. So $f'(y) = f(t)^\sigma$.

Uniqueness. Let $g$ be a second uniformization with the property. Then $g(z) = f'(cz)$ for a constant $c$ with $c \cdot s^{-1}\mathfrak{a} = s^{-1}\mathfrak{a}$. For each $y \in K$ we have $f'(cy) = g(y) = f'(y)$, so $(c - 1)y$ lies in the lattice $s^{-1}\mathfrak{a}$. If $c \neq 1$, then $(c-1)K$ is contained in a discrete lattice. This is false: $K$ contains elements of arbitrarily small absolute value, and the nonzero elements of a lattice have absolute value at least some $\delta > 0$. So $c = 1$ and $g = f'$. $\square$

**Remark 2.3.3 (Formalization).** The field $K$ is a number field of degree $2$ with no real place, with an algebra map into $\mathbb{C}$ ([MainTheorem.lean](lean:GroundTheory/GlobalFields/ComplexMultiplication/MainTheorem.lean#L66)). The uniformization is an additive map $\mathbb{C} \to E(\mathbb{C})$ with analytic coordinate functions near each point, not a map from the quotient ([AnalyticUniformization.lean](lean:GroundTheory/GlobalFields/ComplexMultiplication/AnalyticUniformization.lean#L15)). The idele action on $K/\mathfrak{a}$ is built through the decomposition into local quotients ([IdeleActionQuotient.lean](lean:GroundTheory/GlobalFields/ComplexMultiplication/IdeleActionQuotient.lean#L169)). The level theorem gives existence only; uniqueness is proved at all levels. The proof of the main theorem uses the levels $(n+1)!$ and chooses the functions $F_n$ by choice.
