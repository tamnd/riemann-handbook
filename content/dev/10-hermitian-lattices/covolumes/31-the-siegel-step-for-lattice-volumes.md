---
title: The Siegel step for lattice volumes
decls:
  - GlobalTheory.FlagBase.SiegelStep.glVol_step
  - GlobalTheory.T.lineLatticeClassMean_sum_nonzero_unfold
  - GlobalTheory.FlagBase.SiegelUnfold.latMean_sum_ne_zero
  - GlobalTheory.T.lineLatticeMean_single_pair_orbit_contribution
  - GlobalTheory.OrbitTerm.orbit_term
  - GlobalTheory.OrbitTerm.covol_stabilizer
  - GlobalTheory.GLm.mirClass_diag1_eq_sum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Siegel step for lattice volumes

This section computes the volume of the space of $\mathcal{O}_E$-lattices of rank $j$ over a totally complex field $E$ by induction on $j$, with Siegel's mean value method. Each step multiplies the volume by a power of the discriminant and the Dedekind zeta value $\zeta_E(j)$. The main result is used by the step [every character](/step/every-character/). The proof unfolds the mean of a lattice sum over the orbits of nonzero vectors and computes each orbit term as the covolume of the stabilizer of a line. A last subsection proves a restriction formula for mirabolic class functions on $GL_n(\mathbb{F}_g)$, which the same step uses; it is unrelated to the volume computation.

### Lattices at the infinite places

Let $E$ be a totally complex number field with $f$ complex places $w$ and discriminant $d_E$, and put $v_E = |d_E|^{1/(2f)}/2$. For $j \ge 1$ let $V_j = \prod_w \mathbb{C}^j$ with Lebesgue measure, and $M_j = \prod_w M_j(\mathbb{C})$. For $g \in M_j$ put $N(g) = \prod_w |\det g_w|^2$ and let $\mu_j$ be the measure $N(g)^{-j}\,dg$ on $M_j$, a Haar measure on the set where $N(g) > 0$.

**Definition 2.31.1 (Automorphisms, covolumes and the lattice volume).** For an $\mathcal{O}_E$-lattice $\Lambda \subset E^j$ let $\operatorname{Aut}(\Lambda) \subset M_j$ be the image of $\{\gamma \in GL_j(E) : \gamma \Lambda = \Lambda\}$ under the places. For $\Gamma \subseteq M_j$, a measure $\mu$ and a set $A$, the *covolume* $\operatorname{covol}_\mu(\Gamma, A)$ is the infimum of $\mu(D)$ over the measurable sets $D$ such that every $x \in A$ has some $\gamma x \in D$ with $\gamma \in \Gamma$. The *slab volume* of $\Lambda$ is $\operatorname{covol}_{\mu_j}(\operatorname{Aut}(\Lambda), \{1 \le N(g) < e\})$, and the *lattice volume* is
$$\operatorname{vol}_j(E) = \sum_{[\Lambda]} \operatorname{covol}_{\mu_j}\bigl(\operatorname{Aut}(\Lambda), \{g : 1 \le N(g) < e\}\bigr) \in [0, \infty],$$
the sum over the classes of lattices under $GL_j(E)$.

Lean: `GlobalTheory.FlagMeas.glVol` (also `GlobalTheory.FlagMeas.covol`, the covolume).

For $g \in M_j$ with $N(g) > 0$ let $L_g = g^{-1} \Lambda \subset V_j$ be the lattice of the images of $\Lambda$ at the places, moved by $g^{-1}$, and let $c(L)$ be the covolume of a lattice $L \subset V_j$. For a function $F \ge 0$ of lattices in $V_j$ the *mean* of $F$ is
$$\mathcal{M}_j(F) = \sum_{[\Lambda]} \operatorname{covol}_{F(L_g)\,\mu_j}\bigl(\operatorname{Aut}(\Lambda), \{g : N(g) > 0\}\bigr).$$

Lean: `GlobalTheory.FlagBase.latMean` (also `GlobalTheory.FlagBase.latAt`, the lattice $L_g$).

### The orbit terms

Fix $k \ge 1$. For a nonzero ideal $\mathfrak{a}$ of $\mathcal{O}_E$ and a lattice $\Lambda' \subset E^k$ let
$$L(\mathfrak{a}, \Lambda') = \{y \in E^{k+1} : \mathfrak{a}\, y_0 \subseteq \mathcal{O}_E,\ (y_1, \dots, y_k) \in \Lambda'\} = \mathfrak{a}^{-1} \oplus \Lambda'.$$
Let $\Gamma_0(\Lambda)$ be the set of $x \in \operatorname{Aut}(\Lambda)$ whose first column is the first basis vector $e_0$, the stabilizer of $e_0$.

**Theorem 2.31.2 (The covolume of the stabilizer of a line).** Let $\Lambda = \Lambda_0 \oplus \Lambda'$ with $\Lambda_0 \subset E$ and $\Lambda' \subset E^k$ lattices, $k \ge 1$. Let $\phi \ge 0$ be a measurable function on $(0, \infty)$ and $\Phi \ge 0$ a measurable function on $V_{k+1}$. Then
$$\operatorname{covol}_{\nu}\bigl(\Gamma_0(\Lambda), \{N > 0\}\bigr) = \int_{V_{k+1}} \Phi \cdot c(\Lambda_0)^k\, \frac{v_E^{fk}}{c(\Lambda')} \cdot \operatorname{slab}(\Lambda') \int_0^\infty \phi(t)\,dt,$$
where $\nu$ is the measure $\phi(N(g))\,\Phi(g^{-1} e_0)\,d\mu_{k+1}(g)$.

Lean: `GlobalTheory.OrbitTerm.covol_stabilizer`.

*Proof.* There are measurable coordinates $g \mapsto (h(g), T(g)) \in M_k \times V_k$ on $\{N > 0\}$ with $N(h(g)) = N(g)$, adapted to the first column of $g^{-1}$: for $\gamma = \begin{pmatrix} 1 & \tau \\ 0 & \beta \end{pmatrix}$ in the stabilizer of $e_0$,
$$h(\gamma g) = \beta\, h(g), \qquad T(\gamma g)\,\beta = T(g) + \tau,$$
and the integration formula
$$\int F(h(g))\,Q(T(g))\,\Phi(g^{-1} e_0)\,d\mu_{k+1}(g) = \int \Phi \cdot \int Q \cdot \int F(h)\,N(h)\,d\mu_k(h)$$
holds. An element $\gamma$ of $\Gamma_0(\Lambda)$ has $\beta \in \operatorname{Aut}(\Lambda')$ and $\tau$ in the rows lattice $\{\tau : \tau \cdot y \in \Lambda_0 \text{ for } y \in \Lambda'\}$, and conversely. Take a fundamental domain $D'$ for $\operatorname{Aut}(\Lambda')$ on $\{N > 0\}$ with
$$\int_{D'} F(N(h))\,d\mu_k(h) = \operatorname{slab}(\Lambda') \int_0^\infty F(t)\,\frac{dt}{t},$$
and a fundamental domain $P$ for the rows lattice in $V_k$, of volume $c(\Lambda_0)^k v_E^{fk} / c(\Lambda')$. The set $D = \{g : h(g) \in D',\ T(g) \in P\}$ meets every orbit of $\Gamma_0(\Lambda)$, and $D \cap \gamma D$ is a null set for $\gamma \ne 1$. So the covolume is $\nu(D)$, and the integration formula gives the product, with $\int_0^\infty \phi(t)\,t\,dt/t$. $\square$

**Theorem 2.31.3 (One orbit term).** Let $k \ge 1$, $\mathfrak{a} \ne 0$ an ideal and $\Lambda' \subset E^k$ a lattice, and let $w \ge 0$ and $\Phi \ge 0$ be measurable. Then
$$\operatorname{covol}_{\nu}\bigl(\Gamma_0(L(\mathfrak{a}, \Lambda')), \{N > 0\}\bigr) = \operatorname{slab}(\Lambda')\, \frac{v_E^{f(2k+1)}}{N(\mathfrak{a})^{k+1}} \int_{V_{k+1}} \Phi \int_0^\infty w(t)\,\frac{dt}{t^2},$$
where $\nu$ is the measure $w(c(L_g))\,\Phi(g^{-1} e_0)\,d\mu_{k+1}(g)$ built from $L(\mathfrak{a}, \Lambda')$.

Lean: `GlobalTheory.OrbitTerm.orbit_term` (also `GlobalTheory.T.lineLatticeMean_single_pair_orbit_contribution`, a second name).

*Proof.* The lattice $\Lambda_0 = \mathfrak{a}^{-1}$ in $E$ has covolume $c(\Lambda_0) = v_E^f / N(\mathfrak{a})$ at the places, and $L(\mathfrak{a}, \Lambda') = \Lambda_0 \oplus \Lambda'$. The covolume of $L_g$ is $c(L_g) = \kappa / N(g)$ with $\kappa = c(\Lambda_0)\,c(\Lambda')$. Apply the previous theorem with $\phi(t) = w(\kappa/t)$. The substitution $s = \kappa / t$ gives $\int_0^\infty w(\kappa/t)\,dt = \kappa \int_0^\infty w(s)\,ds/s^2$, and
$$c(\Lambda_0)^k\,\frac{v_E^{fk}}{c(\Lambda')}\,\kappa = c(\Lambda_0)^{k+1}\,v_E^{fk} = \frac{v_E^{f(2k+1)}}{N(\mathfrak{a})^{k+1}}. \qquad \square$$

**Theorem 2.31.4 (Unfolding the mean of a lattice sum).** Let $j \ge 2$ and let $w \ge 0$ on $(0, \infty)$ and $\Phi \ge 0$ on $V_j$ be measurable. Then
$$\mathcal{M}_j\Bigl(w(c(L)) \sum_{x \in L \setminus 0} \Phi(x)\Bigr) = \operatorname{vol}_{j-1}(E)\, v_E^{f(2j-1)}\,\zeta_E(j) \int_{V_j} \Phi \int_0^\infty w(t)\,\frac{dt}{t^2}.$$

Lean: `GlobalTheory.FlagBase.SiegelUnfold.latMean_sum_ne_zero` (also `GlobalTheory.T.lineLatticeClassMean_sum_nonzero_unfold`, a second name).

*Proof.* Write $j = k + 1$. The nonzero vectors of a lattice fall into orbits under its automorphisms, and each orbit is represented by $e_0$ in a lattice of the form $L(\mathfrak{a}, \Lambda')$. An unfolding lemma turns the mean into
$$\sum_{\mathfrak{a} \ne 0} \sum_{[\Lambda']} \operatorname{covol}_{\nu}\bigl(\Gamma_0(L(\mathfrak{a}, \Lambda')), \{N > 0\}\bigr),$$
the inner sum over the classes of lattices $\Lambda' \subset E^k$. By the previous theorem each term is $\operatorname{slab}(\Lambda')\, v_E^{f(2k+1)} N(\mathfrak{a})^{-(k+1)} \int \Phi \int w(t)\,dt/t^2$. The sum of $\operatorname{slab}(\Lambda')$ over the classes is $\operatorname{vol}_k(E)$ by definition. The sum of $N(\mathfrak{a})^{-j}$ over the nonzero ideals is $\zeta_E(j)$: the Dirichlet series with coefficients the number of ideals of norm $m$ converges for $\operatorname{Re} s > 1$, since the number of ideals of norm at most $x$ is $O(x)$, and its value at $j$ is $\zeta_E(j)$. $\square$

### The Siegel step

**Theorem 2.31.5 (The Siegel step for lattice volumes).** Let $j \ge 2$ and suppose $\operatorname{vol}_{j-1}(E) < \infty$. Then
$$\operatorname{vol}_j(E) = \operatorname{vol}_{j-1}(E)\, v_E^{f(2j-1)}\,\zeta_E(j).$$

Lean: `GlobalTheory.FlagBase.SiegelStep.glVol_step`.

*Proof.* Let $\Phi(x) = e^{-\pi \|x\|^2}$, so $\int \Phi = 1$, and put $C_j = \operatorname{vol}_{j-1}(E)\, v_E^{f(2j-1)}\,\zeta_E(j)$. For a lattice $L$ with $c = c(L)$ and dual $L^*$ for the trace form $\operatorname{Re} \sum_w x_w \cdot y_w$, put $A = \sum_{L \setminus 0} \Phi$ and $B = \sum_{L^* \setminus 0} \Phi$. Poisson summation gives $1 + A = c^{-1}(1 + B)$. Multiplying by suitable weights,
$$\mathbf{1}_{c > 1}\,(c^{-1} - c^{-2}) + \mathbf{1}_{c > 1}\, c^{-1} A = \mathbf{1}_{c^{-1} < 1}\, c^{-2} B.$$
Take the mean of both sides; the mean is additive. The mean of a function $w(c(L))$ alone is $\operatorname{vol}_j(E) \int_0^\infty w(t)\,dt/t$, so the first term has mean $\operatorname{vol}_j(E) \int_1^\infty (t^{-2} - t^{-3})\,dt = \operatorname{vol}_j(E)/2$. By the unfolding theorem the second term has mean $C_j \int_1^\infty t^{-3}\,dt = C_j/2$. Since $c(L^*) = c(L)^{-1}$, $L^{**} = L$, and the mean is invariant under $L \mapsto L^*$, the right side has mean
$$\mathcal{M}_j\Bigl(\mathbf{1}_{c < 1}\, c^2 \sum_{L \setminus 0} \Phi\Bigr) = C_j \int_0^1 t^2\,\frac{dt}{t^2} = C_j.$$
Hence $\operatorname{vol}_j(E)/2 + C_j/2 = C_j$. Since $C_j < \infty$, $\operatorname{vol}_j(E) = C_j$. $\square$

**Corollary 2.31.6 (The lattice volume).** With $\operatorname{vol}_1(E) = \operatorname{Res}_{s=1} \zeta_E(s)\, v_E^f$, induction gives
$$\operatorname{vol}_j(E) = \operatorname{Res}_{s=1} \zeta_E(s)\; v_E^{f j^2} \prod_{l=2}^{j} \zeta_E(l).$$

This is the corollary as stated in the notes of the theorem; the Lean code proves the base case and the finiteness of every $\operatorname{vol}_j$ in other declarations, which we did not read. The argument is Siegel's mean value method, in the form of Siegel (1945) for $\mathbb{Z}^n$, with the volume of $SL_n(\mathbb{R})/SL_n(\mathbb{Z})$ computed through $\zeta(2) \cdots \zeta(n)$. We know no published source for this exact normalization over a totally complex field.

### A restriction formula for mirabolic class functions

Let $g$ be a prime and $\psi$ a nontrivial additive character of $\mathbb{F}_g$. Let $G_n = GL_n(\mathbb{F}_g)$ and let $P_n \subset G_n$ be the mirabolic subgroup, the matrices whose last row is $(0, \dots, 0, 1)$. A function $F$ on $G_{k+1}$ is a *mirabolic class function* if $F(p x p^{-1}) = F(x)$ for all $p, x \in P_{k+1}$.

For $0 \le i \le n$ the *derivative* $F^{(i)}$ of a function $F$ on $G_n$ is the function on $G_i$ obtained by restricting $F$ to the parabolic of type $(i, n-i)$, averaging over its unipotent radical, and applying the Whittaker functional for $\psi$ in the $G_{n-i}$ variable. The *Gelfand-Graev character* $\Gamma_m$ of $G_m$ is the character induced from the character $u \mapsto \psi(\sum_i u_{i, i+1})$ of the upper unipotent subgroup. For functions $\alpha$ on $G_a$ and $\beta$ on $G_b$, $\alpha \circ \beta$ denotes the Harish-Chandra (parabolic) induction of $\alpha \otimes \beta$ to $G_{a+b}$.

Lean: `GlobalTheory.GLq.der` (also `GlobalTheory.GLq.gg`, the Gelfand-Graev character, and `GlobalTheory.GLq.hc`, the induction).

**Theorem 2.31.7 (Restriction of a mirabolic class function to the Levi).** Let $F$ be a mirabolic class function on $G_{k+1}$. Then for every $h \in G_k$,
$$F\begin{pmatrix} h & 0 \\ 0 & 1 \end{pmatrix} = \sum_{i=0}^{k} \bigl(F^{(i)} \circ \Gamma_{k-i}\bigr)(h).$$

Lean: `GlobalTheory.GLm.mirClass_diag1_eq_sum`.

*Proof.* The block matrix $\operatorname{diag}(h, 1)$ lies in $P_{k+1}$. A mirabolic class function is, on $P_{k+1}$, the sum over $0 \le i \le k$ of the functions induced in stages from its derivatives $F^{(i)}$, twisted by $\psi$ along the superdiagonal. Each derivative $F^{(i)}$ is a class function on $G_i$, and for a class function $\rho$ on $G_i$ the induced function at $\operatorname{diag}(h, 1)$ equals $(\rho \circ \Gamma_{k-i})(h)$. Summing over $i$ gives the formula. $\square$

The formula is the finite field form of the Bernstein-Zelevinsky filtration of the restriction of a representation of $GL_n$ to the mirabolic subgroup; see Bernstein and Zelevinsky (1977) and Zelevinsky (1981) for finite fields.

**Remark 2.31.8 (Formalization).** The definitions `glVol`, `haarGL`, `detNorm`, `autGL` and `covol` are in [DefClassNum.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DefClassNum.lean#L94), and `slabVol`, `latAt`, `latMean` and `covAt` in [IsLatMeasurableConst.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/IsLatMeasurableConst.lean#L41). The constant $v_E$ is `vInv` and $f$ is `fDeg`. The theorem `glVol_step` is in [GlNormOneAdelicQuotientVolumeSiegelStep.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/GlNormOneAdelicQuotientVolumeSiegelStep.lean#L214); its proof uses the lemma `weighted` and the integrals `lintegral_diff`, `lintegral_cube` and `lintegral_unit` of that file, and the restatements of the covolume mean and the dual mean, whose proofs we did not read. The module name speaks of an adelic norm-one quotient; the Lean object is a sum of archimedean covolumes over classes of lattices on the slab $1 \le N(g) < e$. The unfolding `latMean_sum_ne_zero` is in [LineLatticeClassMeanSumNonzeroUnfold.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LineLatticeClassMeanSumNonzeroUnfold.lean#L89); the lattice $L(\mathfrak{a}, \Lambda')$ is `sumLat`, the orbit decomposition is the restatement `lineLatticeMean_sum_eq_tsum_pair_orbits`, and the zeta sum is `tsum_absNorm_pow_inv`, proved from `hasSum_zetaE` and `lseriesSummable_idealCount`. The sum over $\mathfrak{a}$ is over all nonzero ideals, not over ideal classes, and the identity of the class sum of slab volumes with `glVol` is closed by `rfl`. In [LineLatticeMeanSinglePairOrbitContribution.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LineLatticeMeanSinglePairOrbitContribution.lean#L121) the theorem `covol_stabilizer` states its last factor as `∫⁻ t in Set.Ioi 0, f t * ENNReal.ofReal t / ENNReal.ofReal t`, which is $\int_0^\infty \phi(t)\,dt$ written with a cancelling factor; the coordinates, the rows lattice domain and the domain $D'$ are `exists_coordinates_inverseFirstColumn_infiniteGL`, `exists_fundamentalDomain_embeddedRowsLattice` and `exists_domain` (line 32). The theorem `orbit_term` is at line 241; it uses `exists_lattice_covolume_inverse_ideal` and `translatedLatticeAtInfinity_full_covolume_dual`. The mirabolic definitions `InMir`, `IsMirClass` and `diag1` are in [IsMirClass.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/IsMirClass.lean#L13), and `der`, `gg`, `hc` and `res` in [LabelDatum.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean#L45). The theorem `mirClass_diag1_eq_sum` is in [MirabolicClassFunBlockDiagonalEqSumDerivatives.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/MirabolicClassFunBlockDiagonalEqSumDerivatives.lean#L22); it applies `mirabolicConjInvariant_eq_sum_induced_derivatives`, `mirabolicInduction_blockDiag_eq_harishChandra_gelfandGraev` and `isClassFunction_bernsteinZelevinskyDerivative`, which are restatements whose proofs we did not read. The property `IsMirClass` asks for invariance only for $x$ in the mirabolic subgroup, so $F$ is unconstrained off $P_{k+1}$. The description of the derivative as a Whittaker functional of a constant term reads `der ψ m χ h = wh ψ (res m (n - m) χ h)`, where `wh` is the trace against the idempotent `eU`; we did not unfold `eU`.
