---
id: fundamental-lemma-lattice-degree-one
title: The lattice modification lemma in degree one (named form)
kind: theorem
decl: GlobalTheory.T.fundamentalLemmaLattice_degreeOne
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FundamentalLemmaLatticeDegreeOneStatement
covers: 576
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`FLOne.flAt_one`](/entry/fl-at-one/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its parent in the spine is [`flAt_all`](/entry/fl-at-all/), which proves the same statement for every $r$ by applying this case to a matrix of size $n \times r$.

## Statement

The statement is `FLAt 1`. Let $U \in \mathrm{GL}_n(B_{\mathrm{dR}})$ have entries in $B_{\mathrm{dR}}^+ = \mathrm{Fil}^0$, and the same for $U^{-1}$. Let $x \ne y$ be two column indices. Assume that column $x$ of $U$ is linearly independent modulo $\mathrm{Fil}^1$ over the elements of $\mathbb{Q}_\ell^{\mathrm{ur}}$ fixed by the Frobenius. Then there are $A \in \mathrm{GL}_n(B_{\mathrm{cris}})$ with $\varphi(A) = A$ and $W \in \mathrm{GL}_n(B_{\mathrm{dR}}^+)$ with

$$A = U \, D \, W, \qquad D = \operatorname{diag}(d_j), \quad d_x = t^{-1}, \ d_y = t, \ d_j = 1 \text{ else},$$

where $A$ on the left is read in $B_{\mathrm{dR}}$ through $B_{\mathrm{cris}} \subset B_{\mathrm{dR}}$. The entry [`flAt_one`](/entry/fl-at-one/) gives the statement for general $r$ and the proof.

## Proof

The proof is the term `GlobalTheory.PMon.FLOne.flAt_one`. Nothing else happens.

## In the Lean code

The theorem is in [FundamentalLemmaLatticeDegreeOneStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FundamentalLemmaLatticeDegreeOneStatement.lean#L7). The proof is the tactic `first | exact @GlobalTheory.PMon.FLOne.flAt_one | ...`, and the first branch closes the goal. The file sets `maxHeartbeats` to 1000000. `FLAt` is defined in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L79). The word "degree one" in the name is the value $r = 1$.
