---
id: good-tower-volume-theorem-bis
title: The good tower and the volume theorem from ten inputs
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis
module: Development.WeilBound.CoreStatements.AutomorphicKernels.MoriwakiBigness.HilbertSamuelApplications.GoodTowerVolumeTheoremBis
covers: 21078
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem says that a good tower of integral models of unitary Shimura varieties exists, and that its arithmetic self-intersection numbers obey the volume theorem. Its only caller is [`deepStR_of_use`](/entry/deep-st-r-of-use/), which passes the pair to [`deepStR_of_volume`](/entry/deep-st-r-of-volume/). This is Step 4 of [the Weil bound chapter](/proof/weil-bound/). The theorem only collects inputs. The assembly is [`goodTower_volume_of_reduced`](/entry/good-tower-volume-of-reduced/).

## Statement

**Hypotheses.** Ten Lean statements with names from the literature: `ArithIntersectionSystemStatement`, `HSUse`, `MoriwakiBigStatement`, `ResKStatement`, `SemiAbelianHomExtension`, `FarguesHodgeTate`, `GagaSections`, the Siegel lemma `LineOfLargeDegree.Statement` (stated in [its entry](/entry/line-of-large-degree-of-use/)), `QuotientByFiniteFlatStatement` and `ZarhinStatement`. The [chapter](/proof/weil-bound/) states `HSUse` and `MoriwakiBigStatement`. We do not unfold the others.

**Conclusion.** `GoodTowerExistsX` and `VolumeTheoremX`.

`GoodTowerExistsX`: let $E$ be a CM field with a host $H$ and a datum $D$ of signature $(p, q)$, $p, q \geq 1$, and let $Y$ be a global integral model with split components. Then there are a root tower $T$ and a good origin $o$ of $Y$ in $T$ with the property `Extra`. `Extra` says two things. Near each point of each complex analytic system of $o$, the point map has a local holomorphic lift whose affine coordinates have an injective derivative. The torsion exponent of each Hodge component of $o$ is 4 at each prime of the sets $S_B$ of $o$.

`VolumeTheoremX`: there is $C \geq 0$ with this property. Let $E$ be abelian over $\mathbb{Q}$, let $T$ and $o$ be as above, and let $II$ be a full intersection system. Suppose $q \geq 1$, $3q + 1 \leq N = p + q$, and that $T$ has at most $4\,\#\mathrm{CMType}(H)\,N^2$ bad primes. Then six statements hold: `Proportional` (each component $c$ has volume $\mathrm{vol}(c) > 0$, and geometric degrees on $c$ are $\mathrm{vol}(c)$ times the flag degree), `VolEq` (all volumes are equal), `T1` (slopes are limits of slopes of perturbed nef bundles), `ThmB` (not unfolded), `T2` (a lower bound for the total self-intersection) and `MeanSlope`. The last says: for each weight $u$ with a gap $g$ and each integer $B \geq 128$ with $B + 1 > 4\,\#\mathrm{CMType}(H)\,N^2(1 + \|u\|/g)$ and $B \geq \#\mathrm{bad}(T)$,

$$-C\Big(\big(\log(B\,\mathrm{rd}(E)) + |\ell_d|\big)\|u\|_1 + \min(j, N-j)\,\mathrm{spread}(u)\Big) \leq \frac{1}{\#\mathrm{Comp}(T)} \sum_{c} \mathrm{slope}(c, u).$$

Here $j$ is the index of $T$, $\mathrm{rd}(E) = |\operatorname{disc} E|^{1/[E:\mathbb{Q}]}$, $\ell_d = \operatorname{Re} \frac{L'}{L}(1, \chi_d)$ for the quadratic character modulo the prime $d$ of $H$, $\|u\|_1 = \sum_{\tau,i} |u_{\tau,i}|$, $\mathrm{spread}(u) = \sum_\tau (\max_i u_{\tau,i} - \min_i u_{\tau,i})$, and $\mathrm{slope}(c,u)$ is the self-intersection of the line bundle of weight $u$ on $c$, divided by $(\dim + 1)\,\mathrm{vol}(c)$ and the flag degree of $u$.

## Proof

1. `given_of_use` turns the first eight hypotheses into `Top.Given`, a conjunction of 14 statements.
2. The proof takes 11 parts out of `Top.Given`. It drops `SAStatement`, `SlopeBoundSt` and `AntisymPerturbation.Statement`.
3. It calls [`final_theorem_of_inputs_right`](/entry/final-theorem-of-inputs-right/) with these parts, the Siegel lemma, `PtsIntegrableStatement` (from `ResKStatement` by `points_integrable_of_resolution_statement`), the theorems `topAvoid` and `thetaUnifAV_closed`, and the hypotheses `QuotientByFiniteFlatStatement` and `ZarhinStatement`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [GoodTowerVolumeTheoremBis.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/GoodTowerVolumeTheoremBis.lean#L9). The conclusions are in [GoodTowerExistsX.lean](lean:Development/AutomorphicSpectrum/Statements/TowerExistence/GoodTowerExistsX.lean#L22). It calls `given_of_use`, `final_theorem_of_inputs_right`, `points_integrable_of_resolution_statement`, `Giv.topAvoid` and `thetaUnifAV_closed`.

All ten hypotheses are used. The proof builds `Top.Given` and takes it apart, and `goodTower_volume_of_reduced` builds it again with `final_theorem_of_inputs_left`. The caller `deepStR_of_use` also calls `given_of_use`. So the same conjunction is built three times. The word "bis" in the name means nothing in the statement.
