---
id: branch-proper-at-point
title: A branch of an affine variety is proper near a point
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Branch.branchProperAtPoint
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.BranchProperAtPointHolds
covers: 805
status: drafted
drafted_by: writer@claude
---
This theorem is a lemma of local complex analytic geometry. It says that a holomorphic branch of an affine variety does not come back near one of its points from the rim of its domain. It goes into `lelongLimitAtBranches`, one of the inputs of the Poincaré-Lelong theorems that the [literature step](/step/every-character-of-literature/) uses through `poincare_lelong_inv_of_literature`. Most of the proof assembles about 160 lemmas on analytic sets. The last step is a short compactness argument.

## Statement

Let $J \subset \mathbb{C}[x_1, \dots, x_n]$ be a prime ideal with $\dim \mathbb{C}[x]/J = k$, and let $Z(J) \subseteq \mathbb{C}^n$ be its zero set. A *branch* of $J$ at $p$ (`VarBranch J k p`) is a number $r > 0$ and a map $\gamma \colon \mathbb{C}^k \to \mathbb{C}^n$ that is holomorphic and injective on the ball $B(0, r)$, with $\gamma(0) = p$ and $\gamma(B(0,r)) \subseteq Z(J)$.

**Theorem.** Let $u \in \mathbb{C}^n$ with $\ell_u = \sum_j u_j x_j \notin J$. Let $\gamma_1, \dots, \gamma_m$ be branches of $J$ at $p$, and let $x \in \mathbb{C}^n$. Suppose that

1. near $x$, $Z(J)$ lies in the union of the images $\gamma_b(B(0, r_b))$;
2. for $b \neq b'$, the images of $\gamma_b$ and $\gamma_{b'}$ meet only where $\ell_u = 0$.

Let $s \in B(0, r_b)$ with $\gamma_b(s) = x$, and let $P$ be a neighbourhood of $s$. Then there is $\varepsilon > 0$ such that each $\tau \in B(0, r_b)$ with $|\gamma_b(\tau) - x| < \varepsilon$ is in $P$.

So $\gamma_b^{-1}$ of a small ball around $x$ lies in any given neighbourhood of $s$.

## Proof

1. **Away from the rim.** `BranchAwayFromRim` says: under the same hypotheses, there are $\varepsilon_0 > 0$ and $\rho < r_b$ such that $|\gamma_b(\tau) - x| < \varepsilon_0$ implies $|\tau| \leq \rho$. Its proof uses the normal model of $Z(J)$ (existence and properness), the lift of branches to it, its local irreducibility, and the fact that a branch contains a normal point. We have not unfolded it.
2. **Compactness.** Take an open $P' \subseteq P$ with $s \in P'$, and put $K = \bar B(0, \rho) \setminus P'$. $K$ is compact, so $\gamma_b(K)$ is compact. Since $\gamma_b$ is injective, $x \notin \gamma_b(K)$, so some ball $B(x, \delta)$ misses $\gamma_b(K)$. Put $\varepsilon = \min(\varepsilon_0, \delta)$. If $|\gamma_b(\tau) - x| < \varepsilon$, then $|\tau| \leq \rho$ by step 1, and $\tau \notin K$, so $\tau \in P' \subseteq P$.

## In the Lean code

The theorem is at [BranchProperAtPointHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BranchProperAtPointHolds.lean#L166). It is 161 `have` lines that apply the proofs of named statements to each other. The last two are `BranchAwayFromRim.proof`, in [PBranchAwayFromRim.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PBranchAwayFromRim.lean#L10), and `BranchProperAtPoint.proof`, in [PBranchProperAtPoint.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PBranchProperAtPoint.lean#L10). The statement is in [StBranchProperAtPoint.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StBranchProperAtPoint.lean#L11), and `VarBranch` is in [StatementsCurrent.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StatementsCurrent.lean#L61).

The theorem has two users. `GlobalTheory.T.branch_proper_at_point_holds` is a second name for it. `Ar.Lelong.lelongLimitAtBranches`, in [LelongLimitAtBranches.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LelongLimitAtBranches.lean#L14), passes it on to `poincareLelong` and `poincareLelongInv` in [PoincareLelongInv.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/PoincareLelongInv.lean#L13).
