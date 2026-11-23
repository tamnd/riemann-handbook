---
id: edge-dlog
title: The edge class of two Kummer classes over the local $q$-tower
kind: theorem
decl: GlobalTheory.EdgeLoc.edge_dlog
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.GnFixZeta
covers: 569
status: drafted
drafted_by: writer@claude
---
This theorem is the local form of [the edge class congruence for two Siegel units](/entry/pair-edge-dlog/). Over $p$-adic Laurent series in $q$, it computes modulo $p^n$ the logarithmic $q$-derivative of a $p^n$-th root whose Kummer class is the edge class of two units. `pair_edge_dlog` moves the result to modular functions.

## Statement

Let $p$ be an odd prime. Let $\mathcal{O}_0$ be the $p$-adic completion of $\mathbb{Z}_p((q))$, and $\Omega$ an algebraic closure of its fraction field. Fix compatible $\zeta_m$ of order $p^m$ and $q_m$ with $q_{m+1}^p = q_m$, $q_0 = q$. Let $G_L \subset \mathrm{Aut}(\Omega/\mathcal{O}_0)$ fix $\zeta_L$ and $q_L$, and let $G^{\mathrm{geo}}$ fix every element algebraic over $\mathbb{Z}_p$. "Integral" means integral over $\mathcal{O}_0$, and $x \equiv y \pmod{p^n}$ means $x - y \in p^n \cdot(\text{integral})$.

Let $\mathcal{O}_L = \mathcal{O}_0[x, y]/(\Phi_{p^L}(x), y^{p^L} - q)$, and $\iota \colon \mathcal{O}_L \to \Omega$ with $x \mapsto \zeta_L$, $y \mapsto q_L$. Let $\psi \colon \mathcal{O}_0 \to \Omega$ be injective with $\psi(q) = q_L$, image $\mathcal{O}_0[q_L]$, and $\psi(\sum a_i q^{p^L i}) = \sum a_i q^i$.

**Theorem.** There is $c$ with the following property. Let $1 \le n \le L$. Let $u, v$ be units of $\mathcal{O}_L$ with $d\log u = \alpha\, d\log y + \beta\, d\log x$ and $d\log v = \alpha'\, d\log y + \beta'\, d\log x$ in Kähler differentials over $\mathcal{O}_0$. Let $r^{p^n} = \iota u$, $s^{p^n} = \iota v$, with Kummer characters $x_K, y_K$ on $G_L$, and let $\lambda$ be the Kummer character of $\zeta_{L+n}$. Let $\eta$ be locally constant with $x_K(g)y_K(h) = \eta(h) - \eta(gh) + \eta(g)$ on $G^{\mathrm{geo}} \cap G_L$. Then there is an integral $o$, fixed by $G^{\mathrm{geo}} \cap G_L$, such that for each $\sigma \in G_L$ the following holds. Let $\theta$ have Kummer character on $G^{\mathrm{geo}} \cap G_L$ equal to the edge class $h \mapsto \eta(\sigma h\sigma^{-1}) - \eta(h) - x_K(h)y_K(\sigma) + x_K(\sigma)y_K(h)$. Let $\theta^{p^n} b = \kappa a$ with $\kappa \ne 0$ algebraic over $\mathbb{Z}_p$, where $a = \sum e_t \psi(A_t)$, $a' = \sum e_t \psi(q\tfrac{d}{dq}A_t)$ with Laurent series $A_t$ and integral $e_t$ algebraic over $\mathbb{Z}_p$, and $b, b'$ likewise. Let $a, b$ be units. Then
$$p^c\Bigl(\frac{a'}{a} - \frac{b'}{b}\Bigr) \equiv \sigma^{-1}(o) - o - p^c\, \iota(\alpha\beta' - \beta\alpha')\, \lambda(\sigma) \pmod{p^n}.$$

## Proof

Let $\lambda_q$ be the Kummer character of $q_{L+n}$.

1. `cup_kummer_dlog_mod_primePow_levelL`: $p^{c_1}\bigl(x_K \cup y_K + \iota(\alpha\beta' - \beta\alpha')\, \lambda \cup \lambda_q\bigr)$ is a coboundary on $G_L$.
2. `edge_class_cup_product_geometric` turns this and $\eta$ into $o_1$ such that $p^{c_2}(\text{edge class}) - (\sigma^{-1}o_1 - o_1 - p^{c_2}\iota(\alpha\beta'-\beta\alpha')\lambda(\sigma))\lambda_q$ is a coboundary on $G^{\mathrm{geo}} \cap G_L$.
3. `kummerCocycle_value_expansion_eq_logDeriv_smul`: the Kummer character of a $p^n$-th root of $a$ is $(a'/a)\lambda_q$ up to a coboundary, after scaling by $p^{c_3}$; the same for $b$.
4. Since $\kappa$ is fixed by $G^{\mathrm{geo}}$, `kum_rel` gives: the Kummer characters of $\theta$ and $b$ add up to that of $a$.
5. So $X\lambda_q$ is a coboundary for an explicit fixed integral $X$. `geometric_level_h1_coboundary` then gives $p^{c_4}X \equiv 0$.

Then $c = c_2 + c_3 + c_4$ and $o = p^{c_3+c_4}o_1$.

## In the Lean code

The theorem is in [GnFixZeta.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GnFixZeta.lean#L152). The definitions are in [NotCoboundaryConstantOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/NotCoboundaryConstantOne.lean#L15) and, for `IsReb` and `Ev`, in [EeProd.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/EeProd.lean#L65). The helper `kum_rel` is in the same file. We have not opened the lemmas of steps 1, 2, 3 and 5.

Lines 197 to 207 and 208 to 218 of the proof are the same block; the second copy shadows the first. The sequences $c_a, c_b$ of the hypotheses `Ev` do not appear in the conclusion.
