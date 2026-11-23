---
id: finite-dimensional-single
title: Finiteness for one eigencharacter, from cusp forms and constant terms
kind: theorem
decl: GlobalTheory.HCFGL.finiteDimensional_single
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HarishChandraFinitenessTotallyComplexGLProof
covers: 710
status: drafted
drafted_by: writer@claude
---
This theorem is the induction step of Harish-Chandra's finiteness theorem for $\mathrm{GL}_a$. It treats one eigencharacter $\chi$ and assumes the result for all smaller $b < a$. Its user `coreFiniteGL` runs the induction and proves [the core statement](/entry/harish-chandra-finiteness-totally-complex-gl-proof/), from which [the finiteness of automorphic forms](/entry/automorphic-forms-finite-gl/) follows.

## Statement

We use the notation $\mathcal{F}(L, W, X, N)$ of [the core statement](/entry/harish-chandra-finiteness-totally-complex-gl-proof/).

**Theorem.** Let $E$ be totally complex and $a \geq 0$. Suppose that for each $b < a$, each open $L' \subseteq \mathrm{GL}_b(\mathbb{A}_{E,f})$, each finite-dimensional $W'$, each finite set $X'$ and each $N'$, the span of $\mathcal{F}(L', W', X', N')$ has finite dimension. Then for each open $L \subseteq \mathrm{GL}_a(\mathbb{A}_{E,f})$, each finite-dimensional $W$, each $\chi$ and each $N$, the span $P$ of $\mathcal{F}(L, W, \{\chi\}, N)$ has finite dimension.

## Proof

This is the classical argument of Harish-Chandra (*Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, 1968): the constant terms are controlled by induction, and the forms with zero constant terms are cusp forms.

1. **Constant terms.** By `finiteDimensional_forms_span_level` (proved by `HCFGLct.exists_ct_map`), there is a linear map $T \colon \mathrm{Sm} \to \mathbb{C}^n$ such that each $\varphi \in \mathcal{F}$ with $T\varphi = 0$ is cuspidal. Cuspidal (`IsCuspidal`) means: for each $0 < r < a$, the integral of $x \mapsto \varphi(u(x) g)$ over a fundamental domain of $N_r(E) \backslash N_r(\mathbb{A}_E)$ is zero, where $N_r$ is the unipotent radical of the block upper triangular parabolic of type $(r, a - r)$. The map $T$ is built from these constant terms. They span a finite-dimensional space by `HCFct.finiteDimensional_constTerm`, which uses the induction hypothesis. We have not unfolded that lemma.
2. **Smoothing.** `harishChandra_uniform_smoothing_test_function` gives a test function $\alpha$ on $\mathrm{GL}_a(E_\infty)$ with $\varphi * \alpha = \varphi$ for all $\varphi \in \mathcal{F}$.
3. **Cusp forms.** `finiteDimensional_cuspForms_fixedLevel_Ktypes` says that the span $Q$ of the cuspidal elements of $\mathcal{F}$ has finite dimension.
4. **Linear algebra.** By `harishChandraFiniteFormsGL_single_char_span_mem`, $P = \mathcal{F}$ as a set, so $P \cap \ker T \subseteq Q$. Then $T(P)$ and $P \cap \ker T$ have finite dimension, and so does $P$ (`Submodule.fg_of_fg_map_of_fg_inf_ker`).

## In the Lean code

The theorem is in [HarishChandraFinitenessTotallyComplexGLProof.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarishChandraFinitenessTotallyComplexGLProof.lean#L13). The lemmas it calls:

- `GlobalTheory.T.finiteDimensional_forms_span_level`, a second name for `HCFGLct.exists_ct_map`.
- `GlobalTheory.T.harishChandra_uniform_smoothing_test_function`, a second name for `HCAlphaEll.exists_alpha_smoothing`.
- `GlobalTheory.T.finiteDimensional_cuspForms_fixedLevel_Ktypes`, a second name for `HCFCusp.finiteDimensional_cuspSpan`.
- `GlobalTheory.T.harishChandraFiniteFormsGL_single_char_span_mem`, a second name for `HCF.formsGL_single_span`.

Step 2 is not used. `finiteDimensional_cuspSpan` takes $\alpha$ and the equation $\varphi * \alpha = \varphi$ as hypotheses but binds them as `_` ([FiniteDimensionalCuspFormsFixedLevelKtypes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteDimensionalCuspFormsFixedLevelKtypes.lean#L14)). It gets the finiteness of cusp forms from `finiteDimensional_cuspidalForms_GL_totallyComplex` directly. So the smoothing lemma is in the dependency tree of this theorem but does no work here.

In Lean the smoothing is `smoothing ν α φ`, an integral of $\alpha(y)\,\varphi(g y)$ over matrices $y$ with entries in $E_\infty$, against a Haar measure $\nu$ on the matrix space, with $\alpha$ supported in the invertible matrices.
