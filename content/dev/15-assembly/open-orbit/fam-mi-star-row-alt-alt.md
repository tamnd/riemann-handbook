---
id: fam-mi-star-row-alt-alt
title: The period identity on the row of linked bundles
kind: theorem
decl: GlobalTheory.Fam.miStar_row_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremPublishedResultsFinal
covers: 10465
status: drafted
drafted_by: writer@claude
---
This theorem proves a period identity, `MIstar2`, at every linked bundle of a row. It proves that the real pack of each bundle is true and that a period map does not vanish, and calls [the pack theorem](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/). Its only user is [a renaming](/entry/main-theorem-published-results-final-alt-alt/). The result goes to the multiplicity condition of branch 3 of the [unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

**Rows.** A *row* $\mathrm{RowE}_Q^{\mathrm{Lk}}(E)$ says that a property $E$ of bundles holds eventually in the parameter $\kappa = (\varepsilon, C, c_D, c_h, C_5, c_6, C_b)$. The range (`ParEv`) is: $0 < \varepsilon \le \varepsilon_0$ with $\varepsilon < 1/52$; the constants of $C$ above a threshold that may depend on $\varepsilon$, $C_5$, $c_6$, $C_b$ and $C_{\mathrm{pde}} \ge 1$; then $c_D$ large; then $c_h$ large. For such $\kappa$ with $C_5, c_6, C_b > 0$ there is $x_0$ such that $E$ holds at each bundle $b$ with $\mathrm{Lk}(K, \beta, c, b)$, for each context $K$ of $\kappa$ with $K.s.x \ge x_0$, each point $\beta$ of $K$ in the slot $Q$ and each $c \in \mathbb R$.

Here $Q$ is `IsGoodE p.s`: built points with the kernel condition `EntC` that are good (`GoodO`). A bundle (`BundleCondition D O c`) is a recursion datum, spectral ties, a row side family, columns and a real theta datum $B$ with a realisation $B.Q$, and side conditions. The link `BundleLinkage p` says that $b$ equals a bundle $b'$ over a weighted point $q$ of $p.s$, with a `BundleWitness` for $(q, b')$. `packB_alt b` is the real pack made of these data.

**The period identity.** On the coefficient space $X$ of the realisation, `MIstar2` says that there are a linear map $V$ on $E_X$, scalars $a(u) \ne 0$, matrices $U(u)$ and scalars $\zeta(u,t)$ such that:

1. $V$ preserves the subset `EEl true` and the norm on it, and each $U(u)$ preserves the norm `fnorm`;
2. $\zeta(u,t) \ne 0$, $\zeta(u,\mu_0) = 1$, and $\zeta(u,\mu(w))$ is a unit at $w$ when it lies in the field $K$;
3. for all $u, t, \varphi, F$: $\zeta(u,t)\,\iota\bigl(P_{u,t}(\varphi,F)\bigr) = a(u)\,\bigl\langle s(V\Theta_t(j_t(e_t F))),\ \mathrm{Pu}_u(U(u)\,\iota\varphi)\bigr\rangle$.

We have not unfolded $\Theta_t$, $j_t$, $P_{u,t}$ or $\mathrm{Pu}_u$.

**Theorem.** Assume the literature hypotheses `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `CasselmanWallach`, `HoweUnram`, `WeilRepresentationUnitaryPair`, `WeilSiegelFormulaUnitary`, `SiegelWeilUnitaryConvergent`, `DoublingMethodLocalZetaIntegrals`, `UnramifiedDoublingGL`, `DiscreteSeriesClassification` and `StrongApproxSU`. Assume a diagonal row hypothesis $H_D$ (`RowDiag` for scales with bounded $\Gamma$ constant and `RankMu`). Let $h_L$ be a proof of [RecTExists](/step/rect-exists-def/) and $p$ parameters for $h_L$. Assume that `RXs` is nonempty at each weighted point, and the row of `BundlePointConditions` (ten conditions, among them $1 \le r_S$). Then the row of `MIstar2` holds.

## Proof

1. **True packs.** Unpack the link of $b$ into $q$, $b'$, a witness and $b = b'$. Transport the point conditions along this equality. Then `true_pack_of_bundle_witness` gives `TruePackAlt (packB_alt b)`.
2. **Nonvanishing.** `puNZ_of_truePack` takes $H_D$, $h_L$, $p$ and the row of true packs. It gives the row of `PuNZ D`: each period map $\mathrm{Pu}_u$ is nonzero.
3. **Assembly.** Join the rows of steps 1 and 2 with the point conditions. At each $b$, apply [`main_theorem_from_published_results_alt_alt_alt_alt_alt`](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/) to `packB_alt b` with the true pack, the field $1 \le r_S$ and `PuNZ`. Its conclusion `RealPackageCondition` is `MIstar2` by definition. The rest is bookkeeping.

## In the Lean code

The theorem is in [MainTheoremPublishedResultsFinal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedResultsFinal.lean#L24). It calls:

- `GlobalTheory.T.true_pack_of_bundle_witness`, in [TruePackOfBWitStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TruePackOfBWitStatement.lean#L17);
- `GlobalTheory.T.puNZ_of_truePack`, in [PuNZMemberStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PuNZMemberStatement.lean#L17);
- [`main_theorem_from_published_results_alt_alt_alt_alt_alt`](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/);
- `RowE.imp` and `RowE.and`, next to [`RowE`](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L261).

The hypothesis on `RXs` is used only in step 1, $H_D$ only in step 2, and the literature hypotheses only in step 3.
