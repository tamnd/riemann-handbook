---
id: core-ind
title: The induced spectrum on GL(4) from a Galois-swapped pair on GL(2)
kind: theorem
decl: UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.coreInd
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.InductionEstimates.IwahoriHeckeInjectivity.IdempotentTraces.CoreInd
covers: 819
status: drafted
drafted_by: writer@claude
---
This theorem is step 4 of [the proof of `indCs_of_gm`](/entry/ind-cs-of-gm/). From the trace identity `CIx`, the comparison `GM` and the lifting fact `LiftAll`, it finds a summand of the spectrum of $\mathrm{GL}_4$ over $F$ whose parameters are those of a pair $\tau_1, \tau_2$ on $\mathrm{GL}_2(E)$.

## Statement

Let $E/F$ be a Galois extension of degree 2 of totally complex number fields, with generator $\sigma$. Let $\tau_1, \tau_2 \subset L^2$ for $\mathrm{GL}_2(E)$ be a pair (`Pair`: both cuspidal irreducible and orthogonal), and let $\theta_2$ be a Galois twist for $\sigma$ with $\tau_1 \theta_2 = \tau_2$ and $\tau_2 \theta_2 = \tau_1$. This is the setup `ForSwap`.

For a subspace $V$, `At S V Λ t` says: at each complex embedding $\tau$, archimedean operators act on $V$ by the elementary symmetric functions of the multiset $\Lambda(\tau)$; at each place $w \notin S$, $V$ has spherical vectors on which Satake operators act by the elementary symmetric functions of $t(w)$.

**Theorem.** Assume `CIx`, `GM` and `LiftAll`. Let $S$ be a finite set of places of $F$, all split in $E$, with $E/F$ unramified outside $S$. Suppose $\tau_i$ satisfies `At` with data $m_i, B_i$ off the places over $S$. Then for each Haar measure $\mu_F$ on $\mathrm{GL}_4$ over $F$ there are $V$, $\Lambda$ and $t$ with:

1. $V$ is a summand of the spectrum (`IsSummand`, not unfolded) and `At` holds for $V, \Lambda, t$ off a finite set;
2. $m_1(\tau) + m_2(\tau) = \Lambda(\tau|_F)$ for each embedding $\tau$ of $E$;
3. for almost all places $w$ of $E$, $B_1(w) + B_2(w)$ is the multiset of $b^{f_w}$ for $b \in t(w|_F)$, with $f_w$ the residue degree.

This has the shape of automorphic induction from $\mathrm{GL}_2(E)$ to $\mathrm{GL}_4(F)$ by a comparison of trace formulas, as in Arthur and Clozel (Ann. of Math. Stud. 120, 1989). We do not claim that this exact statement is in that book.

## Proof

1. `T.places` gives a split place $q \notin S$ and a place $w_0$ over it.
2. `infSplit` gives the archimedean datum $D$. Then [`archEx`](/entry/arch-ex/) gives the idempotents at infinity, and its field `ex` gives a level and a nonzero Eisenstein section $f$.
3. `locSm`, `levLaws` and `typeOf` give the local level data, with an Iwahori subgroup at the places over $q$, and a type datum. `galTwistEx` and `galLoc` give a twist $\theta$ that preserves this type.
4. `lineEx`, `projEx` and `convU` give the lines $A, A'$, the projection onto them and an operator $s$. `ampEx`, `ampPosition` and `pairPosition` give the test functions at infinity.
5. The hypothesis `GM` gives a constant $c$, and `goodEx` gives a further datum $\nu$, so that the geometric sides match (`GeoPair`).
6. The proof builds a family $\mathfrak{x}$ (`Fam`) from these data. `rigidF`, which uses `LiftAll`, shows that no datum over $F$ (`Datum.Pt`, not unfolded) has parameters whose base change is that of $\mathfrak{x}$. This is the hypothesis of `CIx`.
7. `CIx` gives $N$ and the trace identity. `famNe` gives $x > 0$ with Eisenstein term $\neq 0$ for infinitely many $j$.
8. By `rigidE` no summand over $E$ has the parameters of $\mathfrak{x}$, so the cuspidal term is zero. Then the $F$ side is not zero, and some $V$ over $F$ with the required parameters exists.

The rest is bookkeeping.

## In the Lean code

The theorem is at [line 84 of CoreInd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/CoreInd.lean#L84). `CoreInd` and `ForSwap` are in [HeckeInj.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/HeckeInj.lean#L221), and `At` is in [TensFun.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/TensFun.lean#L131). We have not unfolded `GM`, `LiftAll`, `rigidE`, `rigidF` or `famNe`.
