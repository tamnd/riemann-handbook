---
id: down-inclusion-w-real-holds
title: The lattice inclusion at the short weight bound
kind: theorem
decl: Formalism.CohomologicalDescent.Down.inclusion_w_real_holds
module: Formalism.PieriBlockIdeals.PieriColumnMinors.CorollaryOfParamsLinkage
covers: 882
status: drafted
drafted_by: writer@claude
---
This theorem moves forms with values in dual Weyl modules into forms with values in Weyl modules, with an explicit power of $l$. It is a pass-through: it takes the version that has the graded Lemma D as a hypothesis and gives it [the proof of that lemma](/entry/h-g/). Its only user is [the inclusion at the coarse weight bound](/entry/down7-inclusion-w-seven-real-holds/), which enlarges the exponent.

## Statement

We use the words of [the lattice inclusion from local models](/entry/l-incl-of-models/). A Hida setting $X$ has an inclusion of exponent $J$ at $l$ (`Incl l J`) if, after localization at the Hecke set $S$, $l^J$ moves each form of level $\Gamma$ with values in $\bigotimes_\tau \nabla(\lambda_\tau)$ into the forms with values in $\bigotimes_\tau \Delta(\lambda_\tau)$. Let $J_{\min}(l)$ be the least such $J$ (`Jmin`).

For parameters $P$ and a weight datum $W$, the short weight bound is $J_W(l) = \sum_\tau c_\tau(l)$ (`JW`). Here, with $e_\tau(l)$ the exponent of that entry (`ex`), $c_\tau(l) = e_\tau(l)$ for $\tau \notin T_2$, and $c_\tau(l) = \min(e_\tau(l), \lfloor c^{(6)}_\tau(l) \rfloor)$ for $\tau \in T_2$, where $c^{(6)}_\tau(l)$ is the explicit real number `cShort6`.

**Theorem.** Let $P$ satisfy `Hyp` and `Large`, and let $W$ satisfy `Ok P`. Let $l$ be a prime with $l > l_J(P)$, and $X$ a Hida setting for the weights of $W$ in which $l$ is not a unit. Suppose that the weight inputs `WInputs` hold for $X$ at $l$. Then $X$ has an inclusion of exponent $J_W(l)$ at $l$, and $J_{\min}(l) \le J_W(l)$.

## Proof

The proof is `ShortWeightBounds.inclusion_w_real_holds hG`. The first lemma has one more hypothesis, $\mathrm{LemmaDGraded}$, and `hG` proves it. The work is in those two lemmas.

## In the Lean code

The theorem is in [CorollaryOfParamsLinkage.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/CorollaryOfParamsLinkage.lean#L24). It calls:

- `ShortWeightBounds.inclusion_w_real_holds`, in [WeightBounds.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/WeightBounds.lean#L510). It is `inclusion_w_of_shape_w shape_w_real_holds`, which builds `TopInputs` and applies `theorem_w_top_short_bound_holds`. That lemma needs the last-graded Lemma D, which `last_graded_of_graded_alone` derives from $\mathrm{LemmaDGraded}$. We did not unfold `theorem_w_top_short_bound_holds`.
- [`hG`](/entry/h-g/), in the same file.

Two definitions have the name `InclWReal`. The one in [StatementDown.lean](lean:Formalism/PieriBlockIdeals/StatementDown.lean#L204) (namespace `Down`) is the statement above. The one in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L318) (namespace `ShortWeightBounds`) is the same statement with $\mathrm{LemmaDGraded}$ as a first hypothesis.
