---
id: ram-sph
title: Base change keeps Satake parameters at ramified places
kind: theorem
decl: UpperTheory.ConvolutionTheory.Sph.ramSph
module: Development.AutomorphicArithmetic.Foundations.Convolution.SphericalIdeles.QuadLift
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem says that a weak base change lift of a cuspidal representation keeps its Satake parameters at a place where the extension ramifies. Two proofs use it: `quadLift`, in the same file, which builds the lift for quadratic extensions, and `strongTC_holds`, which proves the statement `ArthurClozelStrongTC`. Both lie below [EveryCharacter from the Galois row](/step/every-character/). The term only applies `ramSphOf` to three local lemmas; the argument is in `ramSphOf`.

## Statement

Let $M/K$ be a Galois extension of totally complex number fields of prime degree, and $n \geq 1$. Let $\pi$ and $\Pi$ be cuspidal automorphic representations of $\mathrm{GL}_n$ over $K$ and $M$. Suppose that $\Pi$ is a *weak base change* of $\pi$: at almost all finite places $w$ of $M$, with $v$ below $w$ and $N(w) = N(v)^f$, there is a multiset $B$ of Satake parameters of $\pi$ at $v$ such that $\{b^f : b \in B\}$ are Satake parameters of $\Pi$ at $w$.

**Theorem.** Let $w$ be a finite place of $M$ that is ramified over $K$, and $v$ the place below it. If $\pi$ has Satake parameters $B$ at $v$, then $\Pi$ has Satake parameters $B$ at $w$.

Since the degree is prime, $w$ is totally ramified (`normRam`), so $f = 1$ and $B$ is not raised to a power.

## Proof

The proof is `ramSphOf`, from two hypotheses: `LocGal` (a generator $\sigma_w$ of the local Galois group and a norm map $N \colon M_w^\times \to K_v^\times$) and `LiftGood`. `LiftGood` says: if $\pi_v$ is a subquotient of the principal series of $(\omega_1, \dots, \omega_n)$, then $\Pi_w$ is a subquotient of the principal series of $(\omega_1 \circ N, \dots, \omega_n \circ N)$. `liftGood` proves it from `CoreId`, an identity of twisted traces on Jacquet modules, and `coreId` proves that from `varEx`, `varTrace` and `elemPairJ_holds`. We have not unfolded these three.

The steps of `ramSphOf`:

1. `normRam` gives $N(w) = N(v)$. A private lemma shows that $v$ does not split, since $w$ is ramified.
2. `satDict` turns the Satake parameters $B$ into an unramified principal series: $\pi_v$ is spherical and is a subquotient of the principal series of unramified characters with values $\alpha_1, \dots, \alpha_n$ at a uniformizer, and `SSatUniq_holds` gives $B = \{\alpha_i\}$.
3. `weakStable` gives that $\Pi$ is Galois-invariant and has local components. `LiftGood` then puts $\Pi_w$ in the principal series of the $\omega_i \circ N$.
4. `unrNorm`: since $N(w) = N(v)$, each $\omega_i \circ N$ is the unramified character of $M_w^\times$ with the same value $\alpha_i$.
5. `unlinked` gives $\alpha_i \neq N(v)\,\alpha_j$ for all $i, j$. Then `unlSph` shows that $\Pi_w$ is spherical.
6. `satDict` at $w$ gives that $\Pi$ has Satake parameters $\{\alpha_i\} = B$ at $w$.

## In the Lean code

The theorem is in [QuadLift.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/QuadLift.lean#L10). Its proof is the term

```
ramSphOf locGal (liftGood (coreId varEx varTrace elemPairJ_holds))
```

`RamSph` is in [RamDefs.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/RamDefs.lean#L12) and `ramSphOf` in [RamSphOf.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/RamSphOf.lean#L51). `LocGal`, `LiftGood` and `CoreId` are in [ElemPairJ.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/JacobianTraceQuotients/ElemPairJ.lean#L64).

Two small points. `satDict` fixes the sign $\varepsilon = 1$ of the Satake normalization, but `ramSphOf` also handles $\varepsilon = -1$ in a private lemma; that branch is never used. `LocGal` also says that $N$ is the field norm, and `ramSphOf` drops this fact. `unlinked` calls `PositivityTheory.RgJS.unit_exponent_holds`, which we have not unfolded.
