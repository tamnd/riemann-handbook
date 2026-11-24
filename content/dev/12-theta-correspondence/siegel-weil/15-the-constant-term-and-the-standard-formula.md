---
title: The constant term and the standard formula
decls:
  - PositivityTheory.SiegelWeilFormula.Act.C5.unf
  - PositivityTheory.SiegelWeilFormula.Act.secUnf_of_cLaw
  - PositivityTheory.SiegelWeilFormula.Act.secUnf_of
  - PositivityTheory.SiegelWeilFormula.Act.ctSplit_of
  - PositivityTheory.SiegelWeilFormula.KFP.kFinPoly_of
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The constant term and the standard formula

This section proves the standard Siegel-Weil formula: at the point $(m-n)/2$ the Siegel [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) of a $K$-finite Schwartz-Bruhat function equals the mean of the theta function, with the constant $1$ if $n < m$ and $2$ if $n = m$. It is the form of [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula) that the literature route of [every character](/step/every-character-of-literature/) uses, through [the literature statement](/entry/siegel-weil-std-of-literature/). The proof compares Fourier coefficients. The nondegenerate coefficients come from [Section 4.14.5](/entry/whit-gen-eq/), and the degenerate ones are reduced to lower rank by the constant term along a maximal parabolic, which is the subject of the first part.

### The constant term along a parabolic

Let $P$ be the maximal parabolic subgroup of the unitary group $U(n, n)$ that stabilises an isotropic line, see [parabolic subgroups](/learn/groups/#parabolic-subgroups), and $N'$ the unipotent radical of the Siegel parabolic of the smaller group $U(n-1, n-1)$. Write $c_P$ and $c_K$ for the volumes that normalise the Haar measures on $P$ and $K$, and $c_2(x)$ for the second term of the constant term along $P$ of the Eisenstein series of $\varphi_z$, the section attached to $\Phi$.

**Theorem 4.15.1 (Second term of the constant term).** Under the hypotheses $\mathrm{C5.Hyp}$, that is convergence of the Eisenstein series at $z$, a Bruhat decomposition of $P \backslash U / P$ into three cells and the matching of Haar measures,
$$c_2(x) = K \sum_{q'} \int \Bigl( \int \varphi_z\bigl(w_1 \, c_M(c) \, j(q' n'(\beta)) \, x\bigr) \, d\kappa \Bigr) \psi_{T'}(\beta) \, d\lambda'(\beta),$$
with $K = c_P / c_K$, where $q'$ runs over the rational points of the Siegel parabolic of the smaller group modulo $N'$, $w_1$ is the Weyl element of the middle cell, $c_M$ parametrises the Levi factor and $j$ embeds the smaller group.

Lean: `PositivityTheory.SiegelWeilFormula.Act.C5.unf`.

*Proof.* The constant term along $P$ is the integral over $N_P(F) \backslash N_P(\mathbb{A})$ of the sum over $P_{\mathrm{Siegel}}(F) \backslash U(F)$. Sort the sum by the double cosets of the Bruhat decomposition. The middle cell is $P_{\mathrm{Siegel}}(F) w_1 P(F)$, and unfolding its part of the sum against $N_P$ gives an integral over $N_P(\mathbb{A})$ and a sum over the Siegel parabolic of the smaller group. Its unipotent part becomes a Fourier expansion in $\beta$ with characters $\psi_{T'}$. The measures on the unfolded integral and on $P$ and $K$ differ by $c_P / c_K$. $\square$

**Theorem 4.15.2 (Second term law).** Under the hypothesis $\mathrm{CLaw}$, which states the cell decomposition with explicit Haar constants, the second term is the Eisenstein series of $U(n-1, n-1)$ attached to the restricted section, with the factor $K$. This is the statement $\mathrm{SecUnf}$.

Lean: `PositivityTheory.SiegelWeilFormula.Act.secUnf_of_cLaw` (also `PositivityTheory.SiegelWeilFormula.Act.secUnf_of`, which supplies $\mathrm{CLaw}$ from absolute convergence).

*Proof.* Build $\mathrm{C5.Hyp}$ from $\mathrm{CLaw}$ and apply the second term of the constant term. The sum over $q'$ is the Eisenstein series of the smaller group, evaluated at the section $y \mapsto \int \varphi_z(w_1 c_M(c) j(y) x) \, d\kappa$, and the integral over $\beta$ against $\psi_{T'}$ is its $T'$-th coefficient. For `secUnf_of`, absolute convergence of the Eisenstein series in the half plane gives $\mathrm{CLaw}$ (`cLawEx`). $\square$

**Theorem 4.15.3 (Constant term splitting).** For each point and each $\Phi$, the constant term along $P$ is the sum of a first term, an Eisenstein series of the Levi factor, and the second term, an Eisenstein series of $U(n-1, n-1)$. This is the statement $\mathrm{CTSplit}$.

Lean: `PositivityTheory.SiegelWeilFormula.Act.ctSplit_of`.

*Proof.* The three cells of the Bruhat decomposition give three terms (`indepDom`, `cptDom`). The open cell contributes nothing to the constant term by a character integral over a compact domain. The closed cell gives the first term (`firstEq`), and the middle cell gives the second term by the second term law (`secLaw_of`). The exchanges of sum and integral use absolute convergence (`absConv`). $\square$

### $K$-finite functions are Fock vectors

**Theorem 4.15.4 ($K$-finite functions are polynomial).** Let $\Phi$ be a $K$-finite Schwartz function at the archimedean places. Then its image $T\Phi$ under the intertwiner to the Fock model lies in the Fock space $R.\mathrm{fock}$, that is, it is a polynomial times the standard Gaussian.

Lean: `PositivityTheory.SiegelWeilFormula.KFP.kFinPoly_of`.

*Proof.* The span of the $K$-translates of $\Phi$ is finite dimensional, so the action of the rotations $u \mapsto e^{i\theta} u$ on it has finitely many weights. Decompose $\Phi$ along lines through the origin (`line_data`): on each line, the function $\theta \mapsto \Phi(e^{i\theta} u)$ is a trigonometric polynomial. For $\xi$ fixed, the Laplace transform
$$E_\xi(z) = \exp\bigl(-z^2 |\xi|^2/16\pi\bigr) \int h(u) \, e^{-2\pi |u|^2} e^{z \langle \xi, u \rangle} \, du$$
is entire, and the weight condition makes it a polynomial in $z$ (`exists_poly`, `poly_of_rot`). Polynomials along every line give a polynomial in $u$ times the Gaussian (`poly_gauss_of_lines`). $\square$

### The standard formula

**Definition 4.15.5 (Standard Siegel-Weil formula).** Fix good base data with $1 \le m$, $1 \le n$ and $\min(r, s) = 0$, a Hermitian $A$ and a skew-Hermitian $Y$, a [Hecke character](/learn/class-field-theory/#hecke-characters) $\chi$ whose restriction is a power of the quadratic character, a doubling datum, a frame, a standard maximal compact subgroup $K$ and a height. Let $\mu$ be a Haar measure on $U_A(\mathbb{A})$ with a fundamental domain $D$. The statement $\mathrm{SiegelWeilStd}$ is that for every $K$-finite $\Phi$ and every $x$,
$$\operatorname{EisValueAt}\Bigl(\operatorname{flat}\bigl(a(\ell(\omega(x)\Phi))\bigr), \tfrac{m-n}{2}\Bigr) = \kappa \cdot \frac{1}{\mu(D)} \int_D \theta\bigl(\omega(x) S_g \Phi\bigr) \, d\mu(g),$$
with $\kappa = 1$ if $n < m$ and $\kappa = 2$ if $n = m$.

**Theorem 4.15.6 (Standard formula from coefficients).** Assume the constant term splitting and the lower rank formula. Then $\mathrm{SiegelWeilStd}$ holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of`.

*Proof.* Both sides are automorphic forms on $U(n, n)$, and their difference $D$ is orthogonal to cusp forms. Gaussian splitting (`GSplit`) and the vacuum vector at the archimedean places (`VacK`) reduce to $\Phi$ whose archimedean part is a Fock vector. The nondegenerate Fourier coefficients of $D$ vanish: for $n < m$ by `whitGenLt` (`WhitK`), for $n = m$ by the coefficients in the equal rank case (`WhitEq`), and for $m < n$ by the coefficients below the critical rank (`WhitLow`). For the degenerate coefficients use the constant term splitting and induction on $n$ (`AStep.stepOf`). So all coefficients of $D$ vanish, and $D = 0$ (`Atop.siegelWeilStd_of`). $\square$

**Corollary 4.15.7 (Standard formula with leading terms).** The hypotheses of the standard formula from coefficients follow from the local instances, the Gaussian identity, the $K$-finiteness of polynomial vectors and the holomorphy of leading terms.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid`.

*Proof.* The local instances come from `locInst_of`, the Gaussian identity from [Section 4.6.5](/entry/g-idil-of/) (`gIdil_full`), $K$-finiteness of polynomial vectors from `polyKFin_of`, and holomorphy of the leading term below the middle from [Section 4.7.3](/entry/hol-lead-b/) (`HSt.holLeadB`). These give the hypotheses of the standard formula from coefficients. $\square$

**Corollary 4.15.8 (Standard formula before the constant term).** Given the Poisson identity and the constant term splitting, $\mathrm{SiegelWeilStd}$ holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre`.

*Proof.* The Weyl transform identity $\mathrm{TWeyl}$ follows from the bijection of cells, the theta transform, uniqueness up to scalars and the Poisson identity (`tWeyl_of`). With it, $K$-finite functions are polynomial in the sense of $\mathrm{KFinPoly}$ (`kFinPoly_of` with `tUnit`, `tHeis`, `fockMem` and the local operators), and the local data follow (`ldEx_of`). Apply the standard formula with leading terms. $\square$

**Corollary 4.15.9 (Standard formula from the constant term).** The constant term splitting implies $\mathrm{SiegelWeilStd}$.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct`.

*Proof.* Apply the previous corollary with the Poisson identity `TW.Twp.poisson`. $\square$

**Theorem 4.15.10 (Standard Siegel-Weil formula).** $\mathrm{SiegelWeilStd}$ holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd`.

*Proof.* The constant term splitting holds, so the standard formula from the constant term applies. $\square$

This is the theorem cited as Kudla-Rallis and Ichino in [the literature statement](/entry/siegel-weil-std-of-literature/), here proved in Lean for the unitary dual pair in the range $n \le m$ and for $m < n$ in the form of vanishing coefficients.

**Remark 4.15.11 (Formalization).** The statement $\mathrm{SiegelWeilStd}$ is in [HypothesesS.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/HypothesesS.lean#L11). The final proof in [SiegelWeilStd.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStd.lean#L8) passes `kfour.auxEx` and `kfour.coefEx` to `ctSplit_of`, but `ctSplit_of` ignores both arguments ([CtSplitOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/CtSplitOf.lean#L10)); the name `auxEx` is misleading, since it is an auxiliary prime function datum and not a constant term input ([AuxiliaryPrimeFunction.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/AuxiliaryPrimeFunction.lean#L206)). In [SecUnfOfCLaw.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/SecUnfOfCLaw.lean#L13) the hypothesis `hk'` of `secUnf_of_cLaw` is unused. `C5.unf` is in [ImportsAlt.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/ImportsAlt.lean#L21), `SecUnf` in [CtSplitOfParts.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/CtSplitOfParts.lean#L52) and `CTSplit` in [LowerRankDatum.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LowerRankDatum.lean#L155). In [SiegelWeilStdPre.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStdPre.lean#L19) the term `tWeyl_of ... hP` is built twice. `Fin.siegelWeilStd_of` and `Atop.siegelWeilStd_of` share a short name ([SiegelWeilStdOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L52)). The predicates `TWeyl` and `KFinPoly` are at [AuxiliaryPrimeFunction.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/AuxiliaryPrimeFunction.lean#L186), and `kFinPoly_of` is in [KFinPolyOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/RealAdelicFockSpace/KFinPolyOf.lean#L24).
