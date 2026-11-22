---
id: unitary-theory-of-harish-chandra-langlands-alt
title: Equal cuspidal multiplicities for unitary groups that agree at the finite places
kind: theorem
decl: UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.UnitaryThetaCorrespondenceOfHyp
covers: 3683
status: drafted
drafted_by: writer@claude
---
This theorem compares cuspidal multiplicities on the [[unitary groups|0R9R0Y1HDK]] of two hermitian spaces $Y_0$ and $W_i$, given an isometry over the finite adeles. It has the content of a chain of three theorems. [The multiplicity equality](/entry/twisted-multiplicity-eq/) calls it, and [its renaming](/entry/twisted-multiplicity-one/) is used below [the last node of the trunk](/step/nonempty-hyps/). The proof compares trace formulas.

## Statement

Let $D$ be a datum (`D7`) with a CM field $E$ over a totally real field $F$. For a hermitian space $V$ of the datum, let $G_V^f$ (`GfC V`) be the subgroup of its adelic unitary group with trivial archimedean component. The datum has spaces $Y_0$ (`Yc D 0`) and $W_i$ (`Wc D i`) for $i < m$. A real datum $R$ (`RealDat`) fixes, among other data, a family $\theta$ and models $M_W(i)$ on $W_i$ of [[discrete series|9AB7HYGPEK]] representations at the infinite places.

For a discrete series model $M$ on $V$ and a representation $\sigma$ of $G_V^f$, the number $m(\sigma, M)$ (`cuspMult`) is the dimension, as a cardinal, of the space of $G_V^f$-maps from $\sigma$ into the space `allMaps θ M` of the representation `finRep M`. We have not unfolded `Mult`, which defines `allMaps`.

**Theorem.** Assume the ten published-result statements listed in [the multiplicity equality](/entry/twisted-multiplicity-eq/). Let $R$ be a real datum, $F$ a face, and suppose that `Given R F` holds (six conditions, see the same entry). Then `MultEq R` holds: for each $i < m$, each discrete series model $M_0$ on $Y_0$, each matrix $j$ and each isomorphism of topological groups $\Phi \colon G_{Y_0}^f \to G_{W_i}^f$ such that

1. $j^{*} J_{W_i}\, j = J_{Y_0}$ for the Gram matrices over $\mathbb{A}_{F,f} \otimes E$,
2. $\Phi(g)_f\, j = j\, g_f$ for all $g$,
3. $j$ carries the frame of $Y_0$ to the frame of $W_i$ up to an integral matrix that is $1$ at a finite set of places,

and for each irreducible admissible representation $\sigma$ of $G_{Y_0}^f$ that is good (`IsGoodRep`: it has a nonzero vector, fixed by a level group, that satisfies one Hecke relation), we have

$$m(\sigma, M_0) = m(\sigma \circ \Phi^{-1}, M_W(i)).$$

## Proof

The proof is one call to `multEq_of_sides`. That lemma needs nine inputs. Five are built here:

1. `LocalPC`, from [`localPseudoCoefficientExistence_unitaryGroup`](/entry/local-pseudo-coefficient-existence-unitary-group/), with no hypothesis. Each discrete series representation of $U(J_\varepsilon)$ with a weight that meets a gap condition has a pseudo-coefficient.
2. `SpecTraceX`, from `PsCo.SpecX.main` with the discrete series classification and the trace class statement. For admissible test data $f$, the operator `RopG` of $f$ (not unfolded here) has trace $\sum_i m(\sigma_i)\, c_i$, where $c_i$ is the trace of $\sigma_i(f_f)$ and $m$ is the cuspidal multiplicity `mCuspDS`.
3. `Separation`, from `trace_separation_of_iwahori_trace`, with `iwahoriTrace` and `exponentsSeparate` (the geometric lemma and the Zelevinsky ring). If $\sum_i a_i \operatorname{tr} \sigma_i(f_f) = 0$ for all test functions of a given type, then $a_i = 0$ for each $\sigma_i$ that has a vector of that type.
4. `EllTraceX`, from `ellipticSideDirect` with the trace class statement. The same trace is the integral of the elliptic kernel.
5. `EllipticPartX`, from `ellipticT`, with no hypothesis. That integral is a finite sum of orbital terms, one for each characteristic polynomial.

The other four inputs are hypotheses: rapid decay, Harish-Chandra finiteness, Dixmier-Malliavin and the statement of Green. Inside `multEq_of_sides`, `trCusp'_of_steps` joins the five facts into `TRCusp'`. Then `multEq_of_trCusp'` gets `MultEq`, with the statement of Green to find a type vector in $\sigma$. We have not unfolded `TRCusp'` or `TraceEqX`.

## In the Lean code

The theorem is at [UnitaryThetaCorrespondenceOfHyp.lean line 15](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/UnitaryThetaCorrespondenceOfHyp.lean#L15). `multEq_of_sides` is at [TraceEqXOfGeomExpansionX.lean line 555](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceEqXOfGeomExpansionX.lean#L555), and `MultEq` at [FinRepApply.lean line 118](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FinRepApply.lean#L118).

Odd points:

- Two hypotheses are not used. The proof opens with `intro _ ds rd hf tc dm _ ze gl gc`, so `HarishChandraAnalyticity` and `FlathFactorisation` are dropped.
- The name is misleading. No Langlands statement appears in the hypotheses or in the conclusion. The file name speaks of a theta correspondence, and none appears.
- `iwahoriTrace` comes from `BorelCasselman_holds`, a proof in the code of the published-result statement `BorelCasselman`. So that input is not a hypothesis.
