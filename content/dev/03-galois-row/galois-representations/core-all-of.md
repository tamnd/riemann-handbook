---
id: core-all-of
title: Galois representations for polarized cuspidal representations, from four inputs
kind: theorem
decl: UpperTheory.Gal.Int.coreAll_of
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.Development
covers: 1760
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem proves `CoreAll`: regular algebraic polarized cuspidal representations of $\mathrm{GL}_a$ over a CM field have Galois representations, with the right behaviour at spherical places. It is step 5 of the [Galois row chapter](/proof/galois-row/). Its result goes to `rest` in [the conditional row theorem](/proof/galois-row/). The proof is an assembly of four lemmas.

## Statement

**Theorem.** Assume `SeedFinOdd`, `CongFinOdd` and the theta lift statement [TLiftK](/step/tlift-k-def/). Then `CoreAll` holds.

`CoreAll` has two parts. Let $E$ be a CM field, $\ell$ a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ an isomorphism, $a \geq 1$, $\pi$ a cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb{A}_E)$ and $\chi$ a Hecke character of $E^+$. Suppose that $\pi$ is regular algebraic and that $(\pi, \chi)$ is a polarized pair: $\chi_v(-1) = (-1)^a$ at each real place $v$ of $E^+$, and $\pi$ satisfies `DualIsConjBy` for $\chi \circ N_{E/E^+}$ (not unfolded).

1. There is a continuous $r \colon G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ attached to $\pi$ through $\iota$.
2. For each such $r$ and each place $w$ where $\pi$ has Satake parameters $B$: if $w \nmid \ell$, then the Frobenius eigenvalues of $r$ at $w$ are the algebraic normalization of $B$; and if $w \mid \ell$, then $r$ is de Rham with the right Hodge-Tate jumps, crystalline, and its Weil-Deligne representation at $w$ has the characteristic polynomial of the unramified class built from $B$.

`SeedFinOdd` and `CongFinOdd` are the two halves of a limit argument on unitary groups in an odd number $a$ of variables. In outline: `SeedFinOdd` gives Galois representations for spaces $U'$ of automorphic functions with extra conditions at auxiliary places, and `CongFinOdd` approximates the Hecke eigenvalues of a given $U$ by those of such $U'$.

## Proof

1. `Lim.limFinOdd_of` proves `LimFinOdd` from `SeedFinOdd` and `CongFinOdd`. It gives, for each $U$, a semisimple $r$ with the Frobenius, crystalline and de Rham conditions and a joint approximation of its Frobenius traces above $\ell$.
2. `Int.Core.toCoreK` proves `Core` from `TLiftK`, `ClosedPhi`, `DescOffT` and `LimFinOdd`. `Core` is `CoreAll` for a smaller scope: $\sqrt{-d} \in E$ for some $d > 0$, $[E^+ : \mathbb{Q}]$ is even, the non-split places are prime to $\ell$, unramified over $E^+$ and spherical for $\pi$, $\chi$ is the $a$-th power of `quadChar E`, and only split places $w$ count. `TLiftK` enters through `TP.twoUpOK_of_k`.
3. `ClosedPhi` is `ClosedPhiFromClosedTrace.congPhi_holds`: if $r$, a set $C$ of crystalline representations with fixed Hodge-Tate jumps, and a sequence $S$ satisfy `JointApprox` (not unfolded) for the Frobenius power sums at a place above $\ell$, then the power sums of $r$ are $S$. `DescOffT` is `Desc.descOffT`: for each $\pi$ in the small scope and each finite set $Z$ of places, there are a set $T$ of non-split places disjoint from $Z$ and a space $U$ on the unitary group with `MatchOffT U π T` (not unfolded).
4. `Int.Inp.coreAll_of_core` widens `Core` to `CoreAll`. It goes from the small scope to the scope `good` (without the condition on $\chi$) by a twist, and from `good` to all $\pi$ by base change to a family of CM extensions (`QuadLift`). It uses eleven inputs in the structure `Inp`, supplied by `inp_holds`. By their names they are published results (Jacquet-Shalika, Gelfand-Kazhdan, Arthur-Clozel and others). We have not opened them.

## In the Lean code

The theorem is in [Development.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L20). The proof is one term:

```
coreAll_of_core (toCoreK up congPhi_holds descOffT (limFinOdd_of seed cong))
```

- `CoreAll`, `Core` and `SphericalLevelCondition`: [CyclicStrongAtCusp.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/CyclicStrongAtCusp.lean#L96). `Ex`, `InScope` and `Good`: [IsWeight.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/IsWeight.lean#L50).
- `SeedFinOdd`, `CongFinOdd` and `LimFinOdd`: [LimWU4OfLimWU3.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LimWU4OfLimWU3.lean#L103).
- `toCoreK`: [ToCoreK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/ToCoreK.lean#L7).
- `coreAll_of_core_inp`: [CoreAllOfRowStarCoreInp.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineInputs/CoreAllOfRowStarCoreInp.lean#L538).

The three hypotheses are used once each, so the theorem only passes them on. `SeedFinOdd` comes from `GeoOne` (see [the geometric realization](/entry/geometric-realization-of-weight-one/)) by `seedFinOdd_of_geoOne`, outside this subtree. The scope `all` is not all cuspidal $\pi$: it still asks that $\pi$ be regular algebraic and polarized.
