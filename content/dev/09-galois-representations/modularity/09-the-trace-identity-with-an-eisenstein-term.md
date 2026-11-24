---
title: The trace identity with an Eisenstein term
decls:
  - UpperTheory.V.Z.IntegralApplyAeEq.main
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.killExempt
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cixOf
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cix_of
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cix
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The trace identity with an Eisenstein term

This section proves the trace identity that the [induction of a swapped pair](/entry/core-ind/) of Section 8 uses. It compares the twisted spectral side for $\mathrm{GL}_4$ over $E$ with the spectral side for $\mathrm{GL}_4$ over $F$, at the parameters of a family. On the twisted side there is one term more than the cuspidal trace: the Eisenstein term $\tfrac12 \mathrm{tr}_N(x, j)$ of Section 8. It comes from the continuous spectrum of the parabolic of type $(2, 2)$, and its coefficient $\tfrac12$ comes from a model computation in one variable, which we prove first. Then we show that a suitable Hecke operator kills the rest of the spectrum, and we assemble the identity. We keep the notation of Section 8 for sides, families, lines and the Eisenstein term.

### A scattering model in one variable

Let $H$ be a Hilbert space and $V$, $W$ finite-dimensional Hilbert spaces. Write $L(V) = L^2(\mathbb{R}, V)$. For a continuous kernel $\kappa\colon \mathbb{R} \to \mathrm{Hom}(V, W)$ with compact support, its *symbol* is

$$
\hat\kappa(z) = \int_{\mathbb{R}} e^{zt}\,\kappa(t)\,dt .
$$

For isometries $J\colon L(V) \to H$ and $J'\colon L(W) \to H$, an operator $X$ on $H$ *acts by* $\kappa$ from $J$ to $J'$ if $X(Ju) = J'v$ whenever $v(x) = \int \kappa(t)\,u(x + t)\,dt$ for almost all $x$. A *truncation at height $T$* is a self-adjoint idempotent $\Lambda$ whose kernel is the set of $Ju + J'v$ with $u$ and $v$ zero below $T$.

A *scattering datum* is a pair of isometries $J$, $J'$, a height $T_0$, a self-adjoint operator $B$ and compactly supported continuous kernels $\beta$ on $V$ and $\beta'$ on $W$, such that:

1. (Span.) A vector orthogonal to the images of $J$ and $J'$ is zero.
2. (Shift.) $\langle J u', J'v\rangle = \langle Ju, J'v'\rangle$ when $u'$ and $v'$ are the shifts of $u$ and $v$ by the same $t$.
3. (Causality.) $\langle Ju, J'v\rangle = 0$ when $u$ is zero below $s$ and $v$ is zero below $2T_0 - s$.
4. (Spectral operator.) $B$ acts by $\beta$ on $J$ and by $\beta'$ on $J'$, and $\hat\beta(0)$ and $\hat\beta'(0)$ are invertible.
5. (Compactness.) $\Lambda B \Lambda$ is compact for each truncation $\Lambda$ at a height $T \geq T_0$.

**Theorem 8.9.1 (Trace of a truncated convolution).** Let a scattering datum be given. Then there is a unitary $N\colon W \to V$ with these properties.

1. If an operator $Y$ acts by compactly supported continuous kernels $\gamma$ on $J$ and $\gamma'$ on $J'$, then $N\hat\gamma'(0) = \hat\gamma(0)N$.
2. Let $X$ act by a compactly supported continuous kernel $\kappa$ from $J$ to $J'$, let $T \geq T_0$, and let $\Lambda$ be a truncation at height $T$ with $\Lambda X \Lambda$ of trace class. If $\lVert\hat\kappa(z)\rVert \leq K/(1 + |\mathrm{Im}\, z|)$ for $|\mathrm{Re}\, z| \leq 1$, then

$$
\Bigl|\operatorname{tr}(\Lambda X \Lambda) - \tfrac12 \operatorname{tr}\bigl(N\hat\kappa(0)\bigr)\Bigr| \leq (\dim V)\, e^{2T_0}\, K\, e^{-2T}.
$$

Lean: `UpperTheory.V.Z.IntegralApplyAeEq.main`.

*Proof.* We give the steps. The span, shift and causality conditions give a model of $H$ in which $J$ and $J'$ are the two halves of the space and the inner products $\langle Ju, J'v\rangle$ are given by a fixed operator between $V$ and $W$, so that operators acting by convolution on both lines act through their symbols. The spectral operator $B$, the invertibility of its symbols at $0$ and the compactness of $\Lambda B \Lambda$ show that this operator gives a unitary $N\colon W \to V$, and that $N$ intertwines the symbols at $0$ of each operator that acts by convolution on both lines. This is item 1. For item 2, fix $\varepsilon > 0$. In the model, the trace of $\Lambda X \Lambda$ is the integral of the symbol of $\kappa$ against the truncated kernel, up to $\varepsilon$. The point $0$ contributes $\tfrac12\operatorname{tr}(N\hat\kappa(0))$, because the truncation keeps one half of the line through it. The rest is bounded by the symbol on the lines $\mathrm{Re}\, z = \pm 1$, which gives the factor $K e^{-2T}$, times the factor $e^{2T_0}$ from causality and a factor $\dim V$ for the trace. As $\varepsilon$ is arbitrary, item 2 follows. $\square$

The theorem is the source of the factor $\tfrac12$ in the trace identity. In the application, $H$ is $L^2$ for $\mathrm{GL}_4$ over $E$, $J$ and $J'$ are the lines $A$ and $A'$ of a family made into wave packets along the centre of the Levi, $B$ is the operator of the amplifier, and $X$ is $U_q^j R(g)\theta$.

### Killing the rest of the spectrum

An *automorphic datum* over $E$ is a cuspidal datum on a Levi subgroup of $\mathrm{GL}_4$, with its parameters off $S$. A *killing function* is an admissible function $\Phi$ of the Hecke parameters at the places outside $S$, with a generating sequence $G$ of Hecke polynomials whose truncations $G_d$ approximate $\Phi$. It *kills* a datum if it vanishes at the parameters of the datum. Let $P_c$ be the cuspidal projection, $A$ the amplifier of a side and $\chi(A)$ its functional calculus for a real function $\chi$. An *evaluation* sends a Hecke polynomial to its operator on $L^2$.

**Theorem 8.9.2 (Killing outside a family).** Let $E$ be totally complex, let $\theta$ be a twist of $L^2$ for $\mathrm{GL}_4$ over $E$, let a family over a side be given with parameters $(\Lambda, t)$ and projection $P$ onto its lines, and let $\eta > 0$. Then there is a finite list of automorphic data $b_i$ over $E$, each with parameters off $S$ and none with the parameters $(\Lambda, t)$, such that the following holds. Let an evaluation commute with $P$ on the Hecke polynomials outside $S$. Let $\chi$ be continuous with $\chi = 0$ on $(-\infty, \eta/2]$ and $|\chi| \leq 1$. Let $\Phi$ be a killing function that kills each $b_i$, with generating sequence $G$. Then there is $C$ with

$$
\bigl\lVert G_d\,\chi(A)\,(1 - P_c - P)\bigr\rVert \leq \frac{C^{d+1}}{d!} \quad \text{for all } d \geq 0.
$$

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.killExempt`.

*Proof.* First, $PP_c = 0$ and $P_cP = 0$. Indeed, the vectors on the lines are pseudo-Eisenstein series, and their cuspidal projections are zero, since the constant term along the parabolic of type $(2,2)$ carries them. As $P$ and $P_c$ are orthogonal projections, $1 - P_c - P$ is the orthogonal projection onto the complement of the cuspidal spectrum and the lines.

A general killing lemma for the amplifier gives a bound $B$ and reduces the claim to the components of the continuous spectrum. By the Langlands decomposition, these are indexed by cuspidal data $d$ of length at least $2$. There are three cases.

1. The datum $d$ has the parameters $(\Lambda, t)$. Then $d$ is $(\tau_1, \tau_2)$ or $(\tau_2, \tau_1)$, as the parameters of a family are rigid. A vector in the range of $1 - P_c - P$ is orthogonal to the lines $A$ and $A'$, and so its component along $d$ is zero.
2. Some archimedean parameter of $d$ is larger than $B$. Then the cutoff $\chi(A)$ gives the bound directly.
3. All the parameters of $d$ are at most $B$. There are only finitely many such data up to the continuous parameter. Let $b_i$ run through those that do not have the parameters $(\Lambda, t)$. Then $\Phi$ kills $d$, and the truncations $G_d$ give the bound $C^{d+1}/d!$.

The three cases give the claim. $\square$

### The trace identity

**Theorem 8.9.3 (Assembly of the trace identity).** Assume these inputs: the bounds for the local parameters of automorphic summands; the exponential expansion in $j$ of the traces of $U_q^j R(g)\theta$ on the eigenspaces of the amplifier; the existence and uniqueness of the parameters of a summand; the compatibility of the values of Hecke polynomials with base change; the existence of killing functions for two finite lists of data over $E$ and over $F$; the base change of killing functions; the truncation of killing functions; the existence of separating polynomials for disjoint compact sets; the one-sided estimates of a spectral side, without and with a family; the existence of evaluations; the killing lemma for a side; the killing outside a family; and the family estimate for the lines of a family. Then the trace identity below holds.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cixOf`.

The trace identity reads as follows. Let $E$ and $F$ be totally complex with $F \subseteq E$, let $\theta$ be a twist for $\mathrm{GL}_4$ over $E$, and let $\mathfrak{e}$ be a side over $E$ for $\theta$ and $\mathfrak{f}$ an untwisted side over $F$. Let $c \in \mathbb{C}$ be such that the geometric sides of $\mathfrak{e}$ and $\mathfrak{f}$ match up to $c$. Let a family over $\mathfrak{e}$ have parameters $(\Lambda, t)$, and assume that no automorphic datum over $F$ has parameters whose base change is $(\Lambda, t)$ outside $S$. For a property $Q$ of summands, write $\mathrm{tr}_{\mathfrak{e}}(Q; x, j)$ for the spectral trace of $\mathfrak{e}$ over the summands with $Q$, at the eigenvalue $x$ of the amplifier and the power $j$ of $U_q$, and the same for $\mathfrak{f}$.

*Proof.* We give the steps.

Step 1. Take evaluations on both sides. The family estimate gives an isometry $N$ and a constant, by the trace of a truncated convolution. By item 1 of that theorem, $N$ intertwines the symbols at $0$ on the two lines. The Eisenstein term has an exponential expansion in $j$ with a finite set of eigenvalues.

Step 2. The traces on both spectral sides have finite exponential expansions in $j$, and the parameters of the family are bounded.

Step 3. Fix a small $\eta > 0$ and a cutoff $\chi$ for it. The one-sided estimates give error terms on both sides for the cutoff. The killing outside the family on $E$ and the killing lemma on $F$ give two finite lists of data. A killing function $\Phi$ for both lists does not vanish at $t$. Its base change to $F$ kills the list over $F$, and the truncations of $\Phi$ are bounded.

Step 4. A separating polynomial isolates the eigenvalue $x$ of the amplifier from the other eigenvalues. Together with Chebyshev polynomials in the amplifier, $U_q^j$ and the truncations $G_d$, it gives test functions on both sides. The matching of geometric sides applies to them. On the spectral sides, the killed parts contribute at most $C^{d+1}/d!$, and the cuspidal part on $E$, the Eisenstein term and the matching part on $F$ remain.

Step 5. Let $d \to \infty$. The result is an identity of exponential sums in $j$ for all large $j$, multiplied by $x$, the value of the separating polynomial at the parameters, and the value of $\Phi$ at $t$. These three factors are not zero, so we divide by them and get the identity. $\square$

**Theorem 8.9.4 (Trace identity with an Eisenstein term).** In the situation above, there is an isometry $N$ that intertwines the symbols at $0$ of each operator that acts on both lines of the family, such that for each $x > 0$ and all large $j$

$$
\mathrm{tr}_{\mathfrak{e}}(\Lambda, t; x, j) + \tfrac12\,\mathrm{tr}_N(x, j) = c\,\mathrm{tr}_{\mathfrak{f}}(\Lambda', t'; x, j),
$$

where the right side runs over the summands over $F$ with parameters $(\Lambda', t')$ whose base change is $(\Lambda, t)$ outside $S$.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cix` (also `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cix_of`, the form with the kernel estimate and the compactness as hypotheses).

*Proof.* Each input of the assembly theorem is proved. Two of them need more. The one-sided estimate with a family uses the kernel estimate: let $R(f) = R(a)MR(g)$ with $a$, $g$ smooth and $M$ commuting with $P$ and $P_c$, and let the twisted kernel of $f$ vanish above a height $e^{cT}$. Then $\Lambda R(f)\theta P\Lambda$ is of trace class, and the twisted integral of $f$, minus the cuspidal trace and minus this trace, is at most $Ce^{N_0T}\lVert M(1 - P_c - P)\rVert + Ce^{-N_1 T}\lVert M\rVert$, with $N_1$ as large as we want. The family estimate uses the compactness of $\Lambda R(a) P$ for truncations $\Lambda$, together with the trace of a truncated convolution. Both the kernel estimate and the compactness are proved. So the assembly theorem gives the identity. $\square$

**Remark 8.9.5 (Formalization).** The assembly theorem [cixOf](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/ChebyshevNormEstimates/FinsumSum.lean#L306) takes fourteen hypotheses and needs `maxHeartbeats 1600000` (line 305) for one theorem. The trace identity `CIx` ([KillExempt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/KillExempt.lean#L108)) does not ask that $E/F$ be quadratic or that $\theta$ be a Galois twist; these facts enter only through the matching `GeoPair` of the geometric sides. The scattering model is stated in the namespace `PositivityTheory.Rg.Tf.IntegralApplyAeEq` and proved under the name `UpperTheory.V.Z.IntegralApplyAeEq.main` in [ImportsAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ScatteringLimits/ConvolutionSpectra/ImportsAlt.lean#L13), a file name that does not describe its content. Our proof of it, and Steps 1 to 5 of the assembly, summarize lemmas that we have not unfolded (`model`, `nUnit`, `nInt`, `traceNear`, `traceSm`, `famExp`, `sideEstX`, `sep`); the same holds for `Side.tr`, `GeoPair`, `Datum.Pt`, `KX.exempt` and `KX.compZero` in the [killing proof](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/ChebyshevNormEstimates/KillExempt.lean#L22). The proofs of [cix](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/Cix.lean#L5) and [cix_of](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/CixOf.lean#L13) are one term each.
