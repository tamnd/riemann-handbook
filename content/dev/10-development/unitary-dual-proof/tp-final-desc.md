---
id: tp-final-desc
title: The descent statement in positive characteristic, second name
kind: theorem
decl: PositivityTheory.RgUd.TP.Final.desc
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.TwistedPieces.TraceFormAlt
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`Desc.Final.desc`](/entry/desc-final-desc/). It has no proof of its own. Its only caller is [`thmT` in positive characteristic](/entry/tp-final-thm-t/), which uses the descent statement to run an induction. The real content is in the entry [the descent statement from unimodularity](/entry/desc-final-desc/).

## Statement

Let $k$ be a non-archimedean local field of characteristic $p > 0$. For a subalgebra $Z$ of $M_n(k)$, let $B_Z$ be its centralizer in $M_n(k)$ and $G_Z$ its centralizer in $\mathrm{GL}_n(k)$. Call $Z$ *admissible* if it is commutative and reduced.

**Theorem.** Suppose that $G_Z$ is unimodular for each $n$ and each admissible $Z$. Then the statement $\mathrm{Desc}(k)$ holds.

$\mathrm{Desc}(k)$ says: there is a function $\mu$ from admissible subalgebras to $\mathbb{N}$ such that, for each admissible $Z \subseteq M_n(k)$ and each polynomial $\chi \in k[X]$, the matrices $x \in B_Z$ with characteristic polynomial $\chi$ lie in finitely many disjoint closed $G_Z$-stable sets $F_1, \dots, F_m \subseteq B_Z$, and each $F_i$ has one of two properties:

1. there is $c \in Z$ with $x - c$ nilpotent for all $x \in F_i$;
2. if the vanishing statement $\mathrm{Van}(Z')$ holds for all admissible $Z'$ with $\mu(Z') < \mu(Z)$, then each $G_Z$-invariant distribution on $F_i \times k^n$ vanishes on $\{v \neq 0\}$.

$\mathrm{Van}$ is defined in the entry [ThmT in characteristic zero](/entry/t-final-thm-t/).

## Proof

The proof is the term `Desc.Final.desc k p`. Nothing else happens.

## In the Lean code

The theorem is at [TraceFormAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceFormAlt.lean#L13). $\mathrm{Desc}$ is `TP.Desc` in [TraceForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceForm.lean#L30). The pieces are `IsPieces`, and the conclusion of the second case is `FibVan`, in the same file. The unimodularity hypothesis is `T.Desc.SLF.Unimod` in [IsClosedGzS.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/Descent/SliceVanishing/IsClosedGzS.lean#L59). In `thmT` it is supplied by `unimod k (traceForm k)`.
