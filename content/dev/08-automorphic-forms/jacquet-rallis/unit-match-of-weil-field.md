---
id: unit-match-of-weil-field
title: Unit matching in every rank from the quadratic Weil representation
kind: theorem
decl: GlobalTheory.JR.unitMatch_of_weilField
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisUnitMatchOfWeilRepQuadratic
covers: 1042
status: drafted
drafted_by: writer@claude
---
This theorem proves the Jacquet-Rallis fundamental lemma for unit functions, in its Lie algebra form, in every rank, from the Weil representation for a quadratic extension of fields. It does the induction on the rank. The [statement file](/entry/jacquet-rallis-unit-match-of-weil-rep-quadratic/) passes it to [unit matching in all ranks](/entry/unit-match-all/), which removes the hypothesis. Below it are 1,042 declarations of the proof.

## Statement

Let $F$ be a nonarchimedean local field of characteristic $0$, $E/F$ an unramified quadratic extension (the class `Unram`), and $\eta(x) = 1$ if $|x| = |y|^2$ for some $y \in F$, else $-1$. Let $\mathfrak{g}_r$ be the matrices $Y = \begin{pmatrix} A & b \\ c & d \end{pmatrix}$ in $\mathfrak{gl}_{r+1}(F)$, with $\mathrm{GL}_r(F)$ acting by conjugation. Let $\mathfrak{h}_r$ be the Hermitian $(r+1) \times (r+1)$ matrices $(X, v, d)$ over $E$, with $U_r$ (standard form) acting by conjugation. The invariants are the coefficients of the characteristic polynomial of $A$, the numbers $cA^ib$ for $i < r$, and $d$. For an invariant $a$, $\mathrm{sec}(a)$ has $A$ a companion matrix and $b = e_1$; $a$ is regular if the Hankel determinant $\det(cA^{i+j}b)$ of $\mathrm{sec}(a)$ is not $0$. The Haar measures give volume $1$ to $\mathrm{GL}_r(\mathcal{O}_F)$ and to $U_r \cap M_r(\mathcal{O}_E)$. Let $\omega(Y) = \eta(\det(e, eY, \dots, eY^r))$ with $e$ the last row vector.

$\mathrm{UnitMatch}(r)$ says: for each regular $a$ and each $X \in \mathfrak{h}_r$ with invariants $a$,

$$\int_{\mathrm{GL}_r(F)} \mathbf{1}_{\mathfrak{g}_r(\mathcal{O})}(g \cdot \mathrm{sec}(a))\, \omega(g \cdot \mathrm{sec}(a))\, dg = \int_{U_r} \mathbf{1}_{\mathfrak{h}_r(\mathcal{O})}(u \cdot X)\, du,$$

and the left side is $0$ if no such $X$ exists. Our own computation gives $\omega(g \cdot Y) = \eta(\det g)\,\omega(Y)$, so this is the standard form with transfer factor $\omega$. The fundamental lemma was conjectured by Jacquet and Rallis (Clay Math. Proc. 13, 2011) and proved by Yun (Duke Math. J. 156, 2011) for large residue characteristic, and by Beuzart-Plessis (Duke Math. J. 170, 2021) in general.

$\mathrm{WeilField}$ says, for $K/F$ finite with $L = K \otimes_F E$ a field:

- given $\psi$ of conductor $\mathcal{O}_F$, $x \in K^\times$, a self-dual measure on $L$, and $\omega$ the sign of the norm group $N(L^\times)$ in $K^\times$,
- there are $\gamma \in \mathbb{C}$ and a representation of $\mathrm{SL}_2(K)$ on test functions on $L$,
- in which $n(z)$ multiplies by $\psi_K(zxN(y))$, $m(s)$ sends $\varphi$ to $\omega(s)|s|\varphi(sy)$, and $w$ is $\gamma$ times the Fourier transform.

This is the [Weil representation](/learn/theta/#the-weil-representation) for the form $xN_{L/K}$.

**Theorem.** If $\mathrm{WeilField}$ holds, then $\mathrm{UnitMatch}(r)$ holds for all $r$.

## Proof

Induction on $r$. For $r = 0$, `jacquetRallisUnitMatch_sizeOne` computes: both groups are trivial and both sides are $\mathbf{1}(|d| \leq 1)$. The step `jacquetRallisUnitMatch_succ` takes $\mathrm{UnitMatch}(r)$ and three inputs:

1. `WeilEt`, the Weil representation for every étale $K$, from `weilRepresentationEtale_of_quadraticField`;
2. `GammaOne`, from `weilConstantStandardHermitian_eq_one`: $\gamma = 1$ for the standard Hermitian space;
3. `FourierMatch (r+1)`, from `jacquetRallis_fourier_matching_of_weil_field`: matching survives the partial Fourier transforms.

We read the proof of the step, not its lemmas. $\mathrm{SL}_2(F)$ acts on test functions on both sides, with $w$ as the partial Fourier transform, and the $g$ with $gf' - f'$ matching $gf - f$ (for the unit functions) form a monoid. It contains $w$, which fixes the unit functions, and $n(t)$ for $t \in \varpi^{-1}\mathcal{O}_F$, by $\mathrm{UnitMatch}(r)$, so it is all of $\mathrm{SL}_2(F)$. A suitable $n(t)$ then gives matching where $cb \neq 0$, and a density lemma gives the rest.

## In the Lean code

The theorem is at [JacquetRallisUnitMatchOfWeilRepQuadratic.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchOfWeilRepQuadratic.lean#L13). `UnitMatch` is in [FourierMatch.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/FourierMatch.lean#L158), `WeilField` in [IsTestRep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsTestRep.lean#L137), and the step `UnitStep.unitMatch_succ` in [JacquetRallisUnitMatchSucc.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchSucc.lean#L124).

Differences from the standard form. The index $r$ is the size of $A$, so "size one" is $r = 0$. The orbital integral is taken only at $\mathrm{sec}(a)$. The integrals are Bochner integrals, which are $0$ when the integrand is not integrable. There is no condition on the residue characteristic.
