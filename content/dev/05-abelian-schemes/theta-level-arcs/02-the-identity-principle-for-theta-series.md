---
title: The identity principle for theta series
decls:
  - GlobalTheory.T.exists_thetaPoint_complexDegeneration_small
  - GlobalTheory.T.theta_series_identity_principle_complex_points
  - GlobalTheory.ArcIdentity.aeval_arcTx_eq_zero_of_vanishC
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The identity principle for theta series

Let $G$ be a homogeneous polynomial with coefficients in $\mathbb{Z}[\zeta, \rho]$ that vanishes on the theta null points of level $m$ of all complex abelian varieties of our PEL type. In this section we prove that $G$ also vanishes on the formal theta series of every arc, over every algebraically closed field of characteristic $0$. Over $\mathbb{C}$, Mumford's construction with a small parameter $u$ gives an abelian variety whose theta null point is the series at $u$, so the polynomial vanishes at all small $u$, and an identity principle for power series gives the result. A descent to a countable field and an embedding into $\mathbb{C}$ give the general case. The result is used in [the next section](/entry/exists-full-theta/) to show that the series of [the first section](/entry/exists-arc-series-integral-algebraic-over-power-series/) satisfy all the equations of theta null points. For the identity theorem see [analytic continuation and the identity theorem](/learn/complex-analysis/#analytic-continuation-and-the-identity-theorem) in Volume 1.

### Objects with full level structure

We keep the notation of the first section: $E$, the host $(d, \rho_{\mathbb{C}}, w_0)$ and the PEL datum $D$ with lattice $\Lambda$.

**Definition 6.2.1 (Object with full level).** Let $K$ be an algebraically closed field. An *object with full level* over $K$ is a polarized abelian variety $(A, L)$ over $K$ with an action of $\mathcal{O}_E$, an isomorphism of $L$ with the cubical bundle of the pair $(1, w_0)$, an element $\rho \in K$ with $\rho^2 = -d$, the determinant condition of $D$ on the Lie algebra, and a Tate isomorphism $I$. The Tate isomorphism gives roots of unity $\zeta_n \in K$ and maps $\operatorname{ev}_n$ from $\Lambda$ to the $n$-torsion of $A$ that match the hermitian form with the Weil pairing.

For $m \geq 1$ and $v : \Lambda \to K$, we say that $v$ is a *theta point of level $m$* of the object $o$ if $v$ is the theta null point of $(A, L)$ of level $m$ at the torsion points $\operatorname{ev}_{m^2}$. The *coordinates* at a torsion point $z$ are defined in the same way. See [the algebraic theory of theta functions](/learn/theta-functions-cm/#the-algebraic-theory-of-theta-functions).

**Definition 6.2.2 (Complete arc datum).** Let $R$ be a domain and $F$ an algebraically closed field over $\operatorname{Frac} R$. A *complete arc datum* $\mathcal{A}$ over $(R, F)$ consists of degeneration data $D_0$ over $R$ with an action of $\mathcal{O}_E$ on the character lattice, with $\psi$ even and $\tau$ bimultiplicative, an isomorphism of the trace form twisted by $w_0$, an element $\rho \in F$ with $\rho^2 = -d$ and the Lie signature of $D$ at $\rho$, a Tate isomorphism with values in $F$, a numerical degeneration datum $N$ over $F$ with a comparison to $D_0$, and labels $q_n : \Lambda \to Q_n(N)$ that match the Tate isomorphism.

A form $\beta$ on $\mathsf{X}(N)$ is *balanced* if $\beta(a y, z) = \beta(y, \bar a z)$ for all $a \in \mathcal{O}_E$.

### Polynomials that vanish on complex theta points

Write $\zeta_n^{\mathbb{C}} = e^{2\pi i/n}$. For a ring $K$ and $\zeta, \rho \in K$, let $c_{\zeta, \rho} : \mathbb{Z}[x, y] \to K$ be the map that sends $x$ to $\zeta$ and $y$ to $\rho$.

**Definition 6.2.3 (Compatible constants).** Let $n \geq 1$. A pair $(\zeta, \rho)$ in $K$ is *compatible at level $n$* if every $c \in \mathbb{Z}[x, y]$ with $c(\zeta_n^{\mathbb{C}}, \rho_{\mathbb{C}}) = 0$ also has $c(\zeta, \rho) = 0$.

**Definition 6.2.4 (Complex theta relation).** Let $m \geq 1$. A polynomial $G$ in variables indexed by $\Lambda$ with coefficients in $\mathbb{Z}[x, y]$ is a *complex theta relation of level $m$* if $m$ is odd, $G$ is homogeneous, and $G$ vanishes under $c_{\zeta^{\mathbb{C}}_{m^2}, \rho_{\mathbb{C}}}$ at every theta point of level $m$ of every object with full level over $\mathbb{C}$ with $\rho = \rho_{\mathbb{C}}$ and $\zeta_{m^2} = \zeta^{\mathbb{C}}_{m^2}$.

**Definition 6.2.5 (Formal theta series).** Let $N$ be a numerical degeneration datum over $F$, let $\beta$ be a symmetric form on $\mathsf{X}$, let $m$ be odd and let $p = (y, g) \in Q_{m^2}(N)$. The *formal theta series* of $p$ is the power series
$$\Theta_{\beta, m}(p) = \sum_{n \geq 0} \Bigl( \sum_{\chi :\, \beta(y + m\chi,\, y + m\chi) = 2m^2 n} t_m(p, \chi) \Bigr) X^n \in F[[X]].$$

When $u$ is small and the theta terms of the twist $N^{\beta, u}$ are summable, the twisted theta value $\vartheta_m(p^u)$ is a unit times the value of $\Theta_{\beta, m}(p)$ at $u$, where $p^u$ is the class $p$ moved into the twist. The unit depends on $u$ and $y$, but in a homogeneous polynomial it gives only a common factor.

### Mumford's construction over the complex numbers

**Theorem 6.2.6 (Small complex degenerations).** Assume the seven inputs. Let $R$ be a domain with a map $\operatorname{Frac} R \to \mathbb{C}$, let $\mathcal{A}$ be a complete arc datum over $(R, \mathbb{C})$ with $\rho = \rho_{\mathbb{C}}$, let $\beta$ be a balanced form with values in $2k\mathbb{Z}$, and let $m$ be odd with $m^2 \mid k$. Then there is $\varepsilon > 0$ such that for every $u \in \mathbb{C}^\times$ with $|u| < \varepsilon$ the following holds. For each $x \in \Lambda$, the theta terms of $N^{\beta, u}$ at the class $q_{m^2}(x)^u$ are absolutely summable, and there is an object $o$ with full level over $\mathbb{C}$ with $\rho = \rho_{\mathbb{C}}$, $\zeta_{m^2} = \zeta_{m^2}(\mathcal{A})$, and theta point of level $m$ equal to $x \mapsto \vartheta_m(q_{m^2}(x)^u)$.

Lean: `GlobalTheory.T.exists_thetaPoint_complexDegeneration_small`.

*Proof.* We follow the classical construction. The data of $\mathcal{A}$ give a lattice $\mathsf{X}$ with an action of $\mathcal{O}_E$, a period map and a theta function $\vartheta$ on the abelian part. Write $u = e^{2\pi i w}$ with $\operatorname{Im} w$ large; this is possible once $|u| < e^{-2\pi T}$. For $\operatorname{Im} w > T_1$ the periods $\mathsf{X} \to \mathbb{C}^g$ scaled by $w$ form a lattice $\Lambda_w$ with a positive hermitian form, by the positivity of $\beta$. For $\operatorname{Im} w > T_2$ the theta sums converge locally uniformly and are holomorphic. Take $\varepsilon = e^{-2\pi \max(T_1, T_2)}$.

Fix $u$ with $|u| < \varepsilon$. The complex torus $\mathbb{C}^g / \Lambda_w$, with its hermitian form, is the analytic space of a polarized abelian variety $Q$ with an action of $\mathcal{O}_E$ and the determinant condition of $D$; this uses complex uniformisation (input 7). Its torsion points $\Lambda_w / m^2$ give a Tate isomorphism with the roots of unity of $\mathcal{A}$. The theta sum of $\vartheta$ is a nonzero theta function $\Theta$ for the factor of automorphy of $Q$, since some value of the sum is nonzero. By the classical formula for theta null points, the values $\Theta(m^{-1} \ell)$, times the factors $\chi(\ell)\exp(-\pi H(\ell, \ell)/2m^2)$, form the theta point of level $m$ of $Q$ at the points $m^{-2}\ell$. Under the period map these values are the twisted theta series $\vartheta_m(q_{m^2}(x)^u)$, term by term. $\square$

### The identity principle

**Theorem 6.2.7 (Identity principle).** Let $N$ be a numerical degeneration datum over $\mathbb{C}$, let $\beta$ be a form with values in $2k\mathbb{Z}$, let $m$ be odd with $m^2 \mid k$, let $p_i \in Q_{m^2}(N)$ for $i$ in a set $I$, and let $P$ be a polynomial in variables indexed by $I$. Assume there is $\varepsilon > 0$ such that for each $u$ with $0 < |u| < \varepsilon$ the theta terms at all $p_i^u$ are summable and $P(\vartheta_m(p_i^u)) = 0$. Then $P(\Theta_{\beta, m}(p_i)) = 0$ in $\mathbb{C}[[X]]$.

Lean: `GlobalTheory.Ex.ArcForm.aeval_arcTx_eq_zero`.

*Proof.* Each $\Theta_{\beta, m}(p_i)$ converges on the disc $|u| < \varepsilon$, with sum $\vartheta_m(p_i^u)$. So $P(\Theta_{\beta, m}(p_i))$ is a power series that converges on the disc and vanishes on the punctured disc. By the identity theorem it is zero. $\square$

**Theorem 6.2.8 (Theta relations hold for formal theta series).** Assume the seven inputs. Let $R$ be a domain, let $F$ be an algebraically closed field of characteristic $0$ over $\operatorname{Frac} R$, let $\mathcal{A}$ be a complete arc datum over $(R, F)$ and let $\beta$ be a balanced form with values in $2k\mathbb{Z}$. Let $m$ be odd with $m^2 \mid k$, and assume that $(\zeta_{m^2}(\mathcal{A}), \rho)$ is compatible at level $m^2$. Then for every complex theta relation $G$ of level $m$,
$$G^{c}\bigl( x \mapsto \Theta_{\beta, m}(q_{m^2}(x)) \bigr) = 0 \quad \text{in } F[[X]],$$
where $G^c$ is the image of $G$ under $c_{\zeta_{m^2}(\mathcal{A}), \rho}$.

Lean: `GlobalTheory.T.theta_series_identity_principle_complex_points` (also `GlobalTheory.ArcIdentity.aeval_arcTx_eq_zero_of_vanishC`, a second name).

*Proof.* Let $d$ be the degree of $G$.

First we descend. There are a countable domain $R_1$, a countable algebraically closed field $F_1$ of characteristic $0$, an embedding $f : F_1 \to F$ and a complete arc datum $\mathcal{A}_1$ over $(R_1, F_1)$ such that $\mathcal{A}$ is the base change of $\mathcal{A}_1$ along $f$. The form $\beta$ comes from a form $\beta_1$ on $\mathsf{X}(N_1)$, which is balanced since $\beta$ is. A homomorphism of numerical data multiplies each formal theta series by a common unit and carries the coefficients along $f$. Since $G$ is homogeneous, the relation for $\mathcal{A}$ follows from the relation for $\mathcal{A}_1$, because $f$ is injective. The pair $(\zeta_{m^2}(\mathcal{A}_1), \rho_1)$ is compatible at level $m^2$, again because $f$ is injective.

Next we embed $F_1$ in $\mathbb{C}$. The numbers $\zeta^{\mathbb{C}}_{m^2}$ and $\rho_{\mathbb{C}}$ are algebraic over $\mathbb{Q}$: the first is a root of unity and the second satisfies $\rho_{\mathbb{C}}^2 = -d$. Since $F_1$ is countable and algebraically closed, and $\mathbb{C}$ has uncountable transcendence degree, the compatibility gives a field map $g : F_1 \to \mathbb{C}$ with $g(\zeta_{m^2}(\mathcal{A}_1)) = \zeta^{\mathbb{C}}_{m^2}$ and $g(\rho_1) = \rho_{\mathbb{C}}$. Base change along $g$ gives a complete arc datum $\mathcal{A}_2$ over $(R_1, \mathbb{C})$ with $\rho = \rho_{\mathbb{C}}$, with $\zeta_{m^2} = \zeta^{\mathbb{C}}_{m^2}$ and with a balanced form $\beta_2$. As in the descent step, the relation for $\mathcal{A}_1$ follows from the relation for $\mathcal{A}_2$.

Over $\mathbb{C}$, the theorem on small complex degenerations gives $\varepsilon > 0$, and for each $u$ with $|u| < \varepsilon$ an object $o$ with full level whose theta point of level $m$ is $x \mapsto \vartheta_m(q_{m^2}(x)^u)$. Since $G$ is a complex theta relation, $G^c$ vanishes at this point. The identity principle now gives $G^c(\Theta_{\beta_2, m}(q_{m^2}(x))) = 0$. $\square$

**Remark 6.2.9 (Formalization).** The Lean proof of the theorem on small complex degenerations is a separate theorem, `GlobalTheory.Ex.Arch.exists_full_of_small` ([ExistsThetaPointComplexDegenerationSmall.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsThetaPointComplexDegenerationSmall.lean#L198)). It is too small to be a declaration of this chapter, so we gave only a sketch of it, following its steps in `of_steps` (same file, line 138). Of the seven inputs it uses the laws and complex uniformisation. In the identity principle for theta relations, the oddness of $m$ inside the definition of a complex theta relation is discarded, since $m$ is odd by hypothesis ([ThetaSeriesIdentityPrincipleComplexPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ThetaSeriesIdentityPrincipleComplexPoints.lean#L170)). The descent to a countable field and the embedding into $\mathbb{C}$ are the lemmas `exists_countable_model` and `exists_ringHom_complex_of_countable_of_relations`, which we did not unfold. The identity principle is `GlobalTheory.Ex.ArcForm.aeval_arcTx_eq_zero` ([AevalArcTxEqZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/AevalArcTxEqZero.lean#L89)). We have not unfolded `IsThetaPt`, `TateIso` or `DetCond`.
