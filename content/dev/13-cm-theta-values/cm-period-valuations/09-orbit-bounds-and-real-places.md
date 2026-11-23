---
title: Orbit bounds and the real places
decls:
  - GlobalTheory.KerGaussA.kernel_bound
  - GlobalTheory.KerGaussA.kvalGe_gainA
  - GlobalTheory.T.kvalGe_orbitGainWithoutOperator
  - GlobalTheory.OrbitBoundStdRec.orbit_bound_rec
  - GlobalTheory.T.orbitBound_standardSeries_inertPlaces
  - GlobalTheory.Ggeo.frobeniusConjugation_conditions_adaptedKernelDatum_alt
  - GlobalTheory.T.frobeniusConjugation_conditions_adaptedKernelDatum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbit bounds and the real places

This section proves two of the local parts of the kernel condition. The first is the *orbit bound*: at an inert prime $l$, every theta series of the right shape has coefficients divisible by a power of $l$ that grows with the orbit of a Young diagram. The second is the pair of *even conditions*: at an inert prime where the theta series of the kernel entry is a standard series, it has a product form over the real places. Both are used in [the kernel condition over true columns](/entry/at-of-true-columns/).

### Local orbit data

Let $l$ be a prime and $\mathbb{C}_l$ the completion of an algebraic closure of $\mathbb{Q}_l$. Write $K^{\mathrm{ur}}$ for the maximal unramified extension of $\mathbb{Q}_l$ in $\mathbb{C}_l$.

**Definition 5.9.1 (Local orbit datum).** A *local orbit datum* $\Lambda$ consists of a prime $l$, an even number $d$, ranks $N_0 < N_1$, a power series $\Theta$ over $\mathbb{C}_l$ in variables indexed by $\mathbb{Z}/d \times \{1, \dots, N_0\} \times \{1, \dots, N_1\}$, Young diagrams $\nu_s$ for $s \in \mathbb{Z}/d$ with at most $N_0$ rows, and a finite set $T \subseteq \mathbb{Z}/d$. For $s \in \mathbb{Z}/d$ the *cap* is $\mathrm{cap}(s) = \nu_s(1)$, the length of the second row, if $s \in T$, and $\nu_s(0)$, the length of the first row, otherwise. The *size* of $s$ is the number of cells of $\nu_s$, and

$$
\alpha(s) = \begin{cases} \nu_s(0) - \nu_s(1) & s \in T,\\ 0 & s \notin T. \end{cases}
$$

The number $\alpha(s)$ is the number of columns of height one of $\nu_s$ when $s \in T$.

**Definition 5.9.2 (Valuation bound).** Let $\Lambda$ be a local orbit datum and $B \in \mathbb{R}$. The series $\Theta$ has *valuation at least* $B$ along $\nu$ if for every choice $I$ of columns for the diagrams $\nu$ and every monomial $m$, the coefficient of $m$ in the polynomial $G_{\nu, I}\Theta$ has norm at most $l^{-B}$. Here $G_{\nu, I}\Theta$ is the result of a differential operator attached to $(\nu, I)$, evaluated at $0$, with the coefficients of $\Theta$ weighted by factorials. We write $\mathrm{Kv}(\Theta) \ge B$.

**Definition 5.9.3 (Orbit gain).** The *orbit gain* of $\Lambda$ is

$$
\begin{aligned}
g_A(\Lambda) = {}& \sum_{s \in T} \sum_{e} \max\Big(\frac{\alpha(s)}{l^{e}} - \mathrm{cap}(s + e),\, 0\Big)\\
&- \sum_{s \in \mathbb{Z}/d} \Big(N_1\, \lambda(\alpha(s)) + N_0 N_1\, \lambda(\mathrm{size}(s) - \alpha(s))\Big) - \sum_{s \in T} \lambda(\alpha(s))^2,
\end{aligned}
$$

where the inner sum runs over odd $e \ge 1$ such that $e \ge d$ or $s + e \notin T$, and $\lambda = \lambda_l$ is a logarithmic loss function of $l$.

The first sum is the gain: the columns of height one at $s$ carry a factor of $l$ that survives the shift by an odd $e$ when the shifted class has a smaller cap. The other sums are the losses.

**Definition 5.9.4 (Standard exponent).** A series $\beta$ in variables indexed by $\mathbb{Z}/d$ is a *standard exponent* if there are a Frobenius automorphism $\sigma$ of $K^{\mathrm{ur}}$, a law of logarithm $F$, a series $\beta_0$ in two variables, two families $\omega, \omega^*$ of $d/2$ elements and a primitive $(l^d - 1)$-th root of unity $\zeta$ in $K^{\mathrm{ur}}$, with the conditions of a Lubin-Tate type datum on $(\sigma, F, \beta_0, \omega, \omega^*)$, such that $\beta$ is built from $(\sigma, \beta_0, \omega, \omega^*, \zeta)$.

**Definition 5.9.5 (Orbit theta expansion).** Let $\varepsilon \in \mathbb{C}_l$, $s_g \in \mathbb{C}_l$ and $\beta$ a family of series. The series $\Theta$ of $\Lambda$ has an *orbit theta expansion* with $(\varepsilon, s_g, \beta)$ if there is a series $U$ with all coefficients of norm at most $1$ such that the series $\Theta_\varepsilon$ built from $\Theta$ and $\varepsilon$ equals $U$ times the exponential of $s_g \sum \beta$, with the jet logarithm substituted for the variables.

### The kernel bound and the orbit gain

**Theorem 5.9.6 (Kernel bound).** Let $l$ be a prime, $\nu \ge 1$, and $N_0, N_1 \ge 0$. Let $\sigma$ be a Frobenius automorphism of $K^{\mathrm{ur}}$, $F$ a law of logarithm, $\beta_0$ a series in two variables with the two conditions on $(F, \beta_0)$ and $(\sigma, \beta_0)$, and $\omega, \omega^*$ two families of $\nu$ elements that satisfy the orbit condition and the trace duality for $2\nu$. Let $U_0$ be an integral series. Let $T \subseteq \mathbb{Z}/2\nu$, and let column data $(c_s, h_s, I)$ be given with heights $h_s \le N_0$. Then every coefficient of the frame jet of the theta series of $\exp(-\sum \beta_0)\, U_0$ has norm at most $l^{-g}$, where $g$ is the excess gain of $(l, T)$ for the heights, the caps and the losses of the column data.

Lean: `GlobalTheory.KerGaussA.kernel_bound`

*Proof.* The field $K^{\mathrm{ur}}$ is complete for its norm. The constant term of $\beta_0$ is $0$ by the first condition on $(F, \beta_0)$, so the constant term of $\sum \beta_0$ is $0$. The field $K^{\mathrm{ur}}$ contains a primitive $(l^2 - 1)$-th root of unity and an element $\varpi$ with $\varpi^{l^2 - 1} = l$. With these inputs the claim is a kernel estimate for laws of logarithm, proved outside this chapter. $\square$

**Theorem 5.9.7 (Orbit gain bound).** Let $\Lambda$ be a local orbit datum, $\varepsilon \in \mathbb{C}_l$ with $|\varepsilon| = 1$, and $\beta$ a standard exponent. Assume that $\Theta$ has an orbit theta expansion with $(\varepsilon, -1, \beta)$. Then $\mathrm{Kv}(\Theta) \ge g_A(\Lambda)$.

Lean: `GlobalTheory.KerGaussA.kvalGe_gainA` (also `GlobalTheory.T.kvalGe_orbitGainWithoutOperator`, a second name)

*Proof.* A lemma on integral orbit series turns the orbit theta expansion into the form $\Theta = $ theta series of $\exp(-\sum \beta_0)\, U_0$ with $U_0$ integral. Reading the diagrams $\nu_s$ as column data, the kernel bound applies with $d = 2\nu$. The number of columns of height one at $s \in T$ is $\nu_s(0) - \nu_s(1)$. So the heights of the column data give $\alpha$, the caps give $\mathrm{cap}$, the loss set gives $\mathrm{size} - \alpha$, and the excess gain is $g_A(\Lambda)$. $\square$

### The orbit bound at inert places

Each prime $p$ has a class for $D$: inert, signal or other. We write $h_P(p)$ for the image in a finite abelian group $H_D$ of a chosen Frobenius element at $p$ in the Galois group of $E$. For $p$ not of signal class, the *degree* $n_P(p)$ is the order of $h_P(p)$. The *evenness condition* at $p$ says that this order is even. The *class condition* $C_s$ at $p$ says that $p$ is of inert class, that the order of $h_P(p)$ is odd, and that $h_P(p) \ne 0$. We write $X''$ for the prime bound of the size data.

Let $\mathrm{Ee}$ be an entry of orbit data for $D$: rows of diagrams $\nu$, numbers $\varepsilon_w$, series $\beta_w$ and signs $s_g$ at each place $w$. The entry has the *shape* if its diagrams fit the size data; this condition is not unfolded here. A family $(\varepsilon, \beta)$ is a *standard family* if at every place $w$ whose residue characteristic is of inert class with the evenness condition, or of signal class, we have $|\varepsilon_w| = 1$ and every $\beta_w(r)$ is a standard exponent.

**Definition 5.9.8 (Orbit bound).** The entry $\mathrm{Ee}$ satisfies the *orbit bound* for the constants $K$ if for every place $w$ whose residue characteristic $p$ satisfies the orbit condition and is of inert class, with $h_P(p) \ne 0$ and $p \le X''$, every word $u$, every $i < m$ and every representative $t_0$ of the places over $p$, the following holds. For every series $\Theta$ with an orbit theta expansion at the local orbit datum of $(w, u, i, t_0)$, we have

$$
\mathrm{Kv}(\Theta) \ge \max\big(g_0(p, i + 1, t_0),\, 0\big),
$$

where $g_0$ is the word-free orbit number for the constants.

**Theorem 5.9.9 (Orbit bound for standard series).** Let $\mathrm{Ee}$ be an entry with the shape. Assume that the row differences satisfy $\nu_{u, i}(t)(0) - \nu_{u, i}(t)(1) \le 2a$ for all $u$, $i < m$ and $t \in T$, that $\delta_1 \ge 5$ and $\delta_2 \ge 4$, that $(\varepsilon, \beta)$ is a standard family, and that all signs are $-1$. Then $\mathrm{Ee}$ satisfies the orbit bound.

Lean: `GlobalTheory.OrbitBoundStdRec.orbit_bound_rec` (also `GlobalTheory.T.orbitBound_standardSeries_inertPlaces`, a second name)

*Proof.* Fix $w$, $u$, $i$, $t_0$ and $\Theta$ as in the definition. A prime of inert class is not of signal class, so the evenness condition holds at $p$. Then the standard family gives $|\varepsilon_w| = 1$ and a standard exponent. A lemma on standard orbit series gives $\mathrm{Kv}(\Theta) \ge 0$. The orbit gain bound gives $\mathrm{Kv}(\Theta) \ge g_A$. A counting lemma gives $g_0 \le g_A$; it uses the shape, the row differences and the bounds on $\delta_1$ and $\delta_2$. If $g_0 \le 0$ we use the first bound. Otherwise the valuation bound is monotone in $B$, and $g_0 \le g_A$ gives the claim. $\square$

### The even conditions

For a prime $p$ of inert class and a place $w$ over $p$, the series of the kernel entry at $(u, \mu, w, i, c, c')$ is $\Theta_{u, \mu, w, i, c, c'}$. A series $\Theta$ has the *real place expansion* if it is a unit times an exponential of standard data with $d = 2$, with signs $\pm 1$. It has the *theta product form* if it is a product over the real places in the sense of the theta product theorem.

**Definition 5.9.10 (Even conditions).** The *even conditions* for an entry and divisor data say:
1. at every place $w$ free of the level, whose prime $p$ is of inert class with $h_P(p) = 0$, and for every $i < m$ with $N(i) N(i+1)$ even, every series of the entry at $(w, i)$ has the real place expansion;
2. at every place $w$ free of the level whose prime $p$ satisfies the class condition $C_s$, and for every $i < m$ with $N(i) N(i+1)$ even, every series of the entry at $(w, i)$ has the theta product form.

The *host hypothesis* says: for every datum $D$, every curve ideal $\mathfrak{c}$, every twelfth root $\delta$ of its discriminant, every base $B$, every character $\chi$, every prime $p \ge 5$ of inert class or of signal class, and every embedding $\lambda$ of $\overline{\mathbb{Q}}$ into $\mathbb{C}_p$, the host condition holds for $(B, \chi, p, \lambda)$.

**Theorem 5.9.11 (Even conditions for adapted entries).** Assume algebraic torsion and the host hypothesis. Let $t$ be a tied kernel entry for $\mathrm{ex}$ that satisfies the kernel hypotheses and has adapted bases, and assume $3 \le$ the split bound of $D$. Then for all $\varepsilon$, $\beta$ and $s_g$ the orbit entry of $t$ with $(\varepsilon, \beta, s_g)$ satisfies the even conditions.

Lean: `GlobalTheory.Ggeo.frobeniusConjugation_conditions_adaptedKernelDatum_alt` (also `GlobalTheory.T.frobeniusConjugation_conditions_adaptedKernelDatum`, a second name)

*Proof.* The main step is a reduction. Fix $(u, \mu, w)$ with $w$ free of the level and $p$ of inert class, and $i < m$. Let $\mathcal{Q}$ be a property of series. Suppose $\mathcal{Q}$ holds for every standard series $\mathrm{std}(P, P', G)$, where $P, P'$ are standard bases of admitted lattices $L, L'$ at the levels $i$ and $i + 1$ and $G$ is a combination, whenever the host condition holds and $p \ge 5$. Then $\mathcal{Q}$ holds for $\Theta_{u, \mu, w, i, c, c'}$. To see this, note first that $p \ge 5$, because the split bound is at least $3$ and $p$ is of inert class. The adapted bases give matrices $P_m$ with the conjugation property and an expression of $\Theta$ through them. Algebraic torsion and the kernel hypotheses give that the lattices of $t$ are admitted and that the coefficients form a combination. The host hypothesis gives the host condition. The adapted bases are standard bases of the lattices at $w$, and the adapted expression of $\Theta$ is the standard series. So $\mathcal{Q}(\Theta)$ holds.

For condition 1 we take $\mathcal{Q}$ = real place expansion. The standard series has it when $h_P(p) = 0$, by a lemma on standard series of admitted lattices. For condition 2 we take $\mathcal{Q}$ = theta product form. By the class condition, $p$ is of inert class and the degree $n_P(p)$ is odd. Then [the theorem on lattice pairs of odd degree](/entry/lattice-pairs-odd-degree-isometric/) gives the theta product form. $\square$

**Remark 5.9.12 (Formalization).** Several facts about the Lean code:
1. The names with prefix `GlobalTheory.T.` are second names, proved by `first | exact @… | …` under `maxHeartbeats 1000000`.
2. In `GlobalTheory.Ggeo.frobeniusConjugation_conditions_adaptedKernelDatum_alt` the numbers `ep`, `be` and `sg` are quantified but play no role: the even conditions only read the series `t.ent.Th`. The evenness of $N(i)N(i+1)$ is also not used; it is discarded with `_` (FrobeniusConjugationConditionsAdaptedKernelDatum.lean:50). The name speaks of "Frobenius conjugation", which is only the conjugation property of the adapted bases.
3. In `OrbitPlaces.EvenConditionsAtC` (OrbitPlaces.lean:309) the condition "of inert class" is the predicate `IsResidueClassZero`. The element $h_P(p)$ is `hP`, defined with `Classical.epsilon` as some Frobenius element at $p$ (Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean:97). The predicates `HostAt`, `HasThetaProductForm`, `Shape`, the operator `Gxz`, the loss function `lgN` and the conditions `F1`, `F2`, `OwOK`, `TrDual` and `IsLawOfLog` are not unfolded here.
4. `GlobalTheory.KerGaussA.kernel_bound` is proved by one call to `Formalism.L2.Th1.D.kernelOfF`, which is not in this chapter. The hypothesis $m = \nu$ is a renaming.
5. The orbit gain `gainA` is in BeData.lean:55, and the standard family `BeFam` at BeData.lean:29. The valuation bound `KvalGe` is at ProductZerothFirstParts.lean:99, and two further copies of `KvalGe` exist in Formalism/PeriodIntegrals (EntAtD.lean:43, OrbJetBase.lean:102).
