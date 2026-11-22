---
id: laws-true-fam
title: The five kernel laws on the true chains
kind: theorem
decl: GlobalTheory.LvT.Built.TrueLaws.laws_true_fam
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.FivePointLawsTrueChains
covers: 2026
status: drafted
drafted_by: writer@claude
---
This theorem gives, for each column input, a chain datum with a kernel at each step, and proves five laws for the kernels. Through its [second name](/entry/five-point-laws-true-chains/) it goes to [the sharp bound at the last step of a true chain](/entry/true-columns-chain-last-step-sharp-bound/), below [the unitary hypotheses node](/proof/unitary-hypotheses/). Most of it is assembly. The analytic input, in two of the laws, comes from [the integral jet moments](/entry/jet-moments/).

## Statement

Let $I$ be a column input (`ColIn B X`): a frame, characters, a selection of primes, a finite index set $\iota$, tuples and constants. Assume `I.Ok` (six conditions on the spaces, characters and selection) and `I.JetsIn` (jets of the given degree are rational). Let $l$ be a set of laws for $I$, $l_0$ a law at step 0, $Z$ a choice of the five later stages, $u$ a word and $a \in \iota$.

A datum $B_d$ over the record `I.rec7 l Z` holds a number field $E$ with an involution, embeddings into a field $L$, and a decorated chain of lattices with steps $0, \dots, m$. A kernel at step $i$ gives, for each pair of points $(d, d')$ at steps $i$ and $i+1$, a linear map $k(d, d') \colon V_i \to V_{i+1}$.

**Theorem.** There is a datum $B_d$, equal to the standard datum `dat I l Z u a`, such that:

1. the chain of $B_d$ is the twist of `I.tw l l0 Z` at $(u, a)$;
2. for each $i \le m$ the decorated points at step $i$ have a splitting (`Split`): an equivalence "same off $T$" that the moves respect, every unitary $\gamma$ comes from the group, $T \in P \setminus P^2$ for each prime $P \in S_T$, and no two primes of $S_T$ are conjugate;
3. $B_d$ sees the places (`Sees`): for $w$ over $T$, $P \in S_T$ and $x \in E$, the image of $x$ (of $\bar x$ when $w$ is not seen) at $(w, P)$ is integral at $w$ if and only if $v_P(x) \le 1$;
4. for each $i < m$ there is a kernel $k$ with these laws:
   - `KerEq`: $k(g d, g' d') = \rho_{i+1}(g') \circ k(d, d') \circ \rho_i(g)^{-1}$, and $k$ matches the kernel map of the chain;
   - `KerDil`: $k$ is invariant under the diamond moves at each $P$;
   - `KerUK`: the sum of $k(d, d_1)$ over the up-moves $d_1$ of $d'$ at $P$ equals $T^{(t+1)/2}$ times the sum of $k(d_0, d')$ over the $d_0$ whose up-move is $d$;
   - `KerBar`: at a place $w$ over $T$ that is not seen, $k$ maps the lattice at $w$ into $T^{f(t+1)/2}$ times the next lattice;
   - `KerP`: at a seen place $w$, $T^{f N_i + \sum_\tau s_\tau}\, k(F)$ lies in the lattice of the decoration at step $i+1$.

## Proof

Take $B_d$ = `dat I l Z u a`. The first and last clauses are `rfl`. The splitting is `split` and the sight condition is `sees`. For the kernels, take $k$ = `kAt`. `hyp_of_colIn` gives the analytic hypotheses. From them, `normalisedFamily_satisfies_equivarianceLaws` gives the equivariance laws `EqP`, `normalisedThetaFamily_vectors_lattices_thetaZero` gives the vector law `VecP`, and `chTh_ok_of_colIn'` gives the theta chain condition.

- `KerEq`: `kerEq`, with `trueChainKernel_eq_pointKernel_at_representatives` (which uses `VecP`).
- `KerDil`: `kerDil`.
- `KerUK`: `kernelCondition_at_row_family`, by `UpLaw.kAt_uk`, `ukTerm_of_moveStep` and `moveStep_of_family`.
- `KerBar` and `KerP`: `trueChainKernels_bound_conjugatePrimePlaces` and `trueChainKernels_bound_levelPrimePlaces`. Each takes [`kernelJets_levelPlace_integralMoments`](/entry/kernel-jets-level-place-integral-moments/) and `weylModule_simple_closedLowestAlcove` as arguments.

## In the Lean code

The theorem is in [FivePointLawsTrueChains.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FivePointLawsTrueChains.lean#L46). The laws are in [KerIsTerm.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/KerIsTerm.lean#L23). The lemmas `dat`, `split`, `sees`, `kerEq` and `kerDil` are in [MoveStep.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MoveStep.lean#L36). We did not unfold `kAt`, `TwForms`, the fields of `Laws`, or the proofs of the two kernel bounds.

The last clause $B_d$ = `dat I l Z u a` makes the existential trivial: the theorem is about one given datum. The law $l_0$ enters only through `dat_ch`, which is `rfl`. The local lemma `moveStep_fam` repeats the calls to `hyp_of_colIn` and the equivariance lemma. The kernel bounds take as an argument `Published.InducedSimpleLowestAlcove`, which is proved here by `Alc.inducedSimpleLowestAlcove`, not assumed.
