---
id: kato-two-w-of-prints-h
title: Vanishing of two Bloch-Kato Selmer groups, from the extended hypotheses
kind: theorem
decl: UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.KatoTwoWOfPublishedH
covers: 9555
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{KatoTwoW}$ from the extended hypotheses $\mathrm{HypothesesH'}$. The theorem [VWin from the extended hypotheses](/entry/vwin-of-hypotheses-h-e-alt/) uses it as the input to the first count, $\mathrm{CountI}$ (Step 5 of the chapter [The window bound VWin](/proof/vwin/)). The proof only fills in two hypotheses of [the next theorem](/entry/kato-two-w-of-prints-h-of-r-t-of-quad-bc2/), which has the real content.

## Statement

**Theorem.** If $\mathrm{HypothesesH'}$ holds, then $\mathrm{KatoTwoW}$ holds.

In short, $\mathrm{KatoTwoW}$ says this. Let $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ be a [[Galois representation|JQEYEQJY2G]], and suppose that $W$ satisfies a list of side conditions $\mathrm{Used}$ (with an odd prime $\ell$, an integer $e \ge 1$, an imaginary quadratic field $K$ and a quadratic character $\theta$ with kernel $G_K$). Suppose that the twist of $W$ by $\bar\chi^{-e}$ is attached to a newform of weight $2e+1$, and that $W$ satisfies the condition $\mathrm{WitAQ}$. Then the Bloch-Kato Selmer groups of $W$ and of $W \otimes \theta$ vanish. The [next entry](/entry/kato-two-w-of-prints-h-of-r-t-of-quad-bc2/) gives the full statement.

## Proof

Apply `katoTwoW_of_printsH_of_rT_of_quadBC2` to the hypotheses, to the row statement $\mathrm{RowT}$ and to quadratic base change $\mathrm{QuadBC2}$. The row statement is the field `litN.aut.gal` of the hypotheses. $\mathrm{QuadBC2}$ is a theorem.

## In the Lean code

The theorem is in [KatoTwoWOfPublishedH.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KatoTwoWOfPublishedH.lean#L48). The proof is one line:

```
katoTwoW_of_printsH_of_rT_of_quadBC2 P (rowOf' P.toClassicalTheorems.litN.aut.gal) quadBC2
```

- `UpperTheory.Gal.SV.rowOf'` is the identity map on $\mathrm{RowT}$, in [GaloisRepExistsTotallyRealGL2.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RankTwoPatching/GaloisRepExistsTotallyRealGL2.lean#L60).
- `UpperTheory.ConvolutionTheory.R2.quadBC2` proves $\mathrm{QuadBC2}$, in [QuadBC2.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/QuadBC2.lean#L18).

So this theorem is a pass-through. Because $\mathrm{QuadBC2}$ is proved, the hypothesis `hQ` of the next theorem is never a real assumption.
