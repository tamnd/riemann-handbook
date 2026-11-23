---
id: ge-closed
title: Grothendieck's existence theorem for closed subschemes
kind: theorem
decl: GlobalTheory.CompanionTheory.GE.geClosed
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.GrothendieckExistenceClosed
covers: 498
status: drafted
drafted_by: writer@claude
---
This theorem proves `GEClosed`, the existence theorem for closed subschemes over an adically complete Noetherian ring. It is called through its second name [`grothendieck_existence_closed`](/entry/grothendieck-existence-closed/), and from there it goes into [the formal algebraisation theorem](/entry/formal-thickening-formal-algebraisation/). The proof reduces the statement to one about coherent sheaves, [`statement_bot`](/entry/statement-bot/), which has most of the content.

## Statement

Let $R$ be a Noetherian ring and $I$ an ideal, with $R$ complete and separated for the $I$-adic topology. Put $R_e = R/I^{e+1}$. Let $X$ be a scheme over $R$ that is separated, locally of finite type and quasi-compact. Put $X_e = X \times_{R} R_e$, with the closed immersions $X_e \to X_{e+1}$ and $X_e \to X$ (see [schemes](/learn/geometry/#schemes-and-varieties)).

**Theorem.** Let $C_e \to X_e$ ($e \geq 0$) be closed immersions, and let $\beta_e \colon C_e \to C_{e+1}$ be maps over $X_e \to X_{e+1}$ such that $C_e = C_{e+1} \times_{X_{e+1}} X_e$ (the square is a pullback). Suppose that $C_0$ is proper over $R_0$. Then there are a closed immersion $j \colon C \to X$ with $C$ proper over $R$, and maps $b_e \colon C_e \to C$, such that $C_e = C \times_X X_e$ through $b_e$ for each $e$, and $b_{e+1} \circ \beta_e = b_e$.

So a compatible system of closed subschemes of the thickenings, proper at the bottom, comes from one closed subscheme of $X$. This is Grothendieck's existence theorem in its form for closed subschemes with proper support; see EGA III$_1$, §5.1 (Publ. Math. IHÉS 11, 1961).

## Proof

The proof is one line: `geClosed_of_statement_bot` applied to `statement_bot`.

1. [`statement_bot`](/entry/statement-bot/) gives, for each such $R$, $I$ and $X$, the statement `Statement I ⊥`: a compatible system of quotients of a coherent sheaf $E$, with proper support, comes from one quotient of $E$.
2. `geClosed_of_statement_bot` is a second name for `Close.geClosed_of_statement`. That proof takes $E = \mathcal{O}_X$ and $S_e$ the ideal sheaf of $C_e$ in $X$. The pullback squares give $S_e = S_{e+1} + I^{e+1}\mathcal{O}_X$. `exists_ideal_of_statement` then gives an ideal sheaf $\mathcal{J}$ with $\mathcal{J} + I^{e+1}\mathcal{O}_X = S_e$ and $V(\mathcal{J})$ proper over $R$. Put $C = V(\mathcal{J})$. The maps $b_e$ are the factorizations of $C_e \to X$ through $C$. The rest is bookkeeping with pullback squares.

## In the Lean code

The theorem is at [GrothendieckExistenceClosed.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosed.lean#L64). `GEClosed` is in [GEClosedProj.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/GEClosedProj.lean#L13). The thickenings are `thick`, `thickObj` and `thickMap` in [ThickTransComp.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/ThickTransComp.lean#L200).

- `statement_bot`, in the same file.
- `GlobalTheory.T.geClosed_of_statement_bot`, in [GrothendieckExistenceClosedAltBis.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosedAltBis.lean#L6), which is `Close.geClosed_of_statement` in [GeClosedOfStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GeClosedOfStatement.lean#L356).

The Lean form asks for a separated scheme of finite type, not a proper one. Properness is asked only of $C_0$ and given for $C$. "Complete" is Mathlib's `IsAdicComplete`, which includes separatedness.
