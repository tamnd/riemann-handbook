---
id: red-step
title: The reducible case of the monodromy induction
kind: theorem
decl: GlobalTheory.PMon.Red.redStep
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.PotentiallySemistableReducibleUnramifiedSplit
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem proves `RedStep`, the reducible case in the induction of [`matThm_holds`](/entry/mat-thm-holds/). A de Rham representation that is block upper triangular is potentially semistable if its two diagonal blocks are. [`potentially_semistable_reducible_unramified_split`](/entry/potentially-semistable-reducible-unramified-split/) renames it.

## Statement

Use the notation of [`matThm_holds`](/entry/mat-thm-holds/). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r$ an integer and $\rho \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ a homomorphism. Assume:

1. `IsRat r ρ` and `AdmDR P ρ`;
2. `Splits r ρ`: there are a set $s$ of indices with $\emptyset \ne s \ne \{1, \dots, n\}$ and $p \in \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ with entries fixed by $\mathrm{Fr}^r$, such that $(p^{-1}\rho(g)p)_{ij} = 0$ for all $g$, $i \notin s$, $j \in s$;
3. for each $a < n$ and each $\rho' \colon G_K \to \mathrm{GL}_a(\mathbb{Q}_\ell^{\mathrm{ur}})$ with `IsRat r ρ'` and `AdmDR P ρ'`, also `AdmSt P ρ'` holds.

Then `AdmSt P ρ` holds.

## Proof

1. **Conjugate.** Order the indices as $s$, then its complement. Let $\rho'(g) = X \rho(g) Y$, with $X$ the rows of $p^{-1}$ and $Y$ the columns of $p$ in this order. Then $\rho' = \begin{pmatrix} \rho_1 & c \\ 0 & \rho_2 \end{pmatrix}$ with $\rho_1$ of size $|s|$ and $\rho_2$ of size $n - |s|$ (`blk₁`, `blk₂`, `blk_form`).
2. **Transport.** The entries of $X$ and $Y$ are fixed by $\mathrm{Fr}^r$ (`rat_inv`), so by `IsRat` they lie in $K$, and $G_K$ fixes them. Hence conjugation by $X$ and $Y$ keeps `IsRat` (`isRat_of`), `AdmDR` (`deRham_of_conjugate_unramified_rational`) and `AdmSt` (`semistable_of_conjugate_unramified_rational`). The blocks $\rho_1$, $\rho_2$ satisfy `IsRat r` (`isRat_blk₁`, `isRat_blk₂`).
3. **Blocks.** `deRham_blockTriangular_diagonal_blocks` (the statement `SubQuot`) gives `AdmDR` for $\rho_1$ and $\rho_2$. Both sizes are less than $n$, so hypothesis 3 gives `AdmSt` for both.
4. **Extension.** [`deRhamExtension_potentiallySemistable`](/entry/de-rham-extension-potentially-semistable/) (the statement `ExtStep`) gives `AdmSt P ρ'`. Transport back to $\rho$ with step 2.

The real work is in step 4, see [`extStep_holds`](/entry/ext-step-holds/).

## In the Lean code

The theorem is in [PotentiallySemistableReducibleUnramifiedSplit.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PotentiallySemistableReducibleUnramifiedSplit.lean#L222). All helpers named above are in the same file. The conjugation is the group homomorphism `conjHom X Y`, defined for any rectangular $X$, $Y$ with $XY = 1$ and $YX = 1$; here $X$ and $Y$ are square up to the reordering `Equiv.sumCompl`. `SubQuot` is defined in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L58). We have not unfolded its proof.
