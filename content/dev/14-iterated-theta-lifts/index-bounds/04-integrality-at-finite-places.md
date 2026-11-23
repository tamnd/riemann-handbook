---
title: Integrality at finite places
decls:
  - GlobalTheory.ArcQ.finLocalAt_of_intModel
  - GlobalTheory.ArcCM.finLocalAt_of_cmIn
  - GlobalTheory.T.localArcIntegrality_of_cmNormalisedTrivialisation
  - GlobalTheory.ArcCM.cfOf_fin_bound
  - GlobalTheory.T.cmArcDatum_functional_finite_integrality_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integrality at finite places

The functional $\mathrm{cf}_d$ of Section 3 takes values in a number field $K_1$, and this section controls its values at the finite places. Its result is that, for a member $d$ of the CM family and a section $F$ that is integral at a prime $\lambda$ of $K$, the value $\mathrm{cf}_d(F)$ is integral at each prime $w$ over $\lambda$ up to a fixed metrized line and a small error (Theorem (Finite integrality of the coefficient functional)). The error is zero unless $w$ divides $d_E$ or the level $n'$ of the CM point. First, an integral model of the arc gives a *finite cut*, a bound for the evaluation of $F$ along the arc over $w$. Second, the CM input gives such a model with explicit valuations, and a coefficient bound turns the cut into a bound for one coefficient.

**Metrized lines.** We use [Hermitian line bundles](/learn/arakelov/#hermitian-line-bundles) over $\mathcal{O}_{K_1}$ in a simple form.

**Definition 4.4.1 (Metrized line).** A *metrized line* $L$ over $K_1$ is a pair $(I_L, (n_{L,\sigma})_\sigma)$ of a fractional ideal $I_L$ of $\mathcal{O}_{K_1}$ and a real number $n_{L,\sigma}$ for each embedding $\sigma : K_1 \to \mathbb{C}$. It is *good* if $I_L \neq 0$ and $n_{L,\sigma} > 0$ for all $\sigma$. The *length* of $x \in K_1$ at $\sigma$ is $|\sigma(x)|\, n_{L,\sigma}$. The *degree* and the *normalized degree* of $L$ are

$$\deg L = -\log N(I_L) - \sum_{\sigma} \log n_{L,\sigma}, \qquad \widehat{\deg}\, L = \frac{\deg L}{[K_1 : \mathbb{Q}]}.$$

The *trivial line* is $\mathbf{1} = (\mathcal{O}_{K_1}, 1)$. The tensor product multiplies the ideals and the metrics, the dual inverts both, and the power $L^k$ raises both to the power $k$.

So $n_{L,\sigma}$ is a [[Hermitian metric|Q6X6W2N29G]] on the line at $\sigma$, given by its value at $1$. For a prime $w$ of $K_1$ we write $v_w(I)$ for the exponent of $w$ in a fractional ideal $I$, and $\mathrm{ord}_w(x) = v_w(x \mathcal{O}_{K_1})$ for $x \in K_1^\times$.

**Definition 4.4.2 (Value line).** Let $s$ be a CM input for an arc datum $d$ over $K_1$ with lines $T$ and $\ell(\tau, k)$ as in Section 3. For a monomial $X^\mu$ in the letters $X_{\tau,i,l}$ and $n \in \mathbb{N}$, the *value line* is

$$V_s(\mu, n) = (T^\vee)^{\otimes n} \otimes \Big( \bigotimes_{(\tau, i, l)} \ell(\tau, l)^{\otimes \mu(\tau,i,l)} \Big)^\vee.$$

By the definition of the tensor product and the dual, its ideal has the exponent

$$v_w\big(I_{V_s(\mu,n)}\big) = -n\, v_w(I_T) - \sum_{(\tau,i,l)} \mu(\tau,i,l)\, v_w\big(I_{\ell(\tau,l)}\big)$$

at each prime $w$, since $I_T$ and all $I_{\ell(\tau,l)}$ are nonzero for a CM input.

**Definition 4.4.3 (Local error).** Let $K_1$ and $K$ be number fields, let $n' \in \mathbb{N}$ and let $\lambda$ be a prime of $K$. Put

$$m_\lambda(E, n') = \max\big(v_\lambda(|d_E|),\ v_\lambda(n')\big), \qquad \beta_{E,n',A}(\lambda) = A \cdot m_\lambda(E, n')$$

for $A \in \mathbb{N}$, where $v_\lambda(N)$ is the exponent of $\lambda$ in the ideal $N \mathcal{O}_K$.

So $\beta_{E,n',A}(\lambda) = 0$ unless $\lambda$ divides $d_E n'$.

**Integral sections and finite cuts.** Let $\lambda$ be a prime of the field of coefficients $K$. A section $F$ of weight $(a, n)$ is *$\lambda$-integral* if $v(F) \geq 0$ for every valuation $v$ that comes from an algebraic integral framed point over $\lambda$. We write $\mathcal{S}_\lambda(a, n)$ for the set of these sections.

**Definition 4.4.4 (Finite site).** Let $w$ be a prime of $K_1$. A *finite site* at $w$ is a complete field $\mathbb{K}$ with an ultrametric absolute value, an embedding $\iota : K_1 \to \mathbb{K}$ and a real $0 < r < 1$ with $\|\iota(x)\| = r^{\mathrm{ord}_w(x)}$ for $x \neq 0$, a subfield $\mathbb{K}_0$ with infinite residue field on the unit ball, and a set $\Sigma \subset \mathbb{K}$. Each $t \in \Sigma$ has $0 < \|t\| < 1$, the norms of $\Sigma$ are dense in $(0, 1)$, and $t u \in \Sigma$ for $t \in \Sigma$ and $u \in \mathbb{K}_0$ with $\|u\| = 1$.

The completion of $K_1$ at $w$ is the model for $\mathbb{K}$; see [places and completions](/learn/number-fields/#places-and-completions). For a polynomial $N$ in the letters over $K_1((t))$ and $k \in \mathbb{Z}$, let $N^{(k)}$ be the polynomial in the letters over $K_1$ whose coefficients are the coefficients of $t^k$ of the coefficients of $N$.

**Definition 4.4.5 (Finite cut).** Let $d$ be an arc datum over $K_1$, $w$ a prime of $K_1$, $n, m \in \mathbb{N}$, $v_\theta \in \mathbb{Z}$, $v_\eta(\tau, k) \in \mathbb{Z}$ for each $\tau$ and $k$, and $\mathcal{F}$ a set of sections. The datum $d$ has a *finite cut* at $w$ with parameters $(n, v_\theta, v_\eta, m)$ on $\mathcal{F}$ if there are a finite site $(\mathbb{K}, \iota, r, \mathbb{K}_0, \Sigma)$ at $w$, an element $\gamma \in \mathbb{K}$, elements $\eta_{\tau,k} \in \mathbb{K}$ and square matrices $A_\tau, B_\tau$ over $\mathbb{K}$ of size the multiplicity of $\tau$ with:

1. $\gamma \neq 0$ and $\|\gamma\| = r^{v_\theta}$;
2. $\eta_{\tau,k} \neq 0$ and $\|\eta_{\tau,k}\| = r^{v_\eta(\tau,k)}$ for all $\tau, k$;
3. $A_\tau B_\tau = 1$ and $\|(A_\tau)_{kl}\| \leq r^{-m}$ for all $\tau, k, l$;
4. for each $F \in \mathcal{F}$, each $t \in \Sigma$ and each family $Y = (Y_{\tau,i,l})$ of elements of $\mathbb{K}_0$ with $\|Y_{\tau,i,l}\| \leq 1$ and $\|\prod_\tau \det Y_\tau\| = 1$, the terms $\| \iota N_F^{(k)}(Y') \, t^k \|$ tend to $0$ as $|k| \to \infty$, and
$$\Big\| \gamma^{-n} \sum_{k \in \mathbb{Z}} \iota N_F^{(k)}(Y')\, t^k \Big\| \leq 1.$$

Here $N_F$ is the polynomial of Section 3 for the evaluation of $F$ at $y_F$, the map $\iota$ acts on the coefficients, and $Y'_{\tau,i,k} = \big( \sum_l Y_{\tau,i,l} (B_\tau)_{lk} \big)\, \eta_{\tau,k}^{-1}$.

**Integral models.** Let $T$ be a complete discrete valuation ring with finite residue field and field of fractions $\mathrm{Fr}(T)$, with valuation $v_T$; see [discrete valuation rings](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices). Let $i_T : K_1 \to \mathrm{Fr}(T)$ be an embedding with $v_T(i_T(x)) = \mathrm{ord}_w(x)$. Let $W \subset \mathbb{C}$ be a valuation subring. An *integral model* of $d$ over $T$ consists of maps from $W \cap K$ and from $\mathcal{O}_E$ to $T$ that are compatible with $i_T$, an arc over $T$ and an arc over $\mathrm{Fr}(T)$ that are base changes of each other and of the arc of $d$, a nonzero theta section $\theta_T$ over the integral arc, tangent vectors $e^T_{\tau,k}$ of the integral arc, an element $\gamma_T \in \mathrm{Fr}(T)$ and matrices $g_\tau$ over $\mathrm{Fr}(T)$. The base changes of $\theta_T$ and of the theta section of $d$ differ by the factor $\gamma_T$. The base changes of the $e^T_{\tau,l}$ are tangent, and the base change of $e_{\tau,k}$ is the combination of them with the coefficients $(g_\tau)_{kl}$.

**Theorem 4.4.6 (Finite cut from an integral model).** Assume the laws of degenerations, of uniform base change and of evaluation from the list $\mathcal{K}$. Let $d$ be an arc datum over $K_1$ that lies over the base, let $w$ be a prime of $K_1$ and $\lambda$ a prime of $K$. Let $T$, $i_T$ and $W$ be as above, and assume that $v_T(i_T(x)) = e_L\, v_\lambda(x)$ for $x \in K$, for some integer $e_L > 0$. Let $Y$ be a model of the moduli space over $W \cap K$ with the property $N_4$ and an invertible pushforward, and let $M$ be an integral model of $d$ over $T$ with $\gamma_T$ and $g_\tau$. Assume that the integral tangent vectors of $M$ form a basis of the Lie algebra along every arc of $Y$ over $T[[t]]$ with a witness. Let $v_\theta \in \mathbb{Z}$, $m \in \mathbb{N}$, $\eta_{\tau,k} \in \mathrm{Fr}(T)$ and matrices $A_\tau$ over $\mathrm{Fr}(T)$ with:

1. $\gamma_T \neq 0$ and $v_T(\gamma_T) = v_\theta$;
2. $\eta_{\tau,k} \neq 0$ and $v_T(\eta_{\tau,k}) = v_\eta(\tau,k)$;
3. $\det A_\tau \neq 0$ and $(g_\tau)_{kl} = \eta_{\tau,k} (A_\tau)_{kl}$;
4. each entry of $A_\tau$ is $0$ or has valuation at least $-m$.

Then for every weight $(a, n)$, $d$ has a finite cut at $w$ with parameters $(n, v_\theta, v_\eta, m)$ on $\mathcal{S}_\lambda(a, n)$.

Lean: `GlobalTheory.ArcQ.finLocalAt_of_intModel`.

*Proof.* The ring $T$ has finite residue field and $i_T$ matches $\mathrm{ord}_w$, so a lemma on sites gives a finite site at $w$ with a map $i : \mathrm{Fr}(T) \to \mathbb{K}$ over $K_1$ such that $\|i(x)\| = r^{v_T(x)}$ for $x \neq 0$. In particular $\|i(x)\| \leq 1$ for $x \in T$, and $\|i(\varpi)\| < 1$ for a uniformizer $\varpi$ of $T$. The ring $T$ is complete for the ideal $(\varpi)$, so the property $N_4$ of $Y$ gives an arc $\chi$ of $Y$ over $T[[t]]$ with a witness. From $\chi$, the theta section $\theta_T$ and the basis condition, a lemma on framed points over discrete valuation rings gives an integral framed point $y_R$ over the ring $T[[t]][X][(\varpi t \det X)^{-1}]$, and a comparison with the framed point of $d$.

The tangent vectors of $d$ are tangent, since they are combinations of the tangent vectors $e^T$ after base change. So the normal form lemma applies to $d$: there are $\zeta \in K_1$ and $N > 0$ with $\zeta^N = 1$ such that $d$ is normalized at $\zeta$. The rigidity of base change for an integral model then shows that the framed point of $d$ and $y_R$ agree over $\mathrm{Fr}(T)$ after the change of frame by $B_\tau = A_\tau^{-1}$, the scaling by $\eta^{-1}$ and the factor $\zeta \gamma_T$. A second lemma shows that every $\lambda$-integral section has norm at most $1$ at $y_R$, at each point of the site; it uses $e_L$ to compare $v_T$ with $v_\lambda$.

A lemma on frames turns these two facts into a finite cut for $\gamma = \zeta \gamma_T$, $\eta$, $A$ and $B$. The norms are as required: $\|i(\zeta)\|^N = 1$, so $\|i(\zeta)\| = 1$ and $\|i(\zeta\gamma_T)\| = r^{v_\theta}$; $\|i(\eta_{\tau,k})\| = r^{v_\eta(\tau,k)}$; and an entry of $A_\tau$ is $0$ or has norm $r^{v_T} \leq r^{-m}$. $\square$

**Theorem 4.4.7 (Finite cut at a CM arc).** Assume $\mathcal{K}$ and the existence of models at all primes. Let $d$ be a standard arc datum over $K_1$ with a CM input $s$ with parameters $(n', \Lambda_0, c_1)$, lines $T$ and $\ell(\tau,k)$. Let $\lambda$ be a prime of $K$ and $w$ a prime of $K_1$ over $\lambda$, with ramification index $e(w|\lambda)$. Then for every weight $(a', n)$, $d$ has a finite cut at $w$ with parameters

$$\big(n,\ -v_w(I_T),\ (\tau,k) \mapsto -v_w(I_{\ell(\tau,k)}),\ e(w|\lambda)\, m_\lambda(E, n')\big)$$

on $\mathcal{S}_\lambda(a', n)$.

Lean: `GlobalTheory.ArcCM.finLocalAt_of_cmIn` (also `GlobalTheory.T.localArcIntegrality_of_cmNormalisedTrivialisation`, a second name).

*Proof.* Put $e = e(w|\lambda) > 0$ and $m = e\, m_\lambda(E, n')$. The lemma on sites gives a complete discrete valuation ring $T$ with finite residue field and $i_T : K_1 \to \mathrm{Fr}(T)$ with $v_T \circ i_T = \mathrm{ord}_w$. Since $w$ lies over $\lambda$, we have $v_T(i_T(x)) = e\, v_\lambda(x)$ for $x \in K$.

We choose a model. Let $p$ be a prime number in $\lambda$. There is a valuation subring $W \subset \mathbb{C}$ in which $p$ is not a unit and whose trace on $K$ is the valuation ring of $\lambda$. The existence of models gives a model $Y$ over $W \cap K$ with $N_4$ and an invertible pushforward. The elements of $W \cap K$ and of $\mathcal{O}_{K_1}$ have valuation at least $0$, so they lift to $T$. From the CM input, a lemma gives an integral arc over $T$ that matches the arc of $d$, and a second lemma gives an integral model $M$ of $d$ over $T$ for $Y$ with the basis condition. The valuation of its factor $\gamma_T$ is $-v_w(I_T)$.

Now we choose $\eta$ and $A$. For each $(\tau, k)$ we find $c_{\tau,k} \in K_1^\times$ with $\mathrm{ord}_w(c_{\tau,k}) = v_w(I_{\ell(\tau,k)})$ such that each entry of $c_{\tau,k}\, g_\tau$ in row $k$ is $0$ or has valuation at least $-m$:

- If the tangent vector $e_{\tau,k}$ has the first kind, then $\ell(\tau,k) = \mathbf{1}$ and we take $c_{\tau,k} = 1$. The coordinates of the logarithmic tangent of $\xi$ become integral after multiplication by $|d_E|$. So each entry has valuation at least $-v_T(|d_E|) = -e\, v_\lambda(|d_E|) \geq -m$.
- If $e_{\tau,k}$ has the second kind with letter $m'$, then $\ell(\tau,k) = \ell_{m'}$. We take a local generator $c_{\tau,k}$ of $I_{\ell_{m'}}$ at $w$. The letter of the CM abelian scheme is integral up to this generator, and $e_{\tau,k}$ is its pullback along multiplication by $1/n'$. So the entries become integral after multiplication by $n'$, and each entry has valuation at least $-v_T(n') = -e\, v_\lambda(n') \geq -m$.

Put $\eta_{\tau,k} = i_T(c_{\tau,k})^{-1}$ and $A_\tau = \mathrm{diag}(i_T(c_{\tau,k}))_k\, g_\tau$. Then $v_T(\eta_{\tau,k}) = -v_w(I_{\ell(\tau,k)})$, $(g_\tau)_{kl} = \eta_{\tau,k}(A_\tau)_{kl}$, and $\det A_\tau \neq 0$ since $\det g_\tau \neq 0$. The datum $d$ lies over the base since it is standard. Theorem (Finite cut from an integral model) now gives the finite cut. $\square$

**Theorem 4.4.8 (Finite integrality of the coefficient functional).** Assume $\mathcal{K}$ and the existence of models at all primes. Let $d$ be a standard arc datum over $K_1$ with monomial $X^{\mu}$, and let $s$ be a CM input for $d$ with parameters $(n', \Lambda_0, c_1)$, where $\Lambda_0 \geq 1$. Let $\lambda$ be a prime of $K$, $w$ a prime of $K_1$ over $\lambda$, $(a', n)$ a weight, and $F \in \mathcal{S}_\lambda(a', n)$ with $\mathrm{cf}_d(F) \neq 0$. Then

$$-e(w|\lambda)\, \beta_{E, n', \mathrm{abs}(a')}(\lambda) \leq \mathrm{ord}_w\, \mathrm{cf}_d(F) - v_w\big(I_{V_s(\mu, n)}\big).$$

Lean: `GlobalTheory.ArcCM.cfOf_fin_bound` (also `GlobalTheory.T.cmArcDatum_functional_finite_integrality_bound`, a second name).

*Proof.* Put $D = \mathrm{abs}(a')$ and $m = e(w|\lambda)\, m_\lambda(E, n')$. Theorem (Finite cut at a CM arc) gives a finite cut at $w$ with $\gamma$, $\eta$, $A$, $B$ and the parameters of that theorem. Since $F$ is a section of weight $(a', n)$, a lemma on arcs gives a polynomial $P$ in the letters over $K_1((t))$ that maps to the evaluation of $F$ at $y_F$ and is homogeneous of degree $D$. The map from polynomials to functions on the arc is injective, so $N_F = P$ and $\mathrm{cf}_d(F) = [X^\mu t^{j_d}] P$.

A coefficient bound for homogeneous polynomials over a complete ultrametric field, proved outside this chapter, applies to $P$ and the cut, with the constant $C = r^{-m} \geq 1$. It gives

$$\big\| \iota\, \mathrm{cf}_d(F) \big\| \leq \|\gamma\|^n \prod_{(\tau,i,l)} \|\eta_{\tau,l}\|^{\mu(\tau,i,l)} \cdot C^{D}.$$

All terms are powers of $r$ and $0 < r < 1$. We take logarithms to the base $r$ and use $\|\iota x\| = r^{\mathrm{ord}_w x}$:

$$\mathrm{ord}_w\, \mathrm{cf}_d(F) \geq -n\, v_w(I_T) - \sum_{(\tau,i,l)} \mu(\tau,i,l)\, v_w(I_{\ell(\tau,l)}) - m D.$$

By the exponent formula for the value line, the first two terms are $v_w(I_{V_s(\mu,n)})$. Since $m D = e(w|\lambda)\, D\, m_\lambda(E,n') = e(w|\lambda)\, \beta_{E,n',D}(\lambda)$, this is the claim. $\square$

Section 6 sums the error $\beta$ over all primes.

**Remark 4.4.9 (Formalization).** The finite cut is `FinLocalAt` of [FinLocalCutAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/FinLocalCutAt.lean#L43), and the metrized lines are `MLine` of [DetIdeal.lean](lean:Formalism/LocalToGlobal/CMDeterminantIdeals/DetIdeal.lean#L10). The last theorem asks for $\Lambda_0 \geq 1$, but the proof does not use this hypothesis ([CmArcDatumFunctionalFiniteIntegralityBound.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFunctionalFiniteIntegralityBound.lean#L65)). The second theorem asks that $d$ be standard, but it uses only that $d$ lies over the base ([LocalArcIntegralityOfCmNormalisedTrivialisation.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/LocalArcIntegralityOfCmNormalisedTrivialisation.lean#L232)). In the first theorem the index $e_L$ occurs only in its hypothesis on $v_T$ over $K$, not in the conclusion ([FinLocalAtOfIntModel.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/FinLocalAtOfIntModel.lean#L142)). The second names are wrappers. We have not unfolded the property $N_4$, the rigidity of base change or the valuations of integral framed points.
