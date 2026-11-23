---
id: hfree-geom
title: The characteristic polynomial condition gives freeness at a geometric point
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Flat.hfree_geom
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.HeightCharFreeGeometric
covers: 482
status: drafted
drafted_by: writer@claude
---
At a geometric point of characteristic $p$ where the fibre is an extension of an abelian variety by a torus, this theorem turns a condition on characteristic polynomials into freeness of a module of rank $2d$ over $k \otimes \mathcal{O}_E$. Its statement form is [`height_char_free_geometric`](/entry/height-char-free-geometric/). Its user [`HodgeFreeStalk.at_point`](/entry/at-point/) leads to [`germ_system_height_free`](/entry/germ-system-height-free/).

## Statement

Let $E$ be a CM field with host datum $H$ and conjugation $a \mapsto \bar a$. Let $t$ be a semi-abelian scheme over $X$ with $\mathcal{O}_E$-action and a cubical line bundle $L$. Let $x \colon \operatorname{Spec} k \to X$ with $k$ algebraically closed of characteristic $p > 0$.

A *formal germ* $g$ of dimension $d$ at $x$ is a formal group law of dimension $d$ over $k$ with an $\mathcal{O}_E$-action, power series data for the cubical structure, and a chart to $t$ near $x$ (`GermAt.chart`, not unfolded here). Let $\rho(a)$ be the linear term of the action of $a$, and $A(a)$ the bilinear term of the series $\mathrm{ad}(a)$. Put
$$\rho_H(a)(y_1, y_2) = \bigl(\rho(a) y_1,\ \rho(\bar a)^{T} y_2 - A(a)^{T} y_1\bigr) \quad \text{on } k^d \times k^d.$$

- `HChar g r`: for each $a \in \mathcal{O}_E$, $\det(T - \rho_H(a)) = P_a(T)^r$, with $P_a$ the characteristic polynomial of multiplication by $a$ on $\mathcal{O}_E$ over $\mathbb{Z}$.
- `HFree g r`: there are $x_1, \dots, x_r \in k^{2d}$ such that the vectors $\rho_H(b_j) x_i$, for a $\mathbb{Z}$-basis $(b_j)$ of $\mathcal{O}_E$, form a $k$-basis. That is, $k^{2d}$ is free of rank $r$ over $k \otimes \mathcal{O}_E$.
- `GeomPF t x`: the fibre $t_x$ carries a `TorusExtension` with quotient $B$, and $L$ on $t_x$ is pulled back from a line bundle on $B$ with `Out.KTriv`. We have not unfolded these two names.
- `PowFns t`: a condition on global functions of the powers of $t$.

**Theorem.** If `PowFns t`, `GeomPF t x` and `HChar g r`, then `HFree g r`.

## Proof

1. **The torus and the abelian part.** `T.abelian_quotient_of_power_fns` gives an exact sequence $0 \to T \to t_x \to B \to 0$ with $B$ proper. With a germ $g_B$ of $B$ of dimension $d'$ (`T.exists_formal_germ_local`), `T.abelian_quotient_lattice` gives an $\mathcal{O}_E$-module $\Lambda$, a surjection $P \colon k^d \to k^{d'}$ and an injection $j \colon k \otimes \Lambda \to k^d$ onto $\ker P$, compatible with $\rho$.
2. **A gauge.** `T.abelian_quotient_bilinear` gives a matrix $Z$ with $A(a) + \rho(a)^T Z - Z\rho(\bar a) = P^T A_B(a) P$. The change of variables $y_2 \mapsto y_2 + Z^T y_1$ keeps $\dim\ker\rho_H(a)$ (`finrank_ker_gauge`).
3. **The kernel bound.** For $a \ne 0$, linear algebra (`ker_bound`) gives
$$\dim\ker\rho_H(a) \le \dim\ker(\bar a \mid k \otimes \Lambda) + \dim\ker\rho_H^B(a) + \dim\ker(a \mid k \otimes \Lambda).$$
`T.lattice_kernel_rank_bound_norm` bounds the torus terms. For $B$, `T.exists_finite_kernel_nonzero` gives that $B[a]$ is finite of order $m$ with $m^{[E:\mathbb{Q}]} = |N a|^{2d'}$, and `T.proper_multiplication_kernel` gives $p^{\dim\ker\rho_H^B(a)} \mid m$. The lemma `numeric`, with $2d = [E:\mathbb{Q}]\,r$ from `HChar` at $a = 1$, gives $\dim\ker\rho_H(a) \le r\,v_p(N a)$.
4. **Freeness.** `T.exists_free_basis_of_kernel_rank_le_norm_valuation`: a representation of $\mathcal{O}_E$ over $k$ with characteristic polynomials $P_a^r$ and $\dim\ker\rho(a) \le r\,v_p(Na)$ for all $a \ne 0$ is free of rank $r$. It applies since $\rho_H$ is a ring map (`T.formal_hermitian_action_pairing`).

## In the Lean code

The theorem is in [HeightCharFreeGeometric.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/HeightCharFreeGeometric.lean#L230). `HChar` and `HFree` are in [GermSys.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/GermSys.lean#L47), $\rho_H$ is `rhoH` in [GermComp1ZeroPointLeft.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/GermComp1ZeroPointLeft.lean#L39), and `GeomPF`, `PowFns` and `GermAt` are in [ToFirst.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ToFirst.lean#L18). We have not opened the proofs of the statement forms above. The name says "height", but the statement has no height.
