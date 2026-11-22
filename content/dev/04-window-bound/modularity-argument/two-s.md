---
id: two-s
title: Vanishing of two Bloch-Kato Selmer groups, given Satake parameters above the prime
kind: theorem
decl: UpperTheory.V.Z.Kato.WeilSphericalRecords.twoS
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.SphericalDecomposition.SphAtTw
covers: 9174
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{KatoTwoS}$ from two inputs: the Galois cohomology statements $\mathrm{LitCoh}$ and a source statement $\mathrm{SrcS}$. [The theorem above it](/entry/kato-two-w-of-prints-h-of-r-t-of-quad-bc2/) uses it to prove $\mathrm{KatoTwoW}$, which feeds the first count of the chapter [The window bound VWin](/proof/vwin/). The proof applies one vanishing theorem twice, to $W$ and to $W \otimes \det W$. That vanishing theorem comes from [the zeta element theorem](/entry/zeta-ur/), which is the real content below this entry.

## Statement

Let $\ell$ be an odd prime and $e \ge 1$. For a representation $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ and $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $\mathrm{SphAt}(\iota, e, W)$ says the following. Let $\varphi$ be a character that is trivial on $G_{\mathbb{Q}(\mu_M)}$ for some $M \ge 1$. Let $w$ be a place above $\ell$ where $W \otimes \varphi$ has a flag whose characters on inertia are $\bar\chi^{e}$ and $\bar\chi^{-e}$, with $\bar\chi$ the [[cyclotomic character|XSGB5K2KEG]]. Then every regular algebraic cuspidal representation $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ attached to $W \otimes \varphi$ has Satake parameters at $w$.

$\mathrm{SrcS}$ says: if $W$ is admitted and $\mathrm{SphAt}(\iota, e, W)$ holds, then $W$ has an ordinary source $\mathrm{SrcL}$. That is, there is a newform $g$ of weight $2e+1$ and level prime to $\ell$, with $|a_\ell(g)| = 1$, attached to a twist $W \otimes \bar\chi^{-e} (\det W)^{-1} \chi$ with $\chi$ trivial on $\mu_\ell$, together with conditions on the flags of $W$ at $\ell$.

**Theorem.** Assume $\mathrm{LitCoh}$ and $\mathrm{SrcS}$. Let $W$ satisfy the conditions $\mathrm{Used}$ (with $K$, $\theta$, $\psi$ as in [the entry above](/entry/kato-two-w-of-prints-h-of-r-t-of-quad-bc2/)). Let $f$ be a newform of weight $2e+1$ attached to $W \otimes \bar\chi^{-e}$, and suppose that $\mathrm{SphAt}(\iota, e, W)$ holds. Then the Bloch-Kato Selmer groups of $W$ and of $W \otimes \theta$ vanish.

## Proof

1. Let $\mathrm{VanishOrdL}$ be the statement: if $W$ is admitted and has an ordinary source, then its Bloch-Kato Selmer group vanishes. `vanishOrdL_of_zetaUr` proves it from $\mathrm{LitCoh}$ and the zeta element theorem `Final.zetaUr`.
2. `Used.adm` gives $\det W = \theta$ and that $W$ is admitted.
3. For $W \otimes 1 = W$: $\mathrm{SrcS}$ gives the source, and $\mathrm{VanishOrdL}$ gives the vanishing.
4. For $W \otimes \theta$: write $\theta = \det W$. `admissible_twist_by_det` shows that $W \otimes \det W$ is admitted. The kernel of $\det W$ is open and contains the commutator subgroup. So by the Kronecker-Weber theorem (Washington, *Introduction to Cyclotomic Fields*, Theorem 14.1, in Lean `kwAbs`), $\det W$ is trivial on $G_{\mathbb{Q}(\mu_M)}$ for some $M \ge 1$. The private lemma `sphAt_tw` shows that $\mathrm{SphAt}$ survives a twist by such a character: the twist of $W \otimes \det W$ by $\varphi$ is a twist of $W$ by $\varphi \det W$, which is trivial on $\mu_{MN}$. Then $\mathrm{SrcS}$ and $\mathrm{VanishOrdL}$ give the vanishing.

## In the Lean code

The theorem is in [SphAtTw.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SphericalDecomposition/SphAtTw.lean#L16). $\mathrm{SphAt}$ and $\mathrm{KatoTwoS}$ are in [KatoTwoSOfTwo.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/KatoTwoSOfTwo.lean#L9). $\mathrm{SrcL}$ and $\mathrm{VanishOrdL}$ are in [VanishOrdL.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/VanishOrdL.lean#L13).

- `GlobalTheory.Ord2.vanishOrdL_of_zetaUr`, in [VanishOrdLOfZetaUr.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/VanishOrdLOfZetaUr.lean#L20). It puts $W$ in an ordinary normal form $W'$, applies the zeta element theorem to get an Euler system class for $W'$, uses `es_vanish` to get the vanishing for $W'$, and moves it back to $W$. We have not opened `es_vanish`.
- `UpperTheory.V.Z.Kato.Final.zetaUr`.
- `admissible_twist_by_det`, in [AdmissibleTwistByDet.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/AdmissibleTwistByDet.lean#L484).
- `UpperTheory.V.CF.kwAbs` and `sphAt_tw` (line 9 of the same file).

The name `twoS` says only "two, spherical". The hypothesis $\mathrm{LitCoh}$ is used only inside `vanishOrdL_of_zetaUr`.
