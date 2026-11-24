---
title: Generic masses, small fundamental sets and thin tubes
decls:
  - GlobalTheory.WeightsFamPf.weightsFam_of
  - GlobalTheory.T.genericMass_le_heightPow_mul_gluedCount
  - GlobalTheory.GenMassBound.genericMass_le_heightPow_mul_glueSum
  - GlobalTheory.SmallFund.small_fundamental_set
  - GlobalTheory.T.haar_volume_thin_tube_unitary_product_asymptotic
  - GlobalTheory.Tube.thin_tube
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Generic masses, small fundamental sets and thin tubes

This section collects three results that the step [nonempty hypotheses](/step/nonempty-hyps/) uses directly. The first bounds the generic mass of a family of local data by a power of a height times an explicit count, and from it a bound by an abelian constant times the amplitude. The second is a reduction statement for the real points of a unipotent radical: every real point is, up to a rational point of a congruence subgroup, close to the base point in two-step exponential coordinates. The third is an asymptotic for the Haar volume of a thin tube in $U(k, 1)$ or $U(k + 1)$. The three results are independent of each other. They share the setting of [Section 2.15.5](/entry/weights-add-up-to-mass/) and of [Section 2.6.8](/entry/fibre-normal-fibre-volume/).

### The generic mass of a family

Recall from [Section 2.15.5](/entry/weights-add-up-to-mass/) the mass of a genus of local data. A *family* of local data consists of a finite set $P$ of places, local data at each $p \in P$, a positive constant $V_0$, and a local generic mass $n_{\mathrm{gen}}(p)$ at each $p \in P$. Its *total generic mass* is
$$n_{\mathrm{gen}}^{\mathrm{tot}} = V_0 \prod_{p \in P} n_{\mathrm{gen}}(p).$$

**Definition 2.27.1 (Glued sum).** Let $F$ and $F'$ be isotropic flags of rank $r_S$ and let $s$ be a finite set of lattices. The *glued sum* is
$$\Sigma(s) = \sum_{\Lambda \in s} \frac{1}{\# \operatorname{Stab}(\Lambda)},$$
where $\operatorname{Stab}(\Lambda)$ is the finite group of integral elements of the unipotent group of the pair $(F, F')$ that fix $\Lambda$. The set $s$ is a *set of glued representatives* if it is a set of representatives of the lattices glued from the local data, in the sense of the formal predicate. That predicate is not unfolded here.

**Theorem 2.27.2 (Generic mass bounded by a glued count).** Let $4 r_S + 7 \le k$. Let a family of local data with $V_0 > 0$ be given, together with a point $w$ whose image is a given point $\gamma$, flags $F$, $F'$ with $F$ a rational translate of the base flag, and local data that satisfy the base conditions and the mass law: the mass of every datum that agrees with the base datum outside $P$ equals $V_0$ times the product of the local weights over $P$. Assume that the local generic mass at each $p \in P$ is the one of the family, and that at each $p$ there are terms over the datum. Then

1. $n_{\mathrm{gen}}^{\mathrm{tot}} > 0$;
2. the local heights satisfy $H_p \ge 1$ for $p \in P$;
3. there are a point $w$ with image $\gamma$ and a flag $G'$ in the cell of $w$ such that, for every set $s$ of glued representatives for $(F, G')$, the set $s$ is nonempty and
$$n_{\mathrm{gen}}^{\mathrm{tot}} \le H^{3 (r+1)^2}\, \Sigma(s), \qquad H = \prod_{p \in P} H_p.$$

Lean: `GlobalTheory.GenMassBound.genericMass_le_heightPow_mul_glueSum` (also `GlobalTheory.T.genericMass_le_heightPow_mul_gluedCount`, a second name).

*Proof.* The proof bounds each local generic mass by the mass of a pairing class. Upper and lower bounds for the masses of pairing classes give $n_{\mathrm{gen}}(p) \le H_p^{3(r+1)^2} m_p$, where $m_p$ is a local mass and $H_p \ge 1$. The product of the $m_p$ times $V_0$ is a mass of the genus. By the mass law, this mass is the weighted count of the glued lattices, which is $\Sigma(s)$ for any set of glued representatives. The point $w$ and the flag $G'$ come from a normal form of the pair of flags in the cell of $w$. Positivity of $n_{\mathrm{gen}}^{\mathrm{tot}}$ follows from $V_0 > 0$ and the positivity of each local factor. $\square$

The formula for the local factors is taken from the factorization of the generic mass into local pieces. We do not unfold the local mass bounds here.

**Theorem 2.27.3 (Generic masses of families are positive and bounded).** Assume the Siegel-Weil input of the mass formula and the compatibility of the stabilizer volumes with the first Chern class, for every Hida setting. Then for all constants $C_g, c_b, C_w, c_T, C_T, C_0$ there are $C'_0$ and $C_{l,0}$ with the following property. For all $C' \ge C'_0$ and $C_l \ge C_{l,0}$, for every admissible context with these constants, every family of local data tied to a point $\gamma$, relatively generic at each $p \in P$, with terms over each $p$ and with the orbit identity for $V_0$,
$$0 < n_{\mathrm{gen}}^{\mathrm{tot}} \le A_2(2v, r_S, k, f)\, \mathcal{A} \cdot 2 \cdot H(\gamma)^{e(r_S)}\, n(\gamma).$$
Here $A_2$ is an abelian constant that depends on $2v$, $r_S$, $k$ and $f$; $\mathcal{A}$ is the amplitude of the mass data; $H(\gamma)$ is the height of $\gamma$ at the scale $T_u T_{u'}$; $n(\gamma)$ is a count of points; and $e(r)$ is a fixed exponent.

Lean: `GlobalTheory.WeightsFamPf.weightsFam_of` (the property is `GlobalTheory.SnFam.WeightsFam`).

*Proof.* Choose $C'_0$ at least $2$ and at least the constant of the local identity of the families lemma. The standing hypotheses give $4 r_S + 7 \le k$ and $2 r_S + f + 7 \le k$. A local identity for different data gives the mass law for the family in the base situation. The flag norms are congruent modulo the square of the level. [Theorem 2.27.2](/entry/generic-mass-le-height-pow-mul-glue-sum/) then bounds $n_{\mathrm{gen}}^{\mathrm{tot}}$ by $H^{3(r+1)^2} \Sigma(s)$. The glued count is bounded by an explicit weighted count. Its mean constant equals the unscaled main constant of the mass formula; this is the only place where the Siegel-Weil input enters. The norms and invariants of a generic rational pair of frames, and the bound of a power of a Gram invariant by a Haar weight, convert the result into the stated form. The exponents combine by
$$3 (r+1)^2 + 6 (2r + 2) \le e(r). \qquad \square$$

**Remark 2.27.4.** The theorem is conditional. Its hypothesis is a Siegel-Weil statement for the unitary group together with a compatibility of volumes. The proof does not show that hypothesis. For the classical Siegel-Weil formula see Weil (1965) and, for unitary groups, Ichino (2004).

### Small fundamental sets for the unipotent radical

Let $E/F$ be a CM extension of number fields with $f = [F : \mathbb{Q}]$, and let $r_d = |d_E|^{1/(2f)}$. Let $G$ be the unitary group of a Hermitian form $J$ on $E^n$ with a self-dual lattice $L$. For $x \in G(\mathbb{A})$ let $\Lambda_x$ be the lattice of $y \in E^n$ with $x_f^{-1} y \in \hat L$. Let $K(g)$ be the principal congruence subgroup of level $g$ in $G(\mathbb{A}_f)$.

**Definition 2.27.5 (Sizes).** For a lattice $\Lambda$ with the metric induced by $x$, the *size* of $\Lambda$ is its normalized covolume to the power $1/(2 n_\infty \operatorname{rk} \Lambda)$, where $n_\infty$ is the number of infinite places of $E$. For $S \subset \Lambda$ the *quotient size* $\operatorname{size}(\Lambda / S)$ is the same quantity for the quotient. The *largest size* of $\Lambda$ is the supremum of $\operatorname{size}(\Lambda / S)$ over the saturated proper sublattices $S$.

**Theorem 2.27.6 (A small fundamental set for the unipotent radical).** Let $g \ge 1$, let $x \in G(\mathbb{A})$, and let $R \subseteq \Lambda_x$ be a nonzero saturated isotropic sublattice. Let $N_R$ be the unipotent radical of the stabilizer of $E R$. Let $0 < \mathrm{hi}$, $\mathrm{lo}$ and $\rho$ satisfy
$$\begin{aligned} \operatorname{largest\,size}(R) &\le \mathrm{hi}, \\ \operatorname{size}(N / R) &\ge \mathrm{lo} \text{ for all } R < N \le \Lambda_x, \\ \mathrm{hi} &\le \rho\, \mathrm{lo}, \\ \mathrm{hi}^2 &\le \rho / 4. \end{aligned}$$
Then for every $\nu \in N_R(F_\infty)$ there are $\gamma \in G(F) \cap N_R$ with $(x^{-1} \gamma x)_f \in K(g)$ and elements $A_v$, $Z_v$ of the Lie algebra at each infinite place $v$ such that
$$\nu\, x_v = \gamma_v\, x_v \exp(A_v) \exp(Z_v)$$
for all $v$, with
$$\Bigl(\sum_v \|A_v\|^2\Bigr)^{1/2} + \Bigl(\sum_v \|Z_v\|^2\Bigr)^{1/2} \le \frac{n^2 \sqrt{f}\, g\, r_d\, \rho}{4},$$
and such that for all real $s$, $t$ there is $m \in N_R(F_\infty)$ with $m\, x_v = x_v \exp(s A_v) \exp(t Z_v)$ for all $v$. The norms are Hilbert-Schmidt norms.

Lean: `GlobalTheory.SmallFund.small_fundamental_set`.

*Proof.* The group $N_R$ is two-step nilpotent: its Lie algebra is the sum of a first layer and a center. Write $\nu = \exp(Y)$ with $Y$ in the real Lie algebra of $N_R$. Apply the covering radius bound for the first layer to $Y / (2g)$. It gives an integral $Y_0$ in the first layer and a central $Z$ with $Y/(2g) - Y_0 - Z$ small. Put
$$\begin{aligned} A &= 2g\, \bigl(Y/(2g) - Y_0 - Z\bigr), \\ Z'' &= 2g\, Z + \tfrac12 [A, 2g Y_0]. \end{aligned}$$
Then $Z''$ is central. Apply the covering radius bound for the center to $Z''/g$. It gives an integral central $Z_0$ with $Z' = g(Z''/g - Z_0)$ small. The element $\gamma = \exp(2g Y_0 + g Z_0)$ is rational, lies in $N_R$, and its conjugate by $x$ lies in $K(g)$, because $\exp(2g Y_0 + g Z_0) - 1$ maps $\Lambda_x$ into $g \Lambda_x$. In a two-step nilpotent group the exponential factors as
$$\exp(Y) = \exp(2g Y_0 + g Z_0)\, \exp(A)\, \exp(Z').$$
Conjugating by $x$ gives the factorization of $\nu x$. The two covering radius bounds and the inequality
$$2 g \cdot \frac{N f\, r_d\, \rho}{8 \sqrt{2 f}} + g \cdot \frac{N f\, r_d\, \rho}{16 \sqrt{f}} \le \frac{N \sqrt{f}\, g\, r_d\, \rho}{4},$$
with $N = n^2$, give the bound on the norms. The last statement holds because $\exp(sA)$ and $\exp(tZ')$ lie in the real points of $N_R$. $\square$

### Thin tubes

**Theorem 2.27.7 (The Haar volume of a thin tube).** Let $k \ge 1$, $\eta \in \{1, -1\}$ and $H_\eta = \operatorname{diag}(1, \dots, 1, \eta)$ of size $k + 1$. Let $\mu$ be a Haar measure on $U(H_\eta)$ with density $c > 0$, and let $\mu_0$ be the Haar probability measure on $U(k)$, of density $c_0 > 0$. Then
$$\lim_{t \to 0^+} \frac{\mu\{\, g : \bigl| |g_{k k}|^2 - 1 \bigr| \le t \,\}}{t^k} = \frac{c}{c_0} \cdot \frac{(2\pi)^{k+1}}{k!},$$
where $g_{kk}$ is the last diagonal entry.

Lean: `GlobalTheory.Tube.thin_tube` (also `GlobalTheory.T.haar_volume_thin_tube_unitary_product_asymptotic`, a second name).

*Proof.* Near the stabilizer of the last basis vector, use the chart $(X, \theta, w) \mapsto$ a product of $\exp X$ for $X$ in the Lie algebra of $U(k)$, a phase $e^{i\theta}$ and a vector $w \in \mathbb{C}^k$. The condition $\bigl||g_{kk}|^2 - 1\bigr| \le t$ is a condition on $w$ alone, a ball of radius about $\sqrt{t}$ in $\mathbb{C}^k$, of volume $\pi^k t^k / k!$ to first order. The density comparison of [Section 2.26.3](/entry/big-cell-integral/), applied to this chart, gives the factor $c$. The image measure on the $U(k)$ factor has density $c_0$ and total mass $1$, which gives the factor $1/c_0$. The phase is distributed by a rotation-invariant measure on the circle, of total length $2\pi$. An arithmetic limit lemma combines the three factors into the constant $(2\pi)^{k+1}/k!$. $\square$

**Remark 2.27.8 (Formalization).** The property `WeightsFam` ([FamilyGroupSumFactorsWeightAmplitude.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/FamilyGroupSumFactorsWeightAmplitude.lean#L24)) is stated with many contexts: `Ctx`, `MassDataTie`, `MassDataAdmissible`, `FamQ`, `HasPt`, `FamTie`, `RelG` and `OrbitFamilyIdentityAt`. We have not unfolded them. The hypothesis `SWXS` of `weightsFam_of` ([FamilyGenericMassPositiveBoundedProof.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FamilyGenericMassPositiveBoundedProof.lean#L21)) is defined in [InVolumesAtOfSWS.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/InVolumesAtOfSWS.lean#L13) as the conjunction of `SWa1` and `StabilizerFirstChernCompatibility`; so the theorem is an implication, not an unconditional bound. The glued sum is `glueSum` ([GlobSet.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/GlobSet.lean#L48)), and the mass law `MassLaw` is in the same file. The description of the proof of the glued bound is a summary of the main lemmas `mass_pairingClass_bounds` and `ng_factors`. In `small_fundamental_set` ([SmallFundamentalSetRealUnipotent.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SmallFundamentalSetRealUnipotent.lean#L135)) the sizes are `largestSize` and `sizeQ` of the Harder-Narasimhan files, $r_d$ is `rd` and $f$ is `f` of the instance; the hypothesis $R \ne 0$ is not used in the proof. The radius inequality is `radius_le` at line 117 of the same file. In `thin_tube` ([HaarVolumeThinTubeUnitaryProductAsymptotic.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HaarVolumeThinTubeUnitaryProductAsymptotic.lean#L30)) the measure $\mu_0$ is asked to have total mass $1$ and density $c_0$; these two conditions fix $c_0$. The chart and the limit lemma are `exists_productChart_tangentEquiv_ballVolume` and `thinUnitaryTube_volume_limit_arith`; the volume count in the proof above is our reading of them.
