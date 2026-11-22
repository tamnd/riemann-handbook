---
id: link-g-concrete5
title: The bound LinkG from group compatibility and admissibility
kind: theorem
decl: Formalism.L2.G.linkG_concrete5
module: Formalism.LocalToGlobal.GroupLattices.LinkGConcreteNoKer
covers: 5644
status: drafted
drafted_by: writer@claude
---
This theorem is [`linkG_concrete_noKer`](/entry/link-g-concrete-no-ker/) with its hypothesis `Loc` filled by [`loc_proved`](/entry/loc-proved/). It proves that the bound `LinkG` is [closed](/step/closed-def/) on a family class, from two closed hypotheses. The lemma `closed_linkG_of_duty` applies it to the class `D3 3 𝒜`, and [`shape_closed_link_n_of_green`](/entry/shape-closed-link-n-of-green/) passes the result to `topDesWin` as the input `LinkG`. Below this theorem are 5,644 declarations of the proof. They split between `loc_proved` (2,162) and `linkG_concrete_noKer` (1,994).

## Statement

Let $\mathcal{C}$ be a family class. Assume that these two predicates are closed on $\mathcal{C}$:

- `GroupCompatibilityFamily`: eventually in $x$, for each $i$ and $x > x_1$, there is a record `GroupCompatibilityAll` for the datum $D(x,i)$. The record has five fields: a Hermitian datum `herm` and forms `forms` for each word, a compatibility `cmp` of the lattice comparison, a ring compatibility `ring` at each place, and a field `gat` that writes each local datum `D.gat u w` as the datum `gatOfLevelP` of a level at the residue prime of $w$.
- `Adm2F`: eventually in $x$, the admissibility condition `AuxBlock8.adm2` holds for $(D(x,i), L(x,i))$ and its instance.

Then `LinkG` is closed on $\mathcal{C}$. `LinkG` says: there are $C$, $x_0$ and a function $\delta$ with $\delta(x) \to 0$ such that for all $x \ge x_0$ and all $i$, the local bound `LinkG_at` holds with constant $C$ and error $b^{\delta(x)}$, where $b$ is a size parameter of $L(x,i)$. `LinkG_at` is a list of local bounds: for each word $u$ and each place $w$ whose residue characteristic is not the prime $T$ of $u$, a lattice inclusion at the depth $\lfloor \mathrm{ur}(D, w, \tau_w) \rfloor$ and a bound on lattice lengths; a bound on the sums `Sv`; at inert places below a cutoff, an inequality between sums of the von Mangoldt function over classes and the gains; and two orbit conditions.

## Proof

The proof is one line: `linkG_concrete_noKer 𝒞 loc_proved hT h2`. So the statement is `linkG_concrete_noKer` with one hypothesis discharged. That entry describes how `LinkG` follows from `Loc`, `GroupCompatibilityFamily` and `Adm2F`. [`loc_proved`](/entry/loc-proved/) proves `Loc`.

## In the Lean code

The theorem is in [LinkGConcreteNoKer.lean](lean:Formalism/LocalToGlobal/GroupLattices/LinkGConcreteNoKer.lean#L54). `linkG_concrete_noKer` is in the same file at line 48. It calls `link_of_local_closed` in [AdmissibleFamilyNoKernel.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L272) and three short lemmas of this file that derive `TrivialStabiliserFiniteClasses`, `StdSubAt` and `NPDescF` from `GroupCompatibilityFamily`. `GroupCompatibilityFamily` is in [StdSubAtOfRing.lean](lean:Formalism/LocalToGlobal/GroupLattices/StdSubAtOfRing.lean#L88), `Adm2F` in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L903), and `LinkG` in [GlobalTheoremInputs.lean](lean:Formalism/SharpRestriction/GlobalTheoremInputs.lean#L138).

The file does not explain the suffix "5". The same file has `linkG_concrete`, which takes `Loc` and two more closed hypotheses on local data systems, and `linkG_concrete_noKer`, which drops those two. We have not unfolded the fields of `GroupCompatibilityAll` or the parts of `LinkG_at` beyond their names.
