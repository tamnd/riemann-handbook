---
id: part-i-of-semistable-reduction
title: The integral models of Part I, from semistable reduction
kind: theorem
decl: GlobalTheory.partI_of_semistableReduction
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.PartOneOfSemistableReductionPadicPolarized
covers: 1300
status: drafted
drafted_by: writer@claude
---
This theorem derives the statement $\mathrm{PartI}$, a system of integral models of unitary moduli spaces, from the semistable reduction theorem for abelian varieties over $p$-adic fields. It has four callers. Their common dominator in the proof is the literature theorem of the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). One caller, `partI_holds`, applies it to the Lean proof `GlobalTheory.SS.semistableReductionSt` of the hypothesis, so $\mathrm{PartI}$ holds with no hypothesis in the final proof.

## Statement

Let $\mathrm{SSR}$ be the statement `SemistableReductionSt`: for each prime $p$, each finite extension $K$ of $\mathbb{Q}_p$ in $\overline{\mathbb{Q}}_p$ and each polarized abelian variety $A$ over $K$, there are a finite extension $K' \supseteq K$ and a semi-abelian group scheme $G$ over $\mathcal{O}_{K'}$ whose generic fibre is $A \times_K K'$, as group schemes. This is Grothendieck's semistable reduction theorem (SGA 7 I, Exposé IX, Théorème 3.6). The Lean statement does not use the polarization in its conclusion.

**Theorem.** $\mathrm{SSR}$ implies $\mathrm{PartI}$.

$\mathrm{PartI}$ is a conjunction of two clauses.

1. $N_0$: for $h \ge 1$, a prime $p$ and an odd prime $n \neq p$, there are $j$ with $n^j \ge 3$ and a Siegel family of genus $h$ and level $n^j$ at $p$. This is a scheme, smooth of relative dimension $h(h+1)/2$, with a universal principally polarized object, an existence property for points over $p$-adic unit balls, and an unramified condition.
2. For each CM field $E$ with its datum $H$ (`Host`), each PEL datum $D$ (a projective $\mathcal{O}_E$-module with a unimodular alternating form for which $a$ and $\bar a$ are adjoint) of signature $(p, q)$ with $p + q \ge 1$, and each family $X_l$ of moduli spaces indexed by levels $l$, there is a local system $Y(p, W)$ for each prime $p$ and each valuation subring $W \subset \mathbb{C}$ with $p \in \mathfrak{m}_W$. For each level $l$ good at $p$ and each coefficient field $F$, $Y(p, W)$ gives a model: a normal, projective, flat scheme over $W \cap F$, with a dense open immersion of the generic moduli space and a semi-abelian scheme whose abelian locus over the generic fibre is that image. The models satisfy `N2` (level structures, transition maps, comparison with a Siegel family), `SplitFibres`, `N3` (uniformization at complete local rings), `N4` (arcs over $O'[[X]]$) and `N6` (a global model over $\mathcal{O}_F$ that dominates the local ones).

## Proof

The proof is one application: `partI_of_semistableReduction_of_arcFam h arcFam_closed`. The theorem `partI_of_semistableReduction_of_arcFam` takes $\mathrm{SSR}$ and a statement `ArcFamSt` about arcs with frames. It applies `T.modelSystems_jointProperties_of_laws` to proven lemmas and to `modelsSt_of_semistableReduction` $h$. That lemma uses [`exists_fullLevelAmpleModel_of_semistableReduction`](/entry/exists-full-level-ample-model-of-semistable-reduction/), the projective model with ample frames. The theorem `arcFam_closed` proves `ArcFamSt` from proven lemmas.

## In the Lean code

The theorem is in [PartOneOfSemistableReductionPadicPolarized.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/PartOneOfSemistableReductionPadicPolarized.lean#L19). It only passes its hypothesis along. The real content is in `partI_of_semistableReduction_of_arcFam` ([L25](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/PartIOfSemistableReductionOfArcFam.lean#L25)) and in the chain below [`topAmpExists`](/entry/top-amp-exists/).

- `SemistableReductionSt` is in [SemistableReductionSt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SemistableReduction₂/SemistableReductionSt.lean#L15).
- `PartI` is in [UniformisationConclusion.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/UniformisationConclusion.lean#L223). `N0`, `N2` and `N6` are in [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L82).
- `arcFam_closed` is in [ExistsArcFamilyPointWithFramesProof.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsArcFamilyPointWithFramesProof.lean#L21).

We have not unfolded `SplitExt`, `IsGt`, `ArcIn`, `Dominates` or the Siegel moduli data `SiegPre`. The description of the clauses above stops at the level of these names.
