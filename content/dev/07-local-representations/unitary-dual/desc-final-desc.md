---
id: desc-final-desc
title: The descent statement from unimodularity, in positive characteristic
kind: theorem
decl: PositivityTheory.RgUd.TP.Desc.Final.desc
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.TwistedPieces.FiniteDimensionalDescent.Imports
covers: 348
status: drafted
drafted_by: writer@claude
---
This theorem proves the descent statement $\mathrm{Desc}(k)$ for a local field $k$ of characteristic $p > 0$, given unimodularity. It is a pass-through: it puts two proved statements, $\mathrm{Restr}$ and $\mathrm{PieceGood}$, into the assembly lemma `desc_of`. Its caller is the second name [`TP.Final.desc`](/entry/tp-final-desc/), which feeds [`thmT` in positive characteristic](/entry/tp-final-thm-t/).

## Statement

The notation ($B_Z$, $G_Z$, admissible, $\mathrm{Desc}$) is as in [the parent entry](/entry/tp-final-desc/). The statement is the same: if $G_Z$ is unimodular for each admissible $Z$, then $\mathrm{Desc}(k)$ holds.

## Proof

The proof is `desc_of k restr pieceGood p hU`. The lemma `desc_of` takes $\mu$ to be the following invariant. For admissible $Z$, let $e$ run over the primitive idempotents of $Z$, and put

$$\mu(Z) = \sum_{e} \left\lfloor \frac{\dim_k e B_Z}{\dim_k e Z} \right\rfloor.$$

Call a closed set $F \subseteq B_Z$ *good* if either $F \subseteq c + \{\text{nilpotents}\}$ for some $c \in Z$, or there is an admissible $S$ (of any size $N$) with $\mu(S) < \mu(Z)$ such that $\mathrm{Van}(S)$ implies the vanishing on $F \times k^n$ of the second case of $\mathrm{Desc}$. The two inputs are:

- $\mathrm{Restr}$ (`Restr.Final.restr`): for each admissible $Z$ there are an admissible $Z'$ with $\mu(Z') = \mu(Z)$ and a power $q$ of $p$ such that every scalar $a \in k$ has a $q$-th root in $Z'$ and every nilpotent $y \in B_{Z'}$ has $y^q = 0$. For each $\chi$ there is a finite list of polynomials $\chi'$ such that good decompositions for $Z'$ and all these $\chi'$ give a good decomposition for $Z$ and $\chi$.
- $\mathrm{PieceGood}$ (`Piece.Final.pieceGood`): if $G_Z$ is unimodular for all admissible $Z$, then for $Z'$ with these two properties of $q$, every $\chi'$ has a good decomposition.

The proof of `desc_of` chains them: $\mathrm{Restr}$ moves $Z$ to $Z'$, $\mathrm{PieceGood}$ gives the pieces for $Z'$, and $\mathrm{Restr}$ brings them back. A good piece of the second kind gives the second case of $\mathrm{Desc}$, because $\mu(S) < \mu(Z)$. The rest is bookkeeping.

## In the Lean code

The theorem is at [Imports.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/Imports.lean#L11). The lemmas it calls:

- `Asm.desc_of` in [DescOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/DescOf.lean#L9).
- `Restr.Final.restr` in [RestrL.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/RestrictedCharpolys/RestrL.lean#L17), from `restrL`, `phiEx` and `pullPieces`. We have not unfolded these.
- `Piece.Final.pieceGood` in [PieceGood.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/PieceGood.lean#L12), from `pieceGood_of` with Frobenius reciprocity, `sect`, `pieceTop`, `dich` and `transfer`. We have not unfolded these.

The definitions `mu`, `Good`, `HasRoots`, `NilBound`, `Restr` and `PieceGood` are in [PieceGood.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/PieceGood.lean#L19). In `mu` the quotient is division in $\mathbb{N}$, which rounds down. We have not checked whether it is exact. The file name `Imports.lean` does not describe its content.
