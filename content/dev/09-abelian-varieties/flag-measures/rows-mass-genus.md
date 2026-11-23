---
id: rows-mass-genus
title: The row weights over one local orbit sum to a genus mass
kind: theorem
decl: GlobalTheory.Unfold.GenusRows.rows_mass_genus
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.RowWeightsLocalOrbitsSumEqGenusMass
covers: 773
status: drafted
drafted_by: writer@claude
---
The weights $\mathrm{rw}(c)$ of a local family, summed over the pairs (class, double coset) with local data $d$, give the mass of the genus of $d$. This proves [`rowWeights_localOrbits_sum_eq_genusMass`](/entry/row-weights-local-orbits-sum-eq-genus-mass/). It reindexes the sum and calls [`unfolding_genus_weights_sum_to_mass`](/entry/unfolding-genus-weights-sum-to-mass/); [`weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/) does the counting.

## Statement

Terms $t$, rows $j(t)$, weights $w(t)$, double cosets $\nu(t)$ and local families $F_m$ are as in [the entry on group sums](/entry/squared-group-sum-class-double-coset-eq-row-weight/).

**The mass.** Let $F, F'$ be flags of the [[Hermitian|48P4A1CX85]] space $V$ for $u$ and $u'$, and let $H_0$ be the group of isometries of $V$ that fix each frame vector of $F$ and of $F'$. A global datum $y$ is a local datum $y_p$ at each finite place $p$. Two data are related (`GRel`) if one $h \in H_0$ moves $y_p$ to $y'_p$ at every $p$. The datum $y$ is in the genus of $d$ (`InGen`) if $y_p$ and $d_p$ are in one local orbit (`Datum.Rel`) at each $p$, and $y_p = d_p$ for almost all $p$. Then
$$\mathrm{mass}(d) = \sum_{[y],\ y \in \mathrm{genus}(d)} \frac{1}{\lvert \mathrm{Stab}_{H_0}(y) \rvert} \in [0, \infty],$$
over the classes $[y]$, with $1/\infty = 0$ (`massA`).

**Theorem.** Let $z$ be a point with $\hat Z(F, F') = \mathrm{ptMat}(z)$ and $G(F, F') \neq 0$, with image $\gamma$ in `PN.Pts`. Let $T_S$, $\mathrm{cls}$ and $F_m$ (places $P$, base data $d^0_p$) be given. Assume:

1. the local frames of $F_m$ are the localizations of $F, F'$ (`Based`), and its local data are orbit representatives;
2. in a double coset, the classes of $\mathrm{cls}$ are rows (`ClsRow`);
3. $T_S$ is closed under local moves of the term lattice (`LocClosed`);
4. for $p \notin P$, each $t \in T_S$ at $\gamma$ lies over the orbit of $d^0_p$, and a global lattice $\Lambda_0$ has at $p$ the lattice of a term over $d^0_p$;
5. `FamTie` holds at $\gamma$.

Let $d$ be a value of $\mathrm{dat}$, and $\bar d$ the global datum equal to $d$ on $P$ and to $d^0$ off $P$. Then each $\bar d_p$ has a term over it, and
$$\sum_{(c, n) :\ \mathrm{dat}(c, n) = d} \mathrm{rw}(c) = \mathrm{mass}(\bar d).$$

## Proof

1. **Local facts.** By `exists_complementUnitary_mulAction_localInnerDatum`, the local orbit relation is symmetric and transitive, so two representatives in one orbit are equal (`eq_of_rel_reps`). By `hermitianDatum_eq_of_same_lattice`, two data with terms of one lattice are equal.
2. **Each term is in the genus.** Let $t \in T_S$ be at $\gamma$ over the orbits of $d$. `exists_termLattice_baseFrames_of_basePoint` moves its lattice to the base frames, as $\Lambda$, and `localData_of_term_lattice_and_orbits` gives a datum $y$ over $\Lambda$ in the genus of $\bar d$. Almost all places agree, since $\Lambda$ and $\Lambda_0$ have the same completions at almost all $p$ (`hermitianLattice_local_global_principle`).
3. **Reindexing.** Let $K$ be the set of keys $(j(t), \nu(t))$ of the terms of step 2. Send $(c, n)$ to the key of a chosen term of class $c$ and coset $n$. This map is injective by `ClsRow`, and onto $K$ by step 1, since a term over the genus of $\bar d$ has local data $d$. The weights agree, as $w(t)$ depends only on the row.
4. **The sum.** [`unfolding_genus_weights_sum_to_mass`](/entry/unfolding-genus-weights-sum-to-mass/) gives $\sum_{\kappa \in K} w^2 = \mathrm{mass}(\bar d)$.

## In the Lean code

The theorem is in [RowWeightsLocalOrbitsSumEqGenusMass.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowWeightsLocalOrbitsSumEqGenusMass.lean#L74). The mass and the relations are in [LocClosed.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LocClosed.lean#L79). The sums are in $[0, \infty]$ (`ENNReal.ofReal`), and $\lvert \mathrm{Stab} \rvert$ is `Set.encard`.

- The local orbit relation is proved to be an equivalence here (`rel_symm`, `rel_trans`), and again below, in [`weights_add_up_to_mass`](/entry/weights-add-up-to-mass/), by `relEqv`.
- We have not unfolded `Datum.Rel`, `IsTermOver`, `lattice₂` or `frFac`.
