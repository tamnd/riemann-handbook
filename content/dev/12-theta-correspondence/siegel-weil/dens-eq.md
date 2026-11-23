---
id: dens-eq
title: The theta mean as a product of local densities, for an anisotropic form
kind: theorem
decl: PositivityTheory.Rg.Base1.densEq
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.BaseOneSide.BaseOneOf
covers: 541
status: drafted
drafted_by: writer@claude
---
This theorem proves `DensEq`: for an anisotropic Hermitian form $J$ of size $M$ over a CM field, the mean of a theta function over the vectors with Gram matrix $T$ is a product of local densities. It is the last input of [`whitGenEq`](/entry/whit-gen-eq/). Its proof is one line, `densEq_of_one baseOne massOne`. It plugs the rank one case [`baseOne`](/entry/base-one/) and the local mass fact `massOne` into an induction on $M$. That induction is in `swMeasCAll_of`; the rank one case is proved in [`baseOne_of`](/entry/base-one-of/).

## Statement

Let $E/F$ be a CM extension with complex conjugation $\sigma$. For a finite place $v$ of $F$, put $e_v=-1$ if $F_v\otimes_F E$ is a field and $e_v=1$ otherwise, and let $Nv$ be the norm of $v$.

**Theorem.** Let $M\ge1$, let $J$ be an $M\times M$ nondegenerate Hermitian matrix over $E$ with $J(x,x)\neq0$ for $x\neq0$, and let $T$ be an $M\times M$ Hermitian matrix with $\det T\neq0$. Let $\Phi=\Phi_\infty\otimes\bigotimes_v\Phi_v$ be a factorizable Schwartz function on $M$-tuples of adelic vectors in $E^M$, with $\Phi_v$ the indicator of the standard lattice at almost all $v$. Fix a Haar measure $\mu$ on the adelic unitary group of $J$, a fundamental domain $\mathcal{F}$ (the mean is $\mu(\mathcal{F})^{-1}\int_{\mathcal{F}}\,d\mu$), a character $\psi$ and the self-dual measures that it gives. Then there are continuous densities $g_\infty$ and $g_v$ of the Gram map $X\mapsto\operatorname{gram}(X)=\bigl(J(X_a,X_b)\bigr)_{a,b}$ on $M$-tuples of vectors against $\Phi_\infty$ and $\Phi_v$ such that the product below converges and

$$2\,\operatorname{mean}_{h\in\mathcal{F}}\Bigl(\sum_{X:\,\operatorname{gram}(X)=T}\Phi(h^{-1}X)\Bigr)=g_\infty(T)\,\lambda\,\prod_v\frac{g_v(T)}{1-e_v/Nv}$$

for every limit $\lambda$ of $\prod_v(1-e_v Nv^{-s})$ as $s\to1^{+}$.

## Proof

The chain under the one line is this.

1. `densEq_of_one` adds `schwartzDensInf`, a fact on densities at the infinite place, and calls `densEq_of_base`.
2. `densEq_of_base` adds `oneVecBinary` and `oneVecBinaryMass` and calls `densEq_of_pieces`.
3. `densEq_of_pieces` proves `SWMeasCAll`, the same identity in the language of Euler products of measures, with `swMeasCAll_of`. This is an induction on $M$ from `BaseOne`, with four steps: `isomC` (change $J$ by an isometry), `scaleC` (scale $T$), `stepC_of` (pass from rank $M$ to rank $M+1$) and `notRepC_of` (the case where $T$ is not represented). The last two use `massCAll_of`, which comes from `massOne`.
4. `densEq_of_C` turns `SWMeasCAll` into `DensEq`.

I have not unfolded `OneVecBinary`, `OneVecBinaryMass`, `SchwartzDensInf`, or the proofs of the four induction steps.

## In the Lean code

The theorem is in [BaseOneOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/BaseOneSide/BaseOneOf.lean#L30). `DensEq` and $e_v$ (`eSp`) are in [WhitGenLowOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenLowOf.lean#L130). The chain is in [PlugInf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/PlugInf.lean#L8), [DensEqOfBase.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/DensEqOfBase.lean#L9), [DensEqOfPieces.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/DensEqOfPieces.lean#L13), [Induct.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/Induct.lean#L44) and [Bridge.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/Bridge.lean#L50). `SWMeasC` and `SWMeasCAll` are in [SWMeasCAll.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/SWMeasCAll.lean#L28).

`massOne` is passed twice: once to `baseOne` and once to `densEq_of_one`.

`eSp` is $-1$ when $F_v\otimes_F E$ is a field, so also at ramified places, where one would expect $0$. The same $e_v$ appears on both sides of the identity, in $\lambda$ and in the local factors.
