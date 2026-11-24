---
title: Metrics on Lie algebras of semi-abelian schemes
decls:
  - GlobalTheory.CompanionTheory.Ar.TorusUnif.stratum_good
  - GlobalTheory.CompanionTheory.Ar.TorusUnif.torus_unif
  - GlobalTheory.T.semiabelian_lie_metric_height
  - GlobalTheory.CompanionTheory.Ar.SlopeUnif.slope_unif
  - GlobalTheory.T.hodge_cpt_lie_metric_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Metrics on Lie algebras of semi-abelian schemes

A semi-abelian scheme $G$ over a base $X$ has a Lie algebra, and a metric on the tangent spaces at the complex points of $X$ gives every integral point of $X$ a hermitian bundle over a ring of integers. This section proves two uniform bounds for these bundles. The first bound says that the torus part of the Lie algebra is close to an orthonormal lattice, with one constant for all integral points. The second bound controls the maximal slope of the whole Lie algebra by a logarithm of its degree. The second bound is the slope input that the fibre input of [the next sections](/entry/fibre-input/) uses. For the background on semi-abelian schemes see [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction), and for slopes see [hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes).

Throughout, $X$ is a scheme with a point $\xi : \operatorname{Spec}\Omega \to X$ such that every point of $X$ is a specialization of the image of $\xi$. A family of coordinates $y = (y_{k,i})$ in $\Omega$, indexed by $k \in K$ and $i \in J_k$, is tied to $\xi$ over $\mathbb{Z}$: the products $\prod_k y_{k,c(k)}$ give multi-projective charts of $X$. We write $X_{\mathbb{Q}} = X \times_{\mathbb{Z}} \mathbb{Q}$ for the generic fibre.

**Definition 8.1.1 (Lie model).** Let $G$ be a group scheme over $X$, let $x$ be a point of $X$ with values in a ring $A$, and let $E$ be an $A$-module. A Lie model of $G$ at $x$ on $E$ is a bijection from $E$ to the tangent vectors of $G$ at $x$, that is, to the points of $G$ with values in $A[\varepsilon]/(\varepsilon^2)$ above $x$ that reduce to the unit. The bijection is additive and compatible with scalars. On a split torus with character group $\mathsf{X}$, a Lie model on the cocharacters $\operatorname{Hom}(\mathsf{X}, A)$ is a cocharacter model if the tangent vector of a cocharacter $\delta$ takes the value $1 + \varepsilon\,\delta(\chi)$ on each character $\chi$.

**Definition 8.1.2 (Lie metric).** Let $M$ be a Lie model of $G$ at $\xi$ on $\operatorname{Lie}$. A Lie metric for $M$ and $y$ is an inner product $h_z$ on the tangent space at each complex point $z$ of $X$. It is hermitian on every Lie model at $z$, it is compatible with complex conjugation, and it is continuous in the coordinates $y$.

**Definition 8.1.3 (Fibre of a Lie metric).** Let $L$ be a number field and let $z : \operatorname{Spec} \mathcal{O}_L \to X$. Let $B$ be a hermitian bundle over $\mathcal{O}_L$ with a Lie model $M_B$ of $G$ at $z$ on $B$. Then $B$ is the fibre of $h$ at $z$ if, for every embedding $\sigma : L \to \mathbb{C}$, the metric of $B$ at $\sigma$ is $h$ at the complex point $\sigma \circ z$.

**Definition 8.1.4 (Good constant).** Let $L$ be a number field, $z : \operatorname{Spec}\mathcal{O}_L \to X$, let $G_L$ be a group scheme over $L$ with a map $\varphi : G_L \to G$, and let $\tau$ be a torus extension of $G_L$, with split torus of character group $\mathsf{X}$. A constant $C$ is good at $(z, \varphi, \tau)$ if there is a $\mathbb{Z}$-basis $\beta_1, \dots, \beta_r$ of the cocharacters $\operatorname{Hom}(\mathsf{X}, \mathbb{Z})$ with this property. For every cocharacter model of the torus, every fibre $(B, M_B)$ of $h$ at $z$, every family $\varepsilon_1, \dots, \varepsilon_r$ in $B$ such that $\varepsilon_a$ lifts the tangent vector of $\beta_a$ through $\tau$ and $\varphi$, every $\sigma$ and every $w \in \mathbb{C}^r$,

$$
C^{-1} \sum_a |w_a|^2 \;\le\; \Big\| \sum_a w_a \otimes \varepsilon_a \Big\|_\sigma^2 \;\le\; C \sum_a |w_a|^2 .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.TorusUnif.GoodAt`

The published input is the extension theorem for homomorphisms. Over a noetherian normal base $S$ with a dense open $U$, a homomorphism of semi-abelian schemes over $U$ extends uniquely to $S$. We take it as given.

**Lemma 8.1.5.** Assume the extension theorem for homomorphisms of semi-abelian schemes. Let $G$ be a commutative semi-abelian scheme over $X$ with a Lie model $M$ at $\xi$ and a Lie metric $h$. Let $Z$ be an integral scheme with a closed immersion $i : Z \to X_{\mathbb{Q}}$. Then there are a nonempty open $U \subset Z$ and a constant $C \ge 1$ with this property. Let $L$ be a number field, $z : \operatorname{Spec}\mathcal{O}_L \to X$, and let $G_L$ be a group pullback of $G$ along $\operatorname{Spec} L \to X$ with a map $\varphi$ and a torus extension $\tau$. If the generic point of $z$ in $X_{\mathbb{Q}}$ factors as $i \circ z_Z$ with $z_Z$ landing in $U$, then $C$ is good at $(z, \varphi, \tau)$.

Lean: `GlobalTheory.CompanionTheory.Ar.TorusUnif.stratum_good`

*Proof.* Over a finite surjective cover $Z' \to Z$ that is normal and integral, the pullback of $G$ contains a split torus $T_{Z'}$ by a homomorphism that is injective over a nonempty open set. The extension theorem gives this homomorphism over all of $Z'$, and injectivity holds on an open $U'$. On $T_{Z'}$ the cocharacters give a frame of the Lie algebra, and $h$ gives a Gram matrix for this frame. The complex points of $Z'$ over a compact part of $U$ form a compact set, the Gram matrix is continuous, and it is positive definite. So its eigenvalues lie in $[C^{-1}, C]$ for one $C \ge 1$. A point $z$ as in the statement lifts to $Z'$ after a finite extension. The torus of $\tau$ is then the pullback of $T_{Z'}$, and its cocharacters match. The norm of $\sum_a w_a \otimes \varepsilon_a$ at $\sigma$ is the Gram form at the complex point, and the bound follows. $\square$

**Theorem 8.1.6 (Uniform torus metric).** Assume the extension theorem for homomorphisms of semi-abelian schemes. Let $\Omega$ have characteristic $0$, let $G$ be a commutative semi-abelian scheme over $X$, let $M$ be a Lie model of $G$ at $\xi$, and let $h$ be a Lie metric for $M$ and $y$. Then there is $C \ge 1$ such that $C$ is good at $(z, \varphi, \tau)$ for every number field $L$, every $z : \operatorname{Spec}\mathcal{O}_L \to X$, every group pullback $G_L$ of $G$ along $\operatorname{Spec} L \to X$ with map $\varphi$, and every torus extension $\tau$ of $G_L$.

Lean: `GlobalTheory.CompanionTheory.Ar.TorusUnif.torus_unif` (also `GlobalTheory.T.semiabelian_lie_metric_height`, a second name)

*Proof.* The space $X_{\mathbb{Q}}$ is noetherian. We use noetherian induction over its closed irreducible subsets. Each such subset carries an integral closed subscheme $Z$, and the lemma gives an open $U \subset Z$ and a constant on $U$. The complement of $U$ in $Z$ is a smaller closed set, so the induction ends after finitely many steps. The maximum of the constants is good everywhere, since a larger constant stays good. $\square$

The second result concerns a Hodge component $\mathfrak{M}$ of an integral model $Y$ of a unitary Shimura variety of signature $(p, q)$. It carries a base $X$, a point $\xi$, coordinates $y$, a semi-abelian scheme $t$ over $X$ with Lie model $M$ on $\operatorname{Lie}$, and Hodge vector bundles. Its abelian part is principal: proper, with a relatively ample line and trivial canonical sheaf. The slope input is the following statement. There is $C_0 \ge 0$ such that, for the Lie algebra $B$ with the Hodge metric of a principal semi-abelian scheme over $\mathcal{O}_L$,

$$
\mu_{\max}(B) \le C_0 \log\big(2 + \operatorname{rk} B + \max(-\widehat{\deg}_n B, 0)\big).
$$

Here $\widehat{\deg}_n$ is the normalized arithmetic degree, the degree divided by $[L : \mathbb{Q}]$.

**Theorem 8.1.7 (Slope bound for Hodge components).** Assume the existence of the moduli schemes for $1 \le p + q$, the first part of the integral model theory, resolution of singularities in characteristic $0$, the extension theorem for homomorphisms of semi-abelian schemes and the slope input. Let $\mathfrak{M}$ be a Hodge component with Lie metric $h$, and let $1 \le p + q$. Then there is $C \ge 0$ with this property. For every number field $L_0$ and $z_0 : \operatorname{Spec}\mathcal{O}_{L_0} \to X$ there is a finite extension $e : L_0 \to L$ such that every fibre $(B, M_B)$ of $h$ at the base change of $z_0$ to $\mathcal{O}_L$ satisfies

$$
\mu_{\max}(B) \le C \log\big(2 + C + \max(-\widehat{\deg}_n B, 0)\big) + C .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.SlopeUnif.slope_unif` (also `GlobalTheory.T.hodge_cpt_lie_metric_bound`, a second name)

*Proof.* There is $K_0 \ge 1$ such that, on the abelian part, the Hodge inner product is at most $K_0$ times $h$. The uniform torus metric gives $C_1$ and the slope input gives $C_0$. Let $C_c = \max(K_0, C_1, C_0, 1)$.

After a finite extension $L$ of $L_0$ the abelian part extends to an abelian scheme $t'$ over $\mathcal{O}_L$, it stays principal, and the generic fibre of $G$ over $L$ is a torus extension of $t'_L$. Let $B'$ be the Lie algebra of $t'$ with the Hodge metric. The slope input bounds $\mu_{\max}(B')$. The torus extension gives lifts $\varepsilon_a \in B$ of the cocharacters and a quotient map $f : B \to B'$ whose kernel is spanned by the $\varepsilon_a$. The norms satisfy $\|f x\|_\sigma^2 \le K_0 \|x\|_\sigma^2$, and the uniform torus metric gives the Gram bounds for the $\varepsilon_a$ with constant $C_c$.

A general quotient lemma for hermitian bundles now applies. Let $E$ have rank $g$, let $\varepsilon$ be independent and span the kernel of a map $q : E \to E'$ that is surjective up to scalars. If the $\varepsilon$ satisfy the Gram bounds with constant $C_c$, if $\|q x\|^2 \le C_c\|x\|^2$, and if $\mu_{\max}(E') \le C_c \log(2 + \operatorname{rk} E' + \max(-\widehat{\deg}_n E', 0))$, then $\mu_{\max}(E) \le C' \log(2 + C' + \max(-\widehat{\deg}_n E, 0)) + C'$ for a constant $C'$ that depends only on $g$ and $C_c$. The rank $g$ is the rank of $\operatorname{Lie}$, so $C = C'$ does not depend on $z_0$. $\square$

**Remark 8.1.8 (Formalization).** The uniform torus metric `torus_unif` takes `CharZero Ω` as an explicit hypothesis, but the proof introduces it as `hc` and never uses it (SemiabelianLieMetricHeight.lean:333 to 334). The stratum lemma `stratum_good` has no such hypothesis. The slope bound obtains `CharZero Ω` from the injectivity of `𝔐.cst` and passes it on. The steps of both proofs go through named results such as `T.semiabelian_finite_cover_torus`, `T.analytic_points_finite_compact`, `T.hermitian_bundle_quotient_degree_bound` and `T.semi_abelian_pullback_torus_extension`, which we do not unfold. The four inputs of the slope bound are `N1ab` (moduli exist for $1 \le p+q$), `PartI` (integral models with local systems), `Geo.ResK.ResKStatement` (resolution with coordinates) and `SlopeBoundSt`.
