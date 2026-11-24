---
title: From level three to level four
decls:
  - GlobalTheory.T.has4_of_has3_of_lv3Mv
  - GlobalTheory.Mem.SRe.UpS.has4_of_has3_of_sExt_none
  - GlobalTheory.Mem.SRe.exists_sPack_integrable_alt
  - GlobalTheory.T.local_bessel_uniqueness_holds
  - UpperTheory.Lit.exists_spectralData_gap_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## From level three to level four

This section proves the step from level three to level four: for all large contexts, each pinned column datum that has a level three object also has a level four object. The closing theorem of Section 2 uses this step twice, once for the scale $s(N)$ and once for $s(N_g)$. The step needs five facts. Four of them follow at once from the literature hypotheses. The fifth is the existence of an $S$-pack whose archimedean matrix coefficient is integrable, and most of the section builds it. It comes from the spectral setting of a datum whose Harish-Chandra parameters have large gaps. The gap is what makes the Bessel models of the discrete series unique, and that uniqueness gives the decay of the coefficient.

Let $D$ be a datum of the volume: a CM field $E$ with its maximal totally real subfield $F$, a hermitian space over $E$ of rank $r$ with $m$ blocks, and at each archimedean place $\tau$ a Harish-Chandra parameter $b(\tau)$ of a discrete series of the unitary group at $\tau$.

**Definition 6.3.1 (Gap condition and local ties).** The datum $D$ satisfies the *gap condition* if $r \ge 1801$ and, at each archimedean place $\tau$,

$$b_{j+1}(\tau) - b_j(\tau) \ge 16\, r^{19} \quad \text{for each } j \text{ with } j + 1 < m.$$

The datum $D$ is *locally tied* if at each finite place there is a local isomorphism between the two local data of $D$ at that place.

**Definition 6.3.2 (Hida setting and transports).** A *Hida setting* $X$ for $D$ is a unitary group over $F$ whose CM field is identified with $E$, with a basis, a lattice and a discrete series $\sigma_v$ with a chosen vector $w_v$ and formal degree $d_v$ at each infinite place $v$. Its *archimedean coefficient* is the function on $G_\infty = \prod_{v \mid \infty} G_v$ given by

$$\varphi_X(g) = \Bigl(\prod_{v \mid \infty} d_v\Bigr) \cdot \overline{\prod_{v \mid \infty} \langle w_v, \sigma_v(g_v) w_v \rangle}.$$

A *full datum* $Y$ over $X$ is a level character, row representatives and column systems. Let $F$ give a form of $D$ for each word $u$. A *transport* of $X$ to the form $F(u)$ is an isometry of the hermitian space of $D$ that sends the hyperbolic vectors of $X$ to those of $F(u)$; it matches the level of $Y$ with the level of $F(u)$, and its column dictionary maps into the right space, is bijective and is an isometry.

**Definition 6.3.3 (S-pack).** An *$S$-pack* for $(D, F)$ consists of a Hida setting $X$ for $D$ with the instance of $D$ and the identity identification of fields, an isomorphism of adelic groups, a full datum $Y$ over $X$ with the finiteness record, an additive character $\psi$ of $\mathbb{A}_F$ with

$$\psi_\infty(x) = \exp\Bigl(2 \pi i \sum_{w \mid \infty} \operatorname{Re} x_w\Bigr),$$

compatible with the measures, a transport for each word $u$ with the properties above, and a record of good operators of $X$.

We take as given two published statements: the convergence of the Siegel-Weil integral for unitary groups, and the finite dimension of the rows. The first gives the measures and the volumes of the setting. The second gives the finiteness record.

**Theorem 6.3.4 (Spectral setting of a datum with large gaps).** Assume the convergence of the Siegel-Weil integral for unitary groups and the finite dimension of the rows. Let $D$ be a datum with the gap condition that is locally tied, and let $F$ give a form of $D$ for each word. Then there are a Hida setting $X$ for $D$, an isomorphism of adelic groups $h$, an additive character $\psi$ of $\mathbb{A}_F$, a full datum $Y$ over $X$ with the finiteness record, and a transport $t_u$ of $X$ to $F(u)$ for each word $u$, such that:

1. the instance of $X$ is the instance of $D$, and the identification of the CM fields is the identity;
2. the measures of $X$ are tied through $h$;
3. $\psi$ is a character with $\psi_\infty(x) = \exp(2 \pi i \sum_w \operatorname{Re} x_w)$;
4. $\psi$ is compatible with the mass data and, at each word, with the local volumes;
5. the archimedean coefficient $\varphi_X$ is integrable on $G_\infty$;
6. for each $u$, the transport $t_u$ matches the levels, and its column dictionary maps into the right space, is bijective and is an isometry.

Lean: `UpperTheory.Lit.exists_spectralData_gap_alt` (also `GlobalTheory.T.local_bessel_uniqueness_holds`, a second name).

*Proof.* There are five steps.

1. [The existence of a global setting](/entry/exists-setting/) takes the Siegel-Weil convergence and the gap condition. It gives $X$, $h$ and $\psi$ with properties 1 to 4, and for each level character and each word a transport that matches the levels.
2. Since $D$ is locally tied, there is a full datum $Y$ over $X$.
3. The gap condition gives the decay of the coefficients of $X$ and property 5. Here the gap is used through the uniqueness of Bessel maps: for a discrete series of a unitary group of size $2r + k + 1$ with $k \ge 1$ whose parameter gaps $h$ satisfy $h \ge 120 (2r + k + 1)^3$, any two Bessel maps are linearly dependent on smooth vectors. The gap $16 r^{19}$ is far above this bound for $r \ge 1801$.
4. The finite dimension of the rows and the decay of step 3 give the finiteness record of $Y$.
5. Choose $t_u$ among the transports of step 1 at the level character of $Y$. The column dictionary is a core of the stabilizer of the column level, which is trivial, so it has the three properties of item 6.

This proves the theorem. $\square$

**Theorem 6.3.5 (Integrable S-pack).** Assume the convergence of the Siegel-Weil integral for unitary groups and the finite dimension of the rows. Let $D$ be a datum with the gap condition that is locally tied, and let $F$ give a form of $D$ for each word. Then there is an $S$-pack $P$ for $(D, F)$ whose archimedean coefficient $\varphi_P$ is integrable on $G_\infty$ for the Haar measure of the setting.

Lean: `GlobalTheory.Mem.SRe.exists_sPack_integrable_alt`.

*Proof.* [The spectral setting](/entry/exists-spectral-data-gap-alt/) gives all parts of an $S$-pack except the record of good operators, and gives the integrability. The record of good operators exists for every Hida setting of $D$, with no hypothesis. $\square$

Now the step. Let $h_L$ be a recursion datum and $p$ a parameter set over $h_L$ with scale $s$. Recall from Section 1 the column step $\mathrm{Step}_w$, the properties $\mathrm{Has}_3(s)$ and $\mathrm{Has}_4(s)$, and the level three condition. A level three object at a stage $Z$ consists of a group condition, a cohomology datum, a set of places, a row table, a norm choice, theta data, values $\chi_T(j) = x^{2(j+1)}$ for a unit $x$ of order $g_k - 1$ modulo $g_k$, and elements of the position slot and of the norm choice slot. A level four object adds column data at split primes, a real tie, two equalities of scale constants and an element of the $S$-slot.

**Theorem 6.3.6 (From level three to level four).** Assume the following statements from the literature: the infinitesimal characters of discrete series, the finiteness theorem of Harish-Chandra, rapid decay of cusp forms, uniqueness of discrete series of $U(p,q)$, finite dimension of the rows, convergence of the Siegel-Weil integral for unitary groups, existence of discrete series, a formal degree formula and the Siegel mass ratio for CM fields. Let $h_L$ be a recursion datum and $p$ a parameter set over $h_L$ whose $S$-extension is trivial and whose scale $s$ satisfies the level three condition. Then

$$\mathrm{Step}_w\bigl(\text{pinned} \wedge \mathrm{Has}_3(s),\ \mathrm{Has}_4(s)\bigr).$$

Lean: `GlobalTheory.Mem.SRe.UpS.has4_of_has3_of_sExt_none` (also `GlobalTheory.T.has4_of_has3_of_lv3Mv`, a second name).

*Proof.* We use five facts.

1. Saturation at new stages: from the first five statements of the list, there are spectral objects over the replaced stages.
2. The real tie: from the existence of discrete series and the formal degree formula.
3. The existence of an integrable $S$-pack for each datum with the gap condition that is locally tied: this is [the Theorem on integrable S-packs](/entry/exists-s-pack-integrable-alt/), with the Siegel-Weil convergence and the finite dimension of the rows.
4. Volumes equal masses: from the volume ratio that the Siegel-Weil convergence gives.
5. The good idempotent of the real Harish-Chandra series is fixed. This holds with no hypothesis.

Let $K$ be a large context and $w$ a pinned column datum with a level three object at a stage $Z$. For large contexts, the gap condition holds at the data of the construction. We choose a new $S$-stage and move the object to it by the level three condition. At the new stage, fact 3 gives an $S$-pack, fact 2 gives the real tie, fact 4 gives the equality of the scale constants with their standard values, and fact 5 gives the idempotent. Fact 1 gives a new stage again, the level three condition moves the object once more, and the saturated column gives the element of the $S$-slot. Since the $S$-extension is trivial, its extra datum is the unique element of the one point type. This is a level four object at $w$. $\square$

**Remark 6.3.7 (Formalization).** The theorems are at [LevelThreeToFour.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelThreeToFour.lean#L19) (the second name at line 29), [ExistsSPackIntegrable.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ExistsSPackIntegrable.lean#L10), [LocalBesselUniquenessHolds.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/LocalBesselUniquenessHolds.lean#L9) and [BesselSpectral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BesselSpectral.lean#L12). In the step theorem the hypothesis `SiegelMassRatioCM` and the recursion datum are bound to `_` (line 20), so the mass ratio is not used. The fact `goodIdempotent_real_of_harishChandra_series` uses no Harish-Chandra hypothesis. The name `local_bessel_uniqueness_holds` is misleading: its statement is an existence statement with no uniqueness; the uniqueness of Bessel maps (`besselMapUniqGap`) enters only the proof of `wuDecayOfGap_holds'`. The older forms `stepW_has4`, `exists_sPack_integrable` and `exists_spectralData` take the hypothesis `BesselMapUniq`; these forms replace it by the proved gap form. The letters `lv3Mv` suggest "level three move", which fits the level three condition. We did not unfold `LocTied`, `MeasTie`, `MeasCompatψ`, `LocCompatX`, `GoodOp`, `FinX`, `Full`, `Lv3`, `Lv4` or the passage `wuDecayOfGap_of_uniqGap` from the gap condition to the gap of `besselMapUniqGap`, so step 3 of the first proof states only what these lemmas give.
