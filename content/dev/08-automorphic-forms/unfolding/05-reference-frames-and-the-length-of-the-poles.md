---
title: Reference frames and the length of the poles
decls:
  - PI.ScRefExists.Top.target_of_wframe
  - PI.PoleLengthCount.pole_length_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reference frames and the length of the poles

This section proves two results of Volume 10 that the period integrals use next to the unfolding. The first builds a reference frame for a hermitian lattice modulo an integer $g$ from Witt frames at the primes: a hyperbolic part, an anisotropic vector, and weight vectors cut out by an idempotent. It gives [the existence of a reference frame](/entry/sc-reference-exists/). The second bounds the [[length|CZSCNZH8VY]] of the module of poles of a lifted family by a binomial coefficient times a weighted count of points. It gives [the length bound for the poles](/entry/length-pole-t0/).

### Witt frames and reference frames

Let $E/F$ be a CM extension with ring of integers $\mathcal{O}_E$ and involution $a \mapsto \bar a$, let $L \subset E^n$ be a lattice, and let $h$ be a [hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) on $E^n$. For a prime number $p$ let $\mathcal{O}_E^{(p)}$ be the ring of $x \in E$ such that $sx \in \mathcal{O}_E$ for an integer $s$ prime to $p$, and let $L^{(p)}$ be the $\mathcal{O}_E^{(p)}$-span of $L$. A family $e_1, \dots, e_r$, $f_1, \dots, f_r$ is *hyperbolic* if $h(e_a, e_b) = 0$, $h(f_a, f_b) = 0$ and $h(e_a, f_b) = \delta_{ab}$.

**Definition 5.5.1 (Witt frames exist).** We say that *Witt frames exist* if the following holds for every lattice $L$, every prime $p$, all $r, k$ with $n = 2r + k + 1$, every hyperbolic family $e, f$ and every integer $M$ prime to $p$ with $Me_a, Mf_a \in L$: there are $w_0, \dots, w_k$ and $w'_0, \dots, w'_k$ in $L^{(p)}$, orthogonal to all $e_a$ and $f_a$, with $h(w'_i, w_j) = \delta_{ij}$, such that every $y \in L$ lies in the $\mathcal{O}_E^{(p)}$-span of the $e_a$, $f_a$, $w_i$ and in the $\mathcal{O}_E^{(p)}$-span of the $e_a$, $f_a$, $w'_i$.

So locally at $p$ the lattice splits as a hyperbolic part and a part with a pair of dual bases. This is the local [[Hermitian form|48P4A1CX85]] theory over the semilocal ring $\mathcal{O}_E^{(p)}$, which is a principal ideal ring.

**Definition 5.5.2 (Reference frame).** Let $g \geq 1$ be an integer. A *reference frame* of $L$ modulo $g$ for a hyperbolic family $e, f$ consists of vectors $e^0_a$, $f^0_a$, $z_0 \in L$, vectors $b_1, \dots, b_k$ and $b'_1, \dots, b'_k$ in $L$, and an element $\varepsilon \in \mathcal{O}_E$ such that:

1. $e^0$, $f^0$ approximate $e$, $f$, and the Gram matrix of all these vectors is integral;
2. $h(z_0, z_0) + 1 \equiv 0 \bmod g$, and $z_0$ is orthogonal to $e^0$ and $f^0$ modulo $g$;
3. $\varepsilon^2 = \varepsilon$, $\varepsilon\bar\varepsilon = 0$, and $(1 - \varepsilon - \bar\varepsilon)L \subseteq gL$;
4. $b_j = \varepsilon b_j$, $b'_j = \bar\varepsilon b'_j$, and $h(b'_i, b_j) \equiv \delta_{ij}\varepsilon \bmod g$;
5. $L$ is spanned by these vectors modulo $gL$.

**Theorem 5.5.3 (Reference frames).** Assume that Witt frames exist. Let $g \geq 1$ be such that every prime of $F$ dividing $g$ has exactly two primes of $E$ above it. Let $n = 2r + k + 1$, let $e, f$ be a hyperbolic family, and let $c e_a$ and $c f_a$ lie in $L$ for some integer $c$ prime to $g$. Then $L$ has a reference frame modulo $g$ for $e, f$.

Lean: `PI.ScRefExists.Top.target_of_wframe`.

*Proof.* There are four steps.

Step 1 (a local idempotent). Since every prime dividing $g$ splits in $E$, the ring $\mathcal{O}_E/g$ is a product of two copies of $\mathcal{O}_F/g$ exchanged by the involution. So there is $\theta \in \mathcal{O}_E$ with $\theta^2 \equiv \theta$, $\theta\bar\theta \equiv 0$ and $1 - \theta - \bar\theta \equiv 0 \bmod g$.

Step 2 (lifting). There is $\varepsilon \in \mathcal{O}_E$ with $\varepsilon^2 = \varepsilon$, $\varepsilon\bar\varepsilon = 0$ and $\varepsilon \equiv \theta \bmod g$. An element integral at every finite place is in $\mathcal{O}_E$, by the [local global principle](/learn/number-fields/#places-and-completions) for integrality.

Step 3 (prime powers). For $g = p^a$, Witt frames at $p$ give $w$, $w'$ with dual Gram matrix. Choose $z \in L$ in their span with $h(z, z) + 1 \equiv 0 \bmod p^a$; put $b = \theta w$ and $b' = \bar\theta w'$. Then $\theta h(z, b_i) \equiv 0$, $\bar\theta h(z, b'_i) \equiv 0$, $\theta(h(b'_i, b_j) - \delta_{ij}) \equiv 0$, and $L$ lies in the span of $e$, $f$, $z$, $\theta b$, $\bar\theta b'$ plus $p^aL$.

Step 4 (gluing). For coprime $g_1$ and $g_2$ the data modulo $g_1$ and $g_2$ glue by the Chinese remainder theorem to data modulo $g_1g_2$. With the idempotent of Step 2, this gives a reference frame modulo $g$. $\square$

### The length of the poles

Let $\mathcal{O}$ be a discrete valuation ring with fraction field $K$, let $A$ be a reduced finite $K$-algebra, and let $A_s$ be the integral closure of $\mathcal{O}$ in $A$, finite over $\mathcal{O}$. Let $\mathrm{Pts}$ be the set of maximal ideals $\zeta$ of $A_s$, and assume that $A_s$ is a [discrete valuation ring](/learn/commutative-algebra/#regular-local-rings-and-discrete-valuation-rings) at each $\zeta$, with valuation $\operatorname{ord}_\zeta$. Let $f_\zeta$ be the degree of the residue field of $\zeta$ over that of $\mathcal{O}$.

**Definition 5.5.4 (Ball).** Let $V$ be a free $A$-module of rank one with generator $e$, so each $v \in V$ is $a e$ for a unique coordinate $a \in A$. For a function $c \colon \mathrm{Pts} \to \mathbb{Z}$ the *ball* $\mathrm{B}(c)$ is the $A_s$-span of the $v$ with $\operatorname{ord}_\zeta(a) + c(\zeta) \geq 0$ for all $\zeta$.

**Lemma 5.5.5 (Length of a ball quotient).** For $c$ and $m \geq 0$,
$$\operatorname{length}_{\mathcal{O}} \big(\mathrm{B}(c + m) / \mathrm{B}(c)\big) = \sum_{\zeta} m(\zeta) f_\zeta.$$

*Proof.* The quotient is the direct sum over $\zeta$ of $\varpi_\zeta^{-c(\zeta)-m(\zeta)}A_{s,\zeta}/\varpi_\zeta^{-c(\zeta)}A_{s,\zeta}$, which has a filtration with $m(\zeta)$ steps, each a copy of the residue field of $\zeta$, of length $f_\zeta$ over $\mathcal{O}$. $\square$

Now let a family of the period integrals of Volume 10 be given at a prime $\lambda$ of the coefficient field, with local ring $\mathcal{O}$, an integer $T$, and the dimension $d$ of its parameter space. It gives two modules: the module $A_T$ of integral values and the module $A'_T(m) \supseteq A_T \cap A'_T(m)$ of values with poles of multiplicity at most $m(\zeta)$ at the points $\zeta$.

**Theorem 5.5.6 (Length of the poles).** Let the local point data be good for the scaling, the constant $C$, $T$ and $c$, and let all weights of the family lie in the admissible weight set. Assume that the data lie in the lift for $T$. Then
$$\begin{aligned} \operatorname{length}_{\mathcal{O}}\big(A'_T(m) / A_T \cap A'_T(m)\big) &\leq \binom{T-1}{d} \sum_{\zeta} m(\zeta)\, f_\zeta. \end{aligned}$$

Lean: `PI.PoleLengthCount.pole_length_bound`.

*Proof.* Put $a_0 = T - d$. There is a decreasing filtration $F_k$ of $A'_T(m)$ with $F_0$ everything and $F_{a_0} = 0$. For $k < a_0$ the graded map $\psi_k$ sends $F_k$ into $P_k = \prod \mathrm{B}(c + m)$, a product over the monomials of degree $k$ in $d$ variables, and its image contains $Q_k = \prod \mathrm{B}(c)$ on the integral part. By the lemma,
$$\operatorname{length}(P_k / Q_k) = N(d, k) \sum_\zeta m(\zeta) f_\zeta,$$
where $N(d, k)$ is the number of monomials of degree $k$ in $d$ variables. The length of the quotient is at most the sum over $k < a_0$ of these lengths. Finally
$$\sum_{k < T - d} N(d, k) = \binom{T-1}{d}$$
when $d < T$, by the hockey stick identity; when $d \geq T$, $a_0 = 0$ and the left side of the bound is $0$. $\square$

**Remark 5.5.7 (Formalization).** The hypothesis that the data lie in the lift for $T$ is not used; the statement follows from a version without it. In the frame theorem, the proofs of Steps 1 to 4 are proved results that we did not unfold, in particular the gluing at prime powers; we have not opened the definitions of the lattice of an automorphic instance. In the pole theorem we did not unfold the definitions of $A_T$, $A'_T(m)$ or the graded maps; the sketch follows their stated properties. See [TargetOfWframe.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LatticeReferenceFrame/TargetOfWframe.lean#L13) and [LengthPoleInLift.lean](lean:Formalism/PeriodIntegrals/LengthPoleInLift.lean#L17).
