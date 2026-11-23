---
id: hecke-term
title: One isogeny term of a Hecke operator is one coset term
kind: theorem
decl: GlobalTheory.HeckeTerm.heckeTerm
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.HeckeReadingKernelsMatchCosetsThroughFrame
covers: 335
status: drafted
drafted_by: writer@claude
---
This theorem compares the two Hecke operators at a split prime term by term. On one side is a sum over the subgroups $C$ of the torsion of an abelian variety; on the other, a sum over coset representatives in the adelic unitary group. It gives a bijection between the two index sets and an identity for each pair. Its second name [`heckeReading_kernels_match_cosets_through_frame`](/entry/hecke-reading-kernels-match-cosets-through-frame/) carries it to [the Hecke reading theorem](/entry/hecke-read-tie/), which sums it. Below it are 335 declarations.

## Statement

We use the notation of [the Hecke reading theorem](/entry/hecke-read-tie/): framed points $y_h$ for $h \in G(\mathbb{A})$, the functions $\varphi_f$, the set $\mathcal{C}(y)$ of Hecke kernels, and the relation $z \in y/C$.

**Theorem.** Assume the Hecke point laws `HeckePointLaws`, `SplitLinearModel D` and `VacFixed D`. Assume the conditions on $R$, `TieIn`, $\sigma = \sigma_0$ and the frame pin at $i$. Let $(\mathfrak{P}, p, k, \alpha, R_c)$ be Hecke data at a split-off prime, and let $h \in G(\mathbb{A})$ be such that $y_h$ is defined. Then there is a bijection $e \colon \mathcal{C}(y_h) \to R_c$ with two properties for each $C$. First, some point $z$ satisfies $z \in y_h/C$. Second, for each such $z$ and each section $f$ of weight $\kappa_i$,

$$\lambda\, c(h)\mu(h)\, N(\mathfrak{P})^{-\lfloor k n_V/2\rfloor} f(z) = \mu_i(\mathfrak{P})^{-k}\, \varphi_f(h\, e(C)).$$

`HeckePointLaws` is the conjunction of four facts at Hecke primes: the set $\mathcal{C}(y)$ is finite, each $C$ has a quotient point $z \in y/C$, two quotient points for the same $C$ agree, and a section of a given weight that vanishes at all points is zero.

## Proof

1. **The bijection.** `heckeKernel_complex_point_matches_cosets` gives $e$. It also gives, for each $C$ and each $z \in y_h/C$, that $y_{h e(C)}$ is defined and that $z$ is $y_{h e(C)}$ moved by a torus element $t$ of the frame whose coordinates are $1$ except one, $t_0$ (`FrBor`).
2. **Existence of $z$.** `splitSup` shows $\mathfrak{P} + \bar{\mathfrak{P}} = \mathcal{O}_E$ from $\bar{\mathfrak{P}} \ne \mathfrak{P}$. So $\mathfrak{P}$ is a Hecke prime (`isHeckePrime_iff`), and the second point law (totality) gives $z$.
3. **The constant.** `heckeTerm_generator_constant_via_frame` gives, for $a = e(C)$ and $n = n(\kappa_i)$: $t_0^{\,n}\, c(h)\mu(h)\, N(\mathfrak{P})^{-\lfloor k n_V/2\rfloor} = \mu_i(\mathfrak{P})^{-k}\, c(ha)\mu(ha)$.
4. **The weight.** `evR_frBor` says that a section of weight $\kappa_i$ changes by the character of the torus element under the move: $f(z) = \chi(t) f(y_{ha})$. Since $t_j = 1$ for $j \ne 0$, $\chi(t) = t_0^{\,n}$.

Then `phiW_unfold` writes $\varphi_f(ha) = \lambda c(ha)\mu(ha) f(y_{ha})$, and the identity is step 3 times $\lambda f(y_{ha})$ (`linear_combination`).

## In the Lean code

The theorem is in [HeckeReadingKernelsMatchCosetsThroughFrame.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadingKernelsMatchCosetsThroughFrame.lean#L41). Note that the module name belongs to the second name, and this file holds `heckeTerm`. The lemmas:

- `splitSup` and `phiW_unfold`, in the same file, lines 19 and 33.
- `heckeKernel_complex_point_matches_cosets`, a second name for `HeckeTermIdent.heckeKernelCoset` in [HeckeKernelComplexPointMatchesCosets.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeKernelComplexPointMatchesCosets.lean#L73).
- `heckeTerm_generator_constant_via_frame`, a second name for `HeckeGenConst.generator_constant` in [HeckeTermGeneratorConstantViaFrame.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeTermGeneratorConstantViaFrame.lean#L126).
- `FrameEval.evR_frBor` in [ChartCoverFOfSecBaseChange.lean](lean:Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/ChartCoverFOfSecBaseChange.lean#L148).

We have not unfolded the two large lemmas. `SplitLinearModel`, `VacFixed` and the frame pin are only passed to them. The point laws are a hypothesis here; the caller supplies the proved `HeckePointLaw.heckePointLaws`.
