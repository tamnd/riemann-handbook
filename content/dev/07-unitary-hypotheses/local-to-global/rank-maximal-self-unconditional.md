---
id: rank-maximal-self-unconditional
title: The rank maximal condition for self-conjugate charts holds outright
kind: theorem
decl: Formalism.L2.FormalSeriesBounds.rank_maximal_self_unconditional
module: Formalism.LocalToGlobal.CharacterGerms.RankMaximalSelfUnconditional
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem proves `RankMaximalSelfOfNondegenerate` with no hypothesis. The word "unconditional" means that the five inputs of the general lemma are all proved. It is a pass-through: the real argument is in `rank_maximal_self_core`. Its user [`labelSetGeo_of_even_of_rankOK_of_not_dvd_discr`](/entry/label-set-geo-of-even-of-rank-ok-of-not-dvd-discr/) gives it to `rank_maximal_self_charts_of_nondegenerate`, to fill one field of the row data.

## Statement

Let $C$ be a field of characteristic $0$ with a valuation $V$ at a prime $l$, and $Y$ a formal group chart over $C$ (`FBChart`), with a logarithm and an exponential that are inverse to each other. Let $p$ be self-conjugate data on $Y$ (`SelfData`): embeddings indexed by $\mathbb Z/d$ with a shift $h$ that matches the conjugation, eigenvectors and $2 \times 2$ matrices.

**Theorem.** If $Y$ is nondegenerate modulo the maximal ideal (`NDG`) and the raw chart `Y.rawSelf p` satisfies `RankHyp`, then for every family `Hc` of chart hypotheses, `RankMaximalCondition Hc` holds.

`RankMaximalCondition` says: if `AltC` holds and `big g a`, then for each curve $(w, x)$ that is `Good` at $a$, if all coordinates $l \cdot x_1(j)$ lie in the maximal ideal, then all $w_c$ lie in the maximal ideal. We have not unfolded `RankHyp`, `CartHyp` or `IsCurve`.

## Proof

The proof is one line: `rank_maximal_self_of_eigen` applied to `first_vanishing_core`, `funEqCore_holds`, `curve_linear_term_unconditional`, `aLinAdj_holds` and `keyEig_holds`. That lemma turns `KeyEigSt` into `ProjLieSelfSt` (`projLieSelf_of`), then `noLinSelf_of` gives `NoLinSelfSt`, and `rank_maximal_self_core` concludes. `rank_maximal_self_core` argues by contradiction from some $w_c$ outside the maximal ideal.

## In the Lean code

The theorem is at [RankMaximalSelfUnconditional.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RankMaximalSelfUnconditional.lean#L11). The statement is in [RowTieSelfCuts.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RowTieSelfCuts.lean#L48) and `RankMaximalCondition` in [RowTieDefs.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RowTieDefs.lean#L165). The chain is in [RankMaximalSelfOfProjection.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RankMaximalSelfOfProjection.lean#L16) and [RankMaximalSelfCore.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RankMaximalSelfCore.lean#L101).

A second user is [RowTieMainS.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RowTieMainS.lean#L57).
