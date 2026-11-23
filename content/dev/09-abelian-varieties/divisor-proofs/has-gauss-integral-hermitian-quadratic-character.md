---
id: has-gauss-integral-hermitian-quadratic-character
title: The Gauss integral of a hermitian form (statement)
kind: theorem
decl: GlobalTheory.T.hasGaussIntegral_hermitian_quadratic_character
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasGaussIntegralHermitianQuadraticCharacterStatement
covers: 838
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the Gauss integral of a hermitian form](/entry/has-gauss-herm/). Its proof applies that lemma and does nothing else. Its one user is [the Weyl cell relation](/entry/weyl-cell-relation/), where the constant $\gamma_0$ of the statement fixes the scalar $\kappa = s((-1)^n)/\gamma_0$ in front of the Fourier transform.

## Statement

The setting is that of [the Weyl cell relation](/entry/weyl-cell-relation/): the quadratic extension $E/F$ of non-archimedean local fields, the invertible hermitian $m \times m$ matrix $Q$, the characters $\psi$ and $\chi$, the pairing $\mathrm{pr}$ on $X = M_{m \times n}(E)$, an additive Haar measure $\mu$ on $X$, and $s(z) = \chi(z)\lvert N_{E/F}z\rvert_F^{m/2}$. The theorem says: there is $\gamma_0 \in \mathbb C$ such that for each invertible hermitian $b \in M_n(E)$,

$$\int_X \psi\bigl(\tfrac12\mathrm{pr}(x, xb)\bigr)\,d\mu(x) = \gamma_0\, s(\det b)^{-1}$$

in the regularized sense of `HasGauss`: every compact set lies in a compact open subgroup $L$ with $\int_L \psi(\tfrac12\mathrm{pr}(x, xb))\,d\mu(x) = \gamma_0\, s(\det b)^{-1}$.

## Proof

The proof applies `GlobalTheory.KSp.GaussMain.hasGauss_herm` to the same arguments. There is nothing else.

## In the Lean code

The theorem is at [HasGaussIntegralHermitianQuadraticCharacterStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasGaussIntegralHermitianQuadraticCharacterStatement.lean#L9). Its statement is the statement of `KSp.GaussMain.hasGauss_herm`, and the proof is a `first` tactic that tries three ways to apply it. All 837 other declarations below it are below `hasGauss_herm`.
