---
id: law-level-prime-all
title: The twist place law for all tuples, from a lattice shape
kind: theorem
decl: GlobalTheory.LevPrimeAll.lawLevelPrime_all
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeesawLevelPrimeLawAllTuples
covers: 581
status: drafted
drafted_by: writer@claude
---
This theorem proves `TOfShape D`: from a lattice shape that fits the level data, it chooses twist operators and proves the law `TLaw` at the twist places for every tuple. Its only user is the second name [`seesaw_levelPrime_law_all_tuples`](/entry/seesaw-level-prime-law-all-tuples/), which is step 1 of [the finite integral laws from pinned level data](/entry/pins-finite-integrals/).

## Statement

The notation is that of [pins-finite-integrals](/entry/pins-finite-integrals/): a common datum $c$ with spaces $X_j$ and a top space $T$, level data $v$ with twist places $P_T$, a nonarchimedean local field $k$, and a lattice shape datum $o$ with split points $p_i$, frames $\beta_j(i)$, pairs $Q_j(i)$, a uniformiser and characters $\chi_i$ of conductor 1, for $i$ in a list $I$.

For units $\varepsilon_j(i)$ of $\mathcal{O}_k$, let $S_j$ (`o.S ε j`) be the composite over $i \in I$ of the local operators `sOp` at $p_i$. Each is built from a Fourier-type map `FFStar` with a residue character of $\chi_i$, followed by a diagonal map `dia` with $\varepsilon_j(i)$; we have not unfolded these two. An operator $\mathrm{op}_j$ (`BiOp`) is a finite sum of pairs of combinations.

**Theorem.** Assume `c.Is`, `v.Is` and `ShapeOff v o`. There are $\varepsilon$, $\mathrm{op}$, reals $r_j(i) > 0$ and integers $e_j(i)$ such that $v' = $ `v.withT (o.S ε) op` satisfies `Is`, and for every tuple $t$ with decoration $w$ such that $t$ satisfies `Is`, `WeilOK`, `UnrOn` and `UnrK` at $P_T$, and $c_T(j) = \prod_i r_j(i)\, \chi(\varpi_i)^{e_j(i)}$ for the Weil character $\chi$ of $t$, `TLaw v' w` holds.

`TLaw` has two parts. At a double step $j$ (with $j + 2(\sigma + 1) + 2 = m$), for vacua $\Psi_1, \Psi_2$ at $P_T$: $\mathrm{op}_j$ applied to the contracted kernel is a vacuum pair at $P_T$, and for each $\varphi$ in the ramified set and combinations $d, d'$ off $P_T$, the theta pairing of $\varphi$ with the kernel equals $c_T(j)$ times the pairing of $S_j \varphi$ with the kernel moved by $d_T$ and $\mathrm{op}_j$. At the last step ($j + 2 = m$) the same holds after integration against an automorphic $f$ on $T$.

## Proof

1. [`exists_choice`](/entry/exists-choice/) gives, for each $j$, the data $\varepsilon_j, \mathrm{op}_j, r_j, e_j$ with $r_j > 0$, $\mathrm{op}_j$ supported at $P_T$ (`OpAt`), and both parts of the law at $j$.
2. $v'$ satisfies `Is`. All fields but two come from `v.Is`. The field `atT` needs that $\mathrm{op}_j$ lives at $P_T$: this is `OpAt`. The field `ram` needs that $S_j$ maps the ramified set into itself. By `ShapeOff.ram` this set is `o.Ram j`. Then `ram_S` proves it by induction on $I$, with `ram_sOp` for one factor. By `ramifiedOperator_bijective_finite_translation_combination`, `sOp` at $p_i$ is a finite combination of translations at $p_i$, and it is a bijection on the ramified vectors at $p_i$. Translations keep $\varphi$ automorphic, and they commute with the conditions at $p_{i'}$ for $i' \neq i$ since the places are distinct.
3. The law: rewrite $c_T(j)$ with the hypothesis and apply step 1.

## In the Lean code

The theorem is at [SeesawLevelPrimeLawAllTuples.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeesawLevelPrimeLawAllTuples.lean#L77), with `ram_sOp` at line 18 and `ram_S` at line 34. `TOfShape` and `TDat.S` are in [VacOfShape.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VacOfShape.lean#L114), `TLaw` in [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L207), and `sOp` in [PlacesToAdeles.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlacesToAdeles.lean#L25).

The last-step part of `TLaw` has a hypothesis that $f$ is invariant under the stabiliser of the lattice $N_T$ at $P_T$ (`InK`). The proof does not use it: `exists_choice` gives the law for every automorphic $f$. The hypothesis `UnrK` is used only at the last step.
