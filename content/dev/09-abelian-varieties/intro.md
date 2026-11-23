---
title: Introduction
---
This volume gives the shared results of the Lean folder `AbelianVarietyTheory` that are large enough for an entry of their own. Most of them are published theorems that the code proves itself: toroidal compactifications, the arithmetic Hilbert-Samuel formula, pseudo-coefficients, the Jacquet-Rallis fundamental lemma, p-adic monodromy and semistable reduction. They hang from the steps [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), [EveryCharacter from the Galois row](/step/every-character/) and [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), or from entries of [volume 8](/entry/siegel-toroidal-integral-of-literature/).

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Twisted operators.** Good grid frames for the ascent of Bessel periods, under the condition `DepFixed`.
- **Divisor proofs.** The largest chapter. Pseudo-coefficients for discrete series of U(p,q). The arithmetic Hilbert-Samuel formula from principalisation, and Chern-Weil theory for good metrics. The toroidal model of a unitary Shimura variety for a fan: the normalized blowup, the separation of boundary points, charts and rigid charts, and the log Kodaira-Spencer isomorphism. The toroidal compactification of Siegel spaces and its charts. Mumford's semi-abelian uniformisation over complete normal bases. Then `JoinOut`, the Weil representation of split U(n,n), window matrices for p-divisible groups, and the dual abelian scheme.
- **Flag measures.** The type bound for pairs of terms, from the amplitude bound and a count of pairs by Siegel mass formulas.
- **Jet harmonics.** A pointwise bound for matrix coefficients of discrete series, from a bound for Capelli eigenfunctions.
- **Inertia eigenvalues.** A bound for the congruence length of a Hecke point by a Selmer length. The theorem that de Rham representations are potentially semistable, through a matrix form of the p-adic monodromy theorem. The Jacquet-Rallis fundamental lemma for unit functions, by induction on the rank.
- **Moduli proofs** and **degeneration proofs.** Integral models of full level with ample theta frames, and the extension of an abelian scheme with theta structure to a semi-abelian scheme, both from semistable reduction. The Kodaira-Spencer bound on the tangent space of a PEL family, arc families with theta frames, and a group model over a strictly Henselian base.
- **Siegel theta transformation.** Bounded forms of a theta system are sums of hermitian theta series. The Siegel-Weil formula for definite hermitian lattices, by induction on the degree.
- **Cusp form evaluations** and **rings of integers.** Analytic charts at complex points, and bounds for sums of harmonic values over the kernel of an isogeny.
- **Height proofs.** Limits of discrete series coefficients are coefficient series, through K-type projections.
- **Proofs.** Mixed results that the chapters above call: degeneration data and holomorphic arcs, the key invariant of a principally polarized abelian variety and lower bounds for theta sections, the unramified Howe statement, and the inputs of the CM theta norm bound.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Most chapters here alternate between a second name in a `Statement` file and the theorem with the content. The entry for the second name is short and points to the other one. Several hypotheses of these chains, for example `SemistableReductionSt` and `Principalisation`, are also proved outright elsewhere in the code. The entries say where.
