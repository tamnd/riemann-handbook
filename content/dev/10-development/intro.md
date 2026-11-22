---
title: Introduction
---
This volume gives the results of the other shared Lean folders that are large enough for an entry of their own: resolution of singularities, the automorphic kernels, the Siegel-Weil formula, the representation theory of GL and unitary groups, and the Weil bound. Most of them are published theorems that the code proves itself, with no open hypothesis. They hang from three steps and from two entries of [volume 8](/entry/weil-unitary/):

- [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), in [the literature layer](/proof/literature/). Resolution of singularities, the arithmetic Hilbert-Samuel chain, the Siegel-Weil formula in the Schrödinger model and the finiteness theorem of Harish-Chandra fill fields of its bundles.
- [EveryCharacter from Row0b](/step/every-character-of-row/), in [the trunk chapter](/proof/trunk/). It needs the de Rham cohomology of abelian schemes and the global Euler characteristic formula.
- [EveryCharacter from the Galois row](/step/every-character/), the last step of the proof. It needs the Leibniz rule for derivatives and the wave equation on GL_n(C).

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Resolution of singularities.** Strong and functorial resolution in characteristic 0, from principalization, an affine rule and gluing.
- **Ideal principalization.** The canonical rules of the algorithm reduce inductively on the dimension, by maximal contact and order reduction.
- **Automorphic kernels.** The arithmetic Hilbert-Samuel chain with its five volume bounds and the formula on one block. Then the Hodge-de Rham facts for the first de Rham cohomology of an abelian scheme.
- **Siegel-Weil.** Weil's formula for the pair (U(n,n), U(V)) when 2n is less than m, through the Fourier coefficients of singular index and an integral over frames.
- **Representation theory of GL.** The Siegel-Weil formula in the Schrödinger model, the finiteness theorem of Harish-Chandra through constant terms, the Leibniz rule of Bernstein and Zelevinsky, Iwahori-Hecke eigenvalues at inert places, and the wave equation on GL_n(C).
- **Weil bound.** Tate's global Euler characteristic formula.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Most chapters start with a chain of wrappers: a theorem with a long name that passes proved results to the next theorem, and a `Statement` file whose proof is one `first | exact` line. The entry for a wrapper is short and points to the entry with the content. Several of the "hypotheses" in these chains, for example `DivisorReductionHypotheses`, are proved outright elsewhere in the code. The entries say where.
