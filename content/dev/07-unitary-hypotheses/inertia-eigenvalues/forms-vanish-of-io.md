---
id: forms-vanish-of-io
title: Equivariant forms on the Fock space vanish if they vanish on the lowest types
kind: theorem
decl: GlobalTheory.GenByIo.forms_vanish_of_io
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.EquivariantBilinearFormsVanishOfIoGenerationReal
covers: 317
status: drafted
drafted_by: writer@claude
---
This theorem says that a family of equivariant bilinear forms on the polynomial Fock space is zero once it is zero on the vectors that come from the lowest types. It is stated again as [`equivariant_bilinearForms_vanish_of_io_generation_real`](/entry/equivariant-bilinear-forms-vanish-of-io-generation-real/). In [`gen`](/entry/gen/) each form is a downward [[theta|ZBGT50BW0Z]] integral.

## Statement

Let $R$ be a real datum (`RealDat D A Ks`) with a face $F$, let $i$ be a step of the chain and $t \in T$. Write $V$ and $W$ for the hermitian spaces `Vc D i` and `Wc D i`, and $G_\infty \subset U(V)(\mathbb A)$ for the elements with trivial finite component (`GinfC`). The objects are:

- $\mathcal P$, the polynomial ring over $\mathbb C$ in variables $x_{\tau,a,b}$, one for each archimedean index $\tau$, $a < \operatorname{rank} W$ and $b < \operatorname{rank} V$.
- $\omega$, the representation `R.ωP i t` of $U(V)(\mathbb A) \times U(W)(\mathbb A)$ on functions on the space `WO V W` of $\operatorname{rank} W \times \operatorname{rank} V$ matrices over the adeles $\mathbb A_E$. `R.FullP` says it is a Weil representation (`IsWeilFull`, not unfolded here).
- $P \mapsto \phi_P$, the linear map `R.ptP i t` from $\mathcal P$ to these functions. It applies $P$, read in the raising operators `aPlusAll`, to the vector `R.vP i t`.
- $(E, \rho)$, the coefficient space `R.cV i`: a finite-dimensional inner product space with a representation of $U(V)(\mathbb A)$.
- $\iota \colon L \to \operatorname{Hom}(E, \mathcal P)$, the field `R.ioP i`, where $L$ is the tensor product over $\tau$ of the lowest-type subspaces `lowT`.

Let $(B_j)_{j \in I}$ be bilinear forms $\mathcal P \times E^* \to \mathbb C$. Assume `Given R F`, `R.FullP`, and:

1. (equivariance) if $u \in G_\infty$ and $\phi_{P'} = \omega(u, 1)\phi_P$, then $B_j(P', \lambda) = B_j(P, \lambda \circ \rho(u))$ for all $j$ and $\lambda$;
2. (Lie stability) if $Y$ lies in the Lie algebra `lieAt` of $U(W)$ at $\tau$, that is $Y^* G_\tau + G_\tau Y = 0$ for the Gram matrix $G_\tau$, and $\phi_{P'}(z)$ is the derivative at $s = 0$ of $\omega(1, \exp(sY))\phi_P(z)$ for each $z$, then $B_j(P) = 0$ for all $j$ implies $B_j(P') = 0$ for all $j$;
3. (lowest types) $B_j(\iota(x)(e)) = 0$ for all $x \in L$, $e \in E$ and $j$.

**Theorem.** Then $B_j(P) = 0$ for all $P \in \mathcal P$ and all $j$.

## Proof

Let $U = \bigcap_j \ker B_j$. Hypothesis 1 makes $U$ stable under $G_\infty$, hypothesis 2 makes it stable under the Lie algebra of $U(W)$, and hypothesis 3 puts the image of $\iota$ in $U$.

1. `polynomial_mem_span_lifted_maps` (proved by `FockIsotypic.decomp`) writes $P = Q + (P - Q)$. Here $Q$ lies in the span of the vectors $\varphi(e)$, where $\varphi \colon E \to \mathcal P$ is linear and $G_\infty$-equivariant through $\phi$. And $P - Q$ lies in a finite-dimensional $G_\infty$-stable subspace on which every equivariant form vanishes.
2. `compactHoweDuality_isotypic_mem_of_stable_subspace` (proved by `HoweGen.cvType_mem_of_stable`) says that a subspace with the three properties of $U$ contains every $\varphi(e)$. So $Q \in U$. We have not opened its proof.
3. $B_j(P - Q) = 0$ by step 1 and $B_j(Q) = 0$, so $B_j(P) = 0$.

## In the Lean code

The theorem is in [EquivariantBilinearFormsVanishOfIoGenerationReal.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/EquivariantBilinearFormsVanishOfIoGenerationReal.lean#L21). The two lemmas are in [PolynomialMemSpanLiftedMapsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PolynomialMemSpanLiftedMapsStatement.lean#L18) and [CompactHoweDualityIsotypicMemOfStableSubspaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CompactHoweDualityIsotypicMemOfStableSubspaceStatement.lean#L18). The definitions are in [LinksDefs.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean#L516) (`RealDat`), [LinksChar.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LinksChar.lean#L87) (`ptP`) and [TiedSmooth.lean](lean:Formalism/LocalToGlobal/BesselHermitianTheta/TiedSmooth.lean#L19) (`lieAt`).

The hypotheses `Given R F` and `R.FullP` are only passed to the two lemmas. Hypothesis 2 is stated on the common kernel, not on each $B_j$.
