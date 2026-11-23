---
id: charp-of-lift
title: Vanishing in characteristic p for an integral variety with a lift modulo p squared
kind: theorem
decl: GlobalTheory.CharPVanish.charp_of_lift
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.KodairaVanishingModPSquared
covers: 460
status: drafted
drafted_by: writer@claude
---
This theorem proves a vanishing theorem of Deligne-Illusie type for an integral smooth projective variety over $\mathbb{F}_p$ that lifts to $\mathbb{Z}/p^2$. Its second name is [`kodaira_vanishing_mod_p_squared`](/entry/kodaira-vanishing-mod-p-squared/), which only calls it. Through that name, [`charp_vanishing_liftable`](/entry/charp-vanishing-liftable/) applies it to each integral piece of a variety. This entry has the content. Below this theorem are 460 declarations.

## Statement

Let $p$ be a prime and $d < p$. Let $Y$ be a scheme over $\mathbb{Z}/p^2$, and let $X = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p$ with the map $\pi \colon X \to Y$. Suppose that $X$ is integral, smooth of relative dimension $d$ over $\mathbb{F}_p$ and projective. Let $(L_i, \sigma_i)_{i < s}$ be line bundles with sections on $Y$ that form a relative snc family over $\mathbb{Z}/p^2$. Let $K$ be the canonical bundle of $X$, $A$ an ample line bundle and $M$ a line bundle on $X$. Let $r > 0$ and $0 \le b_i < r$ with
$$r[M] = r[K] + \sum_i b_i\, \pi^*[L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$

**Theorem.** $H^q(X, M) = 0$ for all $q > 0$.

For $s = 0$ and $r = 1$ this is Kodaira vanishing for a lift to $W_2$ with $d < p$ (Deligne and Illusie, Invent. Math. 89, 1987).

## Proof

The proof has six steps.

1. `LogAtlas.exists_atlas_decomp` gives Cartier divisors $E_i$ on $X$ with $\mathcal{O}(E_i) = \pi^* L_i$, an snc atlas $\mathcal{A}$ of $X$ for the $E_i$, and the property `Decomp p 𝒜`. This is the place where the lift is used.
2. `Cartier.toPic_surjective` writes $[M] = [\mathcal{O}(M')]$ for a Cartier divisor $M'$.
3. `Cartier.presents_canonical` identifies the canonical divisor with $K$.
4. The divisor $H = rM' - rK - \sum_i b_i E_i$ has the class of $A$. So $\mathcal{O}(H)$ is ample (`IsAmpleLB.of_lbIso`).
5. `subsingleton_coh_of_decomp` gives $H^q(X, \mathcal{O}(M')) = 0$ for $q > 0$.
6. `Div.coh_subsingleton_of_cls_eq` moves the result from $\mathcal{O}(M')$ to $M$, since the classes are equal.

`Decomp p 𝒜` says: for each divisor $G$ and each $\rho$ with $\rho_c < p$, if the hypercohomology of the log de Rham complex of $pG + \sum_c \rho_c E_c$ vanishes in degree $a + b$, then the Čech cohomology of the log $a$-forms of $G$ vanishes in degree $b$. This is the form that the Frobenius decomposition of Deligne-Illusie takes here.

Step 5 works with the twists $G(e) = p^e(M' - K) - \sum_c \lfloor p^e b_c / r \rfloor E_c - \sum_c E_c$. They satisfy $G(e+1) = pG(e) + \sum_c \rho_c E_c$ with $\rho_c < p$ (`frobenius_twist_divisor_recursion`). For large $e$, Serre vanishing on the atlas (`serre_vanishing_snc_atlas`) kills the Čech groups of $G(e)$. `cech_vanishing_frobenius_descent` then carries the vanishing down to $G(0)$ in total degree above $d$. Last, `top_log_forms_canonical_generator` identifies the log $d$-forms of $G(0)$ with sections of $M'$.

## In the Lean code

The theorem is in [KodairaVanishingModPSquared.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KodairaVanishingModPSquared.lean#L17). The lemmas it calls:

- `exists_atlas_decomp` in [FrobeniusDecompositionAtlasModP.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/FrobeniusDecompositionAtlasModP.lean#L100).
- `subsingleton_coh_of_decomp` in [SubsingletonCohOfDecomp.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/SubsingletonCohOfDecomp.lean#L80).
- `Decomp` and `cechFam` in [CechFam.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CechFam.lean#L21).

The Čech groups are subgroups of `abelian₂ X.functionField`, a module of forms over the function field. We have not unfolded `abelian₂`, `logSec`, `coh` or `RelSnc`. The name says "Kodaira vanishing", but the statement has the fractional boundary of Kawamata-Viehweg vanishing.
