---
id: kirillov-semilocal
title: The semi-local Kirillov bump for a cuspidal vector, from the abstract form
kind: theorem
decl: GlobalTheory.JSW.MirSemi.kirillov_semilocal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KirillovSemilocalMirabolicWhittaker
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem proves [the mirabolic form of the semi-local Kirillov bump](/entry/kirillov-semilocal-mirabolic-whittaker/). It puts the Whittaker functions of a semi-local span of $\varphi$ into a space $\mathcal{W}$, applies [the abstract form](/entry/kirillov-semi-local-mirabolic-abstract/) to $\mathcal{W}$, and lifts the result back to an automorphic function. The analysis is in the abstract form and in the lemma that builds $\mathcal{W}$.

## Statement

The statement of [the mirabolic form](/entry/kirillov-semilocal-mirabolic-whittaker/): for $b$ with conditions 1 to 4 of [the bump theorem](/entry/kirillov-semilocal-bump/), and $\varphi$ in a [[cuspidal representation|9AZ164C298]] $\pi$ of $\mathrm{GL}_{m+1}$ with $W_\varphi(p) \ne 0$ for some $p \in P_S$, there is $F \in \mathcal{M}(\pi)$ with $W_F = b$ on $P_S$ and clauses 2 to 4.

## Proof

Let $\mathcal{L}_S(\varphi)$ be the smallest space of functions that contains $\varphi$ and is stable under right translation by $G_S$ and under the archimedean kernel operators $F \mapsto \int_X k(x)\,F(g\,\gamma(x))\,d\nu(x)$, for $k$ and $\gamma \colon X \to \mathrm{GL}_{m+1}(E_\infty)$ with rapid decay (`MirSemi.locSpan`, `kerInf`, `IsRapidInf`).

1. `exists_cusp_form_semi_local_whittaker_space` gives a space $\mathcal{W}$ of functions on $\mathrm{GL}_{m+1}(\mathbb{A})$ with $W_\varphi \in \mathcal{W}$ and five properties: each $W \in \mathcal{W}$ transforms by $\psi_N$ on the left; $\mathcal{W}$ is stable under right translation by $G_S$ and under the kernel operators; each $y \mapsto W(gy_\infty)$ is continuous with polynomial growth in a height; each $W$ is right invariant under an open subgroup of $\mathrm{GL}_{m+1}(\mathbb{A}_f)$. Also each $W \in \mathcal{W}$ is $W_F$ for some $F \in \mathcal{L}_S(\varphi)$.
2. [The abstract form](/entry/kirillov-semi-local-mirabolic-abstract/), with these five properties and $W_\varphi(p) \ne 0$, gives $W \in \mathcal{W}$ with $W = b$ on $P_S$.
3. Step 1 gives $F \in \mathcal{L}_S(\varphi)$ with $W_F = W$. Then $F \in \mathcal{M}(\pi)$ (`locSpan_le_mspanR`), and clause 1 holds.
4. Clauses 2 to 4 hold for every $F \in \mathcal{L}_S(\varphi)$. They come from `archimedeanKernelSpan_cuspForm_right_invariant_open`, `semiLocalSpan_rightInvariant_of_trivial_infinity_finset` and `whittaker_relation_passes_to_semi_local_span`.

## In the Lean code

The theorem is at [line 16 of KirillovSemilocalMirabolicWhittaker.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemilocalMirabolicWhittaker.lean#L16). The proof is six lines and uses every hypothesis. The four `T.` lemmas of steps 1 and 4 are second names of `MirSemi.whitSpace_exists`, `locSpan_openInv`, `locSpan_rightInv` and `whit_rel_locSpan`, whose proofs we have not opened. The height in step 1 is `height`, which we have not unfolded. `locSpan_le_mspanR` is in [KerInfMemLocSpan.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KerInfMemLocSpan.lean#L43).

The name of this theorem differs from `MirSemi.kirillov_semiLocal`, the abstract form in the same namespace, only in the case of one letter.
