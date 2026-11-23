---
id: mul-mem-range-norm
title: The norm group of a local quadratic extension has index two
kind: theorem
decl: GlobalTheory.KSp.NormIndex.mul_mem_range_norm
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MulMemRangeNorm
covers: 772
status: drafted
drafted_by: writer@claude
---
This theorem says that in a quadratic extension of local fields, the product of two non-norms is a norm. It is the content of [its statement form](/entry/mul-mem-range-norm-of-not-mem/), which goes to [the Gauss integral for a Hermitian form](/entry/has-gauss-herm/). Almost all of the 772 declarations below it belong to the local reciprocity map.

## Statement

Let $F$ be a nonarchimedean local field of characteristic $0$. Let $E$ be a field and an $F$-algebra, with an $F$-algebra map $c \colon E \to E$ and a unit $\delta \in E$ such that $c(\delta) = -\delta$ and $(1, \delta)$ is an $F$-basis of $E$. Write $N = N_{E/F}(E^\times) \subseteq F^\times$.

**Theorem.** If $x, y \in F^\times$ and $x \notin N$, $y \notin N$, then $xy \in N$.

Equivalently, $N$ has index at most $2$ in $F^\times$. This follows from the local reciprocity law, $F^\times / N_{L/F}(L^\times) \cong \mathrm{Gal}(L/F)$ for a finite abelian extension $L/F$ (Neukirch, Algebraic Number Theory, Ch. V, Thm. 1.3).

## Proof

1. The basis gives $[E : F] = 2$. So $E/F$ is Galois, since the characteristic is $0$.
2. Embed $E$ in an algebraic closure $\overline{F}$. Let $L$ be the image. Then $L/F$ is Galois of degree $2$, so $\mathrm{Gal}(L/F)$ has order $2$. It is cyclic, so $L/F$ is abelian.
3. `artin_reciprocity_char_zero` gives a local Artin map $\mathrm{Art} \colon F^\times \to G_F^{\mathrm{ab}}$. One of its properties: for each finite abelian $L/F$, the composite $F^\times \to G_F^{\mathrm{ab}} \to \mathrm{Gal}(L/F)$ is surjective, with kernel $N_{L/F}(L^\times)$.
4. The isomorphism $E \cong L$ preserves norms. So $N$ is the kernel of $\rho \colon F^\times \to \mathrm{Gal}(L/F)$.
5. Then $\rho(x) \neq 1$ and $\rho(y) \neq 1$. In a group of order $2$, two elements different from $1$ have product $1$ (`mul_eq_one_of_card_two`). So $\rho(xy) = 1$, and $xy \in N$.

## In the Lean code

The theorem is at [MulMemRangeNorm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MulMemRangeNorm.lean#L29). The lemma `mul_eq_one_of_card_two` is at [line 13](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MulMemRangeNorm.lean#L13).

- `artin_reciprocity_char_zero` is at [TransportC.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportC.lean#L155). It proves `LocalReciprocity F`, whose conditions `IsLocalArtinMap` are at [Reciprocity.lean](lean:ReciprocityTheory/NeutralLocalFields/Reciprocity.lean#L79). The proof reads only the last condition: surjectivity and kernel equal to `normGroup`. We have not unfolded the proof of `artin_reciprocity_char_zero`.
- The condition on $(c, \delta)$ is `IsQuad` in [HilbertNinetyQuotientHomEqIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HilbertNinetyQuotientHomEqIff.lean#L175). The proof uses only its basis field, to get $[E:F] = 2$. The facts that $\delta$ is a unit and that $c(\delta) = -\delta$ are not used, and $c$ itself plays no role.
- The topology on $E$ and the hypothesis `IsModuleTopology F E` are not used.
- The hypothesis of characteristic $0$ is needed because the Lean local reciprocity map is proved only in that case. The standard result holds in all characteristics.
