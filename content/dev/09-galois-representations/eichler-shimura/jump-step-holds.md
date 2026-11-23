---
id: jump-step-holds
title: The Hodge numbers of a piece are Hodge-Tate jumps
kind: theorem
decl: UpperTheory.Gal.Int.Geo.jumpStep_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.GeometricRealizationOfWeightOne
covers: 2709
status: drafted
drafted_by: writer@claude
---
This theorem proves `JumpStep`: at a place above $\ell$ where a tower has good reduction, each degree $b$ of a Hodge group $H^q(Z, \Omega^b)$ that meets the piece is a Hodge-Tate jump of the representation on the piece. It is one of the three inputs of [the local steps](/entry/steps-holds/). It uses [the crystalline step](/entry/crys-step-holds/) and the Hodge-Tate decomposition for good models in [the Hodge-Tate frames](/entry/ht-spec-good/).

## Statement

Let $E$ be a number field, $\ell$ a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ an isomorphism, $H$ a nice tower over $E$ with variety $Z$ and eigenvalues $\theta$, and $\rho$ a continuous piece of $H$ (see [the local steps](/entry/steps-holds/)). Let $w$ be a place of $E$ above $\ell$, and suppose that $H$ has a good cover over $\mathcal{O}_{(w)}$ that is onto (`GoodAt`). Good means that each correspondence of the tower comes from a finite étale correspondence $T_g$ on the model $Y$, with a multiplier $m_g$ (`Lies`, not unfolded).

For an embedding $\tau \colon E \to \mathbb{C}$, say that $b$ *occurs* at $\tau$ (`HOcc`) if for some $q$ the group $H^q(Z_\tau, \Omega^b)$ has a nonzero vector $x$ with $T_g x = \iota\theta(g) x$ for all $g$. Here $T_g$ acts by the trace along $s_g$ of the pullback along $t_g$.

**Theorem.** For each embedding $\tau \colon E \to \overline{\mathbb{Q}}_\ell$ above $w$, the multiset $J$ of Hodge-Tate jumps of $\rho$ at $\tau$ (`IsJumpsAt`) contains each $b$ that occurs at $\iota\tau$.

## Proof

The proof is `G3.jumpStep_of Seam.HT.htSpecGood Seam.crysStep_holds repEx_holds`. It unfolds to `G8.jumpStep_of (G8.jumpCore_of …) crysStep_holds`.

1. `G8.jumpStep_of` reduces `JumpStep` to `JumpCore`, which has one more hypothesis: $\rho$ is crystalline at $w$. The crystalline step, applied to the cover, gives it.
2. `G8.jumpCore_of` proves `JumpCore`. As $\rho$ is crystalline, `G8.jumpsEx_holds` gives its jumps $J$. Let $b$ occur at $\iota\tau$. The good cover gives a second tower `low D` on the generic fibre $Y_K$ of the model, with the correspondences $T_g$ and eigenvalues $\theta(g)/m_g$. `lowHodge_holds` moves the occurrence of $b$ from $Z$ to $Y_K$. `matEx_of` (from `RepEx`) gives a matrix form $\rho_1$ of the Galois action on the piece of $Y_K$.
3. `occ_low` uses `htSpecGood`, a Hodge-Tate comparison for $H^*(Y_{\overline{\mathbb{Q}}_\ell})$ for a good smooth model (see [its entry](/entry/ht-spec-good/)). It proves `HTOcc`: some nonzero $z \in \mathbb{C}_\ell^{d}$ has $\rho_1(\sigma)\sigma(z) = \chi(\sigma)^{-b} z$ on an open subgroup, with $\chi$ the cyclotomic character.
4. `lowPiece_holds` embeds the piece of $Y_K$ into the piece of $Z$. `OccMove_holds` moves the occurrence along this embedding to $\rho_0$, and then to its block diagonal part $\rho$.
5. `jJumpOfHT2` turns the occurrence for $\rho$ into $b \in J$.

## In the Lean code

The theorem is in [GeometricRealizationOfWeightOne.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/GeometricRealizationOfWeightOne.lean#L18). Also used:

- `G3.jumpStep_of`, in [TraceSplitHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/TraceSplitHolds.lean#L78).
- `G8.jumpStep_of`, `JumpCore` and `low`, in [JumpStepOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/GoodCoverEigenspaces/JumpStepOf.lean#L113).
- `G8.jumpCore_of`, in [JumpOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/GoodCoverEigenspaces/JumpOf.lean#L34).

Points to note:

- The conclusion is only an inclusion: each Hodge degree that occurs is a jump. It does not say that each jump comes from a Hodge degree, or with which multiplicity.
- `RepEx` is used only through `matEx_of`.
- `G3.jumpStep_of` uses its own `seamHopEx_holds` and `locTower_holds` in the namespace `G3`. They prove the same statements as `Seam.hopEx_holds` and `Seam.locTower_holds` ([TraceSplitHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/TraceSplitHolds.lean#L46)). The proof of `HopEx` is separate; the proof of `LocTower` is the same term.
- We have not unfolded `IsJumpsAt`, `IsCrysAt`, `Lies` or the lemmas `LocE` and `CoverLow` that `occ_low` uses.
