---
title: Convergence and the coefficients in the convergent range
decls:
  - GlobalTheory.CompanionTheory.SiegelND.Integ.Hua.HS.step
  - GlobalTheory.CompanionTheory.SiegelND.Integ.Hua.HS.summable_delta_rpow
  - GlobalTheory.T.summable_denominator_power_of_lt
  - GlobalTheory.CompanionTheory.SiegelND.Integ.Hua.integrable_starLoc_fin
  - GlobalTheory.T.finite_adelic_siegel_weil_integral_identity
  - GlobalTheory.CompanionTheory.SiegelND.Integ.integrable_starN
  - GlobalTheory.T.siegel_weil_convergent_range
  - GlobalTheory.CompanionTheory.WeilSiegel.NoFrame.W_eq_zero_of_obstruction
  - GlobalTheory.CompanionTheory.WeilSiegel.NoFrame.noFrame
  - GlobalTheory.T.frame_integral_eq_coefficient_nonrepresented
  - PositivityTheory.PfSWUS.SwMatch.matchMono
  - PositivityTheory.PfWsf.Top.head_of_siegel
  - PositivityTheory.PfWsf.Top.head_of_deg
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Convergence and the coefficients in the convergent range

This section supplies the remaining inputs to [the Siegel-Weil formula in the convergent range](/entry/weil-siegel-formula/). The first is a convergence statement: for $2n < M$ the Fourier integral of a Schwartz-Bruhat function against a character of the Gram matrix is integrable over the Hermitian matrices. Its finite part is a Hua type bound for a series over Hermitian matrices modulo integral ones. The second handles the coefficients $\beta$ that no frame represents, where both sides vanish. The third is the matching of the frame integral with the monomial Fock vectors used in the Schrödinger model, and the last part assembles the formula from the two cell identities of [Section 4.4.2](/entry/siegel-frame/).

### A series over Hermitian matrices

Let $E/F$ be CM and $v$ a finite place. For a Hermitian $c \in \operatorname{Herm}_n(E_v)$ let $\delta(c)$ be the index of
$$K_c = \{y \in \mathcal{O}_{E_v}^n : c y \in \mathcal{O}_{E_v}^n\}$$
in $\mathcal{O}_{E_v}^n$. It depends only on $c$ modulo $\operatorname{Herm}_n(\mathcal{O}_{E_v})$, and it is the denominator of $c$ in the sense of Siegel: it is $1$ if $c$ is integral and grows with the poles of the elementary divisors.

**Theorem 4.13.1 (Hua step).** Let $m + 1 < s$. If $\sum_c \delta(c)^{-(s-1)}$ converges over $c \in \operatorname{Herm}_m(E_v)/\operatorname{Herm}_m(\mathcal{O}_{E_v})$, then $\sum_c \delta(c)^{-s}$ converges over the matrices of size $m+1$.

Lean: `GlobalTheory.CompanionTheory.SiegelND.Integ.Hua.HS.step`.

*Proof.* Write a Hermitian matrix of size $m+1$ in blocks
$$c = \begin{pmatrix} c' & b \\ {}^t\bar{b} & d \end{pmatrix}$$
with $c'$ of size $m$. The map to $(c', b, d)$ modulo integral matrices is injective on classes (`delta_block_quotient_injection`). Bound $\delta(c)$ from below by $\delta(c')$ times the torsion contributed by $b$ and $d$ relative to $K_{c'}$ (`delta_block_series_zeta_bound`). The sum over $b$ and $d$ for fixed $c'$ is a sum over a torsion module whose terms are bounded by a local zeta factor with exponent $r = 2s - 1 - m$, which converges because $s > m + 1$ (`torsion_sum_zeta_bound_delta`). This leaves $\sum_{c'} \delta(c')^{-(s-1)}$, which converges by hypothesis. $\square$

**Corollary 4.13.2 (Hua bound).** If $n < s$ then $\sum_c \delta(c)^{-s}$ converges over $c \in \operatorname{Herm}_n(E_v)/\operatorname{Herm}_n(\mathcal{O}_{E_v})$.

Lean: `GlobalTheory.CompanionTheory.SiegelND.Integ.Hua.HS.summable_delta_rpow` (also `GlobalTheory.T.summable_denominator_power_of_lt`, a second name).

*Proof.* Induction on $n$. For $n = 0$ the sum has one term. For the step from $n - 1$ to $n$, apply the Hua step with $m = n - 1$: the hypothesis $m + 1 < s$ is $n < s$, and the sum of $\delta^{-(s-1)}$ in size $n - 1$ converges by induction since $n - 1 < s - 1$. $\square$

This is the local form of Siegel's convergence of the singular series, and of the bound Hua proved for the corresponding integrals over the Siegel domain.

### Integrability of the Fourier integral

Let $\psi$ be a nontrivial additive character of $\mathbb{A}_F/F$. For a Schwartz-Bruhat function $\Phi$ on $n$-tuples in $\mathbb{A}_E^M$ and a Hermitian $b \in \operatorname{Herm}_n(\mathbb{A}_E)$ put
$$\Phi^\star(b) = \int \Phi(X) \, \psi\Bigl(\tfrac{1}{2} \operatorname{Tr} \operatorname{tr}\bigl(b \operatorname{gr}(X)\bigr)\Bigr) \, dX.$$
The local versions $\Phi_\infty^\star$ and $\Phi_f^\star$ are defined in the same way at the archimedean places and on the finite adeles.

**Theorem 4.13.3 (Finite integrability).** Let $2n < M$, let $\psi_f$ be the finite part of $\psi$, let $\mu$ and $\nu$ be Haar measures on tuples and on $\operatorname{Herm}_n(\mathbb{A}_{E,f})$, and let $Q$ be a Schwartz-Bruhat function on finite adelic tuples. Then $\Phi_f^\star$ for $\Phi_f = Q$ is $\nu$-integrable.

Lean: `GlobalTheory.CompanionTheory.SiegelND.Integ.Hua.integrable_starLoc_fin` (also `GlobalTheory.T.finite_adelic_siegel_weil_integral_identity`, a second name).

*Proof.* $Q$ is invariant under an open subgroup, so $Q^\star$ is invariant under translation by an open subgroup of $\operatorname{Herm}_n(\mathbb{A}_{E,f})$ and has support in a compact set modulo it (`finite_adelic_integral_invariant_open_subgroup`, `scaled_integral_hermitian_in_open_subgroup`). At each place the local orbital integral is bounded by $C \delta(b_v)^{-t}$ with $t = M/2$, by counting solutions of the Gram congruence (`finite_local_orbital_integral_bounded`). Since $M/2 > n$, the Hua bound makes the product of local sums converge (`summable_periodic_bound_by_denominator`, `summable_denominator_power_of_lt`), and at almost all places the local factor is $1$ on integral $b_v$. A locally constant function on a lattice quotient with summable values is integrable (`summable_over_lattice_quotient_locally_constant`). $\square$

**Theorem 4.13.4 (Adelic integrability).** Let $2n < M$, let $dx$ and $db$ be self-dual Haar measures, and let $\Phi$ be Schwartz-Bruhat. Then $\Phi^\star$ is $db$-integrable on $\operatorname{Herm}_n(\mathbb{A}_E)$.

Lean: `GlobalTheory.CompanionTheory.SiegelND.Integ.integrable_starN` (also `GlobalTheory.T.siegel_weil_convergent_range`, a second name).

*Proof.* Split both Haar measures as a product of an archimedean and a finite measure (`adelic_haar_splits_as_arch_times_finite`, `hermitian_haar_splits_arch_times_finite`). Write $\Phi = \sum_i P_i \otimes Q_i$ as a finite sum of pure tensors. For a pure tensor
$$(P \otimes Q)^\star(b) = c \, P^\star(b_\infty) \, Q^\star(b_f)$$
with a constant $c$ from the splitting of measures. The archimedean factor is integrable for $2n < M$ by the archimedean identity of [the coefficient section](/entry/pure-identity/) (`archimedean_siegel_weil_integral_identity`), and the finite factor by finite integrability. A product of integrable functions on a product space is integrable, and so is a finite sum. $\square$

### Coefficients that no frame represents

Fix the convergent hypotheses $\mathrm{Hyp}$ of [Section 4.3.8](/entry/whit-eq-integral/), with the frame integral $I_\beta$ and the Whittaker coefficient $W_\beta$.

**Theorem 4.13.5 (Archimedean obstruction).** Assume $\mathrm{Hyp}$. Let $\beta$ be Hermitian, $\rho$ an archimedean place, $\varepsilon = \pm 1$, and $S$ a subspace on which $\varepsilon \beta^\rho$ is nonnegative. Suppose that every subspace on which $\varepsilon \operatorname{gramAt}(V, \rho)$ is positive definite has dimension less than $\dim S$. Then $W_\beta = 0$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.NoFrame.W_eq_zero_of_obstruction`.

*Proof.* By [the coefficient formula](/entry/whit-eq-integral/), $W_\beta$ is a product of local factors, and the factor at $\rho$ is the integral of the archimedean Schwartz function over the fibre $m_\rho(\beta^\rho)$. If $X$ is in this fibre, then $\operatorname{gr}(X) = \beta^\rho$ and the span of $X S$ is a subspace on which $\varepsilon \operatorname{gramAt}(V, \rho)$ is nonnegative of dimension $\dim S$ when $X$ is injective on $S$. A perturbation makes it positive definite, which the hypothesis forbids. So the fibre is empty, or it lies in the degenerate locus of measure zero, and the local factor vanishes. $\square$

**Theorem 4.13.6 (Nonrepresented coefficients).** Assume $\mathrm{Hyp}$, and let $\beta$ be in block normal form with rank $r$. If no rational tuple $x$ of rank $r$ has $\operatorname{gr}(x) = \beta$, then $I_\beta = W_\beta$, and both are $0$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.NoFrame.noFrame` (also `GlobalTheory.T.frame_integral_eq_coefficient_nonrepresented`, a second name).

*Proof.* The frame integral is a sum over the frames with Gram matrix $\beta$, so it is the empty sum. For $W_\beta$, the Hasse principle for Hermitian forms says that $\beta$ is represented over $E$ if it is represented at every place. At the finite places a nondegenerate Hermitian space of dimension $M > 2n$ represents every Hermitian form of size $n$, so the failure is at an archimedean place, where it is a failure of signature (`nonrepresented_signature_obstruction`). This is the obstruction of the previous theorem, and $W_\beta = 0$. $\square$

### Matching and assembly

The cells of [Section 4.4.2](/entry/siegel-frame/) are stated for the frame integral $I_\beta$. The Schrödinger model of [the Weil representation](/learn/theta/#the-schrdinger-model) works with a matching integral $\operatorname{MatchGenA}$ on monomial Fock vectors. The next theorem identifies the two.

**Theorem 4.13.7 (Monomial matching).** Assume the standard data, the range condition and the coefficient data of the Schrödinger model, and let $w$ be the long Weyl element $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Let $\beta$ be Hermitian with $\det \beta \ne 0$, $a \in \mathrm{GL}_n(\mathbb{A}_E)$, $k$ in the standard maximal compact subgroup, and $\varphi$ a monomial Fock vector. Then
$$\operatorname{MatchGenA}\bigl({}^t\bar{a} \beta a\bigr) = |\det a|^{m-n} \, I_\beta\bigl(\varphi(\cdot \, a)\bigr).$$

Lean: `PositivityTheory.PfSWUS.SwMatch.matchMono`.

*Proof.* Both sides are products over places of local integrals, so the identity is checked place by place against a factorisation of $\psi$ (`psiPlaces`). At the real places the Fock vector is a polynomial times a Gaussian, and the local matching is a direct computation with the realification (`realMatch`, `realConj`). At the finite places both sides are integrals of a characteristic function and agree (`finite_places_match`). The factor $|\det a|^{m-n}$ comes from the modulus character of the Siegel parabolic and the change of variables $X \mapsto X a$ (`mod_of_cg`). The height is invariant under $k$, and the family of Haar measures is fixed by the standard data, so the global constants agree (`height_K_invariance`, `haarFam`, `unfolding_holds`). $\square$

Recall from [Section 4.4.2](/entry/siegel-frame/) the two cell identities $\mathrm{SiegelND}$ and $\mathrm{SiegelDeg}$, that $I_\beta = W_\beta$ for $\det \beta \ne 0$ and for $\det \beta = 0$.

**Theorem 4.13.8 (Assembly from the cells).** $\mathrm{SiegelND}$ and $\mathrm{SiegelDeg}$ together imply the Weil-Siegel formula in the convergent range.

Lean: `PositivityTheory.PfWsf.Top.head_of_siegel`.

*Proof.* The Poisson summation formula on $\operatorname{Herm}_n(\mathbb{A}_E)$, applied to $\Phi^\star$, holds because $\Phi^\star$ is integrable by adelic integrability; this is the identity $\mathrm{PoissonHerm}$ (`poissonHerm_main`). With covolume one measures (`exists_isCovolOneH`) it expresses the theta integral as $\sum_\beta I_\beta$, and with the two cell identities as $\sum_\beta W_\beta$, which is the Fourier expansion of the [Eisenstein series](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions) (`hasSum_IfrB`, `bigCell_of_poisson_siegel`). This is the big cell identity. The Weil-Siegel formula follows from the big cell identity and the decomposition of the Eisenstein series into cells, with convergence of both sides on Siegel sets (`weilThetaConvergence_of_siegelSet`, `weilEisensteinSiegelConvergence`). $\square$

**Corollary 4.13.9 (Assembly from the degenerate cell).** $\mathrm{SiegelDeg}$ alone implies the Weil-Siegel formula in the convergent range.

Lean: `PositivityTheory.PfWsf.Top.head_of_deg`.

*Proof.* $\mathrm{SiegelND}$ is proved in Lean as `Hand.Merge.siegelND`, from [the nondegenerate frame identity](/entry/siegel-frame/). Apply the assembly from the cells. $\square$

**Remark 4.13.10 (Formalization).** The names in `GlobalTheory.T` are stated with `first | exact` ([SummableDenominatorPowerOfLtStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SummableDenominatorPowerOfLtStatement.lean#L19), [FiniteAdelicSiegelWeilIntegralIdentityStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FiniteAdelicSiegelWeilIntegralIdentityStatement.lean#L15), [SiegelWeilConvergentRangeStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SiegelWeilConvergentRangeStatement.lean#L12), [FrameIntegralEqCoefficientNonrepresentedStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FrameIntegralEqCoefficientNonrepresentedStatement.lean#L10)). Two file names overstate the content: `SiegelWeilConvergentRange` holds only the integrability of $\Phi^\star$ ([SiegelWeilConvergentRange.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SiegelWeilConvergentRange.lean#L20)), and `FiniteAdelicSiegelWeilIntegralIdentity` is an integrability result, not an identity ([FiniteAdelicSiegelWeilIntegralIdentity.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FiniteAdelicSiegelWeilIntegralIdentity.lean#L25)). The denominator $\delta$ is defined in [HermOf.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HermOf.lean#L79), and the Hua step and its corollary are at [L23 and L88](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SummableDenominatorPowerOfLt.lean#L23). In [FrameIntegralEqCoefficientNonrepresented.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FrameIntegralEqCoefficientNonrepresented.lean#L193) the proof of `noFrame` uses only the first fields of $\mathrm{Hyp}$, and the obstruction at [L120](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FrameIntegralEqCoefficientNonrepresented.lean#L120) needs only one archimedean place. The matching predicate is [MatchMono](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/UnitarySchrodingerModel/DictKAOfParts.lean#L49) and the theorem is in [MatchMono.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/UnitarySchrodingerModel/UnitarySchrodingerLemmas/SchrodingerMatching/MatchMono.lean#L14). The cell predicates are in [BigCellDefs.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/WeilSiegelTheta/BigCellDefs.lean#L68), and the chain `head_of_two`, `big_of_three`, `head_of_three`, `head_of_siegel`, `head_of_deg` is in [HeadOfSiegel.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/WeilSiegelFormula/HeadOfSiegel.lean#L28). Since `head_of_deg` fills in $\mathrm{SiegelND}$ itself, its only remaining input is $\mathrm{SiegelDeg}$ ([L58](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/WeilSiegelFormula/HeadOfSiegel.lean#L58)), which is [the degenerate cell](/entry/siegel-deg/).
