---
id: cnt-trace-definite-forms-identity
title: The sum over definite pairs is an automorphic trace (second name)
kind: theorem
decl: UpperTheory.Gal.Cnt.trace_definite_forms_identity
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.DefiniteTraceForms.WeightedCountDefiniteUnitary
covers: 345
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [GlobalTheory.LKDef.trace_definite_forms_identity](/entry/lkdef-trace-definite-forms-identity/). Its proof is that theorem, with no change. It is the second group-side input $h_2$ of [ksHodge_of_geo](/entry/ks-hodge-of-geo/). With [the weighted count](/entry/weighted-count-definite-unitary/) it turns the fixed-point count into an automorphic trace.

## Statement

Let $G$ be a group datum with exactly one indefinite infinite place, and let definite pairs, their terms and `dSumIrr` be as in [the weighted count](/entry/weighted-count-definite-unitary/). A *definite form* is $\beta \in C^\times$, fixed by the involution, with local conditions and with $H_v\psi_v(\beta^{-1})$ definite as for definite pairs. Its unitary group $\Gamma_\beta$ maps to $G(\mathbb{A}_f) \times G_p$.

**Theorem** (`TraceDefinitePairsEqAutomorphicTrace`). Let $\xi$ be a finite-dimensional complex representation of $C^\times \times \mathbb{Q}^\times$, and $\mathrm{wt}$ a function of polynomials with $\operatorname{tr}\xi(y) = \mathrm{wt}(P_y)$ for each regular $y$. Let $f$ and $f'$ be bi-invariant test functions away from $p$ and at $p$. Assume that the orbital sums of $f \otimes f'$ vanish at each $y$ that is not regular with irreducible minimal polynomial. Then

$$\mathrm{dSumIrr}(\mathrm{wt}, f, f') = \sum_{[\beta]} \operatorname{tr}\bigl(T_{f \otimes f'} \mid \mathcal{A}_\beta(\xi)\bigr),$$

where $\beta$ runs over classes of definite forms and $\mathcal{A}_\beta(\xi)$ is the space of functions $\varphi$ on $G(\mathbb{A}_f) \times G_p$ with $\varphi(\gamma g) = \xi(\gamma)\varphi(g)$ for $\gamma \in \Gamma_\beta$, right invariant under the level (`dTrace`).

## Proof

It is `GlobalTheory.LKDef.trace_definite_forms_identity`. See [its entry](/entry/lkdef-trace-definite-forms-identity/).

## In the Lean code

The theorem is in [WeightedCountDefiniteUnitary.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/DefiniteTraceForms/WeightedCountDefiniteUnitary.lean#L13). The statement is in [TraceDefinitePairsEqAutomorphicTrace.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/TraceDefinitePairsEqAutomorphicTrace.lean#L87), and the original proof in [LieModelBaseChangeMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieModelBaseChangeMap.lean#L14). The trace `heckeTrace` is set to $0$ when no Hecke operator of the given form exists. We have not checked that one always exists here.
