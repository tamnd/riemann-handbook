---
id: cut-leaves-deep-outright
title: The three deep inputs of the local cut hold outright
kind: theorem
decl: Formalism.L2.SG.Closed.CutLeavesDeep_outright
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedVolumeStatements.CutLeavesDeepOutright
covers: 1115
status: drafted
drafted_by: writer@claude
---
This theorem proves the hypothesis of [the row datum from the deep inputs](/entry/rows-datum-p-of-deep/) for every datum $D$, with no condition. So the three "deep" inputs of [the local cut](/entry/cut-at-of-deep/) are not hypotheses of the proof. Its only user is [the theorem S leaves from the carrier gap](/entry/theorem-s-leaves-of-carrier-g/), which passes it to `rowsDatumP_of_deep`.

## Statement

Let $D$ be a datum of the unitary setting.

**Theorem.** $\mathrm{CutLeavesDeep}(D)$ holds.

$\mathrm{CutLeavesDeep}(D)$ says: assume the signature condition for the hermitian space $V$ of $D$. Let $(\delta, M)$ be local data that agree with $D$ at every finite place, let $L$ be a local space, and let $u, u'$ be words with $T_u \equiv T_{u'} \pmod{g_S^2}$ that satisfy the prime hypothesis. Let $\mathcal{W}$ be a set of row representatives for a flag $F_0$. Then:

1. `StepsU`: for each term and each place $p$, a local index ratio has the value given by a weight (`CountAt`), and a unimodularity condition holds (`UnimodAt`);
2. `StabApprox`: if local unitriangular integral matrices move a given matrix at every $p$, then global ones exist that do the same and are integral at every $p$;
3. `FStarC`: for an eligible term $\gamma$ and a point $w'$ of the same kind, the partner set of $\gamma$ is in bijection with a set of global lattices that agree with prescribed local lattices at almost all $p$.

## Proof

The proof is `cutLeavesDeep_of_betaInt D`, applied to `betaInt_holds`.

- `StepsU` comes from `CountAt.countAt_holds` and `ProdEP2Uni.unimodAt_holds`.
- `StabApprox` comes from `TupGlobApprox.stabApprox`, a global approximation argument over the places.
- `FStarC` comes from `fStarC_of_int`. It needs two facts on an isometry $\beta_0$ of $V$ that sends one frame to another. `betaRat_holds` gives such an $E$-linear isometry $\beta_0$. `betaInt_holds` (the statement `BetaInt`) gives an isometry $v$ that fixes the target frame, satisfies $v y - y \in X$ for each $y$ orthogonal to the subspace $X$ of the target frame (the Lean `Xsp`), sends the lattice of $\gamma$ to the target lattice under $v \beta_0$, and satisfies a condition `IotaC₂` that we did not unfold. `betaInt_holds` comes from `pinB_holds`, which uses `spanOm_holds`, `pinOm_holds` and `localOrthogonal_holds`.

We did not unfold the proofs of these lemmas.

## In the Lean code

The theorem is in [CutLeavesDeepOutright.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/CutLeavesDeepOutright.lean#L6). `cutLeavesDeep_of_betaInt` is in [FStarCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarCut.lean#L16) and `betaInt_holds` in [FStarBetaIF.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarBetaIF.lean#L27). `CutLeavesDeep` is in [CoefCutDeep.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/CoefCutDeep.lean#L61).

The proof of `cutLeavesDeep_of_betaInt` starts with `intro _ δ M hA _ u u' hc hP F0 what₂ hR`. So the signature condition and the local space $L$ are never used. The congruence, the prime hypothesis and the row representatives are used only for `FStarC`.

Since this theorem holds for every $D$, the hypothesis of `rowsDatumP_of_deep` is redundant. The name has a capital letter, as for a definition.
