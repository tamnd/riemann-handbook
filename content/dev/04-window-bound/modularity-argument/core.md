---
id: core
title: The eigenform dichotomy over a CM field, at one level
kind: theorem
decl: core
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.WeilDeligneUnramified.LevUnion
covers: 1919
status: drafted
drafted_by: writer@claude
---
This private theorem is the main step of [the transfer from U(2) to U(3)](/entry/spec-out-s/). It works at one level $\mathrm{lev}(K_2, S, V)$. It moves a $U(2)$ eigenform over the CM field $L$ to the norm one group of a quaternion algebra over $L^+$, applies [the dichotomy over a totally real field](/entry/spec-f/), and moves the result back. The theorem `specOutS` then only chooses the levels.

## Statement

Let $L$ be a CM field, and fix a bridge $B$ with `B.Ok`. It writes $L \cong L^+(\sqrt{\Delta})$ and matches $U(3)$ and $SU(2)$ over $L$ with the group $U_3$ of the identity form and the norm one group $D^1$ of the quaternion algebra $D$ over $L^+$ (see [the trace identity](/entry/t-fid0/) for these groups). Fix a choice $T$ of local splittings at the split places.

Let $S$ be a finite set of places of $L$ with local levels $V_w$, and let $A$ be local data over $L^+$ with `A.Ok` that fit $(S, V)$: the places of $A$ are the places of $L^+$ under $S$, and the local levels agree. Let $a_w$ be characters of $L_w^\times$, and let $b$ be the characters of $L^+_v$ that match them under $T$ (the condition `FitCh`). Let $j \ge 1$ and $e$ be weights.

**Theorem.** Let $\varphi \ne 0$ be a form on $U(2)$ of weight $\mathrm{Sym}^j \otimes \det^e$ and level $\mathrm{lev}(K_2, S, V)$, with $\mathrm{EigS}(a_w)$ at each $w \in S$. Let $B_K$ be a space of forms on $D^\times$ of weight $\mathrm{Sym}^{2j+1}$ with `A.dat.IsBK`. Then one of these holds:

1. there is a form $\varphi' \ne 0$ on $U(3)$ of weight `repG j` and level $\mathrm{lev}(K_3, S, V)$, with $\mathrm{EigT}(a_w, 1, a_w^{-1})$ at each $w \in S$;
2. there is a form $\varphi' \ne 0$ in $B_K$ with the eigen condition `A.EigK` for $b^2$.

The conditions $\mathrm{EigS}$ and $\mathrm{EigT}$ are those of [the transfer theorem](/entry/spec-out-s/).

## Proof

1. **Into the quaternion group.** `inS` gives a finite adele $y$ of $D^\times$, trivial at the places of $A$, with this property: every space of forms on $D^1$ at the level conjugated by $y$, of weight `Wt.cS`, holds a nonzero form $\psi$ with the eigen condition `A.EigS` for $b$.
2. **The spaces.** `bG` gives a space $B_G$ of forms on $U_3$ with a twist $s$ (the Galois conjugation), of weight `Wt.cG`, with `IsBG`. `bS` gives the space $B_S$ on $D^1$ at $y$ of weight `Wt.cS`. Step 1 gives $\psi \in B_S$.
3. **The dichotomy.** [`specF`](/entry/spec-f/) gives a nonzero $\psi' \in B_G$ with `A.EigG` for $b$, or case 2.
4. **Back to $L$.** In the first case `outG` turns $\psi'$ into the form $\varphi'$ of case 1.

## In the Lean code

The theorem is `private` in [LevUnion.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/LevUnion.lean#L98). Its name `core` says nothing about its content, and its Lean name has no namespace.

- `inS` is in [AutomorphicInSphericalLevel.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/FiniteOrbits/AutomorphicInSphericalLevel.lean#L318), and `outG` in [LevelStep.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/FiniteOrbits/LevelStep.lean#L230). Their statements `InS` and `OutG` are in [HodgeTateFromSandwich.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/HodgeTateFromSandwich.lean#L109). We read the statements, not the proofs.
- `bG` and `bS` are private wrappers in the same file around `baseG` and `baseS`.
- Case 2 stays on $D^\times$ over $L^+$. The theorem `specOutS` moves it back to $U(2)$ over $L$ with `second`.
