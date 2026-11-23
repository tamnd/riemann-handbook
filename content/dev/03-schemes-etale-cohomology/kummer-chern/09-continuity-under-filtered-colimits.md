---
title: Continuity under filtered colimits
decls:
  - LateralTheory.Fin.Cont.intersectionNumber_baseChange
  - LateralTheory.Fin.Cont.etale_kunneth_cohomology_continuous_under_limits_in_continuity_assembl
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Continuity under filtered colimits

Let $X$ be a quasi-compact and separated scheme over a ring $R$, and let $D = \varinjlim D_j$ be a filtered colimit of $R$-algebras. This section proves that the étale cohomology of $X \times_R \operatorname{Spec} D$ with coefficients $\mathbb{Z}/q(i)$ is the colimit of the cohomology of the schemes $X \times_R \operatorname{Spec} D_j$. We take the affine case as an axiom, and we use induction on the number of affine opens that cover $X$, with the Mayer-Vietoris sequence and the five lemma. The result is used in [the theorem that classes are killed on an étale neighbourhood](/entry/cont-of/).

The cohomology $H^n(X, F)$, its cochains with components $\alpha_p(x)$, and the sheaves $\mathbb{Z}/q(i)$ are as in the section before [the theorem on the Kummer class](/entry/etale-kummer-class-explicit-cocycle-holds-of/). Each sheaf $F$ has a fixed injective resolution $F \to I^\bullet$, and we also write $H^n(X, I)$ for $H^n(X, F)$. A map $f : Y \to X$ gives a pullback $f^*$ on cohomology.

**Theorem 4.9.1 (Continuity, standard form).** Let $X_0$ be a quasi-compact and quasi-separated scheme, let $(X_j)$ be a filtered inverse system of $X_0$-schemes with affine transition maps, and let $X = \varprojlim X_j$. Let $F$ be a sheaf on $X_0$. Then $H^n(X, F) = \varinjlim_j H^n(X_j, F)$ for all $n$.

See J. S. Milne, *Étale Cohomology*, Chapter III, §1. We prove the case $X_j = X_0 \times_R \operatorname{Spec} D_j$ and $F = \mathbb{Z}/q(i)$.

**Definition 4.9.2 (Continuity of a functor).** Let $J$ be a [[filtered category|975PMY4FG8]], let $D : J \to K$ be a functor with a cocone $D_j \to D_\infty$, and let $G$ be a functor from $K$ to abelian groups. We say that $G$ is *continuous* on the cocone if two conditions hold. First, each $x \in G(D_\infty)$ is the image of some $y \in G(D_j)$. Second, if $y \in G(D_j)$ maps to $0$ in $G(D_\infty)$, then $y$ maps to $0$ in $G(D_k)$ for some arrow $j \to k$.

If the cocone is a [[colimit|BJS1CGTKQ5]], continuity says that $\varinjlim G(D_j) \to G(D_\infty)$ is bijective.

**Definition 4.9.3 (The two axioms).** We use two axioms on cohomology.

1. *Affine continuity.* Let $q \geq 0$, let $(D_j)$ be a filtered diagram of rings with colimit $D_\infty$, and let $n, i \in \mathbb{Z}$. If $q$ is a unit in $D_\infty$, then each $x \in H^n(\operatorname{Spec} D_\infty, \mathbb{Z}/q(i))$ is the image of a class on some $\operatorname{Spec} D_j$. If $q$ is a unit in $D_j$ and $y \in H^n(\operatorname{Spec} D_j, \mathbb{Z}/q(i))$ maps to $0$ on $\operatorname{Spec} D_\infty$, then $y$ maps to $0$ on $\operatorname{Spec} D_k$ for some arrow $j \to k$.
2. *Smooth descent.* For each smooth surjective map $f : Y \to X$ and each sheaf $F$, the augmentation from the Čech nerve of $f$ to $X$ induces bijections on $H^n(-, F)$ for all $n$.

The first axiom is the affine case of the standard theorem above. The proof below does not use the second axiom.

**Theorem 4.9.4 (Continuity).** Assume the two axioms. Let $q \geq 1$, let $R$ be a ring in which $q$ is a unit, and let $p : X \to \operatorname{Spec} R$ be quasi-compact and separated. Let $(D_j)$ be a filtered diagram of $R$-algebras with colimit $D_\infty$. For an $R$-algebra $A$ write $X_A = X \times_{\operatorname{Spec} R} \operatorname{Spec} A$. Then for all $n, i \in \mathbb{Z}$ the functor $A \mapsto H^n(X_A, \mathbb{Z}/q(i))$ is continuous on the cocone $D_j \to D_\infty$.

Lean: `LateralTheory.Fin.Cont.etale_kunneth_cohomology_continuous_under_limits_in_continuity_assembl` (also `LateralTheory.Fin.Cont.intersectionNumber_baseChange`, a second name).

Let $I$ be a complex of sheaves and $X$ a scheme. A section $a \in I^n(X)$ *represents* a class $x \in H^n(X, I)$ if $x$ is the class of a cocycle $\alpha$ with $\alpha_0(\mathrm{id}_X) = a$ and $\alpha_p = 0$ for all $p \geq 1$.

**Lemma 4.9.5 (Dictionary).** Let $X$ be a scheme, $I$ a complex of sheaves and $n \in \mathbb{Z}$.

1. Each $a \in I^n(X)$ with $da = 0$ represents some class.
2. Each class in $H^n(X, I)$ is represented by some section.
3. If $a$ represents $x$, then $da = 0$, and $x = 0$ if and only if $a = db$ for some $b \in I^{n-1}(X)$.
4. If $a$ represents $x$ and $a'$ represents $x'$, then $a + a'$ represents $x + x'$ and $-a$ represents $-x$.
5. If $a$ represents $x$ and $f : Y \to X$ is a map, then $f^*a$ represents $f^*x$.

Lean: `LateralTheory.KummerTheory.Dict_of'`.

*Proof.* Parts 1 and 3 are the lemma on sections and cocycles in the section on the Kummer class. For 2, recall from there that the chain complex $\mathrm{Ch}(X)$ has the zero map from degree $1$ to degree $0$. So the projection $\pi$ of $\mathrm{Ch}(X)$ onto its term in degree $0$ is a map of complexes, and with the inclusion $\iota$ of that term it is a chain homotopy equivalence. A cocycle $\alpha$ is thus cohomologous to $\alpha \circ \iota \circ \pi$, whose components in simplicial degree $p \ge 1$ are zero. For 4, sums and negatives of such cocycles are again of this form. For 5, the pullback of $\alpha$ has components $\alpha_p(f \circ y)$. They are zero for $p \ge 1$, and $\alpha_0(f) = f^*a$ by naturality. $\square$

So $H^n(X, I)$ is the $n$-th cohomology group of the complex $I^\bullet(X)$ of global sections, naturally in $X$.

**Definition 4.9.6 (Mayer-Vietoris square).** A *Mayer-Vietoris square* is a pullback square of schemes
$$\begin{array}{ccc} W & \xrightarrow{a} & U \\ {\scriptstyle b}\downarrow & & \downarrow{\scriptstyle f} \\ V & \xrightarrow{g} & X \end{array}$$
in which $f$ and $g$ are [[open immersions|GFC5YKSN5H]] and each point of $X$ lies in the image of $f$ or of $g$.

So $X = U \cup V$ and $W = U \cap V$.

We use a weak form of a long exact sequence. Let $K$ be a category. A *Mayer-Vietoris sequence* of functors on $K$ consists of functors $X_n, U_n, V_n, W_n$ from $K$ to abelian groups, for $n \in \mathbb{Z}$, and natural maps $f_n : X_n \to U_n$, $g_n : X_n \to V_n$, $a_n : U_n \to W_n$, $b_n : V_n \to W_n$ and $\delta_n : W_n \to X_{n+1}$, such that at each object of $K$:

1. $a_n f_n = b_n g_n$;
2. if $a_n(u) = b_n(v)$, then $u = f_n(x)$ and $v = g_n(x)$ for some $x$;
3. if $x \in X_{n+1}$ satisfies $f_{n+1}(x) = 0$ and $g_{n+1}(x) = 0$, then $x = \delta_n(w)$ for some $w$;
4. $\delta_n(w) = 0$ if and only if $w = a_n(u) - b_n(v)$ for some $u$ and $v$.

**Lemma 4.9.7 (Mayer-Vietoris sequence).** Let $F$ be a sheaf with resolution $I$, and let a Mayer-Vietoris square be given. For $w \in H^n(W, F)$ and $x \in H^{n+1}(X, F)$, say that $w$ and $x$ are *linked* if there are $s \in I^n(U)$ and $z \in I^{n+1}(X)$ such that $a^*s$ represents $w$, $z$ represents $x$, $f^*z = ds$ and $g^*z = 0$.

1. For each $n$ there is a homomorphism $\delta : H^n(W, F) \to H^{n+1}(X, F)$ such that $\delta(w) = x$ if and only if $w$ and $x$ are linked.
2. If $a^*u = b^*v$, then $u = f^*x$ and $v = g^*x$ for some $x \in H^n(X, F)$. If $x \in H^{n+1}(X, F)$ satisfies $f^*x = 0$ and $g^*x = 0$, then $x$ is linked to some $w$. The class $w$ is linked to $0$ if and only if $w = a^*u - b^*v$ for some $u$ and $v$.
3. Let $K$ be a category, and let $k \mapsto (W_k, U_k, V_k, X_k)$ be a functor from $K$ to the opposite of the category of commutative squares of schemes, such that each square is a Mayer-Vietoris square. Then there is a Mayer-Vietoris sequence of functors on $K$ with terms $H^n(X_k, F)$, $H^n(U_k, F)$, $H^n(V_k, F)$ and $H^n(W_k, F)$.

Lean: `LateralTheory.KummerTheory.MVnatPf.MVnat_of` (also `LateralTheory.KummerTheory.ExactPf.Exact_of` and `LateralTheory.KummerTheory.ContCut.Delta_of`).

*Proof.* We use two facts on sections. First, the [[sheaf|RT8A8FJ566]] property for the covering $\{U, V\}$ of $X$: a section on $X$ that vanishes on $U$ and on $V$ is zero, and sections on $U$ and $V$ that agree on $W$ glue to a section on $X$. Second, each injective sheaf $G$ restricts surjectively along a monomorphism $W \to U$: the map of free sheaves $\mathbb{Z}[W] \to \mathbb{Z}[U]$ is a monomorphism, and $G(U) = \operatorname{Hom}(\mathbb{Z}[U], G)$ maps onto $\operatorname{Hom}(\mathbb{Z}[W], G) = G(W)$ because $G$ is injective. So the sequence of complexes
$$0 \to I^\bullet(X) \xrightarrow{(f^*, g^*)} I^\bullet(U) \oplus I^\bullet(V) \xrightarrow{a^* - b^*} I^\bullet(W) \to 0$$
is exact. By the dictionary, its long exact cohomology sequence is a sequence of the groups $H^n(-, F)$, with pullbacks as maps, and this gives 2. Let $\delta$ be the connecting map, and let $s|_W$ represent $w$. Then $(s, 0)$ lifts $s|_W$, and $(ds, 0)$ glues to a section $z$ on $X$ with $f^*z = ds$ and $g^*z = 0$. So $\delta(w)$ is the class that $z$ represents, and $\delta(w) = x$ exactly when $w$ and $x$ are linked. This gives 1. For 3, these constructions commute with pullback along maps of squares, and conditions 1 to 4 are parts of 2. $\square$

**Lemma 4.9.8 (Five lemma for colimits).** Let $K$ be a category, and let $(X_n, U_n, V_n, W_n)$ be a Mayer-Vietoris sequence of functors on $K$. Let $J$ be a filtered category, and let $D : J \to K$ be a functor with a cocone $D_j \to D_\infty$. If $U_n$, $V_n$ and $W_n$ are continuous on the cocone for all $n$, then so is $X_n$ for all $n$.

Lean: `LateralTheory.KummerTheory.FivePf.Five_of`.

*Proof.* Fix $n$ and write $X_n = X_{m+1}$ with $m = n - 1$. Since $J$ is filtered, finitely many elements at stages can be moved to one common stage. We write $\bar y$ for the image in $D_\infty$ of an element $y$ at a stage, and we drop the indices of the maps.

Surjectivity. Let $x \in X_{m+1}(D_\infty)$. By continuity of $U$ and $V$ there are $u$ and $v$ at a stage $j$ with $\bar u = f(x)$ and $\bar v = g(x)$. Then $a(u) - b(v)$ maps to $a f(x) - b g(x) = 0$, so it is zero at a later stage $k$, by continuity of $W$. By condition 2 there is $x'$ at stage $k$ with $f(x') = u$ and $g(x') = v$ there. Now $x - \bar{x}'$ is killed by $f$ and $g$, so by condition 3 it is $\delta(w)$ with $w \in W_m(D_\infty)$. Let $w'$ at a stage lift $w$. Then $x$ is the image of $x' + \delta(w')$, moved to a common stage.

Injectivity. Let $y \in X_{m+1}(D_j)$ with $\bar y = 0$. Then $f(y)$ and $g(y)$ map to zero, so they are zero at a later stage $k$. By condition 3, $y = \delta(w)$ there. Then $\delta(\bar w) = 0$, so $\bar w = a(u) - b(v)$ by condition 4. Lift $u$ and $v$ to $u'$ and $v'$ at a stage. The element $w - a(u') + b(v')$ maps to $0$, so it is zero at a later stage $l$. At $l$ we get $y = \delta(a(u') - b(v')) = 0$, by condition 4 again. $\square$

**Lemma 4.9.9 (Induction on covers).** Let $R$ be a ring, and let $P$ be a property of schemes $X$ with a map $p : X \to \operatorname{Spec} R$. Assume that $P$ holds for each affine $X$ and each $p$. Assume that for each Mayer-Vietoris square and each $p : X \to \operatorname{Spec} R$, if $P$ holds for $U$, $V$ and $W$ with the composite maps to $\operatorname{Spec} R$, then it holds for $(X, p)$. Then $P$ holds for each $(X, p)$ with $p$ quasi-compact and [[separated|X30G4V7VAJ]].

Lean: `LateralTheory.KummerTheory.IndPf.Ind_of`.

*Proof.* Since $\operatorname{Spec} R$ is affine, $X$ is [[quasi-compact|41009J4M5D]] and separated. So $X$ is a union of affine opens $U_1, \dots, U_m$. We use induction on $m$. For $m = 1$, $X$ is affine. For $m > 1$, put $U = U_1$ and $V = U_2 \cup \dots \cup U_m$. Then $W = U \cap V$ is the union of the opens $U_1 \cap U_k$ for $k \ge 2$. These are affine, because the intersection of two affine opens of a separated scheme is affine. So $V$ and $W$ are unions of $m - 1$ affine opens. They are opens of $X$, so they are quasi-compact and separated over $\operatorname{Spec} R$. By induction $P$ holds for $U$, $V$ and $W$, so for $X$. $\square$

**Lemma 4.9.10 (Base change).** The base change of a Mayer-Vietoris square over $\operatorname{Spec} R$ along $\operatorname{Spec} A \to \operatorname{Spec} R$ is a Mayer-Vietoris square.

Lean: `LateralTheory.KummerTheory.BCPf.BC_of`.

*Proof.* Open immersions and pullback squares are stable under base change. A point of $X_A$ maps to a point of $X$, which lies in the image of $U$ or of $V$. Since $U_A = U \times_X X_A$, the point lies in the image of $U_A$ or of $V_A$. $\square$

**Lemma 4.9.11 (Affine case).** Let $X$ be affine with a map $p : X \to \operatorname{Spec} R$.

1. There is a functor $T$ from $R$-algebras to rings with $X_A \cong \operatorname{Spec} T(A)$, naturally in $A$. Each $T(A)$ receives a ring map from $R$, and $T$ takes filtered colimits to colimits.
2. Assume affine continuity, and let $q$ be a unit in $R$. Then for all $n$, $i$ the functor $A \mapsto H^n(X_A, \mathbb{Z}/q(i))$ is continuous on each filtered colimit of $R$-algebras.

Lean: `LateralTheory.KummerTheory.AffPf.Aff_of` (also `LateralTheory.KummerTheory.AffRingPf.AffRing_of`).

*Proof.* Write $X = \operatorname{Spec} B$. Then $X_A = \operatorname{Spec}(A \otimes_R B)$, naturally in $A$, so $T(A) = A \otimes_R B$ works. Filtered colimits of $R$-algebras are computed on the underlying modules, and the tensor product preserves colimits. This proves 1. For 2, $q$ is a unit in each $T(A)$, because it receives a map from $R$. Apply affine continuity to the filtered diagram $(T(D_j))$ with colimit $T(D_\infty)$. $\square$

*Proof of the theorem.* Let $P(X)$ be the property: for all $n$, the functor $A \mapsto H^n(X_A, \mathbb{Z}/q(i))$ is continuous on the cocone $D_j \to D_\infty$. By the affine case, $P$ holds for affine $X$. Let a Mayer-Vietoris square over $\operatorname{Spec} R$ be given, with $P$ for $U$, $V$ and $W$. By the base change lemma, for each $R$-algebra $A$ the base changed square is a Mayer-Vietoris square, and it is natural in $A$. Part 3 of the Mayer-Vietoris lemma gives a Mayer-Vietoris sequence of functors of $A$. The five lemma for colimits gives $P$ for $X$. By induction on covers, $P$ holds for each $X$ that is quasi-compact and separated over $\operatorname{Spec} R$. $\square$

**Remark 4.9.12 (Formalization).** Both axioms are hypotheses of the theorem. The formal proof drops smooth descent at the first step; see [ContCut.lean](lean:Development/EtaleCohomology/KummerTheory/ContCut.lean#L117). The Mayer-Vietoris sequence of the formal statement asks only for conditions 1 to 4. It does not ask that $f_{n+1} \circ \delta_n = 0$, and in part 3 of the Mayer-Vietoris lemma it does not say that the maps are pullbacks. We did not open the formal proof that injective sheaves restrict surjectively; the argument above is the standard one. The names of the theorem speak of a Künneth formula, an intersection number and a base change, which do not occur in it.
