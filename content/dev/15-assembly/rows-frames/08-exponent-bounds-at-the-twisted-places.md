---
title: Exponent bounds at the twisted places
decls:
  - GlobalTheory.T.primePowerLatticeInclusion_of_localModels
  - GlobalTheory.ExpTie.lIncl_of_models
  - GlobalTheory.ExpTie.Asm.jexpU_le_jrec7
  - GlobalTheory.sum_exponent_log_le_of_cut
  - GlobalTheory.ExpTie.Asm.hasExpBound_at
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Exponent bounds at the twisted places

This section proves the exponent bound of a leaf object at a point of the main construction. The exponent of a block at a place $w$ measures how far the cut lattice of the block is from its dual lattice at $w$. The bound says that this exponent is at most a number $J^{(7)}(\ell)$ given by the seventh recursion at the residue characteristic $\ell$ of $w$, and that the sum of $J^{(7)}(\ell) \log \ell$ over any set of primes is at most a polynomial in the size data. The result is used by [the exponent statement](/entry/exp-st-of-alt/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The local input is [the weight inputs of a frame](/entry/winputs-frame/) of the last section.

Let $K$ be a CM number field and let $B$ be a block datum over $K$ with a level $\ell_0$ and a subspace $Z$ of its forms. The block gives two $\mathcal{O}_K$-lattices in $K^{d}$: the *cut lattice* $C$, cut out of the lattice of the block by a frame of $Z$, and the *dual cut lattice* $\Delta$, cut out of the dual lattice by the same frame. Let $w$ be a finite place of $K$ with prime ideal $\mathfrak{p}_w$, residue characteristic $\ell = \ell_w$ and ramification index $e_w$. For $J \in \mathbb{N}$, the *lattice inclusion* of power $J$ at $w$ says
$$\ell^J C \subseteq \Delta_{\mathfrak{p}_w},$$
where $\Delta_{\mathfrak{p}_w}$ is the localization at $\mathfrak{p}_w$. The *exponent* of the block at $w$ is
$$J_B(w) = \frac{1}{e_w} \min \{ J : \mathfrak{p}_w^J C \subseteq \Delta_{\mathfrak{p}_w} \}.$$
If the inclusion of power $J$ holds, then $0 \leq J_B(w) \leq J$, since $\ell^J$ and $\mathfrak{p}_w^{e_w J}$ generate the same ideal after localization at $\mathfrak{p}_w$.

Let $P$ be the parameters and $W$ the weights of the numerical datum, with $N$ the rank. They give two numbers at each prime $\ell$. The first is the *naive bound* $J_A(\ell) = \sum_\tau \mathrm{ex}(\tau, \ell)$, the sum of the $\ell$-exponents of the weight $\lambda_\tau$. The second is the *coarse bound* $c_W(\ell)$, a floor sum that takes the large weights in $T_2$ into account. A prime $\ell$ is *in range* if $\ell_J < \ell \leq h$, $\ell$ is not excluded and $\ell$ is not one of the special primes of $W$; here $\ell_J$ and $h$ are thresholds of $P$. The seventh recursion is
$$J^{(7)}(\ell) = \begin{cases} J_A(\ell) & \text{if } \ell \leq \ell_J, \ \ell \text{ is excluded, or } \ell \text{ is special}, \\ c_W(\ell) & \text{otherwise.} \end{cases}$$

A family $X$ of Hida settings *covers* the block at $w$ if the lattice inclusion of power $J$ at $w$ holds whenever each $X_i$ has the Hida lattice inclusion of power $J$ at $\ell$.

**Theorem 7.8.1 (Lattice inclusion from local models).** Let the numerical datum be good for $P$ and $W$, let $\ell = \ell_w$ be in range, and let $\mathrm{fr}$ and $\mathrm{cj}$ be Frobenius data. Let $X$ be a family of Hida settings that covers the block at $w$, such that $\ell$ is not a unit in each $X_i$ and the weight inputs with lattice links hold for $X_i$ and the weights $W$ with the Frobenius data $\mathrm{fr}, \mathrm{cj}$. Then the lattice inclusion of power $c_W(\ell)$ holds at $w$.

Lean: `GlobalTheory.T.primePowerLatticeInclusion_of_localModels` (also `GlobalTheory.ExpTie.lIncl_of_models`).

*Proof.* Changing the Frobenius data keeps the weights good, and at a prime in range it does not change the coarse bound. By the cover, it is enough to show the Hida inclusion of power $c_W(\ell)$ for each $X_i$. Fix $i$. The weight inputs with lattice links give the weight inputs of the Hida setting. With these and the fact that $\ell$ is not a unit, the Hida lattice inclusion at the coarse bound holds for $X_i$ with the changed weights. Its power is the coarse bound of the changed weights, which equals $c_W(\ell)$. $\square$

A *local model* at $w$ is a choice of $\mathrm{fr}$, $\mathrm{cj}$ and $X$ as in the theorem.

**Lemma 7.8.2 (Exponent and seventh recursion).** Assume the cut inequality for the exponents of dual Weyl modules. Let the numerical datum be good. Assume that if $\ell_w$ is not in range, the lattice inclusion of power $J_A(\ell_w)$ holds at $w$, and that if $\ell_w$ is in range, there is a local model at $w$. Then
$$J_B(w) \leq J^{(7)}(\ell_w).$$

Lean: `GlobalTheory.ExpTie.Asm.jexpU_le_jrec7`.

*Proof.* The prime $\ell = \ell_w$ is prime. If $\ell$ is in range, the theorem gives the inclusion of power $c_W(\ell)$, so $J_B(w) \leq c_W(\ell) = J^{(7)}(\ell)$. If $\ell$ is not in range, the inclusion of power $J_A(\ell)$ gives $J_B(w) \leq J_A(\ell)$. It remains to see $J_A(\ell) \leq J^{(7)}(\ell)$. If $\ell \leq \ell_J$, $\ell$ is excluded or $\ell$ is special, the two are equal. Otherwise $\ell > h$, and beyond the height the naive bound is $0$; this uses the cut inequality. $\square$

The *cut inequality* is an inequality for the $\ell$-exponent $\mathrm{ex}_N(\lambda, \ell)$ of a dual Weyl module of rank $N$ with antitone weight $\lambda$, when the shifted entries $\lambda(a) - a$ lie in an interval $[\mathrm{lo}, \mathrm{lo} + w]$. For each $a \leq N$ it says
$$\mathrm{ex}_N(\lambda, \ell) \leq \mathrm{ex}_a(\lambda|_{[0, a)}, \ell) + \mathrm{ex}_{N-a}(\lambda|_{[a, N)}, \ell) + a(N-a) \log_\ell w,$$
where $\log_\ell w$ is the integer part of the logarithm to base $\ell$.

**Theorem 7.8.3 (Sum of the seventh recursion).** Assume the cut inequality. Let $P$ satisfy its hypotheses and be large, with the row and size estimates for some $X'$ and $A$. Let $W$ be good weights on a set of $f$ indices, with at most $5$ special primes and $|T_2| \leq T$. Then for every finite set $Q$ of primes,
$$\sum_{\ell \in Q} J^{(7)}(\ell) \log \ell \leq 30\, T\, m\, b\, L^2 + 2 m b,$$
where $m$, $b$ and $L$ are the rank, the size and the logarithmic scale of $P$.

Lean: `GlobalTheory.sum_exponent_log_le_of_cut`.

*Proof.* The cut inequality gives the recursion for exceptional primes. With the count of primes in short intervals, it bounds the sum by $|T_2|$ times a term in $m$, $b$, $L$, plus a tail. The tail bound holds by the row and size estimates, since $|T_2| \leq f$. The term grows with $|T_2|$, its coefficient $30 m b L^2$ is nonnegative since $b > 0$, and $|T_2| \leq T$. $\square$

Now let a point of the main construction carry a leaf object $O$ with the rank $m$, scale $x$, exponent $\varepsilon$ and count $|T_2|$ of the datum, and let each index $j$ carry parameters $P_j$ and weights $W_j$ that match the datum and are good. The *exponent bound* of $O$ asks:

1. $J_B(w, j) \geq 0$ at each twisted place $w$ and each $j$;
2. there is $J_p(j, \ell) \geq 0$ with $\sum_{\ell \in Q} J_p(j, \ell) \log \ell \leq 30 |T_2| m b x_e^2 + 2 m b$ for each finite set $Q$ of primes, where $x_e = x^\varepsilon$ and $b = e^{x_e}$;
3. $J_B(w, j) \leq J_p(j, \ell_w)$ at each twisted place $w$.

**Theorem 7.8.4 (Exponent bound at a point).** Assume the cut inequality. Let the lattice inclusion of power $J_A$ hold for every block and place, and let there be a local model at each twisted place in range. Then $O$ has the exponent bound.

Lean: `GlobalTheory.ExpTie.Asm.hasExpBound_at`.

*Proof.* Take $J_p(j, \ell) = J^{(7)}_{W_j}(\ell)$, a natural number. Clause 1 follows from the inclusion of power $J_A$, which gives $J_B \geq 0$. For clause 2, the matching of $P_j$ with the datum gives $f$ indices, the special primes and $|T_2|$ at most that of the host, and identifies $L = x_e$ and $b = e^{x_e}$; [the sum for the exceptional set](/entry/sum-exponent-log-le/) then gives the bound. Clause 3 is the lemma, applied to the block at the place over $w$. $\square$

**Remark 7.8.5 (Formalization).** The lattice inclusion is `LIncl` and the cover is `Covers` in [SumExpSt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SumExpSt.lean#L23), with the local model `ModelAt` at line 77. The exponent is `JexpU` in [RowLat.lean](lean:Formalism/LocalToGlobal/Divisibility/RowLat.lean#L161), the quotient of `JexpW` by $e_w$. Here `JexpW` is an `sInf` of a set of naturals ([RowLat.lean](lean:Formalism/LocalToGlobal/Divisibility/RowLat.lean#L39)), so it is $0$ when no power works; the bound $J_B \geq 0$ therefore holds for free, and clause 1 does not need the inclusion it is proved from. The seventh recursion is `Wts.Jrec7` in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L445) and the cut inequality is `ExCut` in [StatementE.lean](lean:Formalism/PieriBlockIdeals/StatementE.lean#L25). The theorem on local models takes primality of $\ell_w$ as a hypothesis, but it always holds by `plc_prime`, which the lemma uses to supply it. Its statement file sets `maxHeartbeats` to 1000000. The proof of the first theorem uses `expo_frob_indep`, `weight_inputs_of_linkage_holds` and `inclusion_w_seven_real_holds`, and the lemma uses `exponent_datum_le_of_primePowerLatticeInclusion` and `exponent_of_record_vs_formulas`; we read their statements. The sum theorem uses `recursion_sum_exceptional` and `tail_bound_holds`. The last theorem calls `UpperTheory.ExcSet.sum_exponent_log_le` for clause 2, not the sum theorem directly. The identity `splitPartNumbers_exponent_eq_liftExponent` at line 45 of [ExpansionOfNumericsModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpansionOfNumericsModel.lean#L45) is `rfl`, and `expSt_of` at line 80 of that file restates a variant proved elsewhere.
