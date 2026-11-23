---
title: Period bounds at the type primes
decls:
  - GlobalTheory.ColPeriodTies.boundAt_of_chainTie
  - GlobalTheory.ColPeriodTies.boundAt_of_ties
  - GlobalTheory.T.periodValuationBound_typePrimePlace_of_chainAgreement
  - GlobalTheory.AtG.jetTableBound_constantOne_of_chainAgreement
  - GlobalTheory.T.propositionCOneUsedTuples_one_of_tiesAt_sizeAt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Period bounds at the type primes

A datum $D$ carries two primes $g_0$ and $g_1$, its *type primes*. This section gives a lower bound for the valuation of a period column at a place $w$ over $g_i$. The bound has the form: minus the losses of the lifts, minus a constant times an error term. It holds at every tuple at which the datum is tied to a chain of characters, and its constant is $1$. The input is the jet bound at split primes of [Jets at a split prime](/entry/jet-at-split-amb-of/). The next section collects these bounds over the used tuples into the arithmetic row at bundle points.

### Places, losses and the error term

Let $D$ be a datum with size data $L$, error data $X$ and divisor data $D_x$. Let $m$ be the length of $D$, $f$ the number of embeddings $\tau$, and $N(m)$ and $t$ the integers of $D$ that the earlier sections use. The *lifts* are the indices $j = 1, \dots, m$.

Let $\mathrm{LL}$ be the field of periods of $D$. A place $w$ of $\mathrm{LL}$ *lies over* $g_i$ if its residue characteristic is $g_i$. For such a place, let $e(w)$ be its ramification index and $v_w$ its additive valuation. The *normalized valuation* is
$$
v_G(w, y) = \frac{v_w(y)}{e(w)}, \qquad y \in \mathrm{LL}.
$$

Let $\bar\pi_i$ be the conjugate of the element $\pi_i$ of the error data $X$ at $g_i$. For a word $u$ and an index $j$, the *row size* $\nu(u, j, \tau)$ is the sum of the first $N(j - 1)$ row values of $u$ at $(j, \tau)$; the row values are not unfolded here. The *loss* of the lift $j$ at $w$ is
$$
\mathrm{loss}(i, u, j, w) = \frac{1}{e(w)} \sum_{\tau} \nu(u, j, \tau)\, v_w\bigl(\tau(\bar\pi_i)\bigr).
$$

The *error term* of $L$ is
$$
\mathrm{err}(D, L) = f \bigl( m\, N(m)\, (N(m) + t) + m^3 \eta_L \bigr),
$$
where $\eta_L > 0$ is the size of $\eta$ given by $L$. Write $\Delta(u, j) = \sum_\tau \nu(u, j, \tau)$.

**Definition 5.16.1 (Size condition).** The datum $D$ satisfies the *size condition* at $i$ if $2 f N(m) + 1 < g_i$ and, for every word $u$ and every lift $j$,
$$
2 \Delta(u, j) + 2 < g_i \quad \text{and} \quad \Delta(u, j) + N(m) < g_i.
$$

**Definition 5.16.2 (Period bound).** Let $C_1$ be a real number. The *period bound* with constant $C_1$ holds at $(i, w, u, \mu)$ if the following is true. For every form $\varphi$ of the module of $u$ and every element $F$ of the lattice $\widetilde{M}(\mu)$, there is $y \in \mathrm{LL}$ whose image is the period column of $(u, \mu)$ at $(\varphi, F)$, and either $y = 0$ or
$$
v_G(w, y) \ge -\sum_{j = 1}^{m} \mathrm{loss}(i, u, j, w) - C_1\, \mathrm{err}(D, L).
$$

A tuple $\mu$ is *used* if it is $\mu_0$ or the tuple $\mu_w$ of a place $w$.

### Ties

The proofs use four ties between $D$ and a system of characters. They are not unfolded here, except for these facts:
1. the *host tie* says that the curve ideal of the host is the unit ideal, that the CM type is induced, that the host field and its abelian unramified extension satisfy their conditions, and that the primes of $X$ are in order;
2. the *character tie* says that the characters $\mathrm{Ch}$ are in order and tied to characters $\mu_0$ and $\eta$, and that the map $\mathrm{sel}$ selects places;
3. the *analytic tie* says that $\delta$ is a twelfth root of the discriminant of the curve ideal, that $\chi$ is a character of the right kind, and that the constants $c_D$ satisfy the generator condition;
4. the *chain tie* at $(u, \mu)$ gives a twist $\xi$, local constants, a chain index with a top element, a kernel equivalence with the ambient kernel of $(B, \chi, c_D)$, an isomorphism of column modules, and a map $j_A$ from the twisted module to the space of $\mu$. The primes of $\mu$ are the primes of $\xi$, and $\xi = 1$ if $\mu = \mu_0$. Under $j_A$ the generators of $\widetilde{M}(\mu)$ are images of rows (the row tie), and the period column is the image of the twisted column (the period tie).

The datum is *tied at* $\mu$ if there are characters, $\mu_0$, $\eta$, $\mathrm{sel}$, $\delta$, a base $B$, $\chi$ and $c_D$ such that the host, character and analytic ties hold and the chain tie holds at $(u, \mu)$ for every word $u$.

### The bounds

**Theorem 5.16.3 (Period bound from a chain tie).** Assume integrality of interlacing branches, and assume that the jet losses of $(D, X, \mathrm{sel}, B, \chi, c_D)$ are bounded. Let $C_1 \ge 1$. Assume the host, character and analytic ties, and the size condition at $i$. Let $w$ lie over $g_i$. If the chain tie holds at $(u, \mu)$, then the period bound with constant $C_1$ holds at $(i, w, u, \mu)$.

Lean: `GlobalTheory.ColPeriodTies.boundAt_of_chainTie`

*Proof.* Take $\varphi$ and $F = j_A(c)$, with coefficients $c_v$ on the generators $v$ of $\widetilde{M}(\mu)$. By the row tie, each $v$ is $j_A(x_v)$ for a row $x_v$. So $x = \sum_v c_v x_v$ has $j_A(x) = F$, and $x$ lies in the integral twisted lattice. Let $y$ be the twisted column of $\varphi$ evaluated at $x$. By the period tie, the image of $y$ is the period column at $(\varphi, F)$.

Next, $g_i$ lies in the prime of $w$: the valuation of $g_i$ at $w$ is $e(w) > 0$. The prime $T_u$ of $u$ and the primes $g_0$ and $g_1$ lie in the bad set of $D$. The size condition gives $2 f N(m) + 1 < g_i$. It also gives, for each $j < m$, that the sum of the weights of row $j + 1$, plus $1$, is less than $g_i$: this sum is $\Delta(u, j + 1)$, it is not negative, and $2 \Delta + 2 < g_i$.

With these facts, a bound on the columns of the chain applies at $w$. A valuation bound on the twisted column then gives
$$
\Bigl| \Bigl( \prod_{j < m} \lambda(i, u, j) \Bigr) y \Bigr|_w \le 1,
$$
where the $\lambda(i, u, j)$ are the loss factors of the weights. These factors are not zero, and a lemma on them gives
$$
v_G\Bigl(w, \prod_{j < m} \lambda(i, u, j)\Bigr) \le \sum_{j = 1}^{m} \mathrm{loss}(i, u, j, w) + \mathrm{err}(D, L).
$$
If $y \ne 0$, the first bound gives $v_G(w, \prod_j \lambda) + v_G(w, y) \ge 0$. Since $\mathrm{err}(D, L) \ge 0$ and $C_1 \ge 1$, we get $v_G(w, y) \ge -\sum_j \mathrm{loss} - C_1 \mathrm{err}$. $\square$

**Theorem 5.16.4 (Period bound from ties).** Assume the jet bound at split primes. Let $D$ be tied at $\mu$ and satisfy the size condition at $i$. Let $w$ lie over $g_i$, and let $u$ be a word whose prime $T_u$ is not the residue characteristic of $w$. Then the period bound with constant $1$ holds at $(i, w, u, \mu)$.

Lean: `GlobalTheory.ColPeriodTies.boundAt_of_ties` (also `GlobalTheory.T.periodValuationBound_typePrimePlace_of_chainAgreement`, a second name)

*Proof.* The jet bound at split primes implies that the jet losses are bounded, for all data $(D, X, \mathrm{sel}, \delta, B, \chi, c_D)$. Integrality of interlacing branches holds by the branching rule for interlacing pairs. Apply the previous theorem with $C_1 = 1$. $\square$

**Corollary 5.16.5 (Period bound at the used tuples).** Assume the jet bound at split primes. Let $D$ be tied at every used tuple and satisfy the size condition at $0$ and at $1$. Then for every $i$, every place $w$ over $g_i$, every word $u$ with $T_u$ different from the residue characteristic of $w$, and every used tuple $\mu$, the period bound with constant $1$ holds at $(i, w, u, \mu)$.

Lean: `GlobalTheory.AtG.jetTableBound_constantOne_of_chainAgreement` (also `GlobalTheory.T.propositionCOneUsedTuples_one_of_tiesAt_sizeAt`, a second name)

*Proof.* Apply the previous theorem at each used tuple. $\square$

The jet bound at split primes is proved in [Jets at a split prime](/entry/jet-at-split-amb-of/). So the corollary depends only on the ties and the size condition. These come from the rows of the constructed point in the next section.

**Remark 5.16.6 (Formalization).** Several facts about the Lean code:
1. The two names `GlobalTheory.T.periodValuationBound_typePrimePlace_of_chainAgreement` and `GlobalTheory.T.propositionCOneUsedTuples_one_of_tiesAt_sizeAt` are second names, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (PeriodValuationBoundTypePrimePlaceOfChainAgreemeStatement.lean:10, JetTableBoundConstantOneOfChainAgreementStatement.lean:9). The file names are cut short: `…ChainAgreeme.lean`.
2. In `boundAt_of_ties` the hypothesis that $T_u$ is not the residue characteristic of $w$ is introduced as `_` and not used (PeriodValuationBoundTypePrimePlaceOfChainAgreeme.lean:99). The chain tie proof does not need it.
3. The period bound is `BoundAt`, the size condition is `SizeAt`, the ties are `HostTie`, `CharTie`, `AnTie` and `ChainTie` (BlockTheory/ThetaLiftGeometry/BadPrimesPeriodBound.lean:61, 64, 70, 73, 120, 136), and "tied at $\mu$" is `GlobalTheory.AtG.TiesAt` (Definitions/GaloisGeometry/JetSplitAmb.lean:29). The jet bound at split primes is `GlobalTheory.AtG.JetSplitAmb` (same file, line 15). The bound with constant $C_1$ at all used tuples is `Formalism.L2.G.Adm2InU.UsedTuplesBoundByConstant` (Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean:25).
4. The loss is `vNN` (Formalism/LocalRingCardinality/DataErr.lean:88), the error term is `LiftErrorLocal.errC` and $v_G$ is `LiftErrorLocal.vG` (Formalism/SharpRestriction/Divisibility/LiftErrorLocal.lean:421 and :28). The column bound is `colMu_bound_all`, the valuation bound is `valuation_PtilE_le_one`, and the lemma on the loss factors is `vG_loss_le` (PeriodBoundOfJetLoss.lean:87). The jet losses come from `GlobalTheory.T.thetaJetIntegrality_typePrime_of_splitTableBound`, and integrality from `GlobalTheory.BranchFormula.integrality` applied to `Formalism.L2.DIV.BrJ.branching_interlacing_pairs`. None of these lemmas is in the chapter outline.
5. A related definition `periodBound_at` (BadPrimesPeriodBound.lean:142) also asks that $g_i$ is not a prime of $\mu$. The theorems here do not need this condition.
