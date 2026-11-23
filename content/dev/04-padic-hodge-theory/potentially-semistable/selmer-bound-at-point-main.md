---
id: selmer-bound-at-point-main
title: A congruence length is bounded by a Selmer length and local terms
kind: theorem
decl: GlobalTheory.SelmerBoundAtPoint.main
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.SelmerLengthBoundAtPoint
covers: 2222
status: drafted
drafted_by: writer@claude
---
This theorem bounds the congruence length of a point of a Hecke algebra by a Selmer length and local terms above $\ell$. It is the content of [`globalLatticeIndexTheorem_of_lengthBoundAtPlaces`](/entry/global-lattice-index-theorem-of-length-bound-at-places/), below the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). It supplies two instances to [`theorem_n5_from_inputs`](/entry/theorem-n5-from-inputs/), which does the work.

## Statement

A datum $D$ of type `D7` and a local index $i$ give a prime $\ell$, a complete discrete valuation ring $\mathcal{O}$ finite over $\mathbb{Z}_\ell$ with fraction field $K$, a finite set $X$, a local subalgebra $\mathbb{T} \subset \mathcal{O}^X$, a subset $Z \subset X$, finite sets $S$, $Q$ of places of $E$, and characters $\chi_c$ of $G_E$. Let $r_x$ (rank $n_V$) and $\rho_x$ (rank $r$) be families of representations of $G_E$ over $\mathcal{O}$, let $\pi \in X$, and let $(\mathrm{row}, \mathrm{col})$ be a partition of the places above $\ell$.

Let $\eta_\pi \subset \mathcal{O}$ be the values at $\pi$ of the functions in $\mathbb{T}$ that vanish off $Z$. Put $\lambda(M) = \operatorname{length} M / \operatorname{length}(\mathcal{O}/\ell)$ and $v_{cc}(\pi) = \lambda(\mathcal{O}/\eta_\pi)$.

The hypotheses:

- Global Artin reciprocity, local Tate duality, and Tate's local Euler characteristic formula (Serre, *Galois Cohomology*, II.5).
- `admG1`: the characteristic polynomial coefficients of the $r_x$ lie in $\mathbb{T}$.
- `admG3`: residually, $r_x$ has the characteristic polynomial of $\rho_\pi$ times that of the $\bar\chi_c$, $c \le t$.
- `admG4`, `FamilyContinuous`: each $r_x$ is continuous and unramified outside $\ell$, $S$, $Q$.
- `admG5`, `TameGeneratorConditions`: inertia at $S \cup Q$ is tame of a fixed shape.
- `admG6`: if $r_x \otimes K$ has a $\chi_1$-eigenvector, then $x \in Z$.
- `SemisimpleDecomposition`: $r_\pi \otimes K \cong \rho_\pi \oplus \chi_1 \oplus \dots \oplus \chi_t$.
- `admG2`, `admBK`, `BlochKatoAnnihilators`, `FontaineAtPlacesOverL`: crystalline and Bloch-Kato conditions above $\ell$.
- `tateH1FinitenessAtPlacesOver`, `LocalCoefficientCompatibility`: local $H^1$ is finite, and the local coefficient maps agree.
- `UnramifiedTrivialH1f`: the unramified part of $H^1_f$ is trivial at the column places.
- `LengthBoundAtPlaces`: at row places, lattice maps onto $T_2$ satisfy `ColLe` with $\mathrm{len}_{\mathrm{row}}(w)$.
- `LiftExponentAtPlaces`, `admTB`: the conditions `LiftAt` with exponent $e'(w)$ at column places, and `TBAt` with a constant $c_B$.

We have not unfolded `GainBoundAt`, `bkBAt`, `ColLe`, `LiftF`, `TBAt` and `adm51`.

The conclusion `GlobalLatticeIndexTheorem`: if $\ell$ differs from two fixed primes of the datum, $\pi \in Z$, and $\mathrm{Sel}_\pi$ and the groups $\text{Ш}(e)$, $0 < e < t$, have finite length, then

$$\begin{aligned} v_{cc}(\pi) \le{}& \sum_{w \in \mathrm{row} \cup \mathrm{col}} \mathrm{len}_w + \lambda(\mathrm{Sel}_\pi) + \sum_{0<e<t} \text{Ш}(e) + v_\ell(h_E) \\ &+ t \sum_{w \in \mathrm{row}} (d_w + 2)\, c_B + 4 n_V (|\mathrm{col}| + 1)\, \delta \\ &+ t\, |\mathrm{col}|\, h_0 + t \sum_{v \in Q} \lambda\bigl(\mathcal{O}/(\zeta_v - 1)\bigr).\end{aligned}$$

Here $\mathrm{Sel}_\pi \subset H^1(G_E, W_\pi \otimes K/\mathcal{O})$ has Bloch-Kato type local conditions, with $W_\pi = \rho_\pi \otimes \chi_1^{-1}$. At column places $\mathrm{len}_w = e'_w + j_w(e'_w + \delta) + 2\delta + h_{0,w}$. Also $\delta = \sum_{0<k<t} (s_0 + v_\ell(k))$, $d_w$ is the local degree, $h_0$ and $h_{0,w}$ are lengths of local invariants, and $\zeta_v = \chi_1(\gamma_v)$ for a tame generator $\gamma_v$.

## Proof

1. `local_duality_class_field_facts_of_artin_tate_euler` turns the published inputs into the instance `T2.Core`, thirteen facts of class field theory and Galois cohomology.
2. `finCore` gives the instance `FinCore`: local invariants of $W_\pi \otimes K/\mathcal{O}$ and of $K/\mathcal{O}(e)$, $e > 0$, have finite length.
3. `unramified_input_of_admitted` puts `UnramifiedTrivialH1f` in the form `UnrIn`.
4. `theorem_n5_from_inputs` takes the other hypotheses unchanged and gives the bound.

## In the Lean code

The theorem is in [SelmerLengthBoundAtPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SelmerLengthBoundAtPoint.lean#L23), with `finCore` at [line 16](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SelmerLengthBoundAtPoint.lean#L16). The conclusion is in [DecompositionData.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DecompositionData.lean#L323), $v_{cc}$ in [DataN.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L224), and `theorem_n5_from_inputs` in [StatementOneBFromUnramified.lean](lean:Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean#L142).

$\lambda$ uses `Module.length (...).toNat`, so infinite length gives $\lambda = 0$. That is why the conclusion assumes finite length. We have not checked that the conditions on `D7` can all hold at once.
