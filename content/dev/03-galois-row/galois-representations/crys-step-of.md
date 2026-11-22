---
id: crys-step-of
title: The crystalline step from the comparison theorem for smooth models
kind: theorem
decl: UpperTheory.Gal.Seam.crysStep_of
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.CrystallineTowers.LocTowerHolds
covers: 4182
status: drafted
drafted_by: writer@claude
---
This theorem proves the crystalline step `CrysStep` from the crystalline comparison theorem for smooth projective models. [The crystalline step](/entry/crys-step-holds/) applies it to a proof of that comparison theorem, and the result goes into [the local steps](/entry/steps-holds/). The proof applies the theorem `crysStep` to eight proved lemmas. The largest is [the embedding into the cohomology of a model](/entry/mat-in-holds/).

## Statement

Let $\mathrm{SMC}$ be the following statement (`SmoothModelCrystalline`). Let $K$ be a finite extension of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, and let $Y$ be a model over $\mathcal{O}_K$ that is good (projective and strictly semistable) and smooth. Then for each $n$ and each basis of $V_n = H^n(Y_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$, the matrix representation of $G_K$ on $V_n$ is $B_{\mathrm{cr}}$-admissible (`IsAdm (Bcr l)`). In words, $V_n$ is crystalline. This is the crystalline comparison theorem of Faltings ("Crystalline cohomology and p-adic Galois-representations", Algebraic analysis, geometry, and number theory, Johns Hopkins Univ. Press, 1989).

**Theorem.** If $\mathrm{SMC}$ holds, then `CrysStep` holds: let $E$ be a number field, $H$ a nice tower over $E$, $\rho$ a continuous piece of $H$, and $w$ a place of $E$ above $\ell$ (see [the local steps](/entry/steps-holds/) for these words). If $H$ has a cover $C$ over $\mathcal{O}_{(w)}$ that is onto, then $\rho$ is crystalline at $w$.

A *cover* (`Cover`) is a smooth projective scheme $Y$ over $\mathcal{O}_{(w)}$, a map from the variety $Z$ of the tower to $Y$ that makes $Z$ finite étale over $Y_E$, and a finite group $\Delta$ that acts on $Z$ with $Z \times_{Y_E} Z$ split by $\Delta$ (`Splits`, not unfolded). Each element of $\Delta$ comes from a map of the tower with $\theta = 1$. *Onto* means that $Z \to Y_E$ is surjective, so that $Z$ is a Galois cover of $Y_E$ with group $\Delta$.

## Proof

Write $\rho$ as the block diagonal part of $\rho_0$, the matrix form of the Galois action on the piece. Fix a place of $\bar E$ above $w$ and an embedding into $\overline{\mathbb{Q}}_\ell$, with $K = E_w$.

1. `intMap` maps $\mathcal{O}_{(w)}$ into $\mathcal{O}_K$. `niceBc` and `locTower_holds` move $H$ to a nice tower over $K$, with a matrix form $\rho_1$ of $G_K$ that agrees with $\rho_0$ on the decomposition group.
2. `bcCover` moves $C$ to a cover $C'$ over $\mathcal{O}_K$ that is onto. Its scheme $Y'$ is smooth and projective, so `goodOf` makes it a good model.
3. `matIn_holds` gives an injective matrix $M$ that intertwines $\rho_1$ with a block sum of the representations on $H^n(Y'_{\overline{\mathbb{Q}}_\ell})$.
4. $\mathrm{SMC}$ makes each block admissible. `isAdmP_of_isAdm` turns this into the form `IsAdmP` that `subAdm` uses. `subAdm` then makes $\rho_0$ crystalline on the decomposition group, as a subrepresentation of a crystalline one.
5. `grCrys` passes from $\rho_0$ to its block diagonal part $\rho$.

## In the Lean code

The theorem is in [LocTowerHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/LocTowerHolds.lean#L25). The proof is one line:

```
crysStep h niceBc locTower_holds bcCover intMap goodOf matIn_holds subAdm grCrys
```

`crysStep` is in [CrysStep.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/CrysStep.lean#L23). The statements of its eight hypotheses are in [LocTower.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/LocTower.lean#L24). $\mathrm{SMC}$ and $B_{\mathrm{cr}}$ are in [SemistableModelSemistable.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/SemistableModelSemistable.lean#L46).

- The names `crysStep_of` and `crysStep` are close. `crysStep_of` only passes arguments; `crysStep` does the work.
- $B_{\mathrm{cr}}$ is the subring of $B_{\mathrm{dR}}$ made by the image of $A_{\mathrm{cris}}$, $1/\ell$ and $1/t$. We have not unfolded `ACris`, `IsAdmP`, `IsCrysAt` or the proofs of `subAdm` and `grCrys`.
- The proof of `crysStep` also calls `UpperTheory.Lit.Cmp.locTied6` to get the input of `isAdmP_of_isAdm`. It does not use the part of `BcCover` that keeps good covers good.
