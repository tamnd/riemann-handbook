---
title: Sharp column valuations at level primes
decls:
  - GlobalTheory.T.kernelJets_levelPlace_integralMoments
  - GlobalTheory.LvT.Built.TrueLaws.laws_true_fam
  - GlobalTheory.T.fivePointLaws_trueChains
  - GlobalTheory.LvT.Built.TrueCols.trueColumns_chain_last_step_sharp_bound
  - GlobalTheory.LvT.Built.TrueCols.row_true
  - GlobalTheory.T.trueColumns_row_sharp_bounds
  - GlobalTheory.LvT.Built.TrueCols.closing_true_cols
  - GlobalTheory.Fc.Cv.row_level_valuations
  - GlobalTheory.T.levelPrimeColumnValuations_bundlePoints_overColumns
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sharp column valuations at level primes

This section proves a sharp lower bound for the valuations of the column map of a lattice chain at the places over a level prime $T_u$. The chain comes from a true column choice, and the bound holds for the chain of the datum and for the twisted chain of every tuple. The proof checks five laws for kernels between consecutive steps of the chain and then applies a stability theorem for lattice chains. The integral moments of jets give the two analytic laws. The result is the last of the six rows at a member in Volume 15 ([six rows at a member](/entry/six-rows-at-member-alt/)). That row fills one field of [the alternative hypotheses](/step/hyps-alt-def/), in Branch 2 of [the unitary hypotheses](/proof/unitary-hypotheses/).

### True column choices and their chains

We use the twisting data of the earlier chapters of this volume without repeating their construction. A *base* $B$ has ranks $m$, $f$ and $N_0, \dots, N_m$, a CM field $E$ with $[E : \mathbb{Q}] = 2f$, and a field $L$ with places $w$. A *true column choice* $I$ over $B$ has a Hecke frame, characters, a set of primes, and a finite set of tuples with a reference tuple $\mu_0$ and a Hecke character for each tuple. It is *good* if six conditions on its spaces, characters and primes hold, and it has *rational jets* if the jets of the given degree are rational. The base has *correct signs* if, at each top embedding, the last entry $u_{k - 1}$ of the Hodge parameter is at most $-(k - 1)/2$, and at each embedding the first entry $e_0$ is at least $k/2$.

Let $l$ be laws for $I$, let $l_0$ be a law at step $0$, and let $Z$ be a choice of the five later stages. They assemble a datum $D$ and a family of twisted forms of $D$. For a word $u$, $D$ has a column chain with lattices $\Lambda_0, \dots, \Lambda_m$ and a column map $\mathrm{col}$ from step $0$ to step $m$. Each tuple $\mu$ has its own twisted chain, with lattices $\Lambda_i^\mu$, column map $\mathrm{col}_\mu$ and an isomorphism $e_\mu$ at step $0$. The twisted chain at $\mu_0$ is the chain of $D$.

For a place $w$ over $T_u$ let $e_w$ be its ramification index. Let $E_T(w)$ be $0$ if $w$ is not seen by the forms, and $2 \sum_\tau W_\tau + f N_m + |\mathrm{tops}| (t + 1)(m + 1)/4$ otherwise, with the weights $W_\tau$ and the set of top embeddings of the datum. Let $N_\lambda(w)$ be the image of the $w$-part of $\Lambda_0$ under $T_u^e U_w^m$, where $U_w$ is a product of Hecke operators at $w$.

**Definition 4.7.1.** A chain satisfies the *sharp column bound* at $u$ if for each place $w$ over $T_u$ and each $c \in L$ with $v_w(c) \geq e_w\, m\, E_T(w)$, the map $\varphi \mapsto c \cdot \mathrm{col}(\varphi)$ sends $N_\lambda(w)$ into the $w$-part of $\Lambda_m$.

### The five kernel laws

A *built datum* over $D$ is a number field with an involution, embeddings into $L$, and a decorated chain of lattices with steps $0, \dots, m$. A *kernel* at step $i$ gives, for each pair $(d, d')$ of points at steps $i$ and $i + 1$, a linear map $k(d, d') : V_i \to V_{i + 1}$. The five laws are as follows.
1. Equivariance: $k(g d, g' d') = \rho_{i + 1}(g') \circ k(d, d') \circ \rho_i(g)^{-1}$, and $k$ matches the kernel map of the chain.
2. Dilation: $k$ is invariant under the diamond moves at each prime $P$.
3. Up-moves: the sum of $k(d, d_1)$ over the up-moves $d_1$ of $d'$ at $P$ equals $T^{(t + 1)/2}$ times the sum of $k(d_0, d')$ over the $d_0$ whose up-move is $d$.
4. Unseen places: at a place $w$ over $T$ that is not seen, $k$ maps the lattice at $w$ into $T^{f(t + 1)/2}$ times the next lattice.
5. Seen places: at a seen place $w$, $T^{f N_i + \sum_\tau s_\tau} k(F)$ lies in the lattice of the decoration at step $i + 1$.

**Theorem 4.7.2 (integral jet moments).** For each admissible datum, each prime $T(u)$ of the datum prime to the norm of the curve ideal, each place $w$ and each embedding $\iota$ into $\mathbb{C}_{T(u)}$ that induces $w$, there are unit weights $u_\tau$ such that the images under $\iota$ of the jet sums lie in the closure of the integral combinations of the point tables, at the seen and at the unseen places.

Lean: `GlobalTheory.T.kernelJets_levelPlace_integralMoments`.

This is a second name for the [integral jet moments](/entry/cm-theta-values/depth-valuations/#integral-jet-moments), which are proved later in this chapter.

**Theorem 4.7.3 (five kernel laws).** Let $I$ be a good true column choice with rational jets, and let $l$, $l_0$, $Z$, a word $u$ and a tuple $a$ be given. Then there is a built datum $B_d$, namely the standard datum of $(I, l, Z, u, a)$, such that:
1. the chain of $B_d$ is the twisted chain at $(u, a)$;
2. for each $i \leq m$ the points at step $i$ split over $T$: there is an equivalence "same off $T$" that the moves respect, every unitary element comes from the group, $T \in P \setminus P^2$ for each prime $P$ of the set $S_T$, and no two primes of $S_T$ are conjugate;
3. $B_d$ sees the places: for $w$ over $T$, $P \in S_T$ and $x \in E$, the image of $x$ (of $\bar x$ when $w$ is not seen) at $(w, P)$ is integral at $w$ if and only if $v_P(x) \leq 1$;
4. for each $i < m$ there is a kernel at step $i$ that satisfies the five laws.

Lean: `GlobalTheory.T.fivePointLaws_trueChains` (also `GlobalTheory.LvT.Built.TrueLaws.laws_true_fam`, a second name).

*Proof.* Take the standard datum. Its chain is the twisted chain by construction. The splitting and the sight condition hold for the standard datum. For the kernels take the standard kernel at step $i$. The analytic hypotheses follow from the goodness of $I$. They give the equivariance of the normalized theta family, the lattice property of its vectors, and the theta chain condition.

Law 1 follows from the equivariance, together with the equality of the chain kernel and the point kernel at representatives, which uses the vector property. Law 2 holds for the standard kernel. Law 3 is the kernel condition for the row family. It comes from the up-move law of the standard kernel and the move steps of the family. Laws 4 and 5 are the kernel bounds at the conjugate prime places and at the level prime places. Both use the integral jet moments and the simplicity of the Weyl module in the closed lowest alcove. $\square$

### The sharp bound

**Lemma 4.7.4 (sharp bound for each tuple).** Let $I$ be a good true column choice with rational jets over a base with correct signs. Then for each word $u$ and each tuple $a$ the twisted chain at $(u, a)$ satisfies the sharp column bound.

Lean: `GlobalTheory.LvT.Built.TrueCols.trueColumns_chain_last_step_sharp_bound`.

*Proof.* Step 1. The five kernel laws give a built datum $B_d$ whose chain is the twisted chain at $(u, a)$, with the splittings, the sight condition and the kernels.

Step 2. We have $[E : \mathbb{Q}] N_m + 1 < T_u$. Indeed $[E : \mathbb{Q}] = 2f$, and the data of the base give a real number $a_0$ with $2 f N_m + 1 < 4 a_0$ and $4 a_0 < T_u$.

Step 3. The weight signs of any chain of the assembled datum are the correct signs of the base. So the chain has the weight signs.

Step 4. The [stability theorem for lattice chains](/entry/cm-theta-values/depth-valuations/#up-moves-and-the-stability-of-lattice-chains) takes the splittings, the sight condition, the kernels, the inequality of Step 2 and the weight signs. It gives the sharp column bound and the stability of the forms. We keep the sharp bound. $\square$

**Theorem 4.7.5 (sharp column bounds for a true column choice).** Let $I$ be a good true column choice with rational jets over a base with correct signs, and let $l$, $l_0$, $Z$ be given, with assembled datum $D$. Let $X$ be a division datum of $D$ and let $u$ be a word. Then:
1. the chain of $D$ satisfies the sharp column bound at $u$;
2. for each place $w$ over $T_u$, each tuple $\mu$ with $\mu \neq \mu_0$, $\mu$ used and $w$ outside the set of $X$ at $\mu$, and each $x \in N_\lambda(w)$, there is $y \in \Lambda_m^\mu$ whose image is $\mathrm{col}_\mu(e_\mu(x))$, with $y = a z$, $z$ in the $\mathcal{O}_w$-span of $\Lambda_m^\mu$, and either $a = 0$ or $v_w(a) \geq -e_w\, m\, E_T(w)$.

Lean: `GlobalTheory.T.trueColumns_row_sharp_bounds` (also `GlobalTheory.LvT.Built.TrueCols.row_true`, a second name).

*Proof.* Part 1. The lemma at the reference tuple $\mu_0$ gives the sharp bound for the twisted chain at $\mu_0$. This chain is the chain of $D$, and the two forms of the sharp bound agree on it by definition.

Part 2. Fix $w$, $\mu$ and $x$. The lemma at $\mu$ gives the sharp bound for the twisted chain at $\mu$. The twisted chain is compatible with the chain of $D$ at step $0$: at each $w$ over $T_u$ the twisted forms see $w$ when $D$ does, and $e_\mu$ maps $N_\lambda(w)$ into the $N_\lambda(w)$ of the twisted chain. So for every $c$ with $v_w(c) \geq e_w m E_T(w)$ the element $c \cdot \mathrm{col}_\mu(e_\mu(x))$ is the image of an element of the $w$-part of $\Lambda_m^\mu$. The number $m E_T(w)$ is an integer $k$. Choose $c$ with $v_w(c) = e_w k$ and write $y = c^{-1}(c y)$. This is the required form, with $a = c^{-1}$. $\square$

The *twisted column bound* of a division datum $X$ at $u$ is the statement of part 2 for all such $w$, $\mu$ and $x$.

**Corollary 4.7.6 (sharp and twisted column bounds).** Under the hypotheses of the theorem, the chain of $D$ satisfies the sharp column bound at $u$, and the twisted column bound of $X$ at $u$ holds.

Lean: `GlobalTheory.LvT.Built.TrueCols.closing_true_cols`.

*Proof.* This is the theorem, with part 2 read as the definition of the twisted column bound. $\square$

### Rows over true columns

A *slot* $Q$ is a predicate on constructed points. It is *over columns* if every point in $Q$ comes from a column datum $w$ and later stages $Z$ with a column view: rational jets, an integrality of rows, the equality of the twisted forms of the object with those of $w$ and $Z$, and a tied tuple. For a datum $D$ and an object $O$ over it, let $R(D, O)$ say: for every word $u$ of $D$, the sharp column bound at $u$ and the twisted column bound of $O$ at $u$ hold. The *level prime row* of $Q$ and a link of bundles says: there is a bundle property that holds eventually at all points in $Q$ and all linked bundles, and for each class $\mathcal{A}$ and selection for it, $R$ holds at $(F.D(x, i), \mathrm{obj}(F, x, i))$ for all $i$ and all large $x$, [closed](/step/closed-def/) on the class.

**Theorem 4.7.7 (column valuations at bundle points).** Let $Q$ be a slot over columns. Then for every bundle type and every link the level prime row of $Q$ holds.

Lean: `GlobalTheory.T.levelPrimeColumnValuations_bundlePoints_overColumns` (also `GlobalTheory.Fc.Cv.row_level_valuations`, a second name).

*Proof.* Step 1. The row statement for any bundle type and link follows from the row statement for the trivial bundle type and the trivial link. So the bundles play no role.

Step 2. For the trivial link it is enough that $R(\beta.D, \beta.O)$ holds eventually at each constructed point $\beta$ in $Q$. The proof takes the bundle property to be $R$ itself and proves closedness with the zero thresholds.

Step 3. It is enough to prove $R(\beta.D, \beta.O)$ for all parameters.

Step 4. Each point of $Q$ comes from a column datum $w$, later stages $Z$, an object $O$ and a column view, over a base with correct signs. The column view rewrites the twisted forms of $O$ to those of $w$ and $Z$. Then the corollary applies to the true column choice of $w$, with the division datum of $O$. $\square$

**Remark 4.7.8 (Formalization).** In `row_true` the three side conditions on $\mu$ are introduced as `_` and not used, so part 2 holds for every tuple and every division datum ([TrueColumnsRowSharpBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TrueColumnsRowSharpBounds.lean#L43)). In `laws_true_fam` the clause $B_d = $ `dat I l Z u a` makes the existential trivial. The name "last step" fits no step: the lemma holds for every tuple, and it drops the stability of the forms. Two different predicates share the name `Conclusion5Sharp`. In `row_level_valuations` the hypothesis `RealTied` is dropped at line 17, and only two parts of the column view are used.
