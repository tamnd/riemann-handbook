---
title: Three rows from Siegel-Weil
decls:
  - GlobalTheory.LocalRows.lg1_sLp_sO_hTF
  - GlobalTheory.LocalRows.sLp_sO_hTF_of_siegelWeil
  - GlobalTheory.LocalRows.at_choice_alt
  - GlobalTheory.LoopRowsByName.loopRows_of_rowsFinDim_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Three rows from Siegel-Weil

This section proves three rows of the record of all rows from the convergent Siegel-Weil formula of Section 2. They are a loop bound, an off-diagonal bound and a frame bound. Step 4 of [the theorem on all rows](/entry/all-rows-of-open0-alt/) uses them. The three bounds hold for every selection of bundles. So the rows hold at every slot and every linkage, and the true slot of Section 1 puts them in linked form. The analytic content is in [the off-diagonal bound](/entry/carrier-gap-off-diag/) and in [the loop rows of a closed gap](/entry/loop-rows-closed-gap/). Here we only assemble.

We use the notation of Section 1. Let $\mathcal{A}$ be a family class and $\sigma$ a selection of bundles for $\mathcal{A}$. Write $\mathcal{D} = \mathcal{D}_3(\mathcal{A})$. A selection $\sigma$ gives a selection $s_\sigma$ of spectral ties: a threshold and the ties of each selected bundle. It also gives a twist selection $T_\sigma$ on $\mathcal{D}$.

**Definition 8.3.1 (The three bounds).** Let $\mathcal{A}$ be a family class and $\sigma$ a selection.

1. The *loop bound* at $(\mathcal{A}, \sigma)$ says: it is [closed](/step/closed-def/) on $\mathcal{D}$ that, eventually in $x$, the sums of $|\langle v_{p_1}, v_{p_2} \rangle|$ of the ties of $s_\sigma$ over the big pairs and over the non-scalar pairs are small, with the constant $3$.
2. The *off-diagonal bound* at $(\mathcal{A}, \sigma)$ says: it is closed on $\mathcal{D}$ that, eventually, under a size hypothesis, for each $x$ above the threshold and each pair of distinct words $u \neq u'$,

$$\|K_0(u, u')\|^2 \le \bigl(1 + b^{-6}\bigr)\, \frac{d(u)\, d(u')}{D^*}.$$

Here $K_0(u, u')$ is an off-diagonal entry of the ties, $b$ is a scale of the size data, and $d$ and $D^*$ are data of the selected datum.

3. The *frame bound* at $\mathcal{A}$ says: it is closed on $\mathcal{D}$ that, eventually, under a size hypothesis, $1 \le \operatorname{Tr}(w)\, \kappa^{2 r_S}$ for each $w$.

The frame bound does not depend on $\sigma$.

**Lemma 8.3.2 (The loop bound from finite dimensional rows).** Let $\mathcal{C}$ be a family class. Assume that the rows are finite dimensional, that the mass ratio under volume holds for each datum, that $T$ is a twist selection on $\mathcal{C}$, that $s$ is a selection of spectral ties and that each family of $\mathcal{C}$ satisfies the size condition on its words. Then the loop bound holds on $\mathcal{C}$ for $s$, with the constant $3$.

Lean: `GlobalTheory.LoopRowsByName.loopRows_of_rowsFinDim_alt`.

*Proof.* This is [the loop rows of a large gap and the discrete series](/entry/loop-rows-of-large-gap-discrete-series/) applied to the hypotheses and five more inputs. Four inputs hold with no hypothesis: the uniqueness of the gap, the Bessel model of the Whittaker data, the pointwise bound for coefficients of the [[discrete series|9AB7HYGPEK]], and the decay of the Whittaker function of a gap. The rank bound is the first part of the ranks and frame bound of a tied class, applied to the mass ratio and $T$. $\square$

**Theorem 8.3.3 (Three bounds at every selection).** Assume the convergent Siegel-Weil formula. Then for each family class $\mathcal{A}$ and each selection $\sigma$, the loop bound, the off-diagonal bound and the frame bound hold.

Lean: `GlobalTheory.LocalRows.at_choice_alt`.

*Proof.* Write $T = T_\sigma$. There are three steps.

1. **Ranks and frame.** The Siegel-Weil formula gives two closed statements on $\mathcal{D}$: a rank bound for the ties, and the frame bound. The second is part 3.
2. **Loop bound.** The volume ratio of the Siegel-Weil formula gives the mass ratio under volume for each datum. The rows are finite dimensional with no hypothesis. Each family of $\mathcal{D}$ satisfies the size condition on its words, since this is part of membership in $\mathcal{D}$. So the Lemma (The loop bound from finite dimensional rows) applies to $\mathcal{D}$, $T$ and $s_\sigma$, and it gives part 1.
3. **Off-diagonal bound.** The Siegel-Weil formula also gives two inputs of the off-diagonal bound: a sum bound over the words, and a bound for the rows of the good points. Each selected datum is tied at its local places, since this is a property of the selected bundle. [The off-diagonal bound](/entry/carrier-gap-off-diag/) takes these inputs, the finite dimension of the rows, the rank bound of step 1 and part 1. It gives part 2. $\square$

The three bounds now become rows. For a slot $Q$ and a linkage $\Lambda$, the *loop row* is $\mathrm{Row}(Q, \Lambda, H_1)$, the *off-diagonal row* is $\mathrm{Row}(Q, \Lambda, H_2)$ and the *frame row* is $\mathrm{Row}(Q, \Lambda, H_3)$, where $H_1$, $H_2$ and $H_3$ are the three bounds as statements in $(\mathcal{A}, \sigma)$.

**Corollary 8.3.4 (Three rows).** Assume the convergent Siegel-Weil formula. Then for each slot $Q$ and each linkage $\Lambda$, the loop row, the off-diagonal row and the frame row hold.

Lean: `GlobalTheory.LocalRows.sLp_sO_hTF_of_siegelWeil`.

*Proof.* A row holds with the true property of bundles when its statement holds for every selection. This is the first fact about rows of Section 1. By the Theorem (Three bounds at every selection), each statement holds for every selection. $\square$

**Corollary 8.3.5 (Three linked rows).** Assume the convergent Siegel-Weil formula. Let $K$ be a property of bases and $Q$, $Q'$ slots, and let $\Lambda$ be a linkage. Then

$$\begin{aligned} &\mathrm{Lg}\bigl(K, Q, Q', S \mapsto \mathrm{Row}(S, \Lambda, H_1)\bigr), \\ &\mathrm{Lg}\bigl(K, Q, Q', S \mapsto \mathrm{Row}(S, \Lambda, H_2)\bigr), \\ &\mathrm{Lg}\bigl(K, Q, Q', S \mapsto \mathrm{Row}(S, \Lambda, H_3)\bigr). \end{aligned}$$

Lean: `GlobalTheory.LocalRows.lg1_sLp_sO_hTF`.

*Proof.* Take $R = \top$. By the Remark on the true slot of Section 1, the large base condition holds. The Corollary (Three rows) applied to the slot $Q' \wedge \top$ gives each row. $\square$

So $K$, $Q$, $Q'$ and $\Lambda$ play no role. The rows hold because the bounds hold for every selection, and not because of any property of the good points.

**Remark 8.3.6 (Formalization).** The three results are at [AtChoice.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean#L16), lines 16, 24 and 27. The three bounds are `SelectionLpBound`, `SelectionOrderBound` and `H_hTF`, and the rows are `SlotLpCondition`, `SlotOrderCondition` and `SlotTorsionFreeCondition` in [CountsIrreducibilityConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CountsIrreducibilityConstants.lean#L95). The names mislead: "Lp" is the loop bound `LoopRowS`, "order" is the off-diagonal bound, and "torsion free" is the frame bound `TFrame`. The fields they fill in the record are `sLp`, `sO` and `hTF`. The proof of the theorem calls `bothRowsFromSiegelWeil_alt`, `volumeRatio`, `rowsFinDim_link`, `swxs_of_siegelWeil`, `rowNGP_of_siegelWeil` and `CarrierGap.offDiag`, and the tie condition of step 3 is the field `LocTied` of the selected bundle. The lemma at [LoopRowsOfRowsFinDim.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LoopRowsOfRowsFinDim.lean#L11) copies `loopRows_of_rowsFinDim` in [LoopRowOfFiniteDim.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowOfFiniteDim.lean#L27), with `TwistSelection` in place of `TSel`; its name mentions one of its five inputs. The second corollary ignores that $\sigma$ is a selection for $Q$ and $\Lambda$.
