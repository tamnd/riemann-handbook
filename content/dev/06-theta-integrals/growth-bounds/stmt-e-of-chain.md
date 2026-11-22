---
id: stmt-e-of-chain
title: Statement E from the chain bound
kind: theorem
decl: Formalism.MainNotions.PairMembershipBlocks.stmtE_of_chain
module: Formalism.SharpRestriction.GrowthBounds.PlaneCoefficients
covers: 1940
status: drafted
drafted_by: writer@claude
---
This theorem reduces [Statement E](/entry/stmt-e/) to one valuation bound, the chain bound `RestChain`. It proves a second bound, the link bound `RestLink`, pairs the two into the plane bound `RestPl`, and applies [Statement E from the plane bound](/entry/stmt-e-of-pl/). Its only user is [Statement E](/entry/stmt-e/), which proves `RestChain`. The real content is further down, in [Statement E from the last steps](/entry/stmt-e-of-last/).

## Statement

**Theorem.** Let $D$ be a datum of the type `D7`. If `RestChain` holds, then `ClosedFormOfAdmitted D` holds.

`ClosedFormOfAdmitted D` is stated in [Statement E](/entry/stmt-e/). `RestChain` and `RestLink` have the same hypotheses. Fix a prime $p$, a discrete valuation ring $O$ whose fraction field has characteristic $0$, integers $n'$ (even), $r$, $K$, $m$ with $m + 1 = r + K$, valid frames `Fr`, an integer $J \ge 2$ and signed chain data `Dt` tied to `Fr`. Take polynomials $A(i)$ over $O$, each in the variables of the letters of `Fr` at $i$, a label $l$, an exponent $\gamma$ with `PlaneEven`, and reals $t(j,u)$ that bound from below the valuations `valS` of $A(j)$ on initial sets of letters. Take a multidegree $d$. Let $Z$ be the part of multidegree $d$ (`compD d`) of the polynomial `levP (zPl A l γ)`, which is built from the product of the $A(j)$ and the monomials $l$ and $\gamma$. Then:

- `RestChain`: for each $\rho'$, each $j \in \mathbb{Z}/J$ and each $i$ below the chain length at $j$, the valuation of `Dt.Fdig ρ' Z` on the chain letters `chainML j i` is at least $t(j, i)$;
- `RestLink`: for each $j$ and each $\mu$ with $\mu + 2 \le r$, the valuation of $Z$ on the letters `TSet j μ` is at least $t(j, n_L(j) + r - 1 - \mu)$ minus a degree term `dwB`.

`RestPl` is the conjunction of the two conclusions, under the same hypotheses. Here `valS` is the valuation that [Statement E](/entry/stmt-e/) describes. We have not unfolded `zPl`, `levP`, `Fdig` or `dwB` past this level.

## Proof

1. `restLink` proves `RestLink` outright, by `level_link_of_degree_letters linkL lkDeg lkVars`. That theorem calls `restLink_of` with the proved facts `valNN`, `homDec`, `restTr` and the weight bound `lkW`.
2. `restPl_of_restChain_of_restLink` gives `RestPl` from the two bounds. It takes the hypotheses once and returns the pair of conclusions.
3. `stmtE_of_pl D` gives `ClosedFormOfAdmitted D` from `RestPl`.

## In the Lean code

The theorem is at [PlaneCoefficients.lean line 59](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients.lean#L59). `restLink` is at line 57, and the private pairing lemma at line 52. `RestChain` and `RestLink` are in [RestPlOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/RestPlOf.lean#L55), at lines 72 and 55. `RestPl` is in [PlaneCoeffOneTTens.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/PlaneCoeffOneTTens.lean#L159).

- The theorem is a reduction. Its hypothesis `RestChain` is proved by `restChain` in [Statement E](/entry/stmt-e/), and the only work here is the proof of `RestLink`.
- The hypothesis does not depend on $D$, and neither does the proof of `RestLink`.
