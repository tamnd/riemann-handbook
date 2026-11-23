---
title: The dual from a relatively ample bundle
decls:
  - GlobalTheory.T.exists_quotient_kernel_polarisation_descended_bundle
  - GlobalTheory.DualQuot.exists_quotient_lam
  - GlobalTheory.T.hasDualRepresentative_of_relAmple_noetherian
  - GlobalTheory.DualPol.hasRepAF_of_relAmple
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The dual from a relatively ample bundle

Over a field, an ample line bundle $L$ on an abelian variety $A$ gives an isogeny $\varphi_L : A \to A^\vee$ with kernel $K(L)$, so $A^\vee = A/K(L)$ (Mumford, *Abelian Varieties*, Chapters II and III). This section carries out this construction over a noetherian affine base with a relatively ample $L$. It forms $B = A/K(L)$ with a line bundle $P$ on $A \times B$ that descends the Mumford class (Theorem (Quotient by the kernel)). Then it proves that $B$ is a good representative of the dual (Theorem (Dual from an ample bundle)). This is the base case of the construction: the reduced case in the next section uses it over normal domains.

We keep the notation of the last section. Let $R$ be a noetherian ring and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$, with a relatively ample line bundle $L$.

**Theorem 1.3.1 (Quotient by the kernel).** There are an $R$-scheme $B$, a line bundle $P$ on $A \times B$ and an $R$-morphism $q : A \to B$ with these properties.

1. $P$ is an additive family, and $B \to \mathrm{Spec}\, R$ is proper, smooth of relative dimension $g$, with geometrically connected fibres.
2. Each finite set of points of $B$ lies in an affine open set.
3. $q$ is finite, flat and surjective.
4. For each $R$-scheme $Y$ and all $a, x \in A(Y)$, $P(a, q x) = \Lambda(L)(a, x)$.
5. For each $R$-scheme $Y$ and all $x, y \in A(Y)$, $q x = q y$ if and only if $x y^{-1} \in K(L)(Y)$.

Lean: `GlobalTheory.DualQuot.exists_quotient_lam` (also `GlobalTheory.T.exists_quotient_kernel_polarisation_descended_bundle`, a second name).

The proof uses six facts, each over the noetherian ring $R$.

1. (Kernel.) $K(L)$ is represented by a finite flat subgroup: there are a group $H$ over $R$, finite and flat, and a homomorphism $i : H \to A$ that is a monomorphism, such that $x \in A(T)$ lies in $K(L)$ if and only if $x$ factors through $i$.
2. (Quotient.) For a finite flat subgroup $i : H \to A$ as in fact 1, there are an abelian scheme $B$ over $R$, a homomorphism $q : A \to B$ that is finite, flat and surjective, and a finite morphism $\pi : B \to A$, such that the square with the maps $(h, a) \mapsto i(h) a$ and $(h, a) \mapsto a$ from $H \times A$ to $A$, followed by $q$, is cartesian. That is, $H \times A \cong A \times_B A$ by $(h, a) \mapsto (i(h) a, a)$.
3. (Descent of the Mumford class.) With $H$ as in fact 1 and $q$, $B$ as in fact 2, there is a line bundle $P_0$ on $A \times B$ with $P_0(a, q x) = \Lambda(L)(a, x)$ for all $a, x \in A(Y)$.
4. (Cube.) Let $A$ and $B$ be abelian schemes over a locally noetherian base, and $P$ a line bundle on $A \times B$ that is trivial on $\{1\} \times B$ and on $A \times \{1\}$. Then $P$ is an additive family.
5. (Dimension.) Let $q : A \to B$ be finite, flat and surjective, with $A$ smooth of relative dimension $g$ and $B$ smooth. Then $B$ is smooth of relative dimension $g$.
6. (Affine open sets.) Each finite set of points of $A$ lies in an affine open set.

Fact 4 is a consequence of the theorem of the cube over a base ([Volume 1](/learn/abelian-varieties/#abelian-schemes)).

*Proof.* Take $H$ and $i$ from fact 1, then $B$, $q$ and $\pi$ from fact 2, then $P_0$ from fact 3. Fact 3 does not control $P_0$ on $\{1\} \times B$, so we correct it. Let
$$P = P_0 \otimes c^* P_0^{-1}, \qquad c : A \times B \to A \times B, \quad (a, t) \mapsto (1, t).$$
Then $P(a, t) = P_0(a, t) - P_0(1, t)$. For $t = q x$ this is $\Lambda(L)(a, x) - \Lambda(L)(1, x) = \Lambda(L)(a, x)$, since $\Lambda(L)(1, x) = L(x) - L(1) - L(x) + L(1) = 0$. This is property 4.

The bundle $P$ is trivial on $\{1\} \times B$, since $P(1, t) = P_0(1, t) - P_0(1, t) = 0$. It is trivial on $A \times \{1\}$: as $q$ is a homomorphism, $1 = q(1)$ in $B(A)$, so $P(a, 1) = \Lambda(L)(a, 1) = L(a) - L(a) - L(1) + L(1) = 0$. So $P$ is additive by fact 4, since $R$ is noetherian and $A$, $B$ are abelian schemes. As $B$ is an abelian scheme, it is proper and smooth with geometrically connected fibres, and fact 5 applied to $q$ gives the relative dimension $g$. This proves property 1. Property 3 is part of fact 2.

For property 2, let $F$ be a finite set of points of $B$. By fact 6, the finite set $\pi(F)$ lies in an affine open set $U$ of $A$. As $\pi$ is finite, it is affine, so $\pi^{-1}(U)$ is an affine open set, and it contains $F$.

For property 5, let $x, y \in A(Y)$. If $q x = q y$, then $(x, y)$ is a point of $A \times_B A$. By the cartesian square it is $(i(z) a, a)$ for a point $(z, a)$ of $H \times A$. So $a = y$ and $x y^{-1} = i(z)$, which lies in $K(L)$ by fact 1. Conversely, if $x y^{-1} \in K(L)(Y)$, fact 1 gives $z \in H(Y)$ with $x = i(z) y$, and the square gives $q(i(z) y) = q(y)$. $\square$

The next theorem shows that $(B, P)$ represents the additive families. It needs three more facts. Let $B$, $P$ and $q$ be as in the theorem above.

7. (Injectivity.) The family $P$ is injective.
8. (Descent of agreement.) Let $N$ on $A \times T$ and $M$ on $A \times U$ be additive families, $y \in T(Y)$, $u \in U(Y)$, and $c : Y' \to Y$ flat, surjective and quasi-compact. If $N$ at $y c$ agrees with $M$ at $u c$, then $N$ at $y$ agrees with $M$ at $u$.
9. (Descent of morphisms.) A morphism of schemes $h : H \to T$ that is flat, surjective and quasi-compact is an effective epimorphism: a morphism $H \to B$ whose two pullbacks to $H \times_T H$ agree factors uniquely through $h$.

Over a field, fact 7 says that $\varphi_L$ induces an injection of $A/K(L)$ into the dual, as $K(L)$ is the kernel of $\varphi_L$. Fact 9 is Grothendieck's faithfully flat descent (A. Grothendieck, *Revêtements étales et groupe fondamental* (SGA 1), Lecture Notes in Math. 224, Exposé VIII).

**Theorem 1.3.2 (Dual from an ample bundle).** Let $R$ be a noetherian ring, $A$ an abelian scheme over $\mathrm{Spec}\, R$ that is smooth of relative dimension $g$, and $L$ a relatively ample line bundle on $A$. Then $\mathrm{Rep}^{\mathrm{af}}_g(A, \mathrm{Spec}\, R)$ holds: the dual of $A$ has a good representative of dimension $g$ over $\mathrm{Spec}\, R$ in which each finite set of points lies in an affine open set.

Lean: `GlobalTheory.DualPol.hasRepAF_of_relAmple` (also `GlobalTheory.T.hasDualRepresentative_of_relAmple_noetherian`, a second name).

*Proof.* Take $B$, $P$ and $q$ from Theorem (Quotient by the kernel), and let $b : B \to \mathrm{Spec}\, R$ be the structure map. Properties 1 and 2 give that $b$ is good of dimension $g$ and that finite sets of points lie in affine open sets. Over $S' = \mathrm{Spec}\, R$ the condition $b \circ x = t$ is automatic. It remains to show: for each $R$-scheme $T$ and each additive family $N$ on $A \times T$ there is exactly one $x_T : T \to B$ with $N \cong P_{x_T}$.

Uniqueness. If $N \cong P_x$ and $N \cong P_{x'}$, then $P$ at $x$ agrees with $P$ at $x'$, and $x = x'$ by fact 7.

Existence. Theorem (Flat cover) of the last section gives $h : H \to T$, flat, surjective and quasi-compact, and $x : H \to A$ with $N(a, h y) = \Lambda(L)(a, x y)$ for all points $a$ and $y$. With property 4,
$$P(a, q x y) = \Lambda(L)(a, x y) = N(a, h y).$$
Call this identity (E).
Let $g_1, g_2 : Z \to H$ with $h g_1 = h g_2$. Apply (E) on $Y = A \times Z$ with $a = \mathrm{pr}_A$ and $y = g_k \circ \mathrm{pr}_Z$ for $k = 1, 2$. The right sides agree, so $P_{q x g_1} \cong P_{q x g_2}$ on $A \times Z$, and fact 7 gives $q x g_1 = q x g_2$. By fact 9 there is a unique $x_T : T \to B$ with $x_T \circ h = q \circ x$. It is a morphism over $R$, since $h$ is an epimorphism. Now (E), with $Y = A \times H$, $a = \mathrm{pr}_A$ and $y = \mathrm{pr}_H$, says that $N$ at $h$ agrees with $P$ at $q x = x_T h$, on $A \times H$. By fact 8, applied to $c = h$, $N$ at $1_T$ agrees with $P$ at $x_T$, that is, $N \cong P_{x_T}$. $\square$

The classical form of this result is the construction of the dual abelian variety as $A/K(L)$ for an ample $L$ over a field (Mumford, *Abelian Varieties*, Chapter II, §8, and Chapter III, §13). The theorem gives the representative only, with no group structure on $B$. The group structure comes later, from the universal property.

**Remark 1.3.3 (Formalization).** Facts 1 to 9 are `GlobalTheory.T.kernelOfLineBundle_finiteFlat_subgroupScheme`, `GlobalTheory.T.exists_quotient_abelianScheme_finiteFlat_subgroup`, `GlobalTheory.T.exists_descent_mumfordBundle_quotient`, `GlobalTheory.CubeNoeth.isAdditive_of_triv_axes` (proved in [IsAdditiveSwapOfTrivAxes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsAdditiveSwapOfTrivAxes.lean#L202)), `GlobalTheory.T.smoothOfRelativeDimension_descends_finite_flat_surjective`, `GlobalTheory.T.finiteSetsInAffineOpen_abelianScheme_relAmple`, `GlobalTheory.T.dualPoint_eq_of_quotient_family_iso`, `GlobalTheory.T.sameLineBundleFamily_descends_flat_surjective_quasiCompact` and the Mathlib instance that makes such morphisms effective epimorphisms (`EffectiveEpi.desc`). Facts other than 4 and 9 are cited by their statements; the remarks above on why they hold are not read from proofs. The quotient $B$ of fact 2 is an abelian scheme with a group structure, but Theorem (Quotient by the kernel) forgets it, and keeps only $q$ as a morphism. Both second names are closed by a `first` list under `set_option maxHeartbeats 1000000`.
