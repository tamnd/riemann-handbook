---
id: exists-std-family
title: Haar measures on adelic unitary groups that fit the one-vector steps
kind: theorem
decl: GlobalTheory.GaugeEx.exists_std_family
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsIsGaugeOfIsCMExt
covers: 302
status: drafted
drafted_by: writer@claude
---
This theorem gives Haar measures on the adelic unitary groups $U(J)(\mathbb{A}_F)$, one for each Hermitian matrix $J$, with positive scalars that make the measures fit together when one passes from $J$ to the orthogonal complement of one vector. Its only caller is [`exists_isGauge_of_isCMExt`](/entry/exists-is-gauge-of-is-cmext/), which makes a gauge family from them for [`exists_isGauge`](/entry/exists-is-gauge/).

## Statement

Let $E/F$ be a CM extension with complex conjugation $\sigma$: $F$ is totally real, $E$ is totally complex, $[E:F] = 2$, and $\tau(\sigma x) = \overline{\tau(x)}$ for each embedding $\tau \colon E \to \mathbb{C}$ (`IsCMExt`). For an $M \times M$ matrix $J$ over $E$ with $\sigma(J_{ji}) = J_{ij}$ and $\det J \neq 0$ (`IsHermND`), let $H_J = U(J)(\mathbb{A}_F)$ be the subgroup of $\mathrm{GL}_M(\mathbb{A}_F \otimes_F E)$ that preserves $J$. Let $s$ be a *standard measure package* (`StdMeas`) of additive Haar measures at the infinite places and at each finite place, for $E$ and for $F$, with the local integers of mass 1.

A *step datum* (`StepData`) is $(J, x, \beta, B, J')$: $J$ of size $M+1$, a vector $x \in E^{M+1}$ with $h_J(x,x) = \beta \neq 0$, a matrix $B$ of size $(M+1) \times M$ whose columns are orthogonal to $x$, and $J' = B^* J B$ nondegenerate. For measures $\mu$ on $H_J$ and $\mu'$ on $H_{J'}$, the *step relation* (`StepRel`) says: for each product measure $\nu$ on the quadric $\{y : q_J(y) = \beta\}$ built from $s$ (`IsStdX`) and each isomorphism $e$ from the stabilizer of $x$ in $H_J$ to $H_{J'}$ that is compatible with $B$, we have

$$\int_{H_J} f \, d\mu = \int \int_{\mathrm{Stab}(x)} f(t(y)\, h) \, d(e^{-1}_*\mu')(h) \, d\nu(y)$$

for each measurable $f \ge 0$ and each section $t$ of the orbit map $g \mapsto gx$ (`IsCompatible`).

**Theorem.** There are measures $\mu_{M,J}$ on $H_J$ and positive reals $\alpha_{M,J}$ such that:

1. each $\mu_{M,J}$ with $J$ Hermitian nondegenerate is a Haar measure (`IsHaar`);
2. for $J' = P^* J P$ with $P \in \mathrm{GL}_M(E)$, there is an isomorphism $H_J \to H_{J'}$ compatible with $P$, and each such isomorphism carries $\mu_{M,J}$ to $\mu_{M,J'}$ (`BasisInv`);
3. $\alpha_{M, P^* J P} = \alpha_{M,J}$;
4. for each step datum with $M \ge 2$, the measures $\alpha_{M+1,J}\, \mu_{M+1,J}$ and $\alpha_{M,J'}\, \mu_{M,J'}$ satisfy the step relation.

## Proof

1. `exists_basisInvariant_haar_family_adelicUnitary` gives a family $\mu$ with properties 1 and 2.
2. `exists_const` gives for each step datum a positive constant $c(J,x,B)$ such that $c\,\mu_{M+1,J}$ and $\mu_{M,J'}$ satisfy the step relation. It compares $\mu_{M+1,J}$ with the unique Haar measure in the step relation with $\mu_{M,J'}$ (`exists_unique_oneVectorStep_haarMeasure`). It depends only on $(J,x,B)$ (`stepData_unique`).
3. `exists_coboundary_of_invariant_unitary_step_constants` writes $c(J,x,B) = \alpha_{M+1,J} / \alpha_{M,J'}$, with $\alpha$ invariant under $J \mapsto P^*JP$. It needs two facts: $c$ does not change under a change of basis (property 2 and `unitaryOneVectorStep_compatible_changeOfBasis`), and two chains of two steps from $J$ to the same $J_0$ give the same product of constants (`unitaryStabilizer_measure_independent_of_path`). In both cases `smul_haar_inj` turns $c\mu = c'\mu$ into $c = c'$.
4. Scale the relation of step 2 by $\alpha_{M,J'}$ (`StepRel.smul`) and use $\alpha_{M+1,J} = c\,\alpha_{M,J'}$.

## In the Lean code

The theorem is in [ExistsIsGaugeOfIsCMExt.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsGaugeOfIsCMExt.lean#L112). `StepData` and `StepRel` are in [T2SpaceNumberFieldInfiniteAdeles.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/T2SpaceNumberFieldInfiniteAdeles.lean#L141). `IsHaar` and `BasisInv` are in [FrameTransport.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GeneralLinearActions/FrameTransport.lean#L29).

`exists_const` (line 77), `smul_haar_inj` (line 56) and `StepRel.smul` (line 45) are in the same file. The four other lemmas are one-line wrappers of lemmas in `GaugeRef`, `GaugeAlg`, `GaugeEx` and `GaugeSquare`, whose proofs we have not opened.

The theorem does not scale $\mu$; the parent scales by $K_M \alpha_{M,J}$, with $K_M$ from `quadricFibreMeasure_eq_smul_normalisedProduct`.
