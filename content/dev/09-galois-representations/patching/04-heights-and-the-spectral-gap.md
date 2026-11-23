---
title: Heights, moments and the spectral gap
decls:
  - PositivityTheory.KB.sPU
  - PositivityTheory.KB.sPU_of
  - PositivityTheory.KB.sMom
  - PositivityTheory.KB.TwSMInt2.sMom_of
  - PositivityTheory.KB.sGap_of
  - PositivityTheory.KB.sLoc
  - PositivityTheory.KB.sLoc_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Heights, moments and the spectral gap

The [Hecke vanishing theorem](/entry/s-hecke/) asks for a cocycle whose Hecke iterates decay at rate $3/5$. This section supplies the analysis that produces such decay. A real cocycle of $\mathrm{GL}_N(\mathcal{O}_L)$ is represented by a differential form on the symmetric space of positive Hermitian matrices. The size of the form is controlled by a height function, and four estimates hold: a partition of unity with controlled derivatives, finiteness of moments of the height on a fundamental domain, a spectral gap for the Hecke operator on $L^2$, and a bound for the evaluation of a cocycle by the $L^2$ norm of the form. The background is in [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups), [quotients of finite volume](/learn/groups/#quotients-of-finite-volume) and [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms).

### The symmetric space and the height

Let $L$ be a number field and $N \ge 1$. For each infinite place $w$ of $L$ fix an embedding $\sigma_w \colon L \to \mathbb{C}$ in its class. Put
$$G_\infty = \prod_{w \mid \infty} \mathrm{GL}_N(\mathbb{C}), \qquad S_\infty = \prod_{w \mid \infty} \mathrm{SL}_N(\mathbb{C}).$$
The group $\Gamma_N = \mathrm{GL}_N(\mathcal{O}_L)$ maps into $G_\infty$ by $\gamma \mapsto (\sigma_w(\gamma))_w$, and $\Lambda_N$ denotes the image of $\mathrm{SL}_N(\mathcal{O}_L)$ in $S_\infty$, a discrete subgroup. Let $\mathcal{H}$ be the real vector space of tuples $h = (h_w)_w$ of Hermitian $N \times N$ matrices, and $\mathcal{P} \subset \mathcal{H}$ the open cone where each $h_w$ is positive definite. The group $G_\infty$ acts on $\mathcal{H}$ by
$$g \cdot h = \big( (g_w^{-1})^{*}\, h_w\, g_w^{-1} \big)_w,$$
and this action preserves $\mathcal{P}$. Write $1 \in \mathcal{P}$ for the tuple of identity matrices. The orbit map $g \mapsto g \cdot 1$ identifies $\mathcal{P}$ with $G_\infty / \prod_w \mathrm{U}(N)$, the symmetric space of $G_\infty$.

For $h \in \mathcal{H}$ and $y \in \mathcal{O}_L^N$ put $q_h(y) = \sum_w \mathrm{Re}\big( \sigma_w(y)^{*} h_w \sigma_w(y) \big)$. For $h \in \mathcal{P}$ this is a positive definite quadratic form on the lattice $\mathcal{O}_L^N$. Its *minimum* is
$$\lambda(h) = \inf_{0 \ne y \in \mathcal{O}_L^N} q_h(y),$$
and $h^\vee = (\overline{h_w}^{-1})_w$ is the dual form.

**Definition 7.4.1 (Height).** The *height* of $x \in G_\infty$ is
$$\mathrm{ht}(x) = \frac{1}{\lambda(x \cdot 1)\, \lambda\big((x \cdot 1)^\vee\big)}.$$

The height is large when the lattice $\mathcal{O}_L^N$ has a short vector or a short dual vector for the form $x \cdot 1$, that is, when $x$ is far out in a cusp. It is invariant under $\Gamma_N$ on the left. We take the following basic properties as given; they are proved by the classical reduction theory of positive forms. For $L$ totally complex and $N \ge 1$, the height is continuous, it satisfies $\mathrm{ht}(\gamma x) = \mathrm{ht}(x)$ for $\gamma \in \Gamma_N$, it is bounded below by a positive constant, and for each compact $K \subset G_\infty$ there is $C$ with $\mathrm{ht}(xg) \le C\, \mathrm{ht}(x)$ for $g \in K$.

### Forms and their frames

A *$q$-form* on $\mathcal{H}$ is a map $\omega$ from $\mathcal{H}$ to continuous alternating $q$-linear forms on $\mathcal{H}$. For a $q$-form $\omega$ and points $y_0, \dots, y_q$ of $\mathcal{P}$, let $\int_{[y_0, \dots, y_q]} \omega$ be the integral of $\omega$ over the affine simplex with these vertices. Since $\mathcal{P}$ is convex, this simplex lies in $\mathcal{P}$. This defines a homogeneous cochain $I_\omega$ on $\mathcal{P}$. The form is *good* if it is continuous on $\mathcal{P}$ and $d I_\omega = 0$; by Stokes's theorem this holds for a closed form of class $C^1$. The *frame* of $\omega$ at $x \in G_\infty$ is the alternating form
$$\mathrm{fr}_\omega(x) = \omega(x \cdot 1) \circ (x \cdot)^{\otimes q},$$
that is, $\omega$ at the point $x \cdot 1$ read in the frame moved from $1$ by $x$. The form is *invariant* under $g$ if $\omega(g \cdot h) \circ (g\cdot)^{\otimes q} = \omega(h)$ for all $h \in \mathcal{P}$; then $\|\mathrm{fr}_\omega\|$ is left invariant under $g$.

A *fundamental domain datum* is a Haar measure $\mu$ on $S_\infty$, which is also right invariant, together with a measurable fundamental domain $D$ for $\Lambda_N$ acting on the left, with $\mu(D) < \infty$.

### The partition of unity

**Definition 7.4.2 (Controlled partition of unity).** Let $H \colon G_\infty \to \mathbb{R}$. A *partition of unity controlled by $H$* is a function $\varphi \colon \mathcal{H} \to \mathbb{R}$, smooth on $\mathcal{P}$, such that:

1. the supports of $h \mapsto \varphi(\gamma^{-1} \cdot h)$ for $\gamma \in \Gamma_N$ form a locally finite family on $\mathcal{P}$, and $\sum_{\gamma \in \Gamma_N} \varphi(\gamma^{-1} \cdot h) = 1$ for $h \in \mathcal{P}$;
2. only finitely many $\gamma$ move a point of the closed support of $\varphi$ into the closed support of $\varphi$;
3. $\varphi(rh) = \varphi(h)$ for $r > 0$, and $\varphi$ is bounded on $\mathcal{P}$;
4. there is $C$ with $\| d\varphi(x \cdot 1) \circ (x \cdot) \| \le C\, H(x)$ for all $x \in G_\infty$.

Such a partition is used to build a form from a cocycle: one spreads the cocycle over the translates of the support of $\varphi$. Condition 4 bounds the frame of the result by a power of $H$.

**Theorem 7.4.3 (Partition of unity).** Let $L$ be totally complex. There is $a \ge 0$ such that for every $N \ge 1$ there is a partition of unity controlled by $\mathrm{ht}^a$.

Lean: `PositivityTheory.KB.sPU` (also `PositivityTheory.KB.sPU_of`, the same statement with the basic properties of the height as a hypothesis).

*Proof.* We describe the construction. The first step is a smooth $\Gamma_N$-equivariant retraction $h \mapsto r(h)$ of $\mathcal{P}$ that pushes each form away from the cusps: $r(h)$ is $h$ plus a smoothed sum of rank one terms coming from the short vectors of $h$, so that $\lambda(r(h))$ and $\lambda(r(h)^\vee)$ are bounded below by positive constants. The lattice point counts of $q_h$ are doubling up to a constant, and this makes the smoothing possible. The retraction moves nearby points to nearby points, with a Lipschitz constant of order $1 + (\lambda(h) \lambda(h^\vee))^{-1}$, which is bounded by a constant times the height. Second, the forms $h$ with $\lambda(h)$ and $\lambda(h^\vee)$ bounded below lie, up to $\Gamma_N$, in a compact subset of $\mathcal{P}$ (Mahler's compactness criterion), and $\Gamma_N$ acts properly on $\mathcal{P}$. So a smooth bump function $\psi$ with compact support in $\mathcal{P}$, normalized by the sum of its translates, gives a partition of unity on the thick part. Third, put $\varphi = \psi \circ r \circ n$, where $n$ is a smooth normalization that makes the result homogeneous of degree $0$. Conditions 1 to 3 follow from the properties of $\psi$ and properness. The chain rule and the Lipschitz bound for $r$ give condition 4, with a fixed power $a$ of the height. $\square$

### Moments of the height

**Theorem 7.4.4 (Moments).** Let $L$ be totally complex. For each $A \ge 0$ there is $N_0$ such that for all $N \ge N_0$ there is a fundamental domain datum $(\mu, D)$ for $\Lambda_N$ in $S_\infty$ with
$$\int_D \mathrm{ht}(x)^A \, d\mu(x) < \infty.$$

Lean: `PositivityTheory.KB.sMom` (also `PositivityTheory.KB.TwSMInt2.sMom_of`, the same statement with the basic properties of the height as a hypothesis).

*Proof.* Take $N_0 = A + 2$ and $N \ge N_0$. We use reduction theory in Siegel sets. For $M, T > 0$ the *Siegel set* $\mathfrak{S}_{M,T}$ is the set of $x = p\, a_s\, k$ in $S_\infty$, where $p$ is upper triangular at each place with entries bounded by $M$ and diagonal entries bounded below by $M^{-1}$, $a_s$ is the diagonal matrix $\mathrm{diag}(e^{s_1}, \dots, e^{s_N})$ at each place with $\sum_i s_i = 0$ and $s_{i+1} \le s_i + T$, and $k$ is unitary at each place. Put $W(s) = \sum_{i=1}^{N-1} |s_i - s_{i+1}|$.

1. Reduction theory: there are finitely many rational elements $c_1, \dots, c_m$ of $S_\infty$ and $M, T$ such that each $x \in S_\infty$ has a translate $\gamma x$, $\gamma \in \Lambda_N$, with $c_j^{-1} \gamma x \in \mathfrak{S}_{M,T}$ for some $j$. This is the theorem of Borel and Harish-Chandra for $\mathrm{SL}_N$ over $L$, deduced here from the reduction of the group $\Gamma_N$.
2. Height on Siegel sets: for each rational $c$ there is $C$ with $\mathrm{ht}(c\, p\, a_s\, k) \le C e^{2 W(s)}$.
3. Integrability: in the coordinates $p\, a_s\, k$ the Haar measure has density bounded by a decreasing exponential in the gaps $s_i - s_{i+1}$. So a function bounded by $C e^{B W(s)}$ on $\mathfrak{S}_{M,T}$ is integrable there when $B < 2(N - 1)$.

Since $\Lambda_N$ is discrete and countable, there is a measurable fundamental domain $D$ contained in the union of the sets $c_j \mathfrak{S}_{M,T}$, and it has finite measure by item 3 with $B = 0$. On $c_j \mathfrak{S}_{M,T}$ we have $\mathrm{ht}^A \le C^A e^{2A W(s)}$, and $2A \le 2(N - 2) < 2(N - 1)$. Item 3 gives integrability. $\square$

### The spectral gap

Let $\pi$ be a prime element of $\mathcal{O}_L$ and $q_\pi = \mathrm{diag}(\pi, 1, \dots, 1)$ as in the [previous section](/entry/s-hecke/). The Hecke operator $T_{q_\pi}$ acts on functions on $G_\infty$ by
$$(T f)(x) = \frac{1}{[\Gamma_N : \Gamma_{N,q_\pi}]} \sum_{c} f\big(\sigma(q_\pi c)\, x\big),$$
where $c$ runs over $\Gamma_{N,q_\pi} \backslash \Gamma_N$ and $\sigma$ is the embedding of $\mathrm{GL}_N(L)$ in $G_\infty$.

**Theorem 7.4.5 (Spectral gap).** Let $L$ be totally complex, $\pi$ a prime element of $\mathcal{O}_L$ with $N(\pi) \ge 25$, and $N \ge 3$. Let $(\mu, D)$ be a fundamental domain datum for $\Lambda_N$. Let $f \colon G_\infty \to \mathbb{R}$ be continuous, invariant under $\Gamma_N$ on the left and under left multiplication by scalar matrices $(s_w 1_N)_w$, with $f|_{S_\infty}$ square integrable on $D$ and $\int_D f \, d\mu = 0$. Then $T f$ has the same properties, and
$$\int_D (T f)^2 \, d\mu \le \left(\tfrac{3}{5}\right)^2 \int_D f^2 \, d\mu.$$

Lean: `PositivityTheory.KB.sGap_of`.

*Proof.* For $r = 0, 1, 2$ let $K_r$ be the subgroup of $\mathrm{SL}_N(L)$ of elements $g$ with $d_r g d_r^{-1} \in \mathrm{SL}_N(\mathcal{O}_L)$, where $d_r$ is diagonal with $r$ entries $\pi$ and $N - r$ entries $1$. So $K_0 = \mathrm{SL}_N(\mathcal{O}_L)$, and $K_1, K_2$ are conjugates of it. On functions on $S_\infty$, the Hecke operator is the averaging operator over $(K_0 \cap K_1) \backslash K_0$ applied to the $K_1$-invariant function $x \mapsto f(\sigma(q_\pi) x)$.

1. Arithmetic. Since $N(\pi) \ge 25$ and $N \ge 3$, the triple $K_0, K_1, K_2$ has finite index intersections, each $K_i$ acts doubly transitively on the cosets of the relevant pairwise intersection, and these indices are at least $25$. This is a computation in $\mathrm{SL}_N$ over the residue field $\mathcal{O}_L / \pi$.
2. Angles. Let $V_i$ be the space of $K_i$-invariant functions in $L^2$. Double transitivity and index at least $25$ give that $V_i$ and $V_j$, orthogonally to $V_i \cap V_j$, have angle cosine at most $1/\sqrt{25} = 1/5$. A lemma on three closed subspaces with pairwise angle bounds $1/5$ then gives the bound $2/5$ for the projection that the Hecke operator realizes.
3. Density. The group generated by $K_0$ and $K_1$ is dense in $S_\infty$, by strong approximation for $\mathrm{SL}_N$. So a function invariant under both is almost everywhere constant, and mean zero removes the constants.
4. Unfolding. Averaging over cosets matches integrals over fundamental domains: a fundamental domain for a subgroup of index $m$ has $m$ times the measure.

Together these give the bound with the constant $(2/5)^2$, which implies the stated bound with $(3/5)^2$. Invariance and continuity of $T f$ follow from the coset description. $\square$

The [Hecke vanishing theorem](/entry/s-hecke/) needs only the weaker rate $3/5$.

### Localization

**Theorem 7.4.6 (Localization).** Let $L$ be a number field, $N \ge 1$, $k \ge 0$, $(\mu, D)$ a fundamental domain datum for $\Lambda_N$, and $z$ a real cycle of degree $k + 1$ of $\Gamma_N$. There is $C$ such that for each good $(k+1)$-form $\omega$, invariant under $\Gamma_N$ and under all scalars, with $\|\mathrm{fr}_\omega\|^2$ integrable on $D$,
$$\big| \mathrm{ev}(I_\omega, 1, z) \big| \le C \left( \int_D \|\mathrm{fr}_\omega(x)\|^2 \, d\mu(x) \right)^{1/2}.$$

Lean: `PositivityTheory.KB.sLoc` (also `PositivityTheory.KB.sLoc_of`, the same statement with the bar complex facts as a hypothesis).

*Proof.* Fix a closed ball $B$ in $\mathcal{P}$ around $1$. By part 2 of the [bar complex proposition](/entry/s-aff/), the evaluation of the invariant cocycle $I_\omega$ on the cycle $z$ does not depend on the base point. So we may average it over base points in $B$, and also replace each vertex by a random point of a translate of $B$. This writes the evaluation as an average of integrals of $\omega$ over simplices with vertices in finitely many compact sets, since $z$ is a finite sum. Each such integral is bounded by the $L^1$ norm of $\omega$ over a compact set $K \subset \mathcal{P}$, the union of the simplices. Unfolding along $S_\infty \to \mathcal{P}$ bounds this by the $L^1$ norm of the frame over a compact set $K' \subset S_\infty$; here scalar invariance is used, since $S_\infty$ does not see the scalars. Since $\Lambda_N$ is discrete, $K'$ meets only finitely many of its translates of $D$, so the $L^1$ norm over $K'$ is at most a fixed multiple of the $L^1$ norm over $D$. The Cauchy-Schwarz inequality on $D$, of finite measure, gives the $L^2$ bound. $\square$

**Remark 7.4.7 (Formalization).** The basic properties of the height are a separate result, used as a hypothesis of `sPU_of` and `sMom_of`. The proofs of the partition of unity and of the localization bound are assembled from the statements of the folders `PartitionUnitySmooth` and `CompactLocalSets`; we have read those statements, not all their proofs, and the description of the retraction follows them. The moment bound takes $N_0 = A + 2$ in [SetLIntegralPreimageMulLeft.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/MomentEntryBounds/SetLIntegralPreimageMulLeft.lean#L70). The spectral gap is proved with the constant $(2/5)^2$ in the abstract step `GapAbs`, but the statement `SGap` only records $(3/5)^2$. The double transitivity in item 1 of the gap proof is the statement `Arith`, which we have not unfolded. The name `TwSMInt2` of the namespace of `sMom_of` carries no meaning.
