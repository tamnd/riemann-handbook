---
id: field
title: The Siegel-Weil formula for unitary groups in the Schrödinger model
kind: theorem
decl: PositivityTheory.SiegelWeilCoefficients.field
module: Development.WeilBound.RepresentationTheoryGL.EisensteinSeries.SiegelEisensteinHalfPlane.IntegralUnitCoefficients.CoefND
covers: 1658
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `SiegelWeilUnitarySchrodinger`: a [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula) for the dual pair $(\mathrm{U}(n,n), \mathrm{U}(V))$, with the Weil representation in the Schrödinger model. The literature layer of [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) cites it as the field `siegelWeilUnitarySchrodinger` of the bundle [UnitaryGroupThirdPlaceHypotheses](/step/unitary-group-third-place-hypotheses-def/). The theorem `convergent` also uses it, through `sw_doubled_of_std`, to get `SiegelWeilUnitaryConvergent`. The proof is a short wrapper. The identity itself is the theorem [lit](/entry/lit/).

## Statement

Let $E/F$ be the CM extension of the data $D$, let $V$ be a Hermitian space over $E$ of dimension $m$ with Witt index $r$, and let $n$ be an integer with

$$n < m \le 2n, \qquad n + r < m.$$

Take the data of the entry [lit](/entry/lit/): a Hecke character $\chi$ with $\chi|_{\mathbb{A}_F^\times} = \eta^m$, the Weil representation $\omega$ of $G = \mathrm{U}(n,n)(\mathbb{A})$ on $S(V(\mathbb{A})^n)$, the height $H$, the section $\Phi_z(g) = H(g)^{z - s_0} (\omega(g)\Phi)(0)$ with $s_0 = \tfrac{m-n}{2}$, and $\Phi$ in the Fock-type space. Then:

1. for each $g$, the theta function $h \mapsto \theta(g, h; \Phi)$ is integrable on $\mathrm{U}(V)(F) \backslash \mathrm{U}(V)(\mathbb{A})$;
2. for $\operatorname{Re} z > \tfrac{n}{2}$, the section $\Phi_z$ is left invariant under $P(F)$, and the [[Eisenstein series|3NZBZXYWAJ]] $E(g, z, \Phi) = \sum_{\gamma \in P(F) \backslash G(F)} \Phi_z(\gamma g)$ converges absolutely;
3. $z \mapsto E(g, z, \Phi)$ continues to a function that is holomorphic at $s_0$, with value the normalized theta integral $I(g, \Phi)$.

## Proof

The proof is `siegelWeilUnitarySchrodinger_of_lit lit wtc`. That lemma takes part 3 from [lit](/entry/lit/) and proves parts 1 and 2:

- part 1 by `integrable_standardPair_theta_weilRange`, from `WeilThetaConvergence` (the theorem `wtc`) and the condition $n + r < m$;
- part 2 by `leftInv_sect`, with the Iwasawa decomposition `Iwasawa.exists_mul`, and by `cosetConv_stdSec`, with `fock_mem_degenerate`.

The rest is bookkeeping.

## In the Lean code

The theorem is at [CoefND.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/IntegralUnitCoefficients/CoefND.lean#L24). The statement is at [SiegelWeilUnitarySchrodinger.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SiegelWeil₂/SiegelWeilUnitarySchrodinger.lean#L107). The bridge lemma is at [Bridge.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/SiegelWeilSchrodinger/Bridge.lean#L21). Of the 1,658 declarations below this theorem, 1,649 are below `lit`.

The names `field` and `lit` say nothing about the content. The file is named after a third theorem, `coefND`.
