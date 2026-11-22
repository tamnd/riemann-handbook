---
id: line-of-large-degree-of-use
title: A Siegel lemma from the successive minima bounds
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Giv.lineOfLargeDegree_of_use
module: Development.WeilBound.CoreStatements.AutomorphicKernels.MoriwakiBigness.HilbertSamuelApplications.LineOfLargeDegreeOfUse
covers: 1206
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem proves a Siegel lemma for hermitian lattices from four inputs of arithmetic intersection theory. Its only caller is [`deepStR_of_use`](/entry/deep-st-r-of-use/), which passes the lemma to `given_of_use` and to [`good_tower_volume_theorem_bis`](/entry/good-tower-volume-theorem-bis/). There it gives the slope bound `SlopeBoundSt` for Lie algebras (Step 3 of [the Weil bound chapter](/proof/weil-bound/)).

## Statement

Let $K$ be a number field. A hermitian lattice $F$ of rank $i$ over $\mathcal{O}_K$ is a finitely generated $\mathcal{O}_K$-submodule of $K^i$ that spans $K^i$, with a hermitian metric at each complex embedding. Write $\mu(F)$ for its slope. For a finite extension $K'$ and $v \in K'^i$, write $\deg_{K'}(v)$ for the normalized degree of the rank one sublattice spanned by $v$ in $F \otimes \mathcal{O}_{K'}$.

**Theorem.** Assume `ArithIntersectionSystemStatement`, `HSUse`, `MoriwakiBigStatement` and `ResKStatement`. Then for each $K$, each $F$ of rank $i \geq 1$ and each $\varepsilon > 0$, there are a finite extension $K'$ of $K$ and $v \in K'^i$ with $v \neq 0$ and

$$\mu(F) - \tfrac12 \log i - \varepsilon \leq \deg_{K'}(v).$$

The conclusion is `LineOfLargeDegree.Statement`. The [chapter](/proof/weil-bound/) calls it an absolute Siegel lemma.

## Proof

The proof uses the two successive minima bounds. Let $X$ be an arithmetic variety of dimension $D+1$ with a semipositive, conjugation invariant hermitian line bundle $\overline{A}$ that is nef on the fibres. Let $II$ be an intersection system.

- Lower bound (`SuccessiveMinimaLowerBound`): if each subvariety $W$ of arithmetic dimension 1 has $e \deg W \leq \overline{A}|_W$, then $(D+1)\,e \deg_A X \leq \overline{A}^{D+1}$.
- Upper bound (`SuccessiveMinimaUpperBound`): if a Zariski dense family of such $W$ has $\overline{A}|_W \leq e' \deg W$, then $\overline{A}^{D+1} \leq (D+1)\,e' \deg_A X$.

These are the two inequalities of Zhang's theorem of successive minima (S. Zhang, *Positive line bundles on arithmetic varieties*, J. Amer. Math. Soc. 8, 1995), in a form for an abstract intersection system.

1. The lower bound is `HSUse.z1`. The upper bound is the third part of `hsLinks_of_use`, which gets it from `MoriwakiBigStatement` by `Z2.proof`.
2. `intersection_exists_of_arith_system` gives `I2.ExistsStatement` from the first hypothesis.
3. The proof builds about 30 auxiliary statements on charts, dual lattices, stacked graphs and Grassmannians. Almost all come from lemmas with no hypotheses. The hypotheses enter in four places: `generic_degree_of_arith_system`, `coordinate_projection_of_arith_system` and `degree_of_system` use the first one, and `points_integrable_of_resolution_statement` and `ptsIndep_of` use `ResKStatement`. We have not unfolded these statements.
4. `LineOfLargeDegreeFromZ.ofOpen` takes 13 of them and gives `LineOfLargeDegreeFromZ.Statement`. That statement is the implication: the lower bound, the upper bound and `I2.ExistsStatement` give the Siegel lemma. The proof applies it to the three inputs of steps 1 and 2.

## In the Lean code

The theorem is in [LineOfLargeDegreeOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/LineOfLargeDegreeOfUse.lean#L10). The conclusion is at [KernelsLattice.lean#L85](lean:GroundTheory/HeightsAndTheta/Heights/KernelsLattice.lean#L85). The successive minima bounds are at [ArithmeticHilbertSamuelLowerBound.lean#L156](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ArithmeticHilbertSamuelLowerBound.lean#L156). The main lemmas:

- `hsLinks_of_use` in [HsLinksOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/HsLinksOfUse.lean#L9), and `HSUse.z1`.
- `LineOfLargeDegreeFromZ.ofOpen` in [Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/Assembly.lean#L110).

All four hypotheses are used. The proof uses both successive minima bounds; the chapter mentions only the upper bound. The upper bound comes from `MoriwakiBigStatement` by `Z2.proof`, not from `HSUse`.
