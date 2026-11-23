---
id: hyodo-theorem-matrix-unramified-coefficients
title: De Rham trivial cocycles of a semistable matrix representation are semistable trivial (named form)
kind: theorem
decl: GlobalTheory.T.hyodo_theorem_matrix_unramifiedCoefficients
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.HyodoTheoremMatrixUnramifiedCoefficientsStatement
covers: 330
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`hyodo_mat`](/entry/hyodo-mat/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its parent in the spine is [`extStep_holds`](/entry/ext-step-holds/), where it moves an extension class from $B_{\mathrm{dR}}$ to $B_{\mathrm{st}}$.

## Statement

Use the notation of [`matThm_holds`](/entry/mat-thm-holds/). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r$ an integer and $\sigma \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ with `IsRat r σ`. Assume that $\sigma$ is semistable over $K$ itself: some $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ has $\sigma(g)\,g(Q) = Q$ for all $g \in G_K$. Let $c \colon G_K \to (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ be a map with entries fixed by $\mathrm{Fr}^r$ and continuous, and with

$$c(gh) = c(g) + \sigma(g)\,c(h).$$

Assume that for each $m \ge 0$ some $b_m \in B_{\mathrm{dR}}^n$ has $\mathrm{Fr}^m(c(g)) = \mathrm{Fr}^m(\sigma(g))\,g(b_m) - b_m$ for all $g$. Then some $b \in B_{\mathrm{st}}^n$ has $c(g) = \sigma(g)\,g(b) - b$ for all $g$.

In words: a $1$-cocycle of a semistable representation that becomes a coboundary over $B_{\mathrm{dR}}$ becomes a coboundary over $B_{\mathrm{st}}$. The Lean name attributes this to Hyodo; we give no source. The form for representations on $\mathbb{Q}_\ell$-vector spaces is [`hyodo_statement`](/entry/hyodo-statement/).

## Proof

The proof is the term `GlobalTheory.PMon.hyodo_mat`. Nothing else happens.

## In the Lean code

The theorem is in [HyodoTheoremMatrixUnramifiedCoefficientsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HyodoTheoremMatrixUnramifiedCoefficientsStatement.lean#L7). The proof is the tactic `first | exact @GlobalTheory.PMon.hyodo_mat | ...`, and the first branch closes the goal. The file sets `maxHeartbeats` to 1000000. The statement is written out in full, not through a named proposition. The proof of [`hyodo_mat`](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HyodoTheoremMatrixUnramifiedCoefficients.lean#L24) passes to a representation over $\mathbb{Q}_\ell$ of size $n r$ by restriction of scalars and then calls `hyodo_statement`; we have not unfolded its steps.
