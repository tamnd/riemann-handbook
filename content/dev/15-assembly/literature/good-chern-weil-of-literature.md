---
id: good-chern-weil-of-literature
title: Chern numbers from good metrics, as a literature input
kind: theorem
decl: UpperTheory.LiteratureTheorems.good_chern_weil_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 1443
status: drafted
drafted_by: writer@claude
---
This theorem gives the statement $\mathrm{GoodChernWeil}$: Chern forms of good metrics in the sense of Mumford integrate to Chern numbers, and a push-forward formula on full flag bundles holds. It takes a proof $O$ of [OpenLiteratureStatements](/step/open-literature-statements-def/) and does not use it. The proof is one term, [`goodChernWeil`](/entry/good-chern-weil/), and that entry has the real content. The result fills the field `p16` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). From there [`toClassicalTheorems`](/entry/to-classical-theorems/) passes it to [proportionality on toroidal flag spaces](/entry/toroidal-flag-proportionality-of-good-chern-weil/). Below this theorem are 1,443 declarations.

## Statement

Let $F$ be a field and let $X$, $Y$ be smooth, geometrically integral, closed subvarieties of projective spaces over $F$ (the structure `Var`). Let $E = (E_\tau)_{\tau}$ be a finite family of vector bundles on $X$ of ranks $m_\tau$, given by local frames. Let $f \colon Y \to X$ carry a full flag of $f^*E$ that refines $E$ (the predicate `Refines`, which we have not unfolded fully). Let $D_{\tau,i}$ be divisors on $Y$ whose line bundles are the graded pieces of the flag (`IsGraded`), and let $x_{\tau,i}$ be the variables for them. For a real polynomial $R$ in the Chern classes $c_k(E_\tau)$, let $R(x)$ be $R$ with $c_k(E_\tau)$ replaced by the $k$-th elementary symmetric function of $x_{\tau,0}, \dots, x_{\tau,m_\tau-1}$. For a polynomial $Q$ in the $x_{\tau,i}$, let $\int_Y Q$ be the intersection number of the divisors that $Q$ names (`interPoly`). Put $\varpi = \prod_{\tau,i} (-x_{\tau,i})^{m_\tau-1-i}$ and $\Delta = \prod_\tau \prod_{i<j} (x_{\tau,j} - x_{\tau,i})$.

**Theorem.** Both parts hold.

1. (`GoodChernNumbers`) Let $\sigma \colon F \to \mathbb{C}$, let $U \subset X$ be open, and let $H$ be a hermitian metric on $E$ over $U(\mathbb{C})$ that is good along $X \setminus U$ (`IsGood`). That is, near each boundary point there are holomorphic coordinates with boundary $z_a = 0$ for $a \in S$, in which $H$ and $(\det H)^{-1}$ grow at most like a power of $\sum_{a \in S} \lvert \log \lvert z_a \rvert \rvert$, and the connection and curvature forms have Poincaré growth. Then for each $R$ the top Chern form $R(c(E, H))$ is integrable on $U(\mathbb{C})$, and its integral is $\int_Y R(x)\, \varpi$.
2. (`FlagPushForward`) Let $F$ have characteristic zero. If $\sum_w \operatorname{sgn}(w)\, w(Q) = R(x)\, \Delta$, with $w$ over the products of the symmetric groups $S_{m_\tau}$, then $\int_Y Q = \int_Y R(x)\, \varpi$.

Part 1 is of the kind proved by Mumford (Invent. Math. 42, 1977) for good metrics. We have not matched it to a numbered theorem there.

## Proof

Apply `GlobalTheory.GoodMetric.goodChernWeil`. The argument $O$ is not used.

## In the Lean code

The theorem is in [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L395). The statement is in [MumfordProportionality.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/MumfordProportionality.lean#L30). The metric conditions are in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L117).

The proof `goodChernWeil` in [GoodChernWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GoodChernWeil.lean#L10) applies `goodChernWeil_of_goodTopChernForm` to three results:

- `T.goodMetric_topChernForm_integral_eq_smooth` (`GoodTopChernForm`): for one bundle, the integral of the Chern form of $c_{\dim X}$ is the same for a good metric on $U$ and for a smooth metric on $X$;
- `T.chernNumbers_eq_integral_chernForms_smoothMetric` (`ChernWeilNumbers`): part 1 for smooth metrics on all of $X$;
- `T.fullFlagBundle_pushForward_formula`, which is part 2 as it stands.

The combining lemma writes $R(c(E, H))$ as a sum of top Chern forms of bundles induced by representations, and compares each one with a smooth metric.

Odd points. The name says "of literature", but the code proves the statement and ignores $O$. $\mathrm{GoodChernWeil}$ joins two independent statements, and part 2 has no metrics.
