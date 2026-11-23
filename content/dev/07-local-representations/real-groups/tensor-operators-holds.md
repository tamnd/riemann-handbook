---
id: tensor-operators-holds
title: Products with dual Weyl elements are given by polarization words
kind: theorem
decl: Formalism.MainNotions.TestSideWords.tensor_operators_holds
module: Formalism.SharpRestriction.GrowthBounds.TwistedSubstitution.OperatorWeightBoundHolds
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves the operator fact `TenOp` with no hypotheses. Under the Fock pairing, it moves a product with an element of a tensor product of dual Weyl modules onto a sum of polarization words. [`stmtE_of_MP`](/entry/stmt-e-of-mp/) uses it to close the hypothesis `TenOp` of [`stmtE_of_TenMP`](/entry/stmt-e-of-ten-mp/). The use of `TenOp` is in [`stmtE_of_TenNS`](/entry/stmt-e-of-ten-ns/).

## Statement

Let $K$ be a field of characteristic $0$ and let $n', m$ be natural numbers with $m \ge 1$. Polynomials have the variables $X_{t,i}$ for $t < n'$ and $i \le m$. For a letter $(t,(i,j))$, the operator is $X_{t,i}\,\partial/\partial X_{t,j}$, and `opWord l` applies the letters of the word $l$ in turn. The Fock pairing is $\langle f, g\rangle = \sum_\alpha f_\alpha g_\alpha \prod_k \alpha_k!$. The map $\Theta_0$ (`Th0`) is a substitution that depends on the flags `vec`. `Pol d` is the space of polynomials of multidegree $d$.

**Theorem.** Fix `vec`, a set of blocks $T$, a multidegree $d$, a bound $c$, and weights $\nu_t$ such that each $\nu_t$ is antitone, $\nu_t(0) \le c$ for $t \in T$, and $\nu_t = 0$ for $t \notin T$. Let $\beta, s$ be in `tensorLat` of the dual Weyl modules of weights $\nu_t$. Then there are a finite set $L$ of words and coefficients $a_l \in K$ with these properties:

1. each word has its letters in blocks of $T$ and uses each block at most $c$ times;
2. for each $G \in$ `Pol d`, the sum $G' = \sum_{l \in L} a_l\, \mathrm{opWord}_l(G)$ is in `Pol d`, and
$$\langle \Theta_0(G)\, s,\ \Theta_0(H)\, \beta\rangle = \langle \Theta_0(G'),\ \Theta_0(H)\rangle \quad \text{for all } H \in \texttt{Pol}\ d.$$

## Proof

The proof has two stages.

1. **One block.** `onePos_of_opBound` proves `OnePos`, the same fact for a single block with words of length at most $c$. Its inputs:
   - `OpBound`: an operator space that is stable under commutators with the $E_{ab} = X_a\,\partial_b$, and that is spanned by weight vectors with weights at most $c$, is in the span of words in the $E_{ab}$ of length at most $c$. This is `operator_words_bound`, proved from `vanishingOnQuadric`.
   - `RestTheta`: the row operators commute with `theta` up to the change `TE`. This is `row_letter_rule`.
   - `RestWt`: `dualWeyl` has a spanning set of weight vectors with weights at most $\nu(0)$. This is `dual_weyl_weights_bounded`. It comes from `bideterminant_span_holds`, which puts `dualWeyl` in the span of bideterminants with strictly increasing rows. A minor with a repeated row is $0$, and the other minors are sorted up to sign.
   - The facts `restAdj`, `restStab`, `restRep` and `restRep2`, which we have not unfolded.
2. **Tensor products.** `adjointTensorOfSingle_valid` takes the block form of the Fock pairing, `fockRBlock`, and `OnePos`, and gives `TenOp`.

## In the Lean code

The theorem is at [line 84](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/OperatorWeightBoundHolds.lean#L84), and the two stages are at [lines 74 to 80](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/OperatorWeightBoundHolds.lean#L74). `TenOp` is in [FirstWeightLeConductor.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/FirstWeightLeConductor.lean#L16), `OpBound` in [OpBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/OpBound.lean#L36), and `OnePos` in [OnePosDef.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/OnePosDef.lean#L18).

`adjointTensorOfSingle_valid` has the type `PI.TenOp`, which is stated with copies of these definitions in [FockRBlock.lean](lean:Formalism/PeriodIntegrals/FockRBlock.lean#L99). The proof uses that the copies agree by definition. On the right side of the identity, $\beta$ is absent. The words depend on $s$ and $\beta$ but not on $G$ or $H$.
