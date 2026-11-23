---
id: count-g-holds
title: The counting step for the twisted trace on a K-type, second name
kind: theorem
decl: PositivityTheory.RgBcC.RealD.countG_holds
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.RealDescent.RealLeviDescent.DiracInequalityKTypes
covers: 380
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It proves the statement `CountG` by the theorem [`countG`](/entry/count-g/) of the namespace `RealCountG`, with no other step. It is step 1 of the proof of [the twisted trace on a K-type](/entry/core-g/). The mathematics is in the entry [`countG`](/entry/count-g/).

## Statement

We use the notation of [`coreG`](/entry/core-g/). Let $\lambda \in \mathbb{Z}^n$ be non-increasing, let $E$ and $T$ satisfy `IsLefK`, and let $V$ with $E^1$, $E^2$, $\sigma$, $A$ satisfy `IsCoreMod`. Let $H$ be the finite set of weights $2\lambda + 2r$, and $V_\mu$ the space of highest weight vectors of weight $\mu$ for $E^1 + E^2$.

**Theorem** (`CountG`). If $\mathrm{Hom}_{U(n)}(E^\vee, V)$ is finite-dimensional, then:

1. each $V_\mu$ with $\mu \in H$ is $A$-stable and finite-dimensional;
2. if $\mathrm{Hom}_{U(n)}(E^\vee, V) \neq 0$, some $V_\mu$ with $\mu \in H$ is nonzero;
3. the trace of $t \mapsto A \circ t \circ T^\vee$ on $\mathrm{Hom}_{U(n)}(E^\vee, V)$ is $2^n \sum_{\mu \in H} \operatorname{tr}(A \mid V_\mu)$.

## Proof

The proof is the term `GlobalTheory.CompanionTheory.RealCountG.countG`. See [`countG`](/entry/count-g/) for its proof: the Hom space splits as a product over $\mu \in H$ of spaces $\mathrm{Hom}(E^\vee_\mu, V_\mu)$, and the trace of $T^\vee$ on each $E^\vee_\mu$ is $2^n$.

## In the Lean code

The theorem is in [DiracInequalityKTypes.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/DiracInequalityKTypes.lean#L9). The statement `CountG` is in [HighestVectorsRegularLine.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/HighestVectorsRegularLine.lean#L63).

The module name does not describe this theorem. The file also holds three other short proofs: `dirac_inequality_k_types`, a second name for a lemma of `DiracKType0`; `adm_least_zero_holds`; and `adm_least_holds`. The last name is declared again in [MultGOfMultFor.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/MultGOfMultFor.lean#L13), in the same namespace, and `CoreG.lean` imports both files.
