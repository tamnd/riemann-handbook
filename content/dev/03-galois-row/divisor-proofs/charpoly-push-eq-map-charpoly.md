---
id: charpoly-push-eq-map-charpoly
title: The characteristic polynomial on de Rham homology over an algebraically closed field
kind: theorem
decl: GlobalTheory.DeRham.charpoly_push_eq_map_charpoly
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CharpolyDeRhamHomologyEndomorphismEqMapLadic
covers: 697
status: drafted
drafted_by: writer@claude
---
This lemma says that an endomorphism $f$ of an abelian variety over an algebraically closed field acts on de Rham homology with characteristic polynomial $P_f$, reduced into the field. It is the last step of [the de Rham characteristic polynomial from an l-adic lattice](/entry/charpoly-push-eq/). Its proof only splits by the characteristic of the field.

## Statement

Let $k$ be an algebraically closed field and $B$ an abelian variety over $k$ of dimension $g$: in the Lean structure `AbVar`, a commutative group scheme over $k$ that is an abelian scheme, smooth of relative dimension $g$. Let $f \in \operatorname{End}(B)$. Let $f_*$ be the action of $f$ on $H_1^{\mathrm{dR}}(B)$, the dual of the primitive part of $H^1_{\mathrm{dR}}(B/k)$, as in [the parent lemma](/entry/charpoly-push-eq/). Suppose $H_1^{\mathrm{dR}}(B)$ has finite dimension. Let $P_f \in \mathbb{Z}[X]$ be the characteristic polynomial of $f$: monic of degree $2g$, with $P_f(n) = \deg(n - f)$ for all $n \in \mathbb{Z}$.

**Theorem.** $\operatorname{charpoly}(f_* \mid H_1^{\mathrm{dR}}(B)) = P_f$ in $k[X]$.

## Proof

The characteristic of $k$ is a prime $p$ or $0$.

- If it is $p$, then $k$ is perfect, since it is algebraically closed. [The perfect field case](/entry/charpoly-de-rham-homology-abelian-variety-char-p/) gives the result. Its proof uses Dieudonné modules, see [the proof in characteristic p](/entry/charpoly-push/).
- If it is $0$, `T.charpoly_deRhamHomology_abelianVariety_charZero` gives the result. Its proof (`DeRhamCharpolyZero.charpoly_push`) descends $B$ and $f$ to a countable subfield $K$, embeds $K$ in $\mathbb{C}$, and uses the case $k = \mathbb{C}$ (`charpoly_push_complex`, which we have not opened).

## In the Lean code

The lemma is in [CharpolyDeRhamHomologyEndomorphismEqMapLadic.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyEndomorphismEqMapLadic.lean#L18). The proof uses `CharP.exists` and `CharP.char_is_prime_or_zero` from Mathlib, then one of:

- `GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charP`;
- `GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charZero`, in [CharpolyDeRhamHomologyAbelianVarietyCharZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharZero.lean#L210).

The instance that $k$ is perfect comes from Mathlib, by type class search. $P_f$ is `AbVar.charpoly f`. It is defined by choice: the chosen $P$ with the three properties if one exists, and $0$ if not. The characteristic $p$ lemma does not need $k$ algebraically closed, only perfect.
