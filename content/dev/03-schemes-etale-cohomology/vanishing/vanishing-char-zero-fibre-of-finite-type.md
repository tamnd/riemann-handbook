---
id: vanishing-char-zero-fibre-of-finite-type
title: Kawamata-Viehweg vanishing in characteristic zero by reduction modulo p squared
kind: theorem
decl: GlobalTheory.vanishing_charZero_fibre_of_finiteType
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.KawamataViehwegSpreading
covers: 521
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement of its second name [`kawamata_viehweg_spreading`](/entry/kawamata-viehweg-spreading/), which [`vanishing_ample_snc_charZero`](/entry/vanishing-ample-snc-char-zero/) uses. It is the step from characteristic $0$ to characteristic $p$. The proof finds a prime $p > d$ and a map $R \to \mathbb{Z}/p^2$ at which the data stay good, proves the vanishing on the fibre over $\mathbb{F}_p$ with [`charp_vanishing_liftable`](/entry/charp-vanishing-liftable/), and carries it back to the fibre over $k$ by semicontinuity. This is the method of Deligne and Illusie (Relèvements modulo $p^2$ et décomposition du complexe de de Rham, Invent. Math. 89, 1987). Below this theorem are 521 declarations.

## Statement

The statement is the one in [`kawamata_viehweg_spreading`](/entry/kawamata-viehweg-spreading/): $R$ of finite type over $\mathbb{Z}$, $\varphi \colon R \to k$ injective with $\operatorname{char} k = 0$, $X \to \operatorname{Spec} R$ smooth of relative dimension $d$ and proper, $\pi \colon X' = X \times_R k \to X$, a relative snc family $(L_i, \sigma_i)$ over $R$, $K$ the canonical bundle of $X/R$, $\pi^* A$ ample, $0 \leq b_i < r$ and $r[M] = r[K] + \sum_i b_i [L_i] + [A]$. Then $H^q(X', \pi^* M) = 0$ for $q > 0$.

## Proof

1. **The ring.** $R$ embeds in $k$, so it is a Noetherian domain of characteristic $0$. Let $F$ be its fraction field; $\varphi$ factors through $F$.
2. **Ampleness on the generic fibre.** $\pi^* A$ is ample on $X'$, and $X'$ is a base change of $X_F$ along $F \to k$. So $A$ is ample on $X_F$ (`FibreAmple.relAmple_of_fieldExtension`). By `AmpleSpread.relAmple_spread` there is $a \neq 0$ in $R$ such that $A$ is relatively ample on $X \times_R R'$ for every map $R \to R'$ that sends $a$ to a unit.
3. **The prime.** `exists_ringHom_zmod_prime_sq_isUnit_of_finiteType` gives a prime $p > d$ and $\chi \colon R \to \mathbb{Z}/p^2$ with $\chi(a)$ a unit. Let $Y = X \times_R \mathbb{Z}/p^2$ and $X_1 = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p$, with $\rho \colon X_1 \to X$.
4. **The fibre over $\mathbb{F}_p$.** $X_1$ is smooth of relative dimension $d$ and proper over $\mathbb{F}_p$. By step 2, $\rho^* A$ is ample on $X_1$, so $X_1$ is projective over $\mathbb{F}_p$. The family $(L_i, \sigma_i)$ pulls back to a relative snc family on $Y$ over $\mathbb{Z}/p^2$. The canonical bundle of $X_1$ is the pullback of $K$, and the relation in $\operatorname{Pic}$ pulls back along $\rho$. So `charp_vanishing_liftable` gives $H^q(X_1, \rho^* M) = 0$ for $q > 0$.
5. **Back to $k$.** `SemicontLB.subsingleton_coh_pull_of_ker_le` says: for $X$ proper and flat over a Noetherian ring $R$, a line bundle $M$, and maps $g_1 \colon R \to \kappa_1$, $g_2 \colon R \to \kappa_2$ to fields with $\ker g_2 \subseteq \ker g_1$, if $H^q$ of the pullback of $M$ to the fibre over $g_1$ is $0$, then so is $H^q$ on the fibre over $g_2$. Take $g_1 = \chi$ followed by reduction mod $p$, and $g_2 = \varphi$, with $\ker \varphi = 0$.

## In the Lean code

The theorem is in [KawamataViehwegSpreading.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegSpreading.lean#L22). The lemmas it calls, besides those named above:

- `relAmple_iff_isAmpleLB_of_isAffine`, to pass between relative and absolute ampleness over an affine base.
- `isProjOver_iff_isProper_and_exists_isAmpleLB`, for projectivity of $X_1$.
- `LogPair.relSnc_baseChange`, in [RelativeSncBaseChange.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/RelativeSncBaseChange.lean#L17), and `CanonLB.baseChange`.
- `GlobalTheory.charp_vanishing_liftable`.

Step 5 is a form of the semicontinuity theorem (Hartshorne, Algebraic Geometry, III.12.8, for projective morphisms). The Lean lemma is in [CohomologyVanishingSpecializes.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/CohomologyVanishingSpecializes.lean#L87); we have not read its proof. The theorem does not assume that $X'$ is projective: projectivity is only needed over $\mathbb{F}_p$, and step 4 gets it from the ample bundle.
