---
id: mc-theorem-mv7
title: The averaged bad-count bound on a progression grid
kind: theorem
decl: Formalism.InvariantFactorPaths.MC.theoremMV7
module: Formalism.ThetaLogCoordinates.PartnerMeanCoordinates.PartnerMeanProofs.GramHypothesisOfLogBound
covers: 1678
status: drafted
drafted_by: writer@claude
---
This theorem bounds the mean bad count of integral polynomial lattices over a grid of tie degrees. Through [`Top.theoremMV7`](/entry/top-theorem-mv7/) and [`alternative_mean_value_theorem`](/entry/alternative-mean-value-theorem/) it gives the fibre bounds of [`restTM_exists`](/entry/rest-tm-exists/).

## Statement

Letters $L$ give each row $j < N$ a sign $v_j \in \{\pm\}$ and a degree $\deg_j$. $P(L)$ is the polynomials over $\mathbb{Q}_p$ in $x_{j,c}$ ($c < r$) of degree $\deg_j$ in row $j$. Tie data $T$ give positions $\mathrm{pos}_1 < \dots < \mathrm{pos}_t$, shifts $z_i$ and thresholds $(J_k, M_k)$. $Y(L) \subseteq P(L)$ (`Y`) is the meet over $k$ of the largest $\mathfrak{gl}_r$-stable subspaces (signed action on rows $< J_k$) with colour-$0$ weight at most $M_k$; $Y_{\mathbb{Z}}$ (`YZ`) is its integral lattice.

The Fock pairing is $\langle F, G \rangle = \sum_m F_m G_m\, m! / \prod_j \deg_j!$ (`fockN`). Put $\beta(F, G) = \langle \phi_1 \cdots \phi_t F, G \rangle$ (`phis`), where $\phi_i = \sum_j c_j E^j F^j$ (`tiePhi`), $E$ multiplies by $\sum_c x_{\mathrm{pos}_i, c}\, x_{\mathrm{pos}_i+1, c}$ and $F = \sum_c \partial_{\mathrm{pos}_i, c}\, \partial_{\mathrm{pos}_i+1, c}$. $\mathrm{bad}(\Lambda, D)$ is $\operatorname{rk}\Lambda$ minus the largest $n$ with $x_1, \dots, x_n, y_1, \dots, y_n \in \Lambda$ and $\beta(x_i, y_j) = p^D \delta_{ij}$.

For $n \in \mathbb{N}^t$, $L_n$ is $L$ with $\deg_{\mathrm{pos}_i + 1} = n_i$ (`setTies`). The grid is $G = \prod_i \{n_{0,i} + d_i j : 0 \le j < Y_i\}$ with top $n^{\mathrm{top}}_i = n_{0,i} + d_i(Y_i - 1)$, and $S_i$ is the degree of $L_{n^{\mathrm{top}}}$ in rows $\le \mathrm{pos}_i$. Put

$$ \lambda = \log_p(8a + r) + 1, \quad \kappa = 3(s+2) r^2 \lambda, \quad \varepsilon_i = \frac{2S_i}{Y_i} + \frac{1}{E}\Bigl(2\kappa + \frac{2 S_i \lambda}{Y_i}\Bigr). $$

**Theorem.** Let $p \ne 2$ be prime, $r \ge 2$, $\rho = r - 1$, $L$ letters of length $2s+1$ and $T$ tie data. Assume: $T$ is admissible ($\mathrm{pos}_i$ has sign $+$, $\mathrm{pos}_i + 1$ sign $-$ and is some $J_k$); signs alternate, $+$ on even rows; each $J_k$ is $2s+1$ or some $\mathrm{pos}_i + 1$; $a \ge 1$, $E \ge 1$; $Y_i \ge 1$, $d_i > 0$ and $\gcd(d_i, p) = 1$; $S_i \le n_{0,i}$; and the total degree of $L_{n^{\mathrm{top}}}$, $Y_i$, $2S_i + 1$ and $\deg_{\mathrm{pos}_i} + \deg_{\mathrm{pos}_i + 1} + r + z_i + 1$ are at most $8a + r$. Then

$$ \frac{1}{|G|} \sum_{n \in G} \mathrm{bad}\bigl(Y_{\mathbb{Z}}(L_n),\ \lfloor t(E + \kappa) + \kappa \rfloor\bigr) \le \sum_{i=1}^{t} \varepsilon_i\, \frac{1}{|G|} \sum_{n \in G} \dim Y\bigl(L_{n[i \mapsto n^{\mathrm{top}}_i]}\bigr). $$

## Proof

The proof applies `theoremMV7Of`, which adds one hypothesis: at each $n \in G$, $L_n$ satisfies `HypP` and `HypW` with $e_1 = \lfloor r^2\lambda \rfloor$ ($p^{e_1}$ clears denominators of certain projectors and Weyl lattices; `IsTypeProj` and `WeylLat` not unfolded), and its truncation to rows $\le \mathrm{pos}_i$ satisfies the Gram hypothesis $|\det(\langle g_a, g_b\rangle)|_p \ge p^{-\kappa_4 k}$, $\kappa_4 = (s+4) r^2 \lambda$, for each basis $g_1, \dots, g_k$ of a graded lattice `grLat`.

1. **`HypP`, `HypW`.** `PW.Top.dischargeP` and `PW.Top.dischargeW` give both when $\binom{r}{2}\lfloor \log_p(d + r - 1) \rfloor \le e_1$ (`kapC`), $d$ the total degree. Since $d \le 8a + r$, `natLog_le_lgSeg` and `choose_two_le` give this.
2. **Gram.** `gram_hypothesis_of_log_bound` proves it from two such log bounds and $(\mathrm{pos}_i + 7)\, r^2\lambda/2 \le \kappa_4$, through `graded_bound_saturation_holds` or `graded_bound_pos_of_proj` (not opened).
3. **`theoremMV7Of`** applies `theoremMXB` with $X_b = \lfloor 8a + r \rfloor$, $\kappa$, $\kappa_4$, $\lambda$, $e_1$ and checks conditions such as $3\lambda + \kappa_4 \le \kappa$.

The content is in `theoremMXB`, which is `theoremMXB_of_point` applied to `meanGamX`, a Smith form over $\mathbb{Z}_p$, adapted bases and a pointwise bound, among others. The rest is bookkeeping.

## In the Lean code

The theorem is in [GramHypothesisOfLogBound.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GramHypothesisOfLogBound.lean#L188). The same file has `theoremMV7Of` (line 124), `gram_hypothesis_of_log_bound` (line 83) and `theoremMXB` (line 17).

- `TheoremMV7` and `TheoremMV7Of` in [ChainOrderLetters.lean](lean:Formalism/PolynomialDimension/ChainOrderLetters.lean#L19); `TheoremMXB` in [TheoremMXB.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/TheoremMXB.lean#L118).
- `Letters`, `Y`, `YZ`, `fockN`, `bad` in [GoodCount.lean](lean:Formalism/MahlerMeasure/GoodCount.lean#L7); `setTies`, `phis` in [StatementTM.lean](lean:Formalism/MahlerMeasure/StatementTM.lean#L13); `HypP`, `HypW`, Gram in [StatementT.lean](lean:Formalism/MahlerMeasure/StatementT.lean#L7).

Two hypotheses are never used: the alternating signs (`ChainOrderLetters`) and the threshold shape (`ConditionShape`). `theoremMV7Of` introduces them as `hch` and `hcond` and drops them; `TheoremMXB` has neither.
