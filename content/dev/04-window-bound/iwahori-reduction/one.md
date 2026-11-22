---
id: one
title: The log derivative of one translated Siegel unit edge
kind: theorem
decl: UpperTheory.Kd.L.one
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.SiegelFixedPoints.CoefQCmulMem
covers: 1048
status: drafted
drafted_by: writer@claude
---
This theorem treats one term of the Siegel zeta class: the Kummer element `wkMu` built from two Siegel units, moved by one matrix $g \in \Gamma_0(N)$. The log derivative mod $\ell^n$ of its $q$-expansion is $N^3 t$ times a product of two weight one Eisenstein series, plus a coboundary. [`mackey`](/entry/mackey/) sums it over all the terms of the class. The analytic input is the edge congruence for a pair of Siegel units, which this theorem specializes.

## Statement

For $j \geq 1$, a level $L$, a root of unity $\zeta$ of order $L$ and $a_1, a_2 \in \mathbb{Z}$, `eisF` is the $q$-expansion with constant term $-B_j(\{a_1/L\})/j$ (a special formula when $j = 1$) and $n$-th coefficient
$$\sum_{d \mid n} \Bigl( [\,n/d \equiv a_1\,] \bigl(\tfrac{n/d}{L}\bigr)^{j-1} \zeta^{a_2 d} - [\,-n/d \equiv a_1\,] \bigl(\tfrac{-n/d}{L}\bigr)^{j-1} \zeta^{-a_2 d} \Bigr),$$
the congruences taken mod $L$. This is the $q$-expansion of an Eisenstein series of weight $j$ and level $L$. The smoothed series is $c^2 E_{a_1,a_2} - c^{2-j}E_{ca_1,ca_2}$. For $g \in \mathrm{SL}_2(\mathbb{Z})$, $E_r(g)$ (`EE`) is the coefficient at $\ell^{m+n} r$ of the product of the smoothed weight one series for $c$ and $d$, of level $N\ell^{m+n}$, with parameters made from the entries of $g$ and from $x$.

**Theorem.** Let $\ell$ be a prime. There is $c_c$ such that for all `Par` data (see [`law`](/entry/law/)), each valuation ring $A$ with $\ell$ in its maximal ideal, $x \in \mathbb{Z}/N$, $m, n \geq 1$, and $g \in \Gamma_0(N)$ with $\ell \nmid g_{00}$ and $\ell \nmid g_{10}$:

1. each $E_r(g)$ lies in $A$;
2. there is $\xi \colon \mathbb{Q} \to A$ such that, for each $s$ that fixes $\mu_M$ ($M = \ell^{m+n}N^2$) and preserves $A$, each $t$ with $s(\zeta_{\ell^{m+2n}}) = \zeta_{\ell^n}^t \zeta_{\ell^{m+2n}}$, and each log derivative $\varphi$ mod $\ell^n$ of the $q$-expansion of $g \cdot w_s$ (`IsDl`, period $M$),
$$\ell^{c_c}\varphi_r \equiv s(\xi_r) - \xi_r + \ell^{c_c} N^3 E_r(g)\, t \pmod{\ell^n A}.$$

## Proof

The case $\ell = 2$ is excluded by `Par`. Part 1: $\ell$ divides neither parameter of the two series, so their coefficients lie in $A$ (`smF_mem`, `coefQ_cmul_mem`).

Part 2. Take $c_c$ from `GlobalTheory.T.siegelUnit_edgeClass_kummer_dlog_congruence`. That lemma takes two Siegel units for $c$ and $d$ at $(A_1, a_2)$ and $(B_1, b_2)$, with $a_2 \equiv N' g'$ and $b_2 \equiv N' h'$ mod $\ell^L$, their $\ell^n$-th roots, the two Kummer characters and a cochain $\eta$ whose coboundary is their cup product (`CobOn`). It gives $\xi$ and the congruence
$$\ell^{c_c}\varphi_r \equiv s^{-1}(\xi_r) - \xi_r - \ell^{c_c}(A_1 h' - g' B_1)\, t\, E'_r,$$
where $E'_r$ is the coefficient of the product of the smoothed weight one series at these parameters, for each $s$ that preserves $A$ and fixes the base field. The proof applies it with $N' = N^3$, $L = m + n$, to the embedding $\begin{pmatrix} N^2 & 0 \\ 0 & 1 \end{pmatrix} \circ g$ of the field of level $M$, with the roots and cochain from `units` and `topex`. The rescaling by $N^2$ turns period $M$ into period $\ell^{m+n}$ (`GlobalTheory.T.isLogDerivQExpansionModPrimePow_rescale`), and `resc` turns $E'_r$ into $E_r(g)$. The lemma is used with $s^{-1}$ and $-t$. Last, $\det g = 1$ gives $A_1 h' - g' B_1 = N^3 + \ell^{m+n} Q$ for an integer $Q$. The rest is bookkeeping.

## In the Lean code

The theorem is in [CoefQCmulMem.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/CoefQCmulMem.lean#L155), with `set_option maxHeartbeats 2000000`. The vacuous branch $\ell = 2$ is at line 162. The edge lemma is stated in [SiegelUnitEdgeClassKummerDlogCongruenceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SiegelUnitEdgeClassKummerDlogCongruenceStatement.lean#L8) and proved as `GlobalTheory.pair_edge_dlog`, which we have not unfolded. The names `one` and `CoefQCmulMem` say little.
