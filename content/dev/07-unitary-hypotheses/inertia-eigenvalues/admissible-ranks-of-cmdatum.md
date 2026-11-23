---
id: admissible-ranks-of-cmdatum
title: The thirteen admitted conditions of theorem B
kind: theorem
decl: GlobalTheory.TheoremBAdm.admissible_ranks_of_CMDatum
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingTheoremBHypothesesAdmitted
covers: 864
status: drafted
drafted_by: writer@claude
---
This theorem proves the 13 conditions `admitted` that [local lifting theorem B](/entry/theorem-b-closing/) needs, with the constants $(10, 23, 32, 32, 8)$. Its second name is [`localLifting_theoremB_hypotheses_admitted`](/entry/local-lifting-theorem-b-hypotheses-admitted/). The proof is an assembly of 17 lemmas.

## Statement

Assume `BlochKatoLocal`, local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK`, as in [local lifting theorem B](/entry/theorem-b-closing/).

**Theorem.** For each datum $D$, Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$, the conjunction `admitted D HW F Cm 10 23 32 32 8` holds.

Most conditions are local: they hold at each prime $\ell \ge 5$, each $K$ inside the maximal unramified extension of $\mathbb{Q}_\ell$, and each coefficient field $L$ good for $K$ at level 1 ("case A"), for the Wach module of $HW$ at $(K, L)$. The 13 conditions, with the lemma that gives each, are:

1. `adm1`, a local conclusion on lattices: `wachModuleLocalConclusions_usedForms`;
2. `adm2`, eight lifting statements with the constants $C_R, C_A, C_B, C_K = 10, 23, 32, 32$: [`localConstants_from_admitted_local_Galois_statements`](/entry/local-constants-from-admitted-local-galois-statements/);
3. `adm5`, saturation: `arcTheorem_tools_of_wachModuleConclusions`;
4. saturation under Frobenius pullback: the same lemma;
5. `adm8`, the killer conditions with $C_\kappa = 8$: the same lemma;
6. `adm9`, a divisibility inequality for power series over a discrete valuation ring: `content_divisibility_clause`;
7. `adm10`, a condition `H1fGeneratorBoundAll` on generators of $H^1_f$, which we did not unfold: `h1fGeneratorBoundAll_loc`;
8. `adm11`, the relay condition: `wachRelayLemma_arcCoordinateHypotheses`;
9. `adm12`, the arc coordinates: `arcCoordinatesCaseA_of_admArcA_of_P1free_of_adm11`;
10. `adm13`, the splitting of classes along arcs: `classSplitting_along_arcs_of_admissible`;
11. `adm14`, the universal part: [`crystallineUniversalPart_caseA`](/entry/crystalline-universal-part-case-a/);
12. `adm15`, exactness and strictness of $D_{\mathrm{cris}}$ (`DcrisExactStrictLocal`, not unfolded): `dcris_exact_strict_elementwise_crystalline`;
13. `adm16`, a crystalline extension criterion of Bloch-Kato type: `blochKato_crystalline_extension_criterion`.

## Proof

Most items come from one lemma each. Four steps need more.

1. `wachLattice_laterClauses_hold` gives a list of lattice facts. The proof keeps four: freeness of the Wach lattices (`P1`) and the facts `P6`, `P8`, `P9`.
2. `wachRelayLemma_arcCoordinateHypotheses` gives the relay condition and `AdmArcA`, the hypotheses of the arc theorem. With `P1` and `ramifiedCoefficientChains_adm11` they give the arc coordinates (item 9).
3. `classSplitting_along_arcs_of_admissible` takes the arc coordinates, `AdmArcA`, the relay condition, `P1`, `P6`, `P8`, `P9`, two parts of item 2, the first filtration from `arcTheorem_tools_of_wachModuleConclusions`, `jumps_exact_adm`, `herr_extension_class_formula`, `fontaine_fullFaithful_exact_psi`, `ramifiedCoefficientChains_adm11` and item 12. It gives item 10.
4. `crystallineUniversalPart_caseA` takes saturation, the killer at levels, the $\Gamma$-stability of the uniformizer, the arc coordinates, `P9`, one part of item 2, and $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ in the unramified case (`dDeRham_eq_dCris_of_unramified`). It gives item 11.

The rest is bookkeeping. Only two lemmas use the three hypotheses: those of items 2 and 8.

## In the Lean code

The theorem is in [LocalLiftingTheoremBHypothesesAdmitted.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremBHypothesesAdmitted.lean#L26). `admitted` is in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L527). Each lemma above is imported from a "Statement" file. We read their statements, not their proofs.

- The name speaks of ranks and of a CM datum. The statement has neither.
- `localConstants_from_admitted_local_Galois_statements` is called twice: once to take parts of it, and once more for item 2.
- The namespace of items 10 and 11 is `UnusedSlot80`, although both are used here.
