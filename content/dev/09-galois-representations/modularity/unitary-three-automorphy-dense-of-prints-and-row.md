---
id: unitary-three-automorphy-dense-of-prints-and-row
title: Three-dimensional seeds from Eisenstein congruences and adjoint automorphy
kind: theorem
decl: UpperTheory.V.Z.Sym.W.unitary_three_automorphy_dense_of_prints_and_row
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.UnitaryThreeInputsOfLiterature
covers: 4237
status: drafted
drafted_by: writer@claude
---
This theorem proves `UnitaryThreeAutomorphyDense`, the statement on three-dimensional automorphic seeds that feeds the count $\mathrm{CountV}$ of the [window bound](/proof/vwin/). It has two hypotheses: the printed hypotheses `HypothesesH'` and the Galois row `RowT`. The seeds are adjoints of two-dimensional representations that are congruent to Eisenstein series. [`unitary_three_automorphy_dense_of_prints`](/entry/unitary-three-automorphy-dense-of-prints/) supplies the row.

## Statement

Let $K$ and $L$ be number fields with $L$ a CM field, $l$ a prime, $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$ an isomorphism, $c \in G_{\mathbb{Q}}$, and $\chi', \eta, \theta$ characters of $G_{\mathbb{Q}}$ with $\chi' \neq \eta$. Assume that these data, with $N, w, j$, satisfy `FieldPairCharacterTripleConditions`, which we have not unfolded. Let $M \neq 0$ with $2l \mid M$, such that `UnrSplit L M` holds and $\chi'$ is trivial on the inertia groups of $G_L$ at places prime to $M$. Write $\varepsilon$ for the cyclotomic character.

`UnitaryThreeAutomorphyDense` says: for each $B$ there is $m \ge B$ with $m \equiv j \pmod{l-1}$ and an irreducible open $r \colon G_L \to \mathrm{GL}_3(\overline{\mathbb{Q}}_l)$ that is a seed (`IsSeedAlt`) with characters $(\varepsilon^j\chi', 1, (\varepsilon^j\chi')^{-1})$ and $(\chi', 1, \chi'^{-1})$ restricted to $G_L$, weights $(m, 0, -m)$ and twist $\varepsilon^{-1}$. We have not unfolded `IsSeedAlt`.

**Theorem.** If `HypothesesH'` and `RowT` hold, then `UnitaryThreeAutomorphyDense` holds.

## Proof

The proof is `adjoint_lift_from_eisenstein_of_propagation` applied to three inputs:

- `PropEGW` from `prop_eg_w_of_printed_hida hH`. For a character $\varphi \neq 1$ split at $N$ and $w$, and all large $k$ with $\varphi(c) = (-1)^k$, it gives $\rho \colon G_{\mathbb{Q}} \to \mathrm{GL}_2$ with `EisRep ι φ θ k ρ` (by its name, a representation that comes from an Eisenstein congruence), `Birth.PR` and `Unlinked (ad0 ρ)`.
- `SeedInW` from `seedInW_alt hH`. It gives a character $\kappa$ of $G_L$ such that the twist of $\rho|_{G_L}$ by $\kappa$ satisfies `AdInW`.
- `AdAutW` from [`adjoint_automorphy_w_of_printed_hida_window`](/entry/adjoint-automorphy-w-of-printed-hida-window/) `hH hR`. This is the only use of `RowT`.

The proof of `adjoint_lift_from_eisenstein_of_propagation` takes $\varphi = \chi'\eta$. It shows $\eta^2 = 1$ and $\eta(c) = -1$. Then $\varphi$ is split at $N$ and $w$, and $\varphi \neq 1$ since $\chi' \neq \eta$. It sets $m = j + (l-1)t$ with $t = B + k_0 + 2$, so $m \ge B$, $m \equiv j$, and $\varphi(c) = (-1)^{m+1}$. `PropEGW` at weight $m+1$ gives $\rho$. The seed is $r = \mathrm{ad}^0\rho|_{G_L}$. Its irreducibility, symmetric pairing, shape away from $l$ and order above $l$ come from facts about $\mathrm{ad}^0$. For automorphy, `SeedInW` gives $\kappa$, `AdAutW` gives automorphy of $\mathrm{ad}^0(\rho|_{G_L} \otimes \kappa) \otimes \varepsilon^{-1}$, and `adjoint_zero_twist` removes $\kappa$, since $\mathrm{ad}^0$ does not see a twist by a character.

## In the Lean code

The theorem is in [UnitaryThreeInputsOfLiterature.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryThreeInputsOfLiterature.lean#L29). `UnitaryThreeAutomorphyDense` is in [SymUse.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/SymUse.lean#L27). The main step is in [AdjointLiftFromEisensteinSeedOfHyps.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AdjointLiftFromEisensteinSeedOfHyps.lean#L184). `PropEGW`, `SeedInW`, `AdInW` and `AdAutW` are in [UnitaryTwoForm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/UnitaryTwoForm.lean#L38). We have not unfolded `HypothesesH'`, `EisRep`, `Birth.PR` or `Unlinked`.
