---
id: vanish-ord-l-of-zeta-ur
title: Bloch-Kato Selmer groups vanish for representations with an ordinary source, given zeta elements
kind: theorem
decl: GlobalTheory.Ord2.vanishOrdL_of_zetaUr
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.VanishOrdLOfZetaUr
covers: 910
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{VanishOrdL}$ from the literature statements $\mathrm{LitCoh}$ and the zeta element statement $\mathrm{ZetaUr}$. [The vanishing theorem for two twists](/entry/two-s/) applies it to $W$ and to $W \otimes \det W$. The proof changes $W$ to an isomorphic representation in normal form, gets an Euler system class from $\mathrm{ZetaUr}$, and gets the vanishing from [`es_vanish`](/entry/es-vanish/), which has the real content.

## Statement

Let $\ell$ be an odd prime, $\Omega$ an algebraic closure of $\mathbb{Q}$, $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $e \ge 1$, and $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$. $\mathrm{VanishOrdL}$ says: if $W$ is admitted and has an ordinary source $\mathrm{SrcL}(\iota, e, W)$, then the Bloch-Kato Selmer group of $W$ vanishes. Both conditions are stated in [the entry for `twoS`](/entry/two-s/). $\mathrm{ZetaUr}$ says that a representation in the normal form $\mathrm{Nf}$ with an unramified source $\mathrm{SrcUr}$ has an Euler system class $\mathrm{ES}$; see [the zeta element theorem](/entry/zeta-ur/), which proves it.

**Theorem.** $\mathrm{LitCoh}$ and $\mathrm{ZetaUr}$ imply $\mathrm{VanishOrdL}$.

## Proof

Let $W$ be admitted with an ordinary source.

1. `exists_ordinary_normal_form_unramified_source` gives a finite set $S$ of places, a place $A$ above $\ell$, a representation $W'$ conjugate to $W$ in $\mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$, and a newform $g$, with $\mathrm{Nf}(e, S, A, W')$ and $\mathrm{SrcUr}(\iota, e, A, W', g)$.
2. $\mathrm{ZetaUr}$ gives $\mathrm{ES}(W', A)$.
3. [`es_vanish`](/entry/es-vanish/), with $\mathrm{LitCoh}$, gives the vanishing of the Bloch-Kato Selmer group of $W'$.
4. `UpperTheory.V.X.Kato.conj` moves the vanishing from $W'$ to $W$ along the conjugation. `repIso_symm_srcL` turns the conjugation around.

## In the Lean code

The theorem is in [VanishOrdLOfZetaUr.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/VanishOrdLOfZetaUr.lean#L20). $\mathrm{VanishOrdL}$ and $\mathrm{SrcL}$ are in [VanishOrdL.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/VanishOrdL.lean#L13), and $\mathrm{ZetaUr}$ and $\mathrm{SrcUr}$ in [ZetaUr.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/ZetaUr.lean#L13).

- `GlobalTheory.T.exists_ordinary_normal_form_unramified_source`, a second name for `GlobalTheory.Ord2.exists_nf_srcUr`. We have not opened its proof.
- `GlobalTheory.Ord2.es_vanish`.
- `UpperTheory.V.X.Kato.conj`, in [KatoConj.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LevelCohomology/KatoConj.lean#L7): an isomorphism of representations carries Bloch-Kato vanishing.

The helper `repIso_symm_srcL` only says that conjugacy of representations is symmetric; the "srcL" in its name has no role. $\mathrm{LitCoh}$ is used only inside `es_vanish`.
