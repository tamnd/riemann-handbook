---
id: exists-unitary-fourier-system-traits-family
title: A normalized Fourier system with a member, stated
kind: theorem
decl: GlobalTheory.T.exists_unitary_fourier_system_traits_family
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryFourierSystemTraitsFamilyStatement
covers: 337
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is the statement of [`exists_system_with_traits_and_family`](/entry/exists-system-with-traits-and-family/), and its proof is that theorem. [Separation on the normalized blowup](/entry/sep-b-of-norm-bl/) calls it in step 2. Below it are 337 declarations.

## Statement

Let $E$, $H$, the datum, $X$ and an integral compactification $Z_o$ with generic fibre $Z_F$ be as in [the parent entry](/entry/sep-b-of-norm-bl/). Let $\varphi$ be any `InvFun`. Let $V$ be a local domain with `Mum.Base`, with a monomial family (`MonoFam`) whose generic point maps through $\xi \colon \operatorname{Spec} V \to Z_F$. Let $n$ be an odd prime and $j_0 \in \mathbb{N}$.

**Theorem.** There are $j \geq j_0$, an integral scheme $M$ with a map to $Z_o$, a point $z_1 \in M$, and a Fourier system $\Phi$ of level $(n^j)^2$ over the local ring $\mathcal{O}_{M, z_1}$ (`VSys`), with a nonempty open $U \subseteq M$ and an index $y$, such that:

1. $M$ is a normal cover of $Z_o$ at $z_1$ (`IsCov`);
2. each trait of $X_F$ through $\operatorname{Spec} \mathcal{O}_{M, z_1}$ and $U$ is an index of $\Phi$ (`HasTraitsOn`);
3. the monomial family is the member $y$ of $\Phi$, with theta terms of level $(n^j)^2$ (`IsMember`).

[The proof entry](/entry/exists-system-with-traits-and-family/) defines these objects.

## Proof

The proof is the term `GlobalTheory.USep.exists_system_with_traits_and_family`.

## In the Lean code

The theorem is in [ExistsUnitaryFourierSystemTraitsFamilyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryFourierSystemTraitsFamilyStatement.lean#L12). The statement repeats the statement of that theorem word for word. `sepB_of_normBl` cites this `T.` name.
