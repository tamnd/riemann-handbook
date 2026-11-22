---
id: harish-chandra-finite
title: Finiteness of automorphic forms on a unitary group
kind: theorem
decl: PositivityTheory.RgHf.harishChandraFinite
module: Development.WeilBound.RepresentationTheoryGL.ConstantTermFiniteness.CuspidalConstantTerms.FiniteOfCuspOfConstTerm
covers: 1228
status: drafted
drafted_by: writer@claude
---
This theorem proves `HarishChandraFinite`: on a unitary group $\mathrm{U}(V)$ over a CM field, the [[automorphic forms|68SJQEC11F]] with a fixed level, a fixed $K_\infty$-type and fixed eigenvalues of the center span a finite dimensional space. It is an input of [EveryCharacter from Row0b](/step/every-character-of-row/). The proof reduces the statement to cusp forms and to constant terms.

## Statement

Let $E/F$ be the CM extension of the data $D$, $V$ a Hermitian space over $E$ of dimension $m$, and $G = \mathrm{U}(V)$. For each archimedean index $\tau$, fix an embedding $\theta_\tau$, a sign vector $\varepsilon_\tau \in \{\pm 1\}^m$ and an invertible matrix $f_\tau$ with $f_\tau^* J_{\varepsilon_\tau} f_\tau$ equal to the Gram matrix of $V$ at $\tau$. Here $J_\varepsilon$ is the diagonal sign matrix. Let $K_\tau$ be the group of unitary matrices that commute with $J_{\varepsilon_\tau}$, that is $\mathrm{U}(p) \times \mathrm{U}(q)$. It maps into $G(\mathbb{A})$ at $\tau$ by $k \mapsto f_\tau^{-1} k f_\tau$.

Let $U \subset G(\mathbb{A})$ be an open subgroup, $\rho_\tau$ a continuous finite dimensional representation of $K_\tau$, and $c_\tau(k) \in \mathbb{C}$ for $k \ge 0$. Let $\mathcal{A}(U, \rho, c)$ be the set of $\varphi \colon G(\mathbb{A}) \to \mathbb{C}$ such that:

1. $\varphi$ is a smooth automorphic function of moderate growth (`IsAutFunSm`): left invariant under $G(F)$, continuous, of some open level, smooth in the archimedean variable, in a finite dimensional space that the Gelfand operators below preserve, and of moderate growth in each derivative;
2. $\varphi(gu) = \varphi(g)$ for $u \in U$ with trivial archimedean part;
3. for each $\tau$ and $x$, the function $k \mapsto \varphi(x k)$ on $K_\tau$ is in the span of the matrix coefficients of $\rho_\tau$;
4. $\Delta_{\tau,k} \varphi = c_\tau(k) \varphi$ for all $\tau, k$, where $\Delta_{\tau,k} = \sum_{i_0, \ldots, i_k} R(E_{i_0 i_1}) R(E_{i_1 i_2}) \cdots R(E_{i_k i_0})$ is the Gelfand operator $\operatorname{tr}(E^{k+1})$ at $\tau$.

**Theorem.** The span of $\mathcal{A}(U, \rho, c)$ is finite dimensional.

This is the finiteness theorem of Harish-Chandra (*Automorphic forms on semisimple Lie groups*, Lecture Notes in Math. 62, 1968, Theorem 1) for $G = \mathrm{U}(V)$. See also the [Learn page](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups).

## Proof

The proof is one call to `finite_of_cusp_of_constTerm` with two inputs:

- `cuspFinite`: the cusp forms in $\mathcal{A}(U, \rho, c)$ span a finite dimensional space;
- [`finite_constTerm`](/entry/finite-const-term/): for each isotropic frame $C$, the constant terms $\varphi_{P_C}$ of the $\varphi \in \mathcal{A}(U, \rho, c)$ span a finite dimensional space.

The lemma is linear algebra. The conditions are linear, so the span $S$ of $\mathcal{A}(U, \rho, c)$ is the set itself (`mem_forms_of_mem_span`). For each rank $r$ for which an isotropic frame exists, choose one, $C_r$, with parabolic $P_r$. Let $\Psi$ send $\varphi \in S$ to its constant terms along the $P_r$. The target is finite dimensional by the second input. If $\Psi(\varphi) = 0$, then the constant term of $\varphi$ along every isotropic frame vanishes (`constTerm_eq_zero_of_frame`), so $\varphi$ is a cusp form (`isCuspFun_iff`). So $\ker \Psi$ is finite dimensional by the first input, and so is $S$.

## In the Lean code

The theorem is at [FiniteOfCuspOfConstTerm.lean](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FiniteOfCuspOfConstTerm.lean#L129), and the reduction lemma at [L61](lean:Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FiniteOfCuspOfConstTerm.lean#L61). The statement is in [HarishChandraFinite.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HarishChandraFinite.lean#L50). `HCCusp.cuspFinite` is in `IteratedDerivOneP.lean`; we read its statement but did not unfold its proof.

The Lean form fixes the eigenvalues of $\operatorname{tr}(E^{k+1})$ for all $k$, not an ideal of finite codimension of the center. This is a special case of Harish-Chandra's statement. The test `IsCuspFun` uses only the maximal parabolics. The reduction lemma does not use that $U$ is open, nor the hypotheses on $\theta$, $f$ and $\rho$.
