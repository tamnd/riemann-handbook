---
id: row-true
title: Sharp column bounds for the datum of a true column choice
kind: theorem
decl: GlobalTheory.LvT.Built.TrueCols.row_true
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.TrueColumnsRowSharpBounds
covers: 2422
status: drafted
drafted_by: writer@claude
---
This theorem proves two valuation bounds at the places over $T_u$ for the datum that a true column choice assembles: a sharp bound for its own column map, and a bound for each twisted column map. Both come from one lemma, [the sharp bound for each twisted chain](/entry/true-columns-chain-last-step-sharp-bound/), applied to the reference tuple and to each other tuple. Through [a relay](/entry/true-columns-row-sharp-bounds/), the result goes to the field `aP10` of [the record HypsAlt](/step/hyps-alt-def/).

## Statement

The data. $B$ is a base (`GlobalTheory.Mem.Base`), with ranks $m$, $f$, $N_i$, a CM field $E$ and a field $L$ with places $w$. $X$ is a `PreX` over $B$. $I$ is a true column choice `TC B X` (an abbreviation of `ColIn B X`): a Hecke frame, characters, a set of primes, and a finite set $\iota$ of tuples with a reference tuple $\mu_0$ and a Hecke character for each tuple. $l$ is a proof of `I.Laws`, $l_0$ of `I.Law0 l`, and $Z$ is a record of five later stages. From these, `I.rec7 l Z` is a datum $D$ of type `D7`, and `I.tw l l0 Z` is a family $\mathrm{Tw}$ of twisted forms of $D$. For a word $u$, $D$ has a column chain with lattices $\Lambda_i$ at levels $0 \le i \le m$, embeddings into function spaces, and a column map $\mathrm{col}$ from level $0$ to level $m$. Each tuple $\mu$ has its own chain, lattices $\Lambda_i^\mu$, column map $\mathrm{col}_\mu$ and an isomorphism $e_\mu$ at level $0$.

The quantities. For a place $w$ over $T_u$, $e_w$ is the ramification index (`ramIdx`) and $E_T(w)$ is `EatT D u w`. It is $0$ if $w$ is not seen by the forms, and otherwise $2\sum_\tau W_\tau + f N_m + |\mathrm{tops}|(t+1)(m+1)/4$, with weights $W_\tau$. $N_\lambda(w)$ is the image of the ramified part of $\Lambda_0$ at $w$ under $T_u^{e}\, U_w^{m}$, where $U_w$ is a product of $U$ operators and $e$ is an exponent (`LT.Nlam`).

**Theorem.** Assume `I.Ok`, `I.JetsIn` and `BaseSigns B`. Let `Dx : DivX D` and let $u$ be a word. Then:

1. (`Conclusion5Sharp D u`) For each place $w$ over $T_u$ and each $c \in L$ with $v_w(c) = n \ge e_w\, m\, E_T(w)$, the map $\varphi \mapsto c \cdot \mathrm{col}(\varphi)$ sends $N_\lambda(w)$ into the $w$-part of $\Lambda_m$.
2. For each place $w$ over $T_u$, each tuple $\mu$ that is used, is not $\mu_0$ and has $w$ outside `Dx.Qp μ`, and each $x \in N_\lambda(w)$, there is $y \in \Lambda_m^\mu$ with image $\mathrm{col}_\mu(e_\mu(x))$, and $y = a z$ with $z$ in the $\mathcal O_w$-span of $\Lambda_m^\mu$ and $a = 0$ or $v_w(a) \ge -e_w\, m\, E_T(w)$ (`ColGeTw` with exponent $-m E_T(w)$).

`BaseSigns B` says: the last entry $u_{k-1}$ of the Hodge parameter at each top embedding is at most $-(k-1)/2$, and the first entry $e_0$ at each embedding is at least $k/2$.

## Proof

Part 1. [The chain lemma](/entry/true-columns-chain-last-step-sharp-bound/) at the tuple $\mu_0$ gives the chain form of the sharp bound for the twisted chain at $\mu_0$. By `own_eq`, this chain is the own chain of $D$ (by `rfl`). By `levelChainSharpColumnValuation_ownChain_iff` (an `Iff.rfl`), the chain form at the own chain is `Conclusion5Sharp D u`.

Part 2. Fix $w$, $\mu$ and $x$.

1. The chain lemma at $\mu$ gives the sharp bound for the twisted chain at $\mu$.
2. `twistedChain_initialLattice_compatible_trueColumns` gives `Step0Tie`: at each $w$ over $T_u$, the twisted forms see $w$ when $D$ does, and $e_\mu$ maps $N_\lambda(w)$ into the $N_\lambda(w)$ of the twisted chain.
3. `tupleChainSharpColumnValuation_of_twisted` combines these. For $c$ with $v_w(c) \ge e_w m E_T(w)$, $c \cdot \mathrm{col}_\mu(e_\mu(x))$ is the image of some element of the $w$-part of $\Lambda_m^\mu$.
4. `colGeTw_of_tupleChainSharpColumnValuation` picks an integer $k = m E_T(w)$ (`exists_int_m_mul_EatT`) and $c$ with $v_w(c) = e_w k$. Then $y = c^{-1}(c\,y)$ has the form that `ColGeTw` asks for.

## In the Lean code

The theorem is in [TrueColumnsRowSharpBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TrueColumnsRowSharpBounds.lean#L36). The equation `own_eq` is in [MoveStep.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MoveStep.lean#L39), and the iff is in [LevelChainSharpColumnValuationOwnChainIff.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LevelChainSharpColumnValuationOwnChainIff.lean#L726). The `Step0Tie` lemma is a relay of `step0Tie_trueCols`, and we have not read the proof of `step0Tie_trueCols`.

The three side conditions on $\mu$ in part 2 are not used: the proof names them `_` (line 43). So part 2 holds for every tuple, $\mu_0$ included. The division datum `Dx` occurs only in one of these unused conditions, so the theorem holds for every `Dx`.

Two different predicates have the name `Conclusion5Sharp`. The conclusion uses `Formalism.MainNotions.product_first_zeroth_parts.Conclusion5Sharp D u`, for a datum and a word. The chain lemma uses `GlobalTheory.LvT.Conclusion5Sharp`, for a chain. They agree on the own chain by definition.
