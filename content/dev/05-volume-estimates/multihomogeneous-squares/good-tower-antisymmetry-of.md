---
id: good-tower-antisymmetry-of
title: The swap relation on a good tower, from seven statements
kind: theorem
decl: SquareStatements.good_tower_antisymmetry_of
module: Development.WeilBound.CoreStatements.MultihomogeneousSquares.GoodTowerAntisymmetryOf
covers: 1426
status: drafted
drafted_by: writer@claude
---
This theorem proves that a good tower satisfies the swap relation $\mathrm{I8}$, from seven named statements. [The swap relation given the singular metric statement](/entry/antisymmetry-of-singular-statement/) fills six of them with proved lemmas, and [the swap relation on a good tower](/entry/good-tower-antisymmetry/) fills the seventh. The relation goes up to [the full intersection tower relation](/entry/full-intersection-tower-i8-relation/) and to the volume branch of [the Weil bound chapter](/proof/weil-bound/).

## Statement

Fix a finite set $\Psi$ and $N \geq 1$. Let $R = \mathbb{R}[X_{\tau,i} : \tau \in \Psi,\ 0 \leq i < N]$, and let $D = |\Psi| \cdot N(N-1)/2$. For a weight $\lambda \colon \Psi \times \{0, \dots, N-1\} \to \mathbb{R}$, put $\ell_\lambda = -\sum_{\tau, i} \lambda_{\tau,i} X_{\tau,i}$. Let $s_{\tau,a,b}\lambda$ be $\lambda$ with the entries $a$ and $b$ of row $\tau$ swapped.

A root tower $T$ has an integer $j$ with $1 \leq j < N$, a finite nonempty set of components $c$, a volume $\mathrm{vol}(c)$, and for each $B$ and $c$ a root model: a multiprojective arithmetic variety of dimension $D + 1$ with Hermitian lines. For an intersection system $I$, the root model gives a linear functional $\mathrm{PP}^B_c$ on $R$. On a monomial it is the limit as $t \to 0^+$ of an $I$-intersection number of lines, divided by a normalizing constant. The flag functional $h$ sends a monomial $m$ of degree $D + 1$ to $(-1)^{\deg m}$ times an $I$-intersection number on a model of the flag variety. It sends the other monomials to $0$. We have not unfolded the Hermitian lines of that model.

**Relation $\mathrm{I8}$.** For all $B \geq 2$, all $c$ and $\tau$, all $a$ and $b = a + 1$ with $b \neq j$, and all $\lambda$, the defect $\delta(\lambda) = \mathrm{PP}^B_c(\ell_\lambda^{D+1}) - \mathrm{vol}(c)\, h(\ell_\lambda^{D+1})$ satisfies $\delta(s_{\tau,a,b}\lambda) = -\delta(\lambda)$.

**Theorem.** Assume `StX`, `StAlg`, `StHt`, `StSing`, `StBase`, `StCmp` and `AntisymmetryFibreSquares`. Assume also `CmpSt`, `Given` and `Out.WeilSt`. Let $E$ be a CM field with a host $H$, a datum $D$ with $p_D \geq 1$ and $q_D \geq 1$, a model $Y$, and a root tower $T$ for $\Psi = \mathrm{CMType}(H)$ and $N = p_D + q_D$ with a good origin over $Y$ that satisfies `Extra`. Then for each full intersection system $I$, $T$ satisfies $\mathrm{I8}$.

## Proof

1. `host_numbers` gives that $\mathrm{CMType}(H)$ is nonempty.
2. `tie_of` turns `StX`, `StAlg`, `StHt`, `StSing` and `StBase` into the tie statement `StTie`. Then `sq_of` turns `StTie` and `StCmp` into `StSq`. Applied to the tower, `StSq` gives `SquaresS`: for each $B$ and $c$, there is a realization $\mathrm{Re}$ with a flag system whose intersection weight and degree polynomial are $m > 0$ times those of the tower.
3. `AntisymmetryFibreSquares` turns `SquaresS` into $\mathrm{I8}$. It needs three more inputs: `Antisymmetry` from `GlobalTheory.T.antisymmetry'`, `AgreementPos` from `GlobalTheory.T.agreement_positive`, and `PB.Inputs`, the tenth part of `Given`.

`Antisymmetry` says that for a realization with a flag system, the weight $\mathrm{PB} - \mathrm{vol} \cdot h$ is a homogeneous polynomial that changes sign under each block simple swap. This is where the sign change comes from.

## In the Lean code

The theorem is in [GoodTowerAntisymmetryOf.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/GoodTowerAntisymmetryOf.lean#L20), with `GoodTowerAntisymmetry` at line 13. The relation is `RootTower.I8` in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L108). The statements are in [AntisymmetryFibreSquares.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/AntisymmetryFibreSquares.lean#L17). The lemmas are `tie_of` in [ChooseTwoAdd.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/ChooseTwoAdd.lean#L55) and `sq_of` in [SqOf.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/SqOf.lean#L13).

The proof takes `PB.Inputs` out of `Given` with the projection `hG.2.2.2.2.2.2.2.2.2.1` (line 24). `tie_of` builds the flag systems with [the square systems on a flag cover](/entry/t-flag-cover-realisation-pullback/). The words "Weil" in the folder name and in `Out.WeilSt` refer to Weil pairings, not to the explicit formula.
