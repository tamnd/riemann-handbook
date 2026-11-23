---
id: v-fin-holds
title: The ℓ-adic cohomology of a proper scheme has finite rank
kind: theorem
decl: UpperTheory.Gal.G3.vFin_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.PAdicWittLattices.VFinHolds
covers: 4157
status: drafted
drafted_by: writer@claude
---
This theorem proves `VFin`: for a proper scheme over an algebraically closed field, the $\ell$-adic cohomology is a finitely generated $\mathbb{Z}_\ell$-module, and the rational cohomology has finite dimension. [The embedding into the cohomology of a model](/entry/mat-in-holds/) uses it to make the cohomology of a smooth projective model finite dimensional. It passes from finite levels to the limit. The finite levels come from [the finiteness theorem](/entry/etale-finiteness-of-duality/), which has most of the 4,157 declarations.

## Statement

**Cohomology in the Lean code.** The proof works in the big étale site of all schemes. For a scheme $X$ and $q \geq 1$, $H^n(X, \mathbb{Z}/q(i))$ (`Ht`) is an Ext group from the free sheaf of $\mathbb{Z}/q$-modules on $X$ to the twist $\mathbb{Z}/q(i)$. Then $H^n(X, \mathbb{Z}_\ell(i))$ (`Hl`) is the module of compatible systems in $\varprojlim_k H^n(X, \mathbb{Z}/\ell^k(i))$, and $H^n(X, \mathbb{Q}_\ell(i)) = \mathbb{Q}_\ell \otimes_{\mathbb{Z}_\ell} H^n(X, \mathbb{Z}_\ell(i))$ (`HQ`).

**Theorem.** Let $\ell$ be a prime and $k$ an algebraically closed field with $\ell \neq 0$ in $k$. Let $X$ be a proper scheme over $k$, and let $n, i \in \mathbb{Z}$. Then $H^n(X, \mathbb{Z}_\ell(i))$ is a finitely generated $\mathbb{Z}_\ell$-module, and $H^n(X, \mathbb{Q}_\ell(i))$ has finite dimension over $\mathbb{Q}_\ell$.

## Proof

1. **Finite levels.** For each $a$ and $m$, the group $H^m(X, \mathbb{Z}/\ell^a(i))$ is finite. This is `Et.etale_finiteness_of_duality`, which proves the statement `E4`: finiteness of $H^m(X, \mathbb{Z}/q(i))$ for $X$ proper over an algebraically closed field with $q$ invertible. It is the finiteness theorem of SGA 4, Exposé XIV (Artin), in the Lean model of cohomology.
2. **Bockstein sequences.** For each $a$ and $b$, the sequence $0 \to \mathbb{Z}/\ell^a \to \mathbb{Z}/\ell^{a+b} \to \mathbb{Z}/\ell^b \to 0$ gives a long exact sequence in cohomology, compatible in $a$ (`BockData`). `Fin.AdicFin.etale_bockstein_sequence_adic_finiteness` proves it from four lemmas on the cohomology: the long exact sequence for coefficients, invariance under the coefficient ring, a bijectivity lemma for support, and `RedCoef.a11`. It also needs that $\ell$ is invertible on $X$ (`FinQCut.inv_of_over`).
3. **The kernel of reduction.** `EWeil.AdicKerPf.AdicKer_of` uses steps 1 and 2: a class in $H^n(X, \mathbb{Z}_\ell(i))$ that vanishes mod $\ell^k$ is $\ell^k$ times a class.
4. **Finite generation.** `EWeil.AdicFinPf.AdicFin_of` proves: if each $H^n(X, \mathbb{Z}/\ell^k(i))$ is finite and the kernel of reduction mod $\ell^k$ is $\ell^k H^n(X, \mathbb{Z}_\ell(i))$, then $H^n(X, \mathbb{Z}_\ell(i))$ is finitely generated over $\mathbb{Z}_\ell$.
5. The base change of a finite module to $\mathbb{Q}_\ell$ is finite (`Module.Finite.base_change`).

## In the Lean code

The theorem is in [VFinHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/VFinHolds.lean#L14). The statement `VFin` is in [SplitsSelfOfIso.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/SplitsSelfOfIso.lean#L10). Also used:

- `etale_finiteness_of_duality`, in [EtaleDualityTraceIsomorphism.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean#L46).
- `AdicFin` and `AdicKer`, in [AdicLimPf.lean](lean:Development/EtaleCohomology/KummerTheory/AdicLimPf.lean#L8).
- `BockData`, in [InjSlice.lean](lean:Development/EtaleCohomology/KummerTheory/InjSlice.lean#L132).

The name of `etale_finiteness_of_duality` says that finiteness comes from duality. Its proof calls `etale_duality_trace_isomorphism`, proper base change and a projective bundle formula among 28 lemmas that `e4` takes. We have not followed which of them give finiteness. We have not unfolded the lemmas `GlobalTheory.T.*` or `RedCoef.a11` in step 2.
