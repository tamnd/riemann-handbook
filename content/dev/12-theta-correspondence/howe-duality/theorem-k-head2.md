---
id: theorem-k-head2
title: Theta integrals agree and local matching, from Eisenstein continuation and Siegel-Weil
kind: theorem
decl: PositivityTheory.ThKR.theoremK_head2
module: Development.WeilBound.ThetaLifts.Reductions.FiniteClosure.TheoremKOfMod
covers: 6823
status: drafted
drafted_by: writer@claude
---
This theorem gives the two theta statements `ThetaIntegralsAgree` and `LocalMatching` from two inputs: the continuation of Siegel Eisenstein series `EisBL` and the Siegel-Weil formula `SiegelWeilStd`. Its user is [theta integrals agree and local matching from the literature](/step/theta-integrals-agree-and-local-matching-of-literature/), which supplies both inputs with theorems of the code (see the [step](/step/theta-integrals-agree-and-local-matching-of-literature/)). The two conclusions are the inputs $h_A$ and $h_M$ of the [theta matching chapter](/proof/theta-matching/). Below this theorem are 6,823 declarations.

## Statement

**Theorem.** If `EisBL` and `SiegelWeilStd` hold, then `ThetaIntegralsAgree` and `LocalMatching` hold.

`ThetaIntegralsAgree` is unfolded in [its step](/step/theta-integrals-agree-def/): for each admissible triple, the theta integrals decay, two theta integrals into the same unitary group $U_W$ are proportional with one nonzero constant when their test functions match, and two recursion laws relate these constants. `LocalMatching` is unfolded in [its step](/step/local-matching-def/): at each place, the two local [[Weil representations|H3Q2703KKV]] have matched quotient maps onto one irreducible representation of $U_W$. `SiegelWeilStd` is the Siegel-Weil formula of the [Siegel-Weil chapter](/proof/siegel-weil/), proved in [its entry](/proof/siegel-weil/). `EisBL` says that the Siegel [[Eisenstein series|3NZBZXYWAJ]] of the doubled group converges and is holomorphic for large $\operatorname{Re} s$. Also, near each $s_0$ there are $k$ and functions $H(s)$ of moderate growth with $H(s) = (s - s_0)^k E(s)$ for $s \neq s_0$, such that $\mu(H(s))$ is holomorphic near $s_0$ for each linear form $\mu$ that is bounded on each growth class (`IsGrowForm`).

## Proof

Apply [`theoremK_head2_of_mod`](/entry/theorem-k-head2-of-mod/) to the theorem `PositivityTheory.Sph.modSt2` and the two inputs. The theorem `modSt2` proves the extra hypothesis `ModSt` of `theoremK_head2_of_mod`, a statement on indices of compact open subgroups at the inert places, stated in that entry. Its proof is `M2.modSt_of M2.chart M2.locMod`, which we have not followed. The real content is in [the assembly `closeSph`](/entry/close-sph/), below `theoremK_head2_of_mod`.

## In the Lean code

The theorem is in [TheoremKOfMod.lean](lean:Development/WeilBound/ThetaLifts/Reductions/FiniteClosure/TheoremKOfMod.lean#L26). Its proof is `theoremK_head2_of_mod PositivityTheory.Sph.modSt2 h11 h12`. The theorem `modSt2` is in [ModSt2.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/ModSt2.lean#L7), and `ModSt` is defined in [FunDefs.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/FunDefs.lean#L98).

The theorem only fills one hypothesis of `theoremK_head2_of_mod` with a theorem. The name "Theorem K" and the suffix "head2" do not describe the statement. `EisBL` and `SiegelWeilStd` are hypotheses here, but in the proof of the Riemann Hypothesis both are proved by theorems of the code, so the conclusion holds with no hypothesis.
