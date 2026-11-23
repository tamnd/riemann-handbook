---
id: flat-integrand-local-factor-splits-twist-place
title: The doubling integrand splits off a local factor at a twist place, the statement form
kind: theorem
decl: GlobalTheory.T.flatIntegrand_localFactor_splits_twistPlace
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.FlatIntegrandLocalFactorSplitsTwistPlaceStatement
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [`local_factor`](/entry/local-factor/) and proves it by calling that theorem. Its only user is [`qPeel_holds`](/entry/q-peel-holds/), which calls it once for each twist place.

## Statement

Assume `UnramifiedDoublingGL` and `CuspRapidDecay`. Take the setting of `QPeel D`, and let $\mathcal I_z$ be the doubling integrand `flatInt`, as in the entry for [`qPeel_holds`](/entry/q-peel-holds/). Let $\mathfrak P$ be a twist place over the place $v$ of $F$, and $G_v$ the local group at $v$.

**Theorem.** There are an open subgroup $J \subseteq G_v$, a Haar measure $\mu$ on $G_v$ with $\mu(J) = 1$, and an integrable function $\zeta$ on $G_v$ with $\zeta = 1$ on $J$, such that:

1. the component at $v$ of $g$ lies in the level group if and only if its projection to $G_v$ lies in $J$;
2. at $z = t/2$, $\int \zeta \, d\mu$ equals `blockL c k 𝔓 * zinv 𝔓 t ((k+1)t)`;
3. for $x$ in `intOff c s` with $x_v = 1$ and all $y \in G_v$, $\mathcal I_z(x y) = \zeta(y) \, \mathcal I_z(x)$.

## Proof

The proof is `first | exact @GlobalTheory.ChainTw.OnePlace.local_factor | ...`. It applies that theorem. The statements are identical.

## In the Lean code

The theorem is in [FlatIntegrandLocalFactorSplitsTwistPlaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatIntegrandLocalFactorSplitsTwistPlaceStatement.lean#L21). The target is in [FlatIntegrandLocalFactorSplitsTwistPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatIntegrandLocalFactorSplitsTwistPlace.lean#L164).
