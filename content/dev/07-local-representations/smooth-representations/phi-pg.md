---
id: phi-pg
title: The twisted Jacquet functor on a mirabolic product, as an extension
kind: theorem
decl: GlobalTheory.CompanionTheory.BZPhiPG.phiPG
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.PhiPgCommutationHolds
covers: 630
status: drafted
drafted_by: writer@claude
---
This theorem proves `PhiPG`, fact 5 of [the Leibniz rule with ordered layers](/entry/leibniz-ord/). It only changes indices. The real content is in [the core of the extension](/entry/phi-pg-core/).

## Statement

We use the notation of the parent entry. Let $P_m$ be the mirabolic subgroup of $\mathrm{GL}_m(k)$.

**Theorem.** Let $k$ be a nonarchimedean local field and $\psi$ a continuous unitary character of $k$ with $\psi \ne 1$. Let $\tau$ be a smooth representation of $P_{i+2}$ and $\sigma$ a smooth representation of $\mathrm{GL}_{t+1}(k)$. Then $\Phi(\tau \times \sigma)$ has a subrepresentation isomorphic to $\Phi\tau \times \sigma$, with quotient isomorphic to $\Psi\tau \times \sigma|_P$. All three are representations of $P_{i+t+2}$.

So there is an exact sequence $0 \to \Phi\tau \times \sigma \to \Phi(\tau \times \sigma) \to \Psi\tau \times \sigma|_P \to 0$. This is one of the exact sequences of Bernstein and Zelevinsky (Ann. Sci. ENS 10 (1977), Section 4).

## Proof

The core theorem gives the same extension, with the three representations written as compactly induced spaces `RO`, `XR'` and `RC`, over the index $(i+1)+t$. The proof casts the extension to the index $i+t+1$. Then it rewrites the three spaces as `prodPGn (phiN ψ τ) σ`, `prodPGn τ σ` and `prodGPn (psiN τ) (gres σ)` with `ro_eq`, `xr_eq` and `rc_eq`, and moves the cast inside $\Phi$ with `phiN_mcast`. The rest is bookkeeping.

## In the Lean code

The theorem is in [PhiPgCommutationHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PhiPgCommutationHolds.lean#L231). `PhiPG` is defined in [LeibnizOrd.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/LeibnizOrders/LeibnizOrd.lean#L29), and `MExt` in [ProdGPn.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/LeibnizOrders/ProdGPn.lean#L34).

The hypothesis $\psi \ne 1$ of `PhiPG` is introduced as `_` and never used. The core theorem does not ask for it.
