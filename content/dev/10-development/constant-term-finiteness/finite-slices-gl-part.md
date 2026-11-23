---
id: finite-slices-gl-part
title: Finiteness of the slices on a general linear block of the Levi
kind: theorem
decl: GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.CoreGL.Rg.finite_slices_glPart
module: Development.WeilBound.RepresentationTheoryGL.ConstantTermFiniteness.CuspidalConstantTerms.FiniteSlicesGlPart
covers: 399
status: drafted
drafted_by: writer@claude
---
This theorem gives the slice hypothesis of [the finiteness of relative cusp forms](/entry/finite-cusp-on/) for each general linear block $H_k$ of the Levi $M_T$. It restricts a relative cusp form to a copy of $\mathrm{GL}_d$ and uses the finiteness of cusp forms on $\mathrm{GL}_d$.

## Statement

Use the notation of [the finiteness of relative cusp forms](/entry/finite-cusp-on/). Let $k \in T$ and $b \in G(\mathbb{A})$. The slices on $H_k$ at $b$ are the functions $t \mapsto \varphi(t\, y\, b)$ on $H_k$, for $\varphi \in \mathcal{A}^{\mathrm{cusp}}_T$ and $y \in M_T(\mathbb{A})$ that commutes with $H_k$.

**Theorem.** The slices on $H_k$ at $b$ span a finite dimensional space.

## Proof

1. **The block.** The columns of the flag between the element of $T$ before $k$ and $k$ form a block of size $d$ (`exists_block`). A block embedding $\iota \colon \mathrm{GL}_d(\mathbb{A}_E) \to G(\mathbb{A})$ has image $H_k$ (`exists_blockEmb`, `block_embedding_parabolic_compatibility`).
2. **Moving $b$.** Fix a maximal compact subgroup $K$ of $G(F_\infty)$ adapted to the frames. `parabolic_block_embedding_compact` writes $b = u\, \iota(y_1)\, g_0$ with $u \in N_T(\mathbb{A})$, $y_1 \in \mathrm{GL}_d(E_\infty)$, and $g_0^{-1} \iota(K_d) g_0 \subseteq K$ for the maximal compact $K_d$ of $\mathrm{GL}_d(E_\infty)$.
3. **Data on $\mathrm{GL}_d$.** A finite dimensional space $S$ of functions on $K$ holds the $K$-coefficients of every $\varphi$ (`typesFiniteSpace`). Through $\kappa \mapsto g_0^{-1}\iota(\kappa) g_0$ it gives a representation $\rho'$ of $K_d$. The level is the open group $L$ of $a \in \mathrm{GL}_d(\mathbb{A}_{E,f})$ with $g_0^{-1}\iota(a) g_0 \in U$. `monic_block` gives monic polynomials in the Capelli elements of the center $\mathcal{Z}$ of $\mathrm{GL}_d$ that kill the restricted forms. Their set $J$ has finite codimension in the sense that $\mathcal{Z}$ is a finite dimensional space plus $\mathcal{Z} J$ (`cofinite_of_capelli_monic`).
4. **The restriction.** For $\varphi$ and $y$ as above, $F(x) = \varphi(\iota(x)\, y\, g_0)$ is a cusp form on $\mathrm{GL}_d(\mathbb{A}_E)$ of level $L$, with $K_d$-coefficients in $\rho'$, killed by $J$. The lemmas are `cuspForm_blockEmb_left_invariant`, `isOpen_rightInv_finGL`, `kinf_finite`, `zfin_of_cofin`, `growth_comp_blockEmb` and `isCuspidal_comp_blockEmb`.
5. **Finiteness on $\mathrm{GL}_d$.** `CuspFinGL.Split.cuspFin` says that these cusp forms span a finite dimensional space. This is the $\mathrm{GL}_d$ case of the theorem of Harish-Chandra (Automorphic forms on semisimple Lie groups, LNM 62, 1968, Theorem 1) that [the finiteness of automorphic forms](/entry/harish-chandra-finite/) states for $G$.
6. **Back to the slices.** Since $t y \in M_T(\mathbb{A})$ normalizes $N_T(\mathbb{A})$ and $\varphi$ is left invariant under $N_T(\mathbb{A})$, the slice at $\iota(x)$ is $F(x\, y_1)$. So the slices are the image of a finite dimensional space under a linear map.

## In the Lean code

The theorem is at [FiniteSlicesGlPart.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FiniteSlicesGlPart.lean#L192), with the helpers `exists_block`, `repOf`, `kfin_of_space` and `zfin_of_cofin` in the same file. `cuspFin` is in [InvariantOfLieOneLEqZero.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/InvariantOfLieOneLEqZero.lean#L103), and `genSpace`, `Cofin` and `CuspFin` in [GenSpace.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/AffineGLForms/GenSpace.lean#L11). `monic_block` is in [DerEndMemLeftInv.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/DerEndMemLeftInv.lean#L420). We have not unfolded the proofs of `cuspFin` and `monic_block`.

