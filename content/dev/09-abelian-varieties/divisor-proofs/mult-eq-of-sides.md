---
id: mult-eq-of-sides
title: Equal cuspidal multiplicities from the two sides of the trace formula
kind: theorem
decl: GlobalTheory.PsCo.Pc.multEq_of_sides
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TraceEqXOfGeomExpansionX
covers: 418
status: drafted
drafted_by: writer@claude
---
This theorem does the comparison of the [entry on equal cuspidal multiplicities](/entry/unitary-theory-of-harish-chandra-langlands-alt/). That entry proves its result by one call to this theorem, and it states the nine inputs and the conclusion $\mathrm{MultEq}\,R$. We use its notation and do not repeat it. Here we unfold the two middle statements, $\mathrm{TraceEqX}$ and $\mathrm{TRCusp'}$, which that entry leaves closed. Below this theorem are 418 declarations.

## Statement

**Theorem.** Assume $\mathrm{LocalPC}$, rapid decay of cusp forms, Harish-Chandra finiteness, the Dixmier-Malliavin factorisation, the Green statement for cuspidal vectors, $\mathrm{SpecTraceX}$, $\mathrm{Separation}$, [$\mathrm{EllTraceX}$](/entry/elliptic-side-direct/) and $\mathrm{EllipticPartX}$. Then $\mathrm{MultEq}\,R$ holds for each real datum $R$ and face $F$ with $\mathrm{Given}\,R\,F$.

The proof goes through three statements.

- $\mathrm{GeomExpansionX}$: for test data $f = f_\infty \otimes f_f$ on $V$ (as in [the elliptic side](/entry/elliptic-side-direct/)), $R(f)$ has trace $\sum_P \mathrm{term}(V, \lambda, f_f, P)$, a finite sum over the torus classes $P$. Here the archimedean factor of each term depends only on $\lambda$.
- $\mathrm{TraceEqX}$: let $V'$ have the same rank as $V$, with local isometries $j_v \colon V_v \to V'_v$ at the finite places that carry the frame lattices to each other. Let $f_f'$ be the transfer of $f_f$ by $j$, and let $f'_\infty$ be a test function for parameters $\lambda$ on $V'$. Then $R_V(f)$ and $R_{V'}(f'_\infty \otimes f_f')$ have the same trace.
- $\mathrm{TRCusp'}$: in the same setting, let $\Phi \colon G_V^f \to G_{V'}^f$ be an isomorphism compatible with $j$. Then for each irreducible admissible $\sigma$ of type $T$, the multiplicity of $\sigma$ in the cuspidal discrete series part with archimedean parameter $M$ equals the multiplicity of $\sigma \circ \Phi^{-1}$ for $V'$ and $M'$.

## Proof

1. **Geometric expansion.** `geomExpansionX_of_parts` combines $\mathrm{EllTraceX}$ and $\mathrm{EllipticPartX}$ with `realStableX`. `realStableX` proves that at each real place the sum of the orbital integrals of $f_\infty$ over a torus class depends only on $\lambda$. For a compact torus it sums the conjugate [[discrete series|9AB7HYGPEK]] characters over the sign vectors and gets a Weyl character. For a noncompact torus the orbital integrals are $0$.
2. **Equal traces.** `traceEqX_of_geomExpansionX` moves the test data from $V$ to $V'$ along $j$ and expands both traces. The terms match, because the stable orbital integrals at finite places are preserved by lattice isometries (`stableOrbitalIntegral_preserved_latticeIsometry`).
3. **Equal multiplicities for a test type.** `trCusp'_of_steps` chooses an auxiliary split place and archimedean pseudo-coefficients from $\mathrm{LocalPC}$. Spectral finiteness (from rapid decay, Harish-Chandra and Dixmier-Malliavin) gives a finite family $\tau_i$ that covers both spectra. Put $a_i = m(\tau_i) - m'(\tau_i')$. $\mathrm{SpecTraceX}$ on both sides and $\mathrm{TraceEqX}$ give $\sum_i a_i \operatorname{tr} \tau_i(f_f) = 0$ for all finite test functions. Then $\mathrm{Separation}$ gives $a_i = 0$.
4. **The conclusion.** `multEq_of_trCusp'` finds a type vector with the Green statement, builds the local isometries and matches the parameters. It rewrites the cuspidal multiplicity as a discrete series multiplicity and applies step 3.

## In the Lean code

The theorem is in [TraceEqXOfGeomExpansionX.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceEqXOfGeomExpansionX.lean#L555). The statements are in the same file: `RealStableX` (line 207), `GeomExpansionX` (line 215), `TraceEqX` (line 229) and `TRCusp'` (line 353). The proof is

```
multEq_of_trCusp' rd hf dm gc (trCusp'_of_steps hL (GlobalTheory.T.cuspidal_spectrum_finiteness_of_decay_harishChandra rd hf dm) hS hSep (traceEqX_of_geomExpansionX (geomExpansionX_of_parts hE hP realStableX))) R F hG
```

All nine hypotheses are used. Rapid decay, Harish-Chandra finiteness and Dixmier-Malliavin are used twice: for spectral finiteness and in `multEq_of_trCusp'`.
