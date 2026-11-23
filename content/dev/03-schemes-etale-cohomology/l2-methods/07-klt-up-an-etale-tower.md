---
title: Klt up an étale tower
decls:
  - GlobalTheory.FieldPair.klt_of_isEtTower
  - GlobalTheory.FieldPair.SpecTower.klt_of_tower
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Klt up an étale tower

The proof of Angehrn and Siu in Section 8 compares a pair on $X$ with a pair on a product $X \times Z'$, where $Z'$ is a model of the non-klt centre. The local ring of the product at a point over $x$ is, up to an étale map, a polynomial ring over the local ring of $X$ at $x$ in the coordinates of $Z'$. This section proves that the klt condition moves up from the base ring to such a ring: if a pair is klt downstairs, then the pulled back pair, with the extra coordinates in the form, is klt upstairs. The proof cuts the extra coordinates one at a time, with the restriction theorem of Section 6.

We keep the notation of Section 6. For a ring map $\iota : R \to T$ and a formal sum $\varphi = \sum \varphi_g [g]$ over $R$ we write $\iota_*\varphi = \sum \varphi_g [\iota(g)]$, and in the same way for other maps.

**Definition 10.7.1 (Étale tower).** Let $K$ and $L$ be fields over $\mathbb{C}$, and $r \ge 0$. An *étale tower* of length $r$ consists of subrings $R \subseteq K$ and $T \subseteq L$, ring maps $\iota : R \to T$ and $\psi : T \to R$, and elements $\tau_1, \dots, \tau_r \in T$, such that:

1. $R$ is an integrally closed local model of $K$, and $T$ is a local model of $L$;
2. $\iota$ is a map over $\mathbb{C}$, and $\psi \circ \iota$ is the identity of $R$;
3. $\psi(\tau_j) = 0$ for each $j$;
4. the map $R[X_1, \dots, X_r] \to T$ that is $\iota$ on $R$ and sends $X_j$ to $\tau_j$ is formally étale.

So $\operatorname{Spec} T \to \operatorname{Spec} R \times \mathbb{A}^r$ is étale at the point, $\psi$ is a section of $\operatorname{Spec} T \to \operatorname{Spec} R$, and its image is the locus $\tau_1 = \dots = \tau_r = 0$. In geometric terms, $T$ is the local ring of a point of a smooth family over $\operatorname{Spec} R$ of relative dimension $r$, with étale coordinates $\tau$ along the fibre that vanish on a section.

**Theorem 10.7.2 (Klt up an étale tower).** Assume principalisation. Let $(R, T, \iota, \psi, \tau)$ be an étale tower of length $r$, with $R \subseteq K$ and $T \subseteq L$. Let $x = (x_1, \dots, x_n)$ in $R$ be a transcendence basis of $K$. Let $\varphi$ be a finite formal sum of nonzero elements of $R$, and let $\theta$ be a finite formal sum of elements of $T$ with $\psi(g) \neq 0$ and $\theta_g \ge 0$ for each $g$ in its support. Suppose that $(dx, \varphi)$ is effective at $R$ and that $(dx, \varphi + \psi_*\theta)$ is klt over $R$. Then
$$\bigl(d\tau_1 \wedge \dots \wedge d\tau_r \wedge d\iota(x_1) \wedge \dots \wedge d\iota(x_n),\ \iota_*\varphi + \theta\bigr)$$
is klt over $T$.

Lean: `GlobalTheory.FieldPair.SpecTower.klt_of_tower` (also `GlobalTheory.FieldPair.klt_of_isEtTower`, the same statement with the length $r$ after $n$ in the arguments).

The pair upstairs is the pull back of $(R, \varphi)$ along the smooth map, plus the boundary $\theta$. The condition $\psi(g) \neq 0$ says that no component of $\theta$ contains the section $\{\tau = 0\}$, and the hypothesis downstairs is on the restriction $\varphi + \psi_*\theta$ of the full boundary to this section. So the theorem is a form of the principle that klt descends from a smooth subvariety, here the section, to a neighbourhood of it.

*Proof.* By induction on $r$, for all fields, rings and data at once.

*The case $r = 0$.* The map $R \to T$ is formally étale, and it has the retraction $\psi$. For an étale tower of length $0$ the map $\psi$ is bijective, a fact that we read as a statement. Geometrically, a section of an étale map is open and closed, and $\operatorname{Spec} T$ is connected. So $\iota$ is an isomorphism with inverse $\psi$, and it extends to an isomorphism $K \to L$ of the fraction fields over $\mathbb{C}$ that maps $R$ onto $T$. Places, forms and discrepancies move along this isomorphism. The form is $d\iota(x)$, the boundary is $\iota_*\varphi + \theta = \iota_*(\varphi + \psi_*\theta)$, and the hypothesis gives the claim.

*The step from $r$ to $r + 1$.* We use four facts, of which we read only the statements.

- (a) *Cutting the last coordinate.* There are a field $L'$ over $\mathbb{C}$, a local model $T' \subseteq L'$ and a surjective ring map $\pi : T \to T'$ over $\mathbb{C}$ whose kernel is the principal ideal $(\tau_{r+1})$ with $\tau_{r+1} \neq 0$, such that $(R, T', \pi \circ \iota, \psi', \pi(\tau_1), \dots, \pi(\tau_r))$ is an étale tower of length $r$ with $\psi' \circ \pi = \psi$. Geometrically, $T'$ is the local ring of the hypersurface $\{\tau_{r+1} = 0\}$, which is étale over $\operatorname{Spec} R \times \mathbb{A}^r$.
- (b) *Effective upstairs.* If $(dx, \varphi)$ is effective at $R$, $\varphi$ has nonzero support, and $\theta \ge 0$ with images of its support nonzero in $L$, then $(d\tau \wedge d\iota(x), \iota_*\varphi + \theta)$ is effective at $T$. The prime divisors of $T$ are either pulled back from $R$, where the discrepancy is unchanged because the map is smooth, or new, where the coefficient of $\iota_*\varphi$ is $0$ and $\theta \ge 0$ only lowers the discrepancy.
- (c) *Normality.* The ring $T$ of an étale tower over a normal ring is integrally closed.
- (d) *A transcendence basis.* $(\tau_1, \dots, \tau_r, \iota(x_1), \dots, \iota(x_n))$ is a transcendence basis of $L$, and the same holds for the images of these elements in $L'$ under the tower of (a).

Let $\theta'$ be the image of $\theta$ in $T'$, that is $\pi_*\theta$. Each $g$ in its support is $\pi(t)$ with $t$ in the support of $\theta$, so $\psi'(g) = \psi(t) \neq 0$, and $\theta' \ge 0$. Also $\psi'_*\theta' = \psi_*\theta$. So the hypothesis is the hypothesis of the theorem for the tower of length $r$ of (a). By induction,
$$\Bigl(d\pi(\tau_1) \wedge \dots \wedge d\pi(\tau_r) \wedge d\pi\iota(x),\ (\pi\iota)_*\varphi + \theta'\Bigr)$$
is klt over $T'$.

Now apply the theorem on klt from the restriction to a hypersurface ([Theorem 10.6.7](/entry/klt-of-klt-restrict/)) to the ring $T$, the map $\pi$, the element $f = \tau_{r+1}$, the family $w = (\tau_1, \dots, \tau_r, \iota(x))$ and the sum $\Theta = \iota_*\varphi + \theta$ over $T$. Its hypotheses hold:

- $T$ is an integrally closed local model, by (c);
- $\pi$ is a map over $\mathbb{C}$ with kernel $(\tau_{r+1})$, $\tau_{r+1} \neq 0$, and image the local model $T'$, by (a);
- $\pi(w)$ is a transcendence basis of $L'$, by (d);
- each $g$ in the support of $\Theta$ has $\pi(g) \neq 0$. For $g = \iota(a)$ with $a$ in the support of $\varphi$, $\psi'(\pi(\iota(a))) = \psi(\iota(a)) = a \neq 0$. For $g$ in the support of $\theta$, $\psi'(\pi(g)) = \psi(g) \neq 0$;
- $(d(f, w), \Theta)$ is effective at $T$, by (b), after a permutation of the coordinates;
- $(d\pi(w), \pi_*\Theta)$ is klt over $T'$, by the induction step above, since $\pi_*\Theta = (\pi\iota)_*\varphi + \theta'$.

So $(d(f, w), \Theta)$ is klt over $T$. The form $d\tau_{r+1} \wedge d\tau_1 \wedge \dots \wedge d\tau_r \wedge d\iota(x)$ differs from $d\tau_1 \wedge \dots \wedge d\tau_{r+1} \wedge d\iota(x)$ by a sign, which changes no order of a form. So the claim holds for $r + 1$. $\square$

The induction uses the restriction theorem $r$ times, and each use rests on principalisation through the inversion of adjunction of Section 6.

**Remark 10.7.3 (Formalization).** The étale tower is the structure `IsEtTower` in Definitions/Divisors/NotDominatesTopPlace.lean, line 19. Its condition 4 is `FormallyEtale` for the evaluation map of the polynomial ring. The base case is `klt_tower_zero`, with the bijectivity `IsEtTower.bijective_of_zero` (Definitions/Divisors/DominatesIffIsLocalHom.lean, line 312) and the transport `ringEquiv_transports_varietyPair_data`. The facts (a) to (d) are `exists_quotient_lastCoordinate_etaleTowerNormalLocal`, `boundaryEffective_up_etale_tower_normal_local`, `isIntegrallyClosed_of_isEtaleTowerOverNormalLocal` and `etaleTower_trBasis_append_coordinates`. We read their statements, not their proofs, and the geometric reasons given for (a) and (b) are ours. The reordering of the coordinates is `exists_equiv_cons_last` with `klt_comp_equiv` and `effAt_comp_equiv`. The two names `klt_of_tower` and `klt_of_isEtTower` differ only in the order of the arguments $n$ and $r$. The second is the one used in Section 8.
