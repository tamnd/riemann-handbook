---
title: Cuspidal lifts along the grid and core chains
decls:
  - GlobalTheory.PairLift.liftsCuspidal_of_functoriality
  - GlobalTheory.PairLift.liftsCuspidal
  - GlobalTheory.PairLift.cuspAlong_of_pairLifts
  - GlobalTheory.T.core_chain_composites_exist_lift_combinations
  - GlobalTheory.ChainLifts.chainEx
  - GlobalTheory.T.core_chain_pre_steps_exist_of_depth_congruence
  - GlobalTheory.CoreOnto.PreSteps.preOK
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cuspidal lifts along the grid and core chains

This section proves two facts about the test grid of [the previous section](/entry/exists-grid-pre/). First, each arrow of a valid grid lifts cusp forms of the given discrete series type to cusp forms, and the lift is the real intertwiner of the arrow. Second, along the core nodes $P_0, \dots, P_m$, the $K$-finite vectors at $P_0$ are reached from each later core node by composites of theta lifts with depth vectors. The first fact feeds [the cuspidality of theta pair lifts](/entry/theta-pair-lift-cuspidal-of-hypotheses/). The second feeds [the surjectivity of the twisted core](/entry/twist-core-surjective-of-local-components/). For the background see [the global theta lift](/learn/theta/#the-global-theta-lift) and [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms).

### Lifting cusp forms along an arrow

Let $N$ be a node of a grid, with Hermitian space $V_N$ and discrete series parameter $S_N$. A function $\phi$ on $U(V_N)(\mathbb{A})$ is a *cusp form of type $N$* if it is a smooth automorphic function, a [cusp form](/learn/automorphic-forms/#constant-terms-and-cusp-forms), and of type $S_N(\tau)$ at each real place $\tau$. Let $\mathcal{C}(N)$ be the space of continuous equivariant maps $F$ from the smooth vectors of the model of $N$ to cusp forms of type $N$.

**Definition 8.8.1 (Multiplicative lift).** Let $A$ and $B$ be nodes, let $\nu$ be a Haar measure on $U(V_A)(\mathbb{A})$ with a fundamental domain $\mathcal{F}$, let $K_p(h, g)$ be a kernel for each $p$ in an index set, and let $I_p$ be maps from the smooth vectors of $A$ to those of $B$. The kernel $K$ *lifts along $I$* if for each $F \in \mathcal{C}(A)$ there is $F' \in \mathcal{C}(B)$ such that for all $p$, all smooth vectors $v$ and all $h$, the function $g \mapsto K_p(h, g) F(v)(g)$ is integrable on $\mathcal{F}$ and

$$\int_{\mathcal{F}} K_p(h, g)\, F(v)(g)\, d\nu(g) = F'(I_p v)(h).$$

Let $G$ be a valid test grid. For an arrow with Weil representation $\omega$ and a finite vector $f$, let $f_p$ be the Fock polynomial vector of $f$ and the polynomial $p$, and let $\theta(h, g; f_p) = \omega(g, h) f_p(0)$ be the theta kernel. The grid *lifts cusp forms* if:

1. for each type $t$ and each vertical arrow from $V_{i+1,j}$ to $V_{i,j}$, the theta kernel lifts from $V_{i,j}$ to $V_{i+1,j}$ along the intertwiner of the arrow;
2. for each row arrow from $V_{i,j}$ to $V_{i,j+1}$, the theta kernel lifts from $V_{i,j+1}$ to $V_{i,j}$;
3. for each down arrow from $P_{i+1}$ to $P_i$, the complex conjugate of the theta kernel lifts from $P_i$ to $P_{i+1}$ along the adjoint intertwiner, and the theta kernel with the arguments exchanged lifts from $P_{i+1}$ to $P_i$;
4. for each column arrow from $X_j$ to $X_{j+1}$, the theta kernel with the arguments exchanged lifts from $X_j$ to $X_{j+1}$.

Here each lift uses the measure of the source node of the integral. The size bounds of the host say that $r > 1800$ and that $2N^3$ is less than each gap $b_{j+1} - b_j$ of the Harish-Chandra parameters at each real place.

A *pair lift* statement for a parameter rule $X$ says: for discrete series models $M$ of $V$ and $M'$ of $W$ whose parameters satisfy the rule $X$ at each real place, for each Weil representation $\omega$ with the matching exponents, each vacuum $f_0$ and each nonzero real intertwiner $I$ of the pure tensors of $f_0$, each Haar measure on $U(W)(\mathbb{A})$ with a fundamental domain, and each finite vector $f$, the theta kernel of the pure tensors of $f$ lifts from $M'$ to $M$ along $I$.

**Theorem 8.8.2 (Cuspidal lifts from pair lifts).** Let $X$ be a parameter rule that satisfies the archimedean Rallis conditions on the up and down line, the fourth condition and the fifth condition. Assume the pair lift statement for $X$ and the size bounds. Let $R$ be a record with a row base, and let $G$ be a valid test grid for $R$. Then $G$ lifts cusp forms.

Lean: `GlobalTheory.PairLift.cuspAlong_of_pairLifts`.

*Proof.* The Rallis conditions turn the pair rule into the parameter rule of the arrows. Then treat each kind of arrow.

1. For a vertical arrow, transport the model of $V_{i+1,j}$ to the negated space. The parameters of the two ends correspond by the contragredient rule for an arrow that adds a block. The exponents of the characters are $\chi_{m-i}$ against the half exponent of $\eta$. The pair lift statement, applied in the source direction, gives the lift.
2. For a row arrow the models need no transport, and the contragredient rule is the rule for an arrow that removes a block. The characters are $\mu_{t,j+1}$.
3. For the up direction of a down arrow, transport both models by complex conjugation, and use that the adjoint of a real intertwiner is a real intertwiner. For the down direction, apply the pair lift statement in the target direction.
4. For a column arrow, transport both models by conjugation and use the rule for the last row arrows.

In each case the Haar measure of the node comes from the validity of $G$ and the row base. $\square$

**Theorem 8.8.3 (Cuspidal lifts from the discrete series inputs).** Let $X$ be a chosen series that satisfies the three Rallis conditions. Assume the published result on Harish-Chandra modules and the rapid decay of cusp forms. Assume for each host that the models are cover series, that the vacuum has the vacuum character, the Lie and compact Fock rules, the density of Fock vectors, the rapid decay lift properties, the tower constant term formula and the $K$-type extension. Then each valid test grid for a record with a row base lifts cusp forms, for each host that satisfies the size bounds.

Lean: `GlobalTheory.PairLift.liftsCuspidal`.

*Proof.* The lower tower lifts vanish on Fock vectors, so they vanish. By the tower constant term formula, the theta lifts are then cuspidal, and the pair theta lift factors through the intertwiner. This gives the pair lift statement for $X$. Apply the previous theorem. $\square$

**Theorem 8.8.4 (Cuspidal lifts from the published results).** Assume the published results on discrete series covers, on Harish-Chandra modules, on the rapid decay of cusp forms and the theorem of Casselman and Wallach. Then each valid test grid for a record with a row base lifts cusp forms, for each host that satisfies the size bounds.

Lean: `GlobalTheory.PairLift.liftsCuspidal_of_functoriality`.

*Proof.* The published results give real discrete series data $X$ with the three Rallis conditions. For each host, they also give the analytic theta pair hypotheses: the cover series bridge, the vacuum character, the Lie and compact Fock rules, the density, the lift laws, the constant term formula and the $K$-type extension. This is the previous theorem applied to these data. $\square$

### Core chains

Now fix a host off the auxiliary primes that satisfies the size bounds, a level character, a scale with gap constant $1$, grid data with a Weil family $W$, and row volumes. For each core node $P_i$ fix a volume datum $v_i$, a Haar measure with a fundamental domain $\mathcal{F}_i$. A *core lattice* at $P_i$ is a relattice of $V_{P_i}$ whose frame lattice is the scaled lattice $(\mathfrak{a}\bar{\mathfrak{a}}^{-1})^{i}\Lambda_{P_i}$, where $\mathfrak{a}$ is the polarisation ideal of the host. A core lattice and a discrete series model give a *stage*: a space, a model, a level group, a measure and a fundamental domain.

**Definition 8.8.5 (Down operator and reach).** For $i < m$, a Schwartz function $f$ on the symplectic space of the down arrow at $i$ and a function $F$ on $U(V_{P_{i+1}})(\mathbb{A})$, put

$$\mathrm{dn}_i(f, F)(g) = \int_{\mathcal{F}_{i+1}} K_i(f; h, g)\, F(h)\, d\nu_{i+1}(h),$$

where $K_i(f)$ is the kernel of $W$ at the down arrow. For $F$ on $P_k$, the set $\mathrm{Below}_k(F)$ consists of the functions $F_0$ on $P_0$ for which there are functions $\Psi_i$ on $P_i$ with:

1. $\Psi_i$ is rapidly decreasing for $i \le k$;
2. for each $i < k$ there is a depth vector $f$ at the core arrow $i$ with $\Psi_i = \mathrm{dn}_i(f, \Psi_{i+1})$;
3. $\Psi_0 = F_0$ and $\Psi_k = F$.

**Definition 8.8.6 (Depth fixed).** The *depth fixed* hypothesis says: for each host off the auxiliary primes and each grid, for each $i < m$ and for the pairs $p$ at the vertex $(i, 0)$ and at the core node $P_i$, each depth vector $f$ of $p$ is fixed by $\omega_p(k, k')$ for all $k$ and $k'$ in the level groups of the two ends of $p$.

**Theorem 8.8.7 (Pre-steps of the core chain).** Assume the depth fixed hypothesis. Let $i < m$, let $r$ and $r'$ be core lattices at $P_i$ and $P_{i+1}$, and fix volume data and models. Then there are a Weil representation $\omega$ and a vector $f$ such that:

1. $\omega$ is a Weil representation of the stages for the characters of the core arrow, the real parameters of the two stages correspond for the up pair with the centre $-c_{m-i}$, $f$ is a vacuum vector, and $f$ is spherical outside the set $S_0$;
2. the level groups of both stages fix the exchanged pure tensors of $f$ under $\omega$;
3. if the matrix coefficient of $g$ against an exchanged pure tensor is nonzero, and $g$ stabilizes the lattice outside $S_0$, then the finite part of $g$ lies in the level congruence group up to a real factor;
4. $\omega$ exchanges with the Weil representation of $W$ at the core arrow, and for each polynomial the exchanged pure tensor of $f$ is a depth vector.

Lean: `GlobalTheory.T.core_chain_pre_steps_exist_of_depth_congruence` (also `GlobalTheory.CoreOnto.PreSteps.preOK`, the proof).

*Proof.* The exchange laws of the theta Heisenberg operators move the Weil representation of $W$ at the core arrow to a Weil representation $\omega$ of the stages. A lattice homomorphism that is onto modulo the depth ideal gives a coset Fock vacuum datum $f$, which is a vacuum, spherical off $S_0$, and whose exchanged pure tensors are depth vectors. The real parameters correspond by the core chain parameter rule. For clause 2, the depth fixed hypothesis fixes the depth vectors under the level, and the exchange map is injective. For clause 3, the coefficient is a coefficient of $W$ by the measure law, the twisted lattice has the same stabilizers as $\Lambda_{P_i}$, and a coset supported coefficient is supported on the congruence group. Split $g$ into a real part and a finite part. $\square$

**Theorem 8.8.8 (Composites of the core chain reach the bottom).** Assume the published results on discrete series covers, on Harish-Chandra modules, on the rapid decay of cusp forms and the theorem of Casselman and Wallach. Assume the depth fixed hypothesis, and assume that each core node has a discrete series model with the Cartan data of $W$. Fix volume data, a core lattice $r_0$ at $P_0$ and a model $M_0$. Then for each $k \le m$ there are a core lattice $r$ and a model $M$ at $P_k$ and a reach map $\Theta$ from the stage at $P_k$ to the stage at $P_0$ along $k$ steps, such that for each $y$ and each $K$-finite vector $x$ at $P_0$, $\Theta(y)(x)$ lies in the span of the sets $\mathrm{Below}_k(y(w))$.

Lean: `GlobalTheory.T.core_chain_composites_exist_lift_combinations` (also `GlobalTheory.ChainLifts.chainEx`, the proof).

*Proof.* Induct on $k$. For $k = 0$ take $r_0$, $M_0$, the identity map and $\Psi_0 = y(x)$, which is rapidly decreasing by the Hecke conjugation bound. For the step from $k$ to $k + 1$, the pre-step theorem gives a Weil representation and a vacuum. The even rank theta chain extends the Weil datum to a step, and the step gives a new reach map. The $K$-finite vectors of the stage at $P_k$ lie in the span of the images of the intertwiner of the step. A chain for $\mathrm{dn}_k(f, F)$ at level $k$ extends to a chain for $F$ at level $k + 1$ by appending $F$. Composing the index maps gives the claim at $k + 1$. $\square$

**Remark 8.8.9 (Formalization).** The three cuspidal lift theorems are in [CuspAlongOfPairLifts.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/CuspAlongOfPairLifts.lean#L419) and [LiftsCuspidalOfFunctoriality.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/LiftsCuspidalOfFunctoriality.lean#L10). The core chain theorems are in [CoreChainCompositesExistLiftCombinations.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/CoreChainCompositesExistLiftCombinations.lean#L36) and [CoreChainPreStepsExistOfDepthCongruence.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/CoreChainPreStepsExistOfDepthCongruence.lean#L35). The pre-step theorem discards two of the six exchange laws it obtains. We have not unfolded the pair lift statement, the Rallis conditions, the pre-step clauses, the reach relation, the depth vectors, the exchange relation or the auxiliary prime conditions.
