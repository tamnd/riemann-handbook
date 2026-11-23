---
id: casselman-wallach
title: The Casselman-Wallach globalization for U(p,q)
kind: theorem
decl: PositivityTheory.CWB.casselmanWallach
module: Development.WeilBound.CoreStatements.PublishedTheorems.CasselmanWallach.FinalB
covers: 436
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `CasselmanWallach` for the unitary groups $U(p,q)$. The renaming [`casselman_wallach_of_literature`](/entry/casselman-wallach-of-literature/) of volume 8 returns it and states its five parts in full. This entry has the proof. Below this theorem are 436 declarations.

## Statement

Let $\sigma$ be an irreducible unitary representation of $G = U(p,q)$ on a Hilbert space $H$, and let $\pi$ be a smooth representation of moderate growth on a Fréchet-type space $E$. Let $T_0 \colon H \to E$ commute with $K = U(p) \times U(q)$ and with the Lie algebra on the $K$-finite vectors.

**Theorem.** $T_0$ extends to a $G$-map $T$ on the smooth vectors with a Sobolev bound. $T$ is unique, its image is closed, and if $T_0 \neq 0$ on the $K$-finite vectors, then $T$ has a lower Sobolev bound.

This has the form of the Casselman-Wallach theorem (Wallach, Real Reductive Groups II, chapter 11).

## Proof

The proof is `cw_of maxPr`. It has three layers.

1. **The model.** `model_of` takes the hypotheses `c1`, `c2a`, `c2b`, `c3a`, `c3b` and `c3c`. It gives, for each irreducible unitary $\sigma$, a model $E$ of its Lie algebra action with the properties `KDer` and `Mod`.
2. **The growth estimate.** `maxPr` proves `MaxPr`. Let $F$ send each vector $v$ of a model to a function on $G$ of growth order $N$, compatible with the Lie algebra action. Then there are $m$, $K$ and a finite set $I_0$ such that $|F e| \le B(1 + s)^N$ for all $e \in I_0$ gives $|F v (1)| \le K B \, \|(1 + \Omega)^m v\|$. Here $s$ is the size function `hs2` and $\Omega$ is `casimirK`. The proof `maxPr_of` uses an eigenbasis of the Casimir and a maximum principle.
3. **The steps.** `lift_of_steps` proves parts 1 to 3, as `CasselmanWallachLift`. The steps `d1` and `d2` extend $T_0$ with a Sobolev bound. `d3` gives equivariance for $K$ and the Lie algebra on smooth vectors. `d5` writes each $g = k \exp X$, and `d4` then gives equivariance for $G$. `d0` says that a map with a Sobolev bound that vanishes on the $K$-finite vectors vanishes on the smooth vectors. This gives uniqueness. `cw_of_steps` adds parts 4 and 5. If $T_0$ is not zero, a continuous seminorm $Q$ of $T$ is positive on nonzero $K$-finite vectors. The bounds `e2a` to `e2d` and `e3c` turn this into a lower Sobolev bound, and `isClosed_image_of_sobolev_lower` gives a closed image. If $T_0$ is zero, `d0` gives $T = 0$ on smooth vectors.

## In the Lean code

The theorem is in [FinalB.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/FinalB.lean#L8). `lift_of` and `cw_of` are in [CwOf.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/CwOf.lean#L32). `model_of`, `lift_of_steps` and `cw_of_steps` are in [CasselmanWallachAdmissible.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/CasselmanWallachAdmissible.lean#L38). `MaxPr` is in [EigBasis.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/EigBasis.lean#L65).

- `cw_of` builds the model, and then `lift_of` builds it again. The code computes it twice.
- Two hypotheses of `cw_of_steps` have names of simplicial identities. `faceMap_comp_succAbove_castSucc` ([line 130](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/SmoothSeminormAndSobolevBounds.lean#L130)) says that a seminorm that is nonzero at $T v_0$ is nonzero at some translate of each $T v$. `faceMap_castSucc_comp_eq_succ` ([line 154](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/SmoothSeminormAndSobolevBounds.lean#L154)) is about powers of the Casimir and $T$.
- `CwOf.lean` imports files named `ZetaClassicalZeroFreeRegion`, `PageTheorem` and `TendstoPiZero`. These names have no clear relation to this proof.
- We have not unfolded `KDer`, `Mod` or the hypotheses `c1` to `c7`.
