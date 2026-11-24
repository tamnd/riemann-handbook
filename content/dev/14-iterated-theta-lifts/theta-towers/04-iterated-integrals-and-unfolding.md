---
title: Iterated integrals and the unfolding along the row
decls:
  - GlobalTheory.RowChain.twisted_iterate_eventually_large
  - GlobalTheory.RowChain.twisted_iterate_eq_linear
  - GlobalTheory.T.twisted_iterate_chain
  - GlobalTheory.RowUnfLast.twisted_theta_integral_unfolding
  - GlobalTheory.T.twisted_theta_integral_unfolds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Iterated integrals and the unfolding along the row

This section writes the pairing of a column function with a lift along the opposite path of the grid as an iterated integral over the row groups, and then unfolds it into a finite sum of periods over the top corner of the grid. The unfolding is the third of the four steps of the row formula in [Theorem 3.6.6](/entry/theta-lift-row-properties-conj/). Both results hold at large scale in the sense of [the cusp step](/entry/cusp-step-of-large-flip-run/).

We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/), and we assume that lifts of Fock vectors keep cusp forms, as in [Section 3.3.4](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/). Let $c$ be a choice of the row, with grid $G$, Weil datum $W$, discrete series model $\mathcal M$ and real matching $\rho$.

**Definition 3.4.1 (Paths of the grid).** Fix an index $t$. The given path runs from the top node $(0, m)$ down the first column to $(0, 0)$, and then right along the bottom row to $(m, 0)$. The opposite path runs from $(0, m)$ right along the top row to $(m, m)$, and then down the last column to $(m, 0)$. A lift along a path is the composite of the theta lifts of its arrows.

The two paths bound the grid, and the flips of Section 5 move one into the other square by square. Along the opposite path, the data of the lifts are a finite combination $\tau_i$ of pairs $P$ of polynomials on the row and on the last column, and a finite combination $\tau$ of pairs of Schwartz data of the row and of the last column at $t$. Together they give a combination of test vectors on the opposite path, which we write $\tau_i \otimes \tau$. For a volume datum $M$ good at $t$, let $\Lambda_{\mathrm{opp}}(\tau_i \otimes \tau)$ be the lift along the opposite path with these test vectors. It is linear in the combination.

**Definition 3.4.2 (The pairing on the top row).** For each $a$, the choice gives a column function $\varphi_a$ on the top node: the pairing of the functional $\xi$ of the choice with the column vector of $a$. For a vector $y$ of the target space at $t$, the choice gives a form $F_y$ on the node $(0, m)$. Let $B^+$ be the Petersson pairing of the model $\mathcal M$ between functions on the top node. Put

$$L(t, M, \tau_i, \tau, a, y) = B^+\bigl( \varphi_a, \Lambda_{\mathrm{opp}}(\tau_i \otimes \tau)(F_y) \bigr).$$

We have not unfolded the pairing $B^+$, the column vectors or the forms $F_y$. A combination $\tau$ is flip-finite for a theta datum $\Phi$ if it meets the finiteness condition of the flips; we have not unfolded it either.

The pairing $L$ is the object of the row formula. It is a nested integral: an integral over the top node of a function that is itself a chain of theta integrals along the row and the last column. The first result says that this nesting is a genuine iterated integral over the row groups.

**Definition 3.4.3 (Iterated quotient integral).** Let $(H_j)_{j \in J}$ be groups with subgroups $R_j \subseteq H_j$, measures $\rho_j$ on $R_j$ and $\mu_j$ on $H_j$. Let $q$ be a function on $\prod_j H_j$, let $j_1, \ldots, j_k$ be a list of indices, let $h \in \prod_j H_j$ and $z \in \mathbb C$. We say that $z$ is the iterated quotient integral of $q$ at $h$ along the list if one of the following holds.

1. The list is empty and $z = q(h)$.
2. The list is $j_1, \ldots, j_k$ with $k \ge 1$, and there is a function $f$ on $H_{j_1}$ such that $f$ is integrable on the quotient $R_{j_1} \backslash H_{j_1}$ for the measures $\rho_{j_1}$ and $\mu_{j_1}$ with integral $z$, and for every $g \in H_{j_1}$ the value $f(g)$ is the iterated quotient integral of $q$ at $h$ with the entry $j_1$ replaced by $g$, along the list $j_2, \ldots, j_k$.

So $z = \int_{R_{j_1} \backslash H_{j_1}} \cdots \int_{R_{j_k} \backslash H_{j_k}} q(g_1, \ldots, g_k)$, with each inner integral defined and integrable. We have not unfolded the condition of integrability on a quotient.

For the grid, the index set $J$ is the set of row indices $j$ of the datum, $H_j$ is the group of the node $(m, j)$, and $R_j$ is the row group at $j$. For a pair $P$ of polynomials and a combination $\tau$, let $q_{P, \tau}$ be the integrand: the sum over the pure tensors $d$ of $\tau$ of $\tau(d)$ times the period over the top node of $\varphi_a$ against the lift of $F_y$, with the test vectors of $d$ and $P$ moved by the point $h$ of the row groups.

**Theorem 3.4.4 (The pairing is an iterated integral).** At large scale, the following holds. There are measures $\rho_j$ on the row groups and $\mu_j$ on the groups of the last column, all Haar measures, such that for every index $t$, every $a$, every combination $\tau$ that is flip-finite for $\Phi_a$, every volume datum $M$ good at $t$, every pair $P$ and every $y$: the value $L(t, M, \delta_P, \tau, a, y)$ is the iterated quotient integral of $q_{P, \tau}$ at $1$ along the row indices. Here $\delta_P$ is the combination with coefficient $1$ at $P$ and $0$ elsewhere.

Lean: `GlobalTheory.RowChain.twisted_iterate_eventually_large`.

*Proof.* We use three facts at large scale: the cusp step of [Theorem 3.3.6](/entry/cusp-step-of-large-flip-run/), the fact that the leading form at the top of the row is a listed cusp form, and the continuity of the column functions $\varphi_a$. Choose Haar measures $\rho_j$ on the row groups and volume data with Haar measures $\mu_j$ at the nodes of the last column; both exist for every grid. Fix $t$, $a$, $\tau$, $M$, $P$ and $y$, and let $d$ be a pure tensor in the support of $\tau$. Cusp forms are rapidly decreasing, by the input on rapid decay. With the cusp step, this shows two things for the pure lift $\Lambda_{\mathrm{opp}}(P \otimes d)(F_y)$: its pairing with $\varphi_a$ converges, and this pairing is the iterated quotient integral of the period at $d$, first for the measures of $M$ and then for the measures $\mu_j$, which agree on the last column. Now

$$L(t, M, \delta_P, \tau, a, y) = \sum_{d} \tau(d)\, B^+\bigl(\varphi_a, \Lambda_{\mathrm{opp}}(P \otimes d)(F_y)\bigr),$$

by linearity of the lift in the test vectors and of $B^+$ in its second argument. The integrand $q_{P, \tau}$ is the same combination of the periods at the pure tensors $d$. An iterated quotient integral is linear in the integrand, since each inner integral is. So the combination of the values is the iterated quotient integral of the combination. $\square$

**Theorem 3.4.5 (Iterated integral and linearity).** At large scale, the conclusion of [Theorem 3.4.4](/entry/twisted-iterate-eventually-large/) holds, and the pairing is linear in $\tau_i$: for every $t$, $a$, flip-finite $\tau$, $M$ good at $t$, every combination $\tau_i$ and every $y$,

$$L(t, M, \tau_i, \tau, a, y) = \sum_{P} \tau_i(P)\, L(t, M, \delta_P, \tau, a, y).$$

Lean: `GlobalTheory.RowChain.twisted_iterate_eq_linear` (also `GlobalTheory.T.twisted_iterate_chain`, a second name).

*Proof.* The first part is [Theorem 3.4.4](/entry/twisted-iterate-eventually-large/). The linearity holds at large scale by a lemma on the valuations at the places of the row; we have not opened its proof. Two statements that hold at large scale hold together with the larger thresholds. $\square$

We now come to the unfolding. For each $t$ and theta datum $\Phi_a$ there is a finite set $\mathrm{supp}_t(\Phi_a)$ of coset families $\beta$. Each $\beta$ has a coefficient $c_w(\beta)$ at each place $w$, a volume condition on volume data and an expansion condition on combinations of pure data. Let $\Xi_t$ be the subgroup of $\mathbb C^\times$ generated by the local values of the character $\xi_t$ of the level. For a pair $P = (P_{\mathrm{col}}, P_{\mathrm{row}})$ of polynomials on the column and the row, a pure datum $d$ and a volume datum $M$, the period over the top corner is

$$\mathcal P_M(P, d; \varphi, F) = \int_{\mathcal F_{mm}} \Lambda_{\mathrm{col}}(\varphi)(\iota h)\, \Lambda_{\mathrm{row}}(F)(h)\, d\nu_{mm}(h).$$

Here $\mathcal F_{mm}$ is the fundamental domain of $M$ at the node $(m, m)$, $\Lambda_{\mathrm{col}}$ is the lift along the column $X_0 \to X_1 \to \cdots \to X_m$ with the Fock test vectors of $d$ and $P_{\mathrm{col}}$, $\Lambda_{\mathrm{row}}$ is the lift along the top row with those of $d$ and $P_{\mathrm{row}}$, and $\iota$ is the embedding of the stabilizer at the top. For combinations $\sigma$ of pairs $P$ and $\tau$ of pure data put

$$\mathcal P_M(\sigma, \tau; \varphi, F) = \sum_{P} \sum_{d} \sigma(P)\, \tau(d)\, \mathcal P_M(P, d; \varphi, F).$$

**Definition 3.4.6 (The sum condition).** The sum condition says that at large scale, for every $t$ and $a$, the sum data of the choice meet the sum condition at $t$ for $\Phi_a$. We have not unfolded the sum condition at $t$.

**Theorem 3.4.7 (Unfolding along the row).** Assume the sum condition. Then the following holds at large scale. For every combination $\tau_i$ there are a combination $\sigma$ of pairs of polynomials on the column and the row, and elements $z_t \in \Xi_t$ for each $t$, with this property. Let $a$ be given, let $\tau$ be flip-finite for $\Phi_a$, and let $M$ be good at $t$. Let $M_\beta$ and $\tau_\beta$, for the families $\beta$, be volume data and combinations of pure data such that $M_\beta$ meets the volume condition and $\tau_\beta$ the expansion condition for each $\beta \in \mathrm{supp}_t(\Phi_a)$. Then for every $y$,

$$\begin{aligned} &B^+\bigl(\varphi_a, \Lambda_{\mathrm{opp}}(\tau_i \otimes \tau)(F_y)\bigr) \\ &\quad = z_t^{-1}\, s \sum_{\beta \in \mathrm{supp}_t(\Phi_a)} \Bigl( \prod_w c_w(\beta) \Bigr)\, \mathcal P_{M_\beta}(\sigma, \tau_\beta; \varphi_a, F_y), \end{aligned}$$

where $s$ is the scalar of the sum data of the choice.

Lean: `GlobalTheory.RowUnfLast.twisted_theta_integral_unfolding` (also `GlobalTheory.T.twisted_theta_integral_unfolds`, a second name).

*Proof.* By [Theorem 3.4.5](/entry/twisted-iterate-eq-linear/), the left side is linear in $\tau_i$, and for each $P$ it is an iterated quotient integral over the row groups. We unfold this integral one row group at a time. Each row group splits into a real part and a finite part. The integrand is invariant on both sides under the row groups and the lattice groups, and it is supported on finitely many cells, the double cosets of the support families $\beta$. Off the twist places each family has a single coset. On each cell the integrand is a constant times a value of the period over the top corner, and this period depends only on the product of the local test functions. Linear relations between the values on cells pass to the integrals. So the iterated integral over the last row is a constant times a finite sum over the cells. The weight of a cell is a ratio of masses, and these masses are matched with the level volumes $M_\beta$; a change of measures in the period accounts for the passage from $M$ to $M_\beta$. The period is reduced to Fock vectors, which gives the combination $\sigma$. The support families are cosets of a staircase shape, and the sum condition identifies them with $\mathrm{supp}_t(\Phi_a)$ and gives the scalar $s$ and the coefficients $c_w(\beta)$. The factor $z_t^{-1}$ collects the values of $\xi_t$ met in the unfolding, so it lies in $\Xi_t$. Each of these facts holds at large scale, and we take the largest thresholds. $\square$

**Remark 3.4.8 (Formalization).** The unfolding joins seventeen statements that each hold at large scale, together with the sum condition. Of these, only the iterated integral of [Theorem 3.4.5](/entry/twisted-iterate-eq-linear/) uses the local inputs and the condition on Fock vectors. We have not opened the other sixteen lemmas, and the proof above follows their names and the way they are combined. The proof is a near copy of the last step of the row unfolding in [UnfoldingOfCuspidalLifts.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/UnfoldingOfCuspidalLifts.lean#L30), which assumes a second list of hypotheses in place of the local inputs. In [TwistedIterateEventuallyLarge.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedIterateEventuallyLarge.lean#L17) lines 17 to 30 are empty sections.
