---
id: normalized-ring-data
title: A ring datum with a real display for a normalized family
kind: theorem
decl: Formalism.MainNotions.N.K.normalized_ring_data
module: Formalism.AdmissibleDesigns.NormalizedRingData
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem builds one ring datum `Dd` for a family that is normalized at $\pi$, and proves the display bound `RealDisplayAllK` for it, with the length of $\mathcal{O}/cc_\pi$ on the left side. [`theorem_n5_of_ring_inputs`](/entry/theorem-n5-of-ring-inputs/) applies it to $r^{\mathrm{N}}$. The theorem joins three results that are proved elsewhere: `ring_objects_exist`, `displayFree` and `realDisplayAllK_of`.

## Statement

Use the notation of [the parent entry](/entry/theorem-n5-of-ring-inputs/), with a family $r$ in place of $r^{\mathrm{N}}$. Let $T$ be the subalgebra of functions $X \to \mathcal{O}$, $Z$ the set of the datum, and $cc_\pi$ the image at $\pi$ of the ideal of functions in $T$ that vanish off $Z$ (`ccAt`).

**Theorem.** Assume:

- `NormAt`: $r_\pi$ is block diagonal, with $\rho_\pi$ in the top block and the characters $\chi_1, \dots, \chi_t$ (`chiU`) on the diagonal below;
- the coefficients of the characteristic polynomial of $r_x(\gamma)$ lie in $T$ as functions of $x$;
- the residual images of $\rho_\pi$ span all $r \times r$ matrices over the residue field;
- `IdemHyp` for $e_B, e_1$ and `DistinctEigenvalueCornerPerturbation` for $g_0, e_B, s$.

Then there is a ring datum `Dd` with `RingDef`, with $v_{cc}(p(\pi')) = \operatorname{length}(\mathcal{O}/cc_\pi)$, with five module instances, with the topology `Dd.Top`, and with `RealDisplayAllK` for $\operatorname{length}(\mathcal{O}/cc_\pi)$ under any compatible topologies.

`RingDef` says that `Dd` adjoins to $T$ the eigenvalues $rr_i$ of $e_B r(g_0) e_B + s$ on a cover $X' \to X$, with a point $\pi'$ over $\pi$ where $rr_i(\pi') = \chi_1(g_0)\varepsilon(g_0)^{-i}$.

## Proof

1. **The ring datum.** `primHyp_of` turns `NormAt` and the characteristic polynomial condition into `PrimHyp`. `absIrr_of_res` turns the spanning condition into `AbsIrr` for the top residual block. This is the easy direction: only $0$ and the whole space are stable under all matrices, and only scalars commute with all matrices. Then `ring_objects_exist` gives `Dd`, `RingDef`, the instances and `Dd.Top`.
2. **Freeness.** `displayFree` gives `LocalToDisplayFree`, which we did not unfold.
3. **The length.** `RingDef` gives $p(\pi') = \pi$. Then `Br.length_ccAt` gives $v_{cc}(\pi) = \operatorname{length}(\mathcal{O}/cc_\pi)$.
4. **The display.** `realDisplayAllK_of` takes `Dd.Top`, the freeness, the product formula $\delta_{\mathcal{O}} = \prod_{0<i<t} (u_1 - u_1\varepsilon(g_0)^{-i})$ with $u_1 = \chi_1(g_0)$ (`SF.deltaO_eq`) and step 3.

## In the Lean code

The theorem is in [NormalizedRingData.lean](lean:Formalism/AdmissibleDesigns/NormalizedRingData.lean#L20). `RingData` and `RingDef` are in [DistinctEigenvalueCornerPerturbation.lean](lean:Formalism/WachLatticeTwists/RamifiedBlockRings/DistinctEigenvalueCornerPerturbation.lean#L12), and `RealDisplayAllK` is in [RealDisplayAllK.lean](lean:Formalism/AdmissibleDesigns/RealDisplayAllK.lean#L20). The file has the section variable `Fact T2.Core`.

The proof discards the `SMulCommClass` part of the instance bundle from `ring_objects_exist` (line 43) and uses a second copy of that instance from the same result. This has no effect on the statement.
