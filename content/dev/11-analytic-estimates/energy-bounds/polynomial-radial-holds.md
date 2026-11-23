---
id: polynomial-radial-holds
title: The radial polynomial relation
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.Core.TC.PR.polynomial_radial_holds
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutJAPRFinal
covers: 488
status: drafted
drafted_by: writer@claude
---
This theorem proves `PolyRadialS` with no hypothesis. `PolyRadialS` says that on the fibre over $\zeta$, the shift operator $S_\zeta$ and an explicit operator $\theta_\zeta$ agree after projection, up to a factor that is polynomial in $\sqrt{|\zeta|^2 - T_P}$. Its only user is [model places from the smoothness of the transfer](/entry/model-place-built2-of-jf/), which passes it to [model places from the radial polynomial relation](/entry/model-place-built2-of-poly-s/). That entry states `PolyRadialS` in full.

## Statement

**Theorem.** `PolyRadialS` holds.

The proof uses two classes of functions. Fix $T > 0$ and put $\sigma(\zeta) = \sqrt{|\zeta|^2 - T}$ on $\{|\zeta|^2 > T\}$. A function $f$ of $\zeta$ is *polynomial in the radius* (`PS T f`) if there are $m \in \mathbb{N}$ and a polynomial $p$ in three variables with

$$(|\zeta|^2 - T)^m f(\zeta) = p\bigl(\zeta, \bar\zeta, \sigma(\zeta)\bigr) \quad \text{for } |\zeta|^2 > T.$$

A vector-valued function is in `PSV T` if it is a finite sum $\sum_i a_i(\zeta) v_i$ with constant vectors $v_i$ and each $a_i$ in `PS T`.

## Proof

The proof is `polyRadialS_of` applied to two facts.

1. `radial_decomposition_holds` proves `Decomp`. Let $\mu(\zeta)$ be the section `theSection` of the place and put $\eta = \mu^{-1} \partial_\zeta \mu$, $\bar\eta = \mu^{-1} \partial_{\bar\zeta} \mu$. Then each matrix unit $E_{ab}$, placed in the group by `wI`, is a sum $\sum_t b_t(\zeta) B_t + \mu(\zeta)^{-1} \bigl(\sum_t b'_t(\zeta) B'_t\bigr) \mu(\zeta) + \beta(\zeta) \eta + \beta'(\zeta) \bar\eta$. Here the $B_t$ lie in the Lie algebra `InLieW` at $z'$, the $B'_t$ in that at $z$, and all coefficients are in `PS`.
2. `word_polynomial_vector_holds` proves `WordPSVOfCut`, the implication from eight facts to `WordPSV`. `WordPSV` says: if $\Phi$ in the radial space equals a constant $X_0$ along the section on the annulus, then for each word $w$ of derivatives $R_Z$ with $Z$ in the Lie algebra (`GLc`), the function $\zeta \mapsto (R_w \Phi(c))(\mu(\zeta))$ is in `PSV`. Here $R_Z = R_{Z_1} + i R_{Z_2}$ for two parts $Z_1, Z_2$ of $Z$ (`Rc`, from `RdV`, which we have not unfolded). The proof is an induction on the length of $w$. The base case is the constant $X_0$. In the step, the first letter is written in matrix units and `Decomp` splits each unit. The left part acts through $\pi$ (`LeftCov`). The right part is moved to the end of the word (`RcComm`), where it acts through $\pi'$ (`RightCov`); the commutators that this creates give words of the same length, covered by the induction hypothesis. The radial parts become $\partial_\zeta$, $\partial_{\bar\zeta}$ along the section (`SecDeriv`). `PSCalc` says that `PS` and `PSV` are closed under these operations.

Inside `polyRadialS_of`, `corePoly_of` supplies the eight facts, all proved lemmas, and gets `CorePoly`: the same property for the operator `Q.tL` applied to $\Phi$, which `lower_unipotent_matrix_words` writes as a `PS` combination of words of matrix units. `polynomialRadial_of_base` combines `CorePoly` with ten more proved facts, among them `phase_invariance_holds` and `word_nonvanishing_holds`, which we have not unfolded.

## In the Lean code

The theorem is in [CutJAPRFinal.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRFinal.lean#L7). The lemmas it calls:

- `polyRadialS_of` and `corePoly_of` in [CutJAPRRest.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRRest.lean#L36);
- `radial_decomposition_holds` in [CutJAPRCPDecomp.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRCPDecomp.lean#L95), a tactic proof;
- `word_polynomial_vector_holds` in [CutJAPRCPWordAsm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRCPWordAsm.lean#L418), a tactic proof.

`Decomp` and `WordPSVOfCut` are in [CutJAPRCoreCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRCoreCut.lean#L91), and `PS`, `PSV` in [CutJAPolyRadialCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPolyRadialCut.lean#L16).

The name of this theorem fits `PolyRadial`, but it proves `PolyRadialS`; the entry for [`modelPlaceBuilt2_of_polyS`](/entry/model-place-built2-of-poly-s/) notes the same point.
