---
id: arch-recip-of-principalisation
title: Reciprocity for the archimedean terms, from principalisation
kind: theorem
decl: GlobalTheory.MixHt.archRecip_of_principalisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArchLogNormReciprocityOfPrincipalisation
covers: 405
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ArchRecip}$: the archimedean part of an arithmetic intersection number does not depend on the order in which two sections cut the variety. It is the second analytic input of [the rules of arithmetic intersection](/entry/ar-calc-of-principalisation/). It reaches that proof through the renaming [`T.archLogNormReciprocity_of_principalisation`](/entry/arch-log-norm-reciprocity-of-principalisation/).

## Statement

Let $Y \to \operatorname{Spec} k$ be an arithmetic variety of dimension $e+2$ (`IsArithVar q (e + 1)`), with $Y$ integral and locally noetherian. For hermitian line bundles $\overline{L}_1, \dots, \overline{L}_d, \overline{M}$ and a rational section $r$ of $\overline{M}$, let $\mathrm{mix}(\overline{L}; \overline{M}, r)$ be the Lean `mixArch`: the polarisation, divided by $d!$, of $n \mapsto$ `archInt` of $\bigotimes_i \overline{L}_i^{n_i}$ against $r$. We have not unfolded `archInt`. By its name it is the integral of $\log \|r\|$ against the top power of the first Chern form, so $\mathrm{mix}$ is the mixed integral against $c_1(\overline{L}_1) \cdots c_1(\overline{L}_d)$. Below, $\overline{L} = (\overline{L}_1, \dots, \overline{L}_e)$. For a point $z$ of $Y$ and a section $t$ of $\overline{N}$, let $\mathrm{res}(\overline{L}, \overline{N}, t, z)$ be $\mathrm{mix}$ on the closure $\overline{\{z\}}$ of the restrictions, if $t$ does not vanish on $\overline{\{z\}}$, and $0$ otherwise.

**Theorem.** Assume $\mathrm{Princ}$. Let $s$ be a section of $\overline{M}$ and $t$ a section of $\overline{N}$, both nonzero at the generic point, such that no point of codimension $1$ is a zero of both. Then

$$\mathrm{mix}(\overline{N}, \overline{L}; \overline{M}, s) + \sum_z \operatorname{ord}_z(s)\, \mathrm{res}(\overline{L}, \overline{N}, t, z) = \mathrm{mix}(\overline{M}, \overline{L}; \overline{N}, t) + \sum_z \operatorname{ord}_z(t)\, \mathrm{res}(\overline{L}, \overline{M}, s, z).$$

By its shape, this is the archimedean half of the symmetry $\widehat{\operatorname{div}}(s) \cdot \widehat{\operatorname{div}}(t) = \widehat{\operatorname{div}}(t) \cdot \widehat{\operatorname{div}}(s)$. For Green currents it is the commutativity of the star product (Gillet and Soulé, Publ. Math. IHÉS 72, 1990).

## Proof

The proof moves each term to the complex places and then uses reciprocity on each complex variety. $Y$ is noetherian and $k$ has finitely many embeddings $\sigma \colon k \to \mathbb{C}$, by `IsArithVar`.

1. **Residual terms.** If $\operatorname{ord}_z(s) \neq 0$, then $z$ has codimension $1$ and $t$ does not vanish at $z$. `T.restrictedArchIntegral_eq_sum_closureIntegrals` writes $\mathrm{res}(\overline{L}, \overline{N}, t, z)$ as $\sum_\sigma$ of an integral `cycInt` of $\log \|t\|_\sigma$ over the closure of $z$ in $Y_\sigma(\mathbb{C})$.
2. **Main terms.** `T.mixedArchLogNormIntegral_eq_sum_embeddings` writes $\mathrm{mix}$ as $\sum_\sigma$ of a complex integral `Mix.int`. After an exchange of the finite sums, each side of the identity is $\sum_\sigma$ of one expression `side`, which we have not unfolded.
3. **Reciprocity at each $\sigma$.** `T.arith_variety_reciprocity_at_complex_embedding` says that `side` is symmetric in $(s, t)$ at each embedding.

Each of the three lemmas takes $\mathrm{Princ}$ as a hypothesis. The rest is bookkeeping.

## In the Lean code

The theorem is in [ArchLogNormReciprocityOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArchLogNormReciprocityOfPrincipalisation.lean#L21). `ArchRecip`, `mixArch` and `resArch` are in [IsAmbOfIsArithVar.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsAmbOfIsArithVar.lean#L113). The three lemmas are restatements in the files `RestrictedArchIntegralEqSumClosureIntegralsStatement.lean`, `MixedArchLogNormIntegralEqSumEmbeddingsStatement.lean` and [ArithVarietyReciprocityAtComplexEmbeddingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithVarietyReciprocityAtComplexEmbeddingStatement.lean#L16). We have not opened their proofs.

The Lean sums over $z$ are `finsum`s over all points of $Y$; only points of codimension $1$ in the support of the divisor contribute.
