---
id: ind-cs
title: Automorphic induction from GL(2) over a quadratic extension to GL(4)
kind: theorem
decl: UpperTheory.V.Z.Bc.indCs
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.BaseChangeUnits.WsIIOfPrintsH
covers: 2024
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{IndCs}$: a cuspidal representation of $\mathrm{GL}_2$ over a quadratic extension $M/K$ of totally complex fields, with distinct weights and good behaviour at the non-split places, has an automorphic induction to $\mathrm{GL}_4$ over $K$. It is used twice in the four-dimensional branch under [`sp4In0_alt`](/entry/sp4-in0-alt/): by [`seedIIs_alt`](/entry/seed-iis-alt/) and by `fourth_initial_of_prints_h`. That branch proves the symplectic automorphy statement that feeds the counts $\mathrm{CountII}$ and $\mathrm{CountIII}$ of the [window bound](/proof/vwin/). The proof is one line. The content is in [`indCs_of_gm`](/entry/ind-cs-of-gm/).

## Statement

Let $K$ be a totally complex number field and $M/K$ an extension of degree 2, with $M$ totally complex. Let $\pi$ be an irreducible cuspidal subspace of automorphic forms on $\mathrm{GL}_2$ over $M$. For a complex embedding $\tau$ of $M$, write $\pi \in \mathrm{Inf}(\tau, m)$ when $\pi$ has infinitesimal character given by the multiset $m$ at $\tau$. Assume:

1. (*Mixed weights*, `MixWtC`.) For each embedding $\varphi \colon K \to \mathbb{C}$ there are two distinct embeddings $\tau \neq \tau'$ of $M$ above $\varphi$ and integer pairs $m, m'$ such that $\pi$ has infinitesimal characters $m$ at $\tau$ and $m'$ at $\tau'$, and the four integers $m_0, m_1, m'_0, m'_1$ are distinct.
2. (*Bad places*, `SplitBad`.) At each finite place $v$ of $K$ that does not split in $M$, the extension is unramified, and $\pi$ has Satake parameters at each place $w$ of $M$ above $v$.

**Theorem.** Then there is a cuspidal $P$ on $\mathrm{GL}_4$ over $K$ with the following properties.

- (*Satake parameters*, `IndSys`.) For all but finitely many places $w$ of $M$, with $v$ the place of $K$ below $w$: if $w' \neq w$ is the other place above $v$, then the Satake parameters of $P$ at $v$ are $B \cup B'$, where $B, B'$ are those of $\pi$ at $w, w'$; and if $Nw = (Nv)^2$, then the Satake parameters of $\pi$ at $w$ are $\{b^2 : b \in B'\}$ and those of $P$ at $v$ are $B' \cup (-B')$ for some $B'$.
- (*Infinitesimal character*.) If $\tau \neq \tau'$ lie above the same embedding $\varphi$ of $K$, and $\pi$ has infinitesimal characters $m, m'$ at $\tau, \tau'$, then $P$ has infinitesimal character $m + m'$ at $\varphi$.

These are the local properties of automorphic induction for a cyclic extension of prime degree (Arthur and Clozel, *Simple algebras, base change, and the advanced theory of the trace formula*, Ann. of Math. Stud. 120, 1989, Chapter 3). The Lean statement asks only for these two properties.

## Proof

The proof applies [`indCs_of_bcfl`](/entry/ind-cs-of-bcfl/) to `bcflUnit`, which proves $\mathrm{BCFLUnit}$, the base change fundamental lemma for the unit element of the spherical Hecke algebra of $\mathrm{GL}_n$ over an unramified cyclic extension of local fields (Kottwitz, *Base change for unit elements of Hecke algebras*, Compositio Math. 60, 1986). See [`indCs_of_bcfl`](/entry/ind-cs-of-bcfl/) for that statement.

## In the Lean code

The theorem is in [WsIIOfPrintsH.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/BaseChangeUnits/WsIIOfPrintsH.lean#L11). The proof is `indCs_of_bcfl bcflUnit`.

- `IndCs` is defined in [HeckeInj.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/HeckeInj.lean#L91). `SplitBad` is at line 87 of the same file.
- `IndSys` and `MixWtC` are in [QuadraticInductionGL2Alt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/BaseChangeUnits/QuadraticInductionGL2Alt.lean#L15).
- `bcflUnit` is in [BcflUnit.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/IntegralUnitBaseChange/BcflUnit.lean#L30). It is outside this subtree.

The same file `QuadraticInductionGL2Alt.lean` has a statement `IndC` (line 80) that is `IndCs` without the hypothesis `SplitBad`. So `IndCs` is a weaker form of `IndC`. The name `indCs` is also used for a different theorem, `E.indCs : IndNorm → IndCs` in `NotConjIso.lean`; the proof of [`indCs_of_gm`](/entry/ind-cs-of-gm/) calls that one. We have not unfolded `CuspSub`, `HasSat` or `HasInfChar` past their names and the definition of `HasInfChar` in `ExpoConjOfIsCsd.lean`.
