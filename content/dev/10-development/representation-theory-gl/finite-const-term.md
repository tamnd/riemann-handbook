---
id: finite-const-term
title: Finiteness of the constant terms of automorphic forms on a unitary group
kind: theorem
decl: GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_constTerm
module: Development.WeilBound.RepresentationTheoryGL.ConstantTermFiniteness.CuspidalConstantTerms.FormsSubsetFormsOnEmpty
covers: 1114
status: drafted
drafted_by: writer@claude
---
This theorem is the second input of [the finiteness of automorphic forms on a unitary group](/entry/harish-chandra-finite/). It says that the constant terms of the forms in $\mathcal{A}(U, \rho, c)$ along a maximal parabolic span a finite dimensional space. The proof is an induction over standard parabolics, down to the forms that are cuspidal relative to a parabolic.

## Statement

Use the notation of [the finiteness of automorphic forms](/entry/harish-chandra-finite/): $G = \mathrm{U}(V)$ with $\dim V = m$, an open subgroup $U$, $K_\infty$-types $\rho_\tau$ and eigenvalues $c_\tau(k)$, with the same hypotheses. Let $C$ be an $m \times r$ matrix over $E$ with $r \ge 1$, linearly independent columns and $C^* J C = 0$ (`IsIsoFrame`), so that its columns span an isotropic subspace $X_C$. Let $P_C$ be the parabolic that fixes $X_C$, with unipotent radical $N_C$, and let

$$\varphi_{P_C}(g) = \int_{N_C(F) \backslash N_C(\mathbb{A})} \varphi(ng)\, dn$$

be the [constant term](/learn/automorphic-forms/#constant-terms-and-cusp-forms) for the measure of mass $1$.

**Theorem.** The functions $\varphi_{P_C}$, for $\varphi \in \mathcal{A}(U, \rho, c)$, span a finite dimensional space.

## Proof

1. **A Witt frame.** By `exists_isWittFrame_initCols`, extend $C$ to a Witt frame: matrices $X, Y$ of size $m \times w$ with $X^* J X = Y^* J Y = 0$, $X^* J Y = 1$, an anisotropic orthogonal complement, and the first $r$ columns of $X$ equal to $C$. For a set $T$ of indices in $\{1, \ldots, w\}$ let $P_T = M_T N_T$ be the standard parabolic that fixes the flag of the spans of the first $k$ columns of $X$, for $k \in T$. Then $P_C = P_{\{r\}}$.
2. **Forms on $P_T$.** Let $\mathcal{A}_T$ (`formsOn`) be the set of smooth functions of moderate growth that are left invariant under $N_T(\mathbb{A}) M_T(F)$ and satisfy conditions 2 to 4 of $\mathcal{A}(U, \rho, c)$. For $T = \varnothing$ this contains $\mathcal{A}(U, \rho, c)$ (`forms_subset_formsOn_empty`).
3. **Constant terms stay in the family.** If $\varphi \in \mathcal{A}_S$ and $S \subseteq T$ with $T$ nonempty, then the constant term of $\varphi$ along $N_T$ is in $\mathcal{A}_T$ (`constAlong_mem_formsOn`). The proof uses `constant_term_moderate_growth_inherited`, `constant_term_parabolic_K_finite` and `constant_term_smooth_moderate_growth`. So $\varphi_{P_C} \in \mathcal{A}_{\{r\}}$.
4. **Induction.** `finite_formsOn` proves that $\mathcal{A}_T$ spans a finite dimensional space for each nonempty $T$, by strong induction on the size of the complement of $T$. Send $\varphi \in \mathcal{A}_T$ to its constant terms along $N_{T \cup \{k\}}$ for $k \notin T$. By induction, the target is finite dimensional. On the kernel, every constant term along a smaller parabolic vanishes, so the kernel lies in the forms that are cuspidal relative to $P_T$. These span a finite dimensional space by `finite_cuspOn`. Hence $\mathcal{A}_T$ is finite dimensional.

Steps 3 and 4 with $T = \{r\}$ give the theorem.

## In the Lean code

The theorem is at [FormsSubsetFormsOnEmpty.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FormsSubsetFormsOnEmpty.lean#L137), with `forms_subset_formsOn_empty`, `constAlong_mem_formsOn` and `finite_formsOn` in the same file. The set `formsOn` is in [MemFormsOnOfMemSpan.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/MemFormsOnOfMemSpan.lean#L29). The lemmas from other files:

- `LeviPart.Rg.finite_cuspOn`, in [FiniteDimensionalOfParts.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FiniteDimensionalOfParts.lean#L62). It splits the Levi $M_T$ into its general linear and unitary parts and calls `finite_slices_uPart` and `finite_slices_glPart`. We have not unfolded these. They carry the analytic content.
- `exists_isWittFrame_initCols` and `constAlong_cocompact_unique_stages`.
- The three inheritance lemmas of step 3.

In Lean the index set $T$ is a `Finset (Fin w)`, numbered from $0$, so $P_C$ is the set $\{r - 1\}$. The proof writes $r$ as $r' + 1$ for this. The base of the induction is $T = \{1, \ldots, w\}$, where there is no larger $T'$ and `finite_cuspOn` gives the whole space.
