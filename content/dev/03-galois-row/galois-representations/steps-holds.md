---
id: steps-holds
title: The local steps for the cohomology of a tower
kind: theorem
decl: UpperTheory.Gal.Int.Geo.steps_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.GeometricRealizationOfWeightOne
covers: 26256
status: drafted
drafted_by: writer@claude
---
This theorem proves `Steps`, a list of 17 facts about the Galois representations that are cut out of the cohomology of a tower of varieties. It is the first of the three parts that [the Galois row from geometry](/entry/geometric-realization-of-weight-one/) assembles. Its fields make the representations of [the statement GeoOne](/step/geo-one-def/). It covers 26,256 declarations.

## Statement

**Towers.** A *tower* $H$ over a field $k$ (`HTower`) is a scheme $Z$ over $k$ and, for each $g$ in an index set $\Gamma$, two maps $s_g, t_g \colon Y_g \to Z$ over $k$. It is *nice* (`Nice`) if $Z$ is smooth and projective and each $s_g$ is finite étale. Each pair $(s_g, t_g)$ gives an operator $T_g$ on $H^*(Z_{\bar k}) = \bigoplus_n H^n(Z_{\bar k}, \mathbb{Q}_\ell)$ (`hop`). For $\theta \colon \Gamma \to \overline{\mathbb{Q}}_\ell$, the *piece* is the subspace of $\overline{\mathbb{Q}}_\ell \otimes H^*(Z_{\bar k})$ where each $T_g$ acts by $\theta(g)$. A representation $\rho$ is *a piece of the tower* (`IsPiece`) if it is the block diagonal part of a block upper triangular matrix form $\rho_0$ of the Galois action on the piece (`IsMat`, `IsGr`).

**Theorem.** `Steps` holds. It has five groups of fields. Here $E$ is a number field, $H$ a nice tower over $E$, $\rho$ a continuous piece of $H$, and $w$ a place of $E$.

1. *Existence* (`RepEx`). For each $H$ and $\theta$, some piece $\rho$ is continuous and semisimple.
2. *Local steps.* Let $R$ be the roots of a Hecke polynomial of the tower at $w$ (`CongAt`, `HasRoots`). At $w \nmid \ell$, $\rho$ is unramified and $\prod_{r \in R}(X - \iota^{-1} r)$ kills $\rho(\mathrm{Frob}_w^{-1})$ (`ESStep`; an Eichler-Shimura relation by its name). At $w \mid \ell$: $\rho$ is crystalline if the tower has a cover over $\mathcal{O}_{(w)}$ that is onto (`CrysStep`); the Hodge numbers of the piece are Hodge-Tate jumps of $\rho$ if the cover is also good (`JumpStep`); and $\rho$ is crystalline with a Frobenius of degree $-1$ on its Weil-Deligne representation whose characteristic polynomial divides a power of $\prod_{r \in R}(X - r)$ (`PhiStep`). `CutStep` changes the form of these hypotheses.
3. *Twists* (`TwES`, `TwCrys`, `TwJ`, `TwPhi`). Let $\chi$ be a continuous character with Frobenius value $c$ and Hodge-Tate weights $m$ at $w$ (the condition `Cl`). Then the four local properties pass from $\rho$ to $\chi \rho$, with $R$ replaced by $cR$ and the jumps moved by $m$.
4. *Translations* to the form of `GeoOne` (`PhiOf`, `SatCard`, `JumpsOf`, `RichOf`).
5. *Characters and generalities.* `CharEx`: algebraic Hecke characters give continuous Galois characters with the expected Frobenius values and Hodge-Tate weights. `SSLeft` and `ContLeft`: semisimplicity and continuity pass to direct summands, to isomorphic representations and to twists.

## Proof

The proof is `steps_of crysStep_holds jumpStep_holds phiStep`. The lemma `steps_of` takes `CrysStep`, `JumpStep` and `PhiStep` as hypotheses and fills the other 14 fields with proved lemmas, one for each field, such as `repEx_holds` and `Mod.esStep_holds`.

- `Seam.crysStep_holds` (4,188 declarations): see [the crystalline step](/entry/crys-step-holds/).
- `jumpStep_holds` (2,709): see [the Hodge-Tate jump step](/entry/jump-step-holds/). It uses `crysStep_holds` and `repEx_holds` again.
- `Ru.crystallineComparison.phiStep` (1,031): see [the Frobenius step](/entry/phi-step/). It is `phiStep_of (geoSide_of finAll smoothModel_crystalline)` (not unfolded here).

Two more outline entries lie directly below this theorem: [a projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/) (1,595) and [proper base change](/entry/proper-base-change/) (1,247). We have not traced which fields use them. The rest is bookkeeping.

## In the Lean code

The theorem is in [GeometricRealizationOfWeightOne.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/GeometricRealizationOfWeightOne.lean#L20). Also used:

- `Steps`, in [MapInvMul.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/MapInvMul.lean#L19); its fields, in [HodgeTrAt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/HodgeTrAt.lean#L103).
- `steps_of`, in [StepsMain.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/StepsMain.lean#L17).
- Towers, pieces and covers, in [IsGrRefl.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/IsGrRefl.lean#L31).

The operator $T_g$ (`GlobalTheory.GalV.hop`) is defined by choice: an operator with the correspondence property `IsCorrOp` if one exists, else $0$. For a nice tower, `HopEx` proves that one exists.
