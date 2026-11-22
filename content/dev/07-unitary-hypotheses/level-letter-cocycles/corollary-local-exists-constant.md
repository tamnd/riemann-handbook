---
id: corollary-local-exists-constant
title: The local lifting theorem and its corollary, with one constant for all data
kind: theorem
decl: Formalism.MainNotions.N.Ln03.corollary_local_exists_constant
module: Formalism.SharpRestriction.LevelLetterCocycles.LocalTheoremOfInputs
covers: 1752
status: drafted
drafted_by: writer@claude
---
This theorem gives one real $C_0$ such that, for every datum that satisfies a list of local hypotheses, the local lifting theorem holds with constant 800 and the colength corollary holds with each constant $C_2 \ge C_0$. The lifting part is [the local theorem from inputs](/entry/local-theorem-of-inputs/), which has most of the content. Its user is [the closing of theorem E and corollary A](/entry/thm-ecor-a-closing/), through `localCorollaryConstant`, which picks $C_0$ by choice.

## Statement

**Theorem.** There is $C_0 \in \mathbb{R}$ with the following property. Let $D$ be a datum with local data $HW$, $F$, $C_m$, and let $C$ be real. Assume the hypotheses of [the local theorem from inputs](/entry/local-theorem-of-inputs/) (with $C$ as the constant of the Wach result) and also `adm12`, the bound `H1fGeneratorBoundAll` on generators of $H^1_f$. Then

1. `Conclusion1 D 800` holds, and
2. `Conclusion2 D C₂` holds for each $C_2 \ge C_0$.

`Conclusion1` is stated in [the local theorem from inputs](/entry/local-theorem-of-inputs/). `Conclusion2 D C` is the corollary `CorAAt` at each $(\ell, K, L, n, \mathrm{emb})$: if the letter condition `Letters` of [the local theorem](/entry/local-theorem-of-inputs/) holds, $\ell \ge 11$, $f \colon T_1 \to T_2$ is a surjection of crystalline lattices with `GoodCoeffs` and $r = \dim_L T_2$, $1 \le j$ and $j + 1 \le n$, and the Hodge-Tate jumps of $T_1$ lie in windows of sizes $sz(i)$ that are thick ($b \le sz(i) \le b + \eta$) or small ($sz(i) \le w$), with $C(j+1)(w+S+\eta+1) \le b$ and a cluster condition, then

$$\mathrm{col}(f) \le C(n+1)\, r \Bigl(\frac{h}{(\ell-1)^{j+1}} + (w+S+\eta+1)(j+1) + \log_\ell h\Bigr) \cdot \lambda,$$

where $h = b + \eta + S$ if some window is thick and $h = w + S + \eta$ otherwise (`hCor`), and $\lambda$ is the length of $\mathcal{O}/(\ell)$. We have not unfolded `GoodCoeffs` or the cluster condition.

## Proof

`corollary_of_Theorem_E` gives $C' \ge 1$ such that, for each $D$ and $C_1 \ge 0$, `Conclusion1 D C₁`, `H1fGeneratorBoundAll` and `JumpsSubL` imply `Conclusion2 D (max C' (4 C₁))`. Take $C_0 = \max(C', 3200)$.

Part 1 is `local_theorem_of_inputs`. For part 2, apply `corollary_of_Theorem_E` with $C_1 = 800$. The hypothesis `JumpsSubL` says that, for a surjection, the jumps of $T_2$ lie in each set that contains the jumps of $T_1$. It follows from the first part of `adm14`, which says that each jump of $T_2$ is a jump of $T_1$. This gives `Conclusion2 D C₀`. Then `corollary_monotone_in_constant` passes to each $C_2 \ge C_0$; it only uses that the bound grows with $C$.

## In the Lean code

The theorem is at [LocalTheoremOfInputs.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalTheoremOfInputs.lean#L112), with `corollary_monotone_in_constant` at [line 95](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalTheoremOfInputs.lean#L95). `corollary_of_Theorem_E` is at [BoundedNumeratorPowerSummability.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BoundedNumeratorPowerSummability.lean#L722); we have not unfolded its proof.

- $C_0$ comes before all data, so it does not depend on $D$ or on $C$. The Lean code gives no value for it: `localCorollaryConstant` is `Classical.choose` of this theorem.
- The constant $C$ of the hypotheses enters only through `ArchimedeanSignatureMatching D HW F C`, which here means `WachResultConstant C`. The conclusions do not mention $C$.
- `adm12` is used only for part 2.
