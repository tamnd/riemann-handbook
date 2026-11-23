---
id: supp-bc-holds
title: Depth-zero components after base change, given inflation matching
kind: theorem
decl: UpperTheory.Gal.InertialTypesAlt.suppBC_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.RegularSemisimpleFibres.TypeOfLblHolds
covers: 1142
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem describes the local component of a cuspidal representation at a place of depth zero, after a chain of cyclic base changes unramified at that place. Its one hypothesis is a matching of orbital integrals for inflated functions. The [unconditional form](/entry/supp-bc-outright/) proves the hypothesis. The result goes to the [toral step](/entry/to-tor-holds/) and then to the Iwahori clause of the [Galois row](/proof/galois-row/).

## Statement

Let $E$ be a totally complex number field, $\Omega = \overline{E}$, and $\pi$ a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_E)$, $n \geq 1$. A *chain* from $(E, \pi)$ to $(K, \pi_K)$ is a finite sequence of steps $(K_i, \pi_i) \to (K_{i+1}, \pi_{i+1})$ in $\Omega$, with $K_{i+1}/K_i$ Galois of prime degree and $\pi_{i+1}$ a weak base change of $\pi_i$: at almost all places $w$ of $K_{i+1}$, if $B$ are suitable Satake parameters of $\pi_i$ below $w$, then $B^f$ are Satake parameters of $\pi_{i+1}$ at $w$, where $f$ is the residue degree.

**Hypothesis.** $\mathrm{InflMatching}$: let $K/k$ be an unramified extension of $p$-adic fields, and let $s \in \mathrm{Gal}(K/k)$ reduce to the Frobenius. Inflate a class function $f$ on $\mathrm{GL}_n(\mathbb{F})$ to $\mathrm{GL}_n(\mathcal{O}_k)$, and its norm lift to $\mathrm{GL}_n(\mathcal{O}_K)$. Then the twisted orbital integral of the second at $\delta$ equals the orbital integral of the first at $\gamma$ when the norm of $\delta$ is regular semisimple with the characteristic polynomial of $\gamma$. Each regular semisimple $\gamma$ with a nonzero orbital integral comes from a norm. We have not unfolded `twOrb`.

**Theorem.** Assume $\mathrm{InflMatching}$. Let $(K, \pi_K)$ be reached from $(E, \pi)$ by a chain. Let $A$ be a valuation ring of $\Omega$ over places $v$ of $E$ and $w$ of $K$, with $E_v \cong \mathbb{Q}_g$ and with $K$ fixed by the inertia group of $A$ over $E$. Let $\tau = \pi_v$ and $\tau' = \pi_{K,w}$. Suppose that $\tau$ has depth zero (a nonzero vector fixed by $K_1 = \ker(\mathrm{GL}_n(\mathcal{O}_v) \to \mathrm{GL}_n(\mathbb{F}_g))$), and that $N(w) = g^f$ with $f$ divisible by the size of each member of the cuspidal support of $\tau$. Then there are smooth characters $\xi_1, \dots, \xi_n$ of $K_w^\times$ such that:

1. each $\xi_j$ is tame, that is, trivial on $1 + \mathfrak{p}_w$;
2. the cuspidal support of $\tau'$ is $\{\xi_1, \dots, \xi_n\}$;
3. for each map $\mathrm{rec}$ to Weil-Deligne representations that obeys the local Langlands laws `LawsT`, each local Artin map $a$ at $w$ and each $t$ in the inertia group of $K$ at $A$, the characteristic polynomial of $t$ on $\mathrm{rec}(\tau)$ is $\prod_j (X - \xi_j(a(t)))$;
4. if $\tau$ is *mixed*, then no two of the $\xi_j$ satisfy $\xi_i = \xi_j |\cdot|$.

Here $\tau$ is mixed if it has depth zero and a cuspidal support with no such pair, whose members of size at least 2 are pairwise not `Inert` (not unfolded).

## Proof

1. `L.finTrace_of_matching` turns $\mathrm{InflMatching}$ into `FinTrace`: across one cyclic step, at a non-split unramified place, if a class function on $\mathrm{GL}_n(\mathbb{F}_v)$ has nonzero pairing with the trace of $\tau^{K_1}$, then its Shintani lift acts nonzero on $\tau'^{K_1}$.
2. `suppAny_of` proves clauses 1 to 3 from `FinTrace`, by induction along the chain on combinatorial labels (`Lbl`) of $\tau^{K_1}$.
3. `mixType_of` proves from `FinTrace` that for mixed $\tau$, a parahoric subgroup acts on a vector of $\tau'$ by a character built from distinct characters of $\mathbb{F}_w^\times$. `mixUnlinked` gets clause 4 from this by `TypesAndIwahori.unlinked_of_typeVec`, since $\tau'$ is generic.
4. `suppBC_of_mix` joins the two parts. This is logic only.

## In the Lean code

The theorem is in [TypeOfLblHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/TypeOfLblHolds.lean#L141). The proof:

```
suppBC_of_mix (suppAny_holds h) (mixUnlinked (mixType_holds h))
```

- `SuppBC`: [NumberField.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/NumberField.lean#L166).
- `suppBC_of_mix`: [SuppBCOfMix.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/SuppBCOfMix.lean#L43).
- `mixUnlinked`: [PMixUnlinked.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/PMixUnlinked.lean#L10).
- `InflMatching`: [IntersectionFamilySymmetric.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IntersectionFamilySymmetric.lean#L30), proved as `L.inflMatch` in [InflMatch.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/FrobeniusLocalPairs/InflMatch.lean#L38).

The hypothesis enters only through `finTrace_of_matching`, once in each half. Clause 3 holds for every map that obeys `LawsT`, not for one fixed local Langlands correspondence.
