---
id: fourier-match-of-weil-field
title: Matching survives the partial Fourier transform, from the quadratic Weil representation
kind: theorem
decl: GlobalTheory.JR.fourierMatch_of_weilField
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisFourierMatchingOfWeilField
covers: 361
status: drafted
drafted_by: writer@claude
---
This theorem proves that matching of test functions in the Jacquet-Rallis setting survives the partial Fourier transform, if the Weil representation exists for quadratic extensions of fields. It puts three lemmas together. [Its statement file](/entry/jacquet-rallis-fourier-matching-of-weil-field/) renames it for [unit matching from the quadratic Weil representation](/entry/unit-match-of-weil-field/), where it is the input $\mathrm{FourierMatch}(r+1)$ of each induction step.

## Statement

**Theorem.** If $\mathrm{WeilField}$ holds, then $\mathrm{FourierMatch}(r)$ holds for every $r \ge 0$.

The notation ($E/F$, $\mathfrak{g}_r \ni (A, b, c, d)$, $\mathfrak{h}_r \ni (X, v, d)$, $\mathrm{sec}$, $\omega$, the measures) is that of [the entry with the induction](/entry/unit-match-of-weil-field/). A *test function* is locally constant with compact support. Test functions $f'$ on $\mathfrak{g}_r$ and $f$ on $\mathfrak{h}_r$ *match* if at each regular invariant $a$ the $\omega$-weighted $\mathrm{GL}_r(F)$-orbital integral of $f'$ at $\mathrm{sec}(a)$ equals the $U_r$-orbital integral of $f$ at each $X$ with invariants $a$, and is $0$ if there is no such $X$.

Let $\psi$ be a character of $F$ with $\psi = 1$ on $\mathcal{O}_F$ and $\psi \ne 1$ on $\varpi^{-1}\mathcal{O}_F$ (`IsStdChar`). The partial Fourier transforms are

$$\begin{gathered}\widehat{f'}(A, b, c, d) = \int_{F^r}\int_{F^r} f'(A, b', c', d)\,\psi(c' b + c b')\,dc'\,db',\\ \widehat{f}(X, v, d) = \int_{E^r} f(X, v', d)\,\psi\bigl(\operatorname{Tr}_{E/F}(v'^* v)\bigr)\,dv',\end{gathered}$$

with the measures that give $\mathcal{O}_F$ and $\mathcal{O}_E$ volume $1$. $\mathrm{FourierMatch}(r)$ says: if $f'$ and $f$ match, then $\widehat{f'}$ and $\widehat{f}$ match.

## Proof

The proof is one line:

```
jacquetRallisFourierMatch_of_weilRepresentation (weilRepresentationEtale_of_quadraticField h)
  etaleOrbitalFourier_rankOne_transfer weilConstantStandardHermitian_eq_one
```

The three inputs, for $K/F$ étale (a finite reduced $F$-algebra) and $L = K \otimes_F E$:

1. `weilRepresentationEtale_of_quadraticField` proves $\mathrm{WeilEt}$ from $\mathrm{WeilField}$: the Weil representation on test functions on $L$ for the form $x N_{L/K}$ exists for every étale $K$, with the sign $\eta(N_{K/F}(s))$ for $m(s)$.
2. `etaleOrbitalFourier_rankOne_transfer` proves $\mathrm{RankOne}$, with no hypothesis. Rank-one orbital integrals are integrals over $K^\times$ (weighted by $\eta \circ N_{K/F}$) and over the norm-one group of $L$. If they match for each class $x$ in $K^\times / N(L^\times)$ up to a constant $\kappa$, then their Fourier transforms match, with the extra factor $\gamma(x)$ of the Weil representation for $x N_{L/K}$.
3. `weilConstantStandardHermitian_eq_one` proves $\mathrm{GammaOne}$, with no hypothesis: $\gamma(x) = 1$ when the Hermitian form $x \operatorname{Tr}_{L/E}(y^* y')$ on $L$ is isometric to the standard form on $E^r$.

We read the proof of the main lemma, `fourierMatch_of_weil`, but not its lemmas. By a density lemma, it is enough to treat $a$ for which the companion matrix of $a$ has a separable characteristic polynomial. Then $a$ defines an étale $K = F[\tau]$ of degree $r$, and $a$ corresponds to a unit $a_0 = x N(y)$ of $K$, with $x$ in a fixed set of representatives. The orbital integrals on $\mathfrak{g}_r$ descend to rank-one integrals over $K$, for $f'$ and for $\widehat{f'}$ with the same $\kappa$. The orbital integrals on $\mathfrak{h}_r$ at Hermitian $X$ with invariants $a$ descend to integrals over the norm-one group of $L$, and such $X$ exist exactly when $(L, x \operatorname{Tr}(y^* y'))$ is isometric to $E^r$. $\mathrm{RankOne}$ moves the matching to the Fourier side, and $\mathrm{GammaOne}$ removes $\gamma(x)$.

## In the Lean code

The theorem is in [JacquetRallisFourierMatchingOfWeilField.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisFourierMatchingOfWeilField.lean#L11). `FourierMatch` is in [FourierMatch.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/FourierMatch.lean#L152), and `WeilEt`, `RankOne`, `GammaOne` are in [IsTestRep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsTestRep.lean#L144). The main lemma is `fourierMatch_of_weil` in [JacquetRallisFourierMatchOfWeilRepresentation.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisFourierMatchOfWeilRepresentation.lean#L105), with the work at one invariant in `fourierMatchAt_of_weil` at line 19.

$\mathrm{WeilField}$ is used only through item 1. The Fourier transforms carry no constant factor, because $\mathrm{GammaOne}$ removes it.
