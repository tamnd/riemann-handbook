---
id: label-set-geo-of-even-of-rank-ok-of-not-dvd-discr
title: Self-conjugate row data and the block bound from an arithmetic labelling
kind: theorem
decl: UpperTheory.labelSetGeo_of_even_of_rankOK_of_not_dvd_discr
module: Development.AutomorphicArithmetic.OrbitLabellings.LabelSetGeoOfEvenOfRankOKOfNotDvdDiscr
covers: 1949
status: drafted
drafted_by: writer@claude
---
This theorem takes an arithmetic labelling of the embeddings of a CM field $E$ at a prime $l$ and builds one row datum for each orbit. It also proves the lower bound `ValBlocksS` on $\nu$ by blocks. Its one user is [`exists_rowFamS`](/entry/exists-row-fam-s/), which supplies the labelling at an inert prime of odd order. The proof is an assembly of many lemmas. The real content is in those lemmas, mostly `blkMemS_selfConjugate_places_of_CMDatum`, `RF.valO_self` and `labelSet_ev_of_geo_of_not_dvd_discr`.

## Statement

Use the setting $E, H, D, X, c$ of [the entry for the packages](/entry/exists-pkg-cs-of-degree-bound-at-inert-primes/), with `star` equal to the conjugation of $H$. Let $T$ be a complete discrete valuation ring over $c$, $y$ an algebraic integral point over $T$ and $C_3$ an integral chart at $y$. Let $C$ be a field of characteristic $0$ with a valuation $V$ (residue prime $l$) and an embedding $\iota$ of the fraction field of $T$ that satisfies `EmbOK`. Let $Y$ be a chart over $C$ that is the base change of $C_3$ at $k$ (`IsBC`).

A labelling `LabS` gives maps $\tau(o,\cdot) \colon \mathbb{Z}/d \to (E \to \mathbb{C})$ for $o$ in a finite set, a shift $h$, $2 \times 2$ matrices $g_m$, numbers $n, j, j'$ and a predicate `big`. `LabSArith` says: $\tau$ is injective; $h \ne 0$ and $2h = 0$; $\overline{\tau(o,s)} = \tau(o,s+h)$; $\tau(o,s+1)(x) \equiv \tau(o,s)(x)^l$ modulo the maximal ideal; and four more conditions on separation, an idempotent and the matrices $g_m$.

**Theorem.** Assume `UpFSt p` for all primes $p$, and `LabSArith`. Assume $l \nmid \mathrm{disc}(E)$, $d$ even, `RankOK` (the multiplicity of $D$ at $\tau(o,s)$ is $n+j$ when `big o 0 s` holds and $j'$ when it fails, with the same rule shifted by $h$ for the second row), `big o 0 s` if and only if $s$ is even, and $j' < n$. Let $g$ be weights with $g(o,s,k) \ne 0$ only for $1 \le k \le \mathrm{mult}\,\tau(o,s)$, tied to $a$ by `WtTieS`. Let $\nu \le$ `nuLocC` at $C_3$. Then there are row data $X_o$ over $C$ on the index set $\Sigma_s \mathrm{Fin}(\mathrm{mult}\,\tau(o,s))$, and flags $F_o$, with $n(X_o) = n$, $m(X_o) = j + j'$, `Alt`, and `rkF 0 s` equal to $\mathrm{mult}\,\tau(o,s)$. Also `ValBlocksS` $h\ X\ F\ n_W\ g\ \nu$ holds.

## Proof

1. `labelSetGeo_of_labelSetArith` turns `LabSArith` into `LabSGeo`: integral Lie basis vectors of $Y$ on which $O_E$ acts through $\tau(o,s)$, and two more conditions.
2. The proof fills the fields of `RawChart.Hyps` for each orbit from chart lemmas. The field `CH` comes from `labelSet_ev_of_geo_of_not_dvd_discr`, the only place that uses `UpFSt` and $l \nmid \mathrm{disc}(E)$.
3. $X_o$ is `rdS` of these charts, and $F_o$ is the standard flag. The rank facts follow by unfolding `rkF`, and `Alt` is $d$ even with the rule for `big`.
4. `RF.valO_self` with `descent_holds` gives a valuation bound with $n = \lfloor n_W/2 \rfloor$. `blkMemS_selfConjugate_places_of_CMDatum` gives block membership. `valBlocksS_of_blkMemS` combines them into `ValBlocksS`.

## In the Lean code

The theorem is in [LabelSetGeoOfEvenOfRankOKOfNotDvdDiscr.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/LabelSetGeoOfEvenOfRankOKOfNotDvdDiscr.lean#L25). `LabS`, `LabSArith`, `LabSGeo` and `RankOK` are in [SelfConjugateRowData.lean](lean:Formalism/LocalToGlobal/CharacterGerms/SelfConjugateRowData.lean#L20). The lemmas of step 4 are in [ValBlocksCChart.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ValBlocksCChart.lean#L26), [BlkMemSSelfConjugatePlacesOfCMDatum.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/BlkMemSSelfConjugatePlacesOfCMDatum.lean#L917) and [ValBlocksSOfBlkMemS.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/ValBlocksSOfBlkMemS.lean#L13). We have not unfolded `RowData`, `rdS`, `CHSt`, `nuLocC` or the chart types.

The name says "labelSetGeo", but the conclusion is row data and `ValBlocksS`, not `LabSGeo`. `LabSGeo` needs none of the three hypotheses in the name. The hypothesis `y.IsAlg` goes only to [`labelSet_ev_of_geo_of_not_dvd_discr`](lean:Development/AutomorphicArithmetic/OrbitLabellings/LabelSetEvOfGeoOfNotDvdDiscr.lean#L24), which drops it with `_`. That lemma also drops "$d$ even" and the rule for `big`.
