---
title: Whittaker integrals at the finite places
decls:
  - PositivityTheory.SiegelWeilFormula.Gunr.unrPoly
  - PositivityTheory.SiegelWeilFormula.Gunr.locC
  - PositivityTheory.SiegelWeilFormula.SwLocFin.locFinX
  - PositivityTheory.SiegelWeilFormula.KLI.locData_of
  - PositivityTheory.SiegelWeilFormula.Fin.whitGenEq
  - PositivityTheory.SiegelWeilFormula.Fin.whitGenLow
  - PositivityTheory.SiegelWeilFormula.KWhit.genDictX_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Whittaker integrals at the finite places

The standard Siegel-Weil formula of the next section compares a Siegel [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) with a theta integral by comparing their Fourier coefficients. [Section 4.9.6](/entry/wr/) computed the archimedean Whittaker integrals. This section treats the finite places: the unramified Whittaker integral is a product of local zeta factors, the ramified one is an entire function whose value at the Siegel-Weil point is a Gram density, and the global coefficient identities follow. The last theorem is the dictionary that writes each Fourier coefficient as a product of local Whittaker integrals times an orbit integral of theta.

Let $E_v/F_v$ be a quadratic extension of local fields at a finite place $v$, with $q$ the order of the residue field of $F_v$, $\varpi$ a uniformiser and $\varepsilon = \pm 1$ according as $E_v/F_v$ is unramified or not split, so that the quadratic character takes the value $\varepsilon$ on $\varpi$. Let $\psi_k$ be the character $b \mapsto \psi(\varpi^{-k} b)$ of $\operatorname{Herm}_n(\mathcal{O}_{E_v}/\varpi^k)$, and for a Hermitian $B$ modulo $\varpi^k$ let $\nu(B)$ be the index of the module of [Section 4.13.1](/entry/hs-step/) at the level $\varpi^k$.

### The unramified integral

**Theorem 4.14.1 (Unramified polynomial).** Let $T$ be a unimodular Hermitian matrix of size $n$ and $k \ge 1$. Then
$$\sum_{B \in \operatorname{Herm}_n(\mathcal{O}_{E_v}/\varpi^k)} \psi_k\bigl(\operatorname{tr}(\bar{T} B)\bigr) \, t^{\log_{q^2} \nu(B)} = \prod_{i=0}^{n-1} \bigl(1 - t (\varepsilon q)^i\bigr),$$
where $\bar{T}$ is the reduction of $T$.

Lean: `PositivityTheory.SiegelWeilFormula.Gunr.unrPoly`.

*Proof.* Group the $B$ by the elementary divisors of their denominator. Because $T$ is unimodular, the character sum over the matrices with a fixed elementary divisor type is a Gauss sum over a Hermitian space over the residue field, and it is computed by counting isotropic subspaces. The counts satisfy a recursion in $n$ obtained by splitting off a line, which gives one factor $1 - t(\varepsilon q)^i$ for each step (`unramified_formula_polynomial_gen`, `unramified_local_formula`). The answer does not depend on $k$ because the terms with denominator beyond the level cancel. $\square$

**Theorem 4.14.2 (Unramified Whittaker integral).** Let $v$ be a good place, that is $E_v/F_v$ unramified or split, $\psi_v$ of conductor $\mathcal{O}_{F_v}$ and the data unramified. For $\operatorname{Re} z > n^2$,
$$\int W(b, z) \, d\nu_v(b) = \prod_{i=0}^{n-1} \bigl(1 - \varepsilon^{M+i} \, N v^{-(2z + n - i)}\bigr).$$

Lean: `PositivityTheory.SiegelWeilFormula.Gunr.locC`.

*Proof.* The integral is over $\operatorname{Herm}_n(E_v)$, and the integrand $W(b, z)$ is the product of $\psi_v(\operatorname{tr}(Tb))$, the denominator of $b$ to the power $-(2z + n)$ and a Weil index factor $\varepsilon^{M \operatorname{ord}}$. It is constant on cosets of $\operatorname{Herm}_n(\mathcal{O}_{E_v})$, so the integral is a sum over $\operatorname{Herm}_n(E_v)/\operatorname{Herm}_n(\mathcal{O}_{E_v})$, which converges for $\operatorname{Re} z$ large by the Hua bound. The sum over the classes of denominator dividing $\varpi^k$ is the unramified polynomial at $t = \varepsilon^M N v^{-2z - n}$ up to normalisation, and letting $k$ grow gives the product. $\square$

The product is $\prod_{i<n} L(2z + n - i, \eta^{M+i})^{-1}$ with $\eta$ the quadratic character of $E/F$, the normalising factor of the Siegel Eisenstein series. This is the unitary case of Shimura's computation of the local singular series.

### Ramified places

**Theorem 4.14.3 (Finite place Whittaker integral).** Let $v$ be finite, let the Haar measures be self-dual, let $L_1$ and $L_2$ be lattices, let $\Phi_v$ be Schwartz-Bruhat, and let $g$ be a continuous Gram density on the invertible Hermitian matrices, so that $\int \Phi_v(X) f(\operatorname{gr} X) \, dX = \int f(S) g(S) \, dS$ for $f$ supported on invertible $S$. Let $T$ be Hermitian with $\det T$ a unit. Then there is an entire function $W$ with
$$\begin{aligned} W\bigl(\tfrac{M-n}{2}\bigr) &= g(T), \\ W(z) &= \int W_{\Phi_v}(b, z) \, d\nu_v(b) \quad (\operatorname{Re} z > t), \end{aligned}$$
for some $t$, where $W_{\Phi_v}(b, z)$ is the local Whittaker integrand of $\Phi_v$.

Lean: `PositivityTheory.SiegelWeilFormula.SwLocFin.locFinX`.

*Proof.* Write $\Phi_v$ in terms of the two lattices, so that the integrand is a finite combination of indicators of shells $\{X : \operatorname{gr}(X) \in T + \varpi^k L\}$ (`shellP`). On each shell the integral over $b$ in a ball is a character sum, and the sum over balls is a polynomial in $N v^{-2z}$ for large $k$; this gives an entire function equal to the integral in the half plane of convergence (`convP`). At $z = (M - n)/2$ the Fourier inversion formula on $\operatorname{Herm}_n(E_v)$, with self-dual measures, turns the integral into the local average of [Section 4.12.5](/entry/avg-free-tendsto/), whose value is $g(T)$ (`dualP`). $\square$

### The local operator data

The global dictionary needs, at each complex place, a local model of the [Weil representation](/learn/theta/#the-weil-representation) that carries a Fock vector to a Gaussian polynomial. This is the role of the next theorem.

**Theorem 4.14.4 (Local operator data).** Let $L$ be a Schrödinger model at a complex place in the sense of $\mathrm{LocHyp}(\mathrm{sg}, L)$: a family of operators with fields for the Weil action, the identity, products, linearity, the unipotent, Levi and opposite unipotent actions, and the long Weyl functional. Put $(p, q) = (m, 0)$ if $\mathrm{sg} = 1$ and $(p, q) = (0, m)$ otherwise. Then there are a section $s_L$, a representation $\rho$ of the maximal compact subgroup and an equivalence $e$ with
$$\begin{aligned} &\mathrm{LocData}(2\pi, 2\pi \cdot \mathrm{sg}, p, q, e, s_L, \rho), \\ &s_L(P)(y) = L(y)(f_P)(0), \\ &L(k) f_P = f_{\rho(k) P}, \end{aligned}$$
where $f_P$ is the Fock vector attached to a polynomial $P$.

Lean: `PositivityTheory.SiegelWeilFormula.KLI.locData_of`.

*Proof.* Define $s_L(P)$ as the function $y \mapsto L(y)(f_P)(0)$. The fields of $\mathrm{LocHyp}$ give the transformation law of $s_L(P)$ under the Siegel parabolic, so it lies in the induced representation. The action of $k$ on $f_P$ preserves the degree of $P$, which defines $\rho$, and $e$ is the identification of the Fock space with polynomials of signature $(p, q)$. The long Weyl functional fixes the normalisation at the identity. $\square$

### The global coefficients

We now state the coefficient identities that feed [the standard formula](/entry/siegel-weil-std-of/). Write $W_T(z)$ for the $T$-th Fourier coefficient of the Siegel Eisenstein series at $z$, normalised so that $z = 0$ is the Siegel-Weil point, and $\operatorname{mean}(\theta_T)$ for the mean over $U_J(F) \backslash U_J(\mathbb{A})$ of the $T$-th coefficient of the theta function.

**Theorem 4.14.5 (Coefficients in the equal rank case).** Let $J$ be anisotropic with $n = M$, and let $T$ be nondegenerate. Then $W_T(0) = 2 \operatorname{mean}(\theta_T)$.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.whitGenEq`.

*Proof.* By the dictionary below, $W_T(z)$ is a constant times a product of local Whittaker integrals. At good places use the unramified integral, at the remaining finite places the finite place integral, and at the real places the archimedean integral of [Section 4.9.6](/entry/wr/) (`realWhitEq_of`). The product of the local values at $z = 0$ is the product of local Gram densities, which by [the Euler product formula](/entry/whit-eq-integral/) and [the density equation](/entry/dens-eq/) is the mean of $\theta_T$ times a constant. The factor $2$ comes from the normalising $L$-factors at $z = 0$ when $n = M$, and the order count (`lOrd`) and the factorisation (`factorX`) fix it. $\square$

**Theorem 4.14.6 (Coefficients below the critical rank).** If $M < n$ then $W_T(0) = 0$ for every nondegenerate $T$, matching the empty theta coefficient.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.whitGenLow`.

*Proof.* A Hermitian space of dimension $M$ does not carry an $n$-frame with nondegenerate Gram matrix, so the theta coefficient is $0$. On the Eisenstein side, the product of local Whittaker integrals has a zero at $z = 0$ of order larger than the order of the pole of the normalising factor, by the order count of the local factors. So $W_T(0) = 0$. $\square$

**Theorem 4.14.7 (Generic dictionary).** Let $\Phi$ be a pure $K$-finite Schwartz-Bruhat function and $x$ in the Levi subgroup of the Siegel parabolic. For each nondegenerate $T$ there are an anisotropic Hermitian $J$ with one prescribed sign at each archimedean place and constants $c$ and $C$ such that
$$W_T\bigl(\Phi, x, z\bigr) = c \, C^{z - s_0} \int \operatorname{whI}(b, z) \, d\nu(b),$$
and the orbit integral of $\omega(x)\Phi$ over the Gram fibre is $c$ times the mean of theta over the fibre $T'$.

Lean: `PositivityTheory.SiegelWeilFormula.KWhit.genDictX_of`.

*Proof.* The coefficient of the Eisenstein series is the integral over the big cell of the Bruhat decomposition (`cellFormula`), which is an adelic Whittaker integral. The relation between $T$ and the Gram fibre $T'$ uses the Levi element $x$ (`relEx`), and the change from $x$ to the identity produces the factor $C^{z - s_0}$ through the height (`heightDict`). The constant $c$ compares the Haar measures (`measDict`), and the identification with the mean of theta is [the theta coefficient formula](/entry/whit-eq-integral/) (`thetaDict`). These five pieces are combined by `dictAsmX`. $\square$

The dictionary is the input to the three coefficient statements `whitK_of`, `whitEq_of` and `whitLow_of`, used in the next section.

**Remark 4.14.8 (Formalization).** The unramified polynomial is the statement `UnrPoly` of [WhitGenOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenOf.lean#L73), and `unrPoly` and `locC` are at [CFinal.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/UnramifiedWhittaker/CFinal.lean#L20). The statement `LocC` in [TraceDual.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/UnramifiedWhittaker/TraceDual.lean#L42) assumes $\operatorname{Re} z > n^2$, which is stronger than its users need. Its proof `locC_of_steps` uses `unrPoly` and nine lemmas, while an older note says fourteen. `LocFinX` is at [WhitGenLowOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenLowOf.lean#L39), and the related `WhitGenX` at [L158](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenLowOf.lean#L158) carries a hypothesis ($n + 2 \le M$ or $J$ anisotropic) that its proof does not use. `locFinX` itself is in [LocFin2.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LocalCharacterIntegrals/LocFin2.lean#L8). The local operator data is in [POfAddQOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LocalOperatorBlocks/POfAddQOf.lean#L89), with `LocHyp` in [LongWeylFunctional.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LocalOperatorBlocks/LongWeylFunctional.lean#L35). The dictionary is in [GenDictXOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhittakerCovolume/GenDictXOf.lean#L19), with `GenDictX` in [WhitAtCOneIff.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhittakerCovolume/WhitAtCOneIff.lean#L43). The coefficient theorems are at [SiegelWeilStdOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L46) and [L49](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L49). The companion `whitGenLt`, the case $n < M$ with constant $1$, is proved elsewhere and is not part of this section.
