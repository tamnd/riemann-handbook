---
title: Up-moves and the stability of lattice chains
decls:
  - GlobalTheory.LvT.Built.TrueLaws.kernelCondition_at_row_family
  - GlobalTheory.LvT.Built.Assemble.sharpBound_stability_latticeColumnChain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Up-moves and the stability of lattice chains

This section proves two results used in the [sharp column valuations](/entry/cm-theta-values/depth-valuations/#sharp-column-valuations-at-level-primes). The first is the third of the five kernel laws: the sum of a kernel over the up-moves of the target decoration is $T^{(t + 1)/2}$ times its sum over the decorations whose up-move is the source. It follows from a move relation of the normalized theta family and a counting argument for up-moves at one prime. The second is the stability theorem: for a built datum whose kernels satisfy the five laws, the chain satisfies the sharp column bound and its forms are stable under the Hecke operators.

### Decorated lattices and up-moves

Let $E$ be a CM field with complex conjugation $x \mapsto \bar x$, let $\langle\ ,\ \rangle$ be the standard Hermitian form on $E^n$, and let $S_T$ and $S_G$ be finite sets of primes of $E$. For a lattice $N \subseteq E^n$ and a prime $P$, write $N_P$ for its localization at $P$ and $N^\vee$ for its dual for $\langle\ ,\ \rangle$.

**Definition 4.11.1.** A *decorated lattice* of rank $n$ for $(S_T, S_G)$ is a triple $d = (N, f, \beta)$ with the following properties. $N \subseteq E^n$ is a lattice with $N^\vee = N$. For each $P \in S_T$, $f_P : E^n \to \mathcal{O}_E/P$ is additive and $\mathcal{O}_E$-linear on $N_P$, vanishes outside $N_P$, and is not zero on $N$. For each $w \in S_G$, $\beta_w : E^n \to (\mathcal{O}_E/w)^n$ is additive and linear on $N_w$, vanishes outside $N_w$, maps $N$ onto $(\mathcal{O}_E/w)^n$, and an element of $N$ with $\beta_w(x) = 0$ lies in $wN$.

The map $f_P$ is a level structure at $P$: a nonzero linear form on $N_P$ modulo $P$. The frames $\beta_w$ at the row primes do not move in this section.

**Definition 4.11.2.** Let $d$ be a decorated lattice, $P \in S_T$ and $q \in \mathcal{O}_E$. For $x \in N$ with $f_P(x) = 1$, put
$$A = N + P^{-1} x, \qquad N^{\uparrow} = A^\vee + \bar P A.$$
The *up-move* $d^{\uparrow} = \mathrm{up}(d, P, q, x)$ has lattice $N^{\uparrow}$, the form $f^{\uparrow}_P(y) = f_P(q y)$ for $y \in N^{\uparrow}_P$ and $f^{\uparrow}_P(y) = 0$ otherwise, and the same $f_Q$ for $Q \neq P$ and the same frames. We say that $d'$ is an *up-move of $d$ at $P$* if $d' = \mathrm{up}(d, P, q, x)$ for some such $x$.

**Definition 4.11.3.** Let $K_P(d)$ be the span of the $x \in N$ with $f_P(x) = 0$. The *down lattice* of $d$ at $P$ is $\mathrm{dn}_P(d) = K_P(d) + P\, K_P(d)^\vee$.

When $q \in P \setminus P^2$, $P \neq \bar P$, no prime of $S_T$ equals $\bar P$, and no prime of $S_G$ is $P$ or $\bar P$, the following hold. An up-move $d_1$ of $d$ at $P$ is again a decorated lattice, and $\mathrm{dn}_P(d_1) = N_d$. The index exponent $\mathrm{ord}_P \det \mathrm{dn}_P(d) - \mathrm{ord}_P \det N_d$ is $1$, and $\mathrm{dn}_P(d)$ agrees with $N_d$ at every other prime of $S_T$. We call these the *move conditions* at $P$.

### The up-move law

Fix the row data of a datum: the primes $V(\pi)$ above $T = T(u)$, the row primes $S_G$, the constants $c_A$ and $c_B$, and $S_{\mathrm{all}} = V(\pi) \cup S_G$. For lattices $N \subseteq E^a$, $N' \subseteq E^b$ and a function $\Xi$, the *kernel* is
$$\mathrm{ker}(N, N'; \Xi) = \sum_{x \in c_A^{-1} H / c_B H} \Xi(x)\, \Theta(N, N', x), \qquad H = H_{S_{\mathrm{all}}}(N, N'),$$
where $\Theta(N, N', x)$ is the theta distribution of the step at $x$, a linear map between the spaces of the two weights. We did not unfold it. The function $\Xi$ lies *in the box* for $(N, N')$ if it vanishes outside $c_A^{-1} H$ and is invariant under $c_B H$. For decorated lattices $d$, $d'$ and an off datum $\Xi_0$, the *term* is $\mathrm{term}(d, d') = \mathrm{ker}(N_d, N_{d'}; \varphi(d, d')\, \Xi_0)$, with $\varphi(d, d')$ the indicator function of the support $\overline{\Sigma}(d, d')$ of the [previous section](/entry/cm-theta-values/depth-valuations/#integral-jet-moments).

**Definition 4.11.4.** The *move step* holds at step $i$ if for self-dual $N_1, N_2 \subseteq E^{N_i}$ and $N'_1, N'_2 \subseteq E^{N_{i + 1}}$ that agree away from $T$, and $\Xi$ in the box for both pairs,
$$\mathrm{ker}(N_1, N'_1; \Xi) = s(N_1, N_2, N'_1, N'_2)\, \mathrm{ker}(N_2, N'_2; \Xi),$$
where, with $r_P(M_1, M_2) = \mathrm{ord}_P \det M_1 - \mathrm{ord}_P \det M_2$, $a = N_i$ and $b = N_{i + 1}$,
$$s = \prod_{P \in V(\pi)} \mu_P^{\,r_P(N'_1, N'_2) - r_P(N_1, N_2)}\; T^{\frac{a}{2} r_P(N'_1, N'_2) - \frac{b}{2} r_P(N_1, N_2)},$$
with the local characters $\mu_P$ of the tuple.

**Lemma 4.11.5 (up-move law for terms).** Assume the move step at step $i$, that $T$ lies in the set $S$ of the row data, and that the fields and primes satisfy their conditions. Let $d$, $d'$ be decorated lattices of ranks $N_i$ and $N_{i + 1}$, let $P \in V(\pi)$ satisfy the move conditions for both, and let $\Xi_0$ be in the box for $(N_d, N_{d'})$ with respect to $S_G$. Then
$$\sum_{d_1 \text{ up-move of } d' \text{ at } P} \mathrm{term}(d, d_1) = T^{(t + 1)/2} \sum_{d_0 :\ d \text{ up-move of } d_0 \text{ at } P} \mathrm{term}(d_0, d').$$

*Proof.* The prime $T$ lies in $P \setminus P^2$. Both sums are finite. Let $d_1$ be an up-move of $d'$. Then $\mathrm{dn}_P(d_1) = N_{d'}$, and $N_d$, $\mathrm{dn}_P(d)$ agree away from $T$, as do $N_{d_1}$, $\mathrm{dn}_P(d_1)$. Since $T$ is not a row prime, the box condition passes to both pairs. The move step gives $\mathrm{term}(d, d_1) = s \cdot \mathrm{ker}(\mathrm{dn}_P(d), N_{d'}; \varphi(d, d_1)\Xi_0)$. Here $r_P = -1$ for both pairs at $P$ and $r_Q = 0$ at the other primes, so the exponent of $\mu_P$ is $0$ and $s = T^{(b - a)/2} = T^{(t + 1)/2}$. Let $d_0$ have up-move $d$. Then $N_{d_0} = \mathrm{dn}_P(d)$, so $\mathrm{term}(d_0, d') = \mathrm{ker}(\mathrm{dn}_P(d), N_{d'}; \varphi(d_0, d')\Xi_0)$. The kernel is linear in $\Xi$. So it is enough to show, for each $x$,
$$\sum_{d_1} \varphi(d, d_1)(x) = \sum_{d_0} \varphi(d_0, d')(x).$$
At most one $d_1$ has $x \in \overline{\Sigma}(d, d_1)$, and at most one $d_0$ has $x \in \overline{\Sigma}(d_0, d')$. If such a $d_1$ exists, there is such a $d_0$, and conversely. So both sides are $0$ or both are $1$. $\square$

**Theorem 4.11.6 (kernel condition for the row family).** Let $I$ be a good true column choice with rational jets, let $l$ be laws for $I$, $Z$ later stages, $u$ a word, $a$ a tuple and $i < m$. Then the standard kernel at step $i$ of the standard built datum of $(I, l, Z, u, a)$ satisfies Law 3: for points $d$, $d'$ at steps $i$ and $i + 1$, every prime $P$ of $S_T$ and every vector $F$,
$$\sum_{d_1 \text{ above } d' \text{ at } P} k(d, d_1) F = T^{(t + 1)/2} \sum_{d_0 \text{ below } d \text{ at } P} k(d_0, d') F.$$

Lean: `GlobalTheory.LvT.Built.TrueLaws.kernelCondition_at_row_family`.

*Proof.* Step 1. The goodness of $I$ gives the analytic hypotheses of the row: a curve ideal, a twelfth root and an admissible character. They give the equivariance laws of the normalized theta family, the lattice property of its vectors, and the theta condition at $0$ in all even ranks. With the rational jets of $I$, the move relation of the family gives the move step at step $i$.

Step 2. The lemma above turns the move step into the up-move law for terms.

Step 3. At each pair of points the standard kernel at step $i$ is a term for some off datum in the box. Every prime of $V(\pi)$ satisfies the move conditions, and the points above and below in the built datum are the up-moves of the decorations. So the up-move law for terms is Law 3. $\square$

### The stability theorem

A built datum $B$ over $D$ with word $u$ has a chain with forms $F_i$ at each step, Hecke operators $U_v$ at the primes $v$ above $T$, and a map $K_T$ from step $i$ to step $i + 1$. The chain has *weight signs* if the top shift $b_\tau$ is $\geq 0$ at each top embedding and the divisor shifts $s_i(\tau)$ are $\geq 0$ for all $i < m$ and all $\tau$. The forms are *stable* if, for each $i \leq m$, each $U_v$ maps $F_i$ into itself, the $U_v$ commute on $F_i$, and $K_T$ maps $F_i$ into $F_{i + 1}$ for $i < m$.

**Theorem 4.11.7 (stability of lattice chains).** Let $B$ be a built datum over $D$ with word $u$. Assume:

1. for each $i \leq m$ the points at step $i$ split over $T$;
2. $B$ sees the places;
3. for each $i < m$ there is a kernel at step $i$ that satisfies the five laws;
4. $[E : \mathbb{Q}]\, N_m + 1 < T$;
5. the chain of $B$ has weight signs.

Then the chain satisfies the sharp column bound, and its forms are stable.

Lean: `GlobalTheory.LvT.Built.Assemble.sharpBound_stability_latticeColumnChain`.

*Proof.* Step 1 (point models). For each $i \leq m$ the splitting gives a point model of the chain at level $i$ with a realisation by the points of $B$.

Step 2 (coordinates). For each $i \leq m$ there are good coordinates on the point model whose value lattices at each place $w$ over $T$ are the lattices of the chain. This step uses that $B$ sees the places.

Step 3 (point kernels). For each $i < m$, the kernel of hypothesis 3 is realised by a point kernel between the models at $i$ and $i + 1$ with the correct target.

Step 4 (laws for the point kernels). Each law of the kernel passes to the point kernel: the dilation law, the up-move law, the bound at the places that are not seen, and the bound at the seen places. The last two use the coordinates of Step 2.

Step 5 (stability). The correct target gives the stability of the forms. The up-move law for the point kernels gives $U_v K_T = T^{(t + 1)/2} K_T U_v$ on $F_i$.

Step 6 (stabilizers and weights). By hypothesis 4, $T$ does not divide the order of any stabilizer of the chain. The weight signs give the weight bounds: $s_i(\tau)$ lies between $0$ and the weight $W_\tau$, and the determinant shift of the weight at level $i + 1$ is $-s_i(\tau)$.

Step 7 (the sharp bound). From the laws, the stabilizers and the weight bounds, at each place $w$ over $T$ the map $T^{E(w)} U_w K_T$ sends the lattice at step $i$ into the lattice at step $i + 1$, where $E(w) = 2 \sum_\tau W_\tau + f N_m$ if $w$ is seen and $0$ otherwise. Iterating over the $m$ steps, with the commutation of Step 5 and the stability, gives the sharp column bound. $\square$

**Remark 4.11.8 (Formalization).** The kernel condition uses all its hypotheses. The move relation of the family discards the twelfth root among the analytic hypotheses ([MoveStepOfFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MoveStepOfFamily.lean#L132)). The proof of the stability theorem copies the hypothesis on kernels and then uses only the copy ([SharpBoundStabilityLatticeColumnChain.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SharpBoundStabilityLatticeColumnChain.lean#L33)). Steps 5 to 7 repeat the body of [LevelChainSharpColumnValuationOfPointKernelLiftL.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LevelChainSharpColumnValuationOfPointKernelLiftL.lean#L21), which the file imports but does not call, because that lemma returns only the sharp bound. We did not unfold the theta distribution, the splitting, the sight condition, the point models or the coordinates, and we used the statements of the lemmas of Steps 1 to 4 and 7 without reading their proofs.
