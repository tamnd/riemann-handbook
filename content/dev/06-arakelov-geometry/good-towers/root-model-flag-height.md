---
id: root-model-flag-height
title: The fibre input of a root model, restated
kind: theorem
decl: GlobalTheory.T.root_model_flag_height
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.RootModelFlagHeightStatement
covers: 519
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`TopFibre.fibreInput`](/entry/fibre-input/), which proves the condition `Ht.FibreInput` for a root model that carries a Hodge component with a flag and root lines. That entry has the content. The one user of this theorem is [`tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/), which applies it to the reference model of each component of a good tower.

## Statement

The statement is the same as that of [`fibreInput`](/entry/fibre-input/). Assume `N1ab`, `PartI`, `ResKStatement`, `SemiAbelianHomExtension` and `SlopeBoundSt`. Let $R$ be a root model with $N = p + q \geq 1$, let $\mathfrak{M}$ be a Hodge component over $R$, and let $\mathrm{Fl}$ be a flag of $\mathfrak{M}$ whose graded pieces have the degrees of the lines of $R$ (`Fl.RootLines`). Then `Ht.FibreInput R` holds: at each algebraic point, the heights of the lines of $R$ are, up to a constant, the graded degrees of a flag pair in a hermitian bundle with small maximal slope.

## Proof

The proof applies `fibreInput`.

## In the Lean code

The theorem is in [RootModelFlagHeightStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/RootModelFlagHeightStatement.lean#L14). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.TopFibre.fibreInput | ...
```

The name says "flag height"; the conclusion is the fibre input. The Hodge component $\mathfrak{M}$, the flag and the root lines appear only in the hypotheses. The conclusion is a property of $R$ alone, so the theorem says: if such data exist, then $R$ has the fibre input.
