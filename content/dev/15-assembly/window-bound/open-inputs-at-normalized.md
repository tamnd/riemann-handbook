---
id: open-inputs-at-normalized
title: The five open inputs for the normalized family
kind: theorem
decl: Formalism.MainNotions.N.K.Closed.open_inputs_at_normalized
module: Formalism.AdmissibleDesigns.StatementOneBFromUnramified
covers: 455
status: drafted
drafted_by: writer@claude
---
This theorem proves the five statements of the last layer `RemainingInputsLastLayer` for one ring datum. Its only caller is [the congruence length bound from the local inputs](/entry/theorem-n5-from-inputs/). The proof moves the hypotheses from $r$ to the normalized family $r^{\mathrm{N}}$ and calls one lemma for each statement.

## Statement

The notation is that of [the parent entry](/entry/theorem-n5-from-inputs/): a datum $D$, an index $i$, families $r_x$ of rank $n_V$ and $\rho_x$ of rank $r$ over $\mathcal{O}$, and a point $\pi$. Let $\chi_1, \dots, \chi_t$ be the characters of $D$ at $i$. The *normalized family* $r^{\mathrm{N}}$ (`Norm.rN`) is $r$ at each $x \neq \pi$, and at $\pi$ it is the block diagonal representation

$$ r^{\mathrm{N}}_\pi = \rho_\pi \oplus \chi_1 \oplus \dots \oplus \chi_t. $$

Fix a declaration `dc`, an element $g_0$, matrices $e_B, e_1, s$, a constant $c_B$, and a ring datum `Dd` with `RingDef` for $r^{\mathrm{N}}$. Assume that $r^{\mathrm{N}}$ is continuous, that `Dd` has the topology `Dd.Top`, and that the first summand has rank 1 over the fraction field of $\mathcal{O}$.

**Theorem.** Assume `admG2`, `admG4`, `admG5` for $r$, `TameGeneratorConditions`, `SemisimpleDecomposition` (over the fraction field, $r_\pi \cong \rho_\pi \oplus \chi_1 \oplus \dots \oplus \chi_t$), `FontaineAtPlacesOverL`, `tateH1FinitenessAtPlacesOver`, `LocalCoefficientCompatibility`, `SelfGood`, `QPow` and `admTB` for $r^{\mathrm{N}}$. Then `RhoOpenA`, `TBOpen`, `ChiOpen`, `FirstLocalConditionOpen` and `RowTieIn` hold for $r^{\mathrm{N}}$.

`TBOpen` says, for each block $c \ge 1$ and each row place $w$: $\ell^{c_B}$ moves the class of each cocycle that comes from an equivariant map into the submodule $F_S(c, w)$, and a length of local classes modulo $F_S(c, w)$ is at most $e \, c_B (\deg w + 1)$. We have not unfolded `InRhoFixReal2`, `InChiFixReal` and `InChiLoc`, which the other clauses use.

## Proof

1. **Transfer.** `normAt_rN` proves that $r^{\mathrm{N}}$ has the block form above. With `SemisimpleDecomposition`, the lemmas `admG2_rN`, `admG4_rN` and `admG5_rN` carry these hypotheses from $r$ to $r^{\mathrm{N}}$. `decomposes_normalized` proves the decomposition for $r^{\mathrm{N}}$ with no hypothesis.
2. **`RhoOpenA`.** `StB.hRho_rN`, from `admG4` and the decomposition for $r$ and the finiteness of $H^1$.
3. **`TBOpen`.** `tbTarget_row`, in the same file, proves the target `TBTarget` from `admTB`, `SelfGood`, `LocalCoefficientCompatibility`, `FontaineAtPlacesOverL` and `admG2`. `StC.tb_of_target` turns it into `ClauseTB`, which has the same text as `TBOpen`.
4. **`ChiOpen` and `FirstLocalConditionOpen`.** `StC.chi_of` and `StC.first_local_clause_of`, from `admG4`, `admG5`, the decomposition, `TameGeneratorConditions` and `QPow` for $r^{\mathrm{N}}$.
5. **`RowTieIn`**, a conjunction of six row conditions. `KRowA.rowTieIn_of`, with `RowB.rowMat_SN` and `RowB.orbC_S`.

## In the Lean code

The theorem is in [StatementOneBFromUnramified.lean](lean:Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean#L74), with `tbTarget_row` at line 45. The five statements are defined in [StatementOneBChangedOfOpen.lean](lean:Formalism/AdmissibleDesigns/StatementOneBChangedOfOpen.lean#L86), and $r^{\mathrm{N}}$ in [GlobalIndexTheoremPlacesOfRNAdm.lean](lean:Formalism/AdmissibleDesigns/GlobalIndexTheoremPlacesOfRNAdm.lean#L93).

Each hypothesis is used, but each clause uses only some of them. `RowTieIn` uses none: its lemmas take only the data and `normAt_rN`. `SelfGood`, `LocalCoefficientCompatibility`, `FontaineAtPlacesOverL` and `admTB` are used only for `TBOpen`.
