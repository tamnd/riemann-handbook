---
title: Introduction
---
This volume gives the results of the other shared Lean folders that are large enough for an entry of their own: resolution of singularities, the automorphic kernels, the Siegel-Weil formula, the representation theory of GL and unitary groups, the twisted trace formula, the classical vanishing theorems, and the Weil bound. Most of them are published theorems that the code proves itself, with no open hypothesis. They hang from three steps and from two entries of [volume 8](/entry/weil-unitary/):

- [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), in [the literature layer](/proof/literature/). Resolution of singularities, the arithmetic Hilbert-Samuel chain, the Siegel-Weil formula in the Schrödinger model and the finiteness theorem of Harish-Chandra fill fields of its bundles.
- [EveryCharacter from Row0b](/step/every-character-of-row/), in [the trunk chapter](/proof/trunk/). It needs the de Rham cohomology of abelian schemes and the global Euler characteristic formula.
- [EveryCharacter from the Galois row](/step/every-character/), the last step of the proof. It needs the Leibniz rule for derivatives and the wave equation on GL_n(C).

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Representation theory of GL.** The Siegel-Weil formula in the Schrödinger model, the finiteness theorem of Harish-Chandra through constant terms, the Leibniz rule of Bernstein and Zelevinsky, Iwahori-Hecke eigenvalues at inert places, and the wave equation on GL_n(C).
- **Weil bound.** Tate's global Euler characteristic formula.
- **Block decomposition.** Grothendieck's existence theorem and the algebraization of coherent quotients, the multiplicity of a hyperplane section, Siegel sets for the adelic unitary group, and the twisted Jacquet functor on a mirabolic product.
- **Resolution of singularities.** Strong and functorial resolution in characteristic 0, from principalization, an affine rule and gluing.
- **Ideal principalization.** The canonical rules of the algorithm reduce inductively on the dimension, by maximal contact and order reduction.
- **Automorphic kernels.** The arithmetic Hilbert-Samuel chain with its five volume bounds and the formula on one block. Then the Hodge-de Rham facts for the first de Rham cohomology of an abelian scheme.
- **Automorphic spectrum.** Analytic matrix coefficients and dense Levi submodules, and the Siegel core for unitary groups.
- **Siegel-Weil.** Weil's formula for the pair (U(n,n), U(V)) when 2n is less than m, through the Fourier coefficients of singular index and an integral over frames.
- **Siegel-Weil proof.** The Siegel-Weil identity at the point s0 and the chain of inputs below it: the rank one measure identity, the theta mean as a product of local densities, and the Howe operators in the Fock model.
- **Hodge-Tate points.** Intersection numbers from a multigraded model, Kleiman's positivity on products of projective spaces, and Serre vanishing along the base direction.
- **Published theorems.** Kawamata-Viehweg and Nadel vanishing, vanishing in characteristic p for a lift modulo p squared, the global Euler characteristic formula, Poitou-Tate duality, the Casselman-Wallach globalization, de Rham Hecke characters, and the pole of the Rankin-Selberg L-function.
- **Metric proofs.** The arithmetic intersection numbers from Poincaré-Lelong and resolution, and the projection formula for heights.
- **Constant term finiteness.** Harish-Chandra's finiteness of automorphic forms on a unitary group, by induction on the flag of standard parabolics.
- **Discrete groups.** A local converse theorem for cuspidal representations of GL(n).
- **Archimedean base change.** The twisted trace formula on a pair of groups: its elliptic part, the vanishing of non-elliptic terms, the products of local twisted orbital integrals, and the Iwahori matching at inert places. Then the multiplicity formula for highest weights and the separation of automorphic subspaces.
- **Unitary dual proof.** Bernstein's theorem that a product of unitary representations of GL(n) over a local field is irreducible, from invariant distributions on matrices and vectors in characteristic zero and p.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Most chapters start with a chain of wrappers: a theorem with a long name that passes proved results to the next theorem, and a `Statement` file whose proof is one `first | exact` line. The entry for a wrapper is short and points to the entry with the content. Several of the "hypotheses" in these chains, for example `DivisorReductionHypotheses`, are proved outright elsewhere in the code. The entries say where.
