---
id: lang-rec-core-of-artin-reciprocity
title: Thirteen facts from Artin reciprocity, Tate duality and the Euler characteristic
kind: theorem
decl: GlobalTheory.langRecCore_of_artinReciprocity
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalDualityClassFieldFactsOfArtinTateEuler
covers: 381
status: drafted
drafted_by: writer@claude
---
This theorem builds the record `T2.Core`, thirteen facts of class field theory and Galois cohomology, from three published theorems. It is the proof of [its second name](/entry/local-duality-class-field-facts-of-artin-tate-euler/), which [the Selmer bound at a point](/entry/selmer-bound-at-point-main/) uses to get the instance `T2.Core`.

## Statement

The three hypotheses:

- `GlobalArtinReciprocity`: for each number field $E$ and algebraic closure $\Omega$, there is a homomorphism from the ideles of $E$ to $\mathrm{Gal}(\Omega/E)^{\mathrm{ab}}$ with the properties `IsGlobalArtin`. We have not unfolded `IsGlobalArtin`.
- `LocalTateDualityK`: for a finite extension $K$ of $\mathbb{Q}_\ell$, $r > 0$ and a finite continuous $\mathbb{Z}/\ell^r[G_K]$-module $M$, $H^2(G_K, \mu_{\ell^r}) \cong \mathbb{Z}/\ell^r$, and the cup products $H^i(M) \times H^{2-i}(M^\vee(1)) \to \mathbb{Z}/\ell^r$ are perfect for $i = 0, 1, 2$.
- `LocalEulerCharK`: in the same setting, $|H^1(M)| = |H^0(M)|\,|H^2(M)|\,|M|^{[K:\mathbb{Q}_\ell]}$.

The last two are Tate's local duality and Euler characteristic formula (Serre, *Galois Cohomology*, II.5.2 and II.5.7).

**Theorem.** These three imply `T2.Core`.

The thirteen fields of `T2.Core`, by group. Here $\mathcal{O}$ is a complete discrete valuation ring over $\mathbb{Z}_p$ with fraction field $F$, and $\varepsilon$ is a cyclotomic character of $G_K$ with values in $\mathcal{O}^\times$.

1. **Decomposition groups** (`dec`). A decomposition group of a number field at a place above $p$ is isomorphic to $G_K$ for some $K/\mathbb{Q}_p$ of the local degree, with inertia and cyclotomic characters matched.
2. **Local duality with $\mathcal{O}$ coefficients** (`inv`, `fin`, `rat`, `int`, `jspan`, `nat`). Compatible invariant maps $H^2(G_K, F/\mathcal{O}(\varepsilon)) \cong F/\mathcal{O}$ and $H^2(G_K, F(\varepsilon)) \cong F$. For dual lattices, $H^1$ is finitely generated, the cup product pairings are nondegenerate on one side, and each class in $H^1$ has a nonzero multiple that comes from the lattice. A natural form of the invariant map (`NatInv`, not unfolded).
3. **Shape of $H^1$** (`shape`, `shapeUnr`). For $M \cong F/\mathcal{O}$ with action $\varepsilon^{-e}$, $e > 0$, there is an injection $(F/\mathcal{O})^{[K:\mathbb{Q}_p]} \to H^1(G_K, M)$ with cyclic cokernel. The same holds for the trivial action modulo unramified classes.
4. **Unramified classes** (`unr`, `vhE`). A decomposition group has a continuous unramified homomorphism to $\mathbb{Z}_p$ that takes the value $1$. If $\ell \neq 2$ or $E$ has no real place, a submodule of $H^1(G_E, F/\mathcal{O})$ of classes unramified everywhere has length at most $\operatorname{length}(\mathcal{O}/\ell) \cdot v_\ell(h_E)$.
5. **Topology** (`top`, `elem`). Each such $\mathcal{O}$ has a $p$-adic topology, and seven elementary facts on topologies and cocycles hold.

## Proof

The proof fills each field with one lemma and adds nothing. Five lemmas use no hypothesis (`dec`, `jspan`, `unr`, `top`, `elem`). Five use Tate duality alone (`inv`, `fin`, `rat`, `int`, `nat`). The two shape lemmas use Tate duality and the Euler characteristic. Only `vhE`, the class number bound, uses Artin reciprocity.

## In the Lean code

The theorem is in [LocalDualityClassFieldFactsOfArtinTateEuler.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalDualityClassFieldFactsOfArtinTateEuler.lean#L21). `T2.Core` and its fields are in [LatDefs.lean](lean:ReciprocityTheory/ReductiveGroups/TraceFormulas/LatDefs.lean#L319). The hypotheses are in [LocalTateDualityK.lean](lean:Formalism/GaloisCohomology/LocalTateDualityK.lean#L47) and [ExistsUniqueHcharOfFiniteOrder.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean#L70).

Each of the thirteen lemmas renames a proof that we have not opened.

The Lean name `langRecCore` does not match the record that the theorem builds, `T2.Core`. The record holds class field theory and local duality only.
