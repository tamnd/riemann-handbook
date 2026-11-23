---
title: Gluing theta level objects over affine covers
decls:
  - GlobalTheory.ThetaAffineGlue.exists_glue
  - GlobalTheory.T.exists_thetaLevelAbelianScheme_glue_affineCover
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing theta level objects over affine covers

The theta families of [the section on theta families](/entry/nonempty-theta-fam/) are built locally: over each affine piece of a scheme of theta values one constructs a theta level object. This section proves that such local objects glue to one object over the whole scheme, if they agree on the overlaps. The key point is rigidity. A map between two theta level objects of level $N'^2$ over a [[reduced|ZXSN8D4MCB]] base is determined by the abelian schemes, the line bundles and the level points, so the local identifications satisfy the cocycle condition automatically. The result is used in the next section to build the open families of theta level objects. The background is [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures).

We use the bases of level $k$, the theta level objects and the maps of theta level objects of [the section on theta level objects](/entry/derivation-eq-zero-of-ks-zero/). Recall that a theta level object $t$ over $s : S \to \operatorname{Spec} o$ is an abelian scheme $A \to S$ of relative dimension $g$ with a principal polarization bundle $L$, a symplectic basis $P_1, \dots, P_{2g}$ of the $k$-torsion and endomorphisms $\alpha_j$ for $j \in J$. A map $t' \to t$ over $f : S' \to S$ is a morphism $\varphi : A' \to A$ that identifies $A'$ with $f^* A$ and respects $L$, the $P_i$ and the $\alpha_j$.

The classical form of rigidity is the following.

**Theorem 5.15.1 (Serre's rigidity lemma).** Let $X$ be an abelian variety over a field with a polarization, $n \ge 3$ an integer prime to the characteristic, and $\sigma$ an automorphism of $X$ that preserves the polarization and acts trivially on the $n$-torsion $X[n]$. Then $\sigma$ is the identity (D. Mumford, *Abelian Varieties*, §21).

Over a reduced base the same holds fibre by fibre, so it holds for the abelian scheme. The form used below is a statement in the chapter on theta level structures: two maps of theta level objects of level $N'^2$ over the same map of reduced affine bases, which agree on the level points, are equal. It needs an integer $m \ge 2$ with $m^2 \mid N'$ and $N'$ odd.

**Theorem 5.15.2 (Gluing over an affine cover).** Assume the laws and the second laws of abelian schemes. Let $o$ be a ring, $g \ge 0$, $N' \ge 0$, $J$ a set, $b$ a base of level $N'^2$ on $o$ and $m$ an integer. Let $S$ be a reduced scheme with $s : S \to \operatorname{Spec} o$, let $(R_i)_{i \in I}$ be rings with maps $x_i : \operatorname{Spec} R_i \to S$, and let $t_i$ be a theta level object of genus $g$ and level $N'^2$ over $s \circ x_i$. Assume:

1. $2 \le m$, $m^2 \mid N'$ and $N'$ is odd;
2. every $x_i$ is an [[open immersion|GFC5YKSN5H]];
3. every point of $S$ lies in the image of some $x_i$;
4. for all $i, i'$, every ring $T$, all maps $a : \operatorname{Spec} T \to \operatorname{Spec} R_i$ and $a' : \operatorname{Spec} T \to \operatorname{Spec} R_{i'}$ with $a$ an open immersion and $x_i \circ a = x_{i'} \circ a'$, and every theta level object $u$ over $s \circ x_i \circ a$: if there is a map $u \to t_i$ over $a$, then there is a map $u \to t_{i'}$ over $a'$.

Then there is a theta level object $t_0$ over $s$ with a map $t_i \to t_0$ over $x_i$ for every $i$.

Lean: `GlobalTheory.ThetaAffineGlue.exists_glue` (also `GlobalTheory.T.exists_thetaLevelAbelianScheme_glue_affineCover`, a second name).

Condition 4 is the agreement on overlaps. It is stated for affine opens of the overlaps, so that it can be checked on rings.

*Proof.* *Opens in place of rings.* Let $U_i \subseteq S$ be the open image of $x_i$, so that $x_i$ is an isomorphism $\operatorname{Spec} R_i \cong U_i$ followed by the inclusion. Theta level objects pull back along every map of schemes. So we pull $t_i$ back along the inverse isomorphism and get a theta level object $t'_i$ over $U_i$ with a map $t'_i \to t_i$. The $U_i$ cover $S$ by condition 3.

*Uniqueness of maps.* Let $V$ be a reduced scheme, $f : V \to S$ a map and $u$ a theta level object over $V$. Let $\varphi, \varphi' : A_u \to A_t$ be two maps that both identify $A_u$ with $f^* A_t$, with $L_u \cong \varphi^* L_t$ and $L_u \cong \varphi'^* L_t$, and with $\varphi \circ P^u_i = \varphi' \circ P^u_i$ for all $i$. Then $\varphi = \varphi'$. To prove this, cover $V$ by affine opens $\operatorname{Spec} R \to V$. Each $R$ is reduced, since an open subscheme of a reduced scheme is reduced. On $\operatorname{Spec} R$, the two maps differ by an automorphism $\psi$ of $A_u$ over $V$ that respects $L_u$ and the points $P^u_i$. Every point of $\operatorname{Spec} R$ is the image of its residue field, at which $u$ restricts to a theta level object with a map to $u$. So the set of such points is [[Dense|0BSJSX7ME2]], and the rigidity statement above, with $m \ge 2$, $m^2 \mid N'$ and $N'$ odd, gives $\psi = 1$ over $\operatorname{Spec} R$. Two maps that agree on an open cover agree.

*Maps are local.* Let $V$ be reduced, $u$ over $V$ and $t$ over $S$, and $f : V \to S$. Assume that every point of $V$ has an open neighbourhood $a : W \to V$ and a theta level object $v$ over $W$ with maps $v \to u$ over $a$ and $v \to t$ over $f \circ a$. Then there is a map $u \to t$ over $f$. The local maps $u|_W \to t$ agree on the overlaps by the uniqueness of maps, since they come from maps of the same objects that respect $L$ and the points. So they glue to a morphism $A_u \to A_t$, and the properties of a map can be checked on the cover.

*Overlaps.* Fix $i, j$. Pull $t'_i$ back to $U_i \cap U_j$ and call it $u$. Then $u \to t'_i$ is a map. We show that there is a map $u \to t'_j$. Let $p$ be a point of $U_i \cap U_j$ and $a : \operatorname{Spec} T \to U_i \cap U_j$ an affine open neighbourhood. Pull $u$ back along $a$ to $v$. Composing maps gives $v \to t'_i \to t_i$ over a map $\operatorname{Spec} T \to \operatorname{Spec} R_i$, which is an open immersion. Condition 4 gives a map $v \to t_j$ over a map $\operatorname{Spec} T \to \operatorname{Spec} R_j$. Since $t'_j \to t_j$ is a map over an isomorphism, the map $v \to t_j$ factors through a map $v \to t'_j$. So $u \to t'_j$ exists locally, and it exists globally by the previous step, since $U_i \cap U_j$ is reduced.

*Gluing.* A lemma on gluing over open covers states: if the $U_i$ cover $S$, if on each $U_i \cap U_j$ there is an object with maps to $t'_i$ and $t'_j$, and if maps into each $t'_i$ over open immersions are unique in the sense above, then there is $t_0$ over $S$ with maps $t'_i \to t_0$ over the inclusions $U_i \subseteq S$. The uniqueness hypothesis holds by the second step, since an open subscheme of $S$ is reduced. Let $t_0$ be the glued object.

*Back to rings.* The map $t'_i \to t_i$ is over an isomorphism, so it has an inverse $t_i \to t'_i$ over $\operatorname{Spec} R_i \cong U_i$. The composite $t_i \to t'_i \to t_0$ is a map over $x_i$. $\square$

**Remark 5.15.3.** The integer $m$ only enters the rigidity statement. Since $N'$ is odd, $m \ge 3$, and so $N'^2$ is divisible by $m^2 \ge 9$. The level of the objects is $N'^2$, which is the level of the theta values in the earlier sections. Without the hypothesis that $S$ is reduced, the uniqueness of maps can fail, since rigidity is proved on fibres.

**Remark 5.15.4 (Formalization).** The theorem is proved in [ExistsThetaLevelAbelianSchemeGlueAffineCover.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaLevelAbelianSchemeGlueAffineCover.lean#L266). The uniqueness of maps is `unique` (line 199), which reduces to `unique_affine` (line 180), and that one applies `GlobalTheory.T.thetaLevel_iso_unique_of_dense_common_fibres`. The locality of maps is `tMap_of_local` (line 215). The gluing lemma is `GlobalTheory.T.exists_thetaLevelAbelianScheme_glue_openCover`, and pullbacks come from `GlobalTheory.tObj_pull`. The integer $m$ and the hypotheses $2 \le m$, $m^2 \mid N'$ and $N'$ odd are passed only to the rigidity lemma; the theorem does not use them anywhere else. The laws and the second laws are also used only there. We followed the statements of the rigidity and gluing lemmas and did not open their proofs. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
