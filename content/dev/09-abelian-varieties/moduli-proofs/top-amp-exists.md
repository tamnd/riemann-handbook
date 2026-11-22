---
id: top-amp-exists
title: A projective model of full level with ample frames
kind: theorem
decl: GlobalTheory.Models.topAmpExists
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsFullLevelModelAmpleFrames
covers: 1047
status: drafted
drafted_by: writer@claude
---
This theorem builds, for each unitary PEL datum and auxiliary prime $n$, a projective model of level $n^J$ with ample theta frames. [`topAmpExists_of_semistableReduction`](/entry/top-amp-exists-of-semistable-reduction/) supplies its inputs. The result feeds [Part I](/entry/part-i-of-semistable-reduction/).

## Statement

**The data.** A `Host` $H$ for a CM field $E$ is a prime $d \equiv 7 \pmod{16}$ with $\sqrt{-d}$ and $w_0 = \tfrac{1 + \sqrt{-d}}{2}$ in $\mathcal{O}_E$, conjugation $a \mapsto \bar a$, a complex root $\rho_0$ of $-d$, and $E/E^+$ unramified. A `Datum` $D$ is a finite projective $\mathcal{O}_E$-module $\Lambda$ with a unimodular alternating form for which $a$ and $\bar a$ are adjoint, and a complex structure of signature $(p, q)$. A family $(X_l)$ gives smooth quasi-projective moduli spaces over $K_l = \mathbb{Q}(\rho_0, \zeta_A)$. An auxiliary prime is an odd prime $n$ with $-d$ not a square modulo $n$ and $n \nmid \operatorname{disc} E$. For $N = n^J$ let $R_N = \mathbb{Z}[\tfrac{1 + \rho_0}{2}, \tfrac1n, \zeta_N]$.

**Theorem.** Assume the ten inputs below. For $E$, $H$, $D$ with $p + q \ge 1$, $(X_l)$ and $n$, there are $J \ge 1$, $k \ge 0$ and a model $T$ of type `Top Xo n (n^J)` with ample frames of level $(n^k)^2$.

The parts of $T$:

- A normal scheme $Z$, projective and flat over $R_N$.
- A semi-abelian scheme $G \to Z$ with an $\mathcal{O}_E$-action and a symmetric cubical line bundle $L$.
- An open abelian locus that holds all generic points.
- For each level $l$ with $A = N$, a map $X_l \to Z$, finite onto the abelian locus over $K_l$.
- A full-level family $\mathcal{M}$ over $R_N$ with level sections $\Lambda \to G_{\mathcal{M}}$.
- A finite map from the abelian locus to $\mathcal{M}$, an isomorphism near the generic fibre.
- For each prime $p \neq n$, a finite unramified map to a Siegel family of level $N$.

Ample frames (`AmpFrames G L m`) are an ample line bundle $\mathcal{A}$ on $Z$ with, on each trivializing open set, a theta section $\theta_i$ of $L$ and a frame $b_i$ of sections of $L^m$. On overlaps $\theta_i = c\,\theta_j$ and $b_i = g\, b_j$, and $\mathcal{A}$ has transition function $c^\alpha \det(g)^\beta$. Over traits into the abelian locus, $\theta_i$ and $b_i$ are bases.

## The ten inputs

1. `HomExtSt`: homomorphisms of semi-abelian schemes extend from the generic fibre over a discrete valuation ring.
2. `Out.Laws`: 24 statements on abelian schemes, by their names on sections, ampleness, rigidity and the Weil pairing. Not unfolded.
3. `Out.Laws2`: four statements `SecBaseChangeAnySt`, `SecTwistSt`, `CharPairSt`, `SmoothDenseSt`. Not unfolded.
4. `SemistableReductionSt`: the semistable reduction theorem.
5. `ThmUSt`: a semi-abelian model with split special fibre gives a uniformization.
6. `UTorsSt`: torsion points correspond to the points `QkPt` of the degeneration data, with the Weil pairing.
7. `ZHGeoSt`: a statement on theta systems over rational models. Not unfolded.
8. Theta objects with integral theta values have good reduction after an extension.
9. The theorem of the cube: $\Theta(M)$ has a nowhere vanishing section.
10. `ThetaUnifAV`: complex theta uniformization with Appell-Humbert data (Mumford, *Abelian Varieties*, §2).

## Proof

Choose a symplectic basis of $\Lambda$ and ring generators of $\mathcal{O}_E$. The lemmas fall in three groups.

- **The family.** `T.exists_thetaFamily_pel_smooth_generic_fibre` (inputs 2, 3, 8, 9, 10) gives a theta family over $R_{n^{2j}}$ with a PEL semi-abelian scheme, smooth over the generic fibre. `T.exists_universal_fullLevel_of_pelThetaFamily` (inputs 2, 3) adds full-level sections.
- **The model with frames.** `T.nonempty_ampleFramedModel_PELThetaFamily` (inputs 2 to 7) gives $k$ and a normal projective model `ZOn` with ample frames of level $(n^k)^2$.
- **The Siegel comparison.** `T.exists_universal_quasiProjective_siegelFamily_large_level` (inputs 2, 3, 9, 10) gives Siegel families, and `T.cmFamily_finite_unramified_over_siegelFamily` (inputs 1 to 3) maps to them.

Take $j$ above the bounds of the lemmas. `exists_tBase_RZ` and `arBase_RZ` check the conditions on $R_N$. Last, `T.exists_fullLevel_model_of_family_birationalModel` (inputs 1 to 3) assembles $T$. The output is $J = 2j$ and $k$.

## In the Lean code

The theorem is in [ExistsFullLevelModelAmpleFrames.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFullLevelModelAmpleFrames.lean#L180), `TopAmpExists` in [TopAmpExists.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/TopAmpExists.lean#L89), `Top` in [AuxiliaryInertOddPrime.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/AuxiliaryInertOddPrime.lean#L95), and `AmpFrames` in [AdmissiblePadicIntMaximalIdeal.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/AdmissiblePadicIntMaximalIdeal.lean#L65).

The six lemmas are `first | exact ...` wrappers whose targets we have not opened. Input 4 is used only for the model with frames.
