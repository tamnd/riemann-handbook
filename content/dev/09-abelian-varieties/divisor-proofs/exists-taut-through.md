---
id: exists-taut-through
title: A degenerating family factors through a rigid tautological chart
kind: theorem
decl: GlobalTheory.UCanon.exists_taut_through
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTautologicalChartVersality
covers: 930
status: drafted
drafted_by: writer@claude
---
Let $S$ be the candidate compactification of [`exists_tautB_chart_at`](/entry/exists-taut-b-chart-at/). This theorem starts from a degenerating monomial family over a complete local domain $V$ that maps to $S$. It gives a power series chart with the conditions `IsTautB`, a map from the chart to $S$, and a local homomorphism from the chart ring to $V$ through which the given map factors. This is a versality property of the chart. It proves [the statement form](/entry/exists-tautological-chart-versality/), which `exists_tautB_chart_at` applies at each boundary point.

## Statement

Use the CM field $E$, the datum of signature $(p, q)$, the moduli scheme $X^\circ_F$, the fan function $\varphi$, the data $Z, i, \pi, S, j, B$, the hypotheses `UPoinOnX` and `SepB`, and monomial families (`MonoFam`) as in [`exists_tautB_chart_at`](/entry/exists-taut-b-chart-at/). For a domain $A$ let $\eta_A \colon \operatorname{Spec} \operatorname{Frac} A \to \operatorname{Spec} A$ be the generic point. For a monomial family $C$ let $y_C$ be its generic point in $X^\circ_F$ and $X_C$ its character group.

Call $V$ an admissible base (`Mum.Base`) if $V$ is a Noetherian, integrally closed local domain of characteristic $0$, complete for its maximal ideal.

**Theorem.** Assume $p + q \geq 1$, `IsPolFan` and `NoSelfInt` for $\varphi$ in rank $\min(p, q)$, `UPoinOnX` and `SepB`. Let $V$ be an admissible base with algebraically closed residue field. Let $C$ be a monomial family over $V$ with $X_C \neq 0$, and $\xi_V \colon \operatorname{Spec} V \to S$ a map with $j \circ y_C = \xi_V \circ \eta_V$. Then there are a field $k$, integers $m, e$, a monomial family $C_1$ over $R = k[[s_1, \dots, s_m, u_1, \dots, u_e]]$, a map $\xi \colon \operatorname{Spec} R \to S$ and a ring map $\theta \colon R \to V$ such that

1. $C_1$ satisfies `IsTautB`;
2. $j \circ y_{C_1} = \xi \circ \eta_R$;
3. $\theta$ is a local homomorphism;
4. $\xi \circ \operatorname{Spec}\theta = \xi_V$.

## Proof

1. [`exists_canonical_family_through_degenerating_family`](/entry/exists-canonical-family-through-degenerating-family/) gives $k, m, e$, a family $C_1$ over $R$ with a canonical structure (`Canon`) whose parameters are $s_1, \dots, s_m$, and a local $\theta \colon R \to V$ with `Through C C₁ θ`. This step does not use $S$.
2. `canonicalFamily_isPointRigid_tautologicalChart` turns the canonical structure into `IsTautB`. It uses $p + q \geq 1$, `IsPolFan` and `NoSelfInt`.
3. `UChart.taut_exists_map` gives $\xi$ with (2). It uses `UPoinOnX` and `SepB`.
4. It remains to prove (4). One clause of `UPoinOnX` says that $S$ is projective over $F$, so $S$ is separated. Two maps from the spectrum of a domain to a separated scheme are equal if they agree after $\operatorname{Spec} f$ for an injective ring map $f$, since $\operatorname{Spec} f$ is dominant. Let $R_s = R[1/\prod_i s_i]$. `Through` gives $y_o \colon \operatorname{Spec} R_s \to X^\circ_F$ that restricts to $y_{C_1}$ at the generic point, and $\kappa \colon \operatorname{Spec}\operatorname{Frac} V \to \operatorname{Spec} R_s$ over $\operatorname{Spec}\theta \circ \eta_V$ with $y_o \circ \kappa = y_C$. Since $\prod_i s_i \neq 0$, the map $R_s \to \operatorname{Frac} R$ is injective. So $\xi$ restricted to $\operatorname{Spec} R_s$ equals $j \circ y_o$, as both restrict to $j \circ y_{C_1}$ at the generic point. Then $\xi \circ \operatorname{Spec}\theta \circ \eta_V = j \circ y_o \circ \kappa = j \circ y_C = \xi_V \circ \eta_V$. As $V \to \operatorname{Frac} V$ is injective, (4) follows.

## In the Lean code

The theorem is in [ExistsTautologicalChartVersality.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartVersality.lean#L38). It calls:

- `GlobalTheory.T.exists_canonical_family_through_degenerating_family`;
- `GlobalTheory.T.canonicalFamily_isPointRigid_tautologicalChart`, a statement form of `UCanon.isTautB_of_canon`;
- `GlobalTheory.UChart.taut_exists_map`, which takes only the first half `IsTaut` of `IsTautB`;
- the helpers `spMap_isDominant_of_injective`, `spMap_ext_of_injective` and `isSeparated_of_projOver` in the same file, and `ext_of_isDominant_of_isSeparated` from Mathlib.

The conclusion does not say that $\theta$ is unique, so the chart is versal, not universal.
