---
id: charpoly-push
title: The characteristic polynomial on de Rham homology, by Dieudonné modules
kind: theorem
decl: GlobalTheory.DeRhamCharpolyP.charpoly_push
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CharpolyDeRhamHomologyAbelianVarietyCharP
covers: 669
status: drafted
drafted_by: writer@claude
---
This theorem proves that, over a perfect field of characteristic $p$, an endomorphism $f$ of an abelian variety acts on de Rham homology with characteristic polynomial $P_f \bmod p$. It is the proof of [the statement in characteristic p](/entry/charpoly-de-rham-homology-abelian-variety-char-p/), which goes into [the algebraically closed case](/entry/charpoly-push-eq-map-charpoly/). The proof passes through the Dieudonné module of the $p$-divisible group of the abelian variety.

## Statement

Let $p$ be a prime, $k$ a perfect field of characteristic $p$, $B$ an abelian variety over $k$ of dimension $g$, and $f \in \operatorname{End}(B)$. Let $f_*$ act on $H_1^{\mathrm{dR}}(B)$, the dual of the primitive part of $H^1_{\mathrm{dR}}(B/k)$, and suppose this space has finite dimension. Let $P_f \in \mathbb{Z}[X]$ be monic of degree $2g$ with $P_f(n) = \deg(n - f)$ for $n \in \mathbb{Z}$.

**Theorem.** $\operatorname{charpoly}(f_* \mid H_1^{\mathrm{dR}}(B)) = P_f \bmod p$.

## Proof

Let $W = W(k)$ be the Witt vectors of $k$.

1. **The $p$-divisible group.** `AVTower.exists_tower` gives a $p$-divisible group $G$ over $k$ of height $2g$ and a torsion tower $t$: maps $G_n \to B$ that identify $G_n$ with $B[p^n]$. Then $f$ induces $t(f) \colon G \to G$.
2. **The Dieudonné module.** Let $M$ be the contravariant Dieudonné functor of [the Dieudonné theory](/entry/theory/). $M(G)$ is a free $W$-module of finite rank. `Dieu.CharpolyAV.charpoly_map_eq` gives $\operatorname{charpoly}(M(t(f)) \mid M(G)) = P_f$ in $W[X]$. Its proof compares $|\det M(R(f))|_p$ with $|\deg R(f)|_p$ for each $R \in \mathbb{Z}[X]$.
3. **Reduction mod $p$.** The theory has a surjective semilinear map $\mathrm{red} \colon M(G) \to \operatorname{RigExt}(G)$ over $W \to k$ with kernel $pM(G)$, and it carries $M(t(f))$ to the action of $t(f)$ on $\operatorname{RigExt}(G)$. Here $\operatorname{RigExt}(G)$ is a quotient of pairs (a 2-cocycle, an invariant differential), the rigidified extensions of $G$ by $\mathbb{G}_a$ in the sense of Mazur and Messing (LNM 370, 1974). The algebra lemma `charpoly_of_red` then says that $\operatorname{RigExt}(G)$ has finite dimension and that its characteristic polynomial is the reduction of the one on $M(G)$.
4. **De Rham cohomology.** `deRhamVectorExtension` gives a natural isomorphism $e$ from the primitive part of $H^1_{\mathrm{dR}}(B)$ to $\operatorname{RigExt}(G)$. Naturality (`Family.Natural.primPull`) gives $e \circ f^* = t(f) \circ e$. So $f^*$ and $t(f)$ have the same characteristic polynomial.
5. **Duality.** $f_*$ is the dual of $f^*$, and `charpoly_dualMap` says that the dual map has the same characteristic polynomial.

The chain of equalities in step 1 to 5 gives the theorem. The rest is bookkeeping with `Polynomial.map_map`.

## In the Lean code

The theorem is in [CharpolyDeRhamHomologyAbelianVarietyCharP.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharP.lean#L81). It calls:

- `GlobalTheory.AVTower.exists_tower`;
- `GlobalTheory.Dieu.theory p` and its fields `base.free`, `base.finite`, `base.red_surjective`, `base.red_eq_zero`, `base.red_smap`;
- `GlobalTheory.Dieu.CharpolyAV.charpoly_map_eq`;
- `charpoly_of_red` and `charpoly_dualMap`, in the same file ([L18](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharP.lean#L18), [L68](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharP.lean#L68));
- `GlobalTheory.deRhamVectorExtension`, a proof of the literature statement `Published.DeRhamVectorExtension` from `T.abelianScheme_deRham_locallyFree_hodgeDegenerates`.

The surjectivity of $W \to k$ comes from the Teichmüller lift. The `Filtered` and `Tangent` parts of `deRhamVectorExtension` are not used here. The isomorphism of $H^1_{\mathrm{dR}}$ with the Dieudonné module mod $p$ is in Oda (Ann. Sci. ENS 2, 1969); the Lean proof gets it from steps 3 and 4.
