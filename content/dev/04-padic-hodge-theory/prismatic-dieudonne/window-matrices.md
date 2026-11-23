---
id: window-matrices
title: Period and Frobenius matrices of a biconnected p-divisible group over a frame
kind: theorem
decl: GlobalTheory.QLog.WindowMat.window_matrices
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasPeriodIntegral
covers: 1206
status: drafted
drafted_by: writer@claude
---
This theorem attaches to a $p$-divisible group $G$ over $\mathcal{O}_C$, connected with connected dual, a Frobenius matrix $U$ and period matrices $Y$ and $\Gamma$ over a frame ring $B$. They come from quasi-logarithms. It is step 2 of the proof of [a Dieudonné theory over $A_{\inf}$](/entry/prismatic-dieudonne-hodge/), where the matrices are lifted to $A_{\inf}$.

## Statement

Let $p$, $C$, $v$, $\mathcal{O}$ and $\varepsilon$ be as in [the parent entry](/entry/prismatic-dieudonne-hodge/). In particular for each $n$ the untilt of the $n$-th $p$-power root of $\varepsilon \in \mathcal{O}^\flat$ is a primitive $p^n$-th root of unity (`IsPrimitiveSystem`). Put $\mu = [\varepsilon] - 1 \in A_{\inf}$.

A *frame* $F$ (`BFrame ε`) is a $p$-adically complete ring $B$ with a map $a \colon A_{\inf} \to B$, a surjection $\theta \colon B \to \mathcal{O}$ extending Fontaine's $\theta$, a Frobenius lift $\sigma$, and an element $\tau$ with $p\tau = a(\mu)$, $\tau^2 = 0$ and $B = a(A_{\inf}) + \tau\, a(A_{\inf})$, with more conditions that we do not list.

Say $M\sigma$ is *nilpotent mod $\mathfrak{m}$* if for some $N$ all entries of $(M\sigma)^N v$ map under $\theta$ to non-units (`IsNil`). Write $\operatorname{blk}(u, u')$ for the diagonal matrix with $d$ entries $u$ and then $k$ entries $u'$.

**Theorem.** Let $G$ be a $p$-divisible group over $\mathcal{O}$ of height $h$. Suppose that $G$ and its dual $G^\vee$ are connected (each finite level is a local ring). Let $F$ be a frame. Then there are $d + k = h$, $U \in \mathrm{GL}_{h}(B)$, $Y \in M_{h}(B)$, $\Gamma \in M_{h}(B)$, a $\mathbb{Z}_p$-basis $t$ of $T_pG$, elements $\chi_1, \dots, \chi_h$ of $T_pG^\vee$, a basis $w$ of $\omega_G$ and a basis $l$ of $\operatorname{Lie}(G^\vee)$ with:

1. $\sigma(Y) = \operatorname{blk}(p,1)\, U^{\mathsf T} Y$ and $U \operatorname{blk}(p,1)\, \sigma(\Gamma)^{\mathsf T} = p\, \Gamma^{\mathsf T}$;
2. $\Gamma Y = a(\mu) \cdot 1_h$;
3. $\theta(Y_{im}) = 0$ for the first $d$ rows, and $\theta(\Gamma_{mj}) = 0$ for the last $k$ columns;
4. $U \operatorname{blk}(p,1)\,\sigma$ and $(U^{\mathsf T})^{-1} \operatorname{blk}(1,p)\,\sigma$ are nilpotent mod $\mathfrak{m}$;
5. $\langle t_m, \chi_{m'} \rangle_\varepsilon = \delta_{mm'}$ for the pairing `epsPairing`;
6. $\theta(Y_{d+j,m}) = l_j(\mathrm{HT}(t_m))$, with $\mathrm{HT} \colon T_pG \to \omega_{G^\vee}$ the Hodge-Tate map;
7. $\operatorname{dlog}(\chi_m) = \sum_i \theta(\Gamma_{m,i})\, w_i$.

We read `hodgeTate` and `dlog` by their names and types. We know no published source for this exact form.

## Proof

1. `exists_pDivGroupFormalChart_of_connected` gives a formal chart of $G$: coordinates of dimension $d$ and a formal group law $\mu_G$ over $\mathcal{O}$. `chartDim_add_finrank_dual_lie_eq_height` gives $d + k = h$.
2. `exists_adapted_quasiLog_basis_pDivGroup_lieDual` gives an adapted basis $e^0$ of quasi-logarithms over $\mathcal{O}$. `exists_formalGroupLawLift_of_surjective` and `exists_lift_adapted_basis_quasi_logarithms_frame` lift $\mu_G$ and $e^0$ to $B$.
3. `exists_frobenius_matrix_quasiLogarithm_basis` gives $U$: the Frobenius of $e_i$ is $\sum_l (U \operatorname{blk}(p,1))_{li}\, e_l$ up to an integral series. `frobenius_matrix_isUnit_adapted_basis` makes $U$ invertible, and `frobenius_nilpotent_mod_maximal_connected_pDivGroup` and `isNil_dual_frobenius_alt` give relation 4.
4. `exists_dual_basis` gives $t$ and $\chi$ with relation 5.
5. $Y_{lm}$ is the unique period of $e_l$ at $t_m$ (`exists_unique_period_quasiLogarithm_pDivGroup`). `exists_quasiLogarithm_of_dualCharacter` gives a quasi-logarithm $f_m$ of $\chi_m$, and $\Gamma_m$ is its coordinate vector in the basis $e$.
6. The other relations follow from the uniqueness and linearity of periods (`hasPeriod_unique`, `hasPeriod_comb`), with `quasiLogarithm_period_frobenius_twist` and `quasiLogarithm_period_eq_tangent_hodgeTate`. The rest is bookkeeping.

## In the Lean code

The theorem is at [HasPeriodIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasPeriodIntegral.lean#L95). `BFrame`, `blk` and `IsNil` are in [EqZeroOfForallPowDvd.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EqZeroOfForallPowDvd.lean#L283). Connectedness is `PDivLat.IsConn` in [GhostFrobenius.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/GhostFrobenius.lean#L85), and $\mu$ is `Sandwich.mu` in [XiMulNu.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/XiMulNu.lean#L26).

- The conclusion holds for every frame $F$. The theorem does not say that a frame exists; the parent gets one from `exists_bFrame`.
- The elements $\chi_m$ are not said to form a basis of $T_pG^\vee$, only to be dual to $t$.
