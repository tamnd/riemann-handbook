---
id: top-slope-slope-bound
title: The Lie slope bound from short vectors and the line bound
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Sl.TopSlope.slopeBound
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.SlopeBoundOfLargeDegreeLine
covers: 850
status: drafted
drafted_by: writer@claude
---
This theorem proves the Lie slope bound `SlopeBoundSt` from the absolute Siegel lemma and the key degree bound. It reaches [`slopeBound_and_lemmaS_of_siegel`](/entry/slope-bound-and-lemma-s-of-siegel/) through the renaming [`T.slope_bound_of_large_degree_line`](/entry/slope-bound-of-large-degree-line/). The [written proof](/proof/weil-bound/) calls this the place where the branch is closest to the Bost slope method, and notes that it uses no slope inequality.

## Statement

The hypotheses are `LineOfLargeDegree.Statement` and `KeyDegSt`, as stated in [the renaming](/entry/slope-bound-of-large-degree-line/). The conclusion is `SlopeBoundSt ∧ Prov.LemmaS`. Here `SlopeBoundSt` says: there is $C' \ge 0$ such that for each principally polarized semi-abelian scheme over $\mathcal{O}_L$ with Lie bundle $\overline{B}$ (the fibre of the Hodge inner product),
$$\mu_{\max}(\overline{B}) \le C' \ell, \qquad \ell = \log\bigl(2 + \operatorname{rk} B + \max(-\widehat{\deg}_n \overline{B}, 0)\bigr).$$
`Prov.LemmaS` is the same statement.

## Proof

Write $|x|_\sigma$ for the hermitian length at $\sigma \colon L \to \mathbb{C}$ and $\operatorname{mean}_\sigma$ for the sum over $\sigma$ divided by $[L:\mathbb{Q}]$.

1. **The line bound.** [`T.line_of_key_degree`](/entry/line-of-key-degree/) turns `KeyDegSt` into `LineSt`: a constant $C \ge 0$ with $-\operatorname{mean}_\sigma \log |x|_\sigma \le C \ell$ for each $x \ne 0$ in the Lie bundle. We take $C' = C + 2$.
2. **A short vector.** Let $F \ne 0$ be a submodule of $B$. `short_vector_of_submodule` uses the Siegel lemma to give a finite extension $L'/L$ and $x$ in $B \otimes \mathcal{O}_{L'}$ with
$$\mu(F) - \tfrac12 \log \operatorname{rk} B - 1 \le -\operatorname{mean}_{\sigma'} \log |x|_{\sigma'}.$$
3. **Base change.** `T.polarized_data_field_extension` gives a datum $D'$ over $L'$ that extends $D$, with the same rank and the same $h$, and an injective isometric map $\iota \colon B \to B'$. `exists_isometric_ext`, proved in the same file, extends $\iota$ to an isometric additive map $\Phi$ from $B \otimes \mathcal{O}_{L'}$ to $B'$.
4. **The bound.** If $\Phi x \ne 0$, `LineSt` for $D'$ bounds $-\operatorname{mean} \log |\Phi x|$ by $C\ell$, since $D'$ has the same $\ell$. If $\Phi x = 0$, every length is $0$, and the Lean convention $\log 0 = 0$ makes the left side $0 \le C\ell$.
5. **Assembly.** Since $\ell \ge \log 2 > \frac23$, we have $1 \le \frac32 \ell$, and $\log \operatorname{rk} B \le \ell$. So $\mu(F) \le C\ell + \frac12 \ell + \frac32\ell = (C+2)\ell$. Taking the supremum over $F$ gives the bound for $\mu_{\max}$.

## In the Lean code

The theorem is in [SlopeBoundOfLargeDegreeLine.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/SlopeBoundOfLargeDegreeLine.lean#L94), with `exists_isometric_ext` at [line 25](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/SlopeBoundOfLargeDegreeLine.lean#L25). The lemmas it calls:

- `GlobalTheory.T.line_of_key_degree`;
- `GlobalTheory.CompanionTheory.Ar.Lines.short_vector_of_submodule`, in [ShortVectorOfSubmodule.lean](lean:Development/AutomorphicSpectrum/Proofs/AdelicProofs/ShortVectorOfSubmodule.lean#L249);
- `GlobalTheory.T.polarized_data_field_extension`.

The proof ends with `⟨hS, hS⟩`: it gives the same term for both conjuncts. Step 2 discards the fact $x \ne 0$ that `short_vector_of_submodule` provides, and step 4 covers the case $\Phi x = 0$ with the junk value $\log 0 = 0$. The term $\frac12 \log$ in `short_vector_of_submodule` uses the rank of $B$, not the rank of $F$.
