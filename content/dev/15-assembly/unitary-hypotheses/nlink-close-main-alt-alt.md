---
id: nlink-close-main-alt-alt
title: The fifteen local bounds of ConclF along a family
kind: theorem
decl: GlobalTheory.NLinkClose.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsFurtherTail
covers: 9872
status: drafted
drafted_by: writer@claude
---
This theorem proves `ConclF F`: at each large member of a family $F$ there is hub data that satisfies fifteen local bounds with one constant. `LinkFam.main` turns `ConclF` into the bound `LinkN` of the field `nRest` of `HypsAlt` (see the [unitary hypotheses chapter](/proof/unitary-hypotheses/)). The theorem is called through its [statement form](/entry/concl-f-of-family-facts-and-bound-at-two-three/), by [LinkN for one family](/entry/link-n-of-tw-good-galois-preconditions/). Below it are 9,872 declarations.

## Statement

Let $F$ be a family with threshold $x_1$, and for $x > x_1$ and $i \in I_x$ let $D$, $L$, $P$ be the datum, size data and parameter choice of the member. For a local index $i$ of $D$ let $\ell_i$ be its prime. For a point $\pi$ and a real $b$, let $\mathrm{Bd}(i,\pi,b)$ be the inequality

$$v(i,\pi) \le s(i,\rho_i,\pi) + b + V(\ell_i) + v_{\ell_i}(h_E) + \epsilon(\ell_i),$$

with named quantities $v, s, V, \epsilon$ that we have not unfolded. Let $m(C) = C f m b \log x + C x^C \lambda^2$ (`midF`), with numbers $f, m, b, \lambda$ of the member.

Assume `Hypotheses₂` (seven named published inputs), $C \ge 0$, $C_T \in \mathbb{N}$, and:

1. `TwGood F`: eventually, a twist condition at each member.
2. `FactsFAlt F C CT`: for $x > x_1$, `NormChoiceFacts`, a commuting endomorphism condition and a paired character condition with constants $C, C_T$.
3. `BoundAtTwoThreeFamilyFonAlt F`: there are $C_a, x_a$ such that for $x \ge x_a$ and all hub data $X$ in setup (`SetupAlt`), $\mathrm{Bd}(i,\pi,m(C_a))$ holds at each twisted index with $\ell_i = 2$, or $\ell_i = 3$ not small, and each good point $\pi$.

Then there are $C_s$ and $x_0$ such that for $x \ge x_0$, $x > x_1$, and each $i$ with `ShaFinOdd`, there is hub data $X$ (homomorphisms $r, \rho$ from a group $G_E$ to matrix groups, length tables, error bounds, an excluded set of primes) with `Concl L P X Cs`. Its fields:

- **Bounds $\mathrm{Bd}$ by prime range**, at twisted indices and good points, each with its own $b$: `two` ($\ell_i$ small or $3$), `ram` ($\ell_i \in \{q,d\}$), `mid` (the middle range, [StarAD](/entry/star-ad-and-bb-le-of-joint-cond/)), `large` ($\ell_i$ above a cutoff $\ell^*$, not excluded, $b = 0$).
- **Other bounds**: `bb` (error bound $\le C_s f n t^2 n_V \lambda^2$), `typ` (at the primes $g_0, g_1$), `mult` (multiplicity at most rank), `exc` (few excluded primes, each at most $3b$), `small`, `num` (five table bounds), `par`.
- **Side facts**: $C_s \ge 0$, `pass`, `rank`, `kill`.

## Proof

1. **Constants.** `theoremE_corollaryA_closing_all_data` gives $C_0$ with `Conclusion2 D C₂` for $C_2 \ge C_0$; put $C_2 = \max(C_0, 1)$. More constants come from [`embedding_jumps_aux2_of_setup`](/entry/embedding-jumps-aux2-of-setup/), `admissible_parameters_family_const` ($C_1$), hypothesis 3 ($C_a$) and `starSF_of_prints` ($C_b$, for the other small primes). $C_s$ is the maximum of these, $3C_2 + 1$, $2000(C+1) + 5C_1$, $C_T$ and $22365$.
2. **Thresholds** come from `exists_hubData_admJ_setup` (hub data in setup), `excludedPrimes_few_and_small_along_family`, `specialPrimes_small_along_family`, [`eventually_congBound_of_facts`](/entry/eventually-cong-bound-of-facts/) and `fam_jointBCD_closed_alt` (joint hub conditions).
3. **Fields.** `mid` and `bb` (constant 7200): [`star_ad_and_bb_le_of_joint_cond`](/entry/star-ad-and-bb-le-of-joint-cond/). `two`: `starF_of`, from hypothesis 3 and $C_b$. `typ`: `star_bound_of_paired_character_condition`. `large`: `localBoundZeroAtLargePrimes_of_congruenceBound`. `ram`: `starG_of_thmB`. `mult`: `goodPointMultiplicityLeRank_proof`. `num`: `RowA.main` and three table lemmas. `sizeConditions_mono` raises the constants to $C_s$. The rest is bookkeeping.

## In the Lean code

The theorem is in [ImportsFurtherTail.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTail.lean#L22); `ConclF` and `Concl` are in [BoundAtTwoThreeFamily.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/BoundAtTwoThreeFamily.lean#L120).

All hypotheses are used. The number $22365$ is $K_3$ of `rowC C₂`, that is $3 \cdot 23 \cdot 320 + 12 \cdot 23 + 9$; `RowK.Le` needs it. The local name `ComplexParameterFamilyContinuity` ([line 30](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTail.lean#L30)) is only the real number $\max(0, C_a, C_b)$. The caller proves hypothesis 3 from `Hypotheses₂` alone, with `at23_family_alt`.
