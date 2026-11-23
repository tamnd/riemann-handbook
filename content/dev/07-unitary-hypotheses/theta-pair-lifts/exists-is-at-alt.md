---
id: exists-is-at-alt
title: A matching translation element for each placed framed Bessel datum
kind: theorem
decl: GlobalTheory.MiTop.exists_isAt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsIsAt
covers: 448
status: drafted
drafted_by: writer@claude
---
This theorem finds, for one placed and framed Bessel datum, two elements $a_0, a$ of $G(X_0)$ whose translation element conjugates the level group $J$ of $Y_0$ onto the row level group. Its second name [`exists_isAt_of_placed_framed`](/entry/exists-is-at-of-placed-framed/) is called twice by [`exists_botDat_pin_of_placed_of_framed`](/entry/exists-bot-dat-pin-of-placed-of-framed/), in steps 1 and 5 of its proof. We use the notation of that entry: $G(V)$, $G_f(V)$, $x_u$, $\iota_{\mathcal B}$, $J$ = `rJ_z W` and $\chi$ = `realCharacter W`.

## Statement

Let $W$ be a real package over $D$ with `PackageHypotheses W`, $u$ a word, $f$ a family character and $\mathcal B$ a Bessel datum on $X_0$. For $a_0, a \in G(X_0)$ the translation element is $t = x_u^{-1}\, \iota_{\mathcal B}(a_0 a)\, f.g.b_0$. $J$ is the level subgroup `levS` of $Y_0$ for the frame $\beta_Y^0$ and the level datum $\Lambda_0$ = `datZero_alt W`, and $\chi$ is its character `levChi`. The row group $J'$ = `rowJ` is the set of $k$ with $\iota_X(k) = (1, k_2)$ and $k_2$ in the set `K2` of the Hida setting `W.S.X`, and $\chi'$ = `rowChi` is $k \mapsto \overline{\chi_2(k_2)}$.

**Theorem.** If $\mathcal B$ is placed for $f$ (`PlacedAlt f B`) and framed, there are $a_0, a$ such that `IsTranslate' f B a₀ a` holds:

1. $a_0$ is a transport adelic correction for `W.S.tr u`;
2. $a \in G_f(X_0)$ and $a$ is central in $G(X_0)$;
3. $t \in G_f(Y_0)$, and for each $k \in G(Y_0)$: $k \in J$ if and only if $t k t^{-1} \in J'$, and then $\chi'(t k t^{-1}) = \chi(k)$ (`Matches J χ t`).

## Proof

1. `exists_transport_adelic_correction` gives $a_0$.
2. `exists_central_stab_of_transport_correction` (from the package hypotheses, placed and framed) gives a central $a \in G_f(X_0)$ with the stabiliser condition: for $\kappa \in G(Y_0)$, $\kappa \in G_f(Y_0)$ and the finite part of $\kappa$ lies in the group `St` of the frame $\beta_t$ = `frameAtTranslate`, if and only if $\iota_X(\kappa) = (1, \kappa_2)$ with $\kappa_2$ in the set `Kset` of the instance `W.S.X.B.I`. We have not unfolded `K2`. The proof (line 62) reads a member of `K2` as a pair whose first part is membership in `Kset`.
3. Each factor of $t$ is in $G_f(Y_0)$: $x_u$ by `iotaX_fst_eq_one_iff`, $\iota_{\mathcal B}(a_0 a)$ by `embA_mem_GfC`, and $f.g.b_0$ by the fields `b` of the placed conditions.
4. `levS_conj_frame` says that conjugation by $t$ maps $J$ onto the level group for the frame $\beta_t = t\,\beta_Y^0$, with the same character. `oneBlock_lev` writes membership in that group as three conditions: $\kappa \in G_f(Y_0)$, the finite part of $\kappa$ in `St` of $\beta_t$, and a reduced tuple `rTup` lies in the subgroup $H$ of $\Lambda_0$. It also writes the character as the extension `ext1` of the character of $\Lambda_0$.
5. `central_adapted_element_property_alt` says that, under the first two conditions, $\kappa \in J'$ if and only if the third holds. `central_adapted_element_value_alt` says that then $\chi'(\kappa)$ is the value of `ext1`. With step 2 this gives clause 3.

## In the Lean code

The theorem is at [ExistsIsAt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsAt.lean#L32). `PlacedAlt`, `translationElement` and `IsTranslate'` are in [Placed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Placed.lean#L29), `Matches` in [ThetaIdentityOfMapsAll.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L72), `ConjLevel` in [EvalTieTOne.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/EvalTieTOne.lean#L14). The hypothesis `Framed` is used only by `exists_central_stab_of_transport_correction`. `oneBlock_lev` needs $\Lambda_0.s = 0$ and $\Lambda_0.Q = \emptyset$; the proof gives both by `rfl`. We have not unfolded `IsTransportAdelicCorrection`, `St` or `rTup`. A parallel copy for `RealPack`, `exists_isAt`, is in [ExistsPlacedBesselPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsPlacedBesselPoints.lean#L47).
