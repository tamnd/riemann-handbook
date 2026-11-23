---
id: exists-fan-order-ideal-theta-compactification
title: A boundary ideal with the valuations of a fan function (statement form)
kind: theorem
decl: GlobalTheory.T.exists_fanOrder_ideal_thetaCompactification
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFanOrderIdealThetaCompactificationStatement
covers: 444
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It proves the statement $\mathrm{IdealSt}$ by [`idealSt_holds`](/entry/ideal-st-holds/), which has the real content. Its one user is [`poinSt`](/entry/poin-st/), which takes the ideal from it in step 1 and then blows $Z$ up along that ideal.

## Statement

Use the theta compactification $(Z, i)$ of the Siegel moduli scheme $X$, the traits and the condition `ValOn` as in [`poinSt`](/entry/poin-st/).

**Theorem** ($\mathrm{IdealSt}$). Let $g \geq 1$, let $n \geq 3$ be odd, and let $(Z, i)$ be a theta compactification over $\mathbb{Z}[\zeta_n, 1/n]$. Let $\varphi$ be a polarization function for $g$. Then there are $d \geq 1$ and an ideal sheaf $J$ on $Z$ such that the support of $J$ does not meet $i(X)$ and `ValOn` holds for $(i, J, d)$: for each trait with uniformizer $\varpi$ and form $\beta$, and each $\xi \colon \operatorname{Spec} V \to Z$ that extends $i \circ y$, we have $\xi^* J = (\varpi^{a})$ with $a = d\,\varphi(\beta)$.

## Proof

The proof applies `GlobalTheory.Poinc.idealSt_holds`.

## In the Lean code

The theorem is in [ExistsFanOrderIdealThetaCompactificationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFanOrderIdealThetaCompactificationStatement.lean#L10). The proof is `first | exact @GlobalTheory.Poinc.idealSt_holds | ...`, a tactic that tries the alias in three forms. The type is `IdealSt`, defined in [IsThetaCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsThetaCompact.lean#L80). A second definition with the name `IdealSt` is in `PointShiftSt.lean`, in another namespace; it is not the one used here.
