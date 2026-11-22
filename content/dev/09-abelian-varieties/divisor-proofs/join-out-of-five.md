---
id: join-out-of-five
title: JoinOut from five results on complex multiplication and zeta values, by composition
kind: theorem
decl: GlobalTheory.JoinFun.joinOut_of_five
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.JoinOutOfFive
covers: 1598
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `JoinOut` from five published results. Its only user is [JoinOut from the literature](/entry/join-out-of-literature/), which supplies the five results. The theorem itself is a composition: it passes its hypotheses to four lemmas and adds nothing. The real content is in those lemmas, which have no entries of their own.

## Statement

Suppose that five statements hold: `EllipticMainTheoremCM` (the main theorem of complex multiplication for elliptic curves), `HilbertClassFieldJ` ($K(j(\mathcal{O}_K))$ is the Hilbert class field of $K$), `SiegelKlingenDeligneRibet` (rationality and congruences of values $L(1-k)$ over a totally real field), `PartialZetaFunctionalEquation` and `HeckeTateFunctionalEquation`. Then `JoinOut` holds.

`JoinOut` is the conjunction `ToricDenominator ∧ Transport ∧ TwistedTransport ∧ ZetaDenominators ∧ Refl`. We have not unfolded the conjuncts here. The entry [JoinOut from the literature](/entry/join-out-of-literature/) describes them.

## Proof

The proof applies `toricPeriodZetaStatements_of_jetIntegrality_algebraicity` to the five hypotheses and to three intermediate statements on lattice values:

1. `JetInt`, an $\ell$-adic integrality bound for iterated derivatives at $0$ of the defining sums `IsDefSum`, from `cmLatticeDividedPowerJetIntegrality_of_ellipticCM`;
2. `LatAlg`, algebraicity of the normalized lattice value `coordIn`, from `latticeValueIsAlgebraic_of_ellipticCM_theorems`;
3. `LatConj`, the action of $g \in \operatorname{Aut}(\mathbb{C})$ on that value under a transport of lattices, from `latticeValueConjugation_of_ellipticCM_theorems`.

Each of these four lemmas is a one-line wrapper. They call `JoinFun.joinOut_of_jetInt`, `JetIntElliptic.jetInt`, `RoadELatAlg.latAlg_of_siegelKlingen` and `LatConjEll.latConj`. The first of these derives the two integrality statements `LatIntRam` and `LatIntUnr` from `JetInt` and calls `JoinFun.joinOut_of_lat`, whose proof we have not opened.

## In the Lean code

The theorem is at [JoinOutOfFive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/JoinOutOfFive.lean#L15). `JoinOut` is at [HypothesisBundleConversions.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HypothesisBundleConversions.lean#L7). `JetInt` is at [JetAnalytic.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/JetAnalytic.lean#L239), and `LatAlg` and `LatConj` are at [TorsTransport.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/TorsTransport.lean#L76).

- The three intermediate lemmas do not use all their hypotheses. [`jetInt`](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CMLatticeDividedPowerJetIntegralityOfHyp.lean#L251) uses only `PartialZetaFunctionalEquation`. [`latAlg_of_siegelKlingen`](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeValueIsAlgebraicOfEllipticCMTheorems.lean#L73) and [`latConj`](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeValueConjugationOfEllipticCMTheorems.lean#L204) use only `SiegelKlingenDeligneRibet` and `PartialZetaFunctionalEquation`. None of the three uses the theorems on complex multiplication or on the Hilbert class field, although their names say "of elliptic CM".
- The wrappers have the form `first | exact @X | exact X | (intros; apply X <;> assumption)`.
- The name "join out" says nothing about the content.
