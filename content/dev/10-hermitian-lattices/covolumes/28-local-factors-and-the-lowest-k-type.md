---
title: Local factors and the lowest K-type
decls:
  - GlobalTheory.T.localBesselJFactor_all_words_of_gap
  - GlobalTheory.JFactTie.jFactN_all
  - GlobalTheory.Jet.FormGapFree.formulaGap
  - GlobalTheory.DSId.LowCharGap.lowChar
  - GlobalTheory.DSId.LowCharGap.lowChar_of_formula
  - GlobalTheory.T.unitary_rep_matrixCoeff_integral_eq_zero
  - GlobalTheory.ConstTermZero.constant_term_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local factors and the lowest K-type

This section gathers four results that the step [nonempty hypotheses](/step/nonempty-hyps/) uses about the archimedean representation theory. The first splits the Hilbert-Schmidt norm of the Bessel operator of a relevant term into a covolume and a product of local factors. The other three concern a discrete series representation $\sigma$ of a unitary group $U(p, q)$ whose Harish-Chandra parameter has large gaps: an integral formula for the matrix coefficients on the lowest $K$-type, the infinitesimal character of these coefficients, and the vanishing of the constant terms of square-integrable matrix coefficients along unipotent radicals. The type bound of [Section 2.10.7](/entry/type-bound-of-gap/) and the formal degree bounds of [Section 2.18.3](/entry/oo-eq-inv-deg-smul-iint/) use the same objects.

### The local factor identity

Fix a setting with a finite pairing of terms, a choice of Bessel data $C$ at level $1$ and words $u$, $u'$, as in [Section 2.23.6](/entry/stabiliser-covolume-relevant-term-le-height-pow/). For a term $t$ over $u, u'$ let $J_t$ be its global Bessel operator, let $\mathrm{vol}(t)$ be the real covolume of $t$, defined from a pinned measure and a fundamental set of the stabilizer of a lift of $t$ (it is $1$ if $t$ is not relevant or has no lift), and let $\mathrm{cov}(u)$ be the covolume attached to the word $u$ by the choice $C$. For each real place $\tau$ the local Bessel map of $C$ gives an operator $J_\tau(t)$ at the local data of $t$; put
$$P_1(t) = \prod_\tau \|J_\tau(t)\|_{\mathrm{HS}}^2.$$

**Definition 2.28.1 (Local factor identity).** The words $u$, $u'$ satisfy the *local factor identity* if for every relevant term $t$ with nonzero Gram value,
$$\|J_t\|_{\mathrm{HS}}^2\,\mathrm{cov}(u)\,\mathrm{cov}(u') = \mathrm{vol}(t)^2\,P_1(t).$$

Lean: `GlobalTheory.Formalism.L2.SG.LoopTerm.JFactN` (also `JFactN`, the name in the file).

The identity is what turns a bound on the Bessel operators of terms into a bound on local Hilbert-Schmidt norms: two lemmas in the same file deduce from it that $J_t = 0$ exactly when $P_1(t) = 0$ (given positive covolumes and pins for all lifts), and an expression for the ratio $\mathrm{vol}(t)^2 P_1(t) / \|J_t\|^2$.

**Theorem 2.28.2 (The local factor identity under the gap hypothesis).** Assume the gap hypothesis of the concrete setting. Then the local factor identity holds for all words $u$, $u'$ and every choice of Bessel data.

Lean: `GlobalTheory.JFactTie.jFactN_all` (also `GlobalTheory.T.localBesselJFactor_all_words_of_gap`, a second name).

*Proof.* Let $t$ be relevant with nonzero Gram value. Witt's theorem on lattices lifts $t$ to a term $s$ of the full setting with $s$ over $t$; $s$ is relevant and its Gram value is nonzero because the Gram value of $t$ is its image under the injective map $F \to E$. By [Section 2.23.6](/entry/stabiliser-covolume-relevant-term-le-height-pow/) the lift has a normalized pin: a point, a pinned Haar measure $\mu_R$ on the real stabilizer and a fundamental set $K$. Unfolding the definitions, $J_t$ is the normalized amplitude of $s$ and $\mathrm{vol}(t) = \mu_R(K)$. The amplitude is invariant under the real stabilizer at each place, since a stabilizer element fixes the relative point. The normalized lift theorem then writes the amplitude as the covolume $\mu_R(K)$ times the tensor product of the local amplitudes. Each local amplitude at the Witt lift equals a quotient integral, and the amplitude constant is the product of the covolumes $\mathrm{cov}(u)\,\mathrm{cov}(u')$. Taking Hilbert-Schmidt norms, the norm of a tensor product is the product of the norms, and the identity follows. $\square$

### The lowest K-type of a discrete series

Let $n \ge 1$, let $\varepsilon : \{1, \dots, n\} \to \{\pm\}$ be a signature and $G = U(\varepsilon)$ the unitary group of $\operatorname{diag}(\varepsilon)$, with maximal compact subgroup $K$ and Cartan decomposition $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$. Let $\mathrm{rk}(\varepsilon) = \min(p, q)$ be the real rank. A vector $\lambda \in \mathbb{R}^n$ is a *Harish-Chandra parameter* if it is strictly decreasing and $\lambda_a - (n-1)/2 \in \mathbb{Z}$ for all $a$. A unitary representation $\sigma$ of $G$ on a Hilbert space $H$ is a *discrete series with parameter* $\lambda$ if it is irreducible, its matrix coefficients are square integrable, it contains the $K$-type of highest weight
$$\Lambda = \lambda + \rho_n - \rho_c,$$
and this $K$-type minimizes $\|\mu + 2\rho_c\|^2$ among the $K$-types $\mu$ of $\sigma$. Let $H_\Lambda \subseteq H$ be the span of all $K$-types of highest weight $\Lambda$. We say $\lambda$ has *gaps at least* $h$ if $|\lambda_a - \lambda_b| \ge h$ whenever $\varepsilon_a \ne \varepsilon_b$.

For $\lambda$ the function $\Phi_\lambda$ on $GL_n(\mathbb{C})$ is a product of powers of the leading principal minors,
$$\Phi_\lambda(z) = \prod_i \Delta_i(z)^{-s_i(\lambda)},$$
with exponents $s_i(\lambda)$ given by the differences of the entries of $\lambda$ along the signature; we have not unfolded the exponents beyond this.

**Theorem 2.28.3 (The compression formula on the lowest K-type).** Let $\sigma$ be a discrete series of $U(\varepsilon)$ with Harish-Chandra parameter $\lambda$ whose gaps are at least $h$, where $120\, n\, \mathrm{rk}(\varepsilon)^{3/2} \le h$. Let $w \in H_\Lambda$ be a unit vector of weight $\Lambda$. Then for every $X \in \mathfrak{p}$ and $u, v \in H_\Lambda$,
$$\langle v, \sigma(\exp X) u\rangle = \dim H_\Lambda \int_K \Phi_\lambda(k^{-1} \exp(X)\, k)\,\langle v, \sigma(k) w\rangle\,\langle \sigma(k) w, u\rangle\,dk,$$
where $dk$ is the Haar probability measure on $K$.

Lean: `GlobalTheory.Jet.FormGapFree.formulaGap` (also `FormulaGap`, the property it proves).

*Proof.* Under the gap condition the vectors of weight $\Lambda$ form a strict lowest $K$-type: there is a gap in the sense of the file, $H_\Lambda$ is a single $K$-type of highest weight $\Lambda$, and the action of $\mathfrak{p}$ followed by projection to $H_\Lambda$ is a derivation of the expected form. The $K$-type extends holomorphically to $K_\mathbb{C}$, and the function $\Phi_\lambda$ is the extension of the highest weight character to the open set where all leading minors are nonzero. The matrix coefficient $\langle v, \sigma(\exp X) u\rangle$ is analytic in $X$, and the compressed coefficient on $H_\Lambda$ is determined by its values at $1$ and by the derivation. Schur orthogonality on $K$, with the factor $\dim H_\Lambda$, rewrites the compressed coefficient as the integral over $K$. $\square$

The formula is the one of Harish-Chandra and Schmid for the lowest $K$-type of a discrete series, written as a $K$-average of the highest weight character. Here it is proved only under the large gap condition, which forces the lowest $K$-type to be strict.

**Theorem 2.28.4 (The infinitesimal character of lowest K-type coefficients).** Assume the compression formula. Let $\sigma$ be a discrete series of $U(\varepsilon)$ with Harish-Chandra parameter $\lambda$ whose gaps are at least $h$, with $120\, n\, \mathrm{rk}(\varepsilon)^{3/2} \le h$, and assume that $H_\Lambda$ is a $K$-type of highest weight $\Lambda$. Then for every $s \in H_\Lambda$ and $y \in H$ the function $f(g) = \langle y, \sigma(g) s\rangle$ is smooth and satisfies
$$\Gamma_m f = \gamma_m(\lambda)\, f \quad \text{on } G$$
for every $m \ge 0$, where $\Gamma_m$ is the $m$-th Gelfand invariant, the trace of the $(m+1)$-st power of the matrix of generators of $\mathfrak{gl}_n$, and $\gamma_m(\lambda) = \sum_{a, b} (A(\lambda + (n-1)/2)^{m+1})_{ab}$ for an explicit matrix $A$.

Lean: `GlobalTheory.DSId.LowCharGap.lowChar_of_formula`.

*Proof.* The Gelfand invariants lie in the centre of the enveloping algebra, so they act on the lowest $K$-type coefficients by scalars $c_m$: the space of functions $g \mapsto \langle y, \sigma(g) s\rangle$ with $s \in H_\Lambda$ is stable under the centre, and on it the centre acts through the irreducible $\sigma$. To compute $c_m$, take a unit vector $w$ of weight $\Lambda$ and extend the $K$-type holomorphically. The compression formula expresses the coefficients on $H_\Lambda$ by $\Phi_\lambda$, and the Gelfand invariants act on the minors $\Delta_i$ through the entries of the matrix $A$. A lemma on the eigenvalues of the centre on the coefficients of a discrete series then identifies $c_m = \gamma_m(\lambda)$. $\square$

**Theorem 2.28.5 (The infinitesimal character under large gaps).** Let $\sigma$ be a discrete series of $U(\varepsilon)$ with Harish-Chandra parameter $\lambda$ whose gaps are at least $h$, with $120\, n\, \mathrm{rk}(\varepsilon)^{3/2} \le h$. Then for every $s \in H_\Lambda$ and $y \in H$ the coefficient $g \mapsto \langle y, \sigma(g) s\rangle$ is an eigenfunction of the Gelfand invariants with the eigenvalues $\gamma_m(\lambda)$.

Lean: `GlobalTheory.DSId.LowCharGap.lowChar`.

*Proof.* Apply the previous theorem. The compression formula holds by the theorem above. The space $H_\Lambda$ is a $K$-type of highest weight $\Lambda$ by the lemma on $K$-types under large gaps, whose hypothesis $|\lambda_a - \lambda_b| > 2n$ for $\varepsilon_a \ne \varepsilon_b$ follows from the gap condition and $h \ge 120\, n\, \mathrm{rk}(\varepsilon)^{3/2}$. $\square$

### Constant terms of square-integrable coefficients

Let $W \subseteq \mathbb{C}^n$ be a nonzero subspace that is isotropic for $\operatorname{diag}(\varepsilon)$, and let $N_W$ be the unipotent radical of its stabilizer in $G$. For $g \in G$ let $d(g)$ be the logarithm of the operator norm of $g$, the distance to $K$ in the operator norm metric.

**Theorem 2.28.6 (Constant terms of matrix coefficients vanish).** Let $\nu$ be a Haar measure on $N_W$. Let $\sigma$ be a unitary representation of $G$ on a complete space $H$ with formal degree $d > 0$, that is,
$$\int_G \langle v, \sigma(g) w\rangle\,\overline{\langle v', \sigma(g) w'\rangle}\,dg = \frac{\langle v', v\rangle\,\langle w, w'\rangle}{d}$$
for all $v, w, v', w'$. Let $c > 12\, n\, \mathrm{rk}(\varepsilon)$, let $w$ be a unit vector, and let $\alpha$ be a smooth function of compact support on $G$ with
$$\int_G \alpha(g)\,\langle u, \sigma(g) w\rangle\,dg = \langle u, w\rangle \quad \text{for all } u \in H.$$
Assume that $|\langle w, \sigma(g) w\rangle| \le C e^{-c\, d(g)}$ for some $C$. Then for all $x, y \in G$,
$$\int_{N_W} \langle w, \sigma(x m y) w\rangle\,d\nu(m) = 0.$$

Lean: `GlobalTheory.ConstTermZero.constant_term_zero` (also `GlobalTheory.T.unitary_rep_matrixCoeff_integral_eq_zero`, a second name).

*Proof.* First $n \ge 1$, since an isotropic subspace in dimension $0$ is zero. Choose a measurable cutoff $\beta \ge 0$ on $G$ with $\int_{N_W} \beta(m^{-1} y)\,d\nu(m) = 1$ for every $y$. Let $a(s) = \exp(s H)$ be the one-parameter split torus of an Iwasawa decomposition adapted to $W$; conjugation by $a(s)$ scales $\nu$ by $e^{\kappa s}$ for a modulus $\kappa$ with $|\kappa| \le 8\, n\, \mathrm{rk}(\varepsilon)$, and $d(m\,a(s)) \ge |s|$ for $m \in N_W$. Let $V$ be the span of the orbit $\sigma(G) w$. The reproducing property of $\alpha$ makes the coefficients of $w$ differentiable along the orbit, and the decay bound passes from $w$ to all pairs of vectors of $V$. For $v \in V$ the formal degree gives the norm identity
$$\int_G \beta(g)\,\Bigl|\int_{N_W} \langle v, \sigma(m g) w\rangle\,d\nu(m)\Bigr|^2\,dg = \frac{\|w\|^2}{d} \int_{N_W} \langle v, \sigma(m) v\rangle\,d\nu(m).$$
A flow argument along $a(s)$, using the modulus, the conjugation bound for $a(s) m a(s)^{-1}$ and the decay with $c > 12\, n\, \mathrm{rk}(\varepsilon)$, shows that the right side vanishes for every $v \in V$. Take $v = \sigma(x^{-1}) w$ and $F(g) = \int_{N_W} \langle v, \sigma(m g) w\rangle\,d\nu(m)$. Then $F$ is continuous and left invariant under $N_W$, and $\beta |F|^2 = 0$ almost everywhere. Since the fibre integrals of $\beta$ are $1$, $F$ vanishes everywhere. At $g = y$ this is the claim, since $\langle \sigma(x^{-1}) w, \sigma(m y) w\rangle = \langle w, \sigma(x m y) w\rangle$. $\square$

This is Harish-Chandra's theorem that the matrix coefficients of a discrete series are cusp forms on $G$, in the special case of a unitary group and a coefficient with explicit exponential decay.

**Remark 2.28.7 (Formalization).** The local factor identity `JFactN` is in [LoopTerm.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LoopTerm.lean#L805); $P_1$ is `P1` at line 122, the local factors are `j1` at line 119, and the covolumes are `volRC` and `covR` at lines 107 and 104. The proof of `jFactN_all` is in [LocalBesselJFactorAllWordsOfGap.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LocalBesselJFactorAllWordsOfGap.lean#L18); its main steps are `liftOntoC_of`, `relevantLift_normalisedData_exist`, `normalisedLift_amplitude_eq_covolume_mul_local`, `localAmplitude_wittLift_eq_quotientIntegral` and `amplitudeConstant_eq_prod_covolumes`, and the description above is our reading of them. The gap hypothesis `GapHyp` of the concrete setting is not unfolded. The property `FormulaGap` is in [EigenfunctionFiniteCoefficients.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/EigenfunctionFiniteCoefficients.lean#L50) and its proof in [LowestKTypeCompressionFormulaOfStrictLowestKType.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LowestKTypeCompressionFormulaOfStrictLowestKType.lean#L22); the lemmas used are `exists_gap`, `isKTypeOf_lowKSub`, `exists_isDer_lowKSub`, `lowK_analytic` and `tauExists`, and the proof sketch is a summary of them. The Harish-Chandra parameter `IsHCParam` and `GapAtLeast` are in [StatementDS.lean](lean:Formalism/FormalDegreeBessel/StatementDS.lean#L16); `GapAtLeast` contains only the gap inequality, and the bound $120 n \mathrm{rk}^{3/2} \le h$ is a separate hypothesis. The discrete series `IsDS`, the space `lowKSub` and `IsHighestUnit` are in [UpqRep.lean](lean:Formalism/PeriodIntegrals/UpqRep.lean#L307); `lowKSub` is the supremum of all $K$-types of highest weight $\Lambda$, so it is an isotypic component, and the statement that it is a single $K$-type is a separate hypothesis `IsKTypeOf` of `lowChar_of_formula`. The function $\Phi_\lambda$ and the eigenvalues `gelfVal` are in [PosPartUnitaryMul.lean](lean:Formalism/PeriodIntegrals/PosPartUnitaryMul.lean#L25). In [LowestKTypeInfinitesimalCharLargeGap.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LowestKTypeInfinitesimalCharLargeGap.lean#L170) the theorem `lowChar_of_formula` takes `FormulaGap` as a hypothesis, and `lowChar` at line 217 discharges it with `lowestKType_compressionFormula_of_strictLowestKType` and the $K$-type hypothesis with `lowestKType_isKType_of_large_gaps` through `two_mul_lt_gap`. The theorem `constant_term_zero` is in [UnitaryRepFormalDegreeBound.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnitaryRepFormalDegreeBound.lean#L385); its last steps are `form_zero` at line 264 and `eq_zero_of_cutoff` at line 32. The formal degree `IsFdeg` is at line 272 of [UpqRep.lean](lean:Formalism/PeriodIntegrals/UpqRep.lean#L272). The hypotheses `IsIsoC` and `IsHaarSub` are not unfolded here.
