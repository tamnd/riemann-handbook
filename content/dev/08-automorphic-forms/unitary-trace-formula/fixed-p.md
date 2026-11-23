---
id: fixed-p
title: The class count for one characteristic polynomial
kind: theorem
decl: GlobalTheory.PreStabU.fixedP
module: Development.WeilBound.CoreStatements.AutomorphicKernels.IsobaricBaseChange.IntegralCoefficientBaseChange.UnitaryBaseChangeCharacters.UnitaryBaseChangeLinks.UnitaryGeometricSideSeparableTest
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem is step 3 of [the rational geometric side of the unitary trace formula](/entry/geom-urat-eq-geom-u/). For one polynomial $P \in \mathrm{Ell}_n$, it turns the sum of orbital integrals over the rational classes with characteristic polynomial $P$ into a sum over the factorizations $P = P_1 P_2$ of signed local sums.

## Statement

Let $E$, $n$, $S$, the level family $K'$ and the test function $f$ be as in the parent entry, and let $P \in \mathrm{Ell}_n$.

**Theorem.** Only finitely many rational conjugacy classes $c$ of $U(E)$ with characteristic polynomial $P$ have $\prod_{w \in S} O_w(c) \ne 0$, and

$$2^{\mathrm{nfac}(P)} \sum_{\chi_c = P} \prod_{w \in S} O_w(c) = \sum_{\substack{P_1, P_2 \text{ monic} \\ P_1 P_2 = P}} \prod_{w \in S} O^\kappa_w(P_1, P_2).$$

## Proof

Let $\mathrm{Fac}(P)$ be the set of ordered monic factorizations $P = P_1P_2$; it is finite (`monic_divisor_sign_sum`). For each $w$, the set of local classes with characteristic polynomial $P$ is finite (`finite_twisted_classes_charpoly`), and $K_w$ is compact. Call a local class good if it is conjugate into $K_w$.

The proof applies the counting lemma `GlobalTheory.T.adelic_class_count_product`, whose statement we have not unfolded, to the map $r \mapsto (\text{class of } r \text{ at } w)_w$ from rational classes to families of local classes. It checks five inputs:

1. At almost all $w$, exactly one local class is good, the orbital integral of $f_w$ at a local class is $1$ if the class is good and $0$ if not, and the signs $\kappa_w(Q, \cdot)$ of the good class are $1$ for each divisor $Q$ of $P$ (`ae_good`, from the test function being the indicator of $K_w$ at almost all $w$).
2. At each $w \notin S$, the place is split, and some local element has characteristic polynomial $P$ (`elliptic_charpoly_local_realisation`).
3. A rational class is good at almost all $w$ (`local_points_integral_almost_all`).
4. Two rational classes with characteristic polynomial $P$ that agree at every $w \in S$ are equal (`unitary_conjugacy_sign_product`).
5. **The sign sum** (`signs`). For a family $x = (x_w)$ of local classes, good at almost all $w$,

$$\sum_{(P_1, P_2) \in \mathrm{Fac}(P)} \prod_{w \in S} \kappa_w(P_1, x_w) = \begin{cases} 2^{\mathrm{nfac}(P)} & \text{if a rational class has the local classes } x_w \text{ for all } w \in S, \\ 0 & \text{otherwise.} \end{cases}$$

Its proof uses `monic_divisor_sign_sum`, `unitary_conjugacy_sign_product` and `kappa_sign_multiplicative`.

The lemma gives finiteness and the identity, with each orbital integral taken at a representative of the local class. Orbital integrals are invariant under conjugation (`twOrb_conj`), and the sum over local classes with the sign is $O^\kappa_w$ (`kapOrb_eq`). The rest is bookkeeping.

## In the Lean code

The theorem is in [UnitaryGeometricSideSeparableTest.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryGeometricSideSeparableTest.lean#L357), with `signs` at [line 263](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryGeometricSideSeparableTest.lean#L263). The global facts on unitary groups (`unitary_conjugacy_sign_product`, `elliptic_charpoly_local_realisation`, `kappa_sign_multiplicative`) come from the namespace `GlobalTheory.T`; we have not unfolded them.
