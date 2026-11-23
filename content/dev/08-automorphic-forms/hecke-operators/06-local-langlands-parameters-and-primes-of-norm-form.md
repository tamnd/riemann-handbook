---
title: Local Langlands parameters and primes of a norm form
decls:
  - UpperTheory.Zero.LLC.cuspEx
  - UpperTheory.Zero.LLC.recTExists
  - UpperTheory.T3.shortNorm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local Langlands parameters and primes of a norm form

This section gives two inputs of [the theorem on every character](/step/every-character/). The first is a local reciprocity map: an assignment of a Weil-Deligne representation to each irreducible smooth representation of $\mathrm{GL}_n$ over a $p$-adic field, with the properties of the local Langlands correspondence that the global argument uses ([the local Langlands correspondence](/learn/galois-representations/#the-local-langlands-correspondence)). The second is a lower bound for the number of primes of the form $(A^2 + dB^2)/4$, with congruence conditions, in a short interval. It enters through [the matching of local theta integrals](/step/theta-local-matching/).

### Reciprocity maps

Fix a number field $E$, an algebraic closure $\Omega$ of $E$, a finite place $w$ of $E$ and a place of $\Omega$ above $w$. This gives a decomposition group, the Weil group $W_w$ and its inertia subgroup $I_w$. Let $\mathrm{Irr}_w$ be the set of isomorphism classes of irreducible smooth representations of $\mathrm{GL}_n(E_w)$, for all $n \ge 0$, and $\mathrm{WD}_w$ the set of isomorphism classes of Frobenius-semisimple Weil-Deligne representations of $W_w$ ([smooth representations](/learn/representations/#smooth-representations-of-p-adic-groups)). Let $a : W_w \to E_w^\times$ be a local Artin map ([local class field theory](/learn/class-field-theory/#local-class-field-theory)).

Each $x \in \mathrm{Irr}_w$ has a cuspidal support, a multiset of cuspidal representations, and a Langlands classification by a list of segments ([cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments)). We say that a cuspidal $y$ is *good* if $y$ is a character, or $E_w \cong \mathbb{Q}_g$ for a prime $g$ and $y$ is a twist by a character of a representation with nonzero vectors under the first congruence subgroup $K_1$ (a depth-zero representation, [depth zero](/learn/representations/#depth-zero-representations-and-types)). We say that $x$ is *good* if every element of its cuspidal support is good.

**Definition 6.6.1 (Reciprocity map).** A map $\mathrm{rc} : \mathrm{Irr}_w \to \mathrm{WD}_w$ is a *reciprocity map* for $a$ if:

- $\mathrm{rc}(x)$ has dimension $n$ when $x$ is a representation of $\mathrm{GL}_n(E_w)$;
- for a character $\chi$ of $E_w^\times$, $\mathrm{rc}(\chi) = \chi \circ a$;
- if $x$ has Langlands data $\Delta_1, \dots, \Delta_k$, then $\mathrm{rc}(x)$ is the direct sum of the Weil-Deligne representations attached to the $\Delta_i$ through $\mathrm{rc}$ on the cuspidal representations;
- $\mathrm{rc}(x)$ is irreducible when $x$ is cuspidal;
- $\mathrm{rc}(x \otimes |\det|^s) = \mathrm{rc}(x) \otimes |a|^s$ for real $s$;
- if $x$ has central character $\omega$, then $|\det \mathrm{rc}(x)(\sigma)| = |\omega(a(\sigma))|$ for $\sigma \in W_w$;
- for good $x$: $\mathrm{rc}$ respects twists by characters, $\det \mathrm{rc}(x) = \omega \circ a$, $\mathrm{rc}$ of the contragredient is the dual, and $\mathrm{rc}(x') = \mathrm{rc}(x)$ implies $x' = x$;
- for good $x$ with nonzero $K_1$-fixed vectors, $\mathrm{rc}(x)$ is tame, that is, trivial on wild inertia;
- (type) if $E_w \cong \mathbb{Q}_g$ and $x$ is inflated from a cuspidal representation $\tau$ of $\mathrm{GL}_n(\mathbb{F}_g)$ whose character on elliptic elements is given by a regular character $\theta$ of $\mathbb{F}_{g^n}^\times$, then $\mathrm{rc}(x)$ has trivial monodromy, and on tame inertia it acts with characteristic polynomial $\prod_{j=0}^{n-1}(X - \theta(z^{g^j}))$, where $z$ is the image of the inertia element in $\mathbb{F}_{g^n}^\times$.

The last law is the explicit form of the correspondence in depth zero: a Deligne-Lusztig cuspidal representation with parameter $\theta$ corresponds to the induced representation from the unramified extension of degree $n$ of the tame character $\theta$.

**Lemma 6.6.2 (Parameters of cuspidal representations).** For every $E$, $\Omega$, $w$ and local Artin map $a$, there is a map $r : \mathrm{Irr}_w \to \mathrm{WD}_w$ such that, on cuspidal representations, $r$ satisfies the laws above: $r(x)$ is irreducible of dimension $n$, $r(\chi) = \chi \circ a$ on characters, $r$ commutes with $|\det|^s$, the absolute value of the determinant is right, the twist, central character, duality, injectivity and tameness laws hold for good cuspidals, and the type law holds.

Lean: `UpperTheory.Zero.LLC.cuspEx`.

*Proof.* There is a map $r_0$ that is defined by local class field theory on characters, respects twists of good cuspidals, and, when $E_w \cong \mathbb{Q}_g$, gives each depth-zero cuspidal $y$ a tame irreducible parameter of dimension $n$ with the right determinant and the right type. On a cuspidal $x$ that is not good, $x$ is not a character, so $n \ge 2$. There is an irreducible Weil-Deligne representation $J_n$ of dimension $n$ with unitary determinant that is not a twist of a tame representation. There is also an exponent $e(x) \in \mathbb{R}$ with $e(x \otimes |\det|^s) = e(x) + s$ that makes $J_n \otimes |a|^{e(x)}$ have the absolute value of the determinant prescribed by the central character of $x$. Put
$$r(x) = \begin{cases} r_0(x) & x \text{ good}, \\ J_n \otimes |a|^{e(x)} & \text{otherwise}. \end{cases}$$
The laws for good cuspidals come from $r_0$. Twisting by $|\det|^s$ preserves goodness, so the law for $|\det|^s$ follows from the property of $e$ on the bad ones. Injectivity on good cuspidals needs $r(x) \ne r(y)$ when $x$ is bad and $y$ is good. This holds since $J_n$ is not a twist of a tame representation and the parameters of good cuspidals are twists of tame ones. $\square$

The map $r$ is a correspondence only on good cuspidals. On the others it is a placeholder with the correct dimension and the correct absolute value of the determinant.

**Theorem 6.6.3 (Existence of reciprocity maps).** For every number field $E$, algebraic closure $\Omega$ and place of $\Omega$ above a finite place $w$, there are a local Artin map $a$ and a reciprocity map $\mathrm{rc}$ for $a$.

Lean: `UpperTheory.Zero.LLC.recTExists`.

*Proof.* Take a local Artin map $a$, and let $r$ be the map of the lemma. Extend $r$ from cuspidal representations to all of $\mathrm{Irr}_w$ by the Langlands classification: for $x$ with Langlands data $\Delta_1, \dots, \Delta_k$, let $\mathrm{rc}(x)$ be the sum of the Weil-Deligne representations of the segments, built from $r$ on the first element of each segment. Then $\mathrm{rc} = r$ on cuspidals, so the laws for characters, irreducibility and type hold. The dimension and the absolute value of the determinant are computed from the cuspidal support. The laws for good $x$ reduce to those for its good cuspidal support: twists act on segments elementwise, the central character is the product over the support, the contragredient reverses the segments, injectivity follows from the uniqueness of the Langlands data, and tameness follows since a depth-zero $x$ has depth-zero support. $\square$

### Primes represented by a norm form in short intervals

Let $d$ be a prime with $d \equiv 3 \pmod 4$, and let $M \ge 1$. For $X \le Y$ let $\mathcal{P}_{d,M}(X, Y)$ be the set of primes $p$ with $\lfloor X \rfloor < p \le \lfloor Y \rfloor$ for which there are integers $A$, $B$ with
$$A^2 + dB^2 = 4p, \qquad M \mid B, \qquad 2M \mid A - 2 - B.$$
In terms of $K = \mathbb{Q}(\sqrt{-d})$: then $A \equiv B \pmod 2$, so $\pi = (A + B\sqrt{-d})/2 = (A - B)/2 + B\,\frac{1 + \sqrt{-d}}{2}$ is an integer of $K$ of norm $p$. The two divisibilities say that $\pi \equiv 1 \pmod{M\mathcal{O}_K}$. So $p$ is in the set when $p$ splits in $K$ and a prime factor of $p$ is trivial in the ray class group of modulus $M$ ([primes represented by norm forms](/learn/analytic-number-theory/#primes-represented-by-norm-forms)).

**Theorem 6.6.4 (Primes of a norm form in short intervals).** There are constants $A, c, c' > 0$ with the following property. Let $d$ be a prime with $d \equiv 3 \pmod 4$ and $d \ge 100$, let $M \ge 3$, $X \ge 1$ and $h \le 1$, and put $D = 4dM^2$. If
$$\log D \le c\sqrt{\log X}, \qquad e^{-c\sqrt{\log X}} \le h,$$
then
$$\#\mathcal{P}_{d,M}\bigl(X, X(1+h)\bigr) \ge \frac{c'\, hX}{D^A \log X}.$$

Lean: `UpperTheory.T3.shortNorm` (also `GlobalTheory.T.normPrimesImagQuad_short_interval_lower_bound`, a second name).

The proof uses a family of ideal-counting functions. For the ray class group $G$ of $K$ of modulus $M$ and $g \in G$, let $a(g, n)$ be the number of integral ideals of norm $n$ in the class $g$. Let $\lambda(g, n) \ge 0$ be the weights in the identity
$$a(g, n) \log n = \sum_{h \in G} \sum_{n_1 n_2 = n} \lambda(h, n_1)\, a(g - h, n_2),$$
that is, the von Mangoldt function of the ray class $h$ (with prime ideals counted by the logarithm of their norm). These satisfy $\sum_g \lambda(g, n) \le 2\Lambda(n)$. The counting functions also satisfy $\#G \le D$, $|\sum_{n \le x} a(g, n) - \kappa x| \le 10\sqrt{x}$ with $1/D \le \kappa \le 4$, a smoothed version of this count, and a positivity property for real characters of $G$ that controls a possible exceptional zero. Also, a prime $p$ with $\lambda(0, p) \ne 0$ is in $\mathcal{P}_{d,M}$: such a $p$ is the norm of a prime ideal of degree one in the trivial ray class.

**Lemma 6.6.5 (Trivial class in short intervals).** There are constants $A, c, c' > 0$ such that for every family as above with bound $D$, every $X \ge 1$ and every $h \le 1$ with $\log D \le c\sqrt{\log X}$ and $e^{-c\sqrt{\log X}} \le h$,
$$\sum_{X < n \le X(1+h)} \lambda(0, n) \ge \frac{c'\, hX}{D^A}.$$

This is the prime ideal theorem for ray classes in short intervals. Its proof uses the explicit formula for the characters $\chi$ of $G$, the zero-free region of $L(s, \chi)$, and the fact that there is at most one exceptional real zero $\beta$, for one real $\chi$, with $1 - \beta \ge c/D^A$ ([zeros of $L$-functions](/learn/analytic-number-theory/#zeros-of-dirichlet-l-functions)). The positivity property gives this polynomial bound for $1 - \beta$. The bound is weaker than Siegel's theorem, but it is effective.

*Proof of the theorem.* Let $Y = X(1+h) \le 2X$. Split the sum of the lemma into primes and prime powers. On primes $p \le Y$, $\lambda(0, p) \le 2\log p \le 2\log Y$, and $\lambda(0, p) \ne 0$ only for $p \in \mathcal{P}_{d,M}$. On prime powers, $\lambda(0, n) \le 2\Lambda(n)$, and the sum of $\Lambda$ over prime powers $n \le Y$ is $\psi(Y) - \theta(Y) \le C\sqrt{Y}$. So
$$\frac{c'\, hX}{D^A} \le 2\log Y \cdot \#\mathcal{P}_{d,M}(X, Y) + 2C\sqrt{2X}.$$
With $c$ small in terms of $A$ and $C$, the hypotheses give $\log X \ge 1$ and $K\sqrt{X} \le hX/D^A$ for $K = 8(|C| + 1)/c'$. To see this, put $s = \sqrt{\log X}$. Then $D^A \le e^{As}$ and $h \ge e^{-s}$, and $K \le e^{s^2/2 - (1+A)s}$ once $s$ is large compared with $A$ and $K$. So the prime-power term is at most half of the left side. With $\log Y \le 2\log X$ this gives $\#\mathcal{P}_{d,M}(X, Y) \ge c' hX/(8 D^A \log X)$. $\square$

**Remark 6.6.6 (Formalization).** The lemma on cuspidal representations takes the map $r_0$, the exponent $e$ and the representations $J_n$ as inputs ([CuspEx.lean](lean:Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/CuspEx.lean#L168)). So the cuspidal representations that are not good get parameters with no arithmetic meaning, and the reciprocity map is unique only on good representations. The statement is weaker than the local Langlands correspondence: it has no $L$-factors or $\varepsilon$-factors, it does not say that $\mathrm{rc}$ is a bijection, and its twist, duality and injectivity laws hold only for good representations ([RecTTransport.lean](lean:Development/AutomorphicArithmetic/Foundations/LocalLanglands/RecTTransport.lean#L86)). The type law is stated only when $E_w$ is isomorphic to $\mathbb{Q}_g$. The extension from cuspidal representations is an input of the existence theorem; we did not unfold it. For primes, the family of counting functions is an abstract structure. Its existence for the ray class group, the lemma on the trivial class and the bound $\psi - \theta \le C\sqrt{x}$ are inputs ([NormPrimesImagQuadShortIntervalLowerBound.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/NormPrimesImagQuadShortIntervalLowerBound.lean#L98)).
