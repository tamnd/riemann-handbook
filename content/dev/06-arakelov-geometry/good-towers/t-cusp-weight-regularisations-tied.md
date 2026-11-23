---
id: t-cusp-weight-regularisations-tied
title: A cusp weight with tied regularisations, restated
kind: theorem
decl: GlobalTheory.T.cusp_weight_regularisations_tied
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.CuspWeightRegularisationsTiedStatement
covers: 686
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the relay theorem](/entry/relay-cusp-weight-regularisations-tied/), which collects the lemmas that do the work. It has two users. The first is [`base_setting_of_good_origin`](/entry/base-setting-of-good-origin/), which builds a base degree setting on each component of a good tower; through it the result reaches [the volume theorem](/entry/volume-theorem-x-of-inputs/). The second is `SheetDecomposition.muMass` in the folder WeilBound.

## Statement

The statement is word for word that of the [relay theorem](/entry/relay-cusp-weight-regularisations-tied/), which defines the objects. In short: assume `Top.Given`. For each component datum $D_c$ with Hodge datum $H_d$ and component origin $O$ over an abelian CM field, there are a cusp weight $U \geq 0$ for $O$, invariant under the torus $(\mathbb{C}^\times)^K$ on $X^o$, a complex model $M$, a tied log-log regularisation $S$ of the Hodge line $\overline\mu$ and a tied bounded regularisation $S'$ with potential $\log h_\mu + U/2$, whose twisted lines are invariant under complex conjugation (`ConjU`).

## Proof

The proof applies `Relay.cusp_weight_regularisations_tied`. Nothing else happens.

## In the Lean code

The theorem is in [CuspWeightRegularisationsTiedStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/CuspWeightRegularisationsTiedStatement.lean#L22). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Relay.cusp_weight_regularisations_tied | ...
```

The name says "regularisations tied", but the statement also produces the cusp weight $U$, which is the main object for its users. `base_setting_of_good_origin` uses all six conclusions; `muMass` uses four of them and discards the cusp weight property and `ConjU`.
