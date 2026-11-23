---
id: back-of-line-formula
title: The L² embedding from fast decay, given the line integration formula
kind: theorem
decl: CompanionTheory.RgExh.Dec.L.back_of_lineFormula
module: CompanionTheory.RealGroups.DiscreteSeries.DiscreteSeriesClassification.DiscreteSeriesExhaustion.MatrixCoefficientDecay.HilbertSchmidtDecay.BackwardOfLineFormula
covers: 301
status: drafted
drafted_by: writer@claude
---
This theorem proves `Back` from one hypothesis, the integration formula `LineFormula`. [Its parent](/entry/backward-of-line-formula/) states `Back` and supplies the formula. The proof is a pass-through: it calls `back_of_inputs` with the proved statement `PolynomialNilpotentPath`.

## Statement

Let $A$ and $P_A$ be as in [the decay estimate](/entry/decay-estimate/). `LineFormula` says: for each Haar measure $\nu$ on $P_A$ and each continuous $\tau \colon G \to \mathbb{R}$ with $\tau(x \exp(tA)) = \tau(x) + t$ on $P_A$, there is $\kappa \in (0, \infty)$ such that for each measurable right $K$-invariant $F \geq 0$ on $G$,
$$\int_G F \, dg = \kappa \int_{\{x \in P_A : 0 \leq \tau(x) < 1\}} \int_{\mathbb{R}} F(x \exp(tA)) \, e^{2\rho_A t} \, dt \, d\nu(x).$$

**Theorem.** `LineFormula` implies `Back`.

## Proof

`back_of_inputs` applies `back_of` to `SA.assembly_of` and ten statements. The argument of `assembly_of` runs as follows; we have not unfolded its inputs.

1. `Growth` gives $M$ with $\int_G |f|^2 \, \|g\|_{\mathrm{hs}}^{-M} \, dg < \infty$ for each coefficient $f$ of the end module.
2. `Geo` gives finitely many $A_j$, with functions $\tau_j$ and sets $U_j$ that cover the set where $\|g\|_{\mathrm{hs}} > R_0$.
3. `PolyNilPath` gives a monic $p_j$ with $p_j(A_j) u$ in the span of $Y v$, where each $Y$ is a sum of eigenvectors of $\operatorname{ad} A_j$ for the eigenvalues $-1$ and $-2$ (`nilpC`). This gives a chain of linear differential equations along $t \mapsto x\exp(tA_j)$.
4. `AbsoluteL2Bound`, with `LineFormula` for each $A_j$ and the decay hypothesis of `Back`, improves the exponent $-M$ to $0$. So each coefficient is in $L^2(G)$.
5. `Pack` turns this into `L2Embedding`.

## In the Lean code

The theorem is in [BackwardOfLineFormula.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/BackwardOfLineFormula.lean#L20). `LineFormula` and `PolyNilPath` are in [AbsoluteL2Bound.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/AbsoluteL2Bound.lean#L73), and `assembly_of` in [HasCharPath.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/DecayAssembly/HasCharPath.lean#L20).

- `PolynomialNilpotentPath` is proved with `first | exact ... | ...`, three tries of the same lemma `PolyNilGrad.polyNilPath` ([PolynomialNilpotentPathStatement.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/PolynomialNilpotentPathStatement.lean#L6)).
- We have not unfolded `Formalism.REAL.hs`, written $\|g\|_{\mathrm{hs}}$ above.
