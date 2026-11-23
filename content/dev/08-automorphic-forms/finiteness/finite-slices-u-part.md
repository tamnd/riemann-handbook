---
id: finite-slices-u-part
title: Finiteness of the slices on the unitary part of the Levi
kind: theorem
decl: GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.UCore.Rg.finite_slices_uPart
module: Development.WeilBound.RepresentationTheoryGL.ConstantTermFiniteness.CuspidalConstantTerms.FiniteSlicesUPart
covers: 337
status: drafted
drafted_by: writer@claude
---
This theorem gives the slice hypothesis of [the finiteness of relative cusp forms](/entry/finite-cusp-on/) for the unitary part $H_0$ of the Levi $M_T$. It restricts a relative cusp form to a smaller unitary group $\mathrm{U}(V')$ and uses finiteness of cusp forms there.

## Statement

Use the notation of [the finiteness of relative cusp forms](/entry/finite-cusp-on/). Let $b \in G(\mathbb{A})$. The slices on $H_0$ at $b$ are the functions $t \mapsto \varphi(t\, y\, b)$ on $H_0$, for $\varphi \in \mathcal{A}^{\mathrm{cusp}}_T$ and $y \in M_T(\mathbb{A})$ that commutes with $H_0$.

**Theorem.** The slices on $H_0$ at $b$ span a finite dimensional space.

## Proof

1. **Reduction to $b = 1$.** `langlands_decomposition_unipotent_levi` writes $b = n\, m\, b_0$ with $n \in N_T(\mathbb{A})$, $m \in M_T(\mathbb{A})$, and $b_0$ such that the frames translated by $b_0$ are adapted to $T$ (`IsAdapted`). `levi_decomposition_hermitian_centralizer` writes $m = m_H m_o$ with $m_H \in H_0$ and $m_o \in M_T(\mathbb{A})$ commuting with $H_0$. For $\varphi \in \mathcal{A}^{\mathrm{cusp}}_T$, the translate $x \mapsto \varphi(x b_0)$ lies in $\mathcal{A}^{\mathrm{cusp}}_T$ for the level $b_0 U b_0^{-1}$ and the translated frames (`frame_family_right_translate`, `constant_term_frame_K_type_coefficients`). Left invariance under $N_T(\mathbb{A})$ removes $n$. So each slice at $b$ is the right translate by $m_H$ of a slice at $1$ for the new data.
2. **The case $b = 1$** (`finite_slices_core`). Let $V'$ be the orthogonal complement of the span of the columns of $X$ and $Y$ up to $\max T$ (`exists_orthogonal_hermitian_subspace`). An embedding $s \colon \mathrm{U}(V')(\mathbb{A}) \to G(\mathbb{A})$ maps onto $H_0$ (`orthogonal_subspace_unitary_embedding`), and the adapted frames give frames and $K_\infty$-types for $V'$ (`frame_adapted_subspace_unitary_group`).
3. **The restriction.** For $\varphi$ and $y$ as above, $h \mapsto \varphi(s(h)\, y)$ is a smooth automorphic function on $\mathrm{U}(V')$ of moderate growth, of level $s^{-1}(U)$ and of the pulled back type. It is cuspidal (`isCuspFun_slice`). By `constant_term_parabolic_eigenfunction` there are finite lists $A_\tau$ such that $\prod_{a \in A_\tau} (\Delta_{\tau,1} - a)$ kills it, where $\Delta_{\tau,1}$ is the first Gelfand operator at $\tau$.
4. **Finiteness on $\mathrm{U}(V')$.** `constant_term_parabolic_finite_type` says that such cusp forms on $\mathrm{U}(V')$ span a finite dimensional space. Since $s$ is onto $H_0$, pullback along $s$ is injective, and the slices at $1$ span a finite dimensional space.

## In the Lean code

The theorem is at [FiniteSlicesUPart.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FiniteSlicesUPart.lean#L23), and `finite_slices_core` at [CoeffSpanCompMem.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/CoeffSpanCompMem.lean#L34). We have not unfolded the proofs of the `GlobalTheory.T` lemmas.

Several of these lemmas have names that do not match their statements or their files:

- `constant_term_parabolic_finite_type` is stated in [CasimirAnnihilatedCuspFormsFiniteDimensionalStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/CasimirAnnihilatedCuspFormsFiniteDimensionalStatement.lean#L13). It states the finiteness of cusp forms killed by a polynomial in $\Delta_{\tau,1}$, as the file name says, and nothing about constant terms.
- `langlands_decomposition_unipotent_levi` is in `LeviDecompositionHermitianCentralizerStatement.lean`, `levi_decomposition_hermitian_centralizer` in `HermitianPartLeLeviStatement.lean`, and `frame_family_right_translate` in `LanglandsDecompositionUnipotentLeviStatement.lean`. The statement files of this folder are shifted by one name.
