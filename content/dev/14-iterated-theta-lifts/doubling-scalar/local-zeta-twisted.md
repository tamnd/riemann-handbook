---
id: local-zeta-twisted
title: The local zeta integral at a tamely ramified twist place
kind: theorem
decl: GlobalTheory.TwistedZeta.local_zeta_twisted
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.UnramifiedDoublingIntegralTwistedPlaceEigenvecto
covers: 342
status: drafted
drafted_by: writer@claude
---
This theorem computes the local zeta integral of one theta chain step at a tamely ramified place. It reduces it to the unramified doubling series for $\mathrm{GL}_{lt}$, a hypothesis. Its second name is [the doubling zeta integral at a twist place](/entry/unramified-doubling-integral-twisted-place-eigenvector/), and [the local factor at a twist place](/entry/local-factor/) uses it with $\mu_0 = 1$.

## Statement

Let $k$ be a nonarchimedean local field of characteristic zero, with integers $\mathcal O \supset \mathfrak p$, residue field of size $q$ and uniformizer $\varpi$. Let $G = \mathrm{GL}_{r+lt}(k)$. Let $J \subset G$ be the parahoric subgroup: the elements of $\mathrm{GL}_{r+lt}(\mathcal O)$ whose lower left block lies in $\mathfrak p$. For $e \in \mathbb Z^{lt}$ let $t_e = \mathrm{diag}(1_r, \varpi^{e})$ and $|e| = \sum |e_i|$.

The hypotheses:

1. the unramified doubling identity `UnramifiedDoublingGL` (a field of the [third place hypotheses](/step/unitary-group-third-place-hypotheses-def/));
2. $\xi$ is unitary, trivial on $1 + \mathfrak p$ but not on $\mathcal O^\times$; $\mu_0$ is unitary and unramified;
3. the multiset of the $\alpha_i \in \mathbb C^\times$ is $B \cdot (\mu_0\xi)(\varpi)^{-1}$, and $|\alpha_i|^{\pm 1} \le q^{\rho}$;
4. $H$ is $\mathrm{GL}(\mathcal O)$-bi-invariant with $H(\mathrm{diag}\,\varpi^e) = q^{-|e|}$, and $m$ is a Haar measure on $G$ with $m(J) = 1$;
5. $c(g) = \langle \omega_{\mu_0\xi}(g, 1)\Phi, \Phi\rangle$ in $L^2$ of $(r+(l+1)t) \times (r+lt)$ matrices, where $\omega_\mu(g,h)\Phi(x) = \mu(\det g/\det h)|\det g|^{b/2}|\det h|^{-a/2}\Phi(h^{-1}xg)$, and $\Phi(x) = \xi(\det x_{11})^{-1}$ when $x$ is integral, $\det x_{11}$ is a unit and the lower left block lies in $\mathfrak p$, and $\Phi(x) = 0$ otherwise.

**Theorem.** $c(1) \neq 0$, and there is $\zeta \colon G \to \mathbb C$ with:

- (i) for every representation $\pi$ of $G$, every $x$ in the $\xi$-type space of $J$ on which the twisted Hecke operators act by the eigenvalues of $B$ (`IsGen`), every $\ell$ with $\ell(\pi(j)v) = \xi(\det j_{22})\ell(v)$ on $J$, and every $g$: $\overline{c(g)}\,\ell(\pi(g)x) = \overline{c(1)}\,\zeta(g)\,\ell(x)$;
- (ii) $\zeta = 1$ on $J$;
- (iii) for $\mathrm{Re}\, s > \rho - \tfrac12$, $\zeta H^{s - t/2}$ is integrable and
$$\int_G \zeta H^{s - t/2}\, dm = L(s + \tfrac12, \alpha)\, L(s + \tfrac12, \alpha^{-1}) \prod_{i=1}^{lt}\bigl(1 - q^{-(2s+i)}\bigr),$$
with $L(s, \alpha) = \prod_i (1 - \alpha_i q^{-s})^{-1}$.

## Proof

1. Let $\mu_K(K) = 1$ on $\mathrm{GL}_{lt}(k)$. By `T.biInvariant_eigenfunction_eq_mul_zonalSpherical` there is a spherical function $\psi$ with parameter $\alpha$, and each bi-invariant Hecke eigenfunction $f$ with the eigenvalues of $\alpha$ is $f(1)$ times its zonal integral $Z_\psi$.
2. `T.twistedPlace_doubleCoset_volume_and_disjoint`: $m(Jt_eJ) = q^{r|e|}\mu_K(Kt_eK)$, and the cells $Jt_eJ$ for antitone $e$ are disjoint.
3. `T.weilRep_chainStep_matrixCoefficient_twisted` gives the bi-equivariance of $c$ under $J$, a support condition, and the value $c(t_e)$: a unit times $C_0\, q^{-(r+(l+1)t)|e|/2}$, with $C_0 > 0$. So $c(1) = C_0 \neq 0$.
4. Put $\zeta = q^{-(2r+(l+1)t)|e|/2} Z_\psi(\varpi^e)$ on $Jt_eJ$ for antitone $e$, and $\zeta = 0$ elsewhere. Then (ii) is the case $e = 0$.
5. For (i) on a cell, the lemma `lower_eigen` computes $\ell(\pi(t_e)x)/\ell(x)$ as a unit times $q^{-r|e|/2} Z_\psi(\varpi^e)$, from `T.lowerBlockCoefficient_isSphericalHeckeEigen` and step 1. Off the cells, $c = 0$ by `T.support_parahoricBiTransforming_doubleCosets`, for $\xi$ tame and ramified.
6. For (iii), `integral_biInvariant_hasSum_doubleCoset` writes the integral as a sum over cells. After the exponents of $q$ are added, the terms are those of the $\mathrm{GL}_{lt}$ doubling series. `T.unramified_doubling_sum_GL_convergent_L_value` uses hypothesis 1 to sum the series.

## In the Lean code

The theorem is in [UnramifiedDoublingIntegralTwistedPlaceEigenvecto.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnramifiedDoublingIntegralTwistedPlaceEigenvecto.lean#L213), with `lower_eigen` at line 137. Hypothesis 1 is in [PairwiseDisjointCell.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/PairwiseDisjointCell.lean#L314). It is an unramified computation of the doubling method (Gelbart, Piatetski-Shapiro and Rallis, *Explicit Constructions of Automorphic L-Functions*, LNM 1254, 1987). We have not opened the proofs of the six `T.` lemmas.

The function $\zeta$ does not depend on $\pi$, $x$ or $\ell$. The hypothesis `CharZero k` is used only to apply `UnramifiedDoublingGL`.
