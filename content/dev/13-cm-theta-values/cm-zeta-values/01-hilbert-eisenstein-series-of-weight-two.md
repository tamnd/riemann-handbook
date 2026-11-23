---
title: Hilbert Eisenstein series of weight two
decls:
  - GlobalTheory.HeckeTwoEq.gFun_eq_eisSum
  - GlobalTheory.T.heckeWeightTwoContinuation_eq_latticeSeries
  - GlobalTheory.HeckeTwo.bOne_isGood
  - GlobalTheory.T.heckeEisensteinNonconstantFourierSum_smoothHolomorphic
  - GlobalTheory.HeckeTwo.heckeWeightTwo_of_fe
  - GlobalTheory.T.heckeWeightTwoContinuation_of_functionalEquation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hilbert Eisenstein series of weight two

Let $F$ be a totally real field of degree $n \geq 2$. The lattice sum that defines a Hilbert Eisenstein series of parallel weight $k$ converges absolutely only for $k \geq 3$. For $k = 2$ we follow Hecke: we add a factor $|\cdot|^{-2\sigma}$, which makes the sum converge for $\operatorname{Re} \sigma > 0$, and we continue in $\sigma$ to $\sigma = 0$. This section proves that the continuation exists, that it is smooth in the variable $z$, and that its value at $\sigma = 0$ is holomorphic with an explicit $q$-expansion. The constant term of the expansion is a value of a partial zeta function at $s = -1$. The only input is the functional equation of partial zeta functions. The result is used in the next section, where the derivatives of the CM lattice sums of weight two are computed, and through it in the proof of the [toric denominator bounds](/entry/join-out-of-five/).

### Notation

Let $\tau_1, \dots, \tau_n$ be the real embeddings of $F$, let $\mathcal{O}_F$ be its ring of integers, $\mathfrak{d}$ its different and $d_F = |\operatorname{disc} F|$. Let $\mathbb{H}^n = \{z \in \mathbb{C}^n : \operatorname{Im} z_j > 0 \text{ for all } j\}$. For $\xi \in F$ write $\xi^{(j)} = \tau_j(\xi)$, and $N\xi = \prod_j \xi^{(j)}$. The letters $\mathfrak{a}, \mathfrak{b}$ denote invertible fractional ideals of $F$, and $N\mathfrak{a}$ is the absolute norm. Let $\mathfrak{a}^\vee = \mathfrak{d}^{-1}\mathfrak{a}^{-1}$; this is the dual lattice of $\mathfrak{a}$ for the trace form ([ideals and the class group](/learn/number-fields/#ideals-and-the-class-group)). The unit group $\mathcal{O}_F^\times$ acts on $\mathfrak{a}^\vee \times \mathfrak{b}$ by $\varepsilon(a, b) = (\varepsilon a, \varepsilon b)$.

**Definition 1.1.1 (Hecke's lattice series).** For $z \in \mathbb{H}^n$ and $(a, b) \in F^2$ put $\ell_j(a, b; z) = 2\pi i\,(a^{(j)} + b^{(j)} z_j)$ and $\ell = \prod_j \ell_j$. For $\sigma \in \mathbb{C}$ let

$$E_{\mathfrak{a},\mathfrak{b}}(z, \sigma) = \sum_{(a, b)} \ell(a, b; z)^{-2}\, |\ell(a, b; z)|^{-2\sigma},$$

where $(a, b)$ runs over the nonzero elements of $\mathfrak{a}^\vee \times \mathfrak{b}$ modulo $\mathcal{O}_F^\times$.

Each term depends only on the orbit, since $N\varepsilon = \pm 1$ and the exponent $-2$ is even. For $\operatorname{Re} \sigma > 0$ the series converges absolutely. At $\sigma = 0$ it is the formal Hilbert Eisenstein series of weight $2$, which does not converge.

**Definition 1.1.2 (partial zeta function).** Let $C$ be an ideal class of $F$. A function $Z : \mathbb{C} \to \mathbb{C}$ is a *partial zeta function of $C$* if $Z$ is holomorphic on $\mathbb{C} \setminus \{1\}$ and $Z(s) = \sum_{J \in C} N J^{-s}$ for $\operatorname{Re} s > 1$, the sum over the nonzero integral ideals $J$ in $C$ ([zeta functions of number fields](/learn/l-functions/#zeta-functions-of-number-fields)).

Let $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$. We take the following as given.

**Theorem 1.1.3 (functional equation of partial zeta functions; Hecke).** Let $F$ be totally real of degree $n$, and let $C, C'$ be ideal classes with $C C' = [\mathfrak{d}]$. Then there are partial zeta functions $Z$ of $C$ and $Z'$ of $C'$ such that

$$d_F^{s/2}\, \Gamma_{\mathbb{R}}(s)^n\, Z(s) = d_F^{(1-s)/2}\, \Gamma_{\mathbb{R}}(1-s)^n\, Z'(1-s)$$

for every $s$ with $s \notin \{0, -2, -4, \dots\}$ and $1 - s \notin \{0, -2, -4, \dots\}$.

This is in J. Neukirch, *Algebraic Number Theory*, Chapter VII, §5, where the partial zeta function of a class is completed and its functional equation is proved by theta series.

### The Fourier expansion in the first variable

The continuation comes from the Fourier expansion of $E_{\mathfrak{a},\mathfrak{b}}$ in $\operatorname{Re} z$. We need four objects. For $w \in \mathbb{C} \setminus \{0\}$ let $\phi_\sigma(w) = w^{-2}|w|^{-2\sigma}$. For $\nu \in \mathbb{R}$ and $y > 0$ let

$$h_\sigma(\nu, y) = \int_{\mathbb{R}} \phi_\sigma(t + iy)\, e^{-2\pi i \nu t}\, dt$$

be the Fourier transform of $\phi_\sigma$ on the horizontal line at height $y$, and $c(\sigma) = h_\sigma(0, 1)$. A change of variables gives $h_\sigma(0, y) = c(\sigma)\,|y|^{-1-2\sigma}$. Let $k(\sigma) = \bigl((2\pi i)^{-2}(2\pi)^{-2\sigma}\bigr)^n$ and $\omega_{\mathfrak{a}} = d_F^{1/2} N\mathfrak{a}$.

**Definition 1.1.4 (the three parts).** Let $Z_{\mathfrak{b}}$ be a partial zeta function of $[\mathfrak{b}]^{-1}$. For $z \in \mathbb{H}^n$ put

$$A(\sigma) = \sum_{a \in (\mathfrak{a}^\vee \setminus 0)/\mathcal{O}_F^\times} \ell(a, 0; z)^{-2}|\ell(a, 0; z)|^{-2\sigma},$$

which does not depend on $z$;

$$B_0(\sigma, z) = k(\sigma)\, \omega_{\mathfrak{a}}\, N\mathfrak{b}^{-1-2\sigma}\, Z_{\mathfrak{b}}(1 + 2\sigma) \prod_j c(\sigma)\, y_j^{-1-2\sigma} \quad (\sigma \neq 0), \qquad B_0(0, z) = 0;$$

$$B_1(\sigma, z) = \sum_{b \in (\mathfrak{b} \setminus 0)/\mathcal{O}_F^\times}\ \sum_{\nu \in \mathfrak{a} \setminus 0}\ \prod_j e^{2\pi i \nu^{(j)} b^{(j)} x_j}\, h_\sigma\bigl(\nu^{(j)}, b^{(j)} y_j\bigr),$$

where $z_j = x_j + i y_j$. Finally let $G(\sigma, z) = A(\sigma) + B_0(\sigma, z) + k(\sigma)\,\omega_{\mathfrak{a}}\, B_1(\sigma, z)$.

The part $A$ collects the terms with $b = 0$. The part $B_0$ is the zero Fourier mode of the terms with $b \neq 0$, and $B_1$ collects the other modes.

**Lemma 1.1.5 (Fourier expansion).** Let $Z_{\mathfrak{b}}$ be a partial zeta function of $[\mathfrak{b}]^{-1}$. For $\operatorname{Re} \sigma > 0$ and $z \in \mathbb{H}^n$ the series $E_{\mathfrak{a},\mathfrak{b}}(z, \sigma)$ converges absolutely, and $G(\sigma, z) = E_{\mathfrak{a},\mathfrak{b}}(z, \sigma)$.

Lean: `GlobalTheory.HeckeTwoEq.gFun_eq_eisSum` (also `GlobalTheory.T.heckeWeightTwoContinuation_eq_latticeSeries`, a second name).

*Proof.* Absolute convergence for $\operatorname{Re} \sigma > 0$ is the convergence of $\sum |N(a + bz)|^{-2-2\operatorname{Re}\sigma}$ over a lattice of rank $2n$ modulo units. Since the terms are invariant under units, we may sum first over $a \in \mathfrak{a}^\vee$ for fixed $b$, and then over the classes of $b$. The terms with $b = 0$ give $A(\sigma)$. Fix $b \neq 0$. Each term is $k(\sigma)$ times $\prod_j \phi_\sigma(a^{(j)} + b^{(j)} z_j)$. By Poisson summation over the lattice $\mathfrak{a}^\vee \subset \mathbb{R}^n$, whose dual lattice for the trace form is $\mathfrak{a}$ and whose covolume is $\omega_{\mathfrak{a}}^{-1}$, the sum over $a$ equals $\omega_{\mathfrak{a}} \sum_{\nu \in \mathfrak{a}} \prod_j e^{2\pi i \nu^{(j)} b^{(j)} x_j} h_\sigma(\nu^{(j)}, b^{(j)} y_j)$. The terms with $\nu \neq 0$ give the inner sum of $B_1$. The term $\nu = 0$ is $\prod_j c(\sigma)|b^{(j)} y_j|^{-1-2\sigma} = |Nb|^{-1-2\sigma} \prod_j c(\sigma) y_j^{-1-2\sigma}$. The map $b \mapsto b\mathfrak{b}^{-1}$ is a bijection from $(\mathfrak{b} \setminus 0)/\mathcal{O}_F^\times$ onto the integral ideals in the class $[\mathfrak{b}]^{-1}$, and $N(b\mathfrak{b}^{-1}) = |Nb|\, N\mathfrak{b}^{-1}$. So $\sum_b |Nb|^{-s} = N\mathfrak{b}^{-s} Z_{\mathfrak{b}}(s)$ for $\operatorname{Re} s > 1$, and with $s = 1 + 2\sigma$ the zero modes add up to $B_0(\sigma, z)$. $\square$

### Smoothness of the nonconstant part

We use the Wirtinger derivatives $\partial_{z_j} = \tfrac12(\partial_{x_j} - i\partial_{y_j})$ and $\partial_{\bar z_j} = \tfrac12(\partial_{x_j} + i\partial_{y_j})$. A *Wirtinger word* is a finite composition of these operators. Let $\Pi = \{\sigma \in \mathbb{C} : \operatorname{Re} \sigma > -\tfrac12\}$.

**Definition 1.1.6 (good family).** A function $P : \mathbb{C} \times \mathbb{H}^n \to \mathbb{C}$ is *good* if $P(\sigma, \cdot)$ is $C^\infty$ on $\mathbb{H}^n$ for each $\sigma \in \Pi$, and if for each Wirtinger word $D$ and each $z \in \mathbb{H}^n$ the function $\sigma \mapsto (D P(\sigma, \cdot))(z)$ is holomorphic on $\Pi$.

Sums and products of good families are good, and a good family times a holomorphic function of $\sigma$ alone is good.

**Proposition 1.1.7 (the nonconstant Fourier sum).** For every totally real $F$ and all $\mathfrak{a}, \mathfrak{b}$, the family $B_1$ is good.

Lean: `GlobalTheory.HeckeTwo.bOne_isGood` (also `GlobalTheory.T.heckeEisensteinNonconstantFourierSum_smoothHolomorphic`, a second name).

*Proof.* Each term $f_{b,\nu}(\sigma, z) = \prod_j e^{2\pi i \nu^{(j)} b^{(j)} x_j} h_\sigma(\nu^{(j)}, b^{(j)} y_j)$ is smooth in $z$ on $\mathbb{H}^n$, and each Wirtinger derivative of it is holomorphic in $\sigma$ on $\Pi$; both follow by differentiation under the integral sign, since $\phi_\sigma(t + iy)$ decays like $|t|^{-2-2\operatorname{Re}\sigma}$ and $2 + 2\operatorname{Re}\sigma > 1$ on $\Pi$. For $\nu y \neq 0$ the transform $h_\sigma(\nu, y)$ decays exponentially in $|\nu y|$, by a shift of the contour. This gives, for each compact $K \subset \mathbb{H}^n$, each compact $L \subset \Pi$ and each order $m$, a summable family of bounds for the $m$-th derivatives of $f_{b,\nu}$ in $z$ that is uniform on $L \times K$. A series of smooth functions whose derivatives of each order converge uniformly on compacts is smooth, and its derivatives are the series of derivatives. A locally uniform limit of holomorphic functions of $\sigma$ is holomorphic. Since the family is absolutely summable, the double sum over $(b, \nu)$ is the iterated sum that defines $B_1$ (Fubini). $\square$

### The continuation and the $q$-expansion

**Definition 1.1.8 (continuation).** A function $G : \mathbb{C} \times \mathbb{H}^n \to \mathbb{C}$ is a *continuation* of Hecke's series for $(\mathfrak{a}, \mathfrak{b})$ if:

1. for $\operatorname{Re} \sigma > 0$ and $z \in \mathbb{H}^n$ the series $E_{\mathfrak{a},\mathfrak{b}}(z, \sigma)$ converges absolutely and equals $G(\sigma, z)$;
2. $G$ is good.

**Definition 1.1.9 ($q$-expansion of weight $k$).** Let $g : \mathbb{H}^n \to \mathbb{C}$ and $k \geq 1$. Let $c_k = ((k-1)!)^n d_F^{(k-1)/2}$. We say that $g$ *has the $q$-expansion of weight $k$ for $(\mathfrak{a}, \mathfrak{b})$* if there is a partial zeta function $Z$ of $[\mathfrak{a}]^{-1}$ such that for every $z \in \mathbb{H}^n$ the series below converges absolutely and

$$\frac{c_k\, g(z)}{\omega_{\mathfrak{a}}^k} = 2^{-n} Z(1 - k) + \sum_{(\mu, \beta)} \Bigl(\frac{|N\mu|}{N\mathfrak{a}}\Bigr)^{k-1} e^{2\pi i \operatorname{tr}(\mu\beta z)},$$

where $\operatorname{tr}(\xi z) = \sum_j \xi^{(j)} z_j$, and $(\mu, \beta)$ runs over the pairs in $\mathfrak{a} \times \mathfrak{b}$ with $\mu\beta$ totally positive, modulo $(\mu, \beta) \sim (\varepsilon^{-1}\mu, \varepsilon\beta)$ for $\varepsilon \in \mathcal{O}_F^\times$.

For $F = \mathbb{Q}$ and $\mathfrak{a} = \mathfrak{b} = \mathbb{Z}$ the right side is $\tfrac12\zeta(1-k) + \sum_{m \geq 1} \sigma_{k-1}(m) q^m$, the classical expansion of $G_k$ up to a constant.

**Theorem 1.1.10 (Hecke's Eisenstein series of weight two).** Assume the functional equation of partial zeta functions. Let $F$ be totally real of degree $n \geq 2$ and let $\mathfrak{a}, \mathfrak{b}$ be fractional ideals. Then there is a continuation $G$ of Hecke's series for $(\mathfrak{a}, \mathfrak{b})$ such that $G(0, \cdot)$ is holomorphic on $\mathbb{H}^n$ and has the $q$-expansion of weight $2$ for $(\mathfrak{a}, \mathfrak{b})$.

Lean: `GlobalTheory.HeckeTwo.heckeWeightTwo_of_fe` (also `GlobalTheory.T.heckeWeightTwoContinuation_of_functionalEquation`, a second name).

*Proof.* Apply the functional equation to $C = [\mathfrak{b}]^{-1}$ and $C' = [\mathfrak{d}][\mathfrak{b}]$. It gives a partial zeta function $Z_{\mathfrak{b}}$ of $[\mathfrak{b}]^{-1}$. The functional equation and the poles of $\Gamma_{\mathbb{R}}$ show that $Z_{\mathfrak{b}}$ has at most a simple pole at $s = 1$: there is an entire $R$ with $Z_{\mathfrak{b}}(s) = R(s)/(s-1)$. Apply it again to $C = [\mathfrak{d}][\mathfrak{a}]$ and $C' = [\mathfrak{a}]^{-1}$. It gives partial zeta functions $Z_{\mathfrak{a}}$ of $[\mathfrak{d}][\mathfrak{a}]$ and $Z_{\mathfrak{a}}'$ of $[\mathfrak{a}]^{-1}$. Let $G$ be the function of the [Lemma 1.1.5](/entry/g-fun-eq-eis-sum/) built with $Z_{\mathfrak{b}}$. Property 1 is that Lemma.

For property 2 we show that the three parts are good. The series $A(\sigma)$ is a lattice sum of type $\sum |Na|^{-2-2\sigma}$ with a sign; it is holomorphic on $\Pi$ and constant in $z$, so it is good. The factor $k(\sigma)$ is entire, so $k\,\omega_{\mathfrak{a}} B_1$ is good by the [Proposition 1.1.7](/entry/b-one-is-good/). For $B_0$, write $Z_{\mathfrak{b}}(1 + 2\sigma) = R(1 + 2\sigma)/(2\sigma)$. The constant $c(\sigma)$ vanishes at $\sigma = 0$, since $\int_{\mathbb{R}} (t + i)^{-2} dt = 0$. As $n \geq 2$, the product $c(\sigma)^n$ has a zero of order at least $2$, so $c(\sigma)^n/(2\sigma)$ is holomorphic on $\Pi$ and vanishes at $0$. Thus $B_0$ extends to a good family whose value at $\sigma = 0$ is $0$, which is the value in the definition. So $G$ is good.

At $\sigma = 0$ we have $B_0(0, z) = 0$, so $G(0, z) = A(0) + k(0)\,\omega_{\mathfrak{a}} B_1(0, z)$. At $\sigma = 0$ the transform is classical, by residues: $h_0(\nu, y) = -4\pi^2 |\nu|\, e^{-2\pi \nu y}$ if $\nu y > 0$, and $h_0(\nu, y) = 0$ if $\nu y < 0$. So only the pairs with $\nu b$ totally positive survive, and a direct computation gives

$$\frac{c_2\, k(0)\,\omega_{\mathfrak{a}} B_1(0, z)}{\omega_{\mathfrak{a}}^2} = \sum_{(\mu, \beta)} \frac{|N\mu|}{N\mathfrak{a}}\, e^{2\pi i \operatorname{tr}(\mu\beta z)}.$$

This $q$-series converges absolutely and is holomorphic on $\mathbb{H}^n$. For the constant term, $A(0) = (2\pi i)^{-2n} \sum_a |Na|^{-2}$. The map $a \mapsto a\mathfrak{d}\mathfrak{a}$ is a bijection from $(\mathfrak{a}^\vee \setminus 0)/\mathcal{O}_F^\times$ onto the integral ideals in the class $[\mathfrak{d}][\mathfrak{a}]$, so $A(0) = (2\pi i)^{-2n} N(\mathfrak{d}\mathfrak{a})^2 Z_{\mathfrak{a}}(2)$. The functional equation for the pair $([\mathfrak{d}][\mathfrak{a}], [\mathfrak{a}]^{-1})$ at $s = 2$ turns this into $c_2 A(0)/\omega_{\mathfrak{a}}^2 = 2^{-n} Z_{\mathfrak{a}}'(-1)$. Adding the two parts gives the $q$-expansion of weight $2$ with $Z = Z_{\mathfrak{a}}'$, and $G(0, \cdot)$ is holomorphic as the sum of a constant and a holomorphic $q$-series. $\square$

**Remark 1.1.11.** The value $G(0, z)$ is holomorphic only because $n \geq 2$. For $F = \mathbb{Q}$ the zero mode $B_0$ does not vanish at $\sigma = 0$: it gives the term $-\pi/y$ of the nonholomorphic Eisenstein series $G_2^*$. For $n \geq 2$ the zero of $c(\sigma)^n$ is of higher order than the pole of $Z_{\mathfrak{b}}(1 + 2\sigma)$, and the correction term disappears.

**Remark 1.1.12 (Formalization).** The part $B_0$ is defined with an explicit case $B_0(0, z) = 0$ ([KFacDifferentiable.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KFacDifferentiable.lean#L47)); the proof then shows that this agrees with the limit, so the case split is harmless. The functional equation is the only published input: it enters as a hypothesis of the Theorem and is used twice. The $q$-expansion asserts the shape of the Fourier series but not that $G(0, \cdot)$ is a Hilbert modular form; modularity is never stated. The statement files of the two second names import Mathlib twice (line 1 and line 3).
