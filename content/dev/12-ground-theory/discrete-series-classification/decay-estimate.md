---
id: decay-estimate
title: Path ends at far labels embed into L² functions on U(p,q)
kind: theorem
decl: CompanionTheory.RgExh.Dec.decay_estimate
module: CompanionTheory.RealGroups.DiscreteSeries.DiscreteSeriesClassification.DiscreteSeriesExhaustion.MatrixCoefficientDecay.DecayEstimate
covers: 811
status: drafted
drafted_by: writer@claude
---
This theorem is fact 3 in the proof of [the exhaustion theorem](/entry/ds-exhaust/). It says that if a path of steps from the module of a square-integrable representation ends at labels far enough out, then the end module embeds into smooth $L^2$ functions on $G$. The proof is one line. It joins three statements, `Start`, `Labels` and `Back`, about the decay of matrix coefficients along one-parameter subgroups. The parent entry fixes the notation $\varepsilon$, $G$, $K$, steps, paths and characters; we use it here.

## Statement

For $\chi, \chi' \in \mathbb{C}^n$ and $B \in \mathbb{R}$, say $\chi'$ is *far from* $\chi$ *beyond* $B$ (`FarLabels`) if for all disjoint $I, I' \subseteq \{1, \dots, n\}$ of the same size with $\operatorname{Re}\bigl(\sum_I \chi_i - \sum_{I'} \chi_i\bigr) < 0$, we have $\operatorname{Re}\bigl(\sum_I \chi'_i - \sum_{I'} \chi'_i\bigr) < -B$.

**Theorem.** Assume `StepChar`: a step in direction $s$ moves the character from $\chi$ to $\chi + e_s$. Then for each $n$ there is $B$ such that the following holds. Let $\sigma$ be a unitary, irreducible, square-integrable representation of $G$, with module $D$ of $K$-finite vectors and character $\chi$. Let $s_1, \dots, s_m$ be a good path whose end label is far from $\chi$ beyond $B$. Then for each nonzero $u$ in the end module $X$, there is a $\mathfrak{gl}_n$-map $c \colon X \to \mathrm{sm}_\varepsilon$ with $c(u) \neq 0$ (`L2Embedding`).

## Proof

Fix $A$ in the Lie algebra of $G$ with $A^* = A$, $A^3 = A$ and $A \neq 0$ (`IsGrad`). Let $P_A$ be the subgroup of $G$ that keeps the subspaces $\operatorname{range} \tfrac12(A^2 - A)$ and $\ker \tfrac12(A^2 + A)$ (`PSub`), with Haar measure $\nu$. Let $\rho_A = j(n - j)$, where $j$ is the real part of the trace of $\tfrac12(A^2 + A)$. For a function $f$ on $G$ and $s \in \mathbb{R}$, say $f$ *decays at rate* $s$ if
$$\int_0^\infty |f(x \exp(tA))|^2 e^{-2st} \, dt < \infty \quad \text{for } \nu\text{-almost all } x \in P_A.$$

1. `Start` (`exhaustion_start`): each coefficient $g \mapsto \langle \xi, \sigma(g) u \rangle$, with $u \in D$, decays at rate $-\rho_A$.
2. `Labels` (`exhaustion_labels`): given `StepChar`, there is $B$ such that, for a path to labels far beyond $B$, every coefficient of the end module (`famP`, built from the base coefficients by the steps) decays at rate $-\rho_A - 1$.
3. `Back` ([`backward_of_line_formula`](/entry/backward-of-line-formula/)): this faster decay for all $A$ gives `L2Embedding`.

`decay_of` takes the $B$ of `Labels`, feeds `Start` into `Labels`, and feeds the result into `Back`.

## In the Lean code

The theorem is in [DecayEstimate.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/DecayEstimate.lean#L8). `Start`, `Labels`, `Back`, `IsGrad`, `PSub` and `rhoA` are in [KeepsMul.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/KeepsMul.lean#L98). `Decay`, `FarLabels` and `L2Embedding` are in [L2Embedding.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/L2Embedding.lean#L24).

- `decay_of` ([DecayOf.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/DecayOf.lean#L7)) never uses the hypothesis that $\sigma$ is irreducible. None of `Start`, `Labels` or `Back` asks for it.
- `Start` and `Labels` are proved from named statements in `GlobalTheory.T` and `GlobalTheory.CompanionTheory`. We have not unfolded them.
- We have not unfolded the target `smD ε (rreg ε)` of the embedding.
