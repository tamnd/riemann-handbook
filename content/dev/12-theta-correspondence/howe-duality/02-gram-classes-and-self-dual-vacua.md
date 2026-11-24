---
title: Gram classes and self-dual vacua
decls:
  - GlobalTheory.Hk3.HoweG.gramClass_sum_mem_span_selfDual_vac
  - GlobalTheory.T.gram_class_translate_sum_mem_span_selfDual_lattice_vacua
  - GlobalTheory.Hk3.HoweG.gramClass_orbit_mod_lower
  - GlobalTheory.T.exists_conjugateModel_extremal_dual_parameter
---
## Gram classes and self-dual vacua

This section works in a lattice model of the [[Weil representation|H3Q2703KKV]] of an unramified unitary dual pair $U(J_S) \times U(J_T)$. Its first theorem writes a sum of translates of the vacuum, taken over one Gram class, as a combination of vacua of self-dual lattices. Its second theorem reads this as a statement in the representation: the span of the $U(J_S)$-orbit of the vacuum contains a nonzero vector that, modulo translates of smaller lattice index, lies in the span of one orbit of the integral group $U(J_T)(\mathcal{O})$. This is the height step of [unramified Howe duality](/entry/howe-unram-holds/) in the next section. We keep the notation of the [previous section](/entry/witt-mod-pow/): $L$, $\mathcal{O}$, an unramified involution $(\varpi, \sigma, q)$, Hermitian $J_S \in GL_n(\mathcal{O})$ and $J_T \in GL_{n'}(\mathcal{O})$, domination, Gram classes and the lattice index $\operatorname{idx}$.

### The lattice model

Let $X = M_{n' \times n}(L)$ and write $X(\mathcal{O})$ for the integral matrices. For $x, y \in X$ and a unit $\delta$ put $H(x, y) = \delta \operatorname{tr}(J_S^{-1} y^* J_T x)$.

**Definition 2.2.1.** Let $\delta \in L$, let $\psi$ be a character of the additive group of $L$, let $M$ be a complex vector space, let $\rho : X \to \operatorname{End}(M)$ be a map and let $\omega : U(J_S) \times U(J_T) \to \operatorname{End}(M)$ be a homomorphism of monoids. The data form a *local dual pair* if:

1. $(\varpi, \sigma, q)$ is an unramified involution with $q$ odd, and $J_S$, $J_T$ are integral and Hermitian;
2. $\delta$ is a unit with $\sigma(\delta) = -\delta$;
3. $\psi(a) = 1$ for every $a \in \mathcal{O}$ with $\sigma(a) = a$, and $\psi(\varpi^{-1} a) \neq 1$ for some such $a$;
4. $\rho(0) = 1$ and, for all $x, y \in X$,
$$\rho(x) \rho(y) = \psi\Bigl(\tfrac{H(x, y) + \sigma H(x, y)}{2}\Bigr) \rho(x + y);$$
5. $M$ is spanned by the vectors $\rho(x) s$ where $s$ is fixed by $\rho(u)$ for every $u \in X(\mathcal{O})$;
6. $\omega(g, h) \rho(x) = \rho(h x g^{-1}) \omega(g, h)$ for all $g, h, x$;
7. $\omega(g, h) s = s$ for integral $g$, $h$ and every $s$ fixed by all $\rho(u)$ with $u \in X(\mathcal{O})$.

A vector $s$ fixed by $\rho(u)$ for every $u \in X(\mathcal{O})$ is a *lattice vacuum*.

Condition 4 says that $\rho$ is a projective representation of the vector group $X$, a form of the [[Heisenberg group|ZZYCV5EX9J]] of the symplectic space $X$ (see the [Weil representation](/learn/theta/#the-weil-representation)); condition 3 says that $\psi$ has conductor $\mathcal{O}$ on $L^{\sigma}$, and conditions 6 and 7 say that $\omega$ is a compatible action of the dual pair that fixes the vacua of the standard lattice. From condition 4 and the vacuum property, for $u \in X(\mathcal{O})$ the vector $\rho(y + u) s$ is a nonzero multiple of $\rho(y) s$.

For $a \in GL_n(L)$ call $a$ *self-dual* if $a^* J_S a$ and $a^{-1} J_S^{-1} (a^{-1})^*$ are integral; then $a \mathcal{O}^n$ is a unimodular lattice for $J_S$. A vector $w$ is a *vacuum of $a$* if $\rho(u a^{-1}) w = w$ for every $u \in X(\mathcal{O})$.

### Averaging over a Gram class

**Lemma 2.2.2.** Let $B$ be a finite abelian group, $Y$ a finite set, $x \in Y$, and let $\chi : B \times Y \to \mathbb{C}^{\times}$ be multiplicative in $b$ for each $y \in Y$. Then for vectors $v_y$ in a complex vector space,
$$\sum_{b \in B} \chi(b, x)^{-1} \sum_{y \in Y} \chi(b, y) v_y = |B| \sum_{y \in Y'} v_y,$$
where $Y' = \{y \in Y : \chi(b, y) = \chi(b, x) \text{ for all } b\}$.

Lean: `GlobalTheory.Hk3.HoweG.sum_charSum_eq_card_filter`

*Proof.* Exchange the sums. For fixed $y$, the map $b \mapsto \chi(b, x)^{-1} \chi(b, y)$ is a character of $B$; it is trivial exactly when $y \in Y'$, and otherwise its sum over $B$ is $0$ by [[orthogonality of characters|S6ARZ7M1YE]]. $\square$

**Theorem 2.2.3 (Gram class sums are combinations of self-dual vacua).** Let the data form a local dual pair, and suppose also that $L$ has characteristic $0$ and is complete. Let $s$ be a lattice vacuum and let $x \in X$ with $x J_S^{-1} x^*$ integral. Then there are a finite set $C \subset X$ and numbers $c_y \in \mathbb{C}$ such that $x \in C$; for every $y \in C$, $c_y \neq 0$, $y$ is dominated by $x$, and $x$ and $y$ have the same Gram class; two distinct elements of $C$ are not congruent modulo $X(\mathcal{O})$; and
$$\sum_{y \in C} c_y \rho(y) s$$
lies in the span of the vacua of the self-dual matrices $a \in GL_n(L)$.

Lean: `GlobalTheory.Hk3.HoweG.gramClass_sum_mem_span_selfDual_vac` (also `GlobalTheory.T.gram_class_translate_sum_mem_span_selfDual_lattice_vacua`, a second name)

*Proof.* Since $x J_S^{-1} x^*$ is integral, there is a self-dual $a$ adapted to $x$: $y$ is dominated by $x$ exactly when $y a$ is integral, the integral vectors $v$ with $x v$ integral are those of $a \mathcal{O}^n$, and the lattice $a \mathcal{O}^n + \mathcal{O}^n$ is $\mathcal{O}^n + x^{\dagger} \mathcal{O}^{n'}$. Take a finite set $Y$ of representatives, modulo $X(\mathcal{O})$, of the matrices dominated by $x$, with $x \in Y$. Next comes a finite abelian group $B$, a self-dual matrix $a_b$ for each $b \in B$, and integral shifts $l(b, y)$, such that for each $b$ the matrices $y + l(b, y)$ with $y \in Y$ represent the classes that make up the vacuum of $a_b$. Then the vector
$$\sum_{y \in Y} \rho(y + l(b, y)) s$$
is a vacuum of $a_b$. By the shift rule for lattice vacua it equals $\sum_y \chi(b, y) \rho(y) s$ with
$$\chi(b, y) = \psi\Bigl(-\tfrac{H(y, l(b, y)) + \sigma H(y, l(b, y))}{2}\Bigr).$$
These numbers are multiplicative in $b$, and $\chi(b, y) = \chi(b, x)$ for all $b$ holds exactly when $x$ and $y$ have the same Gram class. The lemma, with $v_y = \rho(y) s$, gives that $|B| \sum_{y \in Y'} \rho(y) s$ is a combination of vacua of the $a_b$. Take $C = Y'$ and $c_y = 1$. $\square$

### A nonzero vector modulo smaller index

**Theorem 2.2.4 (Orbit modulo lower index).** Let the data form a local dual pair, with $L$ of characteristic $0$ and complete. Let $s \neq 0$ be a lattice vacuum such that the vectors $\rho(x) s$ with $x \in X$ span $M$, and let $x \in X$ with $x J_S^{-1} x^*$ integral. Then there are
$$v \in \operatorname{span}\{\omega(g, 1) s : g \in U(J_S)\}, \qquad u \in \operatorname{span}\{\rho(y) s : \operatorname{idx}(y) < \operatorname{idx}(x)\}$$
with $v - u \neq 0$ and
$$v - u \in \operatorname{span}\{\rho(h x) s : h \in U(J_T) \text{ integral}\}.$$

Lean: `GlobalTheory.Hk3.HoweG.gramClass_orbit_mod_lower` (also `GlobalTheory.T.exists_conjugateModel_extremal_dual_parameter`, a second name)

*Proof.* Take $C$ and $c_y$ from the previous theorem and put $v = \sum_{y \in C} c_y \rho(y) s$.

First, every vacuum $w$ of a self-dual $a$ lies in the span of the $U(J_S)$-orbit of $s$. Indeed $a = g k$ with $g \in U(J_S)$ and $k$ integral, since all unimodular lattices for $J_S$ are in one orbit. By condition 6 the vector $\omega(g^{-1}, 1) w$ is a lattice vacuum. The lattice vacua form the line through $s$, since $\rho(x) s$ span $M$; so $w$ is a multiple of $\omega(g, 1) s$. Hence $v$ lies in the span of the orbit.

Let $u$ be the part of the sum over the $y$ with $\operatorname{idx}(y) \neq \operatorname{idx}(x)$. Domination gives $\operatorname{idx}(y) \leq \operatorname{idx}(x)$, so these $y$ have smaller index. The rest $v - u$ is the sum over the $y \in C$ with $\operatorname{idx}(y) = \operatorname{idx}(x)$. For such $y$, the [integral unitary theorem](/entry/exists-int-unitary-of-gram-class/) gives an integral $h \in U(J_T)$ with $y - h x$ integral, and then $\rho(y) s$ is a nonzero multiple of $\rho(h x) s$. So $v - u$ lies in the span of the integral orbit of $x$.

Finally $v - u \neq 0$. The vectors $\rho(y) s$ for $y$ in distinct classes modulo $X(\mathcal{O})$ lie in independent subspaces, the elements of $C$ are pairwise incongruent, $x \in C$, and $c_x \rho(x) s \neq 0$ because $c_x \neq 0$ and $\rho(x)$ is invertible. $\square$

**Remark 2.2.5 (Formalization).** The local dual pair is the structure `LocPair` and the lattice vacuum is `LocVac`, both in [NormalFam.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/NormalFam.lean#L166). The first theorem and the lemma are in [GramClassTranslateSumMemSpanSelfDualLatticeVacua.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/GramClassTranslateSumMemSpanSelfDualLatticeVacua.lean#L58), the second in [ExistsConjugateModelExtremalDualParameter.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsConjugateModelExtremalDualParameter.lean#L16). The names in `GlobalTheory.T` are restatements proved by applying these ([GramClassTranslateSumMemSpanSelfDualLatticeVacuaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/GramClassTranslateSumMemSpanSelfDualLatticeVacuaStatement.lean#L8), [ExistsConjugateModelExtremalDualParameterStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsConjugateModelExtremalDualParameterStatement.lean#L7)); the second of them has a name about conjugate models and extremal parameters that does not describe its statement. The coefficients produced by the first theorem are all $1$. The group $U(J)$ is a subgroup of `GL`, and the action $\omega$ is a monoid homomorphism into `Module.End ℂ M`, so no topology or smoothness enters.
