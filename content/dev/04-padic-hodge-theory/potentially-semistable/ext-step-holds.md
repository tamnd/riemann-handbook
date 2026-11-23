---
id: ext-step-holds
title: A de Rham extension of potentially semistable blocks
kind: theorem
decl: GlobalTheory.PMon.extStep_holds
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.DeRhamExtensionPotentiallySemistable
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem proves `ExtStep`: a block upper triangular representation that is de Rham, with potentially semistable diagonal blocks, is potentially semistable. The extension class is moved from $B_{\mathrm{dR}}$ to $B_{\mathrm{st}}$ by a matrix form of a theorem that the Lean code names after Hyodo. [`deRhamExtension_potentiallySemistable`](/entry/de-rham-extension-potentially-semistable/) renames it, and [`Red.redStep`](/entry/red-step/) uses it.

## Statement

Use the notation of [`matThm_holds`](/entry/mat-thm-holds/). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r$ an integer, and $\rho \colon G_K \to \mathrm{GL}_{a+b}(\mathbb{Q}_\ell^{\mathrm{ur}})$ with

$$\rho(g) = \begin{pmatrix} \rho_1(g) & c(g) \\ 0 & \rho_2(g) \end{pmatrix},$$

where $\rho_1$, $\rho_2$ are homomorphisms. If `IsRat r ρ`, `AdmDR P ρ`, `AdmSt P ρ₁` and `AdmSt P ρ₂` hold, then `AdmSt P ρ` holds.

## Proof

1. **A common field.** `AdmSt` gives finite extensions $K_1$, $K_2$ of $K$ and period matrices $Q_1$, $Q_2$ over $B_{\mathrm{st}}$. Let $K' = K_1 K_2$. Then $Q_1$, $Q_2$ work for the restrictions of $\rho_1$, $\rho_2$ to $G_{K'}$.
2. **The extension class.** Let $\sigma$ be the action of $G_{K'}$ on $a \times b$ matrices by $\sigma(g)X = \rho_1(g) X \rho_2(g)^{-1}$ (`homRep`), and $e(g) = c(g)\rho_2(g)^{-1}$ (`extCoc`). Then $e(gh) = e(g) + \sigma(g)e(h)$, the entries of $e$ are continuous and fixed by $\mathrm{Fr}^r$, and $\sigma$ satisfies `IsRat r` (`matrixHomRepresentationCocycle_rational_continuous`, `matrixHomRepresentation_restrict_rational_continuous`). So $e$ is a $1$-cocycle with values in $\operatorname{Hom}(\rho_2, \rho_1)$ (see [[Galois cohomology|9MPCZ3EAJM]]).
3. **$\sigma$ is semistable.** The matrix $Q_1 \otimes (Q_2^{-1})^{\mathsf{T}}$ (`homUnit`) is a period matrix of $\sigma$ over $B_{\mathrm{st}}$ (`matrixHom_periodMatrix_semistable`).
4. **$e$ dies in $B_{\mathrm{dR}}$.** `deRham_blockTriangular_diagonal_blocks` gives `AdmDR P ρ₂`. From this and `AdmDR P ρ`, `blockTriangular_extensionCocycle_trivial_deRham` gives, for each $m$, a vector $v_m$ over $B_{\mathrm{dR}}$ with $\mathrm{Fr}^m(e(g)) = \mathrm{Fr}^m(\sigma(g))\, g(v_m) - v_m$.
5. **$e$ dies in $B_{\mathrm{st}}$.** [`hyodo_theorem_matrix_unramifiedCoefficients`](/entry/hyodo-theorem-matrix-unramified-coefficients/) gives $v$ over $B_{\mathrm{st}}$ with $e(g) = \sigma(g)\,g(v) - v$ for $g \in G_{K'}$.
6. **Assembly.** `extension_block_periodMatrix_semistable` builds from $Q_1$, $Q_2$ and $v$ a period matrix $Q \in \mathrm{GL}_{a+b}(B_{\mathrm{st}})$ of $\rho$ on $G_{K'}$.

Step 5 has the real content.

## In the Lean code

The theorem is in [DeRhamExtensionPotentiallySemistable.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamExtensionPotentiallySemistable.lean#L19). `homUnit`, `homRep` and `extCoc` are in [KroneckerTransposeMulVec.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/KroneckerTransposeMulVec.lean#L13). Matrices $a \times b$ are vectors indexed by $a \times b$ through `vecM`, and $\sigma(g)$ is the Kronecker product $\rho_1(g) \otimes (\rho_2(g)^{-1})^{\mathsf{T}}$. The lemmas of steps 2 to 6 are called through their `GlobalTheory.T` names. We have not unfolded their proofs; in particular we do not know the form of $Q$ in step 6. Step 4 works over $K$ and restricts to $K'$.
