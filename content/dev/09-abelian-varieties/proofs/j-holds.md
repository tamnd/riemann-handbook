---
id: j-holds
title: A normalized theta section with a large derivative at zero
kind: theorem
decl: GlobalTheory.ThetaTorus.J_holds
module: Development.AbelianVarietyTheory.Proofs.TorusSplitting.GCauchyHolds
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem gives one theta section of norm $1$ on $V^n$ whose derivative at $0$, along a product of powers of minors, is at least an explicit constant. It is the analytic input of [the lower bound for translates](/entry/i-holds/), which turns it into a bound for a sum over a basis.

## Statement

We use the notation of the [entry for `I_holds`](/entry/i-holds/): the datum $X$ (`PT E`), the spaces $\mathrm{Sec}(q, n)$, the norm $\|F\|_q^2$ (`l2`), the operator $D$ of the polynomial $P_1$ of the blocks `bs`, and the constant $J(n)$ (`Par.Jbound`). A block is an embedding $\tau$, a size $i \leq \dim_\tau$, a power $c \geq 1$ and $i$ distinct columns in $\{0, \dots, n-1\}$. Its polynomial is the $c$-th power of an $i \times i$ minor in the coordinates of type $\tau$. `Disj bs` says that two blocks use no common column.

**Theorem (`JStatement`).** Let $E$ be a CM field, $X$ a datum, `bs` a disjoint family of blocks, and $P$ parameters for $\sum_j i_j c_j$. Then there is $F \in \mathrm{Sec}(q, n)$ with $\|F\|_q^2 = 1$ and $J(n) \leq |DF(0)|^2$.

## Proof

`J_holds` applies `jOf` to six inputs: the bundle `ext_all_inputs` of nine facts (`Ext.All`), `T.greedy_splitting_principal_torus_exists` (`SplitStatement`), `charStatement_holds` (`CharStatement`), and `colTorus`, `colAbel`, `colEmpty`, each built from `ext_all_inputs`, `propA_holds` and `gSup_holds`. `jOf` calls `jof_core`, which runs as follows.

1. **Split.** `SplitStatement` gives a sublattice $I \subseteq L$ (`IsSplit`): saturated, $\mathcal{O}_E$-stable, isotropic for $\operatorname{Im} H$, with $\varepsilon = 1$ on $I$, of bounded rank, and with gap and size conditions on the vectors $u$ attached to lattice points.
2. **Block columns.** `block_data_all` uses `CharStatement`, `ColTorusStatement` and `ColAbelStatement`. For each column $b$ of each block it gives $y_b$ with $|y_b| \leq 2$, a section $s_b \in \mathrm{Sec}(q, 1)$ and $\mu_b \neq 0$. The $c$-th derivative of $s_b$ is close to $\mu_b \prod_k H(x_k, y_b)$, and $\|s_b\|_q^2$ is bounded by $|\mu_b|^2$ times a constant. Each block minor of the $y_b$ has absolute value at least $2^{-r/2}/2$.
3. **Free columns.** `ColEmptyStatement` gives $s_e \in \mathrm{Sec}(q, 1)$ with $|s_e(0)| \geq \tfrac12$ and a bound on its norm.
4. **Tensor.** Put $s_b$ on the columns of the blocks and $s_e$ on the other columns. The tensor product $F_0$ lies in $\mathrm{Sec}(q, n)$, and $\|F_0\|_q^2$ is the product of the factor norms (`l2_tens_eq_prod`).
5. **Expand.** `polyDeriv_determinantPoly_tensor` writes $DF_0(0)$ as a signed sum over choices $T$ of products of one-variable derivatives. `norm_sum_prod_sub_le` compares it with the ideal sum. The error is small by `P.C6` and `num_bound`. So $|DF_0(0)| \geq \tfrac12 C_e M_\mu D_t$, where $C_e$, $M_\mu$, $D_t$ are the products of $|s_e(0)|$, $|\mu_b|$ and the minors.
6. **Normalize.** The bounds of steps 2 and 3 give $J(n)\|F_0\|_q^2 \leq |DF_0(0)|^2$. Then $F = F_0 / \|F_0\|_q$ works.

## In the Lean code

The theorem is at [GCauchyHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/TorusSplitting/GCauchyHolds.lean#L26). `JStatement` is at [GCauchyStatement.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/GCauchyStatement.lean#L197), and `jof_core` is at [HfNormLeTwo.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/HfNormLeTwo.lean#L39). The splitting and column statements are in SplitSt.lean. We have not unfolded the proofs of these five statements or of `Ext.All`. The name `T.greedy_splitting_principal_torus_exists` is a second name of `greedy_splitting_exists`. The file is named GCauchyHolds, but it holds no theorem called `GCauchy`.
