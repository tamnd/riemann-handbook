---
id: adjoint-automorphy-w-of-printed-hida-window
title: Automorphy of the twisted adjoint of a two-dimensional representation
kind: theorem
decl: UpperTheory.V.Z.Sym.W.adjoint_automorphy_w_of_printed_hida_window
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.UnitaryThreeInputsOfLiterature
covers: 3301
status: drafted
drafted_by: writer@claude
---
This theorem proves `AdAutW`: for a two-dimensional representation $r$ of $G_L$ that meets the conditions `AdInW`, the twisted adjoint $\mathrm{ad}^0 r \otimes \varepsilon^{-1}$ is automorphic on $\mathrm{GL}_3$ over $L$. It is the automorphy input of [`unitary_three_automorphy_dense_of_prints_and_row`](/entry/unitary-three-automorphy-dense-of-prints-and-row/), and through it of the count $\mathrm{CountV}$ of the [window bound](/proof/vwin/). It has two hypotheses, the printed hypotheses `HypothesesH'` and the Galois row `RowT`.

## Statement

Let $L$ be a CM field, $l \neq 2$ a prime, $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$, and $M \neq 0$ with $2l \mid M$ and `UnrSplit L M`. Let $r \colon G_L \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$ satisfy `AdInW ι M m r`. This structure asks: $r$ is continuous, irreducible with open image, and automorphic (`AutCsd0`, with a witness `WitA`); $\mathrm{ad}^0 r$ is `Unlinked`; $r$ has a pairing for each complex conjugation; $m \ge 2$; $r$ is unramified at the places prime to $M$; $r$ has a type away from $l$; and above $l$, $r$ has a flag whose characters on inertia are powers of $\varepsilon^{b+m}$ and $\varepsilon^{b}$.

`AdAutW` says: then `AutCsd0 ι (ad0 r ⊗ ε⁻¹)` and `Birth.AllW ι (ad0 r ⊗ ε⁻¹)`.

**Theorem.** If `HypothesesH'` and `RowT` hold, then `AdAutW` holds.

## Proof

The proof is `adjoint_automorphy_w_of_pure_weight_adjoint_lift` applied to two inputs. `PureWeightCompatibility` comes from `weight_compatible_descent hH hR`. It is a structure of six facts: the classical theorems in `hH`, `GalUnitaryT`, `CompatT`, `Same`, `PlainRec` and `DescUse`. Only `GalUnitaryT`, `CompatT` and `Same` use `RowT`. `AdLiftW` comes from `adjoint_lift_w_of_literal_automorphy_spec_out`, applied to `hH.litN` and [`specOutS`](/entry/spec-out-s/). By its statement, `AdLiftW` lifts an automorphic representation of $U(2)$ over $L$ with given local data to one of $U(3)$ with the local components of the adjoint, or else to a second $U(2)$ form with squared components.

The proof of `adjoint_automorphy_w_of_pure_weight_adjoint_lift` calls a private lemma `core` once for each place $w_0$ that divides $M$. The lemma `core` does this:

1. `aboveWeight` gives an automorphic $\sigma$ on $U(2)$ with local data related to $r$. We have not unfolded this relation.
2. It picks a finite set $S$ of places that divide $M$, with $w_0 \in S$, and a set $Q$ of split places prime to $M$ with a Frobenius outside `Ga.Bad r`. At each place in $S \cup Q$ it finds the local characters of $\sigma$: `good_w_statement` on $Q$, and `above_w_statement` or `away_w_statement` on $S$.
3. It applies `AdLiftW`. The second branch of `AdLiftW` is impossible (`branch_two_w_statement`). The first branch, through `branch1W_alt`, gives a cuspidal $\pi$ on $\mathrm{GL}_3(L)$ that is regular algebraic, conjugate self-dual and attached to $\mathrm{ad}^0 r \otimes \varepsilon^{-1}$, with Satake parameters at the places prime to $M$. `plain_at_w_statement` adds a property `PT` of the local components at $w_0$.

The first three facts on $\pi$ give `AutCsd0`. Then `glueW` gives `Birth.AllW`. At a place prime to $M$, it uses the Satake parameters of $\pi$. At a place $w$ that divides $M$, it uses the `PT` property from `core` at $w_0 = w$. We have not unfolded `AutCsd0`, `Birth.AllW`, `PT` or the lemmas of steps 1 to 3.

## In the Lean code

The theorem is in [UnitaryThreeInputsOfLiterature.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryThreeInputsOfLiterature.lean#L28). The main proof and `core` are in [MemOfUnder.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MemOfUnder.lean#L35). `AdInW`, `AdLiftW` and `AdAutW` are in [UnitaryTwoForm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/UnitaryTwoForm.lean#L38). `PureWeightCompatibility` is in [WStmtxx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WStmtxx.lean#L29).

There are two lemmas named `UpperTheory.V.Z.Sym.W.core`: the private one in `DenseThresholdCases/MemOfUnder.lean` (line 35) and one in `WeilDeligneUnramified/MemOfUnder.lean` (line 38).
