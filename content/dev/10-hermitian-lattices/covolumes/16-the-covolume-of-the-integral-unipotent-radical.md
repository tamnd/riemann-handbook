---
title: The covolume of the integral unipotent radical
decls:
  - GlobalTheory.T.covolume_integral_unipotentRadical_real_points
  - GlobalTheory.SnMass.VolN.covolume_N
  - GlobalTheory.T.transportedFundDomain_volume_classical
  - GlobalTheory.CovDom.main
  - GlobalTheory.CovNFormulaPf.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The covolume of the integral unipotent radical

The archimedean factor of a term contains the covolume of the integral points of the unipotent radical $N$ in its real points. This section computes that covolume exactly. The general theorem treats a Hermitian matrix over a CM extension, a self-dual lattice and a frame: every fundamental domain of the integral unipotent group has the same Haar measure, and this measure is an explicit power of the discriminant of $F$ times a product of powers of the scales of the frame. We then specialize to the concrete frames of the setting and obtain the covolume formula $\operatorname{cov}_N = (\theta (2v)^{r^2 + r/2})^{f}$, which is used in the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

**Definition 2.16.1 (Real unipotent radical and its Haar measure).** Let $k, r \ge 0$ and $n = 2r + k + 1$, and let $H_{k,r}$ be the model Hermitian form on $\mathbb{C}^n$ with its unitary group $U(H_{k,r})$. Index the basis so that the flag vectors are $e_{I(0)}, \dots, e_{I(r-1)}$. The *real unipotent radical* $N_{k,r}$ is the set of $g \in U(H_{k,r})$ such that, for every $a < r$, the column $g e_{I(a)}$ agrees with $e_{I(a)}$ in the rows $i \ge a$, and $g$ is the identity on the middle block of indices $r \le j \le r + k$ in the rows $i \ge r$. Let $\mathfrak{n}$ be the real span of its Lie algebra, with Lebesgue measure for a fixed Euclidean structure. For $\kappa \in [0, \infty]$ put
$$\mu_\kappa = \kappa \cdot \exp_* (\mathrm{Leb}_{\mathfrak{n}}),$$
the image of Lebesgue measure under the exponential map, times $\kappa$. This is a Haar measure on $N_{k,r}$.

**Definition 2.16.2 (Fundamental domain of the integral unipotent group).** Let $E/F$ be a CM extension with complex conjugation $\sigma$. Let $J \in M_n(E)$ be Hermitian, $\Lambda$ an $\mathcal{O}_E$-lattice in $E^n$, and $P \in M_{n \times (r+1)}(E)$ a frame. For each infinite place $w$ of $E$ let $A_w \in M_n(\mathbb{C})$. A set $\mathcal{D}$ of families $(x_w)_w$ of complex $n \times n$ matrices is a *fundamental domain* for $(J, \Lambda, P, A)$ if $\mathcal{D}$ is measurable and, for every family $x$ with $x_w \in N_{k,r}$ for all $w$, there is exactly one $\gamma \in M_n(E)$ such that $\gamma$ lies in the unipotent radical of the frame $P$, $\gamma \Lambda = \Lambda$, and
$$\big(A_w\, \gamma^{w} A_w^{-1}\, x_w\big)_w \in \mathcal{D}.$$
Here $\gamma^w$ is the image of $\gamma$ under the embedding at $w$.

The matrices $A_w$ move the frame of $J$ at $w$ to the model frame, so $A_w \gamma^w A_w^{-1}$ is the integral unipotent element written in model coordinates. A fundamental domain is a set of representatives for the left action of the integral unipotent group $\Gamma_N = \{\gamma : \gamma \Lambda = \Lambda\}$ on $\prod_w N_{k,r}$.

**Theorem 2.16.3 (Covolume of the integral unipotent radical).** Let $E/F$ be a CM extension with conjugation $\sigma$ such that $\mathcal{O}_E$ is formally unramified over $\mathcal{O}_F$. Let $J \in M_n(E)$ be Hermitian and nondegenerate, and let $\Lambda$ be a self-dual $\mathcal{O}_E$-lattice for $J$. Let $T \in F$, let $P = (p_0, \dots, p_r)$ be a frame for $J$ with parameter $T$, and let $f = (f_0, \dots, f_{r-1})$ be a dual family for $P$. Let $\mathfrak{D}$ be the inverse different of $E$. Assume that the lattice spanned by the vectors $\mathfrak{D}^{r-b} p_b$ and $\mathfrak{D}^{-(r-b)} f_b$ lies in $\Lambda$. Let $(A_w)_w$ be a model of $J$ at the infinite places, and let $s_0, \dots, s_{r-1} > 0$ with
$$A_w p_a^{w} = s_a\, e_{I(a)}, \qquad A_w f_a^{w} = s_a^{-1}\, e'_{I(a)}$$
for every infinite place $w$ and $a < r$, where $e'_{I(a)}$ is the dual model vector. Then a fundamental domain $\mathcal{D}$ exists, and every fundamental domain satisfies
$$\begin{aligned} \Big(\prod_w \mu_1\Big)(\mathcal{D}) = {}& |d_F|^{-(k+1) r^2 - \frac{4(r^3 - r)}{3} - \frac{3r}{2}} \\ & \times \Big(\prod_{a < r} s_a^{4(r-a) + 2k}\Big)^{\#\{w\}}, \end{aligned}$$
where $w$ runs over the infinite places of $E$.

Lean: `GlobalTheory.SnMass.VolN.covolume_N` (also `GlobalTheory.T.covolume_integral_unipotentRadical_real_points`, a second name).

*Proof.* The integral unipotent elements $\gamma$ with $\gamma \Lambda = \Lambda$ form a group $\Gamma_N$, and $\gamma \mapsto (A_w \gamma^w A_w^{-1})_w$ is a faithful action of $\Gamma_N$ on $\prod_w N_{k,r}$ by left multiplication. Write an element of $N_{k,r}$ in coordinates adapted to the flag. The coordinates fall into four kinds of blocks: the entries above the diagonal between two flag vectors $a < b$, the entries between a flag vector and the middle space, the entries between a flag vector $a$ and a dual vector $b$, and the skew-Hermitian diagonal entries. Order the coordinates by depth in the flag. An element of depth at least $d$ acts on the coordinates of depth $d$ by translation, and on the deeper coordinates by a polynomial map. For each block, the integral elements form a lattice:

1. the ideal lattice $\mathfrak{D}^{r-a} \mathfrak{D}^{-(r-b)}$, scaled by $s_a / s_b$, for the upper entries;
2. a lattice of homomorphisms from the middle part of $\Lambda$ into the ideal $\mathfrak{D}^{r-a}$, scaled by $s_a$, for the middle entries;
3. the ideal lattice $\mathfrak{D}^{r-a} \mathfrak{D}^{r-b}$, scaled by $s_a s_b$, for the entries between flag and dual vectors;
4. a lattice of skew elements of $\mathfrak{D}^{2(r-a)}$, scaled by $s_a^2$, for the diagonal entries.

The covolume of each block lattice is computed from the discriminant and the different; since $E/F$ is unramified at all finite places, these are expressed through $|d_F|$. A layered fundamental domain theorem, for a group that acts by translations on successive layers of coordinates, gives a fundamental domain built as a product of fundamental domains of the block lattices, and shows that every fundamental domain has the measure of this product. Multiplying the covolumes of the blocks over all pairs $a < b$, all $a$ and all infinite places gives the exponent of $|d_F|$ and the powers of the $s_a$. $\square$

### The concrete frames

In the setting of the double coset sum, the frames are concrete. Let $v = \tfrac12 |d_E|^{1/[E:\mathbb{Q}]}$, so that $2v$ is the root discriminant of $E$; then $2v \ge 1$. Let $\mathcal{T}$ be the finite set of archimedean indices of the setting, and put $f = \#\mathcal{T}$. For a word $u$ let $\mathcal{F}_N(u)$ be the fundamental domain of the integral unipotent group of the setting, and let $\operatorname{tr}$ be the transport at the infinite places: the map that writes a family of real points in the model coordinates of each index in $\mathcal{T}$.

**Theorem 2.16.4 (The transported fundamental domain).** In the setting of the double coset sum, let $\theta \in \mathbb{R}$, let $C$ be a choice of transport matrices for $\theta$, and let $u$ be a word. Then
$$\Big(\prod_{\tau \in \mathcal{T}} \mu_1\Big)\big(\operatorname{tr}(\mathcal{F}_N(u))\big) = (2v)^{(r^2 + r k + r/2)\, f}.$$

Lean: `GlobalTheory.CovDom.main` (also `GlobalTheory.T.transportedFundDomain_volume_classical`, a second name).

*Proof.* The concrete Gram matrix of the setting is Hermitian and nondegenerate, and its lattice is self-dual. The word frame and its dual tuple satisfy the integrality condition of the [Theorem 2.16.3](/entry/covolume-n/) above, and the transport matrices give a model of $J$ that is adapted to the frame with explicit scales $s_a$. The extension is CM and unramified. The transported set $\operatorname{tr}(\mathcal{F}_N(u))$ is a fundamental domain: it is measurable, the transport is a bijective multiplicative map on real points, and the integral unipotent group of the setting is the integral unipotent group of the lattice in these coordinates. So the [Theorem 2.16.3](/entry/covolume-n/) applies, and the measure of the domain is its right-hand side. The image of the measure under the map from the places of $E$ to the indices in $\mathcal{T}$ is the product measure on $\mathcal{T}$. Finally, the normalizing constants of the setting are chosen so that the right-hand side equals $(2v)^{(r^2 + rk + r/2) f}$. $\square$

**Definition 2.16.5 (Normalized unipotent covolume).** For $\theta \in \mathbb{R}$ let
$$\mu_N^\theta = \mu_{\kappa(\theta)}, \qquad \kappa(\theta) = \max\big(0, (2v)^{-rk}\, \theta\big).$$
The *normalized covolume* of the unipotent radical for $(C, u)$ is
$$\operatorname{cov}_N(C, u) = \Big(\prod_{\tau \in \mathcal{T}} \mu_N^\theta\Big)\big(\operatorname{tr}(\mathcal{F}_N(u))\big),$$
as a real number.

The factor $(2v)^{-rk}$ in the normalization removes the dependence on $k$ in the last theorem.

**Corollary 2.16.6 (Covolume formula).** For every $\theta > 0$, every choice $C$ for $\theta$ and every word $u$,
$$\operatorname{cov}_N(C, u) = \big(\theta\, (2v)^{r^2 + r/2}\big)^{f}.$$

Lean: `GlobalTheory.CovNFormulaPf.main`.

*Proof.* Put $t = (2v)^{-rk} \theta \ge 0$. Then $\mu_N^\theta = t\, \mu_1$, and a product of $f$ copies of $t \mu_1$ is $t^f$ times the product of the $\mu_1$. By the [Theorem 2.16.4](/entry/cov-dom-main/) on the transported domain,
$$\operatorname{cov}_N(C, u) = t^f\, (2v)^{(r^2 + rk + r/2) f} = \big(\theta\, (2v)^{r^2 + r/2}\big)^f. \qquad \square$$

**Remark 2.16.7 (Formalization).** The transported domain theorem holds for every real $\theta$, and its right-hand side does not depend on $\theta$, $C$ or $u$; the word "classical" in its second name is only a label ([TransportedFundDomainVolumeClassical.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TransportedFundDomainVolumeClassical.lean#L89)). The fundamental domain predicate `IsDomN` does not ask that $\mathcal{D}$ lie in $\prod_w N_{k,r}$ ([NCoords.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/NCoords.lean#L73)). The covolume theorem concludes `AllSome IsDomN (measure = ...)`: a domain exists, and every domain has the stated measure. The model condition `IsModelAt` and the frame conditions `IsFrame` and `IsDual` are not unfolded here, and the description of the four block lattices follows the names of the block covolume lemmas used in the proof. The parameter $T$ of the frame does not appear in the formula.
