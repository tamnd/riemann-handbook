---
id: extreme-u
title: An embedding into a principal series with ordered parameters, for a quasi-split unitary group
kind: theorem
decl: PositivityTheory.SphericalProduct.extremeU
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.IwahoriFactorisation.StrictDominance.UnitaryExtremality.ExtremeU
covers: 684
status: drafted
drafted_by: writer@claude
---
This theorem embeds an irreducible unramified representation of a quasi-split unitary group into a principal series. It also puts the parameters of that principal series in a fixed order: absolute values decrease and are at least 1. It is step 1 of the proof of [`absEig`](/entry/abs-eig/), which turns the embedding into an Iwahori eigenvector. The proof here only chains eight statement lemmas, each a separate theorem of `GlobalTheory.T`.

## Statement

We use the notation of [`absEig`](/entry/abs-eig/): $L$, $\sigma$, $\varpi$, $q$ with `IsUnramInv`, the group $G$, its subgroup $K$, $m = \lfloor n/2 \rfloor$ and the character $\chi_\beta$ of diagonal elements. For $\beta \in (\mathbb{C}^\times)^m$ let $I(\beta)$ be the space of functions $\varphi \colon G \to \mathbb{C}$ with $\varphi(bg) = \chi_\beta(b)\varphi(g)$ for each upper triangular $b \in G$, with $G$ acting by right translation (`psSpaceU`, `psFunU`). See [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

**Theorem** (`ExtremeU`). Let $\rho$ be an irreducible admissible representation of $G$ on $V$, spherical for $K$ with Satake parameters $\alpha$ (`HasSatU`). Then there is $\beta \in (\mathbb{C}^\times)^m$ such that $\beta$ comes from $\alpha$ by a permutation and the inversion of some entries (`WeylConjU`), $|\beta_1| \ge \dots \ge |\beta_m| \ge 1$, and there is an injective $G$-map $f \colon V \to I(\beta)$.

## Proof

Let $J_N(V)$ be the span of the vectors $\rho(u)v - v$ for upper unipotent $u$ (`jacU`). The proof applies one lemma in each step.

1. `unitary_jacquet_nonzero` (`JacNeU`): some $y \notin J_N(V)$ is fixed modulo $J_N(V)$ by the diagonal elements of $K$.
2. `unitary_jacquet_eigenvector_exists` (`EigU`): some $y' \notin J_N(V)$ and some function $\xi$ give $\rho(t)y' - \xi(t)y' \in J_N(V)$ for each diagonal $t$, with $\xi = 1$ on the diagonal part of $K$.
3. `unitary_equivariant_form` (`EqFormU`): a nonzero linear form $\lambda$ vanishes on $J_N(V)$, and $\lambda(\rho(t)v) = \xi(t)\lambda(v)$ for diagonal $t$.
4. `unitary_character_facts` (`CharU`): $\xi = \chi_\beta$ on diagonal elements for some $\beta$.
5. `unitary_frobenius_reciprocity` (`FrobU`): from $\lambda$, $\beta$ is a Weyl conjugate of $\alpha$, and there is an injective $G$-map $V \to I(\beta)$.
6. `unitary_chamber_decomposition` (`ChamberU`) puts $\beta$ in order. It takes two step lemmas as hypotheses. `unitary_swap_reduction` (`SwapStepU`) swaps $\beta_i$ and $\beta_{i+1}$ when $|\beta_i / \beta_{i+1}| < 1$. `unitary_inverse_reduction` (`InvStepU`) inverts $\beta_m$ when $|\beta_m| < 1$. Each move keeps an injective $G$-map into the new principal series.

## In the Lean code

The theorem is in [ExtremeU.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/UnitaryExtremality/ExtremeU.lean#L22). The statement `ExtremeU` is in [IsStrictDom.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/UnitaryExtremality/IsStrictDom.lean#L45). The step statements, from `JacNeU` to `ChamberU`, are in [SatPowNonvan.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/UnitaryExtremality/SatPowNonvan.lean#L37). Each lemma is proved in a statement file in `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`; we have not unfolded those proofs.

The statement of step 2 is written out in full in its statement file, and it is the same as `EigU`. The file `SatPowNonvan.lean` is named after its definition `SatPowNonvan`, which this proof does not use.
