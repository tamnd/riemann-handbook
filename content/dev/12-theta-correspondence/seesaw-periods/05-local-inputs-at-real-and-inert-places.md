---
title: Local inputs at real and inert places
decls:
  - GlobalTheory.TwArch.archOnRecord_closed
  - GlobalTheory.T.archimedeanThetaCorrespondence_towers_real_data
  - GlobalTheory.ChainOnto.std_cayley_of_inert
  - GlobalTheory.T.weilDatum_inertPlace_standard_cayley_pair
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local inputs at real and inert places

The unfolded periods of the chain are products of local factors. The last section treated the split places. This section gives the inputs at the two other kinds of places. At the real places we need the archimedean facts about discrete series and real theta lifts that the chain uses. At a finite place that is inert in $E$ we put a global Weil datum and a nonzero vacuum into a standard local form, and we prove the Cayley rule for its vacuum coefficients. Both results are inputs of the step [the nonempty hypotheses](/step/nonempty-hyps/). For the background see [discrete series](/learn/representations/#discrete-series), [the Fock model](/learn/theta/#the-fock-model) and [the local theta correspondence](/learn/theta/#the-local-theta-correspondence).

### Real places

**Theorem 7.5.1 (Archimedean facts on record).** Assume the classification of the discrete series of the covers with the Blattner properties (Harish-Chandra; Hecht and Schmid), and the theory of Harish-Chandra modules. Then for every global datum the archimedean facts used by the chain hold: the real theta lifts along the chain have no lower occurrence, they reach the expected discrete series when the parameters have the required gaps, their zeta integrals do not vanish, the real theta maps compose as expected, and the lowest $K$-type maps to the Fock model exist, are unique and are harmonic.

Lean: `GlobalTheory.TwArch.archOnRecord_closed` (also `GlobalTheory.T.archimedeanThetaCorrespondence_towers_real_data`, a second name).

*Proof.* This is [Theorem 8.3.10](/entry/arch-on-record/) applied to the two assumptions and the datum. $\square$

### Inert places

Let $v$ be a finite place of $F$ that is inert in $E$, and let $w$ be a place of $E$ above $v$. Then $w$ is the only place of $E$ above $v$: the ideal of $w$ contains the extension of the ideal of $v$, which is prime, and so equal to the ideal of every place above $v$. Let $q_v$ be the size of the residue field of $v$.

**Definition 7.5.2 (Inert data).** Let $E_w$ be the completion, $c$ the Galois involution of $E_w$ and $\varpi$ a uniformizer, with the unramified relation to $q_v$. An inert chart of a Hermitian space $S$ of dimension $m$ is an isomorphism of $U(S)(F_v)$ with the standard unitary group $\mathrm{GU}_m$ of $c$, which carries the frame lattice of $S$ to the standard lattice. A vacuum at $v$ is a theta function $f$ on $W(S, T)$ that is fixed by the Heisenberg operators of the frame lattice of $W(S, T)$ at $v$.

**Definition 7.5.3 (Standard pair and Cayley rule).** Let $M$ be a complex vector space with an action $\rho$ of the additive group $M_{n \times m}(E_w)$ and an action $\omega$ of $\mathrm{GU}_m \times \mathrm{GU}_n$, and let $s \in M$. We say that $(M, \rho, \omega, s)$ is a standard pair for $\delta \in E_w$ and a character $\psi'$ of $E_w$ if $\rho$ and $\omega$ form the local Weil representation for the pairing $\delta \cdot \mathrm{tr}$ with the standard antidiagonal forms, $s \neq 0$ is a vacuum for $\rho$, and the vectors $\rho(x) s$ span $M$. Let $\pi$ be an action of $\mathrm{GU}_N$ on $M$ and $N' \geq 0$. The Cayley rule with exponent $N'$ says: for every linear form $e$ on $M$ invariant under $\rho(u)$ for all integral $u$, and every $g \in \mathrm{GU}_N$ with $\det(1 + g) \neq 0$ and $(1 + g)^{-1}$ integral,

$$\begin{aligned} e\bigl(\pi(g^{-1}) s\bigr) &= \bigl((-1)^{N'} q_v^{N'}\bigr)^{\mathrm{ord}\, \det(1 + g)}\, e(s). \end{aligned}$$

The Cayley rule computes the vacuum coefficient on the elements $g$ whose Cayley transform $(1 - g)(1 + g)^{-1}$ is defined: the coefficient depends only on the valuation of $\det(1 + g)$.

**Theorem 7.5.4 (Standard form at an inert place).** Let $\omega$ be a Weil datum on $(S, T)$ with characters $\chi_S, \chi_T$, with $\dim S = m$ and $\dim T = n$. Let $v$ be inert in $E$ with place $w$ above it, and assume $\chi_S$ and $\chi_T$ are unramified at $w$. Let $c$, $\varpi$ be as above, and let $e_S$, $e_T$ be inert charts of $S$ and $T$. Let $f$ be a nonzero vacuum at $v$. Then there are $\delta \in E_w$, a character $\psi'$ of $E_w$, a subspace $M$ of functions on $W(S, T)$, actions $\rho$ and $\omega_v$ on $M$ and $s \in M$ such that:

1. $(M, \rho, \omega_v, s)$ is a standard pair, and $s = f$;
2. $\omega_v(g, g') m = \omega(e_S^{-1} g, e_T^{-1} g') m$ for all $g, g'$ and $m \in M$, with the local groups embedded at $v$;
3. the action of the first factor satisfies the Cayley rule with exponent $n$, and the action of the second factor satisfies the Cayley rule with exponent $m$.

Lean: `GlobalTheory.ChainOnto.std_cayley_of_inert` (also `GlobalTheory.T.weilDatum_inertPlace_standard_cayley_pair`, a second name).

*Proof.* First we localize: there are $\delta$, $\psi'$, $M$, $\rho$, $\omega_v$ and $s$ with items 1 and 2, such that $M$ consists of theta functions and each $\rho(u)$ acts on $M$ as a Heisenberg operator $H(u_0)$. Choose a Haar measure and a fundamental domain of covolume one, and let $\langle \cdot, \cdot \rangle$ be the inner product of theta functions over this domain. Define the linear form $l(m) = \langle m, f \rangle$ on $M$. Then $l(s) = \langle f, f \rangle \neq 0$, since the inner product is positive definite on theta functions and $f \neq 0$.

The form $l$ is invariant under $\rho(u)$ for integral $u$. Indeed $\rho(u)$ acts as $H(u_0)$, the vacuum $s = f$ is fixed by $\rho(u)$ and so $H(u_0) f = f$, and the inner product is invariant under Heisenberg operators. A criterion for standard pairs now applies: if a linear form with $l(s) \neq 0$ is invariant under the integral part of $\rho$, the Cayley rule holds for each factor as soon as the vacuum coefficient of that factor agrees with an explicit bi-invariant function. For the first factor, the coefficient $g \mapsto \langle \omega(g, 1) f, f \rangle$ is the vacuum matrix coefficient of the source at the inert place. For the second factor, the coefficient $g' \mapsto \langle \omega(1, g') f, f \rangle$ is the matrix coefficient of the vacua at an unramified place. This uses that $\chi_S$ and $\chi_T$ are unramified at every place above $v$, which holds because $w$ is the only such place, and the value of $\chi_S$ at the inert place. Both coefficients have the required form, and the Cayley rules follow. $\square$

**Remark 7.5.5 (Formalization).** The archimedean theorem only passes its two hypotheses to `GlobalTheory.ArchRec.archOnRecord` ([ArchimedeanThetaCorrespondenceTowersRealData.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ArchimedeanThetaCorrespondenceTowersRealData.lean#L12)). The two hypotheses are the Prop-valued literature statements `DiscreteSeriesCover` and `HarishChandraModules`. In the inert theorem the localization, the criterion and the two matrix coefficients are the lemmas `exists_standardLocalisation_weilDatum_inertPlace`, `cayleyRule_of_biInvariantVacuumCoefficient`, `vacuum_matrixCoefficient_source_inert_place_alt` and `weilMatrixCoefficient_vacua_unramifiedPlace`, which are not unfolded here; so is the local pair `LocPair` inside the standard pair. The proof sets `maxHeartbeats` to 2000000.
