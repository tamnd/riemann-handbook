---
id: p-adic-monodromy-theorem-matrix-form
title: The p-adic monodromy theorem in matrix form (named form)
kind: theorem
decl: GlobalTheory.T.pAdicMonodromyTheorem_matrixForm
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.PAdicMonodromyTheoremMatrixFormStatement
covers: 1362
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`PMon.matThm_holds`](/entry/mat-thm-holds/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its parent in the spine is [`deRham_potentiallySemistable`](/entry/de-rham-potentially-semistable/), which turns it into the $p$-adic monodromy theorem for representations on vector spaces.

## Statement

The statement is the proposition `MatThm`. Let $\ell$ be a prime, and let $P$ and $A$ be period data with a tie `LocTied l P A` to Fontaine's rings. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r > 0$, and $\rho \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ a homomorphism. Assume `IsRat r ρ`: the entries of $\rho$ are continuous and fixed by $\mathrm{Frob}^r$, and the elements of $\mathbb{Q}_\ell^{\mathrm{ur}}$ fixed by $\mathrm{Frob}^r$ lie in $K$. Assume `AdmDR P ρ`: for each $m$ there is $Q \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $\mathrm{Frob}^m(\rho(g))\,g(Q) = Q$ for all $g$. Then `AdmSt P ρ` holds: there are a finite extension $K' \supseteq K$ and $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ with $\rho(g)\,g(Q) = Q$ for all $g \in G_{K'}$.

The entry [`matThm_holds`](/entry/mat-thm-holds/) explains these conditions and the proof.

## Proof

The proof is the term `GlobalTheory.PMon.matThm_holds`. Nothing else happens.

## In the Lean code

The theorem is in [PAdicMonodromyTheoremMatrixFormStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PAdicMonodromyTheoremMatrixFormStatement.lean#L7). The proof is the tactic `first | exact @GlobalTheory.PMon.matThm_holds | ...`, and the first branch closes the goal. The file also sets `maxHeartbeats` to 1000000. `MatThm` is defined in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L11).
