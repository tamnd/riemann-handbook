---
title: Theta series span the cusp forms of a row
decls:
  - GlobalTheory.AdSpan.range_thF
  - GlobalTheory.AdSpan.value_mem_span
  - GlobalTheory.AdSpan.span_any
  - GlobalTheory.AdSpan.span_std
  - GlobalTheory.T.thetaLiftFiniteVector_eq_translate_levelDatum
  - GlobalTheory.LiftLevel.thP_vec_eq_translate
  - GlobalTheory.T.thetaLift_level_datum_sum_of_translates
  - GlobalTheory.LiftLevel.lift_level_datum
  - GlobalTheory.T.mem_span_thetaSeries_of_boundedHolomorphic
  - GlobalTheory.AdSpan.mem_span_thetaSet_of_holUpTo
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta series span the cusp forms of a row

This section proves that the theta lift from a large definite Hermitian space onto a row of the tower is onto the cusp forms of the given discrete series type and level. The proof has three parts. First, a theta level vector is a finite adelic translate of a sum of Heisenberg translates of one base vector. Second, a bounded function on the unitary group that is holomorphic up to a real scalar is in the span of theta series built from that sum. Third, the value of a cusp form at an extremal lowest $K$-type vector has these properties. The result feeds the step [the nonempty hypotheses](/step/nonempty-hyps/). Background is in [the global theta lift](/learn/theta/#the-global-theta-lift), [the Fock model](/learn/theta/#the-fock-model) and [Hermitian lattices](/learn/groups/#hermitian-lattices-and-the-mass-formula).

### Level data

We keep the notation of [the section on isotropic means](/entry/isotropic-integrals-determine-theta-mean-products/): $E$ is a CM field over the totally real field $F$, $V$ and $W$ are Hermitian spaces over $E$ of ranks $n$ and $r$ with $r \le n$, and $\mathbb{W} = M_{r \times n}(\mathbb{A}_E)$ carries the symplectic form, the Heisenberg operators $\rho(w)$ and a Weil representation $\omega$ of $U(V)(\mathbb{A}) \times U(W)(\mathbb{A})$. Let $\Lambda \subset E^r$ be the lattice of the context and let $\Lambda_0 \subset E^n$ be the standard lattice. For lattices $L_1 \subset E^n$ and $L_2 \subset E^r$ let $L_1 \otimes L_2$ be the tensor lattice in $M_{n \times r}(E)$, and let $\widehat{L}$ be the closure of a lattice $L$ in the finite adeles.

**Definition 8.5.1 (Level datum).** A *level datum* for $\Lambda$ consists of:

1. an ideal $\mathfrak{m}$ of $\mathcal{O}_E$ with $\mathfrak{m} \ne 0$, $\mathfrak{m} \ne \mathcal{O}_E$, such that $\mathfrak{m}$ is coprime to $\bar{\mathfrak{m}}$ and to $2$;
2. vectors $\beta_1, \dots, \beta_r \in \Lambda$ with $\Lambda \subset \sum_i \mathcal{O}_E \beta_i + \mathfrak{m}\Lambda$;
3. a subgroup $J$ of $\mathrm{GL}_r(\mathcal{O}_E/\mathfrak{m})$ and a character $\lambda$ of $J$;
4. an integral element $w \in E$ with $w + \bar w = 1$;
5. a lattice $\mathrm{sh}(\Lambda)$ and a coefficient function $d$ on $M_{n \times r}(E)$, which we do not unfold.

For $\kappa \in J$, an element $k \in U(W)(\mathbb{A}_f)$ is *in the level group at $\kappa$* if $k$ maps $\widehat{\Lambda}$ onto itself and there is a matrix $\kappa'$ over $\mathcal{O}_E$ that reduces to $\kappa$ modulo $\mathfrak{m}$ with $k \beta_i - \sum_j \kappa'_{ji} \beta_j \in \widehat{\mathfrak{m}\Lambda}$ for each $i$.

**Definition 8.5.2 (Level sum).** Let $\Lambda_1 = (2\bar{\mathfrak{m}})\Lambda$ and $\Lambda_2 = (2\bar{\mathfrak{m}}\mathfrak{m})\Lambda$. For a function $f'$ on $\mathbb{W}$ the *level sum* of $f'$ is

$$u_{\mathfrak{m}}(f') = \sum_{c} d(-c)\, \rho(c) f',$$

where $c$ runs over representatives of $(\Lambda_0 \otimes \Lambda_1)/(\Lambda_0 \otimes \Lambda_2)$, embedded in $\mathbb{W}$ at the finite places. The vector $f'$ is a *base vector* for the datum and a basis $B$ if it is a nonzero theta function, it is a Fock vector for $B$, and it is fixed up to the standard phase by the Heisenberg operators of the closed lattice $\widehat{\Lambda_0 \otimes \mathrm{sh}(\Lambda)}$.

Let $\Lambda_W$ be a self-dual lattice for $W$, let $\beta_V$ and $\beta_W$ be frames of $\widehat{\Lambda_0}$ and $\widehat{\Lambda_W}$, let $P_g \ne \emptyset$ and $Q$ be finite sets of places of $E$ not above $2$, let $\xi_v$ be a character of the residue units at each place $v$, and let $e \in \mathbb{A}_E$ be the sum of the idempotents of the places in $P_g \cup Q$. Let $\Phi$ be the test function on $\mathbb{W}$ built from these data, and let $\bar e$ be the conjugate of $e$. A *theta level vector* is a function $f = T(\Phi)$ for each theta map $T$ of the data.

**Theorem 8.5.3 (The level test function is a sum of lattice indicators).** Assume that $\Lambda$ and $\Lambda_W$ are in the same genus. Then there are a level datum, an element $k_0 \in U(V)(\mathbb{A}_f)$, a lattice $\Lambda'$ with $k_0^{-1}\widehat{\Lambda'} = \widehat{\Lambda_0}$, and a subgroup $L \subset \mathbb{W}$ with these properties:

1. $w \bar w = 2b$ for an integral $b$, and $\mathfrak{m} \subset \bar{\mathfrak{p}}$ for each $\mathfrak{p} \in P_g$;
2. each lift $\kappa'$ of each $\kappa \in J$ is congruent to $1$ modulo $\bar{\mathfrak{p}}$ for each $\mathfrak{p} \in P_g$;
3. the class set $(\Lambda_0 \otimes \Lambda_1)/(\Lambda_0 \otimes \Lambda_2)$ is finite;
4. each $x \in L$ satisfies $\bar e x = x$, a positive multiple of $L$ lies in the standard lattice of $\mathbb{W}$, and a positive multiple of each standard lattice point $x$ with $\bar e x = x$ lies in $L$;
5. for $u$ in the closed lattice of $\Lambda' \otimes \mathrm{sh}(\Lambda)$, the part $\bar e u$ is in $L$, the character $\psi$ of the pairing of $L$ with $e u$ is trivial, and $(1 - e - \bar e)u$ is in the standard lattice;
6. for $y \in \Lambda_0 \otimes \Lambda_1$ there is $v$ in the closed lattice of $\Lambda' \otimes \mathrm{sh}(\Lambda)$ with $k_0 y = \bar e(k_0 y) + 2v$, and $\psi$ of the pairing of $\bar e(k_0 y)$ with $2v$ is $1$;
7. for all $x \in \mathbb{W}$,

$$\Phi(x) = \sum_{c} d(-c)\, \mathbf{1}_L\bigl(x + \bar e(k_0 c)\bigr).$$

Lean: `GlobalTheory.T.thetaLift_level_datum_sum_of_translates` (also `GlobalTheory.LiftLevel.lift_level_datum`, the proof).

*Proof.* The product $\mathfrak{m}$ of the conjugate place ideals of $P_g \cup Q$ is proper, odd and coprime to its conjugate. A finite unitary element $k_0$ moves the standard lattice to $\Lambda'$. Build the level datum on $\mathfrak{m}$ and take $L$ to be the lift lattice. Clauses 1 to 6 are direct lattice computations. Clause 7 sorts the support of $\Phi$ into the level classes. $\square$

**Theorem 8.5.4 (A theta level vector is a translate of a level sum).** Let $f$ be a theta level vector, and keep the assumptions of the previous theorem. Then there are a level datum, a number $M \in \mathbb{N}$, a vector $f'$ and $k_0 \in U(V)(\mathbb{A}_f)$ such that $w \bar w = 2b$ for an integral $b$, $0 < M$ and $M \in \mathfrak{m}$, $f'$ is a base vector, and

$$f = \omega(k_0, 1)\, u_{\mathfrak{m}}(f'),$$

where $u_{\mathfrak{m}}(f')$ is a nonzero theta Fock vector. Each element of the level group stabilizes $\beta_W$ and reduces to $1$ at the places of $P_g$.

Lean: `GlobalTheory.T.thetaLiftFiniteVector_eq_translate_levelDatum` (also `GlobalTheory.LiftLevel.thP_vec_eq_translate`, the proof).

*Proof.* The theta kernel of a nonzero test function is nonzero, so $f \ne 0$. Apply the previous theorem. The theta map of $\mathbf{1}_L$ is a theta function $f''$, a Fock vector and a lattice vacuum. By clause 7, $f = \sum_c d(-c)\rho(\bar e(k_0 c)) f''$. Put $f' = \omega(k_0^{-1}, 1) f''$. The Heisenberg rule of $\omega$ gives $\omega(k_0, 1)\rho(c) f' = \rho(k_0 c) f''$. By clause 6 the difference $k_0 c - \bar e(k_0 c)$ is $2v$ with $v$ in the lattice, and $\rho(2v)$ fixes $f''$ with trivial phase. This gives the formula. The Fock and lattice vacuum properties move along $\omega(k_0^{-1}, 1)$. Take $M$ to be the absolute norm of $\mathfrak{m}$. The last claim is the stabilizer property of the level group. $\square$

### Bounded holomorphic functions

Let $B$ be a good basis at the infinite places. For a test function $\varphi$ let $\Theta_B(\varphi)$ be the theta vector of $\varphi$ in the Fock model of $B$, and for $a \in U(W)(F_\infty)$ let $aB$ be the moved basis. Let $x_B$ be the point of the symmetric domain $\mathcal{D}$ of $U(W)$ given by $B$.

**Definition 8.5.5 (Real scalar).** A function $z$ on $U(W)(\mathbb{A})$ is a *real scalar* for $B$ if for each $a \in U(W)(F_\infty)$ and each standard test function $\varphi$,

$$\omega(1, a)\, \Theta_B(\varphi) = z(a)\, \Theta_{aB}(\varphi).$$

**Definition 8.5.6 (Holomorphic up to a scalar).** Let $\lambda$ be a weight. A function $\phi$ on $U(W)(\mathbb{A})$ is *holomorphic up to $z$ of weight $\lambda$* if for each $g$ there is a function $Q_g$ on frames, holomorphic on $\mathcal{D}$, with $Q_g(xb) = \chi_\lambda(b)\, Q_g(x)$ for $x \in \mathcal{D}$ and $b$ in the Borel subgroup, and with $\phi(ga) = z(a)\, Q_g(x_{aB})$ for $a \in U(W)(F_\infty)$.

For exponent vectors $c, c'$ let $\lambda(c, c')$ be the weight they define, and let $\mathcal{H}(c, c')$ be the space of row-highest pluriharmonic polynomials of exponents $c, c'$. For a vector $u$, the *theta set* $\Theta(u; c, c')$ is the set of functions $g \mapsto \omega(h, g)\, u_P(0)$, where $h \in U(V)(\mathbb{A})$, $P$ has harmonic part in $\mathcal{H}(c, c')$, and $u_P$ is the Fock polynomial vector of $u$ and $P$.

**Theorem 8.5.7 (Bounded holomorphic functions are sums of theta series).** Let $\omega$ be a weak Weil representation, and assume $4[E : \mathbb{Q}]\, r + 4 \le n$. Take a level datum with $w \bar w = 2b$ for an integral $b$, a number $M > 0$ with $M \in \mathfrak{m}$, a good basis $B$ and a base vector $f'$. Let $u = u_{\mathfrak{m}}(f')$. Let $z$ be a real scalar for $B$, and let $\phi$ be holomorphic up to $z$ of weight $\lambda(c, c')$. Assume:

1. $\phi(\gamma g) = \phi(g)$ for $\gamma \in U(W)(F)$;
2. for each $\kappa \in J$ and each $k$ in the level group at $\kappa$, $\omega(1, k)u = u$ and $\phi(gk) = \phi(g)$;
3. $\phi$ is bounded.

Then $\phi$ lies in the span of $\Theta(u; c, c')$.

Lean: `GlobalTheory.T.mem_span_thetaSeries_of_boundedHolomorphic` (also `GlobalTheory.AdSpan.mem_span_thetaSet_of_holUpTo`, the proof).

*Proof.* Choose vacua and multipliers for the lattices of the level. The vector $u$ is a nonzero multiple $t\,u_0$ of the theta vector $u_0$ of the level test function. For each lattice $L'$ in the genus of the level choose $g_{L'}$ that moves $\Lambda$ to $L'$ and is trivial at the level. The functions $Q_{g_{L'}}$, divided by the multipliers, form a family $F$ of holomorphic forms on $\mathcal{D}$ of weight $\lambda(c, c')$ for the level group. They are automorphic since $\phi$ is left invariant, and bounded since $\phi$ is bounded. The size bound gives the classical theta span: $F$ is a finite combination of theta series with pluriharmonic coefficients $P_1, \dots, P_m$ for lattices $L_1, \dots, L_m$. Transport each $L_i$ to the standard lattice by an element $h_i$ that is trivial at the level, and pick polynomials with harmonic parts $P_i$. This gives a function $\psi$ in the span of $\Theta(u; c, c')$. Then $\psi$ is left invariant and level invariant, and $\phi(g_{L'} a) = \psi(g_{L'} a)$ for each $L'$ and each real $a$. Two such functions that agree on these sets are equal, by strong approximation and the finiteness of the genus. $\square$

### The range of the definite lift

**Theorem 8.5.8 (Span at the standard frame).** Let $\omega$ be a weak Weil representation whose action on theta functions is continuous, let the signatures of $W$ be admissible, and assume $4[E : \mathbb{Q}]\, r + 4 \le n$. Let $f$ be a theta level vector for the standard frame and a good basis $B_0$. Let $p, q$ be the signature, let $\Delta$ be the row-highest determinant polynomial of $p, q$ and some exponents, and let $U$ be a space of polynomials with $\Delta \in U$ that is stable under $\omega(h, 1)$ for real $h$, acting through the pure tensors $f_P$ of $f$. Let $\phi$ be a function on $U(W)(\mathbb{A})$ with:

1. $\phi$ is smooth at the real places and is killed by the lowering operators of the reversed basis;
2. for each real torus element $s$ there is $l$ with $\omega(1, s) f_\Delta = l f_\Delta$ and $\phi(gs) = l\phi(g)$;
3. $\phi$ is left invariant under $U(W)(F)$;
4. $\omega(1, k)f = f$ and $\phi(gk) = \phi(g)$ for finite $k$ that fix $\beta_W$ and reduce to $1$ at the places of $P_g$;
5. $\phi$ is bounded.

Then $\phi$ lies in the span of the functions $g \mapsto \omega(h, g) f_P(0)$ with $h \in U(V)(\mathbb{A})$ and $P \in U$.

Lean: `GlobalTheory.AdSpan.span_std`.

*Proof.* Write $f = \omega(k_0, 1)u$ by the translate theorem. Finite elements commute with the Fock polynomial vectors, so $f_P = \omega(k_0, 1) u_P$. Conditions 1 and 2 show that $\phi$ is holomorphic up to the real scalar $z = \det^m$ of weight $\lambda(c, c')$, where $c, c'$ are the exponents of $\Delta$. Conditions 3 to 5 give the remaining hypotheses of the previous theorem, which puts $\phi$ in the span of $\Theta(u; c, c')$. Each element of that set is a function $g \mapsto \omega(h, g) f_P(0)$ with $P \in U$, since $U$ contains the row-highest translates of $\Delta$. $\square$

**Theorem 8.5.9 (Span at any orthogonal frame).** The conclusion of the previous theorem holds for a theta level vector built on any orthogonal frame of $V$ with even rank, any self-dual lattice for $W$, and a discrete series model whose order matches the signature.

Lean: `GlobalTheory.AdSpan.span_any`.

*Proof.* Reframe $V$ by the given basis. This gives a context with the standard frame in which the lattices are in the same genus. This is the previous theorem applied to the reframed context. $\square$

For each row $i$ of the record, let $V_i$ be the definite space and $W_i$ the space of the row. Let $\mathcal{A}_i$ be the span of the continuous equivariant maps $T$ from the smooth vectors of the discrete series model of $W_i$ to [cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms) on $U(W_i)(\mathbb{A})$ with the level and character of the record. Let $\theta_{i,t}$ be the theta lift of the record from a finite dimensional space into these maps.

**Proposition 8.5.10 (Values at an extremal vector).** Assume that cusp forms decay rapidly and $8fr + 4 \le n$, where $2f = [E : \mathbb{Q}]$. Let $u$ be an extremal vector of the lowest $K$-type, and let $w_0$ be a vector with $\iota(u, w_0) = \Delta_i$. Then for $T \in \mathcal{A}_i$, $T(u)$ lies in the span of the functions $g \mapsto \omega_{i,t}(h, g)\, f_{i,t,P}(0)$ with $P$ in the image of $\iota(u, \cdot)$.

Lean: `GlobalTheory.AdSpan.value_mem_span`.

*Proof.* Since $4[E : \mathbb{Q}] = 8f$, the size bound holds. The function $T(u)$ is killed by the lowering operators, is a torus eigenfunction, is level invariant, and is bounded by the decay of cusp forms. Apply the span theorem at any frame. $\square$

**Theorem 8.5.11 (The definite lift is onto).** Under the hypotheses of the proposition, and if the record is built as a family with models and theta data, then $\operatorname{im} \theta_{i,t} = \mathcal{A}_i$ for each $i$ and $t$.

Lean: `GlobalTheory.AdSpan.range_thF`.

*Proof.* The inclusion $\subseteq$ is part of the theta data. For the other inclusion take an extremal vector $u$. Evaluation at $u$ is injective on $\mathcal{A}_i$, since the Petersson norm of $y(v)$ is a constant times $\prod_\rho \|v_\rho\|^2$. By the proposition, $T(u)$ is a sum of theta series, and each theta series is the value at $u$ of some $\theta_{i,t}(x)$. Linear algebra gives $T \in \operatorname{im}\theta_{i,t}$. $\square$

**Remark 8.5.12 (Formalization).** The level number $M$ in the translate theorem is the absolute norm of $\mathfrak{m}$, so the clause $0 < M$, $M \in \mathfrak{m}$ holds for each nonzero ideal and carries no information ([ThetaLiftFiniteVectorEqTranslateLevelDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaLiftFiniteVectorEqTranslateLevelDatum.lean#L26)). The two span theorems and the range theorem are in [ThetaSpanAndGoodRange.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaSpanAndGoodRange.lean#L60). We have not unfolded the coefficient function $d$, the lattice $\mathrm{sh}(\Lambda)$, the test function $\Phi$, the Fock polynomial vectors, the theta data of the record or the classical theta span for the level group.
