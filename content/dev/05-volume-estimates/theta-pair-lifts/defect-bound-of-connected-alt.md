---
id: defect-bound-of-connected-alt
title: The defect bound below the core slope at a point
kind: theorem
decl: GlobalTheory.CovTop.DefCore.defect_bound_of_connected_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DefectBoundOfConnected
covers: 867
status: drafted
drafted_by: writer@claude
---
This theorem bounds the core slope at the last level from below by twice the number $\mathrm{defBound}$, at one point and in the case `FnAlgClosed`: the coefficient field is algebraically closed in the function field of each component of the moduli space at level $i + 1$. It compares the core slope with the slope of a lattice of eigenforms of a finite group. Its only user is [the level statement](/entry/lifts-two-mul-def-bound-sub-unit-e-le-mu-core/) of the same bound, which feeds [the low defect bound](/entry/covering-low-defect-alt/). Below this theorem are 867 declarations.

## Statement

Fix a point $p$ and a level $i$ with $i + 1 = m$. Let $\mathcal{D}$ be the datum at level $i + 1$, with signature $(p_i, q_i)$, let $(a, n)$ be the weight of the point, and let $\Psi$ be the index set `Psi H` of embeddings $\tau$ of the CM field $E$. For a real $c_1$ the Lean code sets

$$\mathrm{defBound}(c_1) = \sum_{\tau \in \Psi} \Bigl( \bigl(\tfrac{|a_\tau|}{p_i} + \tfrac{n}{2}\bigr) c_1 - \tfrac12 \log \dim a_\tau \Bigr) + n\,|\Psi|\,p_i \Bigl( \tfrac{\log 2\pi}{4} - \tfrac{\mathrm{lrd}(E)}{2} \Bigr),$$

where $|a_\tau|$ and $\dim a_\tau$ are the numbers `size` and `dim` of the part of $a$ at $\tau$. We have not unfolded them or `lrd`. Let $\mathrm{flatDegVal} = \tfrac{p_i - q_i}{2}\log\Omega + q_i(\log d - \mathrm{lrd}(E))$ as in [the renaming](/entry/two-mul-def-bound-sub-le-mu-core-of-gram-at/).

**Theorem.** Assume `PublishedHodgeBundleTheorems`. Then there are $M$ and $C_0 \ge 0$ such that for each point $p$ with `RowsTAlt`, each $i$ with $i + 1 = m$, and all $P, A$: if `GramAt`, `WtNum` with $P$, `HostNum` with $P, A, M$ and `FnAlgClosed` at level $i + 1$ hold, then
$$2\,\mathrm{defBound}(-\mathrm{flatDegVal}) - C_0 u \le \mu_{\mathrm{core}}(p, i).$$

The proof takes $M = 0$ and $C_0 = 0$.

## Proof

1. `finite_nonempty_components_and_dict_mem_dom` gives `DefCase`, the definite case: $q_i = 0$, $p_i \ge 1$, the level is good at all primes, the coefficient field is algebraically closed in each function field, and three conditions on the uniformizations. It also says that the set of components is finite and not empty.
2. `exists_finite_group_actLev_char` gives a finite group $G$ that acts on the level structure (`ActLev`) and freely on points (`FreePt`), and a character $\chi \colon G \to F^\times$. Let $\Lambda_\chi$ be the lattice of cusp forms of weight $G_k$ that are $\chi$-eigenvectors (`eigLat`). The theorem gives $\mu(\Lambda_\chi) \le \mu_{\mathrm{core}}(p, i)$, for the slope $\mu$ in the norm `normW`.
3. [flatExistsAt_last_index_of_fnAlgClosed](/entry/flat-exists-at-last-index-of-fn-alg-closed/) says that each component carries flat sections, all of degree $\mathrm{flatDegVal}$.
4. `eigenlattice_slope_lower_bound_definite_case`, from 1, 2, 3 and `GoodW` (part of `GramAt`), gives $\Lambda_\chi \ne 0$ and $\mathrm{defBound}(-\mathrm{flatDegVal}) \le \mu(\Lambda_\chi)/2$.

Then $2\,\mathrm{defBound} \le \mu(\Lambda_\chi) \le \mu_{\mathrm{core}}$, by `linarith`.

## In the Lean code

The theorem is at [DefectBoundOfConnected.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DefectBoundOfConnected.lean#L21). It calls:

- `GlobalTheory.T.finite_nonempty_components_and_dict_mem_dom`, a renaming of `defCase_core_alt`;
- `GlobalTheory.T.exists_finite_group_actLev_char`, a renaming of `exists_finite_group_lev_char_slope`;
- `GlobalTheory.T.flatExistsAt_last_index_of_fnAlgClosed`;
- `GlobalTheory.T.eigenlattice_slope_lower_bound_definite_case`, a renaming of `GlobalTheory.DefPt.eigLat_slope_definite`.

The hypothesis `PublishedHodgeBundleTheorems` is named `_hP` and is not used. The existential over $M$ and $C_0$ is a wrapper: the proof sets both to $0$, so the bound holds with no error term. We have not opened the proofs of the four lemmas. The main estimate is in `eigLat_slope_definite`.
