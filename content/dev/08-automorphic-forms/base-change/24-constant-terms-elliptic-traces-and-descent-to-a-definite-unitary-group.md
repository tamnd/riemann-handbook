---
title: Constant terms, elliptic traces and descent to a definite unitary group
decls:
  - UpperTheory.V.Z.Tf.GlobalTraceComparison.Asm.ctEx
  - UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.growthPiJ_holds
  - UpperTheory.V.Z.Inf.genFE
  - UpperTheory.V.Z.Tf.GaloisFromTraceFormula.runTh
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Constant terms, elliptic traces and descent to a definite unitary group

This section states the global comparison of the twisted trace formula for $\mathrm{GL}_n$ over a CM field with the trace formula of a definite unitary group, and three inputs that are used next to it. The comparison says that a regular algebraic conjugate self-dual cuspidal representation either descends to the unitary group, or shares its Satake parameters at split places with an isobaric sum that does not contain it. It is the trace formula part of the step [EveryCharacter](/step/every-character/). The inputs are the compatibility of twisted constant terms with Satake parameters, the control of the twisted trace on a cuspidal representation by elliptic terms, and the functional equation of Godement and Jacquet with a partial $L$-function.

Throughout, $E$ is a CM field with maximal totally real subfield $F$, and we keep the global notation of [Section 7.15.2](/entry/reading-split-holds/): $w$ runs over the finite places of $E$, a place is split if it is split over $F$, and cuspidal and isobaric data have Satake parameters as defined there. For a finite place $w$, a Hecke expression of rank $n$ is a formal expression built from generators $T_0, \dots, T_n$ with sums, products and scalar multiples. It defines a spherical Hecke function $f_e$ on $\mathrm{GL}_n(E_w)$, and $\mathrm{ev}_w(e, B)$ is the scalar by which $f_e$ acts on a spherical vector with Satake parameter $B$. Hecke expressions for $\mathrm{GL}_a \times \mathrm{GL}_b$ use generators indexed by pairs, and define functions $f_e$ on $\mathrm{GL}_a(E_w) \times \mathrm{GL}_b(E_w)$ and values $\mathrm{ev}_w(e, B_1, B_2)$ in the same way.

### Twisted constant terms of Hecke functions

**Theorem 7.24.1 (Constant terms of Hecke expressions).** Let $w$ be a split place, $\mu$ a Hecke character of $E$ unramified at $w$, and $a + b = n$. There is a substitution $t$ that sends each generator $T_j$, $0 \le j \le n$, to a Hecke expression $t_j$ for $\mathrm{GL}_a \times \mathrm{GL}_b$, such that for every Hecke expression $e$ of rank $n$, with $e[t]$ the expression obtained by substituting $t_j$ for $T_j$:

1. the $\mu_w$-twisted constant term of $f_e$ along the block upper triangular parabolic subgroup, as in Section 15, is $f_{e[t]}$;
2. for multisets $B_1$ and $B_2$ of sizes $a$ and $b$,
$$\mathrm{ev}_w(e[t], B_1, B_2) = \mathrm{ev}_w\big(e,\ \mu_w(\varpi)^bB_1 \cup \mu_w(\varpi)^aB_2\big).$$

Lean: `UpperTheory.V.Z.Tf.GlobalTraceComparison.Asm.ctEx`.

*Proof.* The theorem is deduced from the following facts, with $q$ the residue cardinality at $w$ and $\mathrm{ct}$ the untwisted constant term.

1. $f_e$ is a spherical Hecke function and acts on a spherical vector of Satake parameter $B$ by $\mathrm{ev}_w(e, B)$.
2. $\mathrm{ct}$ is linear on Hecke functions, sends products (convolutions) to products, and sends the unit of $\mathrm{GL}_n(\mathcal{O}_w)$ to the unit of $\mathrm{GL}_a(\mathcal{O}_w) \times \mathrm{GL}_b(\mathcal{O}_w)$.
3. There are numbers $c_{j,p}$, $p = (p_1, p_2)$ with $p_1 \le a$ and $p_2 \le b$, such that
$$\mathrm{ct}(T_j) = \sum_p c_{j,p}\,T_{p_1} \otimes T_{p_2}.$$
4. With the same numbers, the Satake eigenvalues $\lambda_j$ satisfy, for $|B_1| = a$, $|B_2| = b$ and scalars $c_1, c_2$,
$$\lambda_j(c_1B_1 \cup c_2B_2) = \sum_p c_{j,p}\,c_1^{p_1}c_2^{p_2}\,\lambda_{p_1}(B_1)\lambda_{p_2}(B_2).$$
5. The twisting character is trivial on $\mathrm{GL}_a(\mathcal{O}_w) \times \mathrm{GL}_b(\mathcal{O}_w)$, multiplicative, and equal to $\mu_w(\varpi)^{bp_1 + ap_2}$ on the support of $T_{p_1} \otimes T_{p_2}$.
6. An integral over a group modulo an open subgroup of a right invariant function is the sum over the cosets.

By 3 and 5 the twisted constant term of $T_j$ is $\sum_p c_{j,p}\mu_w(\varpi)^{bp_1 + ap_2}T_{p_1} \otimes T_{p_2}$, which is $f_{t_j}$ for the expression $t_j$ with these coefficients. By 2 and 5 the twisted constant term is linear, multiplicative and unital, so 1 holds for every $e$ by induction on $e$. By 4 with $c_1 = \mu_w(\varpi)^b$ and $c_2 = \mu_w(\varpi)^a$, statement 2 holds for the generators, and both sides of 2 are additive and multiplicative in $e$. We did not unfold how fact 6 enters the reduction. $\square$

### Elliptic terms control the twisted trace

Let $\theta$ be the involution $g \mapsto {}^t\bar g^{-1}$ of $\mathrm{GL}_n(\mathbb{A}_E)$ used in Section 07. A cuspidal representation $\pi$ is $\theta$-fixed if its forms are invariant under the split centre and $\varphi \mapsto \varphi \circ \theta$ maps the space of $\pi$ to itself. We use the Hilbert spaces $\mathcal{H}$ of Section 22 for $(a, b) = (n, 0)$, the twisted classes and the regular elliptic orbital terms of [the elliptic formula](/entry/ell-formula2-j/), and we write $\mathrm{Ell}(\phi)$ for the sum of the orbital terms of $\phi$ over pairs of regular elliptic twisted classes. Let $\mathcal{H}_\pi \subset \mathcal{H}$ be the closure of the span of the families whose components are $\psi(x)u(\log|\det x|)$ with $\psi$ in $\pi$ and $u$ continuous with compact support. For a matrix $\Phi$ of test functions and a scalar matrix $M$, put $\mathrm{tr}_M\Phi = \sum_{i,j}\Phi_{ij}M_{ji}$.

**Theorem 7.24.2 (Elliptic terms control the twisted trace).** Let $E$ be a CM field with more than one archimedean place, $n \ge 1$, and $\mu_1$ a Haar measure on $\mathrm{GL}_n(\mathbb{A}_E)$. There is a fundamental domain datum whose measure is $\mu_1$, such that the following holds. Let $\pi$ be a $\theta$-fixed cuspidal representation, $\Phi_1$ and $\Phi_2$ matrices of test functions with right convolution operators $T_1$ and $T_2$, the entries of $\Phi_1$ of finite rank on $\pi$, $M$ a scalar matrix, $r_0, r_1 \ge 0$ and $\varepsilon > 0$. Then there are $C$ and $N$ such that for every $k \ge 0$, every bounded $U$ that maps $\mathcal{H}_\pi$ and $\mathcal{H}_\pi^\perp$ into themselves, every test matrix $\Phi$ whose right convolution operator is $T_1UT_2$ and such that $\mathrm{tr}_M\Phi$ is a test function of size $r_0 + kr_1$, and every $t$ equal to the twisted trace of $\mathrm{tr}_M\Phi$ on $\pi$,
$$\Big|\mathrm{Ell}(\mathrm{tr}_M\Phi) - \frac t2\Big| \le C(1 + k)^N\,\big\|U|_{\mathcal{H}_\pi^\perp}\big\| + C\|U\|\varepsilon^k.$$

Lean: `UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.growthPiJ_holds` (also `growthPi_holds`, a second name).

*Proof.* This is a reduction theorem applied to five inputs: an estimate of the uncut half of the twisted trace formula, an estimate of the cut tail, [the elliptic formula](/entry/ell-formula2-j/) that expresses the elliptic part through orbital integrals, the existence of $\pi$-vectors of each size, and the invariance of $\pi$ under $\theta$. The reduction itself is not unfolded. The shape of the bound shows how the inputs are used: the operator $T_1UT_2$ splits into its parts on $\mathcal{H}_\pi$ and on $\mathcal{H}_\pi^\perp$, the part on $\mathcal{H}_\pi$ gives the twisted trace $t$, the part off $\pi$ is bounded by $\|U|_{\mathcal{H}_\pi^\perp}\|$ times a polynomial in the size, and the remaining terms give $C\|U\|\varepsilon^k$. $\square$

### The functional equation with a partial $L$-function

**Theorem 7.24.3 (Godement-Jacquet functional equation).** Let $K$ be a number field and $n \ge 2$. Let $\varphi_1$, $\varphi_2$ be cusp forms on $\mathrm{GL}_n(\mathbb{A}_K)$ with $\varphi_1$ invariant under the central section $t \mapsto t \cdot 1$ of the positive reals, and let
$$f(g) = \int\varphi_1(xg)\overline{\varphi_2(x)}\,dx,$$
the integral over $\mathrm{GL}_n(K)\backslash\mathrm{GL}^1_n(\mathbb{A}_K)$, with $f \ne 0$. Let $S$ be a finite set of finite places containing those that divide the different of $K$. For each finite $v$ let $\pi_v$ be an irreducible admissible representation of $\mathrm{GL}_n(K_v)$, $\xi_v$ a smooth vector and $\ell_v$ a smooth vector of the dual. For $v \notin S$ assume that $\xi_v$ and $\ell_v$ are fixed by $\mathrm{GL}_n(\mathcal{O}_v)$, that $\ell_v(\xi_v) = 1$, and that $\pi_v$ has Satake parameter $z_v$. Assume that
$$f(g) = f_\infty(g_\infty)\prod_v\ell_v(\pi_v(g_v)\xi_v).$$
For $v \in S$ let $\Phi_v$ be a Schwartz-Bruhat function on $M_n(K_v)$, and for $v \notin S$ let $\Phi_v$ be the indicator function of $M_n(\mathcal{O}_v)$. Then there are $c, c' \ne 0$ such that the Fourier transforms $\hat\Phi_v$, $v \in S$, are Schwartz-Bruhat, and for every Schwartz function $\phi$ on $M_n(K_\infty)$ there are $\sigma \in \mathbb{R}$ and an entire function $\Lambda$ such that for $\mathrm{Re}\,s > \sigma$ we have $L^S(s, \pi) \ne 0$ and
$$\begin{aligned}\Lambda(s) &= c\,Z_\infty(\phi, f_\infty, s)\prod_{v \in S}Z(\Phi_v, f_v, s)\,L^S(s, \pi),\\ \Lambda(1 - s) &= c'\,Z_\infty(\hat\phi, \check f_\infty, s)\prod_{v \in S}Z(\hat\Phi_v, \check f_v, s)\,L^S(s, \tilde\pi).\end{aligned}$$
Here $f_v(g) = \ell_v(\pi_v(g)\xi_v)$, $\check f(g) = f(g^{-1})$, $Z(\Phi, f, s) = \int\Phi(g)f(g)|\det g|^{s + (n-1)/2}\,dg$, $L^S(s, \pi) = \prod_{v \notin S}L(s, \pi_v)$, and $L^S(s, \tilde\pi)$ is the same product for the contragredients.

Lean: `UpperTheory.V.Z.Inf.genFE`.

*Proof.* The global zeta integral of $\phi \otimes \bigotimes_v\Phi_v$ against $f$ extends to an entire function $\Lambda$, and $\Lambda(s) = \Lambda'(1 - s)$ where $\Lambda'$ is the global zeta integral of the adelic Fourier transform against $\check f$; this is the theorem of Godement and Jacquet, taken as an input. For $\mathrm{Re}\,s$ large the global integral factors as an Euler product of local zeta integrals, by the factorization of $f$. For $v \notin S$ the local zeta integral of the indicator function against the spherical matrix coefficient is $L(s, \pi_v)$, and the same holds for the contragredient; the products converge for large $\mathrm{Re}\,s$. The adelic Fourier transform of $\phi \otimes \bigotimes_v\Phi_v$ is a constant times the product of the local transforms, and for $v \notin S$ the indicator function is its own transform, since $v$ does not divide the different. Take $c$ from the normalisation of the measures and $c'$ as $c$ times the Fourier constant. Finally $L^S(s, \pi)$ is a convergent product of nonzero factors, so it is not $0$. $\square$

### Descent to a definite unitary group

Let $U(n)$ be the unitary group of the standard Hermitian form $\sum_i x_i\bar y_i$ over $F$; it is definite at every archimedean place. For a split place $w$ above $v$ we identify $U(n)(F_v)$ with $\mathrm{GL}_n(E_w)$ as in Section 15. A cuspidal representation $\pi$ of $\mathrm{GL}_n(\mathbb{A}_E)$ is conjugate self-dual if its contragredient is isomorphic to its complex conjugate $\pi^c = \pi \circ c$, and regular algebraic if its infinitesimal characters are those of an algebraic representation with regular weight.

**Theorem 7.24.4 (Descent or endoscopy).** Let $E$ be a CM field in which every finite place is unramified over $F$, $n \ge 1$, and $\pi$ a regular algebraic conjugate self-dual cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ that has a Satake parameter at every nonsplit place. Then one of the following holds.

1. There is an automorphic representation $\sigma$ of $U(n)$, unramified at every nonsplit place, such that for all but finitely many split places $w$ there are a smooth irreducible representation $\tau$ of $\mathrm{GL}_n(E_w)$ and a multiset $B$ with $\tau$ a component of $\sigma$ at $w$, $\tau$ of Satake parameter $B$, and $\pi$ of Satake parameter $B$ at $w$.
2. There is a regular isobaric datum $D$ of rank $n$ that does not contain $\pi$, such that at all but finitely many nonsplit places $D$ has a Satake parameter $B$ with $B^{-1} = B$, and at all but finitely many split places $D$ and $\pi$ have the same Satake parameter.

Lean: `UpperTheory.V.Z.Tf.GaloisFromTraceFormula.runTh`.

*Proof.* The theorem is a comparison theorem applied to the following inputs. The first two are the computation of the unit side of the trace formula of $U(n)$ and [the signed stabilization](/entry/g2s/) of Section 20. Then come the existence of admissible characters, the matching of unit elements and of functions at split places, and the stable unit term. The last two are the endoscopic block bound and the stable block bound. The two block bounds are proved from the [spectral bound](/entry/spec-p/) of Section 22, applied to the predicate that reads infinitesimal characters on cusp forms. The comparison theorem also takes four facts about $\theta$-fixed representations (their terms, finiteness, admissibility and twisted trace sums) and the [control by elliptic terms](/entry/growth-pi-j-holds/) above. The comparison theorem itself is not unfolded; alternative 2 is the endoscopic case, in which the stable part of the twisted trace formula is not accounted for by $U(n)$. $\square$

**Remark 7.24.5 (Formalization).** The constant term theorem is the term at [CtEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/TraceAsymptotics/CtEx.lean#L11), `rCtEx` applied to `exAct`, `ctLin`, `ctUnit`, `ctT`, `ctMul`, `satSum`, `muTw` and `hintSph`; the statement `CtEx` is in `SplitLineAlt.lean` (line 35), and the facts 2 to 6 are stated in `FinprodSplitAlt.lean` (lines 22 to 52). We did not unfold `rCtEx` or the proofs of these facts; the substitution in the proof above is read off from them. The control by elliptic terms is at [GrowthPiJHolds.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/AutomorphicRepresentations/GrowthPiJHolds.lean#L52): `rGrowthPiJ_of` with `uncutHalf`, `cutTail`, `ellFormula2J`, `sFun_holds`, `piVecEx_holds` and `piInv`; the statement asks for a Haar measure on $\mathrm{GL}_0(\mathbb{A}_E)$ as well, a trivial group. The reduction `rGrowthPiJ_of` and the uncut and cut estimates were not unfolded; the idea in the proof is only a reading of the inputs. The functional equation is [GenFE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ArchimedeanSchwartz/GenericFunctionalEquation/GenFE.lean#L13). Irreducibility and admissibility are assumed at every $v$ but passed on only for $v \notin S$ (line 48). The set called the ramified places of $K$ is the set of places dividing the different; it has nothing to do with $\pi$, and the hypotheses on $\xi_v$ and $\ell_v$ do the work of unramifiedness. The descent theorem is [DescWeak.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GaloisFromTraceFormula/DescWeak.lean#L9): `runTh_of_pi` applied to `piTerm_holds`, `piFin_holds`, `piAdm_pf`, `twTrSum_pf` and `growthPiJ_holds`, and `runTh_of_pi` (in `DescWeakOfPi.lean`, line 14) passes `uSide`, `g2s`, `muEx`, `matchUnit`, `matchSplit`, `stUnit`, `endoBlockG cuspReadI` and `stableBlockG cuspReadI` to `runTh_of` (`DescWeakOfGalStep.lean`, line 64), which we did not unfold. The statement `RunTh` is in `EvaluationAtUnitaryOne.lean` (line 37); the regularity of the isobaric datum is the condition `CD.Reg`, that the sum of the infinitesimal characters at each embedding is that of a dominant weight.
