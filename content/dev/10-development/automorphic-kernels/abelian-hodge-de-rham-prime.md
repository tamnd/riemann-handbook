---
id: abelian-hodge-de-rham-prime
title: The chapters of the Hodge-de Rham proof
kind: theorem
decl: MainStatements.Hodge.Free.abelianHodgeDeRham'
module: Development.WeilBound.CoreStatements.AutomorphicKernels.AbelianDeRham.AbelianHodgeDeRham.AbelianHodgeDeRham
covers: 1003
status: drafted
drafted_by: writer@claude
---
This theorem proves the structure `Chapters`, a list of 47 statements that together give [the Hodge-de Rham sequence of an abelian scheme](/entry/free-abelian-hodge-de-rham/). It only fills each field with a theorem proved elsewhere. The real content is in those theorems and in the assembly `Chapters.print`, which the parent entry describes. Below it are 1,003 declarations.

## Statement

`Chapters` is a structure of type `Prop` with 47 fields. Most fields are implications between named statements, for example `descent : CxSt → HtpySt → QCalcSt → FubiniSt → AffAcycSt → DescentSt`. The fields fall into these groups:

- Čech complexes: `dict`, `cx`, `low`, `htpy`, `qcalc`, `fubini`, `affacyc`, `descent`, `sysbc`, `cmp`, `fincoh`, `van`.
- Perfectness and base change: `perfnoeth`, `perfbase`, `perf`, `perfh1`, `perfh2`, `perfvb`, `flatbc`, `smalllift`.
- The rank of $H^1(A, \mathcal{O}_A)$: `hopf`, `hopfle`, `hopffield`, `h1le`, `feweqn`, `stalkdim`, `h1ge`, `h1field`, `noprim`, `h1all`.
- Forms: `stein`, `cot`, `par`, `axo`, `axform`, `oneform`, `twoform`, `closed`, `lift`, `alt`, `hyp2`, `bi`, `formbc`.
- Wedge products: `wedgeof`, `wedgefield2`, `oside`.
- Assembly: `final`, which gives `AbelianHodgeDeRham` from seven of the statements.

## Proof

Each field is a named theorem, for example `dict := Dict.dictSt` and `final := HodgeAssembly.abelianHodgeDeRham_of_statements`. There is nothing else.

## In the Lean code

The theorem is in [AbelianHodgeDeRham.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/AbelianHodgeDeRham.lean#L58). The structure is in [Development.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/Development.lean#L13).

`Chapters` alone does not give the theorem. The fields `perf` and `h1ge` take `SchemeModels`, two `Spreads` statements, `TrivLocus` and `KFinite` as hypotheses, and `Chapters.print` must get these separately. We have not unfolded most of the 47 statements; the groups follow their names.
