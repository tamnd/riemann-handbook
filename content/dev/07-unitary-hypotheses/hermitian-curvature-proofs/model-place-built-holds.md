---
id: model-place-built-holds
title: Each place of a built setting is a model place
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.model_place_built_holds
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.TransferSmoothAtBuiltPlace
covers: 1931
status: drafted
drafted_by: writer@claude
---
This theorem proves `ModelPlaceBuilt2` with no hypothesis. The statement says that at each real place of a "built" setting, the local data are an instance of the abstract model setting of [the energy limit in the model setting](/entry/lemma-model/). Its only user is [the carrier inputs from D](/entry/carrier-needs-from-d/), which pairs it with `ThmPActualCpt` and [the bounds at a leading-form setting](/entry/pb-built-bounds2-cpt/).

## Statement

The objects are specific to this code base. A *Hida setting* $S$ (`C.HidaSetting`) is attached to a CM field $E$ and to finite-dimensional complex inner product spaces $W_p(x)$, $W_q(x)$ for each infinite place $x$ of $E$. It lists the $f$ infinite places $v$ with embeddings $\sigma_v \colon E \to \mathbb{C}$, integers $k$, $r$, $l$, cut intervals $[\alpha_v, \beta_v]$, grids and place data. Further data at $v$ are a tower $T_v$ of real place data, a function $f_v$ from $k \times r$ matrices to $\operatorname{Hom}(W_q, W_p)$, a cutoff function $\chi$ and a real $A_0$.

`IsBuiltPlace` with constant $C_c$ asks: $g_1, g_2 > 0$; $\mathfrak{D}_{E/\mathbb{Z}} = \mathfrak{D}_{E^+/\mathbb{Z}} \mathcal{O}_E$ for the maximal real subfield $E^+$, that is, $E/E^+$ is unramified at all finite primes (tower formula for the different, Neukirch, *Algebraic Number Theory*, III.2.2 and III.2.6); the predicate `D.IsBuilt`, which we have not unfolded; $1 \le l$ and $l + 2 \le k$; lower bounds in terms of $C_c$ for the grids, for $\beta_v - \alpha_v$ and for $A_0$; each $f_v$ is smooth; and $[\alpha_v, \beta_v]$ lies in the cut region.

**Theorem.** There is $C_c$ with this property. Let the data satisfy `IsBuiltPlace` with $C_c$, let each place be `Ok`, and let the two sequences $\delta$, $\delta'$ of $S$ be words (`Sz.IsWord`). Let $c$ be a cut with cutoff function $\chi$. Then for each place $v$ there are level data $L$, functions $j$, a real vector $\lambda$ and reals $C_m, \sigma > 0$ such that:

1. the model conditions `MA.HidaSetting`, `JDecay`, `JAdj` and `JEigen` of the [model setting](/entry/lemma-model/) hold for $L$, $j$, $\lambda$ and $[\alpha_v, \beta_v]$;
2. for each $\varepsilon > 0$ and each admissible word $a$, `principalHermitianLattice` at $a$ and at the cut function $f_{v,\varepsilon}$ equals $C_m$ times the model cutoff energy form of $j$ at $\sigma \varepsilon$;
3. the model system admits $a$, with the same size as in $S$.

This is `IsModelPlace` for each $v$.

## Proof

1. `chart_equations_holds` proves `ChartEqs`. In a smooth chart of the group, a function that satisfies the group equations `GEqs` (it is an eigenfunction of invariant operators written as determinants with a shifted diagonal) satisfies a finite system of differential equations with smooth coefficients. At each point, a common zero $\xi \ne 0$ of the principal symbols gives a nonzero nilpotent $\Xi$ in the Lie algebra, orthogonal to two subalgebras. The proof is `chartEqs_of_capJoints` from `capelli_words_holds`, `right_capelli_words_holds` and `left_capelli_words_holds`.
2. [`modelPlaceBuilt2_of_chartEqs`](/entry/model-place-built2-of-chart-eqs/) turns `ChartEqs` into `ModelPlaceBuilt2`.

## In the Lean code

The theorem is in [TransferSmoothAtBuiltPlace.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TransferSmoothAtBuiltPlace.lean#L9). `ModelPlaceBuilt2` is in [StatementJCT.lean](lean:Formalism/HermitianCurvature/StatementJCT.lean#L317), `IsBuiltPlace` at [line 153](lean:Formalism/HermitianCurvature/StatementJCT.lean#L153), `IsModelPlace` in [StatementJC.lean](lean:Formalism/HermitianCurvature/StatementJC.lean#L117), `ChartEqs` in [JfSmoothBuiltOfLeaves.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/JfSmoothBuiltOfLeaves.lean#L56).

The theorems below this one only pass hypotheses along: [`modelPlaceBuilt2_of_chartEqs`](/entry/model-place-built2-of-chart-eqs/), [`modelPlaceBuilt2_of_jf`](/entry/model-place-built2-of-jf/), [`modelPlaceBuilt2_of_polyS`](/entry/model-place-built2-of-poly-s/), `modelPlaceBuilt2_of_SSnRep`, `modelPlaceBuilt2_of_rotK` and `modelPlaceBuilt2_of_ssnRep`. The content is in the leaves: the Capelli word lemmas, `elliptic_regularity_weighted`, `polynomial_radial_holds` and the gauge construction. `chart_equations_holds` is also used by `global_regularity_jacobi`, so its subtree is not in the size of this theorem.

The condition $c.\chi = \chi$ is a hypothesis and again the first clause of `IsModelPlace`. In `IsBuiltPlace`, the clause $2 \le k$ follows from $1 \le l$ and $l + 2 \le k$.
