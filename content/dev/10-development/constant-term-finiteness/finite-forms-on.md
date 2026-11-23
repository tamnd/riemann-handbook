---
id: finite-forms-on
title: Finiteness of the forms on a standard parabolic, by induction on the flag
kind: theorem
decl: GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_formsOn
module: Development.WeilBound.RepresentationTheoryGL.ConstantTermFiniteness.CuspidalConstantTerms.FormsSubsetFormsOnEmpty
covers: 951
status: drafted
drafted_by: writer@claude
---
This theorem is step 4 of [the finiteness of constant terms](/entry/finite-const-term/). It says that for each nonempty set $T$ of flag indices, the family $\mathcal{A}_T$ spans a finite dimensional space. An induction over the flags reduces it to the forms that are cuspidal relative to $P_T$, which [the finiteness of relative cusp forms](/entry/finite-cusp-on/) treats.

## Statement

Use the notation of [the finiteness of constant terms](/entry/finite-const-term/): $G = \mathrm{U}(V)$, a Witt frame $X, Y$ with $w$ columns, the standard parabolic $P_T = M_T N_T$ for $T \subseteq \{1, \ldots, w\}$, and the set $\mathcal{A}_T$ (`formsOn`) of smooth functions of moderate growth on $G(\mathbb{A})$, left invariant under $N_T(\mathbb{A}) M_T(F)$, with the other conditions of [the finiteness of automorphic forms](/entry/harish-chandra-finite/).

**Theorem.** For each $j \ge 0$ and each nonempty $T$ whose complement has $j$ elements, the span of $\mathcal{A}_T$ is finite dimensional.

## Proof

The proof is by strong induction on $j$. Fix $T$. The span of $\mathcal{A}_T$ is $\mathcal{A}_T$ itself (`mem_formsOn_of_mem_span`).

1. **Maps to larger flags.** For $k \notin T$ put $T_k = T \cup \{k\}$. The quotient $N_{T_k}(F) \backslash N_{T_k}(\mathbb{A})$ is compact (`cocompact_unip_std`), so each $\varphi \in \mathcal{A}_T$ has a constant term $\varphi_{T_k}$ along $N_{T_k}$, and $\varphi_{T_k} \in \mathcal{A}_{T_k}$ (`constAlong_mem_formsOn`). The map $L_k \colon \varphi \mapsto \varphi_{T_k}$ is linear. The complement of $T_k$ has $j - 1$ elements, so the target of $L_k$ is finite dimensional by induction.
2. **The kernel.** Let $\Psi = (L_k)_{k \notin T}$. Suppose $\Psi\varphi = 0$, and let $T' \supsetneq T$. Choose $k \in T' \setminus T$. The constant term along $N_{T'}$ is the constant term along $N_{T'}$ of $\varphi_{T_k}$ (constant terms in stages, the last part of `constAlong_cocompact_unique_stages`), so it is $0$. Thus $\ker \Psi$ lies in the forms cuspidal relative to $P_T$, and `finite_cuspOn` makes it finite dimensional.
3. **Conclusion.** The image and the kernel of $\Psi$ are finite dimensional, so the domain is too.

When $T = \{1, \ldots, w\}$ there is no $k$, the product is $0$, and the kernel is all of $\mathcal{A}_T$. Then step 2 is the whole proof.

## In the Lean code

The theorem is at [FormsSubsetFormsOnEmpty.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FormsSubsetFormsOnEmpty.lean#L68). It uses:

- `constAlong_mem_formsOn`, in the same file.
- `constAlong_cocompact_unique_stages`, in [ConstAlongCocompactUniqueStages.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConstAlongCocompactUniqueStages.lean#L77).
- `cocompact_unip_std` and `isConstTermOn_iff_ratPts_inf`, for the existence of the constant term.
- `LeviPart.Rg.finite_cuspOn`.

The statement carries $j$ as an explicit variable for the induction. The hypotheses that $U$ is open, that the frames form a frame family and that each $\rho_\tau$ is continuous are used only to pass them to `finite_cuspOn`.
