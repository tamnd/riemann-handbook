---
title: Introduction
---
This volume gives the results of the ground theory that are large enough for an entry of their own. The ground theory is the Lean code on global and local fields, automorphic forms, heights and theta, profinite cohomology, reductive groups and the companion theories. Only six of its declarations own 1,000 others or more. They hang from two steps and from one entry of [volume 10](/entry/theorem-hsmblock/):

- [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), in [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). It needs the weighted bound on Bessel wave grids, which is Theorem B in the code. The step does not name this branch; the bound reaches it through `analytic_pinnedTheoremB_uniform`.
- [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), in [the literature layer](/proof/literature/). It needs the classification of the discrete series of U(p,q).

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Bessel wave grids.** A uniform bound for a weighted sum of local orbital integrals of discrete series coefficients over admissible global points. Then the three links below it: the hypotheses `HypsG`, the threshold of Zuckerman tensoring, and the assembly from the wave bound at Bessel periods.
- **Heights and theta.** The arithmetic Hilbert-Samuel formula on one block, from 19 inputs that its caller proves.
- **Real groups.** Every irreducible square-integrable representation of U(p,q) has a Harish-Chandra parameter and is determined by its lowest K-type.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Each top theorem in this volume holds with no hypothesis. The links below it take the inputs as hypotheses and pass them along. The real analysis is often in lemmas that are too small for an entry of this tier. The entries name those lemmas.
