---
id: export-f-prm-r-alt-alt
title: The export condition on built points, from a norm choice with a law
kind: theorem
decl: GlobalTheory.Mem.Top.ExportTrue.exportF_prmR_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AutomorphyOfHyp
covers: 2228
status: drafted
drafted_by: writer@claude
---
This theorem proves the export condition `ExportF` for the slot of built points, for parameters made from a norm choice extension $N$. Its only user is [automorphy-of-hypotheses-alt-alt](/entry/automorphy-of-hypotheses-alt-alt/), which has the same statement and goes up to [the base lattice from a pair](/entry/exists-base-lattice-of-pair-alt/) and from there to the step [HypsAlt is nonempty](/step/nonempty-hyps/). The theorem is a short adapter. It changes one hypothesis into the form that [export-f-is-built-e-alt-alt](/entry/export-f-is-built-e-alt-alt/) needs. The real content is lower, in [export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/).

## Statement

Assume the 27 named hypotheses of [export-f-is-built-e-alt-alt](/entry/export-f-is-built-e-alt-alt/) (Galois cohomology, class field theory, theta series, Hecke lattices, Galois representations and `Conclusion5` for each datum). Assume also:

1. `PublishedInputsThirdLayerAlt` and `SerN`, two further named inputs;
2. $h_L$, a proof of [RecTExists](/step/rect-exists-def/);
3. `MemberAtLayerPoint` for $h_L$ and the predicate "each row side $R_w$ with the same local row as the point satisfies `GoodRowCuspParam`";
4. a norm choice extension $N$, an extension datum $S$ (`SExt`) and a geometry datum $\Gamma$ (`GeoP`);
5. $h_N$: at each point, a witness of $N$ gives a witness of `extensionWithLaw`.

Let $p = (\mathrm{RX}, N, S, \Gamma)$ be the parameters `parametersOfExtension N S Γ`. **Then** `ExportF KPx (IsBuiltE p.s)` holds: for all large contexts, at each base where `KPx` holds and the twist datum is untwisted, each core in the slot of built points satisfies `ExportAt` (see [export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/)).

## Proof

The proof applies `exportF_isBuiltE_alt_alt` to the 27 hypotheses, $h_L$ and $p$. That theorem needs one more input: at each point, a witness of $p.N = N$, a witness of $\mathrm{RX}$ and `ColPin` give a `TwistNormChoice`. The lemma `nonempty_twOf_of_extensionWithLaw` gives this from inputs 1 and 3, with `extensionWithLaw` in place of $N$. Input 5 converts $N$ into `extensionWithLaw`. `EvG.imp` carries the change under the quantifier "for all large contexts". The rest is bookkeeping.

## In the Lean code

The theorem is at [AutomorphyOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutomorphyOfHyp.lean#L27). It calls:

- `GlobalTheory.ExportFirst.exportF_isBuiltE_alt_alt`;
- `GlobalTheory.T.nonempty_twOf_of_extensionWithLaw`, at [NonGaloisTwistAtLayer.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonGaloisTwistAtLayer.lean#L55). It is itself a renaming of `TwInputs.AtLayer.nonempty_twOf_of_law_rx_colPin`, which we have not opened.

The same file, at [line 44](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutomorphyOfHyp.lean#L44), states `automorphy_of_hypotheses_alt_alt` with the same type and proves it by `exact` of this theorem. So that theorem is a renaming of this one. Its name does not describe the statement: nothing about automorphy appears in it.
