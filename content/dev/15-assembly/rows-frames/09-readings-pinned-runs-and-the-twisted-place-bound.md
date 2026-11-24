---
title: Readings, pinned runs and the twisted place bound
decls:
  - GlobalTheory.FrameRead.reads_rank
  - GlobalTheory.T.exists_parameterRun_with_laws_and_pins_at_special_prime
  - GlobalTheory.RunOnto.exists_run_pins
  - GlobalTheory.OnAtPlacesBase.on_of_has_atPlaces
  - GlobalTheory.T.twistedPlacesBoundChain_twoRunChain
  - GlobalTheory.OnAtPlacesBase.on_base_atPlaces
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Readings, pinned runs and the twisted place bound

This section proves three inputs of the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The first is a *reading* of the forms of a block at a small place: a map that sends each form to a function with values in a dual Weyl module over $\mathbb{C}_\ell$, compatible with the Hecke operators and the lattices. It is used by [the readings at small places](/entry/reads-of-small-alt/). The second is a run of the parameter datum whose own prime is a given special prime, with its laws and with pins at the twisted places. It is used by [the existence of runs](/entry/exists-runs-at-alt/). The third is the bound at the twisted places for a leaf object that is a record of two runs, used by [the onto path](/entry/onto-path-alt/). Each proof assembles results proved elsewhere.

We use [dual Weyl modules](/learn/representations/#highest-weights-and-branching) and [the $p$-adic numbers](/learn/number-fields/#p-adic-numbers-and-local-fields) of Volume 1.

### Readings at a small place

Fix a point of the main construction, an index $j$ and a finite place $w$ of the field $L$ of the datum, with residue characteristic $\ell$. Let $\lambda_\tau$ be the dominant weights of the datum at $j$, and let $\lambda^W_\tau$ be natural weights with a *shift* $c$: for each $\tau$ and each $a$,
$$\lambda^W_\tau(a) = \lambda_\tau(a) + c_\tau.$$
A *choice* at $w$ is an embedding $e_0 : L \to \mathbb{C}_\ell$, an isomorphism $\mathbb{C}_\ell \cong \mathbb{C}$, evaluations $\mathrm{ev}_\tau$ of the finite adeles of $E$ into $\mathbb{C}_\ell$, matrices $b_\tau$, a finite extension $L_f$ of $\mathbb{Q}_\ell$, and two homomorphisms $\kappa$ and $\chi$ of the level group into matrices and units over the integers of $L_f$. The choice is *good* with shift $s$ if $e_0$ detects $w$ (an integer $x$ lies in $\mathfrak{p}_w$ if and only if $|e_0(x)| < 1$), $e_0$ takes values in $L_f$, $e_0$ is compatible with the complex embedding of $L$, the evaluations are good, $\kappa$ is the evaluation of the level group conjugated by $b$, and $\chi$ is the character with shift $s$.

A choice gives a frame $F$ over $\mathbb{C}_\ell$ with index set $I$. A *reading* of the block $B$ at $w$ for the weights $\lambda^W$ is an embedding $e_0$, a map $\mathrm{ix} : I \to B.\mathrm{Pl} \times \mathbb{N}$ of Hecke indices, and an $e_0$-semilinear map $\mathrm{rd}$ from the forms of $B$ to functions on the frame group with values in $\nabla(\lambda^W)$, such that:

- $e_0$ detects $w$, and $e_0(\mathcal{O}_L)$ lies in the image of the frame;
- each $\mathrm{rd}(f)$ is a form of the frame;
- $\mathrm{rd}$ sends $L$-independent families to $\mathbb{C}_\ell$-independent families;
- $\mathrm{rd}$ turns the Hecke operator of index $\mathrm{ix}(i)$ into the Hecke operator of the frame of index $i$, up to the constant of $i$;
- $\mathrm{rd}$ sends forms with values in the lattice of the block into the lattice of the frame;
- a form whose reading lies in the dual lattice of the frame lies in the dual lattice of the block after multiplication by some $s \notin \mathfrak{p}_w$.

**Theorem 7.9.1 (Readings from a choice).** Let $\ell$ be prime, let $\lambda^W$ be the shift of $\lambda$ by $c$, and let a choice at $w$ be good with shift $-c$ and all $b_\tau = 1$. Then there is a reading of $B$ at $w$ for $\lambda^W$ whose embedding is $e_0$ and whose index map is the inclusion of $I$.

Lean: `GlobalTheory.FrameRead.reads_rank`.

*Proof.* The rank of the frame equals the rank of the datum, so the order isomorphism of ranks is the identity. The tie of the base family gives a coefficient map of the lattice with an injective map to the dual Weyl module. The integers of $L_f$ are the elements of norm at most one. Since $b = 1$, the homomorphism $\kappa$ is the evaluation of the level group. Define $\mathrm{rd}(f)(g)$ by evaluating $f$ at $g$ through the coefficient map and $e_0$. The first two items are the good choice. The Hecke item holds because scalars commute with the evaluation, and a scalar can be cancelled from both sides. The lattice items come from the existence of a reading lattice, which matches the lattice of the block with the lattice of the frame at $w$. The shift $-c$ in $\chi$ cancels the shift $c$ of the weights, so the reading has values in $\nabla(\lambda^W)$ and not in a twist of it. $\square$

### Runs pinned at a special prime

The host has two special primes $\mathrm{pde}$ and $\mathrm{pde}'$, distinct, with characters $\delta$ and $\delta'$. The *own prime* of a twisted place $v$ is $\mathrm{pde}'$ if $\ell_v = \mathrm{pde}$, and $\mathrm{pde}$ otherwise. A full run $r$ of the core is *pinned* at a twisted place $v$ with prime $p$ if $p$ is the own prime of $v$, the $\delta$ data of the run at the positions of $v$ have prime $p$, the half ideal of the run lies in each place over $p$ above $v$, and there is a unitary character $\chi$ of the ideles of $E$ that matches $\delta_{\ell_v}$ and satisfies
$$\xi\big(\det g\big) = \chi(x)$$
whenever $x$ is a determinant root of $g$.

**Theorem 7.9.2 (A run with laws and pins).** At a point of the main construction, assume the core ties of the datum, and let $l \in \{\mathrm{pde}, \mathrm{pde}'\}$. Then there is a run $r$ such that the run has its full laws, it has one cover at each index, every $\delta$ datum of the run in range has prime $l$, $\xi(\det \gamma_0) = 1$ for each $\gamma_0$ in the rational level group, and $r$ is pinned with prime $l$ at every twisted place $v$ whose own prime is $l$.

Lean: `GlobalTheory.T.exists_parameterRun_with_laws_and_pins_at_special_prime` (also `GlobalTheory.RunOnto.exists_run_pins`).

*Proof.* Let $\delta$ be $\delta$ if $l = \mathrm{pde}$ and $\delta'$ otherwise. The core ties say that $\delta$ is a delta character at $l$ with values in the field of the datum. So there are a character $\chi$, a determinant character $\mathrm{de}$ and a finite part with the reciprocity law. The core ties also give that the field is good at $l$. Choose a prime $P$ of $K$ over $l$: if some twisted place has own prime $l$, take the half ideal of the core at $l$, which lies in all the places over $l$; otherwise take any prime over $l$, which exists since $l$ is prime. The laws of the core give a top datum, and the top datum with $P$ and $\mathrm{de}$ extends to a full run with laws and covers. The pins follow from the reciprocity law, since $\xi$ of a determinant equals $\mathrm{de}$ of a determinant root, and $\mathrm{de}$ is trivial on rational points. $\square$

### The bound at the twisted places

Let $O$ be a leaf object over a set $S$ of places with numerical datum $N$, and let $T_w$ be the twisted places. The *bound at the twisted places* with error $\mathrm{err}$ is three statements:

1. for each $w \in T_w$,
$$\sum_j \big(I_w(j, \mu, w) + I_w(j, \mu, \bar w)\big) \leq \Big(\sum_j \big(2 e_w F_0 + e_w\, \mathrm{err}\big) + \frac{2 e_w}{p_w^2}\Big) D,$$
where $I_w$ is the index, $e_w$ the degree, $p_w$ the residue characteristic, $F_0$ the content and $D$ a constant of the leaf;
2. $\mathrm{err} \geq 0$;
3. for each $j$, $\sum_w \log(\ell_w)\big(e_w\, \mathrm{err} + e_w J_0(w, j)\big) \leq E_1(j)$.

**Theorem 7.9.3 (Bound from the leaf properties).** Let $O$ have the rank rows, the Mackey, support, projection, coordinate, span, lemma S, data, identity, share, index, unipotent, depth, page, size and badness properties, the index bound, the twist bound and the exponent bound, and let its error constant be at most $C_E$ and match the definition. Then there is $\mathrm{err}$ such that the bound at the twisted places holds.

Lean: `GlobalTheory.OnAtPlacesBase.on_of_has_atPlaces`.

*Proof.* The index bound, the twist bound and the exponent bound each assert the existence of some data: the index data $\Theta_1, a, r_1, r_2, \delta_2$, a twist $\varepsilon_0$, and a family $J_p$. Put these into $O$. [The core bound at places](/entry/on-core-at-places/) applied to the new object gives the bound. $\square$

**Theorem 7.9.4 (The bound for a record of two runs).** Let $O$ be a leaf object that is a record of two runs, with the family conditions, the group conditions on the real datum and the leaf properties of the last theorem except the Mackey, projection, coordinate, index and unipotent properties. Then there is $\mathrm{err}$ such that the bound at the twisted places holds.

Lean: `GlobalTheory.T.twistedPlacesBoundChain_twoRunChain` (also `GlobalTheory.OnAtPlacesBase.on_base_atPlaces`).

*Proof.* The tied field of the record gives the core ties, and the depth field gives a star structure. These give the level numbers of the tie: the rank of the record equals the rank of the chain. From the ties and the group conditions we get a coordinate $w$ of the tie at the base. From the ties we get the Mackey and projection properties at level, and with the level numbers the index and unipotent properties follow. Replace the coordinate of $O$ by $w$ and apply the last theorem. $\square$

**Remark 7.9.5 (Formalization).** The reading is `Reads` in [HasBlockOfOccurs.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasBlockOfOccurs.lean#L143). `Shift` is at line 22 of LamGApply.lean and `ChoiceOk` at line 106 of ClassesAt.lean. The reading theorem is at line 255 of [ReadsAtSmallPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReadsAtSmallPlace.lean#L255) under `maxHeartbeats 4000000`; it uses `scalar_eq`, `smul_cancel`, `exists_reading_lat`, `evG` and `evG_rat` of the same file. The pin is `RunPin` in ThetaSeriesTies.lean, line 212. The run theorem takes the hypothesis `Links2` and never uses it: the proof binds it to `_`. It uses `exists_xiRec`, `exists_top_of_core` and `exists_full_of_xiRec`, whose statements we read; one output of the last one is dropped with `-`. The bound is `ONwith` in [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L361). In [TwistedPlacesBoundChainTwoRunChain.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwistedPlacesBoundChainTwoRunChain.lean#L26) the first bound discards the first clause of the exponent bound, $J_0 \geq 0$, with `-`, so that clause is not needed for the bound. The record theorem uses only the fields `tied`, `depth` and `rr_eq` of the record, and the replacement of the coordinate is `withCoord`.
