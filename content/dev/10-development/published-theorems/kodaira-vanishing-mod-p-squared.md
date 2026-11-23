---
id: kodaira-vanishing-mod-p-squared
title: Vanishing in characteristic p for an integral variety with a lift modulo p squared, second name
kind: theorem
decl: GlobalTheory.T.kodaira_vanishing_mod_p_squared
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.KodairaVanishingModPSquaredStatement
covers: 461
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`charp_of_lift`](/entry/charp-of-lift/). It has the same statement, and its proof only calls that theorem. [`charp_vanishing_liftable`](/entry/charp-vanishing-liftable/) applies it to each connected component of its variety. The content is in `charp_of_lift`. Below this theorem are 461 declarations.

## Statement

The statement is the one of [`charp_vanishing_liftable`](/entry/charp-vanishing-liftable/), with one more hypothesis: $X$ is integral. So: $p$ prime, $d < p$, $X = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p$ integral, smooth of relative dimension $d$ and projective over $\mathbb{F}_p$, a relative snc family $(L_i, \sigma_i)$ on $Y$ over $\mathbb{Z}/p^2$, $A$ ample on $X$, $0 \leq b_i < r$ and $r[M] = r[K] + \sum_i b_i\, \pi^*[L_i] + [A]$ in $\operatorname{Pic} X$. Then $H^q(X, M) = 0$ for all $q > 0$.

With all $b_i = 0$ and $r = 1$ this gives $H^q(X, K \otimes A) = 0$, Kodaira vanishing for a variety that lifts to $\mathbb{Z}/p^2$ (Deligne and Illusie, Invent. Math. 89, 1987). The general case allows a fractional boundary, as in Kawamata-Viehweg vanishing.

## Proof

The proof is `charp_of_lift` applied to the same arguments. In outline, that proof builds Cartier divisors $E_i$ on $X$ with $\mathcal{O}(E_i) = \pi^* L_i$ and an snc atlas with a decomposition property for Čech complexes of logarithmic forms (`exists_atlas_decomp`, `Decomp`). It writes $M = \mathcal{O}(M')$, checks that $rM' - rK - \sum_i b_i E_i$ gives an ample bundle, and calls `subsingleton_coh_of_decomp`. We have not unfolded `Decomp`; see the entry of `charp_of_lift`.

## In the Lean code

The theorem is in [KodairaVanishingModPSquaredStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KodairaVanishingModPSquaredStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with the name `GlobalTheory.CharPVanish.charp_of_lift` in each branch. The two statements are identical. `charp_of_lift` is in [KodairaVanishingModPSquared.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KodairaVanishingModPSquared.lean#L17).

The name says "Kodaira vanishing", but the statement has the boundary terms $b_i\, \pi^*[L_i]$ of Kawamata-Viehweg vanishing. Kodaira vanishing is the case with no boundary terms and $r = 1$.
