---
id: hyodo-mat
title: De Rham cocycles are semistable, for matrices with unramified entries
kind: theorem
decl: GlobalTheory.PMon.hyodo_mat
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.HyodoTheoremMatrixUnramifiedCoefficients
covers: 329
status: drafted
drafted_by: writer@claude
---
This theorem says that a de Rham cocycle of a semistable matrix representation with entries in $\mathbb{Q}_\ell^{\mathrm{ur}}$ is a coboundary over $B_{\mathrm{st}}$. It is the matrix form of [the statement `Hyodo`](/entry/hyodo-statement/) for representations over $\mathbb{Q}_\ell$, and it gets that form by restriction of scalars. [Its statement file](/entry/hyodo-theorem-matrix-unramified-coefficients/) renames it. The extension step [`extStep_holds`](/entry/ext-step-holds/) of the $p$-adic monodromy theorem uses it for the cocycle of an extension of two semistable blocks.

## Statement

Let $\ell$, $P$, $A$ be as in [the matrix form of the monodromy theorem](/entry/mat-thm-holds/): period data with a tie `LocTied l P A` to [[Fontaine's period rings|K6HW8YWCQJ]]. Write $\mathrm{Fr}$ for the Frobenius of $\mathbb{Q}_\ell^{\mathrm{ur}}$. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r \ge 1$, and $\sigma \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ a homomorphism with `IsRat r σ` (continuous entries fixed by $\mathrm{Fr}^r$, and the $\mathrm{Fr}^r$-fixed elements lie in $K$). Assume:

1. some $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ has $\sigma(g)\,g(Q) = Q$ for all $g \in G_K$;
2. $c \colon G_K \to (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ is continuous, has entries fixed by $\mathrm{Fr}^r$, and satisfies $c(gh) = c(g) + \sigma(g)\,c(h)$;
3. for each $m \ge 0$ some $b_m \in B_{\mathrm{dR}}^n$ has $\mathrm{Fr}^m(c(g)) = \mathrm{Fr}^m(\sigma(g))\,g(b_m) - b_m$ for all $g$.

Then some $b \in B_{\mathrm{st}}^n$ has $c(g) = \sigma(g)\,g(b) - b$ for all $g \in G_K$.

Condition 1 is semistability over $K$ itself, with no extension of $K$.

## Proof

The idea: $\sigma$ is defined over the $\mathrm{Fr}^r$-fixed field, so restriction of scalars gives a representation $\rho_0$ of dimension $nr$ over $\mathbb{Q}_\ell$. Apply `Hyodo` to $\rho_0$ and take one block.

1. `exists_continuous_coords_unramified_frobenius` gives $\omega \in (\mathbb{Q}_\ell^{\mathrm{ur}})^r$ with $W = (\mathrm{Fr}^m(\omega_k))_{m,k}$ invertible. Each continuous $\mathrm{Fr}^r$-fixed function $x$ then has continuous coordinates $a_k$ in $\mathbb{Q}_\ell$ with $\mathrm{Fr}^m(x) = \sum_k W_{mk} a_k$.
2. `exists_rational_form_unramified_restrictionScalars` gives a continuous $\rho_0 \colon G_K \to \mathrm{GL}_{nr}(\mathbb{Q}_\ell)$ and $p \in \mathrm{GL}_{nr}(\mathbb{Q}_\ell^{\mathrm{ur}})$ with entries in $K$ and $p\,\rho_0(g) = \operatorname{diag}(\sigma(g), \mathrm{Fr}(\sigma(g)), \dots, \mathrm{Fr}^{r-1}(\sigma(g)))\,p$. It also gives continuous $c_0$ with $p\,c_0(g) = (\mathrm{Fr}^m c(g))_m$. By `cocycle_restrictionScalars_rational_coords`, $c_0$ is a cocycle for $\rho_0$.
3. `periodMatrix_restrictionScalars_blockDiagonal` makes a period matrix $Q_0 \in \mathrm{GL}_{nr}(B_{\mathrm{st}})$ for $\rho_0$ from $Q$. By `isSemistable_of_invertible_periodMatrix_semistableRing`, $\rho_0$ is semistable.
4. `deRham_trivial_rational_cocycle_restrictionScalars` uses condition 3 for all $m$ (one for each block) to split $c_0$ over $B_{\mathrm{dR}}$. `coboundary_tmul_of_column_deRham` puts this in the tensor form of `Hyodo`.
5. [`hyodo_statement`](/entry/hyodo-statement/) splits $c_0$ over $B_{\mathrm{st}}$. `coboundary_semistableTensor_columns` returns to columns, and `coboundary_restrictionScalars_block_zero` takes the block $m = 0$, which gives $b$.

The continuity of the orbit maps of $\rho_0$ is checked inline. The rest is bookkeeping.

## In the Lean code

The theorem is in [HyodoTheoremMatrixUnramifiedCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HyodoTheoremMatrixUnramifiedCoefficients.lean#L24). Each lemma above is called through its second name in `GlobalTheory.T`. We read their statements, not their proofs.

The hypothesis $T$ (the tie) is used only by the semistability lemma and by `hyodo_statement`. The positivity $r > 0$ comes from `IsRat`. Condition 3 asks for all Frobenius twists, but the conclusion is only for $c$ itself. The twists are needed because $\rho_0$ contains all of them as blocks. `IsRat`, `matD` and the maps `ks`, `kd` into $B_{\mathrm{st}}$ and $B_{\mathrm{dR}}$ are in [AdmSt.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmSt.lean#L33).
