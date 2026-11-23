---
title: Introduction
---
This volume gives the results of the ground theory that are large enough for an entry of their own. The ground theory is the Lean code on global and local fields, automorphic forms, heights and theta, profinite cohomology, reductive groups and the companion theories. Only six of its declarations own 1,000 others or more. They hang from two steps and from one entry of [volume 10](/entry/theorem-hsmblock/):

- [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), in [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). It needs the weighted bound on Bessel wave grids, which is Theorem B in the code. The step does not name this branch; the bound reaches it through `analytic_pinnedTheoremB_uniform`.
- [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), in [the literature layer](/proof/literature/). It needs the classification of the discrete series of U(p,q).

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Bessel wave grids.** A uniform bound for a weighted sum of local orbital integrals of discrete series coefficients over admissible global points. Then the links below it: the hypotheses `HypsG`, the threshold of Zuckerman tensoring, and the assembly from the wave bound at Bessel periods.
- **Automorphic theory.** Uniqueness of Bessel maps for discrete series with large gaps, the real-place integral bound that it gives, and the domination of the cut-off top-degree integrand.
- **Discrete series.** Theorem M: the local Bessel integral of a discrete series has rank one. It rests on a majorant for matrix coefficient integrals, built from the Heisenberg inputs.
- **Heights and theta.** The arithmetic Hilbert-Samuel formula on one block, from 19 inputs that its caller proves.
- **Class field theory.** Local reciprocity for local fields of characteristic zero, from an Artin map for each finite extension of the p-adic numbers.
- **Discrete series classification.** Every irreducible square-integrable representation of U(p,q) is a discrete series, through fast decay on lines and an L² embedding.
- **Real groups.** The Cartan decomposition for p-adic unitary groups, and small compact open subgroups whose Hecke algebras satisfy a polynomial identity.
- **Reductive groups.** Chart values of harmonic polynomials lie in a power of an ideal.
- **L2 estimates for d-bar.** Hörmander's weighted L2 estimate on étale Stein spaces.
- **Poitou-Tate duality.** The Poitou-Tate package for the Galois group unramified outside S, with real places, and restriction to the real places in degrees three and up.
- **Profinite cohomology.** The pairing of H^1 with compactly supported H^2 for prime-power roots of unity, by class field theory and Kummer theory.
- **Scheme cohomology.** Finiteness of coherent cohomology on a proper scheme over a noetherian ring, by noetherian induction on the support.
- **Spectral geometry.** The mean number of rational vectors in an adelic box, and a polynomial bound for the theta measure of a box.
- **Automorphic forms.** Uniqueness of Whittaker functionals for GL(n) over a p-adic field.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Each top theorem in this volume holds with no hypothesis. The links below it take the inputs as hypotheses and pass them along. The real analysis is often in lemmas that are too small for an entry of this tier. The entries name those lemmas.
