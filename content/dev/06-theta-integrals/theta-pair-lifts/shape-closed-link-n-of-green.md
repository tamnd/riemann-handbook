---
id: shape-closed-link-n-of-green
title: The connectedness statement from Green and the slot hypotheses
kind: theorem
decl: UpperTheory.Top.shape_closed_link_n_of_green
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.TopShape
covers: 9550
status: drafted
drafted_by: writer@claude
---
This theorem turns the statement [Green](/step/green-def/) on cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_g)$ into the long implication `TopShapeAlt`, whose conclusion is the connectedness statement `TopG`. The theorem [ZeroFreeAll from Green, VWin and HypsAlt](/entry/zero-free-all-of-green-v-win/) feeds the 46 fields of `HypsAlt` into the slots of this implication, gets `TopG`, and from it the nonvanishing of $L(s,\psi)$ for primitive $\psi$ and $\operatorname{Re}(s) > \tfrac12$. Below this theorem are 9,550 declarations of the proof.

## Statement

The objects are those of the [theta matching chapter](/proof/theta-matching/). A family $F$ (the type `FamP ε`) has a scale $\varepsilon$, a threshold $x_1$, index sets $I_x$ and data $D(x,i)$ with size data $L(x,i)$. A family class is a predicate on families. For a class $\mathcal{C}$ and a predicate $P$, [`Closed 𝒞 P`](/step/closed-def/) says: there is $\varepsilon_1 > 0$ such that for each $\varepsilon \in (0, \varepsilon_1]$ there are thresholds, and $P$ holds for each family of $\mathcal{C}$ with scale $\varepsilon$ whose constants are above them. Write $\mathcal{D}(\mathcal{A})$ for the class `D3 3 𝒜`: the families of $\mathcal{A}$ with five extra conditions (`WithChN`), a smoothness and a twist condition, a choice `ChosenE` with constant $3$, and the size bounds `TuSize` and `DGamSize`.

`TopG` says: for each $\lambda > 1$ and each requirement $G$, if hosts exist on windows of scale $\lambda$ (`HostExW λ G.req`) and each family in the class $G.\mathrm{cls}(\lambda)$ satisfies `HypV`, then $G.\mathrm{cls}(\lambda)$ is `FamilyClassConnected`. That is: there are $e_D, e_L, \varepsilon_1$ with $\varepsilon_1 > 0$ such that for each $\varepsilon \in (0, \varepsilon_1)$ some family of the class satisfies the inequality `ChainTied` at each large $x$ of its window set.

**Theorem.** Assume `Green`. Let $\mathcal{A}$ be a family class. Assume the 52 hypotheses of `TopShapeAlt True True N TopG` on $\mathcal{A}$, where $N(\mathcal{C})$ is `Closed 𝒞 LinkN`. They are a twist selection and its bundle of choices, a duty condition on each family, conditions on the rows of each selected datum, 17 bounds of the form `Closed …`, some uniform statements (`LitThin`, `WuDecayOfGap`, `RowsFinDim`, mass and genus statements for all data $D$), and the slot $N(\mathcal{D}(\mathcal{A}))$. Then `TopG` holds.

The slot $N(\mathcal{D}(\mathcal{A}))$ says that the bound `LinkN` is closed on $\mathcal{D}(\mathcal{A})$. `LinkN` is a bound on a weighted sum over twisted places, `etaSum`, by the size parameters plus the sum $\sum_l \mathrm{vvTerm}(l)$ of Sha lengths.

## Proof

Fix $\lambda > 1$, a requirement $G$, hosts and `HypV`. The proof applies `topDesWin` with $\mathcal{C} = \mathrm{WithChN}(\mathcal{A})$, $\mathcal{C}' = \mathrm{WithChN}(\mathcal{A} \cap G.\mathrm{cls}(\lambda))$, $\mathcal{E} = G.\mathrm{cls}(\lambda)$, $C_0 = 3$, $C_{\mathrm{abs}} = 2$, $e_D = 2$ and $e_L = 0$. `topDesWin` asks that designs exist in $\mathcal{C}'$ and that nine bounds are closed on $\mathcal{D}(\mathcal{A})$. It then picks a family with large constants and gets `ChainTied` from the nine bounds. The inputs come from these lemmas.

1. Designs exist: `designExists_of_tuSize_aux4n_litThin`, from the slot `hEx` at $(\lambda, G)$, `hTu`, `hn4` and `LitThin`.
2. `LinkN`: the slot $N(\mathcal{D}(\mathcal{A}))$ itself.
3. `LinkEta`: `closed_linkEta_of_duty`, from the duty condition.
4. `LinkIRR`: `closed_linkIRR_of_join_count`, from `Green` and the count bound `irrC`. This is the only use of `Green`. Inside it, `admissibleLabelWeights_of_greenCuspidalParametrisation` gives the condition `admLq` on each datum.
5. `SmallLevelRankEq`: `link_alt_alt_alt`, from the selection and the surjectivity slot `zL`.
6. `LinkDIVt`: `closed_linkDIVt_of_closed_bridge_kernel`, applied to a closed bound `DivisionKernelConstantBounds`. That bound combines `link_brest_alt`, `cut_of_stable`, `wire_sel_alt`, the valuation bound `adm2` from [`closed_family_admissible_twist_link_alt`](/entry/closed-family-admissible-twist-link-alt/), and `selection_closed_of_wu_decay_alt`.
7. `NuFullF` with `MuRank`, and `LinkGLOBAL`: the two parts of `link_gl`, from `tie` and the mass and genus slots.
8. `LinkG`: `closed_linkG_of_duty`, which calls [`linkG_concrete5`](/entry/link-g-concrete5/).
9. `LinkS`: `link_alt_alt_bis`.

The rest is bookkeeping: inclusions between the classes, and `Closed.and` to join bounds.

## In the Lean code

The theorem is in [TopShape.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean#L33). `TopShapeAlt` is in [TopShapeAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShapeAlt.lean#L24), `topDesWin` in [DesWin.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean#L11), `TopG` in [ZeroFreeAllOfTopG.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean#L12), and `LinkN` in [GlobalTheoremInputs.lean](lean:Formalism/SharpRestriction/GlobalTheoremInputs.lean#L45).

The name says "closed LinkN", but the theorem does not prove that `LinkN` is closed. It takes this as the slot `nRest` and passes it to `topDesWin` unchanged. The content of `LinkN` comes from `HypsAlt` in the caller.

The slots `hVC : V` and `nR : NR` are never used. Here both are `True`. All other slots are used, but we have not checked which of them carry real content. We have not unfolded `ChainTied`, `HypV`, `LinkGLOBAL` or `LinkS`.
