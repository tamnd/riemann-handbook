---
id: has-gauss-herm
title: The Gauss integral of a hermitian form, by diagonalization
kind: theorem
decl: GlobalTheory.KSp.GaussMain.hasGauss_herm
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasGaussIntegralHermitianQuadraticCharacter
covers: 837
status: drafted
drafted_by: writer@claude
---
This lemma computes how the Gauss integral of the form $x \mapsto \tfrac12\mathrm{pr}(x, xb)$ depends on the hermitian matrix $b$: it is one constant $\gamma_0$ times $s(\det b)^{-1}$. Its second name is [the statement entry](/entry/has-gauss-integral-hermitian-quadratic-character/), and the constant goes into [the Weyl cell relation](/entry/weyl-cell-relation/), where it fixes the scalar in front of the Fourier transform.

## Statement

Use the notation of [the statement entry](/entry/has-gauss-integral-hermitian-quadratic-character/): $E/F$, $Q$ ($m \times m$), $\psi$, $\chi$, $\mu$ on $X = M_{m \times n}(E)$, and $s(z) = \chi(z)\lvert N_{E/F}z\rvert_F^{m/2}$. Let $\eta(t) = 1$ if $t \in N_{E/F}(E^\times)$ and $\eta(t) = -1$ otherwise.

**Lemma.** There is $\gamma_0 \in \mathbb C$ such that for each invertible hermitian $b \in M_n(E)$ the regularized integral (`HasGauss`) of $x \mapsto \psi(\tfrac12\mathrm{pr}(x, xb))$ over $X$ is $\gamma_0\, s(\det b)^{-1}$.

Integrals of this kind are the ones that Weil uses to define his index of a character of second degree (A. Weil, Acta Math. 111, 1964). The lemma does not compute $\gamma_0$.

## Proof

1. **Diagonalize $Q$ and $b$.** `exists_GL_diagonal_congruent_hermitian` writes $Q = u\,\mathrm{diag}(D'_i)\,c(u)^{\mathsf T}$ and $b = a\,\mathrm{diag}(D_j)\,c(a)^{\mathsf T}$ with $u \in \mathrm{GL}_m(E)$, $a \in \mathrm{GL}_n(E)$ and all $D'_i, D_j \in F^\times$.
2. **The form becomes a sum of norms.** By `hermitianMatrixColumnPairing_diagonal_norm`,
$$\tfrac12\mathrm{pr}(x, xb) = \sum_{i,j} t_{ij}\, N_{E/F}\bigl((u^{\mathsf T} x a)_{ij}\bigr), \qquad t_{ij} = \tfrac12 D'_i D_j.$$
3. **The diagonal case.** `gaussIntegral_diagonal_hermitianForm_matrices` gives one $g \in \mathbb C$ such that for all $t \in (F^\times)^{m \times n}$ the regularized integral of $\psi(\sum t_{ij} N(x_{ij}))$ is $g \prod_{i,j} \eta(t_{ij})\lvert t_{ij}\rvert_F^{-1}$.
4. **Change of variables.** The map $x \mapsto u^{\mathsf T} x a$ multiplies $\mu$ by $\bigl(\lvert N\det u\rvert_F^{n}\lvert N\det a\rvert_F^{m}\bigr)^{-1}$ (`map_twoSided_mul_haar_matrix_quadraticExt`), and `hasGaussIntegral_comp_addEquiv_rescale` carries the Gauss value along with this factor.
5. **The constant.** Put $\gamma_0 = g\,\lvert N\det u\rvert_F^{-n}\bigl(\prod_i \eta(s_i)\lvert s_i\rvert_F^{-1}\bigr)^n$ with $s_i = \tfrac12 D'_i$. It does not depend on $b$. Since $\eta$ is a character (`localNormResidueSign_mul`) and $\lvert\cdot\rvert_F$ is multiplicative, the product over $t_{ij} = s_i D_j$ splits into the $s$ part and $\bigl(\prod_j \eta(D_j)\lvert D_j\rvert_F^{-1}\bigr)^m$. The lemma `sc_det_inv` shows that $\lvert N\det a\rvert_F^{-m}$ times this last factor is $s(\det b)^{-1}$. It uses that $\chi = \eta^m$ on $F^\times$.

The rest is bookkeeping.

## In the Lean code

The lemma is at [HasGaussIntegralHermitianQuadraticCharacter.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasGaussIntegralHermitianQuadraticCharacter.lean#L99). `HasGauss` is in [UnipVal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnipVal.lean#L39). The helpers `sgnHom`, `sgn_inv`, `det_herm`, `sc_det_inv`, `glT` and `sandwich` are in the same file.

- The lemmas of steps 1 to 4 are wrappers in `GlobalTheory.T`; we have not opened their proofs. The file has only a few declarations, so most of the 837 are under these lemmas.
- `HasGauss μ f γ` asks that every compact set lie in some compact open subgroup $L$ with $\int_L f\,d\mu = \gamma$. It does not ask that the integral be $\gamma$ for all large $L$. This is weaker than the usual stabilization. The braid relation in the [Weyl cell relation](/entry/weyl-cell-relation/) takes a `HasGauss` value as its hypothesis.
- $\lvert\cdot\rvert_F$ is `distribHaarChar F` in step 4 and `nabs F` in step 5.
