---
id: charp-vanishing-liftable
title: Kawamata-Viehweg vanishing in characteristic p for a lift modulo p squared
kind: theorem
decl: GlobalTheory.charp_vanishing_liftable
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.KawamataViehwegModPSquared
covers: 474
status: drafted
drafted_by: writer@claude
---
This theorem is the vanishing theorem over $\mathbb{F}_p$ that [`vanishing_charZero_fibre_of_finiteType`](/entry/vanishing-char-zero-fibre-of-finite-type/) applies to a fibre of a model. Its proof only removes the hypothesis that $X$ is integral: it cuts $X$ into its connected components and applies [`kodaira_vanishing_mod_p_squared`](/entry/kodaira-vanishing-mod-p-squared/) to each. Below this theorem are 474 declarations.

## Statement

Let $p$ be a prime and $d < p$. Let $g \colon Y \to \operatorname{Spec} \mathbb{Z}/p^2$ be a scheme and $X = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p$, with $\pi \colon X \to Y$, such that $f \colon X \to \operatorname{Spec} \mathbb{F}_p$ is smooth of relative dimension $d$ and projective. Let $L_1, \dots, L_s$ be line bundles on $Y$ with sections that form a relative snc family over $\mathbb{Z}/p^2$ (see [`vanishing_ample_snc_charZero`](/entry/vanishing-ample-snc-char-zero/)). Let $K$ be the canonical bundle of $X/\mathbb{F}_p$, and $M$, $A$ line bundles on $X$ with $A$ ample. Let $r > 0$ and $0 \leq b_i < r$ with

$$r[M] = r[K] + \sum_i b_i\, \pi^*[L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$

Then $H^q(X, M) = 0$ for all $q > 0$.

So $Y$ with the divisors of the $\sigma_i$ is a lift of $X$ with an snc boundary to $\mathbb{Z}/p^2$. Deligne and Illusie (Invent. Math. 89, 1987) prove Kodaira vanishing for smooth projective varieties in characteristic $p$ that lift to the Witt vectors of length $2$, under a bound on the dimension in terms of $p$.

## Proof

1. $X$ is smooth and quasi-compact over $\mathbb{F}_p$. `exists_integral_clopen_cover_of_smooth_quasiCompact_field` gives a cover of $X$ by pairwise disjoint open sets $U_c$, each integral, each with a closed immersion into $X$.
2. By `cohomology_subsingleton_of_disjoint_open_cover`, it suffices to prove $H^q(U_c, M|_{U_c}) = 0$ for each $c$.
3. Fix $c$. Since $\mathbb{Z}/p^2 \to \mathbb{F}_p$ is surjective, `open_subscheme_closed_base_change` gives an open $W \subseteq Y$ with $U_c = W \times_{\mathbb{Z}/p^2} \mathbb{F}_p$. The family $(L_i|_W, \sigma_i|_W)$ is still relative snc, $U_c$ is smooth of relative dimension $d$ and projective, $A|_{U_c}$ is ample (restriction along a closed immersion), and the canonical bundle of $U_c$ is the restriction of $K$. Restrict the relation in $\operatorname{Pic}$ to $U_c$ and apply `kodaira_vanishing_mod_p_squared`.

## In the Lean code

The theorem is in [KawamataViehwegModPSquared.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegModPSquared.lean#L20). The lemmas it calls, all as `GlobalTheory.T.…`: `exists_integral_clopen_cover_of_smooth_quasiCompact_field`, `cohomology_subsingleton_of_disjoint_open_cover`, `open_subscheme_closed_base_change`, `relative_snc_open_immersion`, `canonical_bundle_open_restrict` and `kodaira_vanishing_mod_p_squared`, with `IsAmpleLB.pull_of_isClosedImmersion` for the ample bundle.

The base is $\mathbb{F}_p$ itself, not a perfect field. The only difference from `kodaira_vanishing_mod_p_squared` is the hypothesis that $X$ is integral.
