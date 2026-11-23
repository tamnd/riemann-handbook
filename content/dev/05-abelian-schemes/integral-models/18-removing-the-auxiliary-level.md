---
title: Removing the auxiliary level
decls:
  - GlobalTheory.HTQuot.exists_representing_family_of_level_structure
  - GlobalTheory.T.exists_representingFamily_of_auxiliaryRepresentation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Removing the auxiliary level

This section proves result 3 of Section 8.1: if $b$ has representable auxiliary level $(N, h, M)$, then there is a representing family of level $N$ over $b$ whose map to $\operatorname{Spec} R$ is quasi-projective. The scheme $X$ that represents objects with a symplectic level $M$ structure carries an action of the group of symplectic similitudes of $(\mathbb{Z}/M)^{2h}$, which changes the level structure. The action is free on geometric points, so the quotient $X \to Y$ is a Galois cover. The universal object descends to $Y$, and $Y$ represents objects of level $N$ without a level structure. With result 2 of Section 8.1, which the [previous section](/entry/harris-taylor-moduli-symplectic-level-representable/) proves, this gives the theorem on quasi-projective representing families.

Throughout, $D$ is a datum for $p$, $b$ is a base for $D$ over a ring $R$, $N \geq 3$ is prime to $p$, and $h = \lfloor \operatorname{rk} \Lambda / 2 \rfloor$.

### Similitudes and Galois covers

**Definition 8.18.1 (Symplectic similitudes).** Let $M \geq 1$. The group $G_{h, M}$ consists of the $\mathbb{Z}/M$-linear automorphisms $g$ of $(\mathbb{Z}/M)^{2h}$ for which there is a unit $\mu \in (\mathbb{Z}/M)^\times$ with $\langle gx, gy \rangle = \mu \langle x, y \rangle$ for all $x$ and $y$. Here $\langle \cdot, \cdot \rangle$ is the standard symplectic form of Section 8.1, taken modulo $M$.

Lean: `GlobalTheory.UPel.HT.sympSimGrp`.

**Definition 8.18.2 (Galois cover).** Let $G$ be a group and $\rho : G \to \operatorname{End}(X)$ with $\rho(1) = \operatorname{id}$ and $\rho(ac) = \rho(c) \circ \rho(a)$. A map $\pi : X \to Y$ is a *Galois cover* with group $G$ if $G$ is finite, $\pi \rho(a) = \pi$ for every $a$, $\pi$ is [[finite|N9C4X7XKE4]], [[étale|H84VHC8PX2]] and surjective, and for every algebraically closed field $k$ and all $y, y' : \operatorname{Spec} k \to X$ with $\pi y = \pi y'$ there is a unique $a$ with $\rho(a) y = y'$.

Lean: `GlobalTheory.ZM.IsGaloisCover`.

### Inputs

We use the following results. Let $(X, s, s_1, u, \lambda_u)$ be as in the definition of representable auxiliary level (Section 8.1), and write $G = G_{h, M}$.

1. (The action.) If $M > 0$, there is $\rho : G \to \operatorname{End}(X)$ with $\rho(1) = \operatorname{id}$, $\rho(ac) = \rho(c)\rho(a)$ and $s \rho(a) = s$, such that for every $a$ there is a map of objects $u \to u$ over $\rho(a)$. It changes $\lambda_u$ by $a$ and $s_1$ by an automorphism of $B_M$.
2. (Freeness.) If $M > 0$ and $\rho(a) y = y$ for a geometric point $y$ of $X$, then $a = 1$.
3. (Level structures exist on a Galois cover.) Let $M \geq 3$ be odd and prime to $p$, and $e$ prime to $p$ and to $M$ with $E(\Lambda, -) \supseteq e\Lambda^\vee$. For every object $o$ of level $N$ over $t : T \to \operatorname{Spec} R$ there are a Galois cover $\pi_1 : T_1 \to T$ with group $G$ and action $\rho_1$, a map $y : T_1 \to X$ with $y \rho_1(a) = \rho(a) y$ and $s y = t \pi_1$, and an object $o'$ over $t \pi_1$ with maps of objects $o' \to o$ over $\pi_1$ and $o' \to u$ over $y$.
4. (Classifying maps differ locally by $G$.) Let $M \geq 3$ be odd and prime to $p$. Let $o$ be an object over $t : T \to \operatorname{Spec} R$ and $x, x' : T \to X$ with $s x = s x' = t$ and maps of objects $o \to u$ over $x$ and over $x'$. Then every point of $T$ has an open neighbourhood $V$ with some $a \in G$ such that $\rho(a) x = x'$ on $V$.
5. (Quotients.) Let $R$ be [[noetherian|0670T59HGE]], $X \to \operatorname{Spec} R$ quasi-projective, and $G$ finite acting over $\operatorname{Spec} R$ and freely on geometric points. Then there are a Galois cover $\pi : X \to Y$ with group $G$ and $s_Y : Y \to \operatorname{Spec} R$ [[separated|X30G4V7VAJ]] and [[locally of finite type|AHTE5DVX61]] with $s_Y \pi = s$. If $\pi$ is a Galois cover, $s_Y$ is separated and locally of finite type, and $s_Y \pi$ is quasi-projective, then $s_Y$ is quasi-projective.
6. (Galois covers.) Let $\pi : X \to Y$ be a Galois cover. A map $f : X \to Z$ with $f \rho(a) = f$ for all $a$ is $f' \pi$ for a unique $f' : Y \to Z$. If $g : S \to Y$ and $h_1, h_2 : S \to Z$ agree after composition with $S \times_Y X \to S$ locally on $S \times_Y X$, then $h_1 = h_2$.
7. (Maps of objects.) Two maps of objects over the same map of bases have the same underlying map, and a map of objects $o \to o$ over the identity is the identity. Maps of objects over $f$ and $g$ compose to a map over $g f$. If there are maps $o_1 \to o_3$ over $g f$ and $o_2 \to o_3$ over $g$, there is a map $o_1 \to o_2$ over $f$. Every object has a pullback along every map, with a map of objects to it.
8. (Descent of the data.) Let $R$ be noetherian, $\pi : X \to Y$ a Galois cover and $A$ an abelian scheme over $X$, quasi-projective over $R$, with group pullbacks $\nu_a : A \to A$ along $\rho(a)$ such that $\nu_1 = \operatorname{id}$ and $\nu_{ac} = \nu_c \nu_a$. Then $A$ descends to an abelian scheme $A_0$ over $Y$ with a group pullback $A \to A_0$ along $\pi$. An action of $O$, a line bundle on $A \times A$ with its two trivializations, its symmetry, the relative ampleness of its diagonal and the integer killing its kernel, the Rosati condition, a level map, the Lie and rank conditions, and the Tate condition descend with $A$ when they are compatible with the $\nu_a$.
9. (Quasi-projectivity of $A$.) If $R$ is noetherian, $X \to \operatorname{Spec} R$ is quasi-projective and $A$ over $X$ has a relatively ample line bundle, then $A \to \operatorname{Spec} R$ is quasi-projective.
10. (Moduli maps descend.) Let $\pi_1 : T_1 \to T$ be a Galois cover, $f : T \to Y$, and $o' \to o$ a map of objects over $\pi_1$. If there is a map of objects $o' \to u_Y$ over $f \pi_1$, then there is one $o \to u_Y$ over $f$.

### Two lemmas

**Lemma 8.18.3 (Descent of objects).** Let $R$ be noetherian, $\pi : X \to Y$ a Galois cover with group $G$, and $s_Y : Y \to \operatorname{Spec} R$ with $s_Y$ and $s_Y \pi$ quasi-projective. Let $o$ be an object of level $N$ over $s_Y \pi$ with a map of objects $o \to o$ over $\rho(a)$ for every $a$. Then there is an object $o_Y$ over $s_Y$ with a map of objects $o \to o_Y$ over $\pi$.

Lean: `GlobalTheory.HTQuot.obj_descends_galoisCover`.

*Proof.* Choose maps of objects $m_a : o \to o$ over $\rho(a)$ and let $\nu_a$ be the underlying maps. By result 7, $\nu_1 = \operatorname{id}$. The composite of $m_a$ and $m_c$ is a map over $\rho(ac)$, so $\nu_{ac} = \nu_c \nu_a$ by uniqueness. The bundle $\Delta^* P_o$ is relatively ample, so $A_o$ is quasi-projective over $R$ by result 9. Result 8 descends $A_o$ and all the data of $o$ to $Y$. They form an object $o_Y$, and the descent maps form a map of objects $o \to o_Y$ over $\pi$. $\square$

**Lemma 8.18.4 (A representing family from a level cover).** Let $R$ be noetherian, $s : X \to \operatorname{Spec} R$ quasi-projective and $u$ an object of level $N$ over $s$. Let $G$ be a finite group and $\rho$ an action of $G$ on $X$ over $\operatorname{Spec} R$ that is free on geometric points, with a map of objects $u \to u$ over each $\rho(a)$. Suppose that the conclusions of results 3 and 4 hold for $X$, $s$, $u$ and $\rho$. Then there is a representing family of level $N$ over $b$ whose map to $\operatorname{Spec} R$ is quasi-projective.

Lean: `GlobalTheory.HTQuot.exists_repFam_of_levelCover`.

*Proof.* Result 5 gives a Galois cover $\pi : X \to Y$ with $s_Y$ quasi-projective. The lemma on descent gives $u_Y$ over $s_Y$ and a map of objects $u \to u_Y$ over $\pi$.

Let $o$ be an object over $s' : S \to \operatorname{Spec} R$. Take $\pi_1 : S_1 \to S$, $y$ and $o'$ as in result 3. As $\pi y \rho_1(a) = \pi \rho(a) y = \pi y$, result 6 gives a unique $f : S \to Y$ with $f \pi_1 = \pi y$. Then $s_Y f \pi_1 = s y = s' \pi_1$, and the uniqueness in result 6 gives $s_Y f = s'$. The maps $o' \to u$ over $y$ and $u \to u_Y$ over $\pi$ compose to a map over $f \pi_1$. Result 10 gives a map of objects $o \to u_Y$ over $f$.

Let $f' : S \to Y$ with $s_Y f' = s'$ and a map of objects $o \to u_Y$ over $f'$. By composition there is a map $o' \to u_Y$ over $f' \pi_1$. Let $W = S_1 \times_Y X$, formed with $f' \pi_1$ and $\pi$, with projections $q_1$ and $q_2$, and let $o_W$ be a pullback of $o'$ along $q_1$. There is a map $o_W \to u$ over $y q_1$. There is a map $o_W \to u_Y$ over $f' \pi_1 q_1 = \pi q_2$, so cancellation against $u \to u_Y$ gives a map $o_W \to u$ over $q_2$. Both $y q_1$ and $q_2$ lie over $s' \pi_1 q_1$. By result 4, every point of $W$ has a neighbourhood on which $\rho(a) y q_1 = q_2$ for some $a$. There $\pi y q_1 = \pi \rho(a) y q_1 = \pi q_2 = f' \pi_1 q_1$. By result 6, $\pi y = f' \pi_1$, and the uniqueness of $f$ gives $f' = f$. $\square$

### The theorem

**Theorem 8.18.5 (Removing the auxiliary level).** Let $R$ be noetherian. Let $M \geq 3$ be odd and prime to $p$, and let $e$ be prime to $p$ and to $M$ with $E(\Lambda, -) \supseteq e\Lambda^\vee$. If $b$ has representable auxiliary level $(N, h, M)$, then there is a representing family of level $N$ over $b$ whose map to $\operatorname{Spec} R$ is quasi-projective.

Lean: `GlobalTheory.HTQuot.exists_representing_family_of_level_structure` (also `GlobalTheory.T.exists_representingFamily_of_auxiliaryRepresentation`, a second name).

*Proof.* Let $(X, s, s_1, u, \lambda_u)$ represent the auxiliary level, with $s$ quasi-projective. As $M > 0$, result 1 gives an action $\rho$ of $G = G_{h, M}$ on $X$ over $\operatorname{Spec} R$ with maps of objects $u \to u$ over each $\rho(a)$, and result 2 shows that it is free on geometric points. The group $G$ is finite, because $(\mathbb{Z}/M)^{2h}$ is finite. Results 3 and 4 hold under the hypotheses on $M$ and $e$. The lemma on representing families from a level cover gives the claim. $\square$

The level structure is used only as a tool. The quotient forgets it, and result 3 shows that every object of level $N$ acquires a level structure after a Galois cover with group $G$.

**Remark 8.18.6 (Formalization).** The theorem is [ExistsRepresentingFamilyOfAuxiliaryRepresentatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepresentingFamilyOfAuxiliaryRepresentatio.lean#L178), and the two lemmas are in the same file at [L63](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepresentingFamilyOfAuxiliaryRepresentatio.lean#L63) and [L117](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepresentingFamilyOfAuxiliaryRepresentatio.lean#L117). The group is defined in [HarrisTaylorSymplecticLevelFamilyUniversalProper.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorSymplecticLevelFamilyUniversalProper.lean#L13), and the properties of the action in result 1 are collected at L62 of that file. The Galois cover is [IsGaloisCover.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsGaloisCover.lean#L36); its action is a right action, $\rho(ac) = \rho(c)\rho(a)$. The integer $e$, the condition on $E$ and $\gcd(M, e) = 1$ are used only by result 3. Result 5 also gives that $s_Y$ is quasi-compact, which is not used. The second name is a wrapper that tries three forms of one proof term under a raised heartbeat limit: [ExistsRepresentingFamilyOfAuxiliaryRepresentatioStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepresentingFamilyOfAuxiliaryRepresentatioStatement.lean#L7). We read the statements of results 1 to 10, not their proofs. The sentence on how $\lambda_u$ and $s_1$ change in result 1 summarizes its Lean statement.
