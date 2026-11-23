---
id: unramified-doubling-integral-twisted-place-eigenvector
title: The doubling zeta integral at a twist place, second name
kind: theorem
decl: GlobalTheory.T.unramifiedDoublingIntegral_twisted_place_eigenvector
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.UnramifiedDoublingIntegralTwistedPlaceEigenvectoStatement
covers: 343
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the twisted local zeta integral](/entry/local-zeta-twisted/), which has the real content. The statement is a copy, and the proof only applies that theorem. The theorem is used in [the local factor at a twist place](/entry/local-factor/), which computes the local factor of the flat integrand at one tamely ramified place.

## Statement

Let $k$ be a nonarchimedean local field of characteristic zero, $\xi$ a tame, ramified, unitary character of $k^\times$, and $J$ the parahoric subgroup of $G = \mathrm{GL}_{r+lt}(k)$. Assume the unramified doubling identity for $\mathrm{GL}_n$. Then the matrix coefficient $c$ of the twisted Weil representation is nonzero at $1$, and there is a function $\zeta$ on $G$ with $\zeta = 1$ on $J$ that gives every type matrix coefficient and whose integral against $H^{s-t/2}$ is

$$L(s + \tfrac12, \alpha)\, L(s + \tfrac12, \alpha^{-1}) \prod_{i=1}^{lt} \bigl(1 - q^{-(2s+i)}\bigr).$$

The full statement is in [the source entry](/entry/local-zeta-twisted/).

## Proof

The proof is one line. It applies `GlobalTheory.TwistedZeta.local_zeta_twisted` with the same arguments.

## In the Lean code

The theorem is in [UnramifiedDoublingIntegralTwistedPlaceEigenvectoStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnramifiedDoublingIntegralTwistedPlaceEigenvectoStatement.lean#L7). Its proof is

```
first | exact @GlobalTheory.TwistedZeta.local_zeta_twisted | ...
```

The module name is cut off: it ends in "Eigenvecto". The name says "eigenvector", but the conclusion is an identity of zeta integrals. The eigenvector only enters as a hypothesis.
