---
id: tp-final-thm-t
title: Invariant distributions on matrices and vectors vanish off the zero vector, in characteristic p
kind: theorem
decl: PositivityTheory.RgUd.TP.Final.thmT
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.TwistedPieces.TraceFormAlt
covers: 685
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{ThmT}(k)$ for a non-archimedean local field $k$ of characteristic $p > 0$. It is the positive characteristic half of [ThmT for every local field](/entry/all-thm-t/), its only caller. The proof is an induction on a measure $\mu$ of the subalgebra $Z$, supplied by [the descent statement](/entry/tp-final-desc/). The characteristic zero half, with a different induction, is [`T.Final.thmT`](/entry/t-final-thm-t/).

## Statement

We use $X_n = M_n(k) \times k^n$, $B_Z$, $G_Z$ and $\mathrm{Van}(Z)$ as in [the characteristic zero entry](/entry/t-final-thm-t/).

**Theorem.** Let $k$ have characteristic $p > 0$. For each $n$ and each commutative reduced subalgebra $Z \subseteq M_n(k)$, $\mathrm{Van}(Z)$ holds.

## Proof

For $F \subseteq M_n(k)$, let $\mathrm{FibVan}(Z, F)$ say: each $G_Z$-invariant distribution supported on $F \times k^n$ vanishes on $\{v \neq 0\}$. Let $N_Z$ be the set of nilpotent elements of $B_Z$. Let $Z_N$ be the set of $x$ with $x - c$ nilpotent for some $c \in Z$. The proof joins seven lemmas:

- `traceForm`: there is a $k$-linear $\tau$ on $M_n(k)$, symmetric and nondegenerate on $B_Z$, with $\tau = 0$ on $N_Z$.
- `unimod`: from `traceForm`, a group attached to $G_Z$ is unimodular.
- `desc`: from `unimod`, the statement $\mathrm{Desc}$ of [the descent entry](/entry/tp-final-desc/). This is the only input that uses $p$.
- `locOff`: if each characteristic polynomial fibre of $B_Z$ splits into pieces of the form $\{x - c \text{ nilpotent}, c \in Z\}$ or with $\mathrm{FibVan}$, then a distribution as in $\mathrm{Van}(Z)$ vanishes on open sets with $v \neq 0$ and $x \notin Z_N \cap B_Z$.
- `nilCore`: from `traceForm`, `unimod` and the conclusion of `locOff`, $\mathrm{FibVan}(Z, N_Z)$ holds.
- `transl`: $\mathrm{FibVan}(Z, N_Z)$ gives $\mathrm{FibVan}(Z, F)$ for each $F \subseteq B_Z$ with $x - c$ nilpotent on $F$, $c \in Z$.
- `locAll`: if each fibre splits into pieces with $\mathrm{FibVan}$, then $\mathrm{Van}(Z)$.

`van_of` runs a strong induction on $m = \mu(Z)$. The induction hypothesis gives $\mathrm{Van}(Z')$ for $\mu(Z') < m$, so `desc` splits each fibre into pieces of the nilpotent kind or with $\mathrm{FibVan}$. Then `locOff` and `nilCore` give $\mathrm{FibVan}(Z, N_Z)$, and `transl` turns each nilpotent piece into a piece with $\mathrm{FibVan}$. Now `locAll` gives $\mathrm{Van}(Z)$.

`thmT` applies `van_of` and rewrites the hypotheses of $\mathrm{ThmT}$ as `Supp` and `Inv`.

## In the Lean code

The theorem is at [TraceFormAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceFormAlt.lean#L38), and `van_of` at [L20](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceFormAlt.lean#L20). The lemmas at L11 to L17 are second names for `Loc.Final`, `Nil.Final` and `Desc.Final`. `FibVan`, `IsPieces`, `TraceForm`, `Desc`, `LocOff`, `LocAll`, `Transl` and `NilCore` are in [TraceForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceForm.lean#L14). `Van`, `Supp`, `Inv` and `ZN` are in [LocStep.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/LocStep.lean#L31). `Unimod` is in [IsClosedGzS.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/Descent/SliceVanishing/IsClosedGzS.lean#L59); it is about `GzS Z`, which we have not unfolded. We have not unfolded the proofs of the seven lemmas. In `thmT` the bound variable in `fun p hp` hides the prime $p$; this does no harm.
