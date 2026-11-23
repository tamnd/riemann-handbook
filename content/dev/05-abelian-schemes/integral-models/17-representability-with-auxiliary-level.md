---
title: Representability with auxiliary level
decls:
  - GlobalTheory.UPel.HT.relRep_htPull
  - GlobalTheory.T.harrisTaylor_structures_relatively_representable
  - GlobalTheory.UPel.HT.relRep_siegel
  - GlobalTheory.T.harrisTaylor_structures_representable_siegel_baseChange
  - GlobalTheory.UPel.HT.harrisTaylorModuli_symplecticLevel_representable
  - GlobalTheory.T.harrisTaylor_auxiliary_symplectic_level_representable
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Representability with auxiliary level

This section proves result 2 of Section 8.1: if the Siegel problem $(h, M, e)$ is representable, then $b$ has representable auxiliary level $(N, h, M)$. We prove it in three steps. First, over a locally noetherian base $S$ with a Siegel object $c$, the objects of level $N$ whose abelian scheme is a pullback of $c$ are represented by a scheme finite over $S$. Second, we apply this to the pullback of $c$ to $Y \times \operatorname{Spec} R$, and we carry the symplectic level structure along. Third, we take for $c$ the universal Siegel object.

Throughout, $D$ is a datum for $p$, $b$ is a base for $D$ over a ring $R$, and $N \geq 3$ is prime to $p$. We keep the notation of the [section on the Lie and Tate loci](/entry/lie-geom-locus-closed/). Let $c = (A_c, P_c, \lambda_c)$ be a Siegel object over a scheme $S$ and let $g : T \to S$. A *polarized pullback* of $c$ along $g$ is a pair $(\varphi, \varphi_2)$, where $\varphi : A \to A_c$ is a group pullback along $g$ (Definition 8.2.5) of a group scheme $A$ over $T$, and $\varphi_2 : A \times_T A \to A_c \times_S A_c$ is $\varphi$ on each factor. For an object $o$ of level $N$ over $T$ we also ask that $P_o \cong \varphi_2^* P_c$.

### Inputs

We use the following results. Let $c$ be a Siegel object of genus $h$ and level $M$ over $s_1 : S \to \operatorname{Spec} B$, with $\zeta \in B$ and kernel killed by $e$ prime to $p$, and let $t : S \to \operatorname{Spec} R$.

1. (Action and level map.) Let $S$ be locally [[noetherian|0670T59HGE]]. There are a locally noetherian scheme $E$, a [[finite|N9C4X7XKE4]] map $\pi_E : E \to S$, a commutative group scheme $A_E$ over $E$ with a polarized pullback $(\varphi_E, \varphi_{2E})$ of $c$ along $\pi_E$, an action of $O$ and a level map $\eta_E$ of level $N$, with the Rosati condition for $\varphi_{2E}^* P_c$. They are universal in this sense. Let $g : T \to S$ and let $A_T$ be a group scheme over $T$ with a polarized pullback $(\varphi, \varphi_2)$ of $c$ along $g$, an action of $O$ satisfying the Rosati condition for $\varphi_2^* P_c$, and a level map $\eta$ of level $N$. Then there is a unique $z : T \to E$ with $\pi_E z = g$ for which there is a group pullback $\psi : A_T \to A_E$ along $z$ with $\varphi_E \psi = \varphi$ that commutes with $O$ and carries $\eta$ to $\eta_E$.
2. (The conditions along a pullback.) Let $(A_X, \varphi_X, \varphi_{2X})$ be a polarized pullback of $A_c$ along $\pi_X : X \to S$, let $z : T \to X$, and let $A_T$ have a polarized pullback $(\varphi_T, \varphi_{2T})$ along $\pi_X z$ and a line bundle $P_T \cong \varphi_{2T}^* P_c$. Let $\psi : A_T \to A_X$ be a group pullback along $z$ with $\varphi_X \psi = \varphi_T$ that commutes with $O$ and carries $\eta_T$ to $\eta_X$. Then the Hermitian Lie condition holds for $A_T$ at $(\beta, x)$ if and only if it holds for $A_X$ at $(\beta, z x)$, and the Tate condition for $(A_T, P_T, \eta_T)$ at a geometric point $x$ is equivalent to the Tate condition for $(A_X, \varphi_{2X}^* P_c, \eta_X)$ at $z x$.
3. (An object over the locus.) Let $X$ and $A_X$ be as in the [theorem on the Lie and Tate loci](/entry/lie-geom-locus-closed/), and let $j : Z \to X$ satisfy conditions 1 and 2 of that theorem. Then there are an object $u$ of level $N$ over $Z$, a group pullback $\psi : A_u \to A_X$ along $j$, and $\psi_2$ such that $(\varphi_X \psi, \psi_2)$ is a polarized pullback of $c$, $P_u \cong \psi_2^* P_c$, and $\psi$ commutes with $O$ and carries $\eta_u$ to $\eta_X$.
4. (Maps of objects from a common pullback.) Let $o$ over $T$ and $u$ over $Z$ be objects of level $N$ with polarized pullbacks of the same $(A_0, P_0)$ along $g$ and $\pi_Z$. Let $z : T \to Z$ with $\pi_Z z = g$, and let $\psi : A_o \to A_u$ over $z$ commute with the maps to $A_0$, with $O$ and with $\eta$. Then there is a map of objects $o \to u$ over $z$ whose underlying map is $\psi$.
5. (Pullback of Siegel objects.) A Siegel object has a pullback along every map $f : S' \to S$: a Siegel object $c'$ over $s_1 f$ with a map $c' \to c$ over $f$ (Definition 8.3.1). If the kernel of $c$ is killed by $e$, so is the kernel of $c'$.
6. (Pullback of level structures.) Let $\varphi : A' \to A$ be a group pullback along $f$ with $P' \cong (\varphi \times \varphi)^* P$, and let $\lambda$ be a symplectic level $M$ structure on $(A, P)$. The sections $\lambda'(a)$ of $A'$ with $\varphi \lambda'(a) = \lambda(a) f$ form a symplectic level $M$ structure on $(A', P')$.
7. (Composition and cancellation.) Maps of Siegel objects compose. If $c'' \to c$ is a map over $f$ and $c' \to c$ is a map over $f h$, then there is a map $c' \to c''$ over $h$.
8. (Rigidity.) Let $M \geq 3$ and let $c$ be a Siegel object over $\operatorname{Spec} B_M$ with $\Delta^* P_c$ relatively ample. Two maps $c' \to c$ over the same $f$ have the same underlying map.
9. (Quasi-projectivity.) Let $R$ be noetherian with $M$ a unit in $R$, let $Y \to \operatorname{Spec} B_M$ be quasi-projective, and let $\pi : Z \to Y \times \operatorname{Spec} R$ be finite. Then $Z \to \operatorname{Spec} R$ is quasi-projective. A scheme quasi-projective over a noetherian ring is locally noetherian.
10. (Kernel of the Siegel object.) Let $e$ be prime to $p$ with $E(\Lambda, -) \supseteq e\Lambda^\vee$. For every object of level $N$ with a symplectic level $M$ structure, the Siegel object it defines has kernel killed by $e$.

Products $Y \times \operatorname{Spec} R$ are over $\operatorname{Spec} \mathbb{Z}$, and we write $\mathrm{pr}_1$ and $\mathrm{pr}_2$ for the projections.

### Relative representability

**Theorem 8.17.1 (Relative representability).** Let $S$ be locally noetherian, and let $c$ and $t$ be as above. Then there are a finite map $\pi : Z \to S$, an object $u$ of level $N$ over $t \pi$, and a polarized pullback $(\varphi_u, \varphi_{2u})$ of $c$ along $\pi$ with $P_u \cong \varphi_{2u}^* P_c$, with this property. Let $g : T \to S$, let $o$ be an object of level $N$ over $t g$, and let $(\varphi, \varphi_2)$ be a polarized pullback of $c$ along $g$ with $P_o \cong \varphi_2^* P_c$. Then there is a unique $z : T \to Z$ with $\pi z = g$ such that some map of objects $m : o \to u$ over $z$ has $\varphi_u m = \varphi$.

Lean: `GlobalTheory.UPel.HT.relRep_htPull` (also `GlobalTheory.T.harrisTaylor_structures_relatively_representable`, a second name).

*Proof.* Result 1 gives $\pi_E : E \to S$ and $A_E$. As $E$ is locally noetherian, the [theorem on the Lie and Tate loci](/entry/lie-geom-locus-closed/) gives a closed immersion $j : Z \to E$. The identity of $Z$ factors through $j$, so $j$ satisfies conditions 1 and 2 of that theorem. Result 3 gives $u$ over $Z$ and $\psi : A_u \to A_E$. Put $\pi = \pi_E j$, which is finite, and $\varphi_u = \varphi_E \psi$, which is a group pullback along $\pi$.

Let $g$, $o$ and $(\varphi, \varphi_2)$ be given. The action on $A_o$ satisfies the Rosati condition for $P_o$, hence for $\varphi_2^* P_c \cong P_o$. Result 1 gives $z_0 : T \to E$ and $\psi_0 : A_o \to A_E$. As $o$ is an object of level $N$, the Hermitian Lie condition and the Tate condition hold for $o$. By result 2 they hold for $A_E$ along $z_0$, so $z_0 = j z$ for some $z : T \to Z$. The map $\psi$ identifies $A_u$ with $A_E \times_E Z$. So $\psi_0$ and the map $A_o \to T \to Z$ give $\psi' : A_o \to A_u$ over $z$ with $\psi \psi' = \psi_0$. Both $\psi'$ and its composites with the action of $c \in O$ and with $\eta$ are fixed by their composites with $\psi$ and with $A_u \to Z$. So $\psi'$ commutes with $O$ and with $\eta$. Result 4 gives a map of objects $m : o \to u$ over $z$ with underlying map $\psi'$, and $\varphi_u m = \varphi_E \psi_0 = \varphi$.

Let $z' : T \to Z$ with $\pi z' = g$ and a map of objects $m'$ with $\varphi_u m' = \varphi$. Then $\psi m'$ is a group pullback along $j z'$ that has the properties of result 1. By the uniqueness in result 1, $j z' = z_0 = j z$. A closed immersion is a monomorphism, so $z' = z$. $\square$

### Adding the level structure

**Theorem 8.17.2 (Relative representability with symplectic level).** Let $M \geq 3$ be odd and prime to $p$, and let $e$ be prime to $p$. Let $Y$ be a scheme over $s : Y \to \operatorname{Spec} B_M$ and $c$ a Siegel object of genus $h$ and level $M$ over $s$ with kernel killed by $e$. Let $Y_R = Y \times \operatorname{Spec} R$ be locally noetherian. Then there are a finite map $\pi : Z \to Y_R$, an object $u$ of level $N$ over $\mathrm{pr}_2 \pi$ and a symplectic level $M$ structure $\lambda_u$ on $u$ over $s\, \mathrm{pr}_1 \pi$ with two properties. Let $o$ be an object of level $N$ over $t : T \to \operatorname{Spec} R$ with a symplectic level $M$ structure $\lambda$ over $t_1 : T \to \operatorname{Spec} B_M$.

1. If $g : T \to Z$ and there is a map of objects $o \to u$ over $g$ that carries $\lambda$ to $\lambda_u$, then there is a map of Siegel objects $(o, \lambda) \to c$ over $\mathrm{pr}_1 \pi g$.
2. If $t_0 : T \to Y$ and there is a map of Siegel objects $(o, \lambda) \to c$ over $t_0$, then there is a unique $g : T \to Z$ with $\mathrm{pr}_1 \pi g = t_0$ and $\mathrm{pr}_2 \pi g = t$ such that a map of objects $o \to u$ over $g$ carries $\lambda$ to $\lambda_u$.

Lean: `GlobalTheory.UPel.HT.relRep_siegel` (also `GlobalTheory.T.harrisTaylor_structures_representable_siegel_baseChange`, a second name).

*Proof.* Result 5 gives the pullback $c'$ of $c$ along $\mathrm{pr}_1$, with kernel killed by $e$, and a map $c' \to c$. The theorem on relative representability, for $c'$ over $Y_R$ and $t = \mathrm{pr}_2$, gives $\pi$, $u$ and $(\varphi_u, \varphi_{2u})$. Result 6 gives the level structure $\lambda_u$ with $\varphi_u \lambda_u(a) = \lambda_{c'}(a) \pi$.

For property 1, the map $o \to u$ is a map of Siegel objects over $g$. The pair $(\varphi_u, \varphi_{2u})$ is a map of Siegel objects $u \to c'$ over $\pi$. With $c' \to c$ and result 7 we get $(o, \lambda) \to c$ over $\mathrm{pr}_1 \pi g$.

For property 2, let $g_0 = (t_0, t) : T \to Y_R$, which exists because $\operatorname{Spec} \mathbb{Z}$ is a final object. By result 7, cancellation of $c' \to c$ along $\mathrm{pr}_1 g_0 = t_0$ gives a map $(\varphi, \varphi_2) : (o, \lambda) \to c'$ over $g_0$. The theorem on relative representability gives $g$ with $\pi g = g_0$ and $m : o \to u$ with $\varphi_u m = \varphi$. For each $a$, the maps $m \lambda(a)$ and $\lambda_u(a) g$ agree after composition with $\varphi_u$, since both give $\lambda_{c'}(a) g_0$, and after composition with $A_u \to Z$. As $\varphi_u$ identifies $A_u$ with a fibre product, $m \lambda(a) = \lambda_u(a) g$.

Let $g'$ have the same properties, with a map of objects $m'$. Then $\pi g' = g_0$, because both projections agree. The maps $\varphi_u m'$ and $\varphi$ both underlie maps of Siegel objects $(o, \lambda) \to c'$ over $g_0$. The bundle $\Delta^* P_{c'}$ is relatively ample, so result 8 gives $\varphi_u m' = \varphi$. The uniqueness in the theorem on relative representability gives $g' = g$. $\square$

### The auxiliary level is representable

**Theorem 8.17.3 (Representability with auxiliary level).** Let $R$ be noetherian. Let $M \geq 3$ be odd and prime to $p$, and let $e$ be prime to $p$ and to $M$ with $E(\Lambda, -) \supseteq e\Lambda^\vee$. Let $h = \lfloor \operatorname{rk} \Lambda / 2 \rfloor$. If the Siegel problem $(h, M, e)$ is representable, then $b$ has representable auxiliary level $(N, h, M)$.

Lean: `GlobalTheory.UPel.HT.harrisTaylorModuli_symplecticLevel_representable` (also `GlobalTheory.T.harrisTaylor_auxiliary_symplectic_level_representable`, a second name).

*Proof.* Let $s : Y \to \operatorname{Spec} B_M$ and $c$ represent the Siegel problem, with $s$ quasi-projective. As $M$ is prime to $p$, it is a unit in $R$. Result 9, for $\pi = \operatorname{id}$, shows that $Y_R$ is quasi-projective over $R$, so it is locally noetherian. The previous theorem gives $\pi : Z \to Y_R$, $u$ and $\lambda_u$. Put $s_Z = \mathrm{pr}_2 \pi$ and $s_{1Z} = s\, \mathrm{pr}_1 \pi$. By result 9, $s_Z$ is quasi-projective.

Let $o$ be an object of level $N$ over $t : T \to \operatorname{Spec} R$ with a symplectic level $M$ structure $\lambda$ over $t_1$. The integer $e$ is a unit in $R$, so it is a unit on $T$. By result 10, the Siegel object $(o, \lambda)$ has kernel killed by $e$. Representability gives a unique $f_0 : T \to Y$ with $s f_0 = t_1$ and a map $(o, \lambda) \to c$ over $f_0$. Property 2 of the previous theorem gives $g$ with $\mathrm{pr}_1 \pi g = f_0$, $s_Z g = t$ and a map of objects that carries $\lambda$ to $\lambda_u$. Then $s_{1Z} g = s f_0 = t_1$.

Let $g'$ have $s_Z g' = t$, $s_{1Z} g' = t_1$ and a map of objects carrying $\lambda$ to $\lambda_u$. By property 1, there is a map $(o, \lambda) \to c$ over $\mathrm{pr}_1 \pi g'$, and $s\, \mathrm{pr}_1 \pi g' = t_1$. By the uniqueness of $f_0$, $\mathrm{pr}_1 \pi g' = f_0$. The uniqueness in property 2 gives $g' = g$. $\square$

**Remark 8.17.4 (Formalization).** The three theorems are [HarrisTaylorStructuresRelativelyRepresentable.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorStructuresRelativelyRepresentable.lean#L18), [HarrisTaylorStructuresRepresentableSiegelBaseCha.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorStructuresRepresentableSiegelBaseCha.lean#L16) and [HarrisTaylorAuxiliarySymplecticLevelRepresentabl.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorAuxiliarySymplecticLevelRepresentabl.lean#L16). In the first theorem, $h$, $M$, $B$ and $\zeta$ are arbitrary. In the second theorem, the hypotheses that $M$ is odd and prime to $p$ are not used; only $M \geq 3$ is used, by result 8. Neither property asks that $t_1$ equal $s$ composed with the map to $Y$. In the third theorem, the hypothesis $\gcd(M, e) = 1$ is not used, and neither is the fact that $e$ is a unit on $Y$: [HarrisTaylorAuxiliarySymplecticLevelRepresentabl.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorAuxiliarySymplecticLevelRepresentabl.lean#L18). The rank is halved in the natural numbers. Each second name is a wrapper that tries three forms of one proof term under a raised heartbeat limit, for example [HarrisTaylorStructuresRelativelyRepresentableStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorStructuresRelativelyRepresentableStatement.lean#L7). We read the statements of results 1 to 10, not their proofs.
