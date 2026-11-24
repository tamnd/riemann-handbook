---
title: Cell weights, Fock vectors and the row chain
decls:
  - GlobalTheory.RowChain.iter_chain
  - GlobalTheory.RowChain.iter_colPer
  - GlobalTheory.RowChain.pure_core
  - GlobalTheory.FlipRun.flipAt_of
  - GlobalTheory.T.cell_masses_against_level_volumes_large_depth
  - GlobalTheory.RowWt.wtAt_big
  - GlobalTheory.T.unfolding_cell_mass_eq_const_mul_local_coefficients
  - GlobalTheory.CellMass.cell_mass
  - GlobalTheory.T.lastRowLatticesGoodPosition_large_depth
  - GlobalTheory.RowShape.shapeAt_big
  - GlobalTheory.T.periodReductionToFockVectors_large_depth
  - GlobalTheory.FockRed.fockAt_big
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cell weights, Fock vectors and the row chain

This section collects the last inputs of the unfolding. It has three parts. The first part shows that the theta integral along the row chain of a grid is an iterated integral of column periods. This is used in [the eventual largeness of the twisted iterate](/entry/twisted-iterate-eventually-large/). The second part flips the given path of a grid to the opposite path one square at a time. This is used in [the sign flip step](/entry/twist-sign-flip-succ/). The third part computes the cell weights of the unfolded terms, puts the last row lattices in good position, and reduces the periods to Fock vectors. These three facts are used in [the unfolding of the twisted theta integral](/entry/twisted-theta-integral-unfolding/).

### The row chain

Fix a grid of size $m$, a Weil family $W$, a type $t$ and a volume $M$ of type $t$. The down path from the vertex $V_{m,m}$ to the vertex $V_{m,0}$ goes through a chain of [seesaw pairs](/learn/theta/#seesaw-pairs). Each step of the chain has a Jacobi group $J$ and a Bessel group $B'$. A pure datum $d$ on the down path gives chain data. For a form $F$ on $V_{m,m}$ and a form $\varphi$ on the top node $X_0$, the chain gives a function $Q(d, F, \varphi)$ on the variables of the chain, and the down lift $\mathrm{down}(d, F)$, which is a form on $V_{m,0}$.

**Definition 8.12.1 (Iterated value).** Let $c$ be a chain, $q$ a function on its variables and $z \in \mathbb{C}$. If $c$ has one node, then $c$ *iterates* $q$ to $z$ if $z = q()$. If $c$ starts with a step $(J, B')$ and continues with $c'$, then $c$ iterates $q$ to $z$ if there are functions $f_1$ on $J(\mathbb{A})$ and $f_2$ on $J(\mathbb{A}) \times B'(\mathbb{A})$ such that:

1. $z$ is the absolutely convergent quotient integral of $f_1$ over $J(\mathbb{A})$;
2. for each $h_1$, $f_1(h_1)$ is the absolutely convergent quotient integral of $f_2(h_1, \cdot)$ over $B'(\mathbb{A})$;
3. for each $h_1$ and $h_2$, $c'$ iterates $h \mapsto q(h_1, h_2, h)$ to $f_2(h_1, h_2)$.

The quotient integrals use the [Haar measures](/learn/analysis/#haar-measure) of the chain.

The chain is *rapid* at $(d, F)$ if the partial integrands of the chain decay rapidly. The *column period* $\mathrm{colPer}(d, F, \varphi)$ is the function on the variables that pairs $F$ against $\varphi$ along the columns, step by step.

**Theorem 8.12.2 (The row chain unfolds).** Let $d$ be a pure datum on the down path whose entries are all theta data. Let $F$ be a continuous automorphic form on $V_{m,m}$ and $\varphi$ a continuous automorphic form on $X_0$. If the chain is rapid at $(d, F)$, then the chain iterates $Q(d, F, \varphi)$ to the top period of $\varphi$ against $\mathrm{down}(d, F)$.

Lean: `GlobalTheory.RowChain.iter_chain`.

*Proof.* This is one clause of the general unfolding of a chain of seesaw pairs, applied to the chain data of $d$ at the point $1$. The chain data are theta data because the entries of $d$ are. The translate of $\mathrm{down}(d, F)$ by $1$ is $\mathrm{down}(d, F)$. $\square$

**Theorem 8.12.3 (Column periods along the row chain).** Under the same hypotheses, the chain iterates $\mathrm{colPer}(d, F, \varphi)$ to the top period of $\varphi$ against $\mathrm{down}(d, F)$.

Lean: `GlobalTheory.RowChain.iter_colPer`.

*Proof.* We show that $Q = \mathrm{colPer}$ as functions. Take a subchain that starts at column $j$ and has $\sigma$ steps, with $j + 2\sigma + 2 = m$. We use induction on $\sigma$. For $\sigma = 0$ the identity is the last seesaw step. For the inductive step, the first step of the subchain is a flat step from Bessel to Jacobi data, followed by a flat step from Jacobi to Bessel data. The composite of the two steps moves $Q$ to the column period of the subchain that starts at $j + 2$. The case $j = 0$ gives $Q = \mathrm{colPer}$. Then the previous theorem gives the claim. $\square$

Let $e$ be an idempotent sum for the local places, and let $\rho$ be a real match for $W$. A pair $(\varphi, d)$ of row and down Schwartz data is *local* if each entry of $d$ is a local vector for $e$ and $\rho$ at the place of $\varphi$. Let $\mathrm{rowLift}(P, d, F)$ be the lift of $F$ along the row with polynomials $P$, and let $\mathrm{liftP}$ be the lift along the opposite path with the opposite pure datum.

**Theorem 8.12.4 (The pure core).** Assume that cusp forms of unitary groups decay rapidly in Siegel sets. Let $M_0$ be a row volume, let $M$ be a volume of type $t$, and assume that each step of the path is a cuspidal step for $M$. Let $(\varphi, d)$ be local, let $P$ be a pair of polynomial data, let $F$ be a cusp form on $V_{0,m}$ in the listed spectrum, and let $u$ be a continuous automorphic form on $X_0$. Then:

1. $\mathrm{rowLift}(P_1, d_1, F)$ is a cusp form on $V_{m,m}$ in the listed spectrum;
2. $\mathrm{liftP}(P, d, F)$ is a cusp form on $V_{m,0}$ in the listed spectrum;
3. the chain iterates the opposite period of $(P, d, u, F)$ to $B^{+}_{M_0}(u, \mathrm{liftP}(P, d, F))$.

Lean: `GlobalTheory.RowChain.pure_core`.

*Proof.* Clause 1 is the row case of the cuspidal step hypothesis, applied to the row family of $P_1$ and the local vectors $d_1$. For clause 2, the down datum is the Fock zip of $d_2$ and $P_2$, and its entries are local vectors. The chain properties then give that the down lift of the row lift is a cusp form, and that the chain is rapid. The down lift of the row lift is $\mathrm{liftP}(P, d, F)$. For clause 3, the value $B^{+}_{M_0}$ does not depend on the row volume, and it equals the top period of $u$ against the down lift. The previous theorem then gives the claim, with the rapid decay from the chain properties. $\square$

### Flipping the given path

The *flip order* of a grid of size $m$ is the list of the $m^2$ squares $(i, j)$ with $i, j < m$, in lexicographic order. Flipping the squares in this order moves the given path from $V_{0,m}$ to $V_{m,0}$ to the opposite path. Each flip of a square $(i, j)$ for type $t$ changes the lift by a constant $c_{i,j}(t)$. Put

$$c_{\mathrm{tot}}(t) = \prod_{i < m} \prod_{j < m} c_{i,j}(t).$$

**Theorem 8.12.5 (Flip from Weil convergence and theta).** Let $\mathrm{ch}$ be a choice whose level characters have the level type $\mu_0$. Assume these conditions.

1. For each type $t$ and square $(i, j)$, the Weil actions commute on the square with the constant $c_{i,j}(t)$, and $c_{i,j}(t) \ne 0$.
2. For each $t$ and each volume $M$ of type $t$, each step is a cuspidal step for $M$.
3. For each $t$ and $y$, the top form $F_{t,y}$ is a cusp form on $V_{0,m}$ in the listed spectrum.
4. There is a polynomial datum $P_g$ such that for each $t$ there is $z_t \in \Xi_t$ with this property. For each datum $\Phi$ there is a finite tensor $\tau_g$ that represents the given local stages along the given path, and for each $M$ of type $t$ and each $y$, the lift of $F_{t,y}$ along the given path converges, and $\theta_\chi(\Phi)$ at the lift of $y$ is $z_t^{-1}$ times that lift.
5. At each local place, the local stage stays a tensor after each initial part of the flip order.

Then there are a polynomial datum $\tau_i$ on the opposite path and units $z_t \in \Xi_t$ such that for each $t$ and $\Phi$ there is a flip finite tensor $\tau$ with this property. For each $M$ of type $t$ and each $y$, the lift of $F_{t,y}$ along the opposite path with $(\tau_i, \tau)$ converges, and

$$\theta_\chi(\Phi)(y) = \bigl(z_t\, c_{\mathrm{tot}}(t)\bigr)^{-1} \mathrm{lift}_{\mathrm{opp}}(F_{t,y}).$$

Lean: `GlobalTheory.FlipRun.flipAt_of`.

*Proof.* Put $\tau_i$ equal to the flips of $P_g$ along the whole flip order, moved to the opposite path. We show by induction on $k \le m^2$ that after the first $k$ flips there are a path $p$ on the grid, with the edges of the flipped path, and a finite tensor that represents the local stages along $p$, with the identity for $\theta_\chi(\Phi)$ and the product of the first $k$ constants. For $k = 0$ the path is the given path, and condition 4 gives the identity. For the step from $k$ to $k + 1$, let $(i, j)$ be the next square. The flipped path passes through $(i, j)$, so we can cut $p$ at the square and swap the route. The local stages are tensors before and after the flip, by condition 5. The flip of one square then changes the lift by $c_{i,j}(t)^{-1}$, by conditions 1, 2 and 3. For $k = m^2$ the edges are those of the opposite path, and a path on the grid is determined by its edges. So $p$ is the opposite path. The product of all constants is $c_{\mathrm{tot}}(t)$. $\square$

### Cell weights

Let $B$ be a group with a Haar measure $\mu$, $R$ a subgroup with a Haar measure $\rho$, and $K$ a compact open subgroup of $B$. For $b \in B$ the *cell weight* is

$$\mathrm{cellWt}(\rho, \mu, K, b) = \frac{\mu(K)}{\rho\{r \in R : b^{-1} r b \in K\}}.$$

Let $\mathrm{idx} = \{1, \dots, m - 2\}$. For a family $b$ of finite points of the row groups, $\mathrm{wt}(\rho, \mu, b)$ is the product over $j \in \mathrm{idx}$ of the cell weights of $b_j$, with the level groups of the grid. A family $b$ *represents* a coset family $\beta$ for a sign $s$ if $b$ gives the staircase coset $\beta$ in the expansion of sign $s$.

**Theorem 8.12.6 (Cell mass).** For all large choices, each sign $s$ and Haar measures $\rho_j$ and $\mu_j$ for $j \in \mathrm{idx}$, this holds for each $j \in \mathrm{idx}$. There is $c \in \mathbb{C}$ such that for all $t, \Phi, \beta$ and $b$ that represents $\beta$, all volumes $M$ of type $t$ and $M'$ of the term at $\beta$, and all $x \ge 0$ with $M_{X_j} = x M'_{X_j}$,

$$\mathrm{cellWt}(b_j)\, x = c\, \mathrm{colCoef}(t, \beta, j).$$

Lean: `GlobalTheory.T.unfolding_cell_mass_eq_const_mul_local_coefficients` (also `GlobalTheory.CellMass.cell_mass`, the proof).

*Proof.* The row period at the conjugate level is a Fubini integral over the finite points. The projection to the double cosets scales the volume by a constant. A conjugate of a lattice has a Haar volume. Together these give $c = \mu(K) / (\kappa \kappa' V_0)$, where $\kappa$ and $\kappa'$ are the two projection constants and $V_0$ is the volume of the base lattice. $\square$

**Theorem 8.12.7 (Cell masses against level volumes).** For all large choices, each sign $s$ and Haar measures $\rho_j$ and $\mu_j$ for $j \in \mathrm{idx}$, there is $c \in \mathbb{C}$ with this property. For all $t, \Phi, \beta$ and $b$ that represents $\beta$, all volumes $M$ of type $t$ and $M'$ of the term at $\beta$, there is $x$ such that $M$ scales to $M'$ by $x$ and

$$\mathrm{wt}(\rho, \mu, b)\, \mathrm{sProd}(x) = c \prod_w \mathrm{coef}(\mathrm{term}_w).$$

Lean: `GlobalTheory.T.cell_masses_against_level_volumes_large_depth` (also `GlobalTheory.RowWt.wtAt_big`, the proof).

*Proof.* The measures of the tuple terms differ by scalars, so there is $x$ with $M$ scaling to $M'$ by $x$. Take $c_j$ from the cell mass theorem for each $j \in \mathrm{idx}$ and put $c = \prod_j c_j$. Multiply the identities for $j \in \mathrm{idx}$. The product of the column coefficients is the product of the local coefficients of the term. $\square$

### Lattices and Fock vectors

**Theorem 8.12.8 (The last row lattices are in good position).** For all large choices there are [hermitian lattices](/learn/groups/#hermitian-lattices-and-the-mass-formula) $N$, $N_0$, $L$ and $L_Z$ with these properties.

1. The base points move the row lattices to $N$.
2. $L_Z$ is self dual, and it splits orthogonally at the top.
3. The Bessel data at $j$ and the Jacobi data at $j + 1$ are in good position, and the Jacobi data at $j$ are adapted to the Bessel data at $j + 1$.
4. If the depth $\sigma$ is $0$, the last step is in good position.
5. The characters are unramified at the places that are not local.

Lean: `GlobalTheory.T.lastRowLatticesGoodPosition_large_depth` (also `GlobalTheory.RowShape.shapeAt_big`, the proof).

*Proof.* Take $N$ to be the row lattice of the grid, $N_0$ the core lattice, $L$ the line lattice and $L_Z$ the top lattice. For all large choices, each of the facts holds by the construction of the frames at large depth. $\square$

A family $C$ of vectors is *real* if its entries are Fock vectors at the real places. For a family $c$ of combinations, $\mathrm{combC}(c, C)$ and $\mathrm{combR}(c)$ are the column and row combinations. A family $c$ is a *combination* of an expansion $\tau$ if each $d$ in the support of $\tau$ has a combination $c_d$.

**Theorem 8.12.9 (Period reduction to Fock vectors).** For all large choices there are units $z_t \in \Xi_t$ with this property. For each real family $C$ and each row polynomial $P$ there is $\sigma$ such that for all $t, a, \beta$, each Haar volume $M$, each sum condition at $(t, \Phi_a)$, each expansion $\tau$ at $\beta$ with combinations $c$, and each $y$,

$$\begin{aligned}
&\sum_d \tau_d\, \mathcal{P}_M\bigl(\mathrm{combC}(c_d, C), \mathrm{combR}(c_d), P\bigr) \\
&\quad = z_t^{-1}\, \mathrm{defTot}_M(\sigma, \tau).
\end{aligned}$$

Lean: `GlobalTheory.T.periodReductionToFockVectors_large_depth` (also `GlobalTheory.FockRed.fockAt_big`, the proof).

*Proof.* For all large choices the basic hypotheses of the last row unfolding hold, the moved vectors are combinations of vacua, the column real data have Fock combinations, and the row lift is continuous. The moved vectors are $\kappa_j z_{t,j} \mathrm{comb}(v_j)$ on the columns and $\kappa'_i \mathrm{combR}$ on the rows. Put $z_t = \prod_j z_{t,j}$ and

$$\sigma = \Bigl(\prod_j \kappa_j\Bigr)^{-1} \Bigl(\prod_i \kappa'_i\Bigr)^{-1} \sigma_c,$$

where $\sigma_c$ is the column Fock combination. The period is linear in the vectors, so the scalars come out of each term. This gives the identity. $\square$

**Remark 8.12.10 (Formalization).** The theorems are in [QEqColPer.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/QEqColPer.lean#L56), [IterationAndLinearityCuspidal.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IterationAndLinearityCuspidal.lean#L197), [FlipOfWeilConvergenceAndTheta.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FlipOfWeilConvergenceAndTheta.lean#L62), [CellMassesAgainstLevelVolumesLargeDepth.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/CellMassesAgainstLevelVolumesLargeDepth.lean#L23), [UnfoldingCellMassEqConstMulLocalCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/UnfoldingCellMassEqConstMulLocalCoefficients.lean#L25), [LastRowLatticesGoodPositionLargeDepth.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/LastRowLatticesGoodPositionLargeDepth.lean#L33) and [PeriodReductionToFockVectorsLargeDepth.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/PeriodReductionToFockVectorsLargeDepth.lean#L179). The first theorem takes one clause of a six part result by a chain of projections. The pure core takes the rapid decay of cusp forms as a named hypothesis. The flip theorem and the cell mass theorem raise the heartbeat limit. We have not unfolded the lattice facts, the chain properties or the Fock combinations, so their descriptions above are read from the names and from the way they are used.
