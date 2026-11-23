---
id: twisted-multiplicity-one
title: Equal cuspidal multiplicities, the entry point
kind: theorem
decl: GlobalTheory.T.twisted_multiplicity_one
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedMultiplicityOne
covers: 3685
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the multiplicity equality](/entry/twisted-multiplicity-eq/), and its proof is that theorem. It is the form that the rest of the proof calls: six declarations below [the last node of the trunk](/step/nonempty-hyps/) use it. The content is in [equal cuspidal multiplicities for unitary groups that agree at the finite places](/entry/unitary-theory-of-harish-chandra-langlands-alt/).

## Statement

The statement is word for word the statement of [the multiplicity equality](/entry/twisted-multiplicity-eq/). In short: assume ten statements named after published results (Harish-Chandra analyticity, the classification of discrete series, rapid decay of cusp forms, Harish-Chandra finiteness, trace class of the cuspidal spectrum, Dixmier-Malliavin factorisation, Flath factorisation, the Zelevinsky polynomial ring, the geometric lemma, and the cuspidality statement of Green). Let $R$ be a real datum of the extended type `RealDat3` and $F$ a face of type `Face3`, with eight conditions on them. Then $R$ has the multiplicity equality `MultEq`: cuspidal multiplicities on the unitary groups of the hermitian spaces $Y_0$ and $W_i$ are equal.

## Proof

The proof is the term `twisted_multiplicity_eq`. There is nothing else.

## In the Lean code

The theorem is at [TwistedMultiplicityOne.lean line 30](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedMultiplicityOne.lean#L30). The proof is `first | exact @twisted_multiplicity_eq | ...`, a tactic that tries three ways to apply the other theorem.

- The name is misleading. The conclusion is an equality of two multiplicities, not "multiplicity one", and no twist appears in the statement.
- The callers are in `RealGroupInputsCombined.lean`, `TwistedLocalMultiplicityEq.lean`, `HarishChandraInputsCombined.lean`, `MultiplicativeClosurePrimeMem.lean`, `GaloisRepLambdaAdicDecomposition.lean` and `CompatibleSystemPartitionLambda.lean`.
- Two of the ten hypotheses (Harish-Chandra analyticity and Flath factorisation) are not used anywhere below this theorem. See [the content entry](/entry/unitary-theory-of-harish-chandra-langlands-alt/).
