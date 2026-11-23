---
id: t-final-thm-t
title: Invariant distributions on matrices and vectors vanish off the zero vector, in characteristic zero
kind: theorem
decl: PositivityTheory.RgUd.T.Final.thmT
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.FrobeniusReciprocity.LocStep
covers: 354
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{ThmT}(k)$ for a non-archimedean local field $k$ of characteristic zero. It only restates [`van_all`](/entry/van-all/), which has the real content. It has two callers: `All.thmT`, which joins it with [the case of characteristic $p$](/entry/tp-final-thm-t/) (see [ThmT for every local field](/entry/all-thm-t/)), and `thmB_char0`. Because of the two callers, the first step above it that they share is [EveryCharacter from the Galois row](/step/every-character/).

## Statement

Let $k$ be a non-archimedean local field with $\operatorname{char} k = 0$. Let $X_n = M_n(k) \times k^n$, with the action $g \cdot (x, v) = (g x g^{-1}, g v)$ of $\mathrm{GL}_n(k)$. A *distribution* here is a $\mathbb{C}$-linear form $\xi$ on functions $X_n \to \mathbb{C}$; only its values on locally constant functions with compact support enter. For a subalgebra $Z \subseteq M_n(k)$, let $B_Z$ and $G_Z$ be the centralizers of $Z$ in $M_n(k)$ and in $\mathrm{GL}_n(k)$.

Let $\mathrm{Van}(Z)$ be the statement: if $\xi$ is supported on $B_Z \times k^n$ (it kills each test function that vanishes there) and is $G_Z$-invariant, then $\xi(f) = 0$ for each test function $f$ supported in $\{(x, v) : v \neq 0\}$.

**Theorem** ($\mathrm{ThmT}$). For each $n$ and each commutative reduced subalgebra $Z \subseteq M_n(k)$, $\mathrm{Van}(Z)$ holds.

For $Z = k$ this says: a distribution on $M_n(k) \times k^n$ that is invariant under $\mathrm{GL}_n(k)$ is supported on $M_n(k) \times \{0\}$.

## Proof

Apply `van_all` with $m = \dim_k B_Z$. The hypotheses of $\mathrm{ThmT}$ are those of `van_all` written out: the pair (commutative, reduced) becomes the predicate `CR`, and the two conditions on $\xi$ become `Supp` and `Inv`. There is nothing else.

## In the Lean code

The theorem is at [LocStep.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/FrobeniusReciprocity/LocStep.lean#L32). `ThmT` is defined in [IsInvForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/IsInvForm.lean#L54) with all terms written out. `Van`, `Supp`, `Inv` and `Kills` are in [CompactOrbits/LocStep.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/LocStep.lean#L31). The two callers are in [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L13) and ThmBChar0.lean. Both feed `AB.Final.thmA`, whose statement `ThmA` says that a distribution on $\mathrm{GL}_{n+1}(k)$ invariant under conjugation by the mirabolic subgroup is invariant under conjugation by all of $\mathrm{GL}_{n+1}(k)$. That is the form of Bernstein's theorem on $P$-invariant distributions (J. N. Bernstein, *P-invariant distributions on GL(N) and the classification of unitary representations of GL(N) (non-archimedean case)*, Lecture Notes in Math. 1041, 1984). We have not compared the name `ThmT` with that paper.
