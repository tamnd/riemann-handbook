---
id: realised2-pf
title: The realisation statement for crystalline lattices, from level maps and Wach lemmas
kind: theorem
decl: Formalism.MainNotions.N.Ln03.realised2_pf
module: Formalism.SharpRestriction.LevelLetterCocycles.Realised2Pf
covers: 586
status: drafted
drafted_by: writer@claude
---
This theorem proves `Realised2 hR e`: each surjection of crystalline lattices has coordinates over $\mathcal{O}[[X]]$ in which every cut carries the arc data of theorem E. [The local lifting theorem from local inputs](/entry/local-theorem-of-inputs/) uses it to fill the last field of the record `BrHyp2`, which [the lifting theorem for crystalline lattices](/entry/crystalline-lifting-second-form/) consumes. The arc data come from [`finalArc_holds`](/entry/final-arc-holds/), which has the real content.

## Statement

`Realised2 hR e` says: let $f \colon T_1 \to T_2$ be a surjection of crystalline lattices with `GoodCoeffs`. Take cut data with `CutsOK`, window types for the jumps of $T_1$ (`KindJumps`), jumps of $T_1$ in $[-h, h]$, $g \le h$, `SizesOK` and `ThickLe2`. Then there are:

- coordinates $C_1, C_2$ of $T_1, T_2$ and $C_0$ of the trivial lattice, with a map $C_1 \to C_2$ over $f$;
- an element $e_0$ of $C_0$ that maps to the letter idempotent times $e$ at each index $i$;
- for each irreducible $\varpi \in \mathcal{O}$ and each cut $c$, the arc statement `FinalArc` at $c$.

**Theorem.** Assume the following. Then `Realised2 hR e` holds.

- Level maps $Lb$ that are compatible with $\varphi$ and $\Gamma$ (`hLevN`, `hCmp`, `hLevBφ`, `hLevBΓ`, `hLevΓ`, `hLevφ`).
- $s = 1$, the Wach lemmas `P3`, `P4`, `P5`, `P9`, `Sat`, `LevelMapHodgeFiltration` and `WachLatticeLengthLemma`, and `DdREqDcris`.
- For a surjection $T_1 \to T_2$, each jump of $T_2$ is a jump of $T_1$.
- $\mathcal{O}$ is a valuation ring for $v$, $K$ is unramified, $\ell$ lies in the maximal ideal, $L$ has a primitive $\ell^n$-th root of unity, and $\ell \ge 5$.
- A unit $u \in \mathbb{Z}_\ell^\times$ with $v(u - 1) = 1$ whose image in $\mathcal{O}$ is $\chi(\gamma)$.
- `UnitGen W e`, and the trivial lattice is crystalline.

We have not unfolded the Wach lemmas.

## Proof

`coordSteps_holds` gives $C_1$, $C_2$, $C_0$, the map and $e_0$. Fix $\varpi$ and a cut $c$ of length $\ell_c$. `P9` gives `wachModuleOverLetters` for each crystalline lattice, and `basis_of` turns it into bases of both lattices at $c - \ell_c$. `matrix_of` gives the matrix $P$ of constant terms of the map in these bases. Then `finalArc_holds` gives the arc. Its remaining premises come from `glue2`, `cyclotomicFrobeniusPowerSeries_X` ($\varphi(X) = (1+X)^\ell - 1$), `rhoZ_exp`, `teichOnto_holds`, `hn_of`, `hj_of` and `three_g_le_parameter_bound`. The rest is bookkeeping.

## In the Lean code

The theorem is at [Realised2Pf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/Realised2Pf.lean#L45). `Realised2` is at [CrystallineLiftingEveryOrdering.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingEveryOrdering.lean#L51), and `coordSteps_holds` at [PfAssemble.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L605).

- The proof does not use four premises of `Realised2`: `GoodCoeffs`, the bound $[-h, h]$ on the jumps, `SizesOK` and `ThickLe2`.
- The fields `Ks` and `Δ` of the coordinates are fixed choices, `KsW W` and `DeltaT ℓ`.
