---
id: cm-object-definite-lie-eigen-lattice-degree-difference
title: The degree difference of the two Lie eigenlattices of a definite CM object, second name
kind: theorem
decl: GlobalTheory.T.cmObject_definite_lieEigenLattice_degree_difference
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CmObjectDefiniteLieEigenLatticeDegreeDifferenceStatement
covers: 343
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [cmDiff_definite](/entry/cm-diff-definite/). Its user in the spine is [degLie_core_alt](/entry/deg-lie-core-alt/), which feeds it to `frameDeg_def` in its step 3. Below this theorem are 343 declarations.

## Statement

Let $E$ be a CM field with a host $H$: a prime $d$ with $d \equiv 7 \pmod{16}$, a root $\mathrm{rt}$ of $x^2 = -d$ in $\mathcal{O}_E$ and the complex conjugation $\bar{\ }$. Let $\chi$ be the Kronecker character of $-d$. Let $X$ be a CM object of signature $(p, q)$ over a number field $K$ (`CMObj`), with $\rho \in \mathcal{O}_K$ and $\rho^2 = -d$. Let $F$ be a generic fibre of the abelian scheme $B$ of $X$, and let $h$ be a hermitian family that comes from the complex uniformization of $F$ (`IsHerm`).

**Theorem.** Assume `IsHostField H` and $q = 0$. For each $\tau : \mathcal{O}_E \to \mathcal{O}_K$ with $\tau(\mathrm{rt}) = \rho$,
$$\deg_h L_\tau - \deg_h L_{\tau\circ\bar{\ }} = \frac{p - q}{2}\,\operatorname{Re}\log\Omega(E,\chi),$$
where $L_\tau$ is the lattice of Lie coordinates on which $\mathcal{O}_E$ acts through $\tau$ (`eigLat`). Here $\log\Omega(E,\chi) = \gamma + \log(2\pi/\mathrm{rd}(E)) - L'(1,\chi)/L(1,\chi)$, as in the parent entry.

## Proof

The proof is `exact cmDiff_definite`, inside a `first | ...` that tries three forms of the same call.

## In the Lean code

The theorem is at [CmObjectDefiniteLieEigenLatticeDegreeDifferenceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CmObjectDefiniteLieEigenLatticeDegreeDifferenceStatement.lean#L7). The hypothesis $q = 0$ makes the factor $(p - q)/2$ equal to $p/2$. The same factor $(p_i - q_i)/2$ appears in `FrameDeg`, as the parent entry records. The real content is in [cmDiff_definite](/entry/cm-diff-definite/).
