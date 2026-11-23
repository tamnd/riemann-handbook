---
id: arith-hilbert-samuel-of-literature
title: The arithmetic Hilbert-Samuel formula, as a literature input
kind: theorem
decl: UpperTheory.LiteratureTheorems.arith_hilbert_samuel_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 1773
status: drafted
drafted_by: writer@claude
---
This theorem gives the statement $\mathrm{ArithHilbertSamuel}$: the number of small sections of the powers of a nef hermitian line bundle grows like its arithmetic self-intersection. It takes a proof $O$ of [OpenLiteratureStatements](/step/open-literature-statements-def/) and does not use it. The proof is one term, [`arithHilbertSamuel_of_principalisation`](/entry/arith-hilbert-samuel-of-principalisation/), and that entry has the real content. The result fills the field `q9` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). It is also used by `vol_ge_of_literature` and `vol_nef_of_literature` in the same file. Below this theorem are 1,773 declarations.

## Statement

Let $k$ be a domain that is a finite $\mathbb{Z}$-module, and let $p \colon X \to \operatorname{Spec} k$. Say that $X$ is an *arithmetic variety of dimension $D+1$* (the structure `IsArithVar`) if $X$ is integral, projective over $k$, flat over $\mathbb{Z}$, and of Krull dimension $D+1$. A *hermitian line bundle* $\overline{L}$ (the structure `HermLB`) is a line bundle $L$ on $X$ with a smooth metric on $X_\sigma(\mathbb{C})$ for each $\sigma \colon k \to \mathbb{C}$, compatible with complex conjugation. A section $s \in H^0(X, L)$ is *small* if $\lVert s \rVert_\sigma \le 1$ at each complex point for each $\sigma$.

$\overline{L}$ is *nef* (`IsNef`) if its metrics are semipositive and its degree is nonnegative on each vertical and each horizontal integral curve. $\overline{L}$ has *self-intersection* $a$ (`IsSelfInter`) if there is a function $h$ on the points of $X$ with $h(\eta_X) = a$ that satisfies the recursive rules for the heights of integral subschemes (the structure `IsArithHeight`). This is the inductive form of $\widehat{c}_1(\overline{L})^{D+1}$, as in Bost, Gillet and Soulé (J. Amer. Math. Soc. 7, 1994).

**Theorem.** Let $X$ be an arithmetic variety of dimension $D+1$. Let $\overline{L}$ and $\overline{N}$ be hermitian line bundles, with $\overline{L}$ nef of self-intersection $a$. Then for all large $m$ the set $\widehat{H}^0_m$ of small sections of $\overline{L}^{m} \otimes \overline{N}$ is finite, and

$$\log \# \widehat{H}^0_m = \frac{a}{(D+1)!}\, m^{D+1} + o(m^{D+1}) \qquad (m \to \infty).$$

For ample $L$ with a positive metric and trivial $\overline{N}$, this is the arithmetic Hilbert-Samuel formula of Gillet and Soulé (Invent. Math. 110, 1992) and Abbes and Bouche (Ann. Inst. Fourier 45, 1995). We have not checked a source for the form with nef $\overline{L}$ and a twist $\overline{N}$.

## Proof

Apply `GlobalTheory.arithHilbertSamuel_of_principalisation` to `principalisation_of_literature O`. That theorem is `principalisation_closed`, a principalisation of ideals on smooth projective varieties in characteristic zero, proved in the code. No field of $O$ is read.

## In the Lean code

The theorem is in [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L255). The statement is in [SmallSecTensTriv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/SmallSecTensTriv.lean#L14). The definitions are in [ExistsIsClosedImmersionGenericPoint.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsIsClosedImmersionGenericPoint.lean#L578).

The step below, in [ArithHilbertSamuelOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelOfPrincipalisation.lean#L11), is `T.arithHilbertSamuel_nef_of_ample` applied to three results, each from `Principalisation`:

- `MixHt.arCalc_of_principalisation`, which gives `ArCalc`, seven rules of arithmetic intersection numbers that we have not unfolded;
- `T.ampleArithHilbertSamuel_of_principalisation`, which gives `AmpleHS`, a limit statement for ample $L$ with a semipositive metric, about a counting function `Pair.lc` that we have not unfolded;
- `SemiPullAll.semiPull_of_principalisation`, which gives `SemiPull`: semipositivity is kept under pull-back.

Odd points. The name says "of literature", but the code proves the statement and ignores $O$. All the input comes from one statement on resolution, `Principalisation`, which also fills the field `q16` of the same bundle.
