---
id: exists-row-fam
title: A row family at a prime where Frobenius is complex conjugation
kind: theorem
decl: GlobalTheory.PkgConj.exists_rowFam
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PackagesExistFrobeniusComplexConjugation
covers: 315
status: drafted
drafted_by: writer@claude
---
This lemma labels the embeddings of the CM field $E$ by pairs $(z, s)$ of a place $z$ and a sign $s \in \mathbb{Z}/2$, at a prime where Frobenius acts as complex conjugation. It then gets row data with a block bound on $\nu$. Its one user is [`packages_conj`](/entry/packages-conj/), which turns the result into two packages. The rows and the bound come from [`rowData_supplied_at_selfConjugate_places`](/entry/row-data-supplied-at-self-conjugate-places/). The work here is to choose a field, a chart and a labelling, and to check their conditions.

## Statement

Use the setting of [the entry for `packages_conj`](/entry/packages-conj/): the places $z$, the map $p_l$, the labels $\tau(z,0) = p_l(z)$ and $\tau(z,1) = \overline{p_l(z)}$, the multiplicity $\mathrm{mult}$ and the gap weights $g(z,s,i)$.

**Theorem.** Assume `UpFSt p` for all primes $p$. In the setting of `AllPts`, assume `PhiC N ℓ`. Then:

1. $(z,s) \mapsto \tau(z,s)$ is a bijection onto the embeddings $E \to \mathbb{C}$;
2. there is a row family $R$ for `parOf N j ℓ`, with $d = 2$, such that each row $R_z$ is alternating, its rank $\operatorname{rk} R_z(0,s)$ is $\mathrm{mult}\,\tau(z,s)$, and `ValBlocksC` holds for the rows, $n_W$, the weights $g$ and $\nu$.

A row family is a field $C$ with a valuation of residue characteristic $\ell$, and for each place $z$ a row datum $R_z$ (`RowData`, with $n = k-1$ and $m$ as given) with a flag. `ValBlocksC` says: for each choice of lists of blocks on the rows, where each block attains its value, each monomial block sits on one sign, twice the total width is at most $n_W$, and the weights of the blocks at $(0,s)$ and $(1,s+1)$ add up to $g(z,s,\cdot)$, the number $\nu$ is at most the sum of the values.

## Proof

1. `exists_closed_field_over_place` gives an algebraically closed field $C$ of characteristic $0$, complete for a valuation $V$ with residue characteristic $\ell$, and an embedding $\iota$ of the fraction field of the discrete valuation ring into $C$. It turns $e_\lambda \nu \le$ `nuLocC` into $\nu \le$ `nuLocC` for $V$.
2. `ChartBaseChange.exists_baseChange` gives a chart $Y$ over $C$ at the level $M$. It needs $\ell \ne 2$ (as $\ell$ is not small), the trace identity $w_0 + \bar w_0 = 1$ of the host (`cmHost_idempotent_trace_eq_one`), and that $M$ is a unit at $\ell$.
3. `LabSelf.arithS_tauC` proves that the labelling $(\tau, k-1, j, m-j)$ satisfies `ArithS` (injective, $\tau(z,s+1) = \overline{\tau(z,s)}$, the Frobenius congruence, $\ell \nmid \operatorname{disc} E$) and is onto. Here `PhiC` is used.
4. `RankOK`: $\mathrm{mult}\, \tau(z,0) = p = (k-1) + j$ and $\mathrm{mult}\, \tau(z,1) = q = m - j$. The second uses `not_inPsi_conj`: the conjugate of an embedding in the image of $p_l$ is not in it.
5. `rowData_supplied_at_selfConjugate_places` with $m - j < k - 1$, which holds as $m + 3 \le k$. It gives the rows, the flags and `ValBlocksC`. The rest is bookkeeping.

## In the Lean code

The lemma is in [PackagesExistFrobeniusComplexConjugation.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PackagesExistFrobeniusComplexConjugation.lean#L25). The lemmas it calls:

- `GlobalTheory.PlaceClosedField.exists_closed_field_over_place` in [ExistsClosedCompleteFieldOverPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ExistsClosedCompleteFieldOverPlace.lean#L49);
- `GlobalTheory.ChartBaseChange.exists_baseChange` in [IsCanonGaugeMapFB.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/IsCanonGaugeMapFB.lean#L39);
- `GlobalTheory.QuadTrace.cmHost_idempotent_trace_eq_one`;
- `GlobalTheory.LabSelf.arithS_tauC` and `not_inPsi_conj` in [NotInPsiConj.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/NotInPsiConj.lean#L69);
- `GlobalTheory.T.rowData_supplied_at_selfConjugate_places`.

`tauC`, `LabS`, `ArithS` and `RankOK` are in [IsSelfOf.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/IsSelfOf.lean#L74), `RowFam` in [RestNonneg.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RestNonneg.lean#L44), and `ValBlocksC` in [ContentZeroAt.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentZeroAt.lean#L129). We have not unfolded the blocks, `nuLocC` or the chart types.

`UpFSt` is only passed on. The hypotheses $\ell \ne q_N$, $\ell \ne d_N$ and ($\ell$ inert $\Rightarrow 5 \le \ell$) from `AllPts` are introduced as `_` on line 32 and not used.
