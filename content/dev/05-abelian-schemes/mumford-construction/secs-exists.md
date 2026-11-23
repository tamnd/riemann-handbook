---
id: secs-exists
title: Theta sections whose reduction is the projective embedding of the torus extension
kind: theorem
decl: GlobalTheory.Mum.SecsAsm.secs_exists
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSectionsPrescribedReductionFiniteExt
covers: 486
status: drafted
drafted_by: writer@claude
---
This theorem builds, for a labelled cover, sections of a power of its line bundle on the generic fibre whose reduction along every trait is a fixed projective immersion of the closed fibre of the torus extension. It is the content of [`exists_secs_finExt`](/entry/exists-secs-fin-ext/), and through it of step 1 of [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/).

## Statement

Let $R$ with `Base R`, $\kappa = R/\mathfrak{m}$, $D$ and a labelled cover $C$ with modification $\pi \colon S \to \operatorname{Spec} R$, group $G$, line bundle $L$ and generic fibre $\alpha \colon A \to G$ be as in [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/).

A datum `Secs` for $C$ consists of sections $s_0, \dots, s_N$ of $\alpha^* L^{k}$ and $\theta$ of $\alpha^* L$, a smooth group $Y$ over $\kappa$, an immersion $j \colon Y \to \mathbb{P}^N_R$ over $\operatorname{Spec}\kappa$, and a nonempty open $O \subseteq Y$, with a trait condition. Let $W$ be a complete discrete valuation ring, $R \to W$ injective and local, and $\operatorname{Spec} W \to S$ a lift. Then after a finite extension $W \to W'$ there are sections $\sigma_i, \theta'$ on the pullback $G'$ of $G$ that agree with $s_i, \theta$ on the generic fibre, and a group isomorphism $e$ of the closed fibre of $G'$ with $Y \otimes \kappa(W')$. For each field-valued point $p'$ of that closed fibre with image $y$ in $Y$: $[\sigma_0(p') : \dots : \sigma_N(p')] = j(y)$, and $\theta'(p') \neq 0$ if $y \in O$.

**Theorem.** $C$ has a `Secs` datum.

## Proof

Let $\tilde G$ be the torus extension of $D$ (`Ext D`), a smooth commutative group over $R$ with a map $q$ to the abelian part of $D$.

1. `exists_theta_immersion_torus_extension_projective`: there are a finite set $\Sigma$ of characters and $k_1$ such that for each $k \geq k_1$, sections $\tau_0, \dots, \tau_N$ of $q^* L^k$ define an immersion $\tilde G \to \mathbb{P}^N_R$. Each $\tau_i$ is the term (`IsTermOf`) of a section $b_i$ for a character $\alpha_i \in \Sigma$.
2. `exists_integralThetaFamily_prescribed_leadingTerm`: for large $k$, each $b_i$ is the leading term (`IntFam.Lead`) of an integral family $F_i$.
3. [`exists_secs_of_intFam`](/entry/exists-secs-of-int-fam/): for $k = n^m$ with $m$ large, a map $\Phi$ sends each family $F$ to a section on $A$ with expansion $F$ along each trait, up to a unit. Set $s_i = \Phi(F_i)$.
4. `exists_term_nonzero_closed` gives a degree 1 term $\tau_\theta$ that is nonzero at a point of the closed fibre of $\tilde G$. Step 3 in degree 1 gives $\theta$ for a family led by it.
5. Set $Y = \tilde G \otimes \kappa$, let $j$ be the immersion of step 1 on $Y$, and $O = \{\tau_\theta \neq 0\}$.

For the trait condition, `LabCover.exists_trait` gives a trait datum, and `trait_lead_value` gives $e$: on the closed fibre, a section with expansion led by $b$ is a unit $c$ times the term of $b$, with one $c$ for all $b$. So `toProj_secPull_of_sval` gives $[\sigma_i(p')] = j(y)$, and $\theta'$, a unit times $\tau_\theta$, does not vanish over $O$.

The shape is that of Mumford's construction, where sections of $L^k$ are Fourier series $\sum_\alpha f(\alpha)$ over the characters (Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter III).

## In the Lean code

The theorem is in [ExistsSectionsPrescribedReductionFiniteExt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSectionsPrescribedReductionFiniteExt.lean#L34), with the helpers `gs_scal_one` and `closed_pt`. `Secs` is in [IsProjOverWeierstrass.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProjOverWeierstrass.lean#L87). We read the statements of the called lemmas, not their proofs. The exponent is $m = \max(j_0, k_1 + \sum_{a \in \Sigma} k_0(a))$.
