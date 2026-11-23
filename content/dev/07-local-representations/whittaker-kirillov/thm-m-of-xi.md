---
id: thm-m-of-xi
title: The rank-one Bessel integral from the structural facts and a majorant
kind: theorem
decl: ReciprocityTheory.ChartRestriction.DS.Mult1.thmM_of_xi
module: ReciprocityTheory.ReductiveGroups.DiscreteSeries.MultiplicityOne.ThmMOfXi
covers: 948
status: drafted
drafted_by: writer@claude
---
This theorem proves [the rank-one statement](/entry/thm-m/) for the local Bessel integral $\beta$ from two hypotheses: the structural facts on the unitary group, and the existence of a majorant $\Xi$ ([`XiExists`](/entry/xi-exists/)). Its proof hands about 23 step lemmas to `theoremM_of`, which does the work.

## Statement

**Theorem.** Assume `UnitaryGroupStructuralFacts`, a conjunction of 18 facts on $G$, and `XiExists`. Then `ThmM` holds.

`ThmM` is stated in [the parent entry](/entry/thm-m/). In short: $\beta(u, u') = l(u) \otimes \overline{l(u')}$ for one equivariant map $l$.

## Proof

All the work is in `theoremM_of`. Let $d > 0$ be the formal degree of $\sigma$, given by the Schur orthogonality step `StSchurG`. Let $a$ be the decay exponent of $w$ and $b = a - n^2 - 1$.

1. **Integrability.** The integrand of $\beta(u, u')$ is integrable on $W \times N$ for $u, u' \in V_a$ (`beInt_integrable_of`).
2. **Symmetry.** $\langle \xi, \beta(u, u')\eta\rangle = \langle \beta(u', u)\xi, \eta\rangle$ (`StBeHerm`).
3. **Growth.** For $v \in V_a$, $\|\beta(\sigma(y)w, v)\| \leq C\|y\|^{b}$ (`be_bound`, from `StPairs` and `StSInt`).
4. **Reproducing formula.** $\beta(u, v) = d \int_G \langle \sigma(y)w, u\rangle\, \beta(\sigma(y)w, v)\, dy$ (`StRepro`).
5. **Vanishing minors.** For all $u_1, \ldots, u_4 \in V_a$ and $e_1, \ldots, e_4 \in V$,
$$\langle e_1, \beta(u_1, u_2)e_2\rangle \langle e_3, \beta(u_3, u_4)e_4\rangle = \langle e_1, \beta(u_1, u_4)e_4\rangle \langle e_3, \beta(u_3, u_2)e_2\rangle.$$
`minors_DD` proves this on a smaller set `DDinf`, and `minorsOn_of_DD` extends it to $V_a$ with items 2 to 4. This is the only place where `XiExists` is used: `minors_DD` receives it with the cutoff steps `StCut0` to `StCut4`, the dichotomies `StDichoG` and `StDichoW`, and `StMixed`. We have not unfolded `minors_DD` or `DDinf`.
6. **Factorization.** `multOne_of_minors` takes items 1, 2 and 5, the positivity $\operatorname{Re}\langle \xi, \beta(u, u)\xi\rangle \geq 0$ (`StBePos`), and the equivariance of $\beta$ (`StBeEquiv`). It gives $l$. This is the step from a positive hermitian kernel whose $2 \times 2$ minors vanish to a kernel of the form $f(x)\overline{f(y)}$.

## In the Lean code

The theorem is in [ThmMOfXi.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/ThmMOfXi.lean#L30). `theoremM_of` is in [TheoremMOf.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/TheoremMOf.lean#L16), `MinorsOn` and `multOne_of_minors` in [BeIntIntegrableOf.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/BeIntIntegrableOf.lean#L42), and `minors_DD` in [SepMinors.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/SepMinors.lean#L112).

Most step lemmas take the structural facts as an argument. `stSchurG`, `stFrame`, `stInvChar`, `stInvCC` and `rankOneMinors` do not.

Five parameters of `theoremM_of` are not used in its proof: `h4b` (`StInvChar`), `h5` (`StReps`), `h6` (`StTransM`), `h7` (`StSym`) and `hR` (`RankOneMinors`). The last one is the minors-to-factorization lemma of item 6 for scalar kernels, but `multOne_of_minors` does not receive it.
