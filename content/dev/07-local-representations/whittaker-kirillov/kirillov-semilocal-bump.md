---
id: kirillov-semilocal-bump
title: The semi-local Kirillov bump, from a Whittaker function that is not zero on the semi-local group
kind: theorem
decl: GlobalTheory.JSW.KirSemi.kirillov_semilocal_bump
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KirillovSemilocalSmoothBump
covers: 383
status: drafted
drafted_by: writer@claude
---
This theorem proves [its second name](/entry/kirillov-semilocal-smooth-bump/). It reduces to [the mirabolic form](/entry/kirillov-semilocal-mirabolic-whittaker/), whose hypothesis is that the Whittaker function is not zero at a point of the mirabolic subgroup.

## Statement

Let $E$ be a totally complex number field, $\mathbb{A}$ its adeles, $E_\infty = E \otimes_{\mathbb{Q}} \mathbb{R}$, and $G = \mathrm{GL}_{m+1}$. Let $N$ be the upper unitriangular group and $\psi_N(u) = \psi(u_{1,2} + \dots + u_{m,m+1})$ for $u \in N(\mathbb{A})$, with $\psi$ the fixed additive character of $\mathbb{A}/E$. For a function $F$ on $G(\mathbb{A})$, $W_F(g)$ is the integral of $F(ug)\,\psi_N(u)^{-1}$ over a fundamental domain for $N(E)$ in $N(\mathbb{A})$. Let $S$ be a finite set of finite places. Let $G_S$ be the set of $g \in G(\mathbb{A})$ with $g_w = 1$ at each finite $w \notin S$, and $P_S$ the set of $g \in G_S$ with last row $(0, \dots, 0, 1)$.

Let $b \colon G(\mathbb{A}) \to \mathbb{C}$ satisfy:

1. $b(ug) = \psi_N(u)\,b(g)$ for $u \in N(\mathbb{A})$;
2. there is a compact $C$ with $\{p \in P_S : b(p) \ne 0\} \subset N(\mathbb{A})\,C$;
3. $b$ is right invariant under an open subgroup of $G(\mathbb{A}_f)$;
4. for each $g$, the function $y \mapsto b(g y)$ is smooth on $G(E_\infty)$.

Let $\pi$ be a [[cuspidal representation|9AZ164C298]] of $G$, $\varphi \in \pi$, and suppose $W_\varphi(x) \ne 0$ for some $x \in G_S$.

**Theorem.** There is $F$ in $\mathcal{M}(\pi)$, the span of $\pi$ under right translations and archimedean kernel operators (`mspanR`), such that

1. $W_F = b$ on $P_S$;
2. $F$ is right invariant under an open subgroup of $G(\mathbb{A}_f)$;
3. if $t \in G(\mathbb{A})$ has $t_\infty = 1$ and $t_w = 1$ for $w \in S$, and $\varphi$ is right $t$-invariant, then so is $F$;
4. for such $t$ and $c \in \mathbb{C}$, if $W_\varphi(xt) = c\,W_\varphi(x)$ for all $x \in G_S$, then $W_F(xt) = c\,W_F(x)$ for all $x \in G_S$.

## Proof

The lemma `exists_mirabolic_nonzero` replaces $\varphi$ by a translate $\varphi_1 \in \pi$ with $W_{\varphi_1}(p) \ne 0$ for some $p \in P_S$.

1. Write $x_\infty = p_0\,\rho\,k$ with $p_0 \in G(E_\infty)$ of last row $(0, \dots, 0, 1)$, $\rho \in E_\infty^\times$ a scalar and $k$ in the unitary group (`exists_mirabolic_scalar_unitary_decomposition_archimedean`).
2. The function $c \mapsto W_\varphi(p_0\, c k\, x_f)$ is continuous on $E_\infty^\times$ (`continuous_globalWhittakerCoefficient_archimedean`) and not zero at $\rho$. So it is not zero at the image of some $\beta \in E^\times$ (`exists_field_unit_mem_open_archimedean_units`: the image of $E^\times$ meets each nonempty open subset of $E_\infty^\times$).
3. Let $s = \beta_\infty k\, x_f \in G_S$ and $\varphi_1(g) = \varphi(gs)$. Since $\varphi$ is left invariant under the rational scalar $\beta$ (`aut_central`), $\varphi_1$ is the translate of $\varphi$ by $k$ and by the finite element $x_f\beta_f^{-1}$. So $\varphi_1 \in \pi$. Also $W_{\varphi_1}(p_0) = W_\varphi(p_0 s) \ne 0$, and $p_0 \in P_S$.
4. Each $t$ as in clause 3 commutes with $s$ (`comm_of_supp`), so the hypotheses of clauses 3 and 4 pass from $\varphi$ to $\varphi_1$.

Then [the mirabolic form](/entry/kirillov-semilocal-mirabolic-whittaker/), applied to $\varphi_1$, gives $F$.

## In the Lean code

The theorem is at [line 150 of KirillovSemilocalSmoothBump.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemilocalSmoothBump.lean#L150), and `exists_mirabolic_nonzero` at [line 61](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemilocalSmoothBump.lean#L61). Condition 4 is `ContDiffOn ℝ ∞` of `chart b g` on the invertible matrices. The unitary group is `Kinf`, which we have not unfolded. The translate $\varphi_1$ is `act (Op.cpt k) (act (Op.fin (xf * z)) φ)`, in $\pi$ by `π.stable` twice.
