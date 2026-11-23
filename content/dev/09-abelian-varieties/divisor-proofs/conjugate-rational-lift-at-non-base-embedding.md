---
id: conjugate-rational-lift-at-non-base-embedding
title: The conjugate of a rational theta lift at an embedding over K
kind: theorem
decl: GlobalTheory.ConjRatLiftFive.conjugateRationalLift_at_nonBaseEmbedding
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ConjugatesOfRationalThetaLiftFromCharacterisatio
covers: 461
status: drafted
drafted_by: writer@claude
---
This theorem proves the second part of [the conjugates of a rational theta lift](/entry/conj-rat-lift5/) at an embedding $\sigma$ over $K$ that is not the base embedding $\sigma_0$. It builds a conjugate datum at $\sigma$ from the characterisation clauses, and then sends the real computation to [`conj_lift5`](/entry/conj-lift5/). We use the notation of the parent entry.

## Statement

**Theorem.** Assume the hypotheses of the [parent entry](/entry/conj-rat-lift5/) at the index $i$, and the three facts that its proof derives: the forms evaluate, evaluation at the unit vector is injective, and $j_{\sigma_0}$ is injective. Let $c_0^L$ be a base datum, tied to $R$ by $\mathrm{Comparison}_2$. Let $\sigma$ be over $K$ with $\sigma \neq \sigma_0$. Then $\mathrm{ConjAt}(R, i, \sigma, ph, c_0^L)$ holds.

## Proof

The proof has three parts.

1. **A conjugate datum.** The pins of the oscillator models give a second base datum $c_0^{L\prime}$ with its own comparison. Since $\sigma$ is over $K$, it is a good embedding (`overK_iff_good_ofFive`), and the tie gives the character $\mu'$ at $\sigma$. The clauses of `conjugateCharacters_embeddings_of_characterisation` give a conjugate character $\eta'$ and a Weil datum $\omega$. Then `hypConj5` gives the conditions $\mathrm{HypConj}$ on $(\mu', \eta')$. The clauses of `conjugateLift_of_characterisationClauses` give the forms $(c, c_1, H, j)$, a theta vector $(f_0, f, B)$ and a theta lift $th_P$. `exists_io_conj_ofFive` gives the isomorphism $io$. Together these are a $\mathrm{LiftData}$.
2. **The computation.** [`conj_lift5`](/entry/conj-lift5/) turns this datum into a theta lift $th$ with the projection identity, a phase operator $U$, a central $z$ and $\kappa$ with $|\kappa| = 1$, such that $U(j_\sigma y) = \kappa \, g_\sigma(z) \, th(j(x))$ for each rational lift $y$ of $x$.
3. **Back to $c_0^L$.** The third clause of `conjugateLift_of_characterisationClauses` moves the forms from $c_0^{L\prime}$ to $c_0^L$. Then `conjugateRationalLift_at_embedding_of_datum` assembles $\mathrm{ConjAt}$. It gets the central shift $\zeta$ from `centralShift_phase_conjReadings_fiveClauses`. It uses `lift_unique5` to show that each other conjugate datum gives the same identity, with a second phase of norm 1.

## In the Lean code

The theorem is in [ConjugatesOfRationalThetaLiftFromCharacterisatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatio.lean#L192). `LiftData` and `isConjLift_iff` are in [ReadingsExistRow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReadingsExistRow.lean#L39). `ConjAt` and `IsConjDatum` are in [WeilGramSignature.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilGramSignature.lean#L137).

The hypothesis $\sigma \neq \sigma_0$ is used once, to make the clause "$\sigma = \sigma_0$ implies $u = 1$" of $\mathrm{ConjAt}$ vacuous. The call to `conj_lift5` uses the second base datum, not the one in the statement. The given $\mathrm{Comparison}_2$ enters only in step 3. The cited characterisation clauses are theorems in the `T` namespace, not hypotheses. We have not unfolded their proofs.
