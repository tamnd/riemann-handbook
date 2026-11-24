---
title: The bad locus, the measure condition and equal volumes
decls:
  - GlobalTheory.CovTop.covering_bad_locus_of_descent_steps_alt
  - GlobalTheory.T.liftBadSet_of_deep_size_flatDeg_share
  - GlobalTheory.CovTop.MeasRd.covering_measure_reduction_alt
  - GlobalTheory.T.covering_meas_of_prints
  - GlobalTheory.CompEqVol.equal_volume_of_compactification
  - GlobalTheory.T.compactification_top_chern_eq_volume
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The bad locus, the measure condition and equal volumes

The assembly step of [the covolume bound](/entry/top-covol-g-alt-alt/) combines eight level statements. Two of them are proved in this section: the bound for the bad set of the lift, which says that the part of the type lattice killed by the good projector has small rank, and the measure condition, which compares the Gram norm of the lattice at a level with the Petersson norm of cusp forms up to a factor of size $e^{O(E)}$. The third result of the section is of a different kind. It says that on a deep good cover all components of the moduli space have the same volume, measured by the growth of the dimensions of spaces of cusp forms. It is a consequence of Mumford proportionality ([Mumford's proportionality theorem](/learn/abelian-varieties/#mumfords-proportionality-theorem)): the volume of a component is its covolume times a universal factor, and the covolumes of the components agree.

We use the language of [the first section](/entry/to-classical-theorems/): level statements and cover statements, the unit of error $E$, and a family $\mathcal{F}$ with the parameter $x$. At a point $p$ and a level $i$ the lift has a *type lattice* $M_i$, a lattice over the ring of integers of the field of the lift, and an idempotent $e_i$, the *good projector*, built from the idempotent of the good part of the level. The *bad part* of the type lattice is
$$M_i^{\mathrm{bad}} = M_i \cap \ker e_i,$$
and the good sublattice of [the covolume bound](/entry/top-covol-g-alt-alt/) is $M_i \cap \operatorname{im} e_i$. Ranks are ranks over the ring of integers. The scale of the family gives the parameter $x$ and an exponent $e_z$, which we do not unfold.

**Definition 2.16.1 (Bad set condition).** The *bad set condition* at $(p, i)$ is
$$\operatorname{rk} M_i^{\mathrm{bad}} \le 3 \, e^{-x^{e_z / 7}} \operatorname{rk} M_i.$$
The *bad set condition of the lift* is the level statement of the bad set condition.

The constant $C$ of the level statement plays no role here, since the condition does not involve it.

**Theorem 2.16.2 (The bad set of the lift).** Assume the hypotheses on the family, the published Hodge bundle theorems, Grothendieck's deformation theory, the quoted results, the toroidal compactification of the Siegel space over the integers, the toroidal compactifications for fans with the log Kodaira-Spencer isomorphism, the seminegativity of the Lie algebra, the statement on Green functions of cuspidal type, the Gram condition, the existence of good covers, deep goodness, the size condition, the flat degree condition, the cover degree condition and the share condition. Then the bad set condition of the lift holds.

Lean: `GlobalTheory.CovTop.covering_bad_locus_of_descent_steps_alt` (also `GlobalTheory.T.liftBadSet_of_deep_size_flatDeg_share`, a second name).

*Proof.* Two statements are combined, one for the last level and one for the levels below it. At the last level the bad set condition is a level statement restricted to $i + 1 = m$; it follows from the published list, the statement on Green functions and the Gram condition. Below the last level the bad set condition holds, as a cover statement, on every good cover: for $i + 1 < m$ and every good cover $Y$ of level $i$ the inequality holds. This uses all the hypotheses of the theorem except the existence of good covers, and in particular the [flat degree condition](/entry/flat-deg-alt-alt/).

Take the larger of the three thresholds in $x$ of these two statements and of the existence of good covers. Let $p$ be a point beyond the threshold and $i$ a level. If $i + 1 < m$, the existence of good covers gives a good cover $Y$ of level $i$, and the cover statement at $Y$ gives the inequality. The inequality does not depend on $Y$, so it holds at $(p, i)$. If $i + 1 \ge m$, then $i + 1 = m$ because $i < m$, and the statement for the last level applies. The constant of the level statement can be taken to be $0$. $\square$

The proof does not say anything about covers of the last level; this is why the two cases are proved separately. The argument is the pattern used throughout the chapter: a cover statement becomes a level statement as soon as good covers exist and the conclusion does not mention the cover.

The second level statement compares two norms on cusp forms. At $(p, i)$ the lift identifies each cusp form $f$ of level $i + 1$ and of the weight of the level with a vector of coordinates in the type lattice. At each complex embedding $\sigma$ the lattice has a Gram norm $\|\cdot\|_\sigma$, and $f$ has a Petersson norm $\|f\|_{\mathrm{Pet}, \sigma}$.

**Definition 2.16.3 (Measure condition).** Let $C \ge 0$. The *measure condition with constant* $C$ at $(p, i)$ says: for every embedding $\sigma$ there is $c > 0$ with
$$|\log c| \le C E$$
such that every cusp form $f$ of level $i + 1$ and the weight of the level satisfies $\|f\|_\sigma = c \, \|f\|_{\mathrm{Pet}, \sigma}$. The *measure condition* is its level statement.

So the two hermitian structures on the lattice of cusp forms are proportional, with a factor that is at most $e^{C E}$ and at least $e^{-C E}$. On slopes of [hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes) such a factor changes the slope by at most $C E$, which is within the error of the covolume bound.

**Theorem 2.16.4 (The measure condition).** Assume the published Hodge bundle theorems. Then the measure condition holds.

Lean: `GlobalTheory.CovTop.MeasRd.covering_measure_reduction_alt` (also `GlobalTheory.T.covering_meas_of_prints`, a second name).

*Proof.* At each $(p, i)$ there is a positive ratio $r_i$ built from a normalized measure of the level and the dimensions of the weight spaces. Four statements from the published list are used. The first is that the normalized covolume equals $1$. The second, which uses the first, is a level statement that $r_i > 0$ and $\log r_i \le K_1 E$. The third is a level statement $-K_2 E \le \log r_i$. The fourth, which also uses the first, is an exact comparison: at every point with the row condition, every $\sigma$ and every $f$,
$$\|f\|_\sigma = \sqrt{r_i} \, \|f\|_{\mathrm{Pet}, \sigma}.$$
Take the larger of the thresholds of the second and third statements, and $C = (K_1 + K_2)/2$. Put $c = \sqrt{r_i}$, so $c > 0$ and the identity of norms is the fourth statement. It remains to bound $\log c = \frac12 \log r_i$. If $E \ge 0$, the two bounds give
$$|\log r_i| \le \max(K_1, K_2) E \le (K_1 + K_2) E.$$
If $E < 0$, then $-K_2 E \le \log r_i \le K_1 E$ with $K_1, K_2 \ge 0$ forces $(K_1 + K_2) E \ge 0$, so $K_1 + K_2 = 0$, hence $K_1 = K_2 = 0$ and $\log r_i = 0$. In both cases $|\log c| \le \frac{K_1 + K_2}{2} E = C E$. $\square$

The third result concerns a single deep good cover. Let $Y$ be a deep good cover at level $j$ and $Z$ a component of its moduli space. Let $\lambda_0$ be the standard weight of the datum, of signature $(p, q)$, and let $d$ be the dimension of the flag space. For a weight $G$, let $S_G(Z)$ be the cusp forms of weight $G$ on $Z$, as in [the section on birationality](/entry/bir-on-of-weight-gaps-large/). The *growth* of $G$ on $Z$ is the growth rate of $\tau \mapsto \dim S_{\tau G}(Z)$ in degree $d$, a number in $[0, \infty]$. Let $\deg_{\mathrm{flag}}$ be the degree on the compact dual flag variety, as in Mumford proportionality.

**Definition 2.16.5 (Volume of a component).** The *volume* of $Z$ is
$$v(Z) = \frac{\operatorname{growth}(G_0 \text{ on } Z)}{\deg_{\mathrm{flag}}(\lambda_0)},$$
where $G_0$ is the weight of the standard weight $\lambda_0$, and the growth is taken as a real number. The cover has *equal volumes* if $v(Z) = v(Z')$ for all components $Z, Z'$.

The *top degree* of a weight $\lambda$ on $Z$ is $v(Z) \deg_{\mathrm{flag}}(\lambda)$. By asymptotic Riemann-Roch the growth of a weight is its top self-intersection divided by $d!$, so the top degree is the top Chern number up to the factor $d!$, and proportionality says that this number is the covolume times $\deg_{\mathrm{flag}}(\lambda)$.

**Theorem 2.16.6 (Equal volumes).** Assume the published Hodge bundle theorems, the toroidal compactification of the Siegel space over the integers, the toroidal compactifications for fans with the log Kodaira-Spencer isomorphism and the seminegativity of the Lie algebra. Let $D$ be a family with a core that satisfies the laws, let $j$ be a level in the range of the family with $p, q \ge 1$ at level $j$, and assume $[E : \mathbb{Q}]/2 > 2$. Then every deep good cover $Y$ at level $j$ has equal volumes.

Lean: `GlobalTheory.CompEqVol.equal_volume_of_compactification` (also `GlobalTheory.T.compactification_top_chern_eq_volume`, a second name).

*Proof.* Since $p + q \ge 1$, the toroidal compactifications for fans and the Siegel toroidal integral give model charts of the integral model, and from them charts of the toroidal flag model ([toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)). Fix the embedding $\sigma$ of the coefficient field. The invariant volume statement, proved from a refinement of the covering topology in the published list, from the numerics of nef bundles in the published list and from the seminegativity of the Lie algebra, gives a surjection $k \mapsto Z_k$ from the components of the complex uniformization onto the components of the moduli space, with
$$v(Z_k) = \operatorname{covol}(U_k) \cdot \frac{a}{b}$$
for constants $a$ and $b$ that do not depend on $k$.

Next, the lattice of the core is good at every prime: the laws give goodness from the two primes of the host, and goodness passes to the level of the cover. With $p, q \ge 1$ and the uniformization of the good cover, the components of the complex uniformization then all have the same covolume. Now let $Z, Z'$ be components and write $Z = Z_k$, $Z' = Z_{k'}$ by surjectivity. Then $v(Z) = \operatorname{covol}(U_k) a / b = \operatorname{covol}(U_{k'}) a / b = v(Z')$. $\square$

The equality of covolumes is a statement on arithmetic groups: when the level is good at every prime, the arithmetic subgroups of the components are conjugate in the adelic group, so their quotients have the same volume.

**Remark 2.16.7 (Formalization).** In the equal volume theorem the assumption `InR D j` that the level is in the range of the family is bound as `hj` and never used ([CompactificationTopChernEqVolume.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CompactificationTopChernEqVolume.lean#L20)), and the parameters `e` and `o` of `Y.Good e o` are arbitrary. The second name at line 50 speaks of a top Chern number, but the conclusion is `EqVolume Y.U`, the equality of `vZero` over the components (Multiplier.lean, line 50); the top degree `topDeg` and `vZero` are in IsHomogeneousCompIdeal.lean (lines 230 and 224). The last paragraph before this remark is the standard reason for the equality of covolumes; we did not read the proof of `complexUniformisation_components_covolume_eq`. In the bad set theorem the hypotheses on the family (`HypothesesX`) already contain the toroidal compactifications for fans, the seminegativity and the statement on Green functions, which are also passed separately; the constant of the level statement is set to $0$ ([CoveringBadLocusOfDescentSteps.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoveringBadLocusOfDescentSteps.lean#L35)). The two parts of that proof are `lifts_badAt_last_of_green_cuspidal` (ExistsLiftAtDefiniteBadPlaces.lean, line 67) and `covers_badAt_of_deep_good_size_flat_degree` (BadComponentsIndefinite.lean, line 69), whose proofs we did not read. In the measure condition the constant $(K_1 + K_2)/2$ comes from `measAt_of` (MeasAtOf.lean, line 28); the sharper $\max(K_1, K_2)/2$ would also do. The ratio `ratAt`, the Gram norm `nrmR` and the Petersson norm `petW` are not unfolded. Both second names are proved by `first | exact ...` from the first names.
