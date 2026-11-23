---
id: pow-k-ne-zero-of
title: The top power of the de Rham first Chern class is not zero, from three local inputs
kind: theorem
decl: CrystallineSemistableComparison.Pb.powK_ne_zero_of
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.ConeSectionRestriction.PowKNeZeroOf
covers: 357
status: drafted
drafted_by: writer@claude
---
This theorem has the real argument for [the nonvanishing of $c^d$](/entry/pow-k-ne-zero-main/). It takes three hypotheses, a geometric setup, a local exactness and an algebraic residue statement, and proves from them that $c^d \neq 0$. If $c^d = 0$, the argument writes the unit $(t_0 \cdots t_n)^{-1}$ in a form that the residue statement forbids. Below it are 357 declarations.

## Statement

The hypotheses `GeoSetupP`, `LocExactP` and `ResidAlgP` are described in [the parent entry](/entry/pow-k-ne-zero-main/). Assume all three. Let $K$, $X$, $q$, $d$, $D$ and $c$ be as in [`powK_ne_zero`](/entry/pow-k-ne-zero/): $X$ connected and smooth of relative dimension $d$ over $K$ of characteristic $0$, $D$ a tautological line for a closed immersion $X \to \mathbb{P}^N_K$, and $c \in$ `HdR q 2` a first Chern class of $D$. Then $c^d \neq 0$.

## Proof

If $d = 0$, then $c^0$ is the unit class, and `oneK_ne_zero` shows that it is not zero because $X$ is not empty.

Let $d = n + 1$ and assume $c^{n+1} = 0$.

1. `GeoSetupP` applied to the closed immersion gives $y_0, \dots, y_{n+1}$, the charts $U_k$, the open $V$, the coordinates $t_0, \dots, t_n$ and the rings $B(S)$. Take derivations $D_k$ dual to the $t_j$, and a lift $\Lambda$ of $D$ over the thickenings with $J^{[n+2]} = 0$.
2. `IsFirstChernDeRham` with $s = n + 2$ gives a Čech $2$-cocycle $z$ for $c$ on the pieces $W_k$ over $U_k$. By `powK_pull`, the class of $z^{n+1}$ is $0$.
3. `LocExactP` gives $1$-cochains $b_k$ with $d b_k = e z$ on $W_k$, in the first filtration step. Put $\ell_k = b_k - b_{k+1}$ on the full intersection. Each $\ell_k$ is a cocycle, and it is the truncated $d\log$ of a lift of the ratio of $y_k$ and $y_{k+1}$.
4. On the affine intersections, the cohomology of $\mathrm{gr}^r$ in degree $j$ vanishes if $j \neq r$ or $r > n + 1$ (`gr_aff`, `gr_neg_van`, `gr_top_van`).
5. `rep_cupList` gives a class $c_0$ of $\ell_0 \cup \dots \cup \ell_n$ in $\mathrm{gr}^{n+1}$, degree $n+1$. With the vanishing and $e^{n+1} z^{n+1} \sim 0$, `cech_top_rel` gives Čech data $\omega, f$ that bound $c_0$.
6. `cone_transfer` moves this relation into $\Gamma(V)$. With `dlog_ratios` for the ratios $t_0^{-1}$ and $t_{k-1}/t_k$, and a case split on signs, it gives
$$(t_0 \cdots t_n)^{-1} = \sum_j x_j + \sum_k (-1)^k D_k(\eta_k),$$
with $x_j \in \mathrm{jacS}(B(\text{all} \setminus j))$ and $\eta_k \in \mathrm{jacS}(B(\text{all}))$ for the derivations other than $D_k$.
7. `ResidAlgP` says that no such identity exists. This is the contradiction.

Here $\mathrm{jacS}(B)$ is the additive span of the products $b \cdot \det(D_{\kappa(k)} b_l)$ with all $b, b_l \in B$.

Our reading, which the Lean code does not state: the left side is the form $d\log t_0 \wedge \dots \wedge d\log t_n$, and the right side is a sum of forms that are regular on the intersection of all charts but one, plus exact forms. The proof of `resid_alg` separates them by a trace down to $K(t)$ and a residue.

## In the Lean code

The theorem is in [PowKNeZeroOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/PowKNeZeroOf.lean#L76), under `maxHeartbeats 800000`. The hypotheses are defined in [ConeHyp.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/ConeHyp.lean#L19). `jacS` and `torusS` are in [SeamDefs.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/SeamDefs.lean#L19). The ratios are `g_rel` at line 46 of PowKNeZeroOf.lean. We have not unfolded `cech_top_rel` and `cone_transfer`.
