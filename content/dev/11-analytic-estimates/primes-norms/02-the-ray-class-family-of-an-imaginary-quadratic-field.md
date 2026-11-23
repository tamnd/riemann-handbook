---
title: The ray class family of an imaginary quadratic field
decls:
  - GlobalTheory.Hk.exists_lFam_ray
  - GlobalTheory.T.exists_lFam_normOne_of_mod_four_eq_three
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The ray class family of an imaginary quadratic field

This section builds a family of ray class type, as defined in Section 1, from the ideals of the field $\mathbb{Q}(\sqrt{-d})$ for a prime $d \equiv 3 \pmod 4$. Its size is $B = 4dM^2$, where $M$ is the modulus. Its weights $\lambda(0, p)$ at primes $p$ are nonzero only for primes $p$ that have a representation $4p = A^2 + dB^2$ with congruence conditions modulo $M$. So [the bound for the trivial class](/entry/trivial-class-short-interval/) gives a lower bound for these primes in short intervals. Section 3 carries out this step.

Throughout, $d$ is a prime with $d \equiv 3 \pmod 4$ and $d \geq 100$, and $M \geq 3$ is an integer. Let $K = \mathbb{Q}(\sqrt{-d})$. This is a [[quadratic field|7SV4WA92SM]] of [[discriminant|3BCYVS9E17]] $-d$. Its ring of integers is $\mathcal{O}_K = \mathbb{Z}[\omega]$ with $\omega = (1 + \sqrt{-d})/2$, so $(2\omega - 1)^2 = -d$. For integers $x, y$ the norm of $x + y\omega$ satisfies
$$4N(x + y\omega) = (2x + y)^2 + dy^2.$$

**Definition 2.2.1 (Norm-one primes).** A prime $p$ is a *norm-one prime* for $(d, M)$ if there are integers $A$ and $B$ with
$$A^2 + dB^2 = 4p, \qquad M \mid B, \qquad 2M \mid A - 2 - B.$$
For real $X \leq Y$, let $\mathcal{P}_{d,M}(X, Y)$ be the set of norm-one primes $p$ with $\lfloor X \rfloor < p \leq \lfloor Y \rfloor$.

The name comes from the following fact. Let $\alpha = x + y\omega \in \mathcal{O}_K$ with $\alpha \equiv 1 \pmod{M\mathcal{O}_K}$, that is, $M \mid x - 1$ and $M \mid y$. If $N(\alpha) = p$ is prime, then $A = 2x + y$ and $B = y$ satisfy the three conditions, since $A - 2 - B = 2(x - 1)$. So the norm-one primes include the norms of prime elements that are congruent to $1$ modulo $M$. These are the primes that split in the ray class field of $K$ modulo $M$ (see [the Background on class field theory](/learn/class-field-theory/#global-class-field-theory)).

**Definition 2.2.2 (Ray class group).** A *ray class group of $K$ modulo $M$* is a finite abelian group $G$ with a map $\mathrm{cl}$ from the ideals of $\mathcal{O}_K$ to $G$ with these properties.

1. If $I$ and $J$ are nonzero ideals coprime to $M$, then $\mathrm{cl}(IJ) = \mathrm{cl}(I) + \mathrm{cl}(J)$.
2. Each $g \in G$ is $\mathrm{cl}(I)$ for some nonzero ideal $I$ coprime to $M$.
3. If $I$ and $J$ are nonzero ideals coprime to $M$, then $\mathrm{cl}(I) = \mathrm{cl}(J)$ if and only if $(a)I = (b)J$ for some nonzero $a, b \in \mathcal{O}_K$ with $a \equiv b \equiv 1 \pmod{M\mathcal{O}_K}$.

Such a group exists: the group of fractional ideals coprime to $M$ modulo the principal ideals $(a/b)$ with $a \equiv b \equiv 1 \pmod M$ is one. For $M = 1$ it is the [[ideal class group|WQ46BD3ARY]]. Property 3 says that two ideals have the same class if and only if their quotient has a generator that is congruent to $1$ modulo $M$. Fix a ray class group $(G, \mathrm{cl})$.

**Definition 2.2.3 (Ray class counts).** For $g \in G$ and $n \geq 0$, let $\mathcal{I}(g, n)$ be the set of nonzero ideals $I$ of $\mathcal{O}_K$ coprime to $M$ with $N(I) = n$ and $\mathrm{cl}(I) = g$. For a nonzero ideal $I$, let $\Lambda_K(I) = \log N(\mathfrak{p})$ if $I = \mathfrak{p}^k$ for a nonzero prime ideal $\mathfrak{p}$ and some $k \geq 1$, and $\Lambda_K(I) = 0$ otherwise. Put
$$a(g, n) = |\mathcal{I}(g, n)|, \qquad \lambda(g, n) = \sum_{I \in \mathcal{I}(g, n)} \Lambda_K(I).$$

The function $\Lambda_K$ is the von Mangoldt function of $K$: unique factorization of ideals gives $\log N(I) = \sum_{J \mid I} \Lambda_K(J)$.

**Theorem 2.2.4 (The ray class family).** Let $d$ be a prime with $d \equiv 3 \pmod 4$ and $d \geq 100$, and let $M \geq 3$. Then there is a family of ray class type with $B = 4dM^2$ such that every prime $p$ with $\lambda(0, p) \neq 0$ is a norm-one prime for $(d, M)$.

Lean: `GlobalTheory.Hk.exists_lFam_ray` (also `GlobalTheory.T.exists_lFam_normOne_of_mod_four_eq_three`, a second name).

We use three facts. The first two are proved elsewhere in the development; we prove the third.

**Proposition 2.2.5 (Ideals in a ray class as lattice points).** Let $g \in G$. There are real numbers $\alpha, \gamma \geq 1$ and $l, \theta_1, \theta_2$ with $\alpha\gamma = dM^4/4$ such that the form
$$Q(v) = \alpha(v_1 + \theta_1 + l v_2)^2 + \gamma(v_2 + \theta_2)^2$$
takes only positive integer values on $\mathbb{Z}^2$, and $a(g, n)$ is the number of $v \in \mathbb{Z}^2$ with $Q(v) = n$, for every $n$. As a consequence, for every $y \geq 1$,
$$\Bigl|\sum_{1 \leq n \leq y} a(g, n) - \frac{2\pi}{\sqrt{d}\, M^2}\, y\Bigr| \leq 10\sqrt{y},$$
and for $0 < t \leq 1$,
$$\Bigl|\sum_{n \geq 0} a(g, n) e^{-tn} - \frac{2\pi}{\sqrt{d}\, M^2\, t}\Bigr| \leq (4dM^2)^{10}\, t.$$

Lean: `GlobalTheory.T.rayClassIdealCount_eq_ncard_shiftedBinaryForm`, `GlobalTheory.Hk.rayCountTheta`.

The ellipse $\{Q \leq y\}$ has area $\pi y/\sqrt{\alpha\gamma} = 2\pi y/(\sqrt{d} M^2)$. So the main term is the area, and the error is the error of a lattice point count in an ellipse.

**Proposition 2.2.6 (Class number bound).** $|G| \leq h_K M^2 \leq 4|d_K| M^2 = 4dM^2$, where $h_K$ is the class number of $K$.

Lean: `GlobalTheory.Hk.card_ray_le`.

**Proposition 2.2.7 (Real characters of the ray class group).** Let $\varepsilon : G \to \{\pm 1\}$ be a homomorphism. Put $A(n) = \sum_g a(g, n)$ and $A_\varepsilon(n) = \sum_g \varepsilon(g) a(g, n)$. Then for every $n$,
$$0 \leq \sum_{de = n} A(d) A_\varepsilon(e) \quad \text{and} \quad A(n) \leq \sum_{de = n^2} A(d) A_\varepsilon(e).$$

Lean: `GlobalTheory.Hk.RaySq.conv_real_char`.

*Proof.* Let $f(J) = \varepsilon(\mathrm{cl}\, J)$ if $J$ is coprime to $M$ and $f(J) = 0$ otherwise. Then $f$ is completely multiplicative on nonzero ideals, with values in $\{0, 1, -1\}$. For a nonzero ideal $C$ put $r(C) = \sum_{J \mid C} f(J)$. Expanding the products, $\sum_{de = n} A(d) A_\varepsilon(e)$ is the sum of $f(J')$ over the pairs $(J, J')$ of ideals coprime to $M$ with $N(JJ') = n$. Group the pairs by $C = JJ'$. This gives $\sum_{de = n} A(d)A_\varepsilon(e) = \sum_{C} r(C)$, where $C$ runs over the ideals coprime to $M$ of norm $n$. The function $r$ is multiplicative, and $r(\mathfrak{p}^k) = \sum_{j=0}^k x^j$ with $x = f(\mathfrak{p}) \in \{0, 1, -1\}$. This sum is $1$, $k+1$, or $0$ or $1$ according to $x = 0, 1, -1$. So $r(C) \geq 0$, and $r(C^2) \geq 1$, since all exponents of $C^2$ are even. The first inequality follows. For the second, $I \mapsto I^2$ maps the ideals coprime to $M$ of norm $n$ injectively to the ideals coprime to $M$ of norm $n^2$, and $r(I^2) \geq 1$. $\square$

*Proof of the theorem.* Take $G$ and $a, \lambda$ as above, $B = 4dM^2$ and $\kappa = 2\pi/(\sqrt{d} M^2)$. We check the properties of a family in the order of Section 1.

1. $B \geq 4$ is clear, and $|G| \leq B$ is the class number bound. Since $d \geq 100$ and $M \geq 3$, we have $\kappa \leq 2\pi/90 \leq 4$. Also $\kappa \geq 1/B$ means $8\pi d \geq \sqrt{d}$, which holds.
2. No nonzero ideal has norm $0$, so $a(g, 0) = 0$. The only ideal of norm $1$ is $\mathcal{O}_K$, and its class is $0$, so $a(0, 1) = 1$ and $a(g, 1) = 0$ for $g \neq 0$.
3. and 4. These are the lattice point estimates of the first proposition.
5. Clearly $\lambda \geq 0$. The sum $\sum_g \lambda(g, n)$ is the sum of $\log N\mathfrak{p}$ over the prime powers $\mathfrak{p}^k$ coprime to $M$ with $N(\mathfrak{p}^k) = n$. It is $0$ unless $n = p^j$ for a rational prime $p$. If $p$ splits, there are two primes above $p$, each of norm $p$, and each has at most one power of norm $n$; the sum is at most $2\log p$. If $p$ is inert, there is one prime of norm $p^2$, and the sum is at most $2\log p$. If $p$ ramifies, the sum is at most $\log p$. In all cases the sum is at most $2\Lambda(n)$.
6. Let $I \in \mathcal{I}(g, n)$. Then $\log n = \log N(I) = \sum \Lambda_K(J)$, over the factorizations $I = JI'$ with $J$ a prime power. Here $J$ and $I'$ are coprime to $M$, and $\mathrm{cl}(I') = g - \mathrm{cl}(J)$. Sort the pairs $(J, I')$ by $h = \mathrm{cl}(J)$ and by $d = N(J)$, $e = N(I')$. This gives $a(g, n)\log n = \sum_h \sum_{de = n} \lambda(h, d)\, a(g - h, e)$.
7. Let $\chi$ be a character of $G$ with $\chi^2 = 1$. Then $\chi$ takes the values $\pm 1$, so $\mathrm{Re}\,\chi = \chi$ is a homomorphism to $\{\pm 1\}$. The two inequalities are those of the proposition on real characters.

It remains to check the property of the primes. Let $p$ be prime with $\lambda(0, p) \neq 0$. Then some prime power $\mathfrak{p}^k$ coprime to $M$ has norm $p$ and class $0$. So $k = 1$ and $\mathfrak{p}$ is a prime of degree one. By property 3 of the ray class group, $(a)\mathfrak{p} = (b)$ with $a \equiv b \equiv 1 \pmod M$. Then $\alpha = b/a$ lies in $\mathcal{O}_K$, generates $\mathfrak{p}$, and $a(\alpha - 1) = b - a \in M\mathcal{O}_K$. Since $(a)$ is coprime to $M$, we get $\alpha \equiv 1 \pmod M$. Now $N(\alpha) = p$, and the remark after the definition of norm-one primes shows that $p$ is a norm-one prime. $\square$

**Remark 2.2.8 (Formalization).** The lattice point proposition and the class number bound are separate formal results, and we have not followed their proofs. The count in ellipses is `GlobalTheory.T.abs_ncard_qForm_le_sub_pi_div_sqrt_mul_le_ten_sqrt`, and the class number bound uses `GlobalTheory.classNumber_le_four_mul_abs_discr`. The property of the primes is part of `GlobalTheory.Hk.LamRay.lamRay_props`. The constant $\kappa = 2\pi/(\sqrt{d} M^2)$ is the same for every class $g$ ([ExistsLFamRay.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsLFamRay.lean#L101)). The class number bound $h_K \leq 4|d_K|$ is very weak, but a polynomial bound in $d$ is all that is needed. The ray class group used is the one built from fractional ideals ([NonemptyRayDataOfNeZero.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonemptyRayDataOfNeZero.lean#L200)); it is written multiplicatively there, and the family uses its additive copy.
