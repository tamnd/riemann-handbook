---
title: Analytic charts at complex points
decls:
  - GlobalTheory.AnVal.isFrame_of_isAnE
  - GlobalTheory.AnVal.AnPt.chartOf
  - GlobalTheory.AnVal.exists_analytic_chart
  - GlobalTheory.T.exists_analytic_biextension_chart_complex_point
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Analytic charts at complex points

A harmonic value is read in a formal chart of the universal abelian scheme. Over a general base the chart is built from jets, and its formal group law is not additive. At a complex point there is a better chart: the one that comes from a complex uniformization. In it the group law is $X + Y$, the action of the integers of $E$ is linear, and the germ of a section is the Taylor series of the theta function that represents it. This section builds that chart. The next section uses it to identify harmonic values with derivatives of theta functions. The background is in [complex tori](/learn/abelian-varieties/#complex-tori), [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization) and [theta functions on complex tori](/learn/theta-functions-cm/#theta-functions-on-complex-tori).

### Analytic points

Let $E$ be a CM [[number field|MWBDFS2KJ5]] with complex conjugation $a \mapsto \bar a$ on $\mathcal{O}_E$. Let $X_o$ be the moduli scheme of a datum and a level, with universal abelian scheme $A$, line bundle $L$, cubical structure and $\mathcal{O}_E$-action. Let $F \subset \mathbb{C}$ be a coefficient field of the level.

**Definition 2.2.1 (framed point).** A *framed complex point* $y$ is a point $x$ of $X_o$ over $\mathbb{C}$ together with a tangent vector $u_\ell$ of $A_x$ at $0$ for each letter row $\ell = (\tau, i)$, with $i < m_\tau$.

**Definition 2.2.2 (analytic point).** Let $y$ be a framed complex point, $g \geq 0$, $t_1, \dots, t_g$ embeddings of $E$ and $\epsilon$ a bijection from $\{1, \dots, g\}$ to the letter rows. An *analytic point* over $y$ consists of:

1. a surjective holomorphic homomorphism $e : \mathbb{C}^g \to A_x(\mathbb{C})$ whose kernel is a lattice $\Lambda$;
2. a Hermitian form $H$ on $\mathbb{C}^g$, a character $\chi$ of $\Lambda$ with $|\chi| = 1$, and nonvanishing holomorphic trivializations $f_j$ of $e^\ast L$ that satisfy the Appell-Humbert law
$$f_j(z) = \chi(\lambda)\, \exp\Bigl(\pi H(z, \lambda) + \tfrac{\pi}{2} H(\lambda, \lambda)\Bigr) f_j(z + \lambda), \qquad \lambda \in \Lambda;$$
3. the linearity $e(t(a) z) = a \cdot e(z)$ for $a \in \mathcal{O}_E$, where $t(a)$ multiplies coordinate $k$ by $t_k(a)$, and the adjointness $H(t(a) z, w) = H(z, t(\bar a) w)$;
4. for each row $\ell$, the derivative of $e$ at $0$ along the coordinate $\epsilon^{-1}(\ell)$ is $u_\ell$.

A section $s$ of $L^k$ at $x$ *reads as* a function $\theta : \mathbb{C}^g \to \mathbb{C}$ if $s(e(z)) = \theta(z) f_j(z)^k$ in each trivialization.

The jets of $e$ at $0$ give a compatible family of maps $x_m$ from the $m$-th order jet scheme to $A$. A *biextension frame* is a family $e_m$ of generators of the pullback of the cube line bundle along the pair of jet points. It is *analytic* if each $e_m$ is a generator that reads, through the addition map $(z_0, z_1) \mapsto z_0 + z_1$, as a product of the trivializations $f_j$.

### Charts

**Definition 2.2.3 (chart).** A *chart* at a framed point $y$ consists of a dimension $d$, a formal group law $\mathcal{F}(X, Y)$ in $d$ variables, an action of $\mathcal{O}_E$ by power series, four cocycles $\varphi_1, \varphi_2, \sigma, \alpha_a$, tangent coordinates $u_\ell \in \mathbb{C}^d$, jet maps $x_m$, a biextension frame $e_m$, a primitive generator $w$, and a gauge $h$. These data satisfy five conditions:

1. *chart:* the maps $x_m$ are compatible with truncation, send the augmentation to $0$, carry $\mathcal{F}$ to the group law and the formal action to the action of $\mathcal{O}_E$, and have tangent vectors $u_\ell$, which form a basis;
2. *frame:* each $e_m$ is a generator, and $\varphi_1, \varphi_2, \sigma, \alpha_a$ measure its failure to satisfy the two partial laws of the biextension, the symmetry and the adjointness;
3. *primitive:* $w$ is a generator that restricts to the rigidification along the zero section;
4. *gauge:* the formal data are in the canonical gauge $h$;
5. *rigidity:* at order $0$ the frame and $w$ give the rigidification of $L$ at $0$.

A section $s$ of $L^k$ has *germ* $f \in \mathbb{C}[[z_1, \dots, z_d]]$ if for every $m$ the pullback of $s$ to the $m$-th jet scheme is the truncation of $f$ times the $k$-th power of the generator built from $e_m$ and $w$.

We do not unfold the conditions further. The exact form of the cube generators is not needed in this section.

**Lemma 2.2.4 (analytic frames are frames).** Assume that the involution of $\mathcal{O}_E$ is the conjugation of $E$. Let $(e_m)$ be an analytic biextension frame. Then $(e_m)$ satisfies the frame condition for the additive law $X + Y$, the linear action $a \mapsto t(a)$, and all four cocycles equal to $1$.

Lean: `GlobalTheory.AnVal.isFrame_of_isAnE`.

*Proof.* The frame condition has five parts. The generator part is the first half of the analyticity. First, the jet maps $x_m$ are exponential immersions at $0$. Then the two partial laws, the symmetry and the adjointness hold with trivial cocycles, by four lemmas. Each lemma compares two readings of the same generator through the Appell-Humbert law. In the additive chart the two readings agree on the nose. The adjointness uses the hypothesis on the involution, through the equation $H(t(a) z, w) = H(z, t(\bar a) w)$. $\square$

**Definition 2.2.5 (the analytic chart).** Let $y$, $\Phi = (e, H, \chi, f_j)$ be an analytic point, $(e_m)$ an analytic frame and $w$ a primitive generator. The *analytic chart* has $d = g$, the additive law, the action $t(a)$, trivial cocycles, gauge $h = 0$, tangent coordinates $u_\ell = $ the standard basis vector at $\epsilon^{-1}(\ell)$, jet maps the jets of $e$ at $0$, frame $(e_m)$ and primitive generator $w$.

Lean: `GlobalTheory.AnVal.AnPt.chartOf`.

The five conditions hold as follows. The chart condition holds because the exponential jets of a CM uniformization form a chart. The frame condition is the Lemma. The gauge condition holds because the trivial data with $h = 0$ are canonical. The rigidity comes from the Appell-Humbert description of the line bundle frame at $0$.

### The chart theorem

**Theorem 2.2.6 (analytic chart at a complex point).** Assume that the involution of $\mathcal{O}_E$ is complex conjugation. Let $\Phi$ be an analytic point of dimension $g$ over a framed complex point $y$. Then there is a chart $C$ at $y$ of dimension $d = g$ with gauge $h = 0$ such that:

1. the formal group law is $\mathcal{F}_i(X, Y) = X_i + Y_i$ for every $i$;
2. for every row $\ell$, the tangent coordinate $u_\ell$ is the standard basis vector at $\epsilon^{-1}(\ell)$;
3. for every $k$, every section $s$ of $L^k$ at $x$ and every $\theta$ such that $s$ reads as $\theta$, the germ of $s$ in $C$ is the Taylor series
$$\sum_{\nu \in \mathbb{N}^g} \frac{\partial^\nu \theta(0)}{\nu!}\, z^\nu.$$

Lean: `GlobalTheory.AnVal.exists_analytic_chart` (also `GlobalTheory.T.exists_analytic_biextension_chart_complex_point`, a second name).

*Proof.* A lemma gives an analytic biextension frame $(e_m)$. A second lemma gives a primitive generator $w$ that reads as $1$ in the analytic frame. Let $C$ be the analytic chart built from them. Then $d = g$ and $h = 0$ by definition. Claims 1 and 2 hold by definition of the additive law and of the tangent coordinates.

For claim 3, fix $m$. The jet point $x_m$ is the exponential jet of $e$. A lemma on jet readings gives a generator $\tau$ of the pullback of $L^k$ that reads as a power of the trivialization. Since $s$ reads as $\theta$, the pullback of $s$ to the jet scheme is the value of $\theta$ at the jet, that is, the truncation of the Taylor series at order $m$, times $\tau$. The Appell-Humbert lemma for the frame says that $\tau$ is the $k$-th power of the generator built from $e_m$ and $w$. This is the germ condition at order $m$. $\square$

**Remark 2.2.7.** Classically, a section of $L^k$ on a complex torus $\mathbb{C}^g / \Lambda$ is a theta function for the factor of automorphy of Appell and Humbert. In the analytic chart the germ is the Taylor expansion of that theta function. So harmonic values defined through germs become values of differential operators on theta functions. The Theorem gives this identification in all orders at once. It is the complex form of the classical theory in Mumford, *Tata Lectures on Theta I*, Chapter II.

**Remark 2.2.8 (Formalization).** The Theorem is in [ExistsAnalyticBiextensionChartComplexPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsAnalyticBiextensionChartComplexPoint.lean#L73), with the Lemma at L30 and the chart at L50. The statement carries an equality $d = g$ and renames the variables of the germ along it. The proof takes $d = g$ by definition and removes the renaming with a small lemma at L67. Two of the three goals close by a `first | rfl | simp` combinator at L79 and L83. The second name is in [ExistsAnalyticBiextensionChartComplexPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsAnalyticBiextensionChartComplexPointStatement.lean#L10), proved by a `first` combinator under a raised heartbeat limit. The chart structure and the frame condition are in [ThGerm.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThGerm.lean#L189). The trivial formal data are in [ComposeLinearAction.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PullbackSections/HolomorphicFamilies/ComposeLinearAction.lean#L110).
