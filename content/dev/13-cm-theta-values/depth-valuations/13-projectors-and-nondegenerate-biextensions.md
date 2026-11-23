---
title: Projectors and nondegenerate biextensions
decls:
- GlobalTheory.T.hasGaugeAdjointLieProjectors_selfConjugatePlace
- GlobalTheory.ProjSelf.hasProj_self
- GlobalTheory.T.biextension_nondegenerate_mod_maximalIdeal_integral_chart
- GlobalTheory.AlphaPair.ndg_at_chart
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Projectors and nondegenerate biextensions

This section proves two facts about the charts of the section on [row data and packages at good primes](/entry/cm-theta-values/depth-valuations/#row-data-and-packages-at-good-primes). The first says that the doubled chart of a self-conjugate place carries a pair of integral projectors onto its two families of eigenvectors, and the projectors are adjoint for the biextension. The second says that the biextension of a chart that comes from an integral chart is nondegenerate modulo the maximal ideal. Both are inputs of the row hypotheses there: the projectors at self-conjugate places, and the nondegeneracy for the maximal rank condition.

### Charts and adjoint pairs

Let $C$ be an algebraically closed field of characteristic $0$ with a valuation $v$, and let $\ell$ be a prime with $v(\ell) = 1$. An element $x$ of $C$ is *integral* if $v(x) \ge 0$, and lies in the maximal ideal $\mathfrak{m}$ if $v(x) > 0$. A power series is integral if all its coefficients are. Let $\mathcal{O}$ be a commutative ring with an involution $x \mapsto x^*$.

A *chart* $Y$ over $C$ with an action of $\mathcal{O}$ consists of a formal group law $F$ of dimension $n$ over $C$, an action of $\mathcal{O}$ on $F$ by series $[x]$, a logarithm $\lambda$ with linear part the identity and an inverse $\eta$, a biextension series $h$ in two sets of $n$ variables and two biextension laws, an element $w_0 \in \mathcal{O}$ with $w_0 + w_0^* = 1$, and an integer $k$ with $v(k) = 0$. We require that $\ell$ is odd, that $C$ is complete in the sense that ℓ-adic Cauchy sequences converge, and that $F$, the action, the laws and the adjoints are integral. The *linear action* of $x$ is the matrix $L(x)$ of the linear terms of $[x]$. It is integral, and $x \mapsto L(x)$ is a ring map. We did not unfold the gauge of $Y$ or its biextension laws.

A *raw chart* $X$ on a finite set $\kappa$ of variables has a logarithm $\lambda_X$, an exponential $\eta_X$, a biextension series $h_X$ and two families of vectors $u_{g, c} \in C^\kappa$, for $g \in \{0, 1\}$ and $c$ in index sets $I_g$. For a matrix $M$ on $C^\kappa$ write $M \cdot x = \eta_X(M \lambda_X(x))$.

**Definition 4.13.1 (adjoint pair, projectors).** A pair $(M, M')$ of matrices is an *adjoint integral pair* on $X$ if $M \cdot x$ and $M' \cdot x$ are integral series and
$$\exp\big(h_X(M \cdot x, y) - h_X(x, M' \cdot y)\big)$$
is integral. The raw chart $X$ *has projectors* if there are matrices $P_0, P_1$ such that $(P_0, P_1)$ and $(P_1, P_0)$ are adjoint integral pairs, $P_g u_{g, c} = u_{g, c}$ and $P_g u_{1 - g, c} = 0$ for all $g$ and $c$, and the image of $P_g$ lies in the span of the $u_{g, c}$.

### Projectors at self-conjugate places

**Definition 4.13.2 (self-conjugate place data).** Let $d \ge 1$ and let $I_0$ be a finite set. *Self-conjugate place data* $p$ on $Y$ consist of:
1. ring maps $\sigma_a : \mathcal{O} \to C$ for $a \in \mathbb{Z}/d$ with integral values, such that $\sigma_{a+1}(x) \equiv \sigma_a(x)^\ell$ modulo $\mathfrak{m}$, and distinct $\sigma_a$ are separated by some $x$ with $v(\sigma_a(x) - \sigma_{a'}(x)) = 0$;
2. an element $\varepsilon \in \mathcal{O}$ with $\varepsilon^2 - \varepsilon \in \ell\mathcal{O}$, $\sigma_a(\varepsilon) \equiv 1$ modulo $\mathfrak{m}$ for all $a$, and $\varepsilon x \in \ell \mathcal{O}$ whenever every $\sigma_a(x)$ lies in $\mathfrak{m}$;
3. a shift $\delta \in \mathbb{Z}/d$ with $\delta \ne 0$, $2\delta = 0$ and $\sigma_a(x^*) = \sigma_{a+\delta}(x)$;
4. integral vectors $e_c \in C^n$ with types $t(c) \in \mathbb{Z}/d$, for $c \in I_0$, with $L(x) e_c = \sigma_{t(c)}(x) e_c$, saturated (there are integral $w_{c'}$ with $\langle e_c, w_{c'} \rangle = \delta_{c c'}$), and full (every common eigenvector of type $a$ is a combination of the $e_c$ with $t(c) = a$);
5. matrices $\gamma_a \in M_2(C)$ such that for every $N$ there is $G \in M_2(\mathcal{O})$ with $v(\gamma_a - \sigma_a(G)) \ge N$ entrywise, and $\gamma_{a+\delta}^{\mathsf{T}} \gamma_a = \left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right)$.

The *doubled chart* of $p$ is the raw chart on $\{0, 1\} \times \{1, \dots, n\}$ with two copies of $\lambda$ and $\eta$, the biextension series $h(x_0, y_0) + h(x_1, y_1)$, index sets $I_0$ for both $g$, and vectors
$$u_{g, c}(s, j) = \gamma_{t(c)}(s, g)\, e_c(j),$$
of type $t(c)$ for $g = 0$ and $t(c) + \delta$ for $g = 1$.

**Theorem 4.13.3 (projectors at a self-conjugate place).** The doubled chart of self-conjugate place data has projectors.

Lean: `GlobalTheory.T.hasGaugeAdjointLieProjectors_selfConjugatePlace` (also `GlobalTheory.ProjSelf.hasProj_self`, a second name).

*Proof.* Step 1 (one copy). There is a linear map $v \mapsto b(v) \in C^{I_0}$ with the following property. Let $\varphi : \mathbb{Z}/d \to C$ be an ℓ-adic limit of values of $\mathcal{O}$: for every $N$ there is $x \in \mathcal{O}$ with $v(\varphi(a) - \sigma_a(x)) \ge N$ for all $a$. Then there are matrices $M, M'$ on $C^n$ such that $(M, M')$ and $(M', M)$ are adjoint integral pairs on one copy of $Y$, $M e_c = \varphi(t(c)) e_c$, $M' e_c = \varphi(t(c) + \delta) e_c$, and $M v = M(\sum_c b(v)_c e_c)$, $M' v = M'(\sum_c b(v)_c e_c)$ for every $v$.

The powers $\varepsilon^{\ell^m}$ form an ℓ-adic Cauchy sequence, because $\varepsilon^2 \equiv \varepsilon$ modulo $\ell$. The limit of their linear actions is an integral endomorphism $E$. The range of $E$ lies in the sum of the common eigenspaces, and fullness writes $E v = \sum_c b(v)_c e_c$. Next choose $s_m \in \mathcal{O}$ that approximate $\varphi$ and satisfy $\varepsilon^{\ell^m} s_m \equiv s_m$ modulo $\ell^m$. The limits of the actions of $s_m$ and of $s_m^*$ give $M$ and $M'$, adjoint integral pairs in both orders. On $e_c$ they act by the limits of $\sigma_{t(c)}(s_m)$ and of $\sigma_{t(c)}(s_m^*) = \sigma_{t(c)+\delta}(s_m)$. Finally $M$ absorbs $E$, since $\varepsilon^{\ell^m} s_m - s_m \in \ell^m \mathcal{O}$. The same holds for $M'$, using $\varepsilon \varepsilon^* \equiv \varepsilon^*$ modulo $\ell$. That congruence follows from item 2 applied to $1 - \varepsilon^*$.

Step 2 (entries). The entries of $\gamma_a$ are integral: take $N = 0$ in item 5. For $r, s \in \{0, 1\}$ let $\varphi_{rs}(a) = \gamma_a(r, 0)\, \gamma_{a+\delta}(s, 1)$. It is an ℓ-adic limit of values: if $G$ approximates $\gamma$ to order $N$, then $x = G(r, 0)\, G(s, 1)^*$ satisfies $\sigma_a(x) = \sigma_a(G(r, 0))\, \sigma_{a+\delta}(G(s, 1))$. Step 1 gives matrices $M_{rs}$ and $M'_{rs}$.

Step 3 (blocks). Let $P_0$ be the block matrix with blocks $M_{rs}$, and $P_1$ the block matrix with blocks $M'_{sr}$. For a type $a = t(c)$,
$$(P_0 u_{g, c})(r, j) = \sum_s \gamma_a(s, g)\, \gamma_a(r, 0)\, \gamma_{a+\delta}(s, 1)\, e_c(j) = u_{0, c}(r, j) \sum_s \gamma_{a+\delta}(s, 1)\gamma_a(s, g).$$
By item 5 the sum is $1$ for $g = 0$ and $0$ for $g = 1$. The same computation, with $2\delta = 0$, gives $P_1 u_{g, c} = u_{1, c}$ for $g = 1$ and $0$ for $g = 0$.

Step 4 (adjointness). Block matrices built from adjoint integral pairs on one copy are adjoint integral pairs on the doubled chart. This uses three facts: the doubled formal group law is integral and gauged, an elementary block placed in position $(r, s)$ of an adjoint pair is an adjoint pair, and adjoint pairs are closed under sums. So $(P_0, P_1)$ and $(P_1, P_0)$ are adjoint integral pairs.

Step 5 (images). For every $v$, the absorption in Step 1 gives $P_0 v = \sum_c \beta_c u_{0, c}$ with $\beta_c = \sum_s b(v_s)_c\, \gamma_{t(c)+\delta}(s, 1)$, where $v_s = v(s, \cdot)$. The same holds for $P_1$ with $\gamma_{t(c)+\delta}(s, 0)$. $\square$

### Nondegeneracy modulo the maximal ideal

Let $Y$ be a chart over $C$. A *convergent direction* is a tuple $\gamma = (\gamma_1, \dots, \gamma_n)$ of power series in one variable over $C$ that converge in the sense of the chart. We did not unfold this condition. For a direction $\gamma$ write $\gamma'(0)$ for the vector of linear coefficients. The *linear term* of the second biextension law in the direction $u \in C^n$ is the series $\Lambda_u(x, y) = \sum_i u_i\, \partial_{z_i} \mathrm{ph}_2(z, x, y)|_{z = 0}$, taken coefficient by coefficient.

**Definition 4.13.4 (nondegenerate modulo $\mathfrak{m}$).** The biextension of $Y$ is *nondegenerate modulo $\mathfrak{m}$* if the following holds for every convergent direction $\gamma$ with some $\gamma_i'(0) \notin \mathfrak{m}$. Suppose $F(\gamma(x), \gamma(y)) \equiv \gamma(x + y)$ modulo $\mathfrak{m}$ in every monomial $x^a y^b$ with $a, b < \ell$. Then there is no integral series $b$ in $n$ variables with
$$\Lambda_{\gamma'(0)}(x, y) \equiv b(F(x, y)) - b(x) - b(y) \pmod{\mathfrak{m}}$$
in every coefficient.

We use the integral points of the section on row data and packages. Let $T$ be a complete discrete valuation ring with an embedding of the coefficient field into its fraction field, $y$ an integral framed point of the moduli space over $T$, and $C_3$ an integral chart at $y$. Let $\iota$ be an embedding of the fraction field of $T$ into $C$ that matches the valuations: $v(\iota x) = v_T(x)/v_T(\ell)$ for $x \ne 0$. Let $Y$ be a chart over $C$ with $\mathcal{O} = \mathcal{O}_E$ that is the base change of $C_3$ along $\iota$ at level $k$: its group law, action, laws and adjoints are the images under $\iota$ of those of $C_3$.

**Theorem 4.13.5 (nondegenerate biextensions at integral charts).** Assume that the involution of $\mathcal{O}_E$ is the conjugation of the host. With $T$, $y$, $C_3$, $\iota$ and $Y$ as above, the biextension of $Y$ is nondegenerate modulo $\mathfrak{m}$.

Lean: `GlobalTheory.T.biextension_nondegenerate_mod_maximalIdeal_integral_chart` (also `GlobalTheory.AlphaPair.ndg_at_chart`, a second name).

The proof reduces to the cubical structure of a semi-abelian scheme at a point of characteristic $\ell$. Let $\Omega$ be an algebraically closed field of characteristic $p$, $G$ a commutative group scheme over a base $S$ with a point $s : \operatorname{Spec} \Omega \to S$, and $c$ a cubical structure on a rigidified line bundle on $G$, with its Weil pairing. An *$\alpha_p$-family* $g$ assigns to every $\Omega$-algebra $A$ and every $a \in A$ with $a^p = 0$ an $A$-point $g(a)$ of $G$, naturally in $A$ and additively in $a$. It is *orthogonal* if for every $\Omega$-algebra $A$ with an augmentation $\pi : A \to \Omega$ of nilpotent kernel, every $e \in A$ with $e^2 = 0$, and every $A$-point $z$ with $\pi(z) = 1$ and $z^p = 1$, the Weil pairing of $g(e)$ and $z$ is trivial. The structure $c$ is *nondegenerate at $s$* if every orthogonal $\alpha_p$-family has $g(\epsilon) = 1$ for the dual number $\epsilon$ of $\Omega[\epsilon]$.

**Lemma 4.13.6 (nondegeneracy at the special fibre).** Let $V$ be a complete discrete valuation ring of characteristic $0$, $t$ a semi-abelian scheme over $V$ of the host type whose generic fibre is polarized, and $\beta : V \to \Omega$ a ring map to an algebraically closed field of characteristic $p$ that kills the maximal ideal. Then the cubical structure of $t$ is nondegenerate at $\beta$.

*Proof.* Step 1. There are a finite extension $W$ of $V$, a semi-abelian scheme $t'$ over $W$ whose special fibre splits, and a point $\beta'$ of $W$ over $\beta$. At the field point, the group of $t$ is an extension of the group of $t'$ by a torus with a free character group of finite rank, compatible with the cubical structures. Nondegeneracy passes from $t'$ to $t$: an orthogonal family of $t$ maps to an orthogonal family of $t'$. If its image is trivial at $\epsilon$, the value at $\epsilon$ lies in the torus, and an $\alpha_p$-family of multiplicative characters is trivial at $\epsilon$.

Step 2. The scheme $t'$ has a uniformization with a polarized abelian scheme $A$ over $W$. Modulo the ideal, the group of $t'$ is again an extension of $A$ by a torus, and the projection to the abelian part respects orthogonality. By the argument of Step 1, nondegeneracy for $A$ gives nondegeneracy for $t'$, with the cubical structure that comes from $A$.

Step 3. For a polarized abelian scheme over a noetherian local domain of characteristic $0$, multiplication by $n \ge 1$ is finite, and the cubical Weil pairing of $n$-torsion is perfect: an $n$-torsion point whose pairing with every $n$-torsion point after every base change is trivial is trivial.

Step 4. Over an algebraically closed field, finiteness of $[p]$ and perfection give nondegeneracy. For an orthogonal family $g$, the point $g(\epsilon)$ is $p$-torsion, and its pairing with every $p$-torsion point over a local Artinian $\Omega$-algebra is trivial. So $g(\epsilon) = 1$.

Step 5. A cubical structure on the group of $t'$ for its line bundle is unique, so Steps 2 to 4 give the nondegeneracy of the given cubical structure of $t'$. Step 1 then gives it for $t$. $\square$

*Proof of the theorem.* Suppose the biextension of $Y$ is degenerate. Step 1. The residue field $\Omega$ of the valuation ring of $C$ is algebraically closed of characteristic $\ell$, with reduction $\rho$. The embedding $\iota$ restricts to a ring map $j$ from $T$ to the valuation ring of $C$ that sends the maximal ideal of $T$ into $\mathfrak{m}$.

Step 2. The integral chart $C_3$ is a formal biextension over $T$ whose group law and second law are those of $C_3$, and whose two cocycle identities hold at zero in each variable.

Step 3. The group law and the second law of $Y$ are the images of those of $C_3$ under $j$. A degenerate direction of $Y$ therefore reduces under $\rho$ to a degenerate series direction over $\Omega$ for the reduction of $C_3$.

Step 4. The formal chart of $C_3$ has a point over $\Omega$ with nilpotent coordinates that lies over $\rho \circ j$. The universal chart points and the partial frame laws hold at this point, and the cocycle identities of Step 2 pass to $\Omega$. Under these conditions a degenerate series direction is incompatible with the nondegeneracy, at $\rho \circ j$ and for $p = \ell$, of the cubical structure of the semi-abelian scheme of $C_3$.

Step 5. That scheme is the integral framed model of $y$, which is polarized on the generic fibre, and $T$ is a complete discrete valuation ring of characteristic $0$. The lemma gives this nondegeneracy, since $\rho \circ j$ kills the maximal ideal of $T$. This is a contradiction. $\square$

**Remark 4.13.7 (Formalization).** Both `T.` statements are relays: `first | exact @…` under `maxHeartbeats 1000000` ([HasGaugeAdjointLieProjectorsSelfConjugatePlaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/HasGaugeAdjointLieProjectorsSelfConjugatePlaceStatement.lean#L12), [BiextensionNondegenerateModMaximalIdealIntegralCStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/BiextensionNondegenerateModMaximalIdealIntegralCStatement.lean#L6)). Step 1 of the projectors is `exists_pair` ([HasGaugeAdjointLieProjectorsSelfConjugatePlace.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/HasGaugeAdjointLieProjectorsSelfConjugatePlace.lean#L310)). It works on a one-copy raw chart `rawOne` with empty index sets, $d = 0$ and $k = n = j = j' = 0$, and it keeps only one of the five properties that the limit lemma gives for $E$. The word "Lie" in the name refers to nothing in the statement, which is `HasProj`. In `ndg_at_chart` the hypothesis on the involution is used only to rewrite the star structure, by `obtain rfl` ([BiextensionNondegenerateModMaximalIdealIntegralC.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/BiextensionNondegenerateModMaximalIdealIntegralC.lean#L173)), and the proof is by contradiction. The perfection step `perf_of_polAV` takes the uniformization laws from `firstFiveLaws.1` ([BiextensionNondegenerateModMaximalIdealIntegralC.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/BiextensionNondegenerateModMaximalIdealIntegralC.lean#L122)). We did not open the limit lemmas, the block lemmas, the degenerate direction lemmas, the torus extension lemmas or the uniformization.
