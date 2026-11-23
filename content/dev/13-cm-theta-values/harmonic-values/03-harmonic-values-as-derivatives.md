---
title: Harmonic values as derivatives of theta functions
decls:
  - GlobalTheory.AnVal.harm_nab_eq_polyDeriv
  - GlobalTheory.T.harmonicValue_canonicalConnection_eq_polyDeriv
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Harmonic values as derivatives of theta functions

A harmonic value is a harmonic polynomial evaluated on the jets of sections of a line bundle. The jets are taken with a canonical connection, which is defined over any base through formal charts. This section shows that at a complex point a harmonic value is an ordinary derivative: the harmonic polynomial, read as a constant coefficient differential operator, applied to a product of theta functions at $0$. The proof compares an arbitrary chart with the analytic chart of the [previous section](/entry/exists-analytic-chart/). The result is used in the step [every character of literature](/step/every-character-of-literature/) to bound harmonic values by analytic means. The analytic background is in [theta functions on complex tori](/learn/theta-functions-cm/#theta-functions-on-complex-tori).

### Canonical connections

We keep the notation of the two previous sections. Let $X_o$ be a moduli scheme with universal abelian scheme $A$ and line bundle $L$, and let $F$ be a coefficient field. For a chart $C$ at a point $y$ over a $\mathbb{Q}$-algebra $S$, with tangent coordinates $u_\ell$, gauge $h$ and group law $\mathcal{F}$, and for a power series $f$ in $d$ variables, put
$$\nabla^C_k(f)(P) = \Bigl(P(D_u)\bigl(f \cdot \exp(k\, h_L)\bigr)\Bigr)(0),$$
where $P$ is a polynomial in the rows $\ell$, $D_{u_\ell}$ is the invariant derivation of $\mathcal{F}$ along $u_\ell$, and $h_L$ is the gauge restricted along the graph of the action of $w_0$. We do not unfold the gauge term. It vanishes when $h = 0$.

**Definition 2.3.1 (canonical connection).** A *connection* assigns a value $\nabla_y(s)(\alpha) \in S$ to every point $y$ over $S$, every $k$, every section $s$ of $L^k$ at $y$ and every multi-index $\alpha$ in the rows. It is *canonical* if the involution of $\mathcal{O}_E$ is the conjugation of $E$ and, for every $S$ and $y$, there is a chart $C$ at $y$ such that every section has a germ in $C$ and
$$\nabla_y(s)(\alpha) = \nabla^C_k(f)(z^\alpha)$$
whenever $f$ is a germ of $s$ in $C$.

**Definition 2.3.2 (harmonic value).** Let $s_1, \dots, s_n$ be sections of $L^k$ at $y$ and let $P$ be a polynomial in the letters $(\tau, i, b)$ with coefficients in $F$. For a monomial $m$ of $P$ and a column $b$, let $m_b$ be the multi-index in the rows given by the exponents of the letters of column $b$. The *harmonic value* is
$$\nabla_y(s)(P) = \sum_m P_m \prod_{b=1}^{n} \nabla_y(s_b)(m_b).$$
The *chart value* $\nabla^C(f)(P)$ of germs $f_1, \dots, f_n$ in a chart $C$ is the same sum with $\nabla^C_k(f_b)(z^{m_b})$ in place of $\nabla_y(s_b)(m_b)$.

### Chart independence

The main input is that chart values of integral harmonic polynomials do not depend on the chart.

**Theorem 2.3.3 (chart independence).** Assume that the involution of $\mathcal{O}_E$ is the conjugation of $E$. Let $y$ be a point over a $\mathbb{Q}$-algebra $S$, let $C$ and $C'$ be two charts at $y$, and let $s_1, \dots, s_n$ be sections of $L^k$ with germs $f_b$ in $C$ and $f'_b$ in $C'$. Then for every row degree $a$ and every $P \in \mathcal{H}_a^{\mathcal{O}}$,
$$\nabla^C(f)(P) = \nabla^{C'}(f')(P).$$

This is proved in a later chapter from the global sections of the moduli scheme. We use it here as a hypothesis. The statement asks for integral coefficients. The next lemma removes this condition.

**Lemma 2.3.4 (clearing denominators).** For every $P \in \mathcal{H}_a$ there is an integer $N > 0$ with $N P \in \mathcal{H}_a^{\mathcal{O}}$ and with the same support as $P$.

*Proof.* The field $F$ is a number field, so each coefficient of $P$ becomes integral after multiplication by a positive integer. Take $N$ to be a common multiple. The three conditions on $\mathcal{H}_a$ are linear, so $N P$ keeps them, and multiplication by $N \neq 0$ keeps the support. $\square$

### The theorem

For a function $\Theta$ on $(\mathbb{C}^g)^n$ and a polynomial $P$ in the letters, let $\partial_P \Theta(0) = \sum_m P_m\, \partial^m \Theta(0)$, where the letter $(\tau, i, b)$ acts as the partial derivative along the coordinate $\epsilon^{-1}(\tau, i)$ of the factor $b$.

**Theorem 2.3.5 (harmonic values are derivatives).** Assume chart independence. Let $\Phi$ be an analytic point of dimension $g$ over a framed complex point $y$, and let $\nabla$ be a canonical connection. Let $s_1, \dots, s_n$ be sections of $L^k$ at $y$, and let $s_b$ read as $\theta_b$ in the frame of $\Phi$. Then for every row degree $a$ and every $P \in \mathcal{H}_a$ with coefficients in $F$,
$$\sum_m P_m \prod_{b=1}^{n} \nabla_y(s_b)(m_b) = \partial_P\Bigl((z_1, \dots, z_n) \mapsto \prod_{b=1}^{n} \theta_b(z_b)\Bigr)(0).$$

Lean: `GlobalTheory.AnVal.harm_nab_eq_polyDeriv` (also `GlobalTheory.T.harmonicValue_canonicalConnection_eq_polyDeriv`, a second name).

*Proof.* The proof has five steps.

*Step 1.* By the Lemma, choose $N > 0$ with $N P$ integral and with the same support as $P$.

*Step 2.* Since $\nabla$ is canonical, there is a chart $C_1$ at $y$ in which each $s_b$ has a germ $f_b$. Then $\nabla_y(s_b)(\alpha) = \nabla^{C_1}_k(f_b)(z^\alpha)$ for all $\alpha$. So the left side is the chart value $\nabla^{C_1}(f)(P)$.

*Step 3.* By the [analytic chart theorem](/entry/exists-analytic-biextension-chart-complex-point/) there is a chart $C$ of dimension $g$ with gauge $0$, additive group law and tangent coordinates the standard basis vectors at $\epsilon^{-1}(\ell)$. In it the germ of $s_b$ is the Taylor series of $\theta_b$ at $0$. Each $\theta_b$ is holomorphic, since a section that reads as a function reads as a theta function.

*Step 4.* Chart independence for $N P$, $C_1$ and $C$ gives $\nabla^{C_1}(f)(N P) = \nabla^{C}(\mathrm{tay}\,\theta)(N P)$. Since $N P$ has the support of $P$, both sides are $N$ times the values for $P$. Cancel $N$, which is not zero in $\mathbb{C}$.

*Step 5.* In the chart $C$ the gauge term vanishes and the invariant derivations are the partial derivatives. So for every polynomial $Q$ in the rows,
$$\nabla^C_k(\mathrm{tay}\,\theta_b)(Q) = \bigl(Q(\partial)\,\theta_b\bigr)(0).$$
By the Leibniz rule for functions of separate variables, $\partial_P$ of the product $\prod_b \theta_b(z_b)$ at $0$ is $\sum_m P_m \prod_b \partial^{m_b}\theta_b(0)$. The two sides now agree term by term. $\square$

**Remark 2.3.6.** Over $\mathbb{C}$ a section of $L^k$ is a theta function, and its jets in the additive chart are the Taylor coefficients. The content of the Theorem is that the canonical connection, which is defined algebraically, gives these Taylor coefficients at complex points. Harmonicity of $P$ is used only to apply chart independence. For a nonharmonic $P$ the left side would depend on the chart.

**Remark 2.3.7 (Formalization).** The Theorem is in [HarmonicValueCanonicalConnectionEqPolyDeriv.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HarmonicValueCanonicalConnectionEqPolyDeriv.lean#L25), with a helper at L17 that moves $N$ out of the sum. The second name is in [HarmonicValueCanonicalConnectionEqPolyDerivStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HarmonicValueCanonicalConnectionEqPolyDerivStatement.lean#L10) and is proved by a `first` combinator. Chart independence is a hypothesis of the Theorem, stated in [ThExprUniqOfChartIndep2.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/ThExprUniqOfChartIndep2.lean#L12). It is proved without hypotheses in [EmbeddingsDifferOnInteger.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/EmbeddingsDifferOnInteger.lean#L98), so the hypothesis is not a real assumption. The chart value is in [CIndSt.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/CIndSt.lean#L12), the clearing lemma in [ExistsNatCastSmulCoeffIsIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsNatCastSmulCoeffIsIntegral.lean#L31) and Step 5 in [TaylorPSEqTay.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PullbackSections/HolomorphicFamilies/TaylorPSEqTay.lean#L29).
