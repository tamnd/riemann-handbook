---
id: charpoly-push-eq
title: The de Rham characteristic polynomial from an l-adic lattice
kind: theorem
decl: GlobalTheory.DeRham.charpoly_push_eq
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CharpolyDeRhamHomologyEndomorphismEqMapLadic
covers: 705
status: drafted
drafted_by: writer@claude
---
This lemma says that an endomorphism of an abelian variety has the same characteristic polynomial on de Rham homology as on a lattice that models its $\ell$-power torsion. It is the proof of [the de Rham and l-adic characteristic polynomials agree](/entry/charpoly-de-rham-homology-endomorphism-eq-map-ladic/), which has the same statement. That result sits below the [six facts about the Kuga-Sato tower](/entry/kodaira-spencer-of-weight-one/). The work is done in [the next lemma](/entry/charpoly-push-eq-map-charpoly/).

## Statement

Let $k$ be an algebraically closed field and $A$ a commutative group scheme over $k$ that is an abelian scheme. For $f \colon A \to A$ a homomorphism, let $f^*$ act on the primitive classes of $H^1_{\mathrm{dR}}(A/k)$, the classes $c$ with $\mu^* c = \mathrm{pr}_1^* c + \mathrm{pr}_2^* c$. Let $H_1^{\mathrm{dR}}(A)$ be the dual of this space and $f_*$ the dual of $f^*$. Suppose $H_1^{\mathrm{dR}}(A)$ has finite dimension.

Let $L$ be a free $\mathbb{Z}$-module of finite rank, $\varphi \in \operatorname{End}_\mathbb{Z}(L)$, and $\ell$ a prime with $\ell \neq 0$ in $k$. For each $j \geq 0$ let $\mathrm{ev}_j \colon L \to A(k)$ be a map such that:

1. $\mathrm{ev}_j$ is a group homomorphism;
2. $\mathrm{ev}_j(\varphi x) = f(\mathrm{ev}_j x)$;
3. $\mathrm{ev}_j(x) = 0$ if and only if $x \in \ell^j L$;
4. the image of $\mathrm{ev}_j$ is $A[\ell^j](k)$.

So $\mathrm{ev}_j$ gives $L/\ell^j L \cong A[\ell^j](k)$, compatible with $\varphi$ and $f$.

**Theorem.** $\operatorname{charpoly}(f_* \mid H_1^{\mathrm{dR}}(A))$ is the image in $k[X]$ of $\operatorname{charpoly}(\varphi \mid L) \in \mathbb{Z}[X]$.

## Proof

1. `AV.exists_smoothOfRelativeDimension_of_isAbelianScheme` gives $g$ with $A$ smooth of relative dimension $g$. So $A$ is an abelian variety $B$ in the sense of the Lean structure `AbVar`.
2. `T.l_power_torsion_endomorphism_evaluation` gives $\operatorname{charpoly}(\varphi) = P_f$. Here $P_f$ is `AbVar.charpoly f`: the monic $P \in \mathbb{Z}[X]$ of degree $2g$ with $P(n) = \deg(n - f)$ for all $n \in \mathbb{Z}$, as in Mumford (Abelian Varieties, §19).
3. [The algebraically closed case](/entry/charpoly-push-eq-map-charpoly/) gives $\operatorname{charpoly}(f_*) = P_f$ in $k[X]$.

## In the Lean code

The lemma is in [CharpolyDeRhamHomologyEndomorphismEqMapLadic.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyEndomorphismEqMapLadic.lean#L29). It calls:

- `GlobalTheory.AV.exists_smoothOfRelativeDimension_of_isAbelianScheme`;
- `GlobalTheory.T.l_power_torsion_endomorphism_evaluation`, an alias of `AV.AbVar.charpoly_eq_lattice_model`, which we have not opened;
- `charpoly_push_eq_map_charpoly`.

$H_1^{\mathrm{dR}}$ is `HdR A`, the dual of `primDR A`, and $f_*$ is `push (dp0 k) (𝟙 _) f`. The first cohomology is `Cris.H1` with the zero divided power structure; we have not unfolded it further. The finiteness hypothesis is always true: `DeRhamCharpolyZero.finite_HdR` proves it for each `AbVar`. The maps $\mathrm{ev}_j$ need not be compatible as $j$ varies.
