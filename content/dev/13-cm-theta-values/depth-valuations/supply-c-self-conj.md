---
id: supply-c-self-conj
title: Row data and the block bound at self-conjugate places
kind: theorem
decl: GlobalTheory.RowAt.supplyC_selfConj
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.RowDataSuppliedAtSelfConjugatePlaces
covers: 302
status: drafted
drafted_by: writer@claude
---
This theorem builds, from a chart at an integral point, one row datum for each orbit of a labelling of the embeddings, and proves the block bound `ValBlocksC` on $\nu$ for them. Its alias [`rowData_supplied_at_selfConjugate_places`](/entry/row-data-supplied-at-self-conjugate-places/) gives the result to [`exists_rowFam`](/entry/exists-row-fam/). The proof assembles twelve lemmas. The main inputs are a character bound, the only place where `UpFSt` is used, and a bound of chart values on products.

## Statement

Use the setting of [the entry for `goodPrime_packages`](/entry/good-prime-packages/).

**Theorem.** Assume `UpFSt p` for all primes $p$, and that the involution on $\mathcal{O}_E$ is the conjugation of $H$. Let $T$ be a complete discrete valuation ring with a map $F \to \operatorname{Frac} T$, $y$ an algebraic integral point of $X$ over $T$, and $C_3$ a chart at $y$. Let $C$ be a field of characteristic $0$ with a valuation $V$ of residue characteristic $\ell$, $\iota \colon \operatorname{Frac} T \to C$ with `EmbOK`, and $Y$ a chart over $C$ tied to $C_3$ by `IsBC` at level $k$. Let $\mathrm{Orb}$ be a finite set and $\tau \colon \mathrm{Orb} \times \mathbb{Z}/2 \to (E \to \mathbb{C})$ a labelling with ranks $n, j, j'$ such that:

1. (`ArithS`) $\tau$ is injective, $\tau(o, s+1) = \overline{\tau(o,s)}$, $\tau(o,s+1)(x) \equiv \tau(o,s)(x)^\ell$ modulo the maximal ideal of $V$ after the embeddings into $C$, and $\ell \nmid \operatorname{disc} E$;
2. $\tau$ is onto;
3. (`RankOK`) $\mathrm{mult}\,\tau(o,0) = n + j$ and $\mathrm{mult}\,\tau(o,1) = j'$;
4. $j' < n$.

Let $a$ be a dominant weight, $n_W \in \mathbb{N}$ and $\nu \le$ `nuLocC` $C_3$ at the exponent of $V$, level $k$, weight $a$ and $n_W$. Then `SupplyC` holds: for each $o$ there are a row datum $X_o$ with $d = 2$ and a flag $F_o$ such that $X_o$ has sizes $n$ and $j + j'$, is alternating, and has ranks $\operatorname{rk} X_o(0,s) = \mathrm{mult}\,\tau(o,s)$; and `ValBlocksC` holds for these rows, $n_W$, the gap weights $\mathrm{gap}(\mathrm{mult}\,\tau(o,s), a(\tau(o,s),\cdot))$ and $\nu$.

[The entry for `exists_rowFam`](/entry/exists-row-fam/) explains `ValBlocksC`; [the entry for `packages_conj`](/entry/packages-conj/) defines $\mathrm{gap}$.

## Proof

1. `exists_selfConjugatePlaceData_intChart` gives self data $p_o$ on $Y$ for each orbit, tied to $\tau$ (`IsSelfOf`), separated (`SelfSep`), and, under `RankOK`, with the rank and alternating conditions.
2. The raw chart of each $p_o$ gets its hypotheses `Hyps`: five formal statements from `rowLaw_formal_statements_selfConjugate`; the nondegeneracy of $Y$ from `biextension_nondegenerate_mod_maximalIdeal_integral_chart`, which gives the rank conditions through `rankMaximal_rawSelf_of_ndg`; and the character bound from `characterBound_selfConjugate_degreeTwo_integralChart`, which uses `UpFSt`.
3. The rows $X_o$ are the row data of these raw charts. `flag_of_letterNumbering_rowData` gives the flags and the ranks.
4. `RF.valBlocksC_G` with $n_W/2$ gives `ValBlocksC` from four inputs: the value bound `chartValues_bound_products_on_planes` (after `nuLocC_le_nuPlE_baseChange` turns the bound on $\nu$ into a bound by `nuPlE` of $Y$), the jet product rule `jetProd`, the block membership `blockProd_mem_at_selfConj_places`, and the admissibility `RF.blkAdmC`. Admissibility uses $j' < n$, the alternating rows, and $\mathrm{gap}(i) = 0$ for $i > \mathrm{mult}$.

## In the Lean code

The theorem is in [RowDataSuppliedAtSelfConjugatePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/RowDataSuppliedAtSelfConjugatePlaces.lean#L32). The lemmas it calls, all with the prefix `GlobalTheory.T.` except the last four:

- `exists_selfConjugatePlaceData_intChart`, `rowLaw_formal_statements_selfConjugate`, `biextension_nondegenerate_mod_maximalIdeal_integral_chart`, `rankMaximal_rawSelf_of_ndg`;
- `characterBound_selfConjugate_degreeTwo_integralChart`, `flag_of_letterNumbering_rowData`, `chartValues_bound_products_on_planes`, `blockProd_mem_at_selfConj_places`;
- `GlobalTheory.nuLocC_le_nuPlE_baseChange`, `GlobalTheory.JetProd.jetProd`, and `RF.valBlocksC_G` in [BlockMembershipSelfConjugate.lean](lean:Formalism/LocalToGlobal/CharacterGerms/BlockMembershipSelfConjugate.lean#L234), `RF.blkAdmC` in [RowTieAdm.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RowTieAdm.lean#L190).

The file also defines `pairCols`, the embedding $(i, b) \mapsto 2i + b$, and `tyShift`. `SupplyC`, `LabS`, `ArithS` and `IsSelfOf` are in [IsSelfOf.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/IsSelfOf.lean#L36). We have not unfolded the five formal statements, `NDG`, `SelfSep`, the character bound `CHSt`, `nuPlE` or `IsBC`. All hypotheses of the theorem are used.
