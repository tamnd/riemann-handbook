---
id: pres
title: A presentation of the patched module from the Selmer conditions
kind: theorem
decl: UpperTheory.V.Pa.pres
module: Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.SelmerScaling.AlCSmul
covers: 321
status: drafted
drafted_by: writer@claude
---
This theorem turns three conditions on Selmer classes into a presentation of a module $N$ over a complete local ring $\hat B$, modulo a small ideal. The private lemma `ctx_out` uses it to prove `galOut`, a statement that one prime of $\hat B$ lies in another. It lies below the [main fork](/proof/vwin/). The proof is linear algebra on the tangent space of $\hat B$.

## Statement

Fix a context $S$ (`Ctx`). It contains a point $x$ with fraction field $F$, a local ring $\hat B$ (a completion of the universal ring at the kernel of an ordinary point) with a map $r_F \colon \hat B \to F$ whose kernel is the maximal ideal $\mathfrak{m}$, a complete discrete valuation ring $\mathcal{O}'$ that maps onto $F$ through $\hat B$, and an algebra $\hat B + N$ (`U.AA`) with a finite $\hat B$-submodule $N$. It also contains $g$ classes $\kappa_1, \dots, \kappa_g$. Let

$$J_2 = \mathfrak{m}_{\mathcal{O}'} \hat B + \mathfrak{m}^2 + (yy' : y, y' \in N,\ yy' \in \hat B),$$

and let $T$ be the $F$-space of derivations $\alpha \colon \hat B \to F$ at $r_F$ that kill $\mathcal{O}'$ and the products $yy' \in \hat B$ with $y, y' \in N$.

**Theorem.** Suppose:

1. `SelmerRankBoundLaurent`: each family of cocycles in `Sel1`, with values in matrices over the ring `DD` and with bounded denominators, that is independent modulo `Bd1`, has at most $D_0$ elements;
2. `EvenCocyclesLiftLaurent`: among any $g+1$ families of $g$ bounded cocycles in `SelP`, some nonzero combination lifts to a bounded element of `Sel2`;
3. `SelmerSpannedByKappaLaurent`: each bounded cocycle in `SelM` is a combination of the $\kappa_j$ modulo `BdM`.

Then (`Pres`) there are $X_1, \dots, X_{D_0} \in \mathfrak{m}$, generators $m_1, \dots, m_g$ of $N$ and coefficients $c_{ij,a} \in \mathcal{O}'$ such that the $g^2$ vectors $(\bar c_{ij,a})_a$ are linearly independent over the residue field, $\mathfrak{m} \subseteq (X_1, \dots, X_{D_0}) + J_2$, and

$$\sum_{j} \Bigl(\sum_a c_{ij,a} X_a\Bigr) m_j \in J_2 N \quad \text{for each } i.$$

## Proof

1. `tpDual`: $T$ is finite-dimensional, an element of $\mathfrak{m}$ killed by all of $T$ lies in $J_2$, and each linear form on $T$ comes from an element of $\mathfrak{m}$.
2. `alSel` maps each $\alpha \in T$ linearly to a bounded cocycle in `SelP`. Let $U \subseteq T^g$ be the families $(\alpha_j)$ whose cocycles lift. It is a subspace by `liftsSub`.
3. Hypothesis 2 shows that any $g+1$ elements of $T^g$ have a nonzero combination in $U$. Hypothesis 1, through `claim1`, gives $e + g^2 \le D_0$ for each independent family $\alpha_1, \dots, \alpha_e$ with all $\alpha_i e_j \in U$.
4. `linAlg` then gives linear forms $X_1, \dots, X_{D_0}$ that span $T^*$ and $g^2$ independent coefficient vectors $c$ with $\sum_{j,a} c_{ij,a} X_a(\alpha_j) = 0$ on $U$. Lift the $X_a$ to $\mathfrak{m}$ by step 1 and the $c$ to $\mathcal{O}'$.
5. `dualEx`, from hypothesis 3, gives the generators $m_j$. The relations follow from `phSep` and `claim2`.

## In the Lean code

The theorem is in [AlCSmul.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SelmerScaling/AlCSmul.lean#L12). `Ctx`, the three hypotheses and `Pres` are in [SelmerSpannedByKappaLaurent.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SelmerScaling/SelmerSpannedByKappaLaurent.lean#L38). `linAlg` is in [LinAlg.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SelmerScaling/LinAlg.lean#L45). The user is `ctx_out` in [GalOut.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/GalOut.lean#L16). We have not unfolded `Sel1`, `Sel2`, `SelP`, `SelM`, `BndD` or the module structure `URep`.
