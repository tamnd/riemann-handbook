---
id: arch-ex
title: Archimedean idempotents for the induction from GL(2) to GL(4)
kind: theorem
decl: UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.archEx
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.InductionEstimates.IwahoriHeckeInjectivity.IdempotentTraces.ArchEx
covers: 361
status: drafted
drafted_by: writer@claude
---
This theorem gives the archimedean test data for [the induced spectrum on GL(4)](/entry/core-ind/). For a Galois-swapped pair $\tau_1, \tau_2$ on $\mathrm{GL}_2(E)$ it finds matching idempotents at infinity over $F$ and over $E$, and a nonzero Eisenstein section that they fix. We use the notation of that entry.

## Statement

Let $K_n$ be the compact group `archCompact` of $\mathrm{GL}_n$ at the infinite places. An idempotent (`IdemA`) is a Haar probability measure $\kappa$ on $K_n$ and a continuous $e \colon K_n \to \mathbb{C}$ with $e(k^{-1}) = \overline{e(k)}$ and $e * e = e$. An Eisenstein section (`IsSec`) is a continuous bounded function $f$ on $\mathrm{GL}_4$ over $E$, left invariant under the unipotent radical of the $(2,2)$ parabolic and under $\mathrm{diag}(r, r, r^{-1}, r^{-1})$ for $r > 0$, such that each $(m_1, m_2) \mapsto f(\mathrm{diag}(m_1, m_2) g)$ is a finite sum of products of functions from $\tau_1$ and $\tau_2$.

**Theorem.** In the setup `ForSwap`, let $D$ be an archimedean datum for $\sigma$. Then there are idempotents $(\kappa_F, e_F)$ on $K_4$ over $F$ and $(\kappa, e)$ on $K_4$ over $E$, a measure $\kappa_2$ and functions $p_1, p_2$ on $K_2$ over $E$, and $k_0 \in K_4$ over $E$, with:

1. $e(k) = \prod_i e_F(k_i)$, when $k_1, k_2$ are the two components of $k$ given by $D$ (`IsSq`);
2. each $p_i$ is an idempotent with a nonzero fixed vector in $\tau_i$, and each $p_i R(g)$ acts by a scalar on these fixed vectors (`RankInf`);
3. if $f$ is a section fixed by $e$, then $m_1 \mapsto f(\mathrm{diag}(m_1, m_2) k_0 h)$ is fixed by $p_1$, and the same holds in $m_2$ for $p_2$;
4. a section fixed by $e$ that is zero at all these points is zero;
5. if $\tau_1, \tau_2$ have spherical vectors off a finite $S$, there are a level $U$ and a nonzero section $f$ fixed by $e$ and by $U$ off $S$.

Items 2 to 5 are the fields of `ArchLine`.

## Proof

1. `coEx` gives coordinates at infinity, and `u4` gives a measure.
2. `minEx` gives minimal $K$-types of $\tau_1$ and $\tau_2$ at each infinite place. `minSwap` moves the type from one to the other with the twist $\theta_2$.
3. `ext4` and `extPi` extend these types to $\mathrm{GL}_4$. Then `lineVal`, `rankInf`, `lineInj` and `lineEx` give items 3, 2, 4 and 5. The private `idemTr` gives the idempotent properties.
4. A product computation over the two components gives item 1.

## In the Lean code

The theorem is at [line 35 of ArchEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/ArchEx.lean#L35). `ArchEx`, `IdemA` and `ArchLine` are in [HeckeInj.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/HeckeInj.lean#L64), and `IsSec` is in [AdelDefs.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/TruncatedCuspIrreducibility/AdelDefs.lean#L55). We have not unfolded `minEx` or `lineEx`. In item 3 the Lean code writes $\mathrm{diag}(m_1, m_2)$ as `lv m₁ m₂ 0`.
