---
id: hodge-free-every-stalk
title: Freeness of the formal germ at every specialization of the generic point
kind: theorem
decl: PositivityTheory.Xgn.hodge_free_every_stalk
module: Development.WeilBound.CoreStatements.TorusUniformisation.ChowMahlerFamilies.HodgeFreeEveryStalk
covers: 527
status: drafted
drafted_by: writer@claude
---
This theorem moves the characteristic polynomial condition `HChar` from the generic germ of a germ system to the germ at each specialization, and then proves the freeness condition `HFree` there. Its one user is the second name [`hfree_at_component_stalks`](/entry/hfree-at-component-stalks/), whose entry sketches the same three steps. The last step, freeness at one stalk, is [`at_point`](/entry/at-point/).

## Statement

Let $E$ be a CM field with host datum $H$, and let the star map on $\mathcal{O}_E$ be $a \mapsto \bar a$. Let $t$ be a semi-abelian scheme with $\mathcal{O}_E$-action over a scheme $X$ (`SAB H X`). Let $\Omega$ be a field of characteristic $0$, $\xi \colon \operatorname{Spec} \Omega \to X$ a point with image $\eta$, and $M$ a Lie model of $t$ at $\xi$ of dimension $d$. Let $\operatorname{Cpt}(\xi)$ be the set of points $x \in X$ with $\eta \rightsquigarrow x$. A germ system $S$ gives a formal germ $g_0$ of $t$ at $\xi$ and a germ $g_x$ over $\mathcal{O}_{X,x}$ for each $x \in \operatorname{Cpt}(\xi)$. It also gives, for each $x$, an isomorphism of formal germs from $g_0$ to the base change of $g_x$ along $\mathcal{O}_{X,x} \to \Omega$.

For a germ $g$ over a ring $R$, let $\rho_H(a)$ be the operator of $a \in \mathcal{O}_E$ on $R^d \times R^d$, and let $P_a$ be the characteristic polynomial of multiplication by $a$ on $\mathcal{O}_E$ over $\mathbb{Z}$. `HChar g r` says $\det(T - \rho_H(a)) = P_a(T)^r$ for all $a$. `HFree g r` says that $R^{2d}$ is free over $\mathcal{O}_E \otimes R$ on $r$ generators, in the form of [`at_point`](/entry/at-point/).

**Theorem.** Assume `PowFns t`. Suppose that $\mathcal{O}_{X,\eta} \to \Omega$ is bijective and that $\mathcal{O}_{X,x} \to \Omega$ is injective for each $x \in \operatorname{Cpt}(\xi)$ (`IsCptGen ξ`). Suppose `HChar g₀ r`, and `FibPF t x` for each $x \in \operatorname{Cpt}(\xi)$ whose residue field has characteristic $p > 0$. Then `HFree g_x r` holds for every $x \in \operatorname{Cpt}(\xi)$.

## Proof

Fix $x$ and let $g_x^\Omega$ be the base change of $g_x$ to $\Omega$.

1. **Transport** (`hchar_iso`). By `formal_isomorphism_transport`, the isomorphism from $g_0$ to $g_x^\Omega$ gives a bijective linear map $\Omega^{2d} \to \Omega^{2d}$ that conjugates $\rho_H(a)$ for $g_x^\Omega$ to $\rho_H(a)$ for $g_0$. Conjugate maps have the same characteristic polynomial, so `HChar` holds for $g_x^\Omega$.
2. **Descent** (`hchar_of_map`). Write $\rho_H(a)$ as a block matrix $h(a)$ of size $2d$ (`charpoly_eq`). The matrix of $g_x^\Omega$ is the image of that of $g_x$ (`hm_map`), and characteristic polynomials commute with base change. Since $\mathcal{O}_{X,x} \to \Omega$ is injective, so is the map on polynomial rings. So `HChar` holds for $g_x$.
3. **Freeness at the stalk.** [`at_point`](/entry/at-point/) gives `HFree g_x r`, by residue characteristic $0$ or $p$.

## In the Lean code

The theorem is in [HodgeFreeEveryStalk.lean](lean:Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/HodgeFreeEveryStalk.lean#L178). The lemmas `hchar_of_map` and `hchar_iso` are at lines 105 and 113, and `at_point` at line 148. The definitions `HFree`, `HChar` and `GermSys` are in [GermSys.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/GermSys.lean#L19). Of `IsCptGen ξ` only the injectivity part is used. `PowFns t` and the star condition go unchanged to `at_point`. We have not unfolded `PowFns`.
