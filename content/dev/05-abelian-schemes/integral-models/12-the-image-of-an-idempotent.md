---
title: The image of an idempotent
decls:
  - GlobalTheory.IdemLocus.exists_open_locus
  - GlobalTheory.T.exists_open_locus_idempotent_image_siegel
  - GlobalTheory.UPel.HT.idemImage_locus
  - GlobalTheory.T.siegel_family_idempotent_image_open_locus
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The image of an idempotent

Zarhin's trick of the previous section makes a Siegel object $c$ of genus $h$ with kernel killed by $d$ the image of an idempotent on a principal Siegel object $z$ of genus $h'$ with an action. This section goes back. Given a principal Siegel object $z$ with an action over a locally noetherian base $S'$, we find the largest open subscheme of $S'$ over which the image of the idempotent is a Siegel object $c$ of genus $h$ with kernel killed by $d$ and $z$ is Zarhin related to $c$. This is result 7 of the section on the Siegel problem with kernel killed by $d$, and it is used in the proof of [the representability of the Siegel problem](/entry/sd-rep-of-coprime/). We keep the notation of the earlier sections: Siegel objects and maps of Siegel objects (Definitions 8.1.5 and 8.3.1), principal objects (Definition 8.3.2), right actions with the Rosati condition and maps with actions (Definition 8.7.2), and the Zarhin relation (Definition 8.7.4).

Throughout, we fix integers $h$, $h'$, $M$ and $d$, a ring $O$, a map $a \mapsto \bar{a}$ from $O$ to $O$, an element $e \in O$, an additive map $\jmath : \mathbb{Z}^{2h} \to \mathbb{Z}^{2h'}$, elements $o_1, \dots, o_n \in O$ and additive maps $\kappa_1, \dots, \kappa_n : \mathbb{Z}^{2h'} \to \mathbb{Z}^{2h}$. The Zarhin relation uses only $O$, $e$, $\jmath$, the $o_k$ and the $\kappa_k$, so it makes sense for these data. In a map of Siegel objects with families of endomorphisms indexed by $O$ we ask, as in Definition 8.7.2, that the group pullback commutes with the endomorphisms; the families need not be actions.

### Inputs

We use the following results.

1. (The image of an idempotent.) Let $A$ be a commutative semi-abelian group scheme over a scheme $S$ and $\varepsilon$ an endomorphism of $A$ with $\varepsilon^2 = \varepsilon$. Then there are a commutative semi-abelian group scheme $G$ over $S$ and maps of group schemes $\iota : G \to A$ and $q : A \to G$ with $q \iota = 1$ and $\iota q = \varepsilon$.
2. (Retracts of abelian schemes.) Let $A$ be an abelian scheme, $G$ a semi-abelian group scheme, and $\iota : G \to A$ and $q : A \to G$ maps of group schemes with $q \iota = 1$. Then $G$ is an abelian scheme.
3. (Restriction of the bundle.) If $P$ is a line bundle on $A \times_S A$ that is trivial on $0 \times A$ and on $A \times 0$ and symmetric, and $\iota : G \to A$ is a map of group schemes, then $(\iota \times \iota)^* P$ has the same three properties on $G \times_S G$.
4. (Open loci.) Let $S'$ be locally noetherian with a map $t : S' \to \operatorname{Spec} B_M$. Each of the following conditions has an *open locus*: an open set $U \subseteq S'$ such that the condition holds over every open $V \subseteq U$, and such that $g(T) \subseteq U$ for every map $g : T \to S'$ over which the condition holds.
   - (i) The integer $d$ is a unit.
   - (ii) Two additive maps $x, y : \mathbb{Z}^{2m} \to A(S')$ with $Mx = My = 0$ agree, where $A$ is an abelian scheme and $M \geq 1$.
   - (iii) For $M \geq 3$ odd, an abelian scheme $G$ with a line bundle $P_G$ as in result 3 and an additive map $\lambda_G : \mathbb{Z}^{2h} \to G(S')$ with $M \lambda_G = 0$, the map $\lambda_G$ is a symplectic level $M$ structure for $P_G$. Over $g : T \to S'$, the condition means: there are a Siegel object $c'$ of genus $h$ over $t g$ and a group pullback $\varphi : A_{c'} \to G$ along $g$ with $P_{c'} \cong (\varphi \times \varphi)^* P_G$ and $\varphi \lambda_{c'}(a) = \lambda_G(a) g$ for all $a$.
   - (iv) For $G$ and $P_G$ as in (iii), the line bundle $\Delta^* P_G$ is relatively ample.
   - (v) For $G$ and $P_G$ as in (iii), the kernel is killed by $d$: every point $x$ such that the pullback of $P_G$ along $(a, s) \mapsto (x(s), a)$ is trivial satisfies $d x = 0$. Over $g : T \to S'$, we ask in addition that $d$ is a unit on $T$ and that (iv) holds.
5. (Pullback of principal objects.) Let $z$ be a principal Siegel object over $s : S \to \operatorname{Spec} B_M$ with a right action with the Rosati condition, and let $f : S_1 \to S$. Then there is a principal Siegel object $w$ over $s f$ with a right action with the Rosati condition and a map from $w$ with its action to $z$ with its action over $f$.
6. (Images commute with base change.) Let $\psi : A' \to A$ be a group pullback along $g : T \to S'$, let $\iota, q$ split an idempotent $\varepsilon$ of $A$ through $G$, and let $\iota', q'$ split an idempotent $\varepsilon'$ of $A'$ through $G'$, as in result 1. If $\psi \varepsilon' = \varepsilon \psi$, then there is a group pullback $\varphi : G' \to G$ along $g$ with $\psi \iota' = \iota \varphi$ and $(\psi \times \psi)(\iota' \times \iota') = (\iota \times \iota)(\varphi \times \varphi)$.
7. (Level formulas.) Let $z$ be a Siegel object of genus $h'$ over $t : S' \to \operatorname{Spec} B_M$ with endomorphisms $[a]$, $a \in O$. Let $g : T \to S'$, let $c'$ be a Siegel object of genus $h$ over $t g$, and let $w'$ be a Siegel object of genus $h'$ over $t g$ with endomorphisms $[a]'$, Zarhin related to $c'$, with a map from $w'$ to $z$ with the endomorphisms over $g$. Then after pullback along $g$ we have $[e] \lambda_z(\jmath(a)) = \lambda_z(\jmath(a))$ for all $a \in \mathbb{Z}^{2h}$ and $\lambda_z(a) = \sum_k [o_k] \lambda_z(\jmath(\kappa_k(a)))$ for all $a \in \mathbb{Z}^{2h'}$.

For the second theorem we also use three facts about maps. Let $y : S_2 \to S_1$.

8. (Transport of the relation.) If $w_2 \to w_1$ is a map with the endomorphisms over $y$, $c_2 \to c_1$ is a map of Siegel objects over $y$, and $w_1$ is Zarhin related to $c_1$, then $w_2$ is Zarhin related to $c_2$.
9. (Cancellation.) If $w_1 \to z$ is a map with endomorphisms over $g_1 : S_1 \to S$ and $w_2 \to z$ is a map with endomorphisms over $g_1 y$, then there is a map $w_2 \to w_1$ with endomorphisms over $y$.
10. (Maps of images.) If $w_2 \to w_1$ is a map with endomorphisms over $y$, $w_1$ is Zarhin related to $c_1$ and $w_2$ is Zarhin related to $c_2$, then there is a map $c_2 \to c_1$ of Siegel objects over $y$.

Maps with endomorphisms also compose.

### The open locus

**Theorem 8.12.1 (Open locus of the idempotent image).** Let $S'$ be a locally noetherian scheme, $t : S' \to \operatorname{Spec} B_M$, and $z$ a principal Siegel object of genus $h'$ and level $M$ over $t$ with a right action $a \mapsto [a]$ of $O$ with the Rosati condition. Assume $h \geq 1$, $M \geq 3$ odd, $d > 0$, $\gcd(M, d) = 1$ and $e^2 = e$. Then there are an open set $U \subseteq S'$ with inclusion $u : U \to S'$, a Siegel object $c$ of genus $h$ over $t u$, a principal Siegel object $w$ of genus $h'$ over $t u$ and a right action of $O$ on $w$ with the Rosati condition, with these properties:

- $c$ has kernel killed by $d$, and $d$ is a unit on $U$;
- there is a map from $w$ with its action to $z$ with its action over $u$, and $w$ is Zarhin related to $c$;
- let $g : T \to S'$ and let $c'$ be a Siegel object of genus $h$ over $t g$ with kernel killed by $d$, where $d$ is a unit on $T$. If there is a Siegel object $w'$ of genus $h'$ over $t g$ with endomorphisms $[a]'$, $a \in O$, that is Zarhin related to $c'$ and has a map to $z$ with the endomorphisms over $g$, then $g(T) \subseteq U$.

Lean: `GlobalTheory.IdemLocus.exists_open_locus` (also `GlobalTheory.T.exists_open_locus_idempotent_image_siegel`, a second name).

*Proof.* Since the action is a right action, $[e][e] = [e^2] = [e]$. An abelian scheme is semi-abelian, so result 1 gives $G$ with $\iota : G \to A_z$ and $q : A_z \to G$, $q \iota = 1$ and $\iota q = [e]$. By result 2, $G$ is an abelian scheme. Put $P_G = (\iota \times \iota)^* P_z$, which by result 3 is trivial on the two axes and symmetric. Put $\lambda_G(a) = q \lambda_z(\jmath(a))$, an additive map killed by $M$.

Let $U_1$ to $U_6$ be the open loci of result 4 for these conditions: (i) $d$ is a unit; (ii) $[e] \lambda_z(\jmath(a)) = \lambda_z(\jmath(a))$ for all $a$; (ii) again, for $\lambda_z(a) = \sum_k [o_k] \lambda_z(\jmath(\kappa_k(a)))$ for all $a$; (iii) $\lambda_G$ is a symplectic level structure for $P_G$; (iv) $\Delta^* P_G$ is relatively ample; (v) the kernel of $P_G$ is killed by $d$. Let $U = U_1 \cap \dots \cap U_6$ and $u : U \to S'$ the inclusion.

Let $c$ be the pullback of $(G, P_G, \lambda_G)$ to $U$. By $U_4$ it is a Siegel object of genus $h$, and by $U_5$ and $U_6$ its kernel is killed by $d$. By $U_1$, $d$ is a unit on $U$. Let $w$ be the pullback of $z$ to $U$ with the pulled back action. It is principal, the action is a right action with the Rosati condition, and the projection is a map with actions over $u$. We check that $w$ is Zarhin related to $c$ with the pullbacks of $\iota$ and $q$. Clause 1 holds by result 1. Clause 2 holds by the definition of $P_G$. For clause 3, $\iota \lambda_G(a) = \iota q \lambda_z(\jmath(a)) = [e] \lambda_z(\jmath(a)) = \lambda_z(\jmath(a))$ over $U_2$. For clause 4, clause 3 gives $[o_k] \iota \lambda_G(\kappa_k(a)) = [o_k] \lambda_z(\jmath(\kappa_k(a)))$, and the sum over $k$ is $\lambda_z(a)$ over $U_3$.

For the last property, let $g$, $c'$ and $w'$ be as stated. We show $g(T) \subseteq U_i$ for each $i$. For $U_1$, $d$ is a unit on $T$. For $U_2$ and $U_3$, result 7 gives the two level formulas over $g$. For the others, let $\psi : A_{w'} \to A_z$ be the group pullback of the map $w' \to z$, and let $\iota', q'$ be the maps of the Zarhin relation between $w'$ and $c'$. Then $\iota'$ and $q'$ split $[e]'$ through $A_{c'}$, and $\psi [e]' = [e] \psi$. Result 6 gives a group pullback $\varphi : A_{c'} \to G$ along $g$ with $\psi \iota' = \iota \varphi$. Then

$$\begin{aligned} P_{c'} &\cong (\iota' \times \iota')^* P_{w'} \cong (\iota' \times \iota')^* (\psi \times \psi)^* P_z \\ &= (\varphi \times \varphi)^* (\iota \times \iota)^* P_z = (\varphi \times \varphi)^* P_G. \end{aligned}$$

For the level structures, $\iota \varphi \lambda_{c'}(a) = \psi \iota' \lambda_{c'}(a) = \psi \lambda_{w'}(\jmath(a)) = \lambda_z(\jmath(a)) g$, by clause 3 for $w'$ and the compatibility of $\psi$ with levels. Applying $q$ and $q \iota = 1$ gives $\varphi \lambda_{c'}(a) = \lambda_G(a) g$. So $g(T) \subseteq U_4$. Since the kernel of $c'$ is killed by $d$, $\Delta^* P_{c'}$ is relatively ample, which gives $g(T) \subseteq U_5$, and with $d$ a unit on $T$ it gives $g(T) \subseteq U_6$. $\square$

### The image of the idempotent as an immersion

**Theorem 8.12.2 (The image of the idempotent).** Let $S'$, $t$, $z$ and the action be as in the previous theorem, and make the same assumptions. Then there are a scheme $Y$, an immersion $\jmath_Y : Y \to S'$ that is quasi-compact, and a Siegel object $c$ of genus $h$ over $t \jmath_Y$ with kernel killed by $d$, where $d$ is a unit on $Y$, with two properties.

- (a) Let $t' : T \to \operatorname{Spec} B_M$, let $y : T \to Y$ with $t \jmath_Y y = t'$, and let $c'$ be a Siegel object of genus $h$ over $t'$ with a map $c' \to c$ over $y$. Then there are a principal Siegel object $w$ of genus $h'$ over $t'$ and a right action of $O$ on $w$ with the Rosati condition, with a map from $w$ with its action to $z$ with its action over $\jmath_Y y$, such that $w$ is Zarhin related to $c'$.
- (b) Let $g : T \to S'$, let $c'$ be a Siegel object of genus $h$ over $t g$ with kernel killed by $d$, where $d$ is a unit on $T$. Assume that there is a Siegel object $w$ of genus $h'$ over $t g$ with endomorphisms indexed by $O$, Zarhin related to $c'$, with a map to $z$ with the endomorphisms over $g$. Then there is a unique $y : T \to Y$ with $\jmath_Y y = g$ such that there is a map $c' \to c$ over $y$.

Lean: `GlobalTheory.UPel.HT.idemImage_locus` (also `GlobalTheory.T.siegel_family_idempotent_image_open_locus`, a second name).

*Proof.* Take $U$, $c$, $w$ and its action from the previous theorem, let $Y = U$ and let $\jmath_Y = u$ be the inclusion. The open immersion $u$ is quasi-compact, since $S'$ is locally noetherian and so every open subset of an affine open of $S'$ is quasi-compact.

For (a), result 5 gives a principal Siegel object $w_2$ over $t'$ with a right action with the Rosati condition and a map from $w_2$ to $w$ with actions over $y$. Composed with the map from $w$ to $z$ over $u$, it gives a map from $w_2$ to $z$ over $u y$. By result 8, applied to $w_2 \to w$ and $c' \to c$ over $y$, the object $w_2$ is Zarhin related to $c'$.

For (b), the previous theorem gives $g(T) \subseteq U$, so $g = u y$ for a unique $y : T \to U$. Result 9, applied to $w \to z$ over $u$ and the given map to $z$ over $u y$, gives a map with endomorphisms over $y$ from the given object to $w$. By result 10 there is a map $c' \to c$ over $y$. If $y'$ also satisfies $u y' = g$, then $y' = y$, since an open immersion is a monomorphism. $\square$

**Remark 8.12.3 (Formalization).** In the theorem on the open locus, the hypotheses $h \geq 1$, $d > 0$ and $\gcd(M, d) = 1$ are not used, and the map $a \mapsto \bar{a}$ need not be additive: [ExistsOpenLocusIdempotentImageSiegel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsOpenLocusIdempotentImageSiegel.lean#L160). The immersion of the second theorem is the inclusion of the open set, so the theorem gives an open immersion, which is more than the statement says: [SiegelFamilyIdempotentImageOpenLocus.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyIdempotentImageOpenLocus.lean#L20). In the maximality property and in (b), the object $w'$ need not be principal and its endomorphisms need not form an action. Both second names are wrappers that try several forms of one proof term under a raised heartbeat limit: [ExistsOpenLocusIdempotentImageSiegelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsOpenLocusIdempotentImageSiegelStatement.lean#L6) and [SiegelFamilyIdempotentImageOpenLocusStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyIdempotentImageOpenLocusStatement.lean#L6). We read the statements of results 1, 2 and 4 to 10, not their proofs. We did not unfold the definition of a semi-abelian group scheme.
