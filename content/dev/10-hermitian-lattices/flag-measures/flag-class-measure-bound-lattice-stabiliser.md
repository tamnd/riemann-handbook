---
id: flag-class-measure-bound-lattice-stabiliser
title: The bound for one flag class, a second name
kind: theorem
decl: GlobalTheory.T.flagClass_measure_bound_lattice_stabiliser
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.FlagClassMeasureBoundLatticeStabiliserStatement
covers: 782
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the bound for one flag class](/entry/bound/). That entry has the content. Its user is [`unfoldBound`](/entry/unfold-bound/), which sums it over the slices of a flag type.

## Statement

**Theorem.** Let $G$, $G_0$ be unitary groups over the same CM field, and let $(x_f, S, \Lambda, x_0, T, T', T_0)$ be an adapted model of an isotropic flag of type $j$ (`IsAdapted`, described in [`unfoldBound`](/entry/unfold-bound/)). Let $G$ have signature $(p,q)$, let $c, c_0$ be gauges and let $B$ be a measurable set of increasing $\tau \in (0,1/2)^a$. Then the gauge covolume of $\{g \in G_\infty : \mathrm{sizes}(g) \in B\}$ modulo the arithmetic group that preserves the flag is at most

$$c_{\mathrm{Iw}}^f\, r_d^{f d_N/2} \prod_i 2^{f j_i^2} \mathrm{vol}(\Lambda_i) \cdot \mathrm{vol}_{x_0}(G_0) \int_B \mathrm{dens}(\tau)\, d\tau.$$

The two volumes are defined in [the bound for one flag class](/entry/bound/).

## Proof

The proof applies `GlobalTheory.FlagBase.OneClass.bound`, which has the same statement.

## In the Lean code

The theorem is in [FlagClassMeasureBoundLatticeStabiliserStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagClassMeasureBoundLatticeStabiliserStatement.lean#L6). The statement is written out in full, with the same text as `bound`. The proof is a `first | exact ... | ...` combinator with three tries, and each try applies the same lemma. The file sets `maxHeartbeats 1000000`, which is not needed. The word "lattice stabiliser" in the name refers to the condition $x_f^{-1} \gamma x_f \in K_f$ in the arithmetic group.
