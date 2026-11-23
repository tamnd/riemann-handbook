---
id: cong-fin-g-of-ex
title: The congruence statement from lacunary weights and a fixed type
kind: theorem
decl: UpperTheory.Gal.Int.Cong.congFinG_of_ex
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.CongruenceOddLevel.CongFinOddOfLvLac
covers: 492
status: drafted
drafted_by: writer@claude
---
This theorem proves `CongFinG` from `WtLacEx`. Its user is [congFinOdd_of_ex](/entry/cong-fin-odd-of-ex/). `WtLacEx` approximates the Hecke eigenvalues of $U$ by those of forms $U'$ with a lacunary weight. `StepSt` asks in addition that each $U'$ has the type `TyEll` at $w_0$. The proof gets `StepSt` from `WtLacEx` with the lemma `stepSt_of_ex`. Then [congFinG_of_step](/entry/cong-fin-g-of-step/) gives `CongFinG`. The type condition is the new content here. Below it are 492 declarations.

## Statement

**Theorem.** If `WtLacEx` holds, then `CongFinG` holds.

`WtLacEx` is `WtTo GapWt`. In short: let $U$ have weight $\lambda$ and level $K \cap K_v$, and let $\eta(U)$ be the eigenvalues of $U$ for a family of Hecke operators. Then $\eta(U)$ satisfies `PolyApprox` by the vectors $\eta(U')$, where $U'$ has level $K$ and a weight $\mu$. The weight $\mu$ differs from $\lambda$ only at embeddings $\tau$ over $v'$, and its jumps at $\tau_0$ are lacunary (`GapWt`). `StepSt` is the same statement with `TyEll E l a w₀ U'` added. `TyEll` is explained in [congFinG_of_step](/entry/cong-fin-g-of-step/).

## Proof

The proof is `congFinG_of_step (stepSt_of_ex ellSt_holds H)`.

`EllSt` says: for each place $w_0$ above $\ell$, each neighborhood $N$ of $1$ in $\mathrm{GL}_a(E_{w_0})$ and each $m_0$, there are $m \geq m_0$, an open compact torsion-free subgroup $J \subseteq N$ and a surjection $\theta : J \to \mathbb{Z}/\ell^m$ such that each smooth irreducible representation with a nonzero vector on which $J$ acts by $\chi \circ \theta$, $\chi \neq 1$, is cuspidal. `ellSt_holds` is the lemma `exists_ellType`, which we have not opened.

`stepSt_of_ex` goes like this.

1. `WtLacEx` approximates $\eta(U)$ by the $\eta(U_1)$ for forms $U_1$ of lacunary weight $\mu$.
2. For a fixed $U_1$, the forms of weight $\mu$ and level $K$ with `TyEll` at $w_0$ are dense. For a form $f$ and $\varepsilon > 0$: `smoothAt_holds` gives $N$ such that $f$ is fixed by $N$ at $w_0$. `EllSt` gives $J \subseteq N$ with $\lVert \ell \rVert^m < \varepsilon$. `tyStep_holds` then gives an approximation of $f$ within $\lVert \ell \rVert^m$ by forms of type `TyEll`. We have not unfolded `tyStep_holds`.
3. `toPolyX_holds` turns this density into an approximation of $\eta(U_1)$ by the $\eta(U')$ for forms $U'$ with `TyEll`. The lemma `intL_congr` checks that the Hecke operators stay integral for $\mu$.
4. `combine_holds` composes the two approximations.

## In the Lean code

The theorem is in [CongFinOddOfLvLac.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/CongFinOddOfLvLac.lean#L13), and `ellSt_holds` is at line 9 of the same file. `EllSt`, `StepSt` and `stepSt_of_ex` are in [NotApartOfOverPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/NotApartOfOverPair.lean#L76). `WtTo`, `GapWt` and `WtLacEx` are in [WtDefs.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/WtDefs.lean#L13). `WtLacEx` itself is proved by `wtLacEx_holds`, in [LadicWeightEmbeddingOverPlace.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/WeightCharacters/LadicWeightEmbeddingOverPlace.lean#L73).
