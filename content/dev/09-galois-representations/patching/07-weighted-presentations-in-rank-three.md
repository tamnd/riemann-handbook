---
title: Weighted presentations of a rank three deformation ring
decls:
  - UpperTheory.V.UnitaryThreeInertia.exists_unobstructed
  - UpperTheory.V.UnitaryThreeInertia.Rel.card_ker_le
  - UpperTheory.V.UnitaryThreeInertia.exists_relations
  - UpperTheory.V.UnitaryThreeInertia.abstract_count
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weighted presentations of a rank three deformation ring

This section studies the universal deformation ring of a reducible residual representation into the group $\mathcal{G}_3 = \mathrm{GL}_3 \rtimes \{\pm 1\}$ of Clozel, Harris and Taylor. A torus acts on the ring, so the ring is graded by weights. The main results bound the number of relations of each weight by the dimension of an obstruction group of that weight, and then bound the lengths of certain Selmer groups by valuations of traces at finitely many characteristic zero points. The last bound is the abstract form of [the count for case V](/entry/count-v-of-finiteness-duality-euler-host/). The background is in [deformation functors](/learn/deformations-patching/#deformation-functors), [local deformation problems and global deformation rings](/learn/deformations-patching/#local-deformation-problems-and-global-deformation-rings) and [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology).

### Frames and their points

Let $\mathcal{O}$ be a complete discrete valuation ring of characteristic zero with finite residue field $k$. A *CO-algebra* is a complete noetherian local $\mathcal{O}$-algebra $R$ whose structure map is local and whose residue field is $k$.

The group $\mathcal{G}_3(R) = \mathrm{GL}_3(R) \rtimes \{\pm 1\}$ has $-1$ acting by $\theta(g) = J (g^{T})^{-1} J$, where $J$ is the antidiagonal matrix with entries $1$. For a unit $t$ put $\tau(t) = \mathrm{diag}(t, 1, t^{-1})$. Give the entry $(a, b)$ of a $3 \times 3$ matrix the weight $w(a) - w(b)$, where $w = (1, 0, -1)$. So the weights lie in $[-2, 2]$, and conjugation by $\tau(t)$ multiplies an entry of weight $j$ by $t^j$.

A *frame* consists of profinite groups $G$ and $\Gamma$ with a map $G \to \Gamma$, characters $\eta \colon \Gamma \to \{\pm 1\}$ and $\Psi \colon \Gamma \to \mathcal{O}^\times$, an element $c$ of order $2$ with $\eta(c) = -1$, a finite set of places with decomposition and inertia subgroups $D_v \supset I_v$ of $G$, a place $v_l$, and a set $S_b$ of places not containing $v_l$. The *residual point* is
$$r_0(g) = (\tau(\Psi(g)), \eta(g)).$$
A *point* of the frame over a CO-algebra $R$ is a continuous homomorphism $r \colon \Gamma \to \mathcal{G}_3(R)$ with multiplier $\eta$ that reduces to $r_0$, is normalised at $c$ and at a marked element $g_1$, and satisfies local conditions: triangular at $v_l$, diagonal at the places of $S_b$, and trivial on a subgroup $N_v$ of inertia at the other places. A *universal point* is a point $u$ over a CO-algebra $R$ such that each point over a CO-algebra $R'$ is $f_* u$ for exactly one $f \colon R \to R'$.

For $j \in \mathbb{Z}$ let $\mathfrak{g}_j$ be the weight $j$ part of $M_3(k)$, with $\Gamma$ acting through $r_0$ by the adjoint action. Write $H^1_L(j)$ for the Selmer group cut out by the local conditions above, and $\mathrm{Ob}(j)$ for the *obstruction group*: pairs $(c, (a_v)_v)$, where $c$ is a continuous $2$-cocycle of $\Gamma$ with values in $\mathfrak{g}_j$ and each $a_v$ is a continuous $1$-cochain of $D_v$ with $da_v = c|_{D_v}$, modulo pairs $(db, (b|_{D_v})_v)$ and pairs $(0, (z_v)_v)$ with $z_v$ in the local condition. The frame satisfies *Count* if all these spaces are finite-dimensional and
$$\dim H^1_L(j) - \dim \mathrm{Ob}(j) = \delta(j), \qquad \delta(-1) = -1, \quad \delta(1) = \delta(2) = 1, \quad \delta(j) = 0 \text{ otherwise}.$$
This is a global Euler characteristic formula, weight by weight. The frame satisfies *LocVan* if the local $H^2$ in each weight $j \ne 0$ vanishes at $v_l$ and at the places of $S_b$, and the local $H^1$ in each weight $j \ne 0$ vanishes at the places of $S_b$.

### Weights on the deformation ring

Let $u$ be a universal point over $R$. The weight $j$ part $R_j$ is the set of $x \in R$ such that $f'(x) = t^j f(x)$ whenever $f'_* u = \tau(t) (f_* u) \tau(t)^{-1}$. These parts are $\mathcal{O}$-submodules with $R_i R_j \subset R_{i+j}$, and each entry $(a, b)$ of $u(g)$ lies in $R_{w(a) - w(b)}$.

A *weighted presentation* of $R$ is a surjection $\pi \colon \mathcal{O}[[z_s : s \in \sigma]] \to R$, with $\sigma$ finite and each $z_s$ given a weight, whose kernel is homogeneous. It is *adapted* to $u$ if each $z_s$ maps to $u(g)_{ab} - r_0(g)_{ab}$ for some $g$ with $\eta(g) = 1$ of the same weight, and if the image of the weight $j$ power series is $R_j$. It is *minimal* if every element of $\ker \pi$ has all its linear coefficients in the maximal ideal of $\mathcal{O}$.

### Small extensions

**Theorem 7.7.1 (Unobstructed small extensions).** Let $F$ be a frame that satisfies Ok and LocVan, and let $g_1$ be marked. Let $R$ and $R'$ be CO-algebras, with $R$ graded by $\mathcal{O}$-submodules $\mathcal{A}_j$. Let $p \colon R \to R'$ be surjective and $j \in \mathbb{Z}$. Assume that $I = \ker p$ is a *small extension of weight $j$*: $R$ is finite, $\mathfrak{m}_R I = 0$, $I \subset \mathfrak{m}_R$ and $I \subset \mathcal{A}_j$. Assume that $\mathrm{Ob}(j)$ is finite-dimensional and
$$|k|^{\dim \mathrm{Ob}(j)} < |I|.$$
Let $r'$ be a point over $R'$ such that each $r'(g)$ is the image of a matrix over $R$ whose entry $(a, b)$ lies in $\mathcal{A}_{w(a) - w(b)}$. Then there are a CO-algebra $R''$, a surjection $p_1 \colon R \to R''$, a map $q \colon R'' \to R'$ that is not injective with $q p_1 = p$, and a point $r$ over $R''$ with $q_* r = r'$.

Lean: `UpperTheory.V.UnitaryThreeInertia.exists_unobstructed`.

*Proof.* Choose a continuous set-theoretic lift $s \colon \Gamma \to \mathcal{G}_3(R)$ of $r'$ with graded matrices and multiplier $\eta$. At each place $v$, choose a homomorphism $\rho_v \colon D_v \to \mathcal{G}_3(R)$ that lifts $r'|_{D_v}$, satisfies the local condition at $v$ and has graded matrices. LocVan is used here, through the vanishing of the local $H^2$ and $H^1$ in weights $j \ne 0$; there is one lifting lemma for $v_l$, one for the places of $S_b$, and one for the other places.

Put $K(g, h) = s(g) s(h) s(gh)^{-1} - 1$ and $A_v(g) = s(g) \rho_v(g)^{-1} - 1$. Both have entries in $I$ of weight $j$, so they lie in $\mathfrak{g}_j \otimes_k I$, since $\mathfrak{m}_R I = 0$. For each $k$-linear form $\varphi$ on $I$, the pair $(\varphi(K), (\varphi(A_v))_v)$ is a $2$-cocycle of the kind that defines $\mathrm{Ob}(j)$. The map $\varphi \mapsto [\varphi(K), (\varphi(A_v))_v]$ from the dual of $I$ to $\mathrm{Ob}(j)$ is additive. The dual of $I$ has $|I|$ elements, more than $|\mathrm{Ob}(j)|$, so the map is not injective, and there is $\varphi \ne 0$ whose class vanishes.

Let $I_0 \subset I$ be the kernel of $\varphi$, $R'' = R / I_0$, and $q \colon R'' \to R'$ the projection. The kernel of $q$ is $I / I_0 \cong k$, so $q$ is not injective. The image of $s$ in $R''$ has an obstruction class that is the class of $(\varphi(K), (\varphi(A_v))_v)$, which is zero. So the image of $s$ can be corrected by a $1$-cochain with values in $\mathfrak{g}_j \otimes \ker q$ to a homomorphism $r_1$ that satisfies all local conditions and lifts $r'$. A last lemma, on lifting along the surjection $q$ with graded matrices, replaces $r_1$ by a point $r$ that is also normalised at $c$ and $g_1$, still with $q_* r = r'$. $\square$

**Lemma 7.7.2 (Kernels of small extensions).** Let $F$ satisfy Ok, LocVan and Count, let $g_1$ be marked, and let $u$ be a universal point over $R$ with an adapted minimal weighted presentation $\pi \colon P = \mathcal{O}[[z_s]] \to R$. Let $A$ be a graded CO-algebra, $\phi \colon P \to A$ a surjection that preserves weights, and $p \colon A \to A'$ a surjection whose kernel is a small extension of weight $j$ and equals $\phi(\ker \pi)$. Then
$$|\ker p| \le |k|^{\dim \mathrm{Ob}(j)}.$$

Lean: `UpperTheory.V.UnitaryThreeInertia.Rel.card_ker_le`.

*Proof.* Since $\ker p = \phi(\ker \pi)$, the map $p \phi$ factors through $\pi$ as a map $\psi \colon R \to A'$, and $\psi$ is local. Suppose the inequality fails. The point $\psi_* u$ lifts to graded matrices over $A$, so the theorem gives $p_1 \colon A \to R''$, a non-injective $q$ with $q p_1 = p$, and a point $r$ over $R''$ that lifts $\psi_* u$. By universality, $r = s_* u$ for some $s \colon R \to R''$, and $q s = \psi$ by uniqueness.

The two maps $p_1 \phi$ and $s \pi$ from $P$ to $R''$ agree modulo $\ker q$, and $\mathfrak{m}_{R''} \ker q = 0$. Two such maps agree on $\mathfrak{m}_P^2$: for $x, y \in \mathfrak{m}_P$, the product of the two values of $x$ and $y$ differs by terms in $\mathfrak{m}_{R''} \ker q = 0$. So they agree on each $f$ whose linear coefficients lie in $\mathfrak{m}_{\mathcal{O}}$, since $f$ is then a constant plus an element of $\mathfrak{m}_P^2$. By minimality this applies to $f \in \ker \pi$, which gives $p_1(\phi(f)) = s(\pi(f)) = 0$. So $p_1$ kills $\ker p = \phi(\ker \pi)$, and $\ker q = p_1(\ker p) = 0$. This contradicts the choice of $q$. $\square$

**Theorem 7.7.3 (Relations by weight).** Let $F$ satisfy Ok, LocVan and Count, let $g_1$ be marked, and let $u$ be universal over $R$ with an adapted minimal weighted presentation $\pi \colon P \to R$. Then there are power series $f_{j,i}$, for $j \in \mathbb{Z}$ and $1 \le i \le \dim \mathrm{Ob}(j)$, with $f_{j,i}$ of weight $j$, that generate $\ker \pi$.

Lean: `UpperTheory.V.UnitaryThreeInertia.exists_relations`.

*Proof.* Let $J = \ker \pi$. By the Artin-Rees lemma there is $N \ge 1$ with $\mathfrak{m}_P^N \cap J \subset \mathfrak{m}_P J$. Let $T$ be the ideal of power series whose coefficient in each monomial of degree $e$ lies in $\mathfrak{m}_{\mathcal{O}}^{N - e}$. Then $T \subset \mathfrak{m}_P^N$, the quotient $\bar{P} = P/T$ is finite, and it is graded by the images of the weight parts. The image $\bar{J}$ of $J$ is homogeneous.

For each $j$, let $K_j = \mathfrak{m} \bar{J} + (\text{homogeneous elements of } \bar{J} \text{ of weight} \ne j)$. The map $\bar{P}/K_j \to \bar{P}/\bar{J}$ is a small extension of weight $j$, and its kernel is the image of $J$. The lemma gives $|\bar{J}/K_j| \le |k|^{\dim \mathrm{Ob}(j)}$. So the weight $j$ part of $\bar{J}/\mathfrak{m}\bar{J}$ has dimension at most $\dim \mathrm{Ob}(j)$, and there are homogeneous $\bar{f}_{j,i} \in \bar{J}$ of weight $j$ with $\bar{J} \subset (\bar{f}_{j,i}) + \mathfrak{m} \bar{J}$. Lift them to homogeneous $f_{j,i} \in J$ of weight $j$, and let $S$ be the ideal they generate. Then each $x \in J$ is $y + t$ with $y \in S + \mathfrak{m}_P J$ and $t \in T \cap J \subset \mathfrak{m}_P^N \cap J \subset \mathfrak{m}_P J$. So $J \subset S + \mathfrak{m}_P J$, and Nakayama's lemma gives $J = S$. $\square$

### Counting points

For $a \in \mathcal{O}$ nonzero, let $\ell(a)$ be the length of the Selmer group of the character $\Psi^{-1}$ with coefficients in $\mathcal{O}/(a)$: classes unramified on $N_v$ outside $\{v_l\} \cup S_b$ and coboundaries at $v_l$ and on $S_b$. Write $v_l(x) = -\log |x| / \log l$ on $\overline{\mathbb{Q}}_l$ and $e_{\mathcal{O}}$ for the ramification index of $\mathcal{O}$. A representation $r$ over $\overline{\mathbb{Q}}_l$ is of *type I* if it is irreducible on $\ker \eta$, and is *rigid* if its tangent space for the local conditions vanishes. It is a *characteristic zero point* if a conjugate of it by a torus element is a point over the ring of integers of a finite extension of $\mathcal{O}$.

**Theorem 7.7.4 (Abstract count).** Assume the graded algebra lemmas M and M′. Let $F$ satisfy Ok, LocVan, Count, VanE, Cl1 and Xpp, let $g_1$ be marked, and let $u$ be universal over $R$ with $R_0$ finite over $\mathcal{O}$. Let $\varphi \in \Gamma$, and let Good be a property of representations into $\mathcal{G}_3(\overline{\mathbb{Q}}_l)$ that holds for each specialization of $u$ of type I. Assume that each characteristic zero point of type I that is Good is rigid and satisfies $\operatorname{tr} r(\varphi) \ne \operatorname{tr} r_0(\varphi)$. Then there are characteristic zero points $r_1, \dots, r_n$ of type I that are Good and pairwise non-isomorphic on $\ker \eta$, and an integer $V$ with $\ell(a) \le V$ for all $a \ne 0$ and
$$V \le 2 e_{\mathcal{O}} \sum_{i=1}^{n} v_l\bigl(\operatorname{tr} r_i(\varphi) - \operatorname{tr} r_0(\varphi)\bigr).$$

Lean: `UpperTheory.V.UnitaryThreeInertia.abstract_count`.

*Proof.* Choose an adapted minimal presentation. It has an origin, a map $R \to \mathcal{O}$ that sends $u$ to $r_0$. The theorem on relations bounds the relations of weight $j$ by $\dim \mathrm{Ob}(j)$, and Count with the bound on $\dim H^1_L(j)$ gives that the number of variables of weight $j$ is at least $\dim \mathrm{Ob}(j) + \delta(j)$. Let $a = \operatorname{tr} u(\varphi) - \operatorname{tr} r_0(\varphi)$, of weight $0$, which vanishes at the origin.

A point $\xi$ of the weight graded subalgebra determines a unique representation $r_\xi$, with $\xi(a) = \operatorname{tr} r_\xi(\varphi) - \operatorname{tr} r_0(\varphi)$. If $\xi$ is nonzero in some negative and some positive weight, then $r_\xi$ is a characteristic zero point of type I, and so Good. If $\xi$ vanishes in all negative or in all positive weights, then $r_\xi$ is conjugate to $r_0$, and $\xi$ is the origin. Rigidity says that the tangent vectors at a two-sided point are tangent to the torus orbit, and that $\xi(a) \ne 0$. VanE gives that the tangent coordinates of nonpositive weight vanish in the required way. These are the hypotheses of lemmas M and M′ for the graded ring. They give finitely many two-sided points, the integer $V$ with the bound on lengths, and the inequality. Points that are isomorphic on $\ker \eta$ lie in one torus orbit, which gives distinctness. $\square$

**Remark 7.7.5 (Formalization).** The lemma `Rel.card_ker_le` is declared `private` in [ExistsRelations.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/ExistsRelations.lean#L53), but it carries the hypotheses of a stand-alone result. In `abstract_count` ([AbstractCount.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/AbstractCount.lean#L25)) the predicate Good is a free argument: it is only used to pass from the points of the ring to the rigidity hypothesis. The lemmas M and M′ enter as hypotheses `LemmaM → LemmaM' → …` rather than as imported theorems. The conditions VanE, Cl1, Xpp and the local conditions of a point are used through lemmas of the folder and are not unfolded here, and the main counting step is `Abs.coord_count` in [AbsCoord.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/AbsCoord.lean#L68).
