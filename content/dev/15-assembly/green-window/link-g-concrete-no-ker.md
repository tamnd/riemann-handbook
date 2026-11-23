---
id: link-g-concrete-no-ker
title: The bound LinkG from group compatibility, given Loc
kind: theorem
decl: Formalism.L2.G.linkG_concrete_noKer
module: Formalism.LocalToGlobal.GroupLattices.LinkGConcreteNoKer
covers: 1994
status: drafted
drafted_by: writer@claude
---
This theorem proves the family bound `LinkG` on a closed family class from two closed hypotheses and the record `Loc`. It turns one hypothesis, group compatibility, into the three local hypotheses that [LinkG from local data](/entry/link-of-local-closed/) asks for, and then applies that theorem. Its only user is [the concrete LinkG theorem](/entry/link-g-concrete5/), which supplies `Loc` by [`loc_proved`](/entry/loc-proved/). The real content is in [LinkG from local data](/entry/link-of-local-closed/).

## Statement

Let $\mathcal{C}$ be a family class. For a family $F$ (a value of `FamP ε`), write $\mathrm{Ev}_F(P)$ for "there is $x_0$ such that $P(x,i)$ holds for all $x \ge x_0$ and all indices $i$". $\mathrm{Closed}(\mathcal{C}, P)$ is the predicate of [the definition Closed](/step/closed-def/).

**Theorem.** Assume `Loc`, $\mathrm{Closed}(\mathcal{C}, \mathrm{GroupCompatibilityFamily})$ and $\mathrm{Closed}(\mathcal{C}, \mathrm{Adm2F})$. Then $\mathrm{Closed}(\mathcal{C}, \mathrm{LinkG})$.

- `Loc` is a record with one field: `SecondTheoremReduced D` for each datum $D$ of the type `D7`.
- `GroupCompatibilityFamily F` says: eventually in $x$, for each $i$, there is a record `GroupCompatibilityAll` for the datum $D(x,i)$. The record holds a Hermitian level datum, a comparison datum, and two facts about each local datum `D.gat u w` of $D(x,i)$ (a discrete valuation ring with its fraction field, places and a finite family of levels): its rings are isomorphic to standard rings built from the residue characteristic (`RingCompatibleAt`), and it comes from a level datum by `gatOfLevelP` (`GatIs`).
- `Adm2F F` is $\mathrm{Ev}_F$ of the condition `adm2`, which we have not unfolded.
- `LinkG F` is a list of local bounds at the places of $D(x,i)$, for all large $x$. See [LinkG from local data](/entry/link-of-local-closed/).

## Proof

The proof applies `link_of_local_closed` with `Loc` and `Adm2F` unchanged. It gets the other three hypotheses from group compatibility, with `Closed.imp`.

1. `gatEF_of_tied` gives $\mathrm{Ev}_F$ of `TrivialStabiliserFiniteClasses`, from the Hermitian levels and the field `gat`, by `gatE_of_gatIs`.
2. `stdSubF_of_tied` gives $\mathrm{Ev}_F$ of `StdSubAt`, from the field `ring`, by `stdSubAt_of_ring`.
3. `npDescF_of_tied` gives `NPDescF`, from the comparison datum, by `Cmp.npDescF_of_valRatF`.

The rest is bookkeeping.

## In the Lean code

The theorem is at [LinkGConcreteNoKer.lean line 48](lean:Formalism/LocalToGlobal/GroupLattices/LinkGConcreteNoKer.lean#L48). The three helpers are in the same file, at lines 13, 20 and 28.

- The theorem only passes hypotheses along, with three small conversions.
- The same file has `linkG_concrete` (line 35). It needs two more hypotheses, the local data systems `hsys` and `hsysS`, and goes through `link_of_numbers_proved`. The present theorem does not need them. The suffix "noKer" refers to the route through `linkG_without_kernels`, which [LinkG from local data](/entry/link-of-local-closed/) describes.
