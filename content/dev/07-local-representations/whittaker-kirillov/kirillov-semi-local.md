---
id: kirillov-semi-local
title: A semi-local Kirillov statement on the mirabolic subgroup
kind: theorem
decl: GlobalTheory.JSW.MirSemi.kirillov_semiLocal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KirillovSemiLocalMirabolicAbstract
covers: 309
status: drafted
drafted_by: writer@claude
---
A space of Whittaker-type functions on $\mathrm{GL}_n(\mathbb{A}_E)$ with enough stability realizes every smooth function on the semi-local mirabolic set that is compactly supported modulo $N$. Its restatement [`T.kirillov_semiLocal_mirabolic_abstract`](/entry/kirillov-semi-local-mirabolic-abstract/) is used by [`MirSemi.kirillov_semilocal`](/entry/kirillov-semilocal/), which applies it to the Whittaker functions of a cusp form.

## Statement

Let $E$ be a totally complex number field, $n = m + 1$, $G = \mathrm{GL}_n(\mathbb{A}_E)$ and $S$ a finite set of finite places of $E$. Let $N \subset G$ be the upper unitriangular matrices and $\psi_N(u) = \psi(\mathrm{superDiag}(u))$, with $\psi$ the standard additive character of $\mathbb{A}_E$ (`superDiag`, not unfolded). Let $G_S$ be the set of $g \in G$ with $g_w = 1$ at each finite $w \notin S$. Let $P_S$ be the set of $g \in G_S$ whose last row is $(0, \dots, 0, 1)$. For $y \in \mathrm{GL}_n(E_\infty)$ let $\mathrm{ht}(y) = 1 + \|y\| + \|y^{-1}\|$.

Let $b \colon G \to \mathbb{C}$ satisfy:

1. $b(ug) = \psi_N(u) b(g)$ for $u \in N$;
2. there is a compact $C \subset G$ such that each $p \in P_S$ with $b(p) \neq 0$ lies in $NC$;
3. $b$ is right invariant under an open subgroup of $\mathrm{GL}_n(\mathbb{A}_f)$;
4. for each $g$, the map $y \mapsto b(gy)$ is $C^\infty$ on $\mathrm{GL}_n(E_\infty)$, seen as an open set of matrices.

Let $\mathcal{W}$ be a complex vector space of functions on $G$ such that each $W \in \mathcal{W}$:

1. satisfies $W(ug) = \psi_N(u) W(g)$;
2. stays in $\mathcal{W}$ after right translation by any $h \in G_S$;
3. stays in $\mathcal{W}$ after convolution $g \mapsto \int_X k(x) W(g\gamma(x))\,d\nu(x)$ by a kernel $\gamma \colon X \to \mathrm{GL}_n(E_\infty)$ with $|k| \cdot \mathrm{ht}(\gamma)^r$ integrable for all $r$;
4. has moderate growth at infinity: $y \mapsto W(gy)$ is continuous on $\mathrm{GL}_n(E_\infty)$ and bounded by $c\,\mathrm{ht}(y)^r$;
5. is right invariant under an open subgroup of $\mathrm{GL}_n(\mathbb{A}_f)$.

**Theorem.** If some $W_0 \in \mathcal{W}$ is nonzero at some $p_0 \in P_S$, then some $W \in \mathcal{W}$ equals $b$ on $P_S$.

This has the shape of the fact that a Kirillov model contains the smooth functions on the mirabolic subgroup with compact support modulo $N$. We do not name a source for this semi-local form.

## Proof

1. **Patching over the finite places.** `exists_eq_on_mirabolic_of_slices_finitePlaces` reduces the theorem to slices. It is enough that for each $q \in P_S$ with $q_\infty = 1$ some $W \in \mathcal{W}$ equals $b$ at each point $qy \in P_S$ with $y \in \mathrm{GL}_n(E_\infty)$.
2. **A form that is nonzero at $q$.** Fix such a $q$. Since $q^{-1}p_0 \in G_S$, the translate $W'(g) = W_0(g q^{-1} p_0)$ lies in $\mathcal{W}$, and $W'(q) = W_0(p_0) \neq 0$.
3. **The archimedean step.** `semiLocal_kirillov_archimedean_kernel_complexPlaces`, applied to $b$, $W'$ and $q$, gives a kernel of rapid decay whose convolution with $W'$ equals $b$ on the slice of $q$. By condition 3 on $\mathcal{W}$, it lies in $\mathcal{W}$.

## In the Lean code

The theorem is at [line 16 of KirillovSemiLocalMirabolicAbstract.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemiLocalMirabolicAbstract.lean#L16). The sets `NA`, `supS`, `mirS`, the character `psiN` and the condition `IsRapidInf` are in [IsRapidInf.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsRapidInf.lean#L19). The convolution `kerInf` is in [MeasurableCompInfGL.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/MeasurableCompInfGL.lean#L20). `chart`, for condition 4 on $b$, is in [DifferentiableAtChart.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/DifferentiableAtChart.lean#L248). Here $E_\infty$ is `Cinf E`, a copy of $\mathbb{C}$ for each infinite place.

The two lemmas are proved by citing `KirArchTransfer.kirillov_arch` and `MirPatch.exists_eq_on_mirS_of_slices`, which we have not unfolded.

The restatement `T.kirillov_semiLocal_mirabolic_abstract` has the same statement and is proved by this theorem. The names `MirSemi.kirillov_semiLocal` (this theorem) and `MirSemi.kirillov_semilocal` (its user) differ only in one capital letter but have different statements.
