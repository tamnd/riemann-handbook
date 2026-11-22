---
id: thm-pactual-cpt-of-r
title: The compact form of Theorem P from the radial operators
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_R
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutSETopR
covers: 1227
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThmPActualCpt`, the compact form of Theorem P, from two facts about radial operators, `RDSOpR` and `RDSOpRv`. Its only user is [the compact form of Theorem P](/entry/actual-compact-theorem/), which proves the two facts and states `ThmPActualCpt` in full. Below this theorem are 1,227 declarations. The proof here is two lines: it passes the hypotheses to larger lemmas.

## Statement

Use the setting of [the compact form of Theorem P](/entry/actual-compact-theorem/): the group $G$, the radial space $\mathcal{R}$, the restriction `resG` to the last level and the domain `DomR`. Fix data with `IsData`, $1 \le l_0 \le k$, a real place datum $D$ with the same $z, z', \pi, \pi'$, and $r > 0$. A differential operator $\Theta$ on $G$ (`B.DiffOp`) is a finite sum of terms $T(g)\, R_w F(g)$, where $T(g)$ is a coefficient and $R_w$ is the right action of a word $w$ in the Lie algebra. We have not unfolded $R_w$. `OpProp1` says that the coefficients of $\Theta$ are smooth on $\{G_f > 0\}$, commute with the action of $D$, have polynomial bounds, and that $\Theta$ and its formal adjoint keep the class `NiceAll`.

`RDSOpR` says: for each real $Y$ with $Y - 1$, $Y$, $Y + 1$ in the set `st.inv`, there is $\Theta$ with `OpProp1` such that

$$\mathrm{resG}(\Theta J) = G_i\, \xi(Y)\, R_h(Y)\, \mathrm{resG}(J) \quad \text{on DomR}$$

for each $J$ in the class `FFl`. Here $G_i$ is `GiR`, the product of three elements `Dri`, `Drbi`, `GGi` of the level data, $\xi(Y)$ is `st.xi Y`, and $R_h(Y)$ is `RhR`, built from the entries of the matrix `st.QQ Y` and operators of the level data. `RDSOpRv` says the same for $G_i\, \xi(Y + 1)\, R_{hv}(Y + 1)$ (`RhvR`).

**Theorem.** `RDSOpR` and `RDSOpRv` imply `ThmPActualCpt`.

## Proof

1. `rDIdentSpec_of_R` proves `RDIdentSpec`. It calls `rDIdentSpec_of_open` with the two hypotheses and six proved lemmas: the operators for `Ahat` and `Ahatv` (`spectral_operator_A`, `spectral_operator_A_adjoint`), `spectral_pairing_adjoint`, `spectral_quadratic_adjoint`, `spectral_xi_test` and `spectral_pairing_identity`. That lemma adds seven more and calls `rDIdentSpec_of_cut`. The proof of `rDIdentSpec_of_cut` picks a real $Y$ with $Y - 1, Y, Y + 1 \in$ `st.inv` (`spectral_Y_real`). It takes four operators $\Theta_0, \dots, \Theta_3$, one from each input. `rAdj_thR` shows that each radial operator in the list is adjoint to its partner for the inner product `radIp` on $\mathcal{R}$. From this, `rds_adj_of_apply` shows that the formal adjoint $\Theta_j^*$ acts on restrictions by that partner.
2. `RDIdentSpec` says: there are a real $Y$ with $Y, Y + 1 \in$ `st.inv` and four operators with the properties `RDOpsProp` (`OpProp1` for each) such that $\Theta_j$ and $\Theta_j^*$ act on restrictions as the $j$-th entry of `thR` and its adjoint. The four entries are $\hat{A}_v(Y + 1)$, $G_i \xi(Y) R_h(Y)$, $G_i \xi(Y + 1) R_{hv}(Y + 1)$ and $\hat{A}(Y)$.
3. `thmPActualCpt_of_spec` gives `ThmPActualCpt` from `RDIdentSpec`. It turns `RDIdentSpec` into `RadDecay` (`radDecay_of_spec`, through `radial_identity_of_spectral_data`). This step lifts the four operators to a group identity $s \cdot w_s J = \Theta_0^*(w_s \Theta_1 J) - \Theta_2^*(w_s \Theta_3 J)$ (`RDGrpIdProp`). Then `thmPActualCpt_of_leaves` combines `RadDecay` with `one_letter_density_estimate` and `density_smooth_class`.

We have not unfolded `RadDecay`, `OneLetterDens`, `DensSmoothCls` or the wave operator $w_s$ (`wvG`).

## In the Lean code

The theorem is at [CutSETopR.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSETopR.lean#L14). The lemmas it calls:

- `rDIdentSpec_of_R`, in the same file at line 11.
- `rDIdentSpec_of_open` in [CutSERDIdentSpecAsm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSERDIdentSpecAsm.lean#L12), and `rDIdentSpec_of_cut` in [CutSERDIdentSpec.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSERDIdentSpec.lean#L410).
- `thmPActualCpt_of_spec` in [CutSE_TopSpec.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSE_TopSpec.lean#L13).

`RDSOpR` and `RDSOpRv` ask for $Y - 1 \in$ `st.inv`, but `RDIdentSpec` does not keep this condition.
