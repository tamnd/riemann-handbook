---
id: core-o-of-literal-automorphy-n
title: Derivations that kill the inertia characters kill the traces
kind: theorem
decl: UpperTheory.V.Th.core_o_of_literal_automorphy_n
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.TCoreO
covers: 855
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{OrdinaryMainCase}$ from `LiteratureRankNHypothesis`. It is step 4 of [the theorem on ordinary adjoint cocycles](/entry/ordinary-vanishing-two-of-printed-hida/): a derivation of the universal ordinary determinant ring at $x$ that kills the inertia characters kills all traces. The proof checks the inputs of the counting theorem `count` and then applies it.

## Statement

Use the Hida setting $s$, the level $V_0$ with set of places $S$, the residual representation $r$ over the coefficient ring $\mathcal{O}$ of $c$, the universal ordinary determinant ring $B$ and the arithmetic point $x \colon B \to \mathcal{O}$ of the parent entry. Let $J$ be an ideal of $B$ with $J \subseteq \ker x$ that meets `LevelIdealCondition`. Let $y$ be a point with a representation $\rho_y$ over $\mathcal{O}$, such that $x$ maps the determinant of $B$ to the determinant of $\rho_y$ and the characters of $B$ to those of $y$. Suppose $y$ meets the condition `N4`. Let $\sigma_1, \dots, \sigma_q$ lie in the subgroup $G'$, with $\operatorname{charpoly} \rho_y(\sigma_j) = \prod_i (X - a_{j,i})$ for distinct $a_{j,i}$. Suppose also `DetQ`: a polarized cocycle $z$ of $\operatorname{ad} \rho_y$ with $\operatorname{tr}(z(\sigma_j)\rho_y(\sigma_j)^k) = 0$ for all $j, k$ is a coboundary.

**Theorem.** Under `LiteratureRankNHypothesis`: let $\delta \colon B \to \mathcal{O}$ be an $\mathcal{O}$-linear derivation at $x$ with $\delta(\psi_{v,i}(g)) = 0$ for all $v$, $i$ and all $g$ in the inertia group $I_v$. Then $\delta(\operatorname{tr} g) = 0$ for every $g$.

## Proof

1. $\mathrm{CohP}$ is read off from `hN.coh`, as in the parent entry.
2. `arPl` gives a structure $T$ of type `TWGrp` with the property `TWPl`, whose elements are the $\sigma_j$. `ipEq` compares the inertia subgroups of $r$ and of the frame. We have not unfolded `TWGrp`.
3. The algebra $B$ is generated over $\mathcal{O}$ by the values of its pair, up to each power of the maximal ideal (`GenBy`). This is `CA.exists_adjoin_coeff_character_sub_mem_maximalIdeal_pow`.
4. The private lemmas `red_unip`, `unip_pow` and `rhoPLO` show that $\rho_y$ is trivial on $\mathrm{PL}_l(T.H)$. Here $\mathrm{PL}_l(H)$ is the intersection of the open normal subgroups $U$ such that each $h \in H$ has some power $h^{l^e}$ in $U$. The reason: for $h \in T.H$, $\rho_y(h)$ is unipotent mod $\mathfrak{m}$, so $\rho_y(h)^{l^{n+m}} \equiv 1$ mod $\mathfrak{m}^m$.
5. Apply `count`. Its inputs are `has_operator_statement`, `etOf` and `b1O`. `b1O` gives the bound `B1` on the number of trace functions of Selmer classes mod $\mathfrak{m}^m$. It uses `W.locCFT`, `N4` and `DetQ`. `count` needs $l \ne 2$, which comes from `s.odd`. The hypothesis of `count` on $\delta$ is only at the weight elements $b.\mathrm{wt}.\gamma_k$, and these lie in inertia by `LevelIdealCondition`.

`count` argues by contradiction. If $\delta(\operatorname{tr} g_0) \ne 0$, it combines `coc`, `trPsi` and `split` with the counting lemma `cnt` to pick an exponent $m$ that contradicts `B1`. We have not read the rest of its proof.

## In the Lean code

The theorem is in [TCoreO.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TCoreO.lean#L129). `OrdinaryMainCase` and `LevelIdealCondition` are in [ThDefs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThDefs.lean#L53). The statements `Count`, `B1`, `Et` and `OpAt` are in [OrdinaryHeckeAlgebraIntegral.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdinaryHeckeAlgebraIntegral.lean#L134). The theorem `count` is in [MapRingHomSingleMulPartialCharpoly.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/MapRingHomSingleMulPartialCharpoly.lean#L131).

The statement that `b1O` proves is named `ordinaryHeckeAlgebraIntegral`, but it is the Selmer count bound `B1`. No integrality statement for a Hecke algebra appears in it. The same file has `CoreO` at line 217. It is the same statement as `OrdinaryMainCase`, with `LevelX` in place of `LevelIdealCondition`.
