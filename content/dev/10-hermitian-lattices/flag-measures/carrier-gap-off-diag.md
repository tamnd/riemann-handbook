---
id: carrier-gap-off-diag
title: The off-diagonal bound for a selection of spectral ties
kind: theorem
decl: GlobalTheory.CarrierGap.offDiag
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.OffK0Closed
covers: 12991
status: drafted
drafted_by: writer@claude
---
This theorem bounds the off-diagonal entries $K_0(u, u')$ of the spectral ties of a selection, for each family of a class. It is part 2 of [`at_choice_alt`](/entry/at-choice-alt/), which gives it all its inputs from the Siegel-Weil hypothesis. Its proof is short. Most of the work is in Theorem S, which it gets from [`theoremS_leaves_of_carrierG`](/entry/theorem-s-leaves-of-carrier-g/).

## Statement

Let $\mathcal C$ be a family class and $s$ a selection for $\mathcal C$ (`SSel`): for each family $F$ in $\mathcal C$, a threshold $x_0$ and spectral ties $s(F, x, i)$ for each $x > x_1$ with $x \ge x_0$ and each index $i$. Assume:

1. `SWXS`: for each datum $D$ and each Hida setting of $D$, a Siegel-Weil condition `SWa1` and a compatibility of first Chern classes `StabilizerFirstChernCompatibility`. We have not unfolded these two.
2. `RowNGP`: a bound on the rows, eventually in the constants.
3. `RowsFinDim`: for each automorphic datum, each locally constant $e$ and each discrete series $\sigma_v$ with unit vectors of integrable coefficients, the operator integral gives a finite-dimensional space.
4. `LocTied` for each selected datum: at each finite place $p$, the local component is isomorphic to a fixed model.
5. The rank bound `RanksRow 3 𝒞` and the loop row bound `LoopRowS 3 𝒞 s`.

**Theorem.** It is [closed](/step/closed-def/) on $\mathcal C$ that, for each $F$ in $\mathcal C$, eventually in $x$ and under the size hypothesis `AdmissibleBoundsFromSource.hyp` with $C_0 = 3$, for each $x$ above the threshold, each $i$ and all words $u \neq u'$,
$$\|K_0(u,u')\|^2 \le (1 + b^{-6}) \frac{d(u)\, d(u')}{D^*}.$$
Here $K_0(u,u')$ is the sum of the identity, generic and non-generic parts of the term of the ties for $(u, u')$, $b$ is a scale of the size data, and $d$ and $D^*$ are fields of the datum (`duS`, `Dstar`). This is `TheoremSSelected`.

## Proof

1. `hTF_of_ranks` turns the rank bound into the frame bound `TFrame`. With `finXC_of` (from `RowsFinDim` and the decay `WuDecayOfGap`) and `LocTied`, `selOK_of` shows that, eventually, each selected tie satisfies the seven conditions of `STiesOK`.
2. `theoremS_leaves_of_carrierG` gives the 19 hypotheses of Theorem S from `carrierP`, `RowNGP`, `RowsFinDim`, `uniqGap_holds` and `SWXS`. `theoremS_of_conj` gives Theorem S, and `theoremS_distinct_of_closed` keeps its bound for distinct words.
3. `offDiagonalK0_of_rows` combines this bound with step 1, the size rows (`sizesRowS_of`, `hRw_of_ranks`, `thrRow_holds`), the size bound `hA_of_ranks` with `aSz 3`, the loop rows and `absConvTied_holds`.

## In the Lean code

The theorem is at [OffK0Closed.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean#L673). `TheoremSSelected`, `SSel` and `STiesOK` are in [ThmSOwn.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean#L669). `offDiagonalK0_of_rows` and `theoremS_distinct_of_closed` are in [LinkSFinalP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LinkSFinalP.lean#L58).

The lemmas: `hTF_of_ranks`, `selOK_of`, `theoremS_leaves_of_carrierG`, [`carrierP`](/entry/carrier-p/), `theoremS_of_conj`, `theoremS_distinct_of_closed`, `offDiagonalK0_of_rows`.

The proof gets `WuDecayOfGap` twice: from `wuDecayOfGap_holds'`, and again inside step 2 from `wuDecayOfGap_of_uniqGap`. Theorem S also gives a Hilbert-Schmidt bound on the ties, and `theoremS_distinct_of_closed` drops it. The constant $C_0 = 3$ is fixed. $K_0$ leaves out the degenerate part of the term (the words $t$ with $G(t) = 0$ that are not the identity), so the bound is not a bound on the full entry $K(u, u')$.
