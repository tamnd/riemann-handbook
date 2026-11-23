---
id: xi-exists
title: A majorant for convolutions of decaying coefficients
kind: theorem
decl: ReciprocityTheory.ChartRestriction.DS.Xi.xiExists
module: ReciprocityTheory.ReductiveGroups.DiscreteSeries.TailIntegrals.XiExistsOfIn
covers: 942
status: drafted
drafted_by: writer@claude
---
This theorem proves `XiExists`: there is a function $\Xi$ on the group that majorizes convolutions of fast-decaying functions and is integrable against the Bessel subgroup. It is an input of [HypsAlt](/step/nonempty-hyps/), and [the rank-one theorem](/entry/thm-m-of-xi/) uses it. The proof only fills the hypothesis of [`xiExists_of_in`](/entry/xi-exists-of-in/) with the proved facts `heisenbergHaarFacts_hold`. That entry has the real content.

## Statement

Let $G$, $N$, $W$, $z$ and the measures be a real-place datum `RealPlaceData`, with $n = 2r + k + 1$ and $\|x\|$ the Frobenius norm. Let $\lambda(m) = \operatorname{Re}(c\,\ell(m))$ be the linear form on $N$ that defines the character.

**Theorem.** For every $A \geq 2(k + r)(r + 1) + 1$ there is $\Xi \colon G \to \mathbb{R}_{\geq 0}$ with these properties.

1. There is $C$ such that, for measurable $F, F'$ with $\|g\|^A \|F(g)\| \leq c$ and $\|g\|^A \|F'(g)\| \leq c'$ on $G$, and for all $x, y \in G$,
$$\int_G \|F(x^{-1}gy)\|\, \|F'(g)\|\, dg \leq C c c'\, \Xi(x)\, \Xi(y).$$
2. $\Xi$ is measurable, and $\int_W \int_N \Xi(mh)\,(1 + |\lambda(m)|)^{-2}\, dm\, dh < \infty$, for $z$ and for $z'$.

## Proof

`xiExists_of_in heisenbergHaarFacts_hold`. The function is explicit: $\Xi(x) = \prod_{l=0}^{r} \Delta_l(x)^{-s_l}$. Here $\Delta_l(x)$ is the square root of the Gram determinant of $x\varphi_0, \ldots, x\varphi_l$, where $\varphi_a$ are the isotropic basis vectors $e^*_a$ for $a < r$ and $\varphi_r = (w_0 + w_k)/\sqrt{2}$. The exponents are a little below $2$ for $l < r$ and below $k$ for $l = r$. The two bounds come from an induction on $r$.

## In the Lean code

The theorem is in [XiExistsOfIn.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/XiExistsOfIn.lean#L21). `XiExists`, `CoefBound` and `XiInt` are in [StatementB.lean](lean:Formalism/HermitianCurvature/StatementB.lean#L439). The function $\Xi$ is `xiN` in [InductiveHeisenbergInputs.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/InductiveHeisenbergInputs.lean#L33).
