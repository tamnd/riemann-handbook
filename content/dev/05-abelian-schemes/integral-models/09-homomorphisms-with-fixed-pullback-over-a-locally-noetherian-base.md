---
title: Homomorphisms with fixed pullback over a locally noetherian base
decls:
  - GlobalTheory.HomFixLocal.exists_local_homFixRep
  - GlobalTheory.T.exists_local_representing_scheme_homFixedPullback
  - GlobalTheory.HomFixAff.exists_homFixRep_finiteType
  - GlobalTheory.T.exists_finiteType_scheme_representing_polarizedHoms
  - GlobalTheory.HomFixGlue.homFix_finiteType
  - GlobalTheory.T.exists_finiteType_representing_polarizedHoms_locNoeth
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Homomorphisms with fixed pullback over a locally noetherian base

This section proves that homomorphisms with fixed pullback have a representing scheme over every locally noetherian base, when both line bundles are rigidified and relatively ample. The representing map is quasi-compact, separated and locally of finite type. The previous section gives such a scheme over $\operatorname{Spec} R$ with $R$ noetherian, under two extra assumptions: a fixed power $M^k$ is very ample, and $L^k$ and $M^k$ have base-change-stable bases. Here we show that both assumptions hold on the members of an open cover of $\operatorname{Spec} R$, and then we glue, first over $\operatorname{Spec} R$ and then over a locally noetherian scheme. The next section proves that the representing map is finite. We keep the notation of the previous section: test data, maps of test data, representing schemes, rigidified, very ample and relatively ample line bundles, and base-change-stable bases.

### Inputs

We use the following results. Let $R$ be a ring and $S = \operatorname{Spec} R$.

1. (A uniform very ample power.) Let $B$ be an abelian scheme over $S$ and $M$ a relatively ample line bundle on $B$. Then there is $k \geq 1$ with this property. For every ring map $R \to R'$ and every group pullback $\varphi_{B'} : B' \to B$ along $\operatorname{Spec} R' \to S$, the line bundle $\varphi_{B'}^* M$ on $B'$ is very ample of degree $k$.
2. ([Local bases of sections](/entry/exists-basic-open-base-change-stable-section-basis/).) Let $R$ be noetherian, $A$ an abelian scheme over $S$, $L$ a rigidified, relatively ample line bundle on $A$, and $k \geq 1$. For every $p \in S$ there is $f \in R$ with $p \in D(f)$ such that the following holds. For every $g \in R$ with $D(g) \subseteq D(f)$ and every group pullback $\varphi : A_g \to A$ along $\operatorname{Spec} R_g \to S$, the line bundle $(\varphi^* L)^k$ on $A_g$ has a base-change-stable basis.
3. (Basic open sets.) Let $A$ and $B$ be group schemes over $S$ with line bundles $L$ and $M$, and let $f \in R$. Assume that for all group pullbacks $\varphi_A : A_f \to A$ and $\varphi_B : B_f \to B$ along $\operatorname{Spec} R_f \to S$, homomorphisms from $(A_f, \varphi_A^* L)$ to $(B_f, \varphi_B^* M)$ with fixed pullback have a representing scheme whose map is quasi-compact, separated and locally of finite type. Then the same holds for some group pullbacks of $A$ and $B$ along the inclusion of the open subscheme $D(f)$.
4. (Pullback.) Let $\varphi : A' \to A$ be a group pullback along any map $S' \to S$ of schemes, with $A$ an abelian scheme and $L$ a rigidified, relatively ample line bundle on $A$. Then $A'$ is an abelian scheme and $\varphi^* L$ is a rigidified, relatively ample line bundle on $A'$.

Result 3 holds because the open subscheme $D(f)$ of $S$ is isomorphic to $\operatorname{Spec} R_f$ over $S$, and a representing scheme can be moved along this isomorphism.

For the gluing we use three more results. Let $S$ be a scheme.

5. (Gluing over an open cover.) Let $S$ be locally noetherian, let $A$ and $B$ be abelian schemes over $S$, and let $L$ and $M$ be rigidified line bundles on $A$ and $B$. Let $(U_j)$ be an open cover of $S$. Assume that for every $j$ there are group pullbacks $A_j \to A$ and $B_j \to B$ along the inclusion $U_j \to S$ such that homomorphisms from $(A_j, L|_{A_j})$ to $(B_j, M|_{B_j})$ with fixed pullback have a representing scheme whose map is quasi-compact, separated and locally of finite type. Then homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback have a representing scheme with the same three properties.
6. (Gluing along open immersions.) Assume the following statement. *For every scheme $H$, every homomorphism $\Phi : A \to B$ of abelian schemes over $H$ and all rigidified line bundles $L$ on $A$ and $M$ on $B$, if every point of $H$ has an open neighbourhood $W$ such that $L$ and $\Phi^* M$ are isomorphic over the inverse image of $W$, then $L \cong \Phi^* M$.* Then the conclusion of result 5 holds for every scheme $S$ and for every family of open immersions $V_j \to S$ whose images cover $S$ in place of the open cover $(U_j)$.
7. (Isomorphism is local for rigidified bundles.) The statement in italics in result 6 holds.
8. (Restriction to an open subscheme.) Let $A$ be an abelian scheme over $S$ with a rigidified, relatively ample line bundle $L$, and let $V \to S$ be an open immersion. Then there is a group pullback $\varphi : A_V \to A$ along $V \to S$, and $A_V$ is an abelian scheme with the rigidified, relatively ample line bundle $\varphi^* L$.

Here is why results 5 to 7 hold. A representing scheme over $U_j$ is unique up to a unique isomorphism, so the representing schemes over $U_j$ and $U_{j'}$ agree over $U_j \cap U_{j'}$, and they glue. The glued scheme represents the functor $T \mapsto \{\Phi' : A_T \to B_T \text{ with } \Phi'^* M_T \cong L_T\}$ because this functor is a Zariski sheaf. Homomorphisms glue, so the only point is that the condition $\Phi'^* M_T \cong L_T$ is local on $T$, and this is result 7. For result 7, an isomorphism $L \cong \Phi^* M$ can be scaled to respect the rigidifications at the zero section. A scaled isomorphism is unique, because a function on an abelian scheme that is $1$ along the zero section is $1$. So the scaled local isomorphisms agree on overlaps and glue.

### The representing scheme

**Theorem 8.9.1 (Local representing schemes).** Let $R$ be a noetherian ring and $S = \operatorname{Spec} R$. Let $A$ and $B$ be abelian schemes over $S$ with rigidified, relatively ample line bundles $L$ on $A$ and $M$ on $B$. Then for every $p \in S$ there are an open set $U \ni p$, group pullbacks $\varphi_A : A_U \to A$ and $\varphi_B : B_U \to B$ along the inclusion $U \to S$, and a representing scheme $\pi : H \to U$ for homomorphisms from $(A_U, \varphi_A^* L)$ to $(B_U, \varphi_B^* M)$ with fixed pullback, such that $\pi$ is quasi-compact, separated and locally of finite type.

Lean: `GlobalTheory.HomFixLocal.exists_local_homFixRep` (also `GlobalTheory.T.exists_local_representing_scheme_homFixedPullback`, a second name).

*Proof.* Result 1, applied to $B$ and $M$, gives $k \geq 1$. Result 2, applied to $(A, L)$, $k$ and $p$, gives $f_1 \in R$ with $p \in D(f_1)$. Result 2, applied to $(B, M)$, $k$ and $p$, gives $f_2$ with $p \in D(f_2)$. Let $f = f_1 f_2$ and $U = D(f) = D(f_1) \cap D(f_2)$, so $p \in U$. By result 3 it is enough to give a representing scheme over $\operatorname{Spec} R_f$, with the three properties, for arbitrary group pullbacks $\varphi_A : A_f \to A$ and $\varphi_B : B_f \to B$ along $\operatorname{Spec} R_f \to S$.

Let $L_f = \varphi_A^* L$ and $M_f = \varphi_B^* M$. By result 4, $A_f$ and $B_f$ are abelian schemes, $L_f$ and $M_f$ are rigidified, and $L_f$ is relatively ample. By result 1, applied to the ring map $R \to R_f$, the line bundle $M_f$ is very ample of degree $k$. As $D(f) \subseteq D(f_1)$ and $D(f) \subseteq D(f_2)$, result 2 gives base-change-stable bases of $L_f^k$ and $M_f^k$. The ring $R_f$ is noetherian, as a localization of a noetherian ring. So the [Theorem 8.8.8](/entry/exists-hom-fix-rep-of-sec-bases/) on representing schemes from bases of sections applies to $(A_f, L_f)$, $(B_f, M_f)$ and $k$. It gives the representing scheme. $\square$

The choice of $k$ is the key point of the proof. It comes from $B$ alone, and result 1 makes it uniform over all base changes. Then result 2 is applied twice with the same $k$, once to $A$ and once to $B$.

**Theorem 8.9.2 (Representing scheme over a noetherian ring).** Let $R$ be a noetherian ring and $S = \operatorname{Spec} R$. Let $A$ and $B$ be abelian schemes over $S$ with rigidified, relatively ample line bundles $L$ on $A$ and $M$ on $B$. Then homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback have a representing scheme $\pi : H \to S$ such that $\pi$ is quasi-compact, separated and locally of finite type.

Lean: `GlobalTheory.HomFixAff.exists_homFixRep_finiteType` (also `GlobalTheory.T.exists_finiteType_scheme_representing_polarizedHoms`, a second name).

*Proof.* For every $p \in S$ the theorem on local representing schemes gives an open set $U_p \ni p$ with the data that result 5 asks for. The sets $U_p$ cover $S$, and $S$ is noetherian, so result 5 gives the representing scheme. $\square$

**Theorem 8.9.3 (Representing scheme over a locally noetherian base).** Let $S$ be a locally noetherian scheme. Let $A$ and $B$ be abelian schemes over $S$ with rigidified, relatively ample line bundles $L$ on $A$ and $M$ on $B$. Then homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback have a representing scheme $\pi : H \to S$ such that $\pi$ is quasi-compact, separated and locally of finite type.

Lean: `GlobalTheory.HomFixGlue.homFix_finiteType` (also `GlobalTheory.T.exists_finiteType_representing_polarizedHoms_locNoeth`, a second name).

*Proof.* We apply result 6. Its hypothesis in italics is result 7. For the family of open immersions we take, for each affine open $U \subseteq S$, the canonical open immersion $\operatorname{Spec} \Gamma(S, U) \to S$ with image $U$. Every point of $S$ has an affine open neighbourhood, so the images cover $S$. Fix an affine open $U$. As $S$ is locally noetherian, the ring $\Gamma(S, U)$ is noetherian. Result 8 gives group pullbacks $A_U \to A$ and $B_U \to B$ along $\operatorname{Spec} \Gamma(S, U) \to S$ such that $A_U$ and $B_U$ are abelian schemes with rigidified, relatively ample line bundles $L_U$ and $M_U$. The theorem on representing schemes over a noetherian ring, for $(A_U, L_U)$ and $(B_U, M_U)$, gives a representing scheme with the three properties. Now result 6 gives the representing scheme over $S$. $\square$

**Remark 8.9.4 (Formalization).** The open set of the local theorem is a basic open set $D(f_1 f_2)$, and the exponent $k$ comes from $B$ alone: [ExistsLocalRepresentingSchemeHomFixedPullback.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLocalRepresentingSchemeHomFixedPullback.lean#L22). After the base change to $R_f$, the relative ampleness of $M_f$ is computed and then dropped, since the theorem of the previous section needs only that $M_f$ is very ample: [ExistsLocalRepresentingSchemeHomFixedPullback.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLocalRepresentingSchemeHomFixedPullback.lean#L36). The gluing result 6 takes the local-to-global statement of result 7 as a hypothesis, and the proof passes result 7 to it: [ExistsFiniteTypeRepresentingPolarizedHomsLocNoet.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteTypeRepresentingPolarizedHomsLocNoet.lean#L19). The module name of this theorem ends in "LocNoet", while its second name ends in "locNoeth". Results 5 and 6 are two forms of one gluing statement, one for open sets with a noetherian base and one for open immersions with any base. We read the statements of results 1 to 8, not their proofs, and the reasons given above for results 3 and 5 to 7 are ours.
