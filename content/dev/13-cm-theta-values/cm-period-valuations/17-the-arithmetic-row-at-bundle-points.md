---
title: The arithmetic row at bundle points
decls:
  - GlobalTheory.AtG.row_atG_of_jetSplitAmb
  - GlobalTheory.T.typePrimePeriodRow_of_constructedPointChains
  - GlobalTheory.AtG.row_atG_pinned
  - GlobalTheory.T.atGRows_bundlePoints_of_jetSplitAmbient
  - GlobalTheory.AtG.jetSplitAmb_holds
  - GlobalTheory.T.jetTableBound_splitPrime
  - GlobalTheory.AtG.row_aAtG_of_rowPin
  - GlobalTheory.T.holds_at_bundlePoints_of_trueColumns
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The arithmetic row at bundle points

This section proves the *arithmetic row*: for families of bundles over constructed points, the period bound of Section 16 holds with a constant $C_1$ at the used tuples, and the size data are bounded at the type primes by the same constant. The hypothesis is that the rows of every constructed point are pinned. The proof turns pinned rows into ties, and ties into the period bound with $C_1 = 1$. The jet bound at split primes, which Section 16 assumed, is proved here by a reference to [Jets at a split prime](/entry/jet-at-split-amb-of/). The result is used in [the arithmetic row at built points](/entry/row-a-at-g-at-built-alt/) of Volume 15.

We keep the notation of Section 6 (slots $Q$, linkages $\mathrm{Lk}$, constructed points $\beta$, the row condition, "holds in a row") and of Section 16 (the type primes $g_i$, the losses, the error term $\mathrm{err}(D, L)$, the size condition, the period bound, ties, used tuples).

### The conditions

Let $\mathcal{F}$ be a family with scale $\varepsilon$ and threshold $x_1$. For each $x > x_1$ and each index $i$ it has a datum $D_{x, i}$, size data $L_{x, i}$ and error data $X_{x, i}$. The family also has an error constant $g(\mathcal{F})$.

**Definition 5.17.1 (Size bound at the type primes).** The family $\mathcal{F}$ has the *size bound at the type primes* with constant $C_1$ if there is $x_0$ such that the following holds for all $x \ge x_0$ with $x > x_1$ and all $i$. Let $D = D_{x, i}$ and $L = L_{x, i}$. For every type prime $g_k$ of $D$, every place $w$ over $g_k$ and every word $u$ whose prime $T_u$ is not the residue characteristic of $w$,
$$
\sum_{j = 1}^{m} \bigl( L_F(j, w) - L_E(u, j, w) \bigr) \le -\sum_{j = 1}^{m} \mathrm{loss}(k, u, j, w) - C_1\, \mathrm{err}(D, L).
$$
Here $L_F$ and $L_E$ are values of the size data; they are not unfolded here.

A family class $\mathcal{A}$ has a subclass $\mathcal{A}_3$ of families with three further size conditions; this subclass is not unfolded here. A property $P$ of families and numbers $C_H$ is *closed* on a class if there is $\varepsilon_1 > 0$ such that for every scale $\varepsilon \le \varepsilon_1$ there are thresholds $K$ with this property: $P(\mathcal{F}, C_H)$ holds for every family $\mathcal{F}$ of scale $\varepsilon$ in the class that is large for $K$ and $C_H$.

**Definition 5.17.2 (Arithmetic row).** The *arithmetic condition* holds for a family class $\mathcal{A}$ if the following property is closed on $\mathcal{A}_3$: there is $C_1$ such that, for all large $x$ and all $i$, the period bound with constant $C_1$ holds for $(D_{x, i}, L_{x, i}, X_{x, i})$ at every type prime $g_k$, every place $w$ over $g_k$, every word $u$ with $T_u$ different from the residue characteristic of $w$ and every used tuple; and $\mathcal{F}$ has the size bound at the type primes with constant $C_1$. The *arithmetic row* for $(Q, \mathrm{Lk})$ says that the arithmetic condition holds in a row.

### From ties to the row

**Theorem 5.17.3 (Arithmetic row from ties).** Assume the jet bound at split primes. Let $Q$ be a slot and $\mathrm{Lk}$ a linkage. Assume that the property "the datum $D$ of the object $O$ is tied at every used tuple, with the error data and divisor data of $O$" satisfies the row condition for $(Q, \mathrm{Lk})$. Then the arithmetic row holds for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.AtG.row_atG_of_jetSplitAmb` (also `GlobalTheory.T.typePrimePeriodRow_of_constructedPointChains`, a second name)

*Proof.* We take $E$ to be the property of the hypothesis. Let $\sigma$ be a selection along $E$ for $\mathcal{A}$. We prove closure with $\varepsilon_1 = 1/100$. Fix a scale $\varepsilon \le 1/100$; then $\varepsilon < 1/52$. A lemma on kernel degrees gives $x_0$ with this property: every datum $D$ with size data $L$ that satisfy the parameter choice and the size conditions, with scale $\varepsilon$ and $x \ge x_0$, satisfies the size condition of Section 16 at $0$ and at $1$.

We take the thresholds $K = (0, 0, 2, 0)$. Let $\mathcal{F}$ be a family of $\mathcal{A}_3$ of scale $\varepsilon$ that is large for $K$. Largeness for the third threshold gives $g(\mathcal{F}) \ge 2$. The family lies in $\mathcal{A}$, so the selection gives, at each $(x, i)$, that $D_{x, i}$ is tied at every used tuple. We take $C_1 = 1$.

The period bound: for $x \ge x_0$ and each $i$, the size condition holds at $0$ and at $1$ by the lemma on kernel degrees, applied with the parameters and sizes of $\mathcal{F}$ at $(x, i)$. The [period bound at the used tuples](/entry/jet-table-bound-constant-one-of-chain-agreement/) of Section 16 gives the period bound with constant $1$.

The size bound: a lemma on the family says that the size bound at the type primes holds with constant $C_1$ whenever $0 \le C_1$ and $2 C_1 \le g(\mathcal{F})$. With $C_1 = 1$ both conditions hold. $\square$

**Definition 5.17.4 (Pinned rows).** Let $\beta$ be at a position with a part over $(w, Z)$, and let $a$ be a tuple of the datum. The rows are *pinned* at $a$ if for every word $u$ there is a linear isomorphism $e$ from the module of periods of $(u, a)$ to the space of $a$ with three properties:
1. $e$ is the standard isomorphism of $u$ if $a = \mu_0$, and the twisted isomorphism of $(u, a)$ otherwise;
2. every generator of $\widetilde{M}(a)$ is the image under $e$ of a row form;
3. a row form lies in the integral lattice if and only if its image under $e$ is an integral combination of the generators of $\widetilde{M}(a)$.

**Theorem 5.17.5 (Arithmetic row from pinned rows and split jets).** Assume the jet bound at split primes. Let $Q$ be a slot and $\mathrm{Lk}$ a linkage. Assume that every core with $Q$ is at a position with a part over some $(w, Z)$ at which the rows are pinned at every tuple. Then the arithmetic row holds for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.AtG.row_atG_pinned` (also `GlobalTheory.T.atGRows_bundlePoints_of_jetSplitAmbient`, a second name)

*Proof.* Let $\beta$ be a constructed point whose core satisfies $Q$. A lemma on normalized rows says that pinned rows tie the datum $\beta.D$ to a chain at every tuple $\mu$, with the error data and divisor data of $\beta.O$. This holds for all points and all parameters, so the property of the previous theorem satisfies the row condition. The previous theorem applies. $\square$

**Theorem 5.17.6 (Jet bound at split primes).** The jet bound at split primes holds for every ambient kernel.

Lean: `GlobalTheory.AtG.jetSplitAmb_holds` (also `GlobalTheory.T.jetTableBound_splitPrime`, a second name)

*Proof.* This is [Jets at a split prime](/entry/jet-at-split-amb-of/), with the same hypotheses in the same order. $\square$

The jet bound says: let the ambient kernel of $(B, \chi, c_D)$ be formed over a seam in order, with a curve ideal, with $\delta$ and $\chi$ as in the analytic tie, and with the lattice hypothesis at $(a, b, S)$ for a finite set $S$ of primes. Let $N$ and $N'$ be self-dual lattices of even ranks $a$ and $b$, standard at a prime $p \ge 5$ that does not divide the discriminant of $E$ or $d$, with $|\iota(c_D(\tau))| \le 1$ for all $\tau$. Let $p = \pi \bar\pi$ with $\pi$ a quadratic integer, split in the kernel. Then for every $c' > 0$ prime to $p$, every $x$ in the divided lattice of level $c'$ and every multi-index $m$,
$$
\bigl| \iota\bigl( \sigma_0 (J(p c', x, m)) \bigr) \bigr| \cdot |\iota(\bar\pi)|^{|m|} \cdot |p|^{f a b} \le 1,
$$
where $J$ is the jet of the kernel and $\iota : \mathbb{C} \to \mathbb{C}_p$ is a field isomorphism.

**Corollary 5.17.7 (Arithmetic row at bundle points).** Let $Q$ be a slot and $\mathrm{Lk}$ a linkage. Assume that every core with $Q$ is at a position with a part over some $(w, Z)$ at which the rows are pinned at every tuple. Then the arithmetic row holds for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.AtG.row_aAtG_of_rowPin` (also `GlobalTheory.T.holds_at_bundlePoints_of_trueColumns`, a second name)

*Proof.* Combine the two previous theorems. $\square$

**Remark 5.17.8 (Formalization).** Several facts about the Lean code:
1. The four `GlobalTheory.T.*` names are second names, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (TypePrimePeriodRowOfConstructedPointChainsStatement.lean:9, PeriodValuationsTypePrimesOfJetTableSplitPrimeStatement.lean:8, JetTableBoundSplitPrimeStatement.lean:5, DeliveryAtBundlePointsOfTrueColumnsStatement.lean:8).
2. In `row_atG_of_jetSplitAmb` the closure constant is fixed as $\varepsilon_1 = 1/100$, the thresholds as `⟨0, fun _ => 0, fun _ => 2, fun _ => 0⟩`, and the constant as $C_1 = 1$ (TypePrimePeriodRowOfConstructedPointChains.lean:21, 23 and 26). The lemma on kernel degrees is `GlobalTheory.T.kernelDegrees_small_against_typePrimes` (KernelDegreesSmallAgainstTypePrimesStatement.lean:10) and the lemma on the family is `Formalism.MainNotions.J.family_type_prime_loss` (Formalism/SharpRestriction/AdmissibleParameterJoins/GandSaj.lean:43).
3. The ties are produced at every tuple by `GlobalTheory.T.concreteChainAgreesAtTuple_of_normalisedRows`, a second name of `GlobalTheory.Svd.tiesAt_of_rowPin`, (PeriodValuationsTypePrimesOfJetTableSplitPrime.lean:14), but `row_atG_of_jetSplitAmb` asks for them only at $\mu_0$ and at the tuples $\mu_w$ (TypePrimePeriodRowOfConstructedPointChains.lean:16).
4. The arithmetic condition is `H_aAtG` and the arithmetic row is `AllBundlePointProperties.ArithmeticConditionAtBundlePoints` (Definitions/GlobalTwisting/LevelPrimeColumnValuationsAtBundlePoints.lean:21 and :25). Closure is `Closed` (Formalism/SharpRestriction/ParamsHeightRankConstant.lean:159), the subclass $\mathcal{A}_3$ is `W3` (ValidForConstructedPointClassesEventuallyWorking.lean:371), and the size bound at the type primes is `familySizeBoundAtTypePrime`, built from `SgAtG` (Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean:1147 and :1002).
5. Pinned rows are `GlobalTheory.AtG.RowPin` (Definitions/GaloisGeometry/JetSplitAmb.lean:35). The jet bound at split primes is `GlobalTheory.AtG.JetSplitAmb` (same file, line 15), and `jetSplitAmb_holds` introduces 42 arguments and passes all but the five implicit ones to `Formalism.L2.Ker.Test.jetAtSplit_ambOf` in the same order (JetTableBoundSplitPrime.lean:7). The corollary is the one-line term `atGRows_bundlePoints_of_jetSplitAmbient jetTableBound_splitPrime` (ConstructionAtBundlePointsOfTrueColumns.lean:11).
