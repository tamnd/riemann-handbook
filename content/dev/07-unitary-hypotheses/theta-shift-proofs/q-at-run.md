---
id: q-at-run
title: The quotient index bound at a run
kind: theorem
decl: GlobalTheory.RunJoin.qAt_run
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.RecursivePageLatticeBound
covers: 837
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `QAt` at each run of the record, with explicit constants. Its statement form [`recursive_page_lattice_bound`](/entry/recursive-page-lattice-bound/) gives `QAt` to [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/). The work is in [`qat_of_kill_detect`](/entry/qat-of-kill-detect/).

## Statement

Let $B$ be the provider `recB h.toLawsCore` of the record. It gives a number field $K$ of degree $d_K$, for each weight $\kappa$ a finite-dimensional $K$-space $S_\kappa$ of cusp forms with an $\mathcal{O}_K$-submodule $M_\kappa$, and a sup norm $\|F\|_\sigma$ for each embedding $\sigma \colon K \to \mathbb{C}$. Let $h(F) = d_K^{-1} \sum_\sigma \log \|F\|_\sigma$ and $\ell(\lambda) = \log N\lambda$. Let $|\kappa| \ge 1$ be the size of $\kappa$ (`Wt.size`), and let $P(C, A) = C z^A$, where $z$ is `zBase L`.

For parameters $C_R, T, c$, let $\mathcal{K} \subseteq S_\kappa$ (`MggK`) be the intersection of the kernels of the maps `sg` at all index pairs that are `Killed`. Let $Q = M_\kappa / (M_\kappa \cap \mathcal{K})$ and let $\rho$ be its rank.

*The bound* `QAt` $(C_R, C_k, C_h, A_h, C_c, A_c, T, c)$. Suppose $C_R \ge 0$, `Obound` ($\log d_K$ and the log root discriminant of $K$ are at most $P(C_h, A_h)$), $\kappa$ has $n = n_V$ and `LastPos`, $|\kappa| \le C_k k f b$, $T > 0$, $c > 0$ and $Tc \le 1$. Then there is a finitely supported $\beta \ge 0$ on the primes of $\mathcal{O}_K$ with $d_K^{-1} \sum_\lambda \beta(\lambda) \ell(\lambda) \le P(C_c, A_c) |\kappa|$, such that: for all $\theta_1, \dots, \theta_\rho \in M_\kappa$ with $K\theta_1 + \dots + K\theta_\rho + \mathcal{K} = S_\kappa$ and $h(\theta_i) \le P(C_h, A_h)|\kappa|$, there is a finitely supported $\nu$ with

$$\operatorname{length}_{\mathcal{O}_{K,\lambda}} \bigl(Q / \langle \bar\theta_1, \dots, \bar\theta_\rho \rangle\bigr)_\lambda \le \nu(\lambda) + \rho\,\beta(\lambda) \text{ for all } \lambda, \qquad \frac{1}{d_K} \sum_\lambda \nu(\lambda)\ell(\lambda) \le \rho\, P(C_c, A_c) |\kappa|.$$

So small forms that span modulo $\mathcal{K}$ span a submodule of $Q$ of bounded index.

**Theorem.** There is $C_q \colon \mathbb{R}^2 \to \mathbb{R}$ such that, if `PageOK` holds for $X_j$, $j \in [1, m)$ and $M_\kappa$ is a lattice in $S_\kappa$, then `QAt` holds with $C_R = 7$, $C_k = H.C_K$, $C_h = 1$, $A_h = 4$, $C_c = C_q(H.C_A, H.C_K)$, $A_c = 4$, $T = T_n$ and $c = $ `cc D L C2 A2 7 wL`.

## Proof

Put $C_q(a, b) = 1 + 3 C_0(a, 7, b) + 1041$, where $C_0 \ge 0$ comes from step 1.

1. `exists_polynomial_bound_runConstants_degree_four` gives $C_0$. From the hypotheses of `QAt`, `ParA` and $\log N\mathfrak{c} \le L$ (both in `PageOK`), and $r \ge 3$ (from $r \ge 8$ in `PageOK`), it gives $z \ge 1$ and `RoomAt` with constant $C_0(H.C_A, 7, H.C_K)$ and exponent $4$.
2. `thetaNet_dimension_and_pointCount_bound` gives $\log \dim_K S_\kappa \le 1041 z^3 \le P(1041, 3)|\kappa|$.
3. `gamAt_of_lawsCore` gives `GamAt`. `arithmeticCMKnownTheorems_proof` gives `Known`. Then `killQ_of_gamAt` gives `KillQ`, and [`cmFamilyFunctionals_detect_lowCoefficients`](/entry/cm-family-functionals-detect-low-coefficients/) gives `DetectQ`.
4. [`quotientBound_of_kill_detect_constantRoom`](/entry/quotient-bound-of-kill-detect-constant-room/), with $C_h = 1$, $A_h = 4$, $A_0 = 4$, $C_d = 1041$, $A_d = 3$, gives `QAt` with $C_c = 1 + 3C_0 + 1041$ and $A_c = \max(4, 4, 3) = 4$.

## In the Lean code

The theorem is in [RecursivePageLatticeBound.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/RecursivePageLatticeBound.lean#L35). `QAt` and `LatAt` are in [WeightedPrimeSumBound.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/WeightedPrimeSumBound.lean#L38), `MggK` and $\rho$ (`rhoP`) in [WeightFamilies.lean](lean:Formalism/SharpRestriction/Divisibility/WeightFamilies.lean#L325). We have not unfolded `recB`, `sg`, `Killed`, `ParA` or the parameter `cc`.

- `QAt` is a chain of implications. Its eight hypotheses are introduced at line 38. Steps 1 and 3 use some; step 4 gets all.
- `Known` is a structure of fourteen fields; here it is proved outright by `arithmeticCMKnownTheorems_proof`, so it is not a hypothesis of this theorem.
