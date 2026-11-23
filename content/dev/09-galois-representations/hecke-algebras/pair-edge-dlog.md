---
id: pair-edge-dlog
title: The edge class of two Siegel units and a product of Eisenstein series
kind: theorem
decl: GlobalTheory.pair_edge_dlog
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.SiegelUnitEdgeClassKummerDlogCongruence
covers: 1017
status: drafted
drafted_by: writer@claude
---
This theorem computes, modulo $p^n$ and up to a coboundary, the logarithmic $q$-expansion of an "edge" Kummer class made from two Siegel units. The answer is a product of two smoothed Eisenstein series. It is restated as [the Siegel unit edge congruence](/entry/siegel-unit-edge-class-kummer-dlog-congruence/), which [the Siegel unit lemma `one`](/entry/one/) uses.

## Statement

Let $p$ be an odd prime. Then there is a constant $c$ with the following property.

Let $X$ be a tower of modular function fields over $\overline{\mathbb{Q}} \subset \mathbb{C}$ with holomorphic $j$-function, and let $A$ be a valuation ring of $\overline{\mathbb{Q}}$ with $p$ in its maximal ideal. Let $1 \le n \le L$, let $N > 0$ be prime to $p$, and let $c, d > 1$ be prime to $6Np$. Let $(A_1, a_2)$ and $(B_1, b_2)$ be integer pairs with $N \mid a_2, b_2$, $a_2 \equiv Ng$ and $b_2 \equiv Nh \pmod{p^L}$, and $Np^L \nmid A_1, B_1$. Let $F \subset K \subset \Omega'$ with $K/F$ normal and $\Omega' = \overline{K}$, and let $e$ embed $K$ into the functions of $X$ invariant under $T^{p^L}$.

- Put $M = Np^L$. In $K$ we have $\zeta_{p^n}$ and two Siegel units: $a$ is the image of $g_{c}(A_1/M, a_2/M)$ under $\operatorname{diag}(N, 1)$, and $b$ the same with $d$ and $(B_1, b_2)$. Here $g_c$ is the Lean `siegel X c`, which we have not unfolded. In $\Omega'$ take $\alpha^{p^n} = a$ and $\beta^{p^n} = b$.
- Let $x, y \colon \mathrm{Gal}(\Omega'/F) \to \mathbb{Z}/p^n$ be the Kummer characters of $\alpha$ and $\beta$. Let $\eta$ be a locally constant cochain with $x(g)y(h) = \eta(h) - \eta(gh) + \eta(g)$ for $g, h$ in $\mathrm{Gal}(\Omega'/K)$.

**Theorem.** There is $\xi \colon \mathbb{Q} \to A$ such that the following holds. Let $s \in \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ preserve $A$, fix $\zeta_{p^L}$ and fix $F$, with $s(\zeta_{p^{L+n}}) = \zeta_{p^n}^t \zeta_{p^{L+n}}$. Let $\sigma \in \mathrm{Gal}(\Omega'/F)$ act on $K$ as $s$ acts on $X$. Let $w \in K$ have a $p^n$-th root whose Kummer character on $\mathrm{Gal}(\Omega'/K)$ is the edge class
$$h \mapsto \eta(\sigma h \sigma^{-1}) - \eta(h) - x(h)y(\sigma) + x(\sigma)y(h).$$
Let $\varphi$ be a logarithmic $q$-expansion of $w$ modulo $p^n$ (`IsDl`: $w = \kappa a'/b'$ with $\varphi \equiv \theta a'/a' - \theta b'/b'$, where $\theta = p^L q\,d/dq$). Then for each $r \in \mathbb{Q}$,
$$p^{c} \varphi_r \equiv s^{-1}(\xi_r) - \xi_r - p^{c}(A_1 h - g B_1)\, t \cdot [q^r]\bigl(F_c \cdot F_d\bigr) \pmod{p^n A}.$$
Here $F_c = c^2 E_{A_1, a_2} - c\, E_{cA_1, ca_2}$ and $F_d$ is the same with $d$ and $(B_1, b_2)$. The series $E_{a_1, a_2}$ has $m$-th coefficient $\sum_{k \mid m} \bigl([m/k \equiv a_1]\, \zeta_M^{a_2 k} - [-m/k \equiv a_1]\, \zeta_M^{-a_2 k}\bigr)$ for $m \ge 1$, with congruences mod $M$ and $\zeta_M = e^{2\pi i/M}$. We have not unfolded its constant term. The product is the Cauchy product, and $[q^r]$ takes the coefficient of index $rp^L$.

## Proof

1. `EdgeLoc.edge_dlog` is the same congruence for units with logarithmic coordinates in a field $\Omega_p$ with a $p$-adic tower. It gives $c_0$, and $c = c_0 + 1$. `exists_cusp_embedding` gives $\Omega_p$ and the maps to it.
2. `siegel_logCoords_alt`, for $a$ and for $b$, gives local units with logarithmic coordinates.
3. `extend_to_closure` extends the embedding of $K$ to $\Omega'$, and `galois_side` moves $x$, $y$, $\eta$ and the edge relation to $\Omega_p$.
4. The local result gives an integral element. `geofix`, `ev_ring` and `exists_xi` turn it into $\xi$.
5. For a given $s$, `dl_pres` writes $w$ as a quotient of two expansions, and the local result gives a congruence of values.
6. `value_cong` and `coef_bridge` turn it into a congruence of coefficients, and `isDl_unique` replaces the expansion by $\varphi$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [SiegelUnitEdgeClassKummerDlogCongruence.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SiegelUnitEdgeClassKummerDlogCongruence.lean#L457). The helpers of steps 3 to 6 are in the same file. The local result `edge_dlog` is in [GnFixZeta.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GnFixZeta.lean#L152). The definitions are in [EeProd.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/EeProd.lean#L28) and [Integral.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/Integral.lean#L27). We have not unfolded the local tower `K5.Tower`.
