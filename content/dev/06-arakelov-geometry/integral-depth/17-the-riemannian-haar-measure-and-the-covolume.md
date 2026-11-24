---
title: The Riemannian Haar measure and the covolume
decls:
  - GlobalTheory.RiemConst.riemHaar_eq_smul
  - GlobalTheory.T.riemannianHaar_specialUnitary_eq_smul_haar
  - GlobalTheory.SUCovol.covolume_realSU
  - GlobalTheory.T.covolume_realSpecialUnitary_eq_flagDomain_mass
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Riemannian Haar measure and the covolume

The real points of a special unitary group over a CM field form a product of groups $\mathrm{SU}(p_0, r - p_0)$, one for each embedding in a CM type. On this group there are two natural measures: the Haar measure that the Riemannian metric defines, and a Haar measure that comes from the mass of a fundamental set in the flag domain. This section computes the constant between them and uses it to express the covolume of an arithmetic subgroup as a constant times the mass of a fundamental set. The result is used in [the lower bound for a sum of covolumes](/entry/sum-mu-f-le/).

**Definition 3.17.1 (Hermitian data).** Let $E$ be a CM field and $r \in \mathbb{N}$. *Hermitian data* $X$ of rank $r$ over $E$ consist of, among other fields:

1. a CM type $\Psi$: a set of embeddings $E \to \mathbb{C}$ that contains exactly one of each pair $\tau$, $\bar\tau$;
2. a hermitian matrix $G \in M_r(E)$ with $\det G \ne 0$ and an integer $p_0 \le r$ such that for each $\tau \in \Psi$ the form $h_\tau$ defined by $\tau(G)$ on $\mathbb{C}^r$ has signature $(p_0, r - p_0)$;
3. a lattice $\Lambda \subset E^r$ and a subgroup $\Gamma \subset \mathrm{GL}_r(E)$ of elements that keep $G$ and $\Lambda$, of finite index among all such elements.

We do not use the other fields here. Write $d = [E : \mathbb{Q}]/2$, so $|\Psi| = d$.

**Definition 3.17.2 (Frames and the flag chart).** A *frame* is a family $x = (x_\tau)_{\tau \in \Psi}$ of complex $r \times r$ matrices. The *Gram matrix* of $x_\tau$ is the matrix of the values of $h_\tau$ on the columns of $x_\tau$. A frame is *orthonormal* if for each $\tau$ its Gram matrix is $\mathrm{diag}(1, \dots, 1, -1, \dots, -1)$ with $p_0$ entries $1$. The *domain* $\mathcal{D}$ is the set of frames with $\det x_\tau \ne 0$ whose Gram matrices have leading principal minors $d_{\tau, i}$ with the signs of this diagonal matrix. The group $B$ is the set of frames $b$ with each $b_\tau$ invertible and upper triangular; it acts on frames on the right by $(x b)_\tau = x_\tau b_\tau$.

Fix a frame $x$. Let $V$ be the complex space with one coordinate $z_{\tau, a, b}$ for each $\tau \in \Psi$ and each pair $b < a$ in $\{1, \dots, r\}$. For $z \in V$ let $n(z)$ be the frame of lower unitriangular matrices with entries $z_{\tau, a, b}$ below the diagonal, and put $c_x(z) = x\, n(z)$. Let $\Omega_x = \{ z : c_x(z) \in \mathcal{D} \}$.

**Definition 3.17.3 (Mass on the flag chart).** The *mass* $\mu_x$ is the measure on $V$ with
$$d\mu_x(z) = \mathbf{1}_{\Omega_x}(z) \prod_{\tau \in \Psi} \prod_{i = 0}^{r - 1} |d_{\tau, i}(c_x(z))|^{-2}\, dz,$$
where $dz$ is Lebesgue measure on $V$ and $d_{\tau, i}$ is the $i$-th leading principal minor of the Gram matrix at $\tau$. A set $F \subset V$ is a *fundamental set* for $x$ if:

1. $F$ is measurable and $F \subset \Omega_x$;
2. if $z, z' \in F$, $\gamma \in \Gamma$ and $b \in B$ satisfy $c_x(z') = \gamma\, c_x(z)\, b$, then $z = z'$;
3. for $\mu_x$-almost every $z$ there are $z' \in F$, $\gamma \in \Gamma$ and $b \in B$ with $c_x(z) = \gamma\, c_x(z')\, b$.

Here $\gamma$ acts on frames on the left by $(\gamma x)_\tau = \tau(\gamma) x_\tau$. So a fundamental set picks one point of each orbit of $\Gamma \times B$ in the domain, up to a null set.

**Definition 3.17.4 (Riemannian Haar measure).** Let $\mathrm{SU}_\Psi$ be the group of families $g = (g_\tau)_{\tau \in \Psi}$ in $\mathrm{GL}_r(\mathbb{C})$ with $\det g_\tau = 1$ and $h_\tau(g_\tau u, g_\tau w) = h_\tau(u, w)$ for all $\tau$. Its Lie algebra $\mathfrak{su}_\Psi$ is the real space of families $Y_\tau$ with trace $0$ that are skew for $h_\tau$. For a frame $x$, let $\lambda_x$ be the measure on $\mathfrak{su}_\Psi$ that is the image of Lebesgue measure under $Y \mapsto (x_\tau Y_\tau x_\tau^{-1})_\tau$, where $Y$ runs over the real subspace that this map sends into $\mathfrak{su}_\Psi$ and Lebesgue measure comes from an orthonormal basis for the standard euclidean structure on the matrix entries. The *Riemannian Haar measure* $\mathrm{vol}_x$ is the multiple $c\,\mu_{\mathrm{Haar}}$ of a Haar measure, where
$$c = \limsup_{\varepsilon \to 0^+} \frac{\lambda_x(T_\varepsilon)}{\mu_{\mathrm{Haar}}(U_\varepsilon)}.$$
Here $T_\varepsilon$ is the set of families of matrices with all entries of absolute value less than $\varepsilon$, and $U_\varepsilon = \{ g : g - 1 \in T_\varepsilon \}$. So near the identity $\mathrm{vol}_x$ has density one with respect to $\lambda_x$.

**Theorem 3.17.5 (Riemannian Haar measure as a multiple).** Let $X$ be hermitian data of rank $r \ge 1$ over $E$ and $x$ an orthonormal frame. Let $\nu$ be a Haar measure on $\mathrm{SU}_\Psi$ that lies over the flag domain: for every measurable $\varphi : \{\text{frames}\} \to [0, \infty]$ with $\varphi(y b) = \varphi(y)$ for all $y \in \mathcal{D}$ and $b \in B$,
$$\int \varphi(g x)\, d\nu(g) = \int \varphi(c_x(z))\, d\mu_x(z).$$
Then
$$\mathrm{vol}_x = C_r^{\,d}\, \nu, \qquad C_r = 2^{r(r-1)/2} (2\pi)^{r-1} \sqrt r.$$

Lean: `GlobalTheory.RiemConst.riemHaar_eq_smul` (also `GlobalTheory.T.riemannianHaar_specialUnitary_eq_smul_haar`, a second name).

*Proof.* Both measures are Haar measures, so $\mathrm{vol}_x = k \nu$ for a constant $k$. We compute $k$ from the densities of both measures near the identity in one chart.

*The chart.* Put $m = (r - 1) d$ and let $N$ be the number of coordinates of $V$, so $N = d\, r(r-1)/2$. Input lemmas give:

1. a map $\sigma$ from $V$ to $\mathrm{SU}_\Psi$ with $\sigma(0) = 1$ and $\sigma(z) x \in x\, n(z) B$ near $0$;
2. a map $t$ from $\mathbb{R}^{m}$ to the diagonal torus of $\mathrm{SU}_\Psi$ in the frame $x$, with $t(0) = 1$, given by angles;
3. a real linear map $D$ that is the derivative of $(z, \theta) \mapsto \sigma(z)\, t(\theta)$ at $0$; it is injective, and its values lie in $\mathfrak{su}_\Psi$;
4. the product map covers a neighbourhood of $1$ in $\mathrm{SU}_\Psi$.

*The Riemannian side.* An input lemma on the Lie algebra says that $\lambda_x$ is $K$ times the image of Lebesgue measure under $D$, with
$$K = 2^{N} (\sqrt r)^{d}.$$
The Riemannian Haar measure has density one with respect to $\lambda_x$ at the identity.

*The flag side.* Since $\nu$ lies over the flag domain, an input formula for Haar measures in the product chart says that, near $0$, the measure $\nu$ pulled back to the chart has density
$$\frac{\prod_\tau \prod_i |d_{\tau, i}(c_x(z))|^{-2}}{(2\pi)^{m}}$$
with respect to Lebesgue measure. The density is continuous at $0$. Since $x$ is orthonormal, all leading minors of the Gram matrix of $x_\tau$ have absolute value $1$, so the density at $0$ is $a = (2\pi)^{-m}$. A lemma on charts of matrix groups then gives
$$\lim_{\varepsilon \to 0^+} \frac{\nu(U_\varepsilon)}{D_*(\mathrm{Leb})(T_\varepsilon)} = a.$$

*Comparison.* Multiply by $k$ and divide by $K$. The left side becomes $\mathrm{vol}_x(U_\varepsilon)/\lambda_x(T_\varepsilon)$, which tends to $1$. So $k a K^{-1} = 1$, and
$$k = K a^{-1} = 2^{N} (\sqrt r)^{d} (2\pi)^{(r-1) d}.$$
With $N = d\, r(r-1)/2$ this is $C_r^{\,d}$. $\square$

The constant has one factor for each embedding in $\Psi$. Each factor has a part $2^{r(r-1)/2}$ from the unipotent coordinates, a part $(2\pi)^{r-1}$ from the angles of the torus and a part $\sqrt r$ from the trace condition.

**Theorem 3.17.6 (Covolume and the mass of a fundamental set).** Let $X$ be hermitian data of rank $r \ge 1$ over $E$ such that $\det \gamma = 1$ for all $\gamma \in \Gamma$. Let $x$ be an orthonormal frame and $F$ a fundamental set for $x$. Let $\Gamma_\infty$ be the image of $\Gamma$ in $\mathrm{SU}_\Psi$ under $\gamma \mapsto (\tau(\gamma))_\tau$. Then
$$\mathrm{covol}_{\mathrm{vol}_x}(\Gamma_\infty \backslash \mathrm{SU}_\Psi) = C_r^{\,d}\, \mu_x(F).$$

Lean: `GlobalTheory.SUCovol.covolume_realSU` (also `GlobalTheory.T.covolume_realSpecialUnitary_eq_flagDomain_mass`, a second name).

*Proof.* An input lemma gives a Haar measure $\nu$ that lies over the flag domain. By the previous theorem $\mathrm{vol}_x = C_r^d \nu$, so for every measurable $B$-invariant $\varphi$ on $\mathcal{D}$,
$$\int \varphi(g x)\, d\mathrm{vol}_x(g) = C_r^{\,d} \int \varphi(c_x(z))\, d\mu_x(z).$$
Let $T = \{ c_x(z) b : z \in F, b \in B \}$, a measurable set of frames with $T B = T$, and let $\Phi = \{ g : g x \in T \}$. We show that $\Phi$ is a fundamental domain for $\Gamma_\infty$ in $\mathrm{SU}_\Psi$.

*Almost all of $\mathrm{SU}_\Psi$ is covered.* Let $S$ be the set of frames of the form $\gamma\, c_x(z')\, b$ with $\gamma \in \Gamma$, $z' \in F$ and $b \in B$. The formula with $\varphi = \mathbf{1}_{S^c}$ and part 3 of the definition of a fundamental set show that $\{ g : g x \notin S \}$ is a null set. If $g x = \gamma\, c_x(z')\, b$, then $\tau(\gamma)^{-1} g$ lies in $\Phi$. Here $\det \gamma = 1$ is used: it puts the image of $\gamma^{-1}$ in $\mathrm{SU}_\Psi$.

*The translates are disjoint.* If $\gamma_1 g_1 = \gamma_2 g_2$ with $g_1 x = c_x(z_1) b_1$ and $g_2 x = c_x(z_2) b_2$ in $T$, then $c_x(z_2) b_2 = \gamma_2^{-1}\gamma_1\, c_x(z_1) b_1$. Part 2 of the definition gives $z_1 = z_2$. Then $\gamma_2^{-1}\gamma_1$ fixes the frame $c_x(z_1)$ up to an element of $B$, and since $\Gamma$ acts freely in this sense on $\mathcal{D}$, we get $\gamma_1 = \gamma_2$.

*The measure.* By the formula with $\varphi = \mathbf{1}_T$, and since $c_x(z) \in T$ if and only if $z \in F$,
$$\mathrm{vol}_x(\Phi) = C_r^{\,d} \int \mathbf{1}_T(c_x(z))\, d\mu_x(z) = C_r^{\,d}\, \mu_x(F).$$
The covolume is the measure of a fundamental domain. $\square$

**Remark 3.17.7 (Formalization).** The Riemannian Haar measure is defined by a $\limsup$ of ratios, and an input lemma shows that it is a Haar measure with density one ([EmbGLMemRealSU.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/EmbGLMemRealSU.lean#L127)). The exponent of $C_r$ is $d = [E:\mathbb{Q}]/2$, and $|\Psi| = d$ is an input lemma ([RiemannianHaarSpecialUnitaryEqSmulHaar.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RiemannianHaarSpecialUnitaryEqSmulHaar.lean#L23)). The free action of $\Gamma$ that the disjointness uses is a field of the hermitian data. The covolume theorem does not take $\nu$ as a hypothesis; it obtains $\nu$ from an input lemma and then applies the first theorem ([CovolumeRealSpecialUnitaryEqFlagDomainMass.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CovolumeRealSpecialUnitaryEqFlagDomainMass.lean#L129)). We have not unfolded the chart maps $\sigma$ and $t$ or the product chart formula. The second names are wrappers.
