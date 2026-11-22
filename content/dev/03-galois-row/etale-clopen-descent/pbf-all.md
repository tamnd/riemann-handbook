---
id: pbf-all
title: The projective bundle formula for the trivial bundle, by induction on the rank
kind: theorem
decl: UpperTheory.Pbf.pbf_all
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.EtaleCohomologyProjectiveBundleFormula
covers: 975
status: drafted
drafted_by: writer@claude
---
This lemma proves the projective bundle formula in étale cohomology with coefficients $\mathbb{Z}/q(i)$ for the trivial bundle of each rank $N$ on each space on which $q$ is invertible. It is an induction on $N$ that joins four lemmas, one for each case. [The formula on a scheme](/entry/cb-etale-cohomology-projective-bundle-formula/) uses it at $E = \operatorname{sch} U$, after it shows that each bundle on $\operatorname{sch} U$ is trivial.

## Statement

Spaces, $B\mathrm{GL}_N$, the projective bundle $\mathbb{P}(V)$ with its projection $\pi$ and line bundle $L$, and the groups $H^n(E, \mathbb{Z}/q(i))$ are as in [pbf_disc](/entry/pbf-disc/). Let $\mathrm{triv}_N \colon E \to B\mathrm{GL}_N$ be the trivial bundle, and $P = \mathbb{P}(\mathrm{triv}_N)$. Say that $q$ is invertible on $E$ (`Inv q E`) if $q$ is a unit on each scheme $T$ over which $E$ has a $0$-simplex.

**Lemma.** Let $q \geq 1$ and $N \geq 0$. For each space $E$ on which $q$ is invertible, and all $n, i \in \mathbb{Z}$, the map

$$\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) \to H^n(P, \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup c_1(L)^j$$

is bijective.

This is the projective bundle formula (SGA 5, Exposé VII) for the trivial bundle, in the model of [pbf_disc](/entry/pbf-disc/).

## Proof

Induction on $N$, with four cases.

1. $N = 0$: `projectiveBundleFormula_rank_zero`. The source is an empty sum, and the proof shows that the target has at most one element. This case needs no hypothesis on $q$.
2. $N = 1$: `projectiveBundleFormula_rank_one_of_homotopyInvariant`. The map is $\pi^*$ (the class $c_1(L)^0$ is $1$), and the proof shows that $\pi \colon P \to E$ induces a quasi-isomorphism of chain complexes (the private lemma `chains_qi`).
3. $N = 2$: [projectiveBundleFormula_rank_two](/entry/projective-bundle-formula-rank-two/). The proof covers $P$ by two charts, uses Mayer-Vietoris, and uses a Künneth formula for $\mathbb{G}_m \times E$ with the Kummer class (`bijective_cohomology_gm_product_kummer_cup`).
4. $N + 1$ with $N \geq 2$: [projectiveBundleFormula_succ_of_forall](/entry/projective-bundle-formula-succ-of-forall/) takes the formula in rank $N$ for all spaces and gives it in rank $N + 1$. Its proof uses a second form of the formula (`projBundleFormula_iff_pglForm`), a blowup and Mayer-Vietoris covers, which we have not unfolded.

The induction hypothesis is used only in case 4. Cases 1 to 3 are proved directly.

## In the Lean code

The lemma is the private theorem `pbf_all` in [EtaleCohomologyProjectiveBundleFormula.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/EtaleCohomologyProjectiveBundleFormula.lean#L30). `PBF` and `triv` are in [ConstCompSingle.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/ConstCompSingle.lean#L28), where `PBF` is the Leray-Hirsch condition `LH` for $\pi$ and the classes $c_1(L)^j$. `Inv` is in [GalMapMul.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/GalMapMul.lean#L250). The four lemmas are in `Development/AutomorphicArithmetic/CommutativeAlgebra/`: [rank zero](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/ProjectiveBundleFormulaRankZero.lean#L64), [rank one](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/ProjectiveBundleFormulaRankOneOfHomotopyInvarian.lean#L471), [rank two](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/ProjectiveBundleFormulaRankTwo.lean#L104) and [the step](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/ProjectiveBundleFormulaSuccOfForall.lean#L36).

The name of the rank one lemma says "of homotopy invariant", but its statement has no hypothesis of homotopy invariance: it is `∀ q E, Inv q E → PBF q E 1`. The induction is on $N$ with $E$ quantified inside, because the step lemma takes the rank $N$ formula for all spaces as its hypothesis.
