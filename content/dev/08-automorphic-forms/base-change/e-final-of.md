---
id: e-final-of
title: The limit statement EFinal from separation, finiteness and limit vectors
kind: theorem
decl: PositivityTheory.Rg.BcB.SpectralAccumulation.eFinal_of
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.InfinitesimalCharacterLimits.EFinalOf
covers: 362
status: drafted
drafted_by: writer@claude
---
This theorem proves the limit statement `EFinal` from three hypotheses: [the separation statement](/entry/separation-holds/) `Sep4`, a finiteness statement `FinDisc` and a limit statement `LimVec`. It only passes them, with seven proved lemmas, to the gluing theorem `e45_final_gluing`. Its two callers, `eisenstein_final_of_separation` and `eFinal_holds'`, supply the hypotheses, and `EFinal` goes on to `readLimit_of_efinal`. The first step above it is [EveryCharacter from the Galois row](/step/every-character/).

## Statement

**Theorem.** $\mathrm{Sep4} \wedge \mathrm{FinDisc} \wedge \mathrm{LimVec} \Rightarrow \mathrm{EFinal}$.

`EFinal` says, in short: let $f_k$ be nonzero continuous vector-valued functions on $\mathrm{GL}_a(\mathbb{A}_E) \times \mathrm{GL}_b(\mathbb{A}_E)$, of a fixed type, with automorphic slices, under the conditions `LeftInv` and `WL2`. Suppose that they are Hecke eigenvectors with convergent eigenvalues, and that the infinitesimal characters of the slices converge to multisets $n_1$, $n_2$ of real numbers with $n(\bar\tau) = -n(\tau)$ and gaps of at least $\tfrac12$. Then there are untwisted good trees $s_1$, $s_2$ with infinitesimal characters $n_1$, $n_2$ and a nonzero $F$ in the tensor product of their spaces, of the same type, that is a Hecke eigenvector with the limit eigenvalues. `FinDisc` says that discrete spectra of bounded type, bounded infinitesimal character and exponents bounded away from $0$ fall into finitely many isomorphism classes.

## Proof

`e45_final_gluing` has the type `InfinitesimalCharacterGlue`:
$$\begin{aligned}&{\mathrm{E3} \to \mathrm{Sep4} \to \mathrm{Lim5} \to \mathrm{Graft} \to \mathrm{TwShift} \to {}}\\ &{\quad \mathrm{TrStable} \to \mathrm{LimVec} \to \mathrm{AdmDisc} \to \mathrm{UntwOfReal} \to \mathrm{InfTree} \to \mathrm{EFinal}.}\end{aligned}$$
The proof supplies `E3` from `etale_base_change_of_duality`, `Lim5` from `LimG.lim5` applied to `FinDisc`, the four tree lemmas from `Trees.treeLemmas`, `AdmDisc` from `admissible_discrete_spaces` and `UntwOfReal` from `Untw.untwOfReal_holds`. There is nothing else.

## In the Lean code

The theorem is at [EFinalOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/InfinitesimalCharacterLimits/EFinalOf.lean#L11). `EFinal` is in [InfinitesimalCharacterGlue.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/InfinitesimalCharacterLimits/InfinitesimalCharacterGlue.lean#L20), and `FinDisc` and `LimVec` are in [AllLeaves.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/InfinitesimalCharacterLimits/AllLeaves.lean#L99). `e45_final_gluing` is in [E45FinalGluingStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/E45FinalGluingStatement.lean#L7); its proof tries `eFinalGlue` in three forms with `first`. We have not unfolded `E3`, `WL2` or `LeftInv`.
