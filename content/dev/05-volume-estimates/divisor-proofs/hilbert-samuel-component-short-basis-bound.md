---
id: hilbert-samuel-component-short-basis-bound
title: The Hilbert-Samuel bound on a component with a short basis, second name
kind: theorem
decl: GlobalTheory.T.hilbertSamuel_component_short_basis_bound
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HilbertSamuelComponentShortBasisBoundStatement
covers: 747
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [hsClaimS_component_geo](/entry/hs-claim-s-component-geo/). Its only user is [hilbertSamuel_estimate_at_level](/entry/hilbert-samuel-estimate-at-level/), which calls it at line 69 of `ExistsDegreeParametersBound.lean`. Below this theorem are 747 declarations.

## Statement

**Theorem.** Assume the quoted theorems `Quoted`. Take a component $Z$ of the moduli space with its uniformizations $U$, weight parameters $P$, a choice $R$, ready data $h$, cusp frames $f_1$ and $f_2$, a section and constants $k$. Let $\Lambda_0$ be a real number such that the hermitian data `h.data f₁ f₂ th k` satisfies `GeoHyp` at $\Lambda_0$. Then `HSClaimS` holds with the constant $26$, the numbers $T = P.T$, $D$ the dimension of the flag variety, $n = f_1.n$ and $\Lambda = k.\Lambda_2$, and with these values read off the component:

- $\delta$ is the degree of $Z$ at the weight of $u_1$ (`compDeg`);
- $h$ is the height of $Z$ at that weight (`compHeight`);
- $d$ is the dimension of the cusp forms on $Z$ at the weight $P.\mathrm{wt}(T)$ (`cuspOn`);
- the last argument is the degree of their lattice (`degOn`).

The term `HSClaimS` is spelled out in [geoBound_of_quoted'](/entry/geo-bound-of-quoted-prime/).

## Proof

The proof is `exact hsClaimS_component_geo`, inside a `first | ...` that tries three forms of the same call.

## In the Lean code

The theorem is at [HilbertSamuelComponentShortBasisBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSamuelComponentShortBasisBoundStatement.lean#L17). The name says "short basis", but the statement does not build a short basis. The hypothesis `GeoHyp` already contains the short families at $0$, $D$ and $T$. The caller gets `GeoHyp` from `hermitian_geometric_hypothesis_holds`. The real step is in [hsClaimS_component_geo](/entry/hs-claim-s-component-geo/), and the bound itself is in [geoBound_of_quoted'](/entry/geo-bound-of-quoted-prime/).
