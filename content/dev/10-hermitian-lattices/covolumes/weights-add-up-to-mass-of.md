---
id: weights-add-up-to-mass-of
title: Unfolding the mass of a genus into squared row weights
kind: theorem
decl: GlobalTheory.Unfold.SumK.weights_add_up_to_mass_of
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnfoldingGenusWeightsSumToMass
covers: 732
status: drafted
drafted_by: writer@claude
---
This theorem unfolds the mass of a genus of global data into a sum of squared row weights over the keys (row, double coset) of terms. It has two hypotheses on local orbits, which [`weights_add_up_to_mass`](/entry/weights-add-up-to-mass/) discharges. [`rows_mass_genus`](/entry/rows-mass-genus/) uses it through [`unfolding_genus_weights_sum_to_mass`](/entry/unfolding-genus-weights-sum-to-mass/).

## Statement

The group $H_0$, global data, the relation $y \sim y'$ (`GRel`), the genus and $\mathrm{mass}(d)$ are as in [the entry for `rows_mass_genus`](/entry/rows-mass-genus/). The terms $t$, rows $j(t)$, weights $w(t)$ and double cosets $\nu(t)$ are as in [the entry on group sums](/entry/squared-group-sum-class-double-coset-eq-row-weight/). Let $F, F'$ be flags for $u, u'$ and $z$ a point with $\hat Z(F, F') = \mathrm{ptMat}(z)$ and $G(F, F') \neq 0$. Further:

- $t$ *moves to* $\Lambda$ (`TG`) if one isometry $g$ is adapted from the standard flag of $u$ to $F$ and from the frame of $t$ to $F'$, and $\Lambda = g(\lambda(t))$;
- $y$ *lies over* $\Lambda$ (`LocOver`) if $\Lambda$ is a lattice and each $y_p$ has a term with lattice $\Lambda_p$;
- the key of $t$ is $(j(t), \nu(t))$.

The hypotheses are: ($h_{\mathrm{Rel}}$) at each place the local orbit relation is an equivalence; ($h_{\mathrm{Inv}}$) if $y$ lies over a lattice, $y$ is in the genus of $d$, and $y \sim y'$, then $y'$ is in the genus of $d$.

**Theorem.** Assume $h_{\mathrm{Rel}}$ and $h_{\mathrm{Inv}}$. Let the local frames be the localizations of $F, F'$ (`Based`) with `RelG` at each place. Let $T_S$ be closed under local moves of the moved lattice (`LocClosed`). Let $t_0 \in T_S$ move to $\Lambda_0$, let $y_0$ lie over $\Lambda_0$, and let $y_0$ be in the genus of $d$. Let
$$K = \{\mathrm{key}(t) : t \in T_S,\ t \text{ moves to } \Lambda,\ y \text{ lies over } \Lambda,\ y \in \mathrm{genus}(d)\},$$
and let $\omega \colon K \to \mathbb{R}$ satisfy $\omega(\kappa) = w(t)^2$ for each $t$ with key $\kappa$. Then
$$\sum_{\kappa \in K} \omega(\kappa) = \mathrm{mass}(d) \quad \text{in } [0, \infty].$$

## Proof

`rationalClass_lattices_iff_rationalClass_localFramePairs` says that $\sim$ is an equivalence, that stabilizer sizes are constant on classes, and that for $y_i$ over $\Lambda_i$: $\Lambda_1, \Lambda_2$ are related by $H_0$ (`LRel`) if and only if $y_1 \sim y_2$, and $\mathrm{Stab}(\Lambda_1) = \mathrm{Stab}(y_1)$.

Send each $\kappa \in K$ to the class $\varphi(\kappa)$ of a chosen datum $y$ for it. This is well defined: two terms with one key have related lattices (`same_row_doubleCoset_inner_data_one_rational_class`). Split the sum into fibres of $\varphi$. Fix a class $o$ with representative $y$.

1. If $y$ is not in the genus of $d$, the fibre is empty by $h_{\mathrm{Inv}}$, and the class adds $0$ to both sides.
2. If $y$ is in the genus, then $y$ is in the genus of $y_0$ (`inGen_symm_of`, with $h_{\mathrm{Rel}}$). `genusFamily_carried_by_lattice_in_localOrbits` gives a lattice $\Lambda_1$ under $y$, locally in the orbits of $\Lambda_0$. `exists_rowTerm_of_local_completions_terms` gives a term $t_1$ that moves to $\Lambda_1$, and `LocClosed` puts $t_1$ in $T_S$.
3. `orbitCount_rows_doubleCosets_innerDatum_class` at $(t_1, \Lambda_1)$: the set $K_1$ of keys of terms that move to a lattice related to $\Lambda_1$ is finite, all these terms have weight $w(t_1)$, and $\lvert K_1 \rvert \, w(t_1)^2 = 1/\lvert \mathrm{Stab}(\Lambda_1) \rvert$.
4. The fibre over $o$ is $K_1$, so its sum is $\lvert K_1 \rvert \, w(t_1)^2 = 1/\lvert \mathrm{Stab}(y) \rvert$, the term of $o$ in $\mathrm{mass}(d)$.

## In the Lean code

The theorem is in [UnfoldingGenusWeightsSumToMass.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnfoldingGenusWeightsSumToMass.lean#L28). The definitions are in [LocClosed.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LocClosed.lean#L63). The five lemmas are statement forms of `Unfold.ratCls_agree`, `KeyRel.same_key_lrel`, `GlueOrbit.glue_local_orbits`, `RowTermReal.exists_term_of_locOver` and `OrbitCount.orbit_count`. We have not opened their proofs. The fibre decomposition is `ENNReal.tsum_fiberwise`. The point $z$ and its hypotheses only pass to these lemmas.
