---
id: exists-spectral-data-gap-alt
title: The spectral setting of a datum with large gaps
kind: theorem
decl: UpperTheory.Lit.exists_spectralData_gap_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.BesselSpectral
covers: 1859
status: drafted
drafted_by: writer@claude
---
This theorem builds the spectral setting of a datum: a Hida setting with a full datum, transports for each word, and an integrable archimedean coefficient. It is the content behind [`local_bessel_uniqueness_holds`](/entry/local-bessel-uniqueness-holds/) (a copy) and [`exists_sPack_integrable_alt`](/entry/exists-s-pack-integrable-alt/) (a repacking), which feed [the step from level three to level four](/entry/has4-of-has3-of-s-ext-none/). Below this theorem are 1,859 declarations.

## Statement

**Theorem.** Assume `SiegelWeilUnitaryConvergent` and `RowsFinDim`. Let $D$ be a datum (`D7`), and let $F$ give a form `Forms0 D u` for each word $u$. Suppose `GapHyp D` (the rank is $r \ge 1801$, and consecutive Harish-Chandra parameters at each archimedean place differ by at least $16 r^{19}$) and `LocTied D` (a local isomorphism at each finite place, not unfolded). Then there are

- a Hida setting $X$ for $D$ and an isomorphism of adelic groups $h_b$ (`AdBridgeIso`),
- an additive character $\psi$ of $\mathbb{A}_F$,
- a full datum $Y$ over $X$, with the finiteness record `FinX Y`,
- for each word $u$ a transport $t_u$ of $X$ to the form $F(u)$,

with these properties:

1. the instance of $X$ is `instOf D`, and the identification of the CM fields is the identity;
2. `MeasTie`: a tie of the measures of $X$ through $h_b$ (not unfolded);
3. $\psi$ is a character, and $\psi_\infty(x) = \exp\bigl(2\pi i \sum_w \operatorname{Re} x_w\bigr)$;
4. $\psi$ is compatible with the mass data and, at each word, with the local volumes (`MeasCompatψ`, `LocCompatX`, not unfolded);
5. $\varphi_X(g) = \bigl(\prod_v d_v\bigr) \overline{\prod_v \langle w_v, \sigma_v(g_v) w_v\rangle}$ is integrable on $G_\infty$, where $d_v$ is the formal degree of the discrete series $\sigma_v$;
6. for each $u$, $t_u$ matches the level of $Y$ with the level of $F(u)$, and its column dictionary maps into the right space, is bijective and is an isometry.

## Proof

The proof has five steps.

1. [`exists_setting`](/entry/exists-setting/) takes `SiegelWeilUnitaryConvergent` and `GapHyp D`. It gives $X$, $h_b$, $\psi$ and properties 1 to 4. It also gives, for each level character and each word, a transport with the level match.
2. `fullExists_of_locTied` takes `LocTied D` and gives $Y$.
3. `wuDecayOfGap_holds'` takes `GapHyp D` and gives `WuDecay X` and property 5. It is proved in the code from `besselMapUniqGap`. That statement says: for a discrete series of a group of size $2r + k + 1$ with $k \ge 1$ and parameter gaps $h \ge 120 (2r+k+1)^3$, any two Bessel maps are linearly dependent on smooth vectors. We have not followed its proof.
4. `finX_of_decay` takes `RowsFinDim` and step 3, and gives `FinX Y`.
5. The proof chooses $t_u$ from step 1 at the level character of $Y$. Then `colDictCore_holds`, with `columnLevel_stabTriv`, gives the three properties of the column dictionary.

The rest is bookkeeping.

## In the Lean code

The theorem is in [BesselSpectral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BesselSpectral.lean#L12). The lemmas it calls:

- `exists_setting` in [ExistsGlobalSetting.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsGlobalSetting.lean#L45).
- `fullExists_of_locTied`, `finX_of_decay`, `colDictCore_holds`, `columnLevel_stabTriv`.
- `CompanionTheory.Lime.BM.wuDecayOfGap_holds'` in [MultiplicityOneUnitaryBranchingOfGapHyp.lean](lean:CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/MultiplicityOneUnitaryBranchingOfGapHyp.lean#L12), and `besselMapUniqGap` in [BesselMapUniqGap.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/BesselMapUniqGap.lean#L252).

The version without `_gap_alt`, [`exists_spectralData`](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsGlobalSetting.lean#L71), has the same conclusion and the same proof, with one more hypothesis `BesselMapUniq`. It uses that hypothesis in step 3. This version replaces it with the proved gap form. The passage from `GapHyp` to the gap condition of `besselMapUniqGap` is in `wuDecayOfGap_of_uniqGap`, which we have not unfolded.
