---
id: at-point
title: Freeness of the Hodge module at one stalk
kind: theorem
decl: PositivityTheory.Xgn.HodgeFreeStalk.at_point
module: Development.WeilBound.CoreStatements.TorusUniformisation.ChowMahlerFamilies.HodgeFreeEveryStalk
covers: 518
status: drafted
drafted_by: writer@claude
---
This theorem proves the freeness condition `HFree` for a formal germ at the stalk of one point $z$ of the base, from the characteristic polynomial condition `HChar`. It splits on the residue characteristic at $z$. Its one user is [`hodge_free_every_stalk`](/entry/hodge-free-every-stalk/), which first moves `HChar` from the generic germ to the germ at each specialization and then calls this theorem.

## Statement

Let $E$ be a CM field with host datum $H$, with the star map $a \mapsto \bar a$ on $\mathcal{O}_E$. Let $t$ be a semi-abelian scheme over $X$ with $\mathcal{O}_E$-action and a cubical line bundle, with `PowFns t`. Let $z \in X$, let $R = \mathcal{O}_{X,z}$ with residue field $\kappa(z)$, and let $g$ be a formal germ of $t$ of dimension $d$ at $\operatorname{Spec} R \to X$. Let $\rho_H(a)$ be the operator of $a \in \mathcal{O}_E$ on $R^d \times R^d$, as in [the entry on `hfree_geom`](/entry/hfree-geom/), and let $P_a$ be the characteristic polynomial of multiplication by $a$ on $\mathcal{O}_E$.

**Theorem.** Suppose that $\det(T - \rho_H(a)) = P_a(T)^r$ for each $a$ (`HChar g r`). Suppose that, if $\kappa(z)$ has characteristic $p > 0$, there is a point $x \colon \operatorname{Spec} k \to X$ with $k$ algebraically closed, image $z$, and `GeomPF t x` (`FibPF t z`). Then there are $x_1, \dots, x_r \in R^{2d}$ such that the vectors $\rho_H(b_j) x_i$, for a $\mathbb{Z}$-basis $(b_j)$ of $\mathcal{O}_E$, are an $R$-basis of $R^{2d}$ (`HFree g r`).

## Proof

Write $\rho_H(a)$ as a block matrix $h(a)$ of size $2d$ (`hm`, `rhoH_eqv`). By `formal_hermitian_action_pairing`, $a \mapsto h(a)$ is a ring map $\mathcal{O}_E \to M_{2d}(R)$ (`exists_hom`). Two facts on such maps come from other files. `representation_basis_linear_independent`: if the condition of `HFree` holds after a local map $R \to k$ to a field, it holds over $R$. This is a lifting of a basis over the residue field, in the spirit of Nakayama's lemma; we have not opened its proof. `characteristic_polynomial_free_generators`: over a field of characteristic $0$, the condition on characteristic polynomials gives the free generators.

1. **$\operatorname{char} \kappa(z) = 0$.** `hfree_char0` maps $h$ to $\kappa(z)$, applies `characteristic_polynomial_free_generators` there and lifts to $R$.
2. **$\operatorname{char} \kappa(z) = p > 0$.** Take $x$ and $k$ from `FibPF`. Let $f \colon R \to k$ be the local map at the closed point; then $p = 0$ in $k$. `formal_germ_base_change` gives a germ $g_2$ over $k$ with `IsMapOf f g g₂`. `hchar_map` moves `HChar` to $g_2$. [`height_char_free_geometric`](/entry/height-char-free-geometric/) gives `HFree` for $g_2$, and `hfree_of_map` lifts it to $g$.

## In the Lean code

The theorem is in [HodgeFreeEveryStalk.lean](lean:Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/HodgeFreeEveryStalk.lean#L148). The helper lemmas `hfree_char0`, `hfree_of_map`, `hchar_map` and `exists_hom` are in the same file, at lines 131, 124, 99 and 51. The hypotheses `hs` and `PowFns t` are used only in the case $p > 0$, where they go to `formal_germ_base_change` and `height_char_free_geometric`. The hypothesis on `FibPF` is stated for all primes $p$ with $p = 0$ in $\kappa(z)$; at most one prime has this property.
