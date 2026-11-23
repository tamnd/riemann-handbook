---
title: Additive line bundles and the dual functor
decls:
  - GlobalTheory.T.exists_flatCover_additiveFamily_eq_lambda
  - GlobalTheory.DualCover.exists_cover
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Additive line bundles and the dual functor

The dual of an abelian scheme $A$ is the scheme that parametrizes the additive line bundles on $A$. This section defines additive families of line bundles, the dual of $A$, and the weaker notion of a representative of the dual functor over a base, which the proof constructs first. It also defines the Mumford class $\Lambda(L)$ and the group $K(L)$ of a line bundle $L$, and relative ampleness. Its theorem says that over a noetherian affine base, each additive family becomes a family of bundles $\Lambda(L)(\cdot, x)$ after a flat surjective base change (Theorem (Flat cover)). This is the existence half of the construction of the dual in the next section.

Let $S$ be a scheme and $A$ a group over $S$, as in the last section. All products are fibre products over $S$. For an $S$-scheme $Y$ we write $\mathrm{Pic}(Y)$ additively ([Picard groups](/learn/commutative-algebra/#picard-groups)). Let $T$ be an $S$-scheme and $M$ a line bundle on $A \times T$. For $a \in A(Y)$ and $t \in T(Y)$ we write
$$M(a, t) = (a, t)^* M \in \mathrm{Pic}(Y),$$
where $(a, t) : Y \to A \times T$. For a line bundle $L$ on $A$ and $a \in A(Y)$ we write $L(a) = a^*L$. For $y \in T(Y)$ we write $M_y = (1 \times y)^* M$, a line bundle on $A \times Y$.

**Definition 1.2.1 (Additive family).** A line bundle $M$ on $A \times T$ is an *additive family* if for each $S$-scheme $Y$, all $a, a' \in A(Y)$ and $t \in T(Y)$,
$$M(a a', t) \cong M(a, t) \otimes M(a', t).$$

With $a = a' = 1$ this gives $M(1, t) = 0$ in $\mathrm{Pic}(Y)$: an additive family is trivial along the unit section $e \times T$. Over an algebraically closed field $k$, with $T = \mathrm{Spec}\, k$, the condition on $M$ is property (b) of [Volume 1](/learn/abelian-varieties/#duality-and-the-poincar-bundle), so $M$ lies in $\mathrm{Pic}^0(A)$. A bundle $\mathrm{pr}_T^* N$ pulled back from $T$ is additive only if $N$ is trivial, since then $N = 2N$. So the additive families on $A \times T$ are the families of elements of $\mathrm{Pic}^0$ of the fibres, parametrized by $T$ and normalized along the unit section.

**Definition 1.2.2 (Agreement).** Let $N$ be a line bundle on $A \times T$ and $M$ one on $A \times U$. For $y \in T(Y)$ and $u \in U(Y)$ we say that *$N$ at $y$ agrees with $M$ at $u$* if $N_y \cong M_u$ on $A \times Y$. We say that $M$ is *injective* if $M$ at $u$ agrees with $M$ at $u'$ only when $u = u'$.

**Definition 1.2.3 (Dual).** Let $B$ be a group over $S$ and $P$ a line bundle on $A \times B$. The pair $(B, P)$ is a *dual* of $A$ if $P$ is an additive family, $P(a, 1) = 0$ for the identity point $a \in A(A)$ (so $P$ is trivial on $A \times \{1\}$), and for each $S$-scheme $T$ and each additive family $M$ on $A \times T$ there is exactly one $x : T \to B$ with $M \cong P_x$.

So $B$ represents the functor $T \mapsto \{\text{additive families on } A \times T\}/\cong$, with universal family $P$. This is the definition of a [[dual abelian variety|HZXSESHC8P]] in [Volume 1](/learn/abelian-varieties/#duality-and-the-poincar-bundle), with the condition on the fibres replaced by additivity.

The proof first constructs a scheme that represents the functor over a base, with no group structure.

**Definition 1.2.4 (Representative).** Let $S'$ be an $S$-scheme. A *representative of the dual of $A$ over $S'$* is an $S$-morphism $b : B \to S'$ with a line bundle $P$ on $A \times B$ such that $P$ is an additive family and the following holds. For each $S$-scheme $T$, each $S$-morphism $t : T \to S'$ and each additive family $N$ on $A \times T$, there is exactly one $S$-morphism $x : T \to B$ with $b \circ x = t$ and $N \cong P_x$. The representative is *good of dimension $g$* if $b$ is [[proper|9537RKBZPP]], smooth of relative dimension $g$, and has geometrically connected fibres. We write $\mathrm{Rep}_g(A, S')$ for the statement that a good representative of dimension $g$ over $S'$ exists, and $\mathrm{Rep}^{\mathrm{af}}_g(A, S')$ if, in addition, each finite set of points of $B$ lies in an affine open set.

If $S' = S$, the condition $b \circ x = t$ is automatic, and a representative over $S$ represents the same functor as a dual. Over an open set $V$ of $S$, a representative represents the functor of additive families on the restriction $A_V$. The pinching step of a later section needs the property that finite sets lie in affine open sets.

**Definition 1.2.5 (Preserved dimension).** Let $B$ be an $S$-scheme. We say that $B$ *keeps the dimension of $A$* if for each $g$, each scheme $T$ and each morphism $t : T \to S$, if $A \times_S T \to T$ is smooth of relative dimension $g$, then so is $B \times_S T \to T$.

**Lemma 1.2.6 (Change of base).** (a) Let $f : S_1 \to S$ be a morphism and $A_1 = A \times_S S_1$, with its group structure. Then for each $S_1$-scheme $T$ we have $\mathrm{Rep}_g(A_1, T)$ if and only if $\mathrm{Rep}_g(A, T)$, where on the right $T$ is an $S$-scheme through $f$. The same holds for $\mathrm{Rep}^{\mathrm{af}}_g$. (b) If $S'' \to S'$ is a morphism of $S$-schemes and $\mathrm{Rep}_g(A, S')$ holds, then $\mathrm{Rep}_g(A, S'')$ holds.

Lean: `GlobalTheory.T.hasProperSmoothDualRepresentative_grpPullback_iff`, `GlobalTheory.T.baseChangeBis`.

Part (b) is the base change $B \times_{S'} S'' \to S''$ of a representative. We use the lemma as given.

Now let $L$ be a line bundle on $A$.

**Definition 1.2.7 (Mumford class).** For $a, x \in A(Y)$, put
$$\Lambda(L)(a, x) = L(a x) - L(a) - L(x) + L(1) \in \mathrm{Pic}(Y).$$

This is $M(a, x)$ for the bundle $M = m^*L \otimes p_1^*L^{-1} \otimes p_2^*L^{-1} \otimes (e f)^*L$ on $A \times A$, where $f : A \times A \to S$ is the structure map. The last factor makes $\Lambda(L)(1, x) = \Lambda(L)(a, 1) = 0$. If $A$ is an [[abelian scheme|JDDXZ89N33]], the theorem of the cube ([Volume 1](/learn/abelian-varieties/#abelian-schemes)) makes $\Lambda(L)$ additive in each variable. Over a field and for a rational point $x$, the bundle $\Lambda_x$ on $A$ is $t_x^*L \otimes L^{-1}$, the point $\varphi_L(x)$ of the dual in Volume 1.

**Definition 1.2.8 (Kernel of $L$).** For $x \in A(T)$, let $\tau_x : T \times A \to A$ be the map $(t, a) \mapsto x(t) a$. We say that $x$ lies in $K(L)$ if $T$ has an open cover by sets $V$ such that $\tau_x^* L \otimes \mathrm{pr}_A^* L^{-1}$ is trivial on $V \times A$.

So $K(L)(T)$ is the set of $T$-points $x$ for which the translate of $L$ by $x$ is isomorphic to $L$, locally on $T$. Over a field this is the group $K(L)$ of Mumford, *Abelian Varieties*, Chapter II.

**Definition 1.2.9 (Relatively ample).** Let $f : A \to S$ be the structure map. A line bundle $L$ on $A$ is *relatively ample* if for each affine open set $U$ of $S$ there are an integer $N \geq 1$ and sections $s_0, \dots, s_M$ of $L^{\otimes N}$ over $A_U = f^{-1}(U)$ such that the open sets $D(s_i)$ where $s_i$ does not vanish cover $A_U$, each $D(s_i)$ is affine, and the ring $\mathcal{O}(D(s_i))$ is generated as a $\Gamma(U, \mathcal{O}_S)$-algebra by the ratios $s_j / s_i$.

The last two conditions say that $D(s_i) \to \mathbb{A}^M_U$, given by the ratios $s_j/s_i$, is a closed immersion. These maps glue to a morphism $A_U \to \mathbb{P}^M_U$, and the preimage of the chart $x_i \neq 0$ is $D(s_i)$. So the morphism is a closed immersion, and $L^{\otimes N}$ is very ample over $U$. In particular $L$ is ample on each fibre.

**Theorem 1.2.10 (Flat cover).** Let $R$ be a noetherian ring, $A$ an abelian scheme over $\mathrm{Spec}\, R$ that is smooth of relative dimension $g$, and $L$ a relatively ample line bundle on $A$. Let $T$ be an $R$-scheme and $N$ an additive family on $A \times T$. Then there are an $R$-scheme $H$, a morphism $h : H \to T$ that is flat, surjective and quasi-compact, and a morphism $x : H \to A$ such that
$$N(a, h y) = \Lambda(L)(a, x y)$$
for each $R$-scheme $Y$, each $a \in A(Y)$ and each $y \in H(Y)$.

Lean: `GlobalTheory.DualCover.exists_cover` (also `GlobalTheory.T.exists_flatCover_additiveFamily_eq_lambda`, a second name).

The proof uses two facts. Let $\Lambda$ be the bundle on $A \times A$ of the remark after the definition of the Mumford class.

1. (Twisted kernel.) Let $T$ be affine and $N$ an additive family on $A \times T$. Then there is a closed subscheme $H \subseteq A \times T$, finite, flat and surjective over $T$, whose $Y$-points are the $(a, t)$ such that $\Lambda$ at $a$ agrees with $N$ at $t$.
2. (Gluing of agreement loci.) Let $M$ be a line bundle on $A \times U$ and $N$ one on $A \times T$, with $M(1, u) = 0$ and $N(1, t) = 0$ for all points $u$ and $t$. Suppose that for each affine open $V \subseteq T$ the points $(u, t)$ of $U \times V$ where $M$ at $u$ agrees with $N$ at $t$ are the points of a closed subscheme of $U \times V$ that is finite, flat and surjective over $V$. Then the same holds for $U \times T$ over $T$.

Fact 1 is where relative ampleness enters. Over a field it says that the $a$ with $\varphi_L(a) = N_t$ form a torsor under the finite group $K(L)$.

*Proof.* Apply fact 2 with $U = A$ and $M = \Lambda$. Its hypotheses hold: $\Lambda(1, u) = 0$ by the definition of $\Lambda$, and $N(1, t) = 0$ since $N$ is additive. The restriction of $N$ to $A \times V$ is additive, so fact 1 gives the closed subschemes over the affine open sets $V$. So there is a closed subscheme $H \subseteq A \times T$, finite, flat and surjective over $T$, whose $Y$-points are the pairs $(a, t)$ such that $\Lambda$ at $a$ agrees with $N$ at $t$. Let $h : H \to T$ and $x : H \to A$ be the two projections. Then $h$ is flat and surjective, and it is quasi-compact because it is finite. Let $y \in H(Y)$. Then $(x y, h y)$ is a point of $H$, so $\Lambda_{xy} \cong N_{hy}$ on $A \times Y$. Pull back both sides along $(a, 1) : Y \to A \times Y$. This gives $\Lambda(a, x y) = N(a, h y)$, and $\Lambda(a, xy) = \Lambda(L)(a, xy)$. $\square$

**Remark 1.2.11 (Formalization).** Line bundles are given by Čech data: an open cover, and units on the double intersections with $g_{ii} = 1$ and the cocycle rule. An isomorphism $M \cong N$ is a generating section of $N \otimes M^{-1}$, and $\mathrm{Pic}$ is the quotient by this relation. The definitions above are `GlobalTheory.AbDual.IsAdditive`, `GlobalTheory.AbDual.IsDual`, `GlobalTheory.DualCon.Rep` with `GlobalTheory.DualCon.HasRep`, `GlobalTheory.DualCon.HasRepAF`, `GlobalTheory.DualCon.Good` and `GlobalTheory.DualCon.FinAff`; agreement is `GlobalTheory.DualCon.Same`, injectivity is `GlobalTheory.DualCon.Inj`, and preserved dimension is `GlobalTheory.DualCon.DimLe`. The Mumford class is `GlobalTheory.CechPic.lam`, $K(L)$ is `GlobalTheory.MemKL` and relative ampleness is `Out.RelAmple`. The theorem assumes that $A$ is smooth of relative dimension $g$, and this hypothesis is not used ([ExistsFlatCoverAdditiveFamilyEqLambda.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFlatCoverAdditiveFamilyEqLambda.lean#L14)). Facts 1 and 2 are `GlobalTheory.T.exists_twistedKernel_closed_finiteFlat_affineBase` and `GlobalTheory.T.exists_lineBundleFamily_agreementLocus_of_affineOpens`, cited by their statements; the closed immersion of the glued $H$ is not used. The second name is closed by a `first` list under `set_option maxHeartbeats 1000000`.
