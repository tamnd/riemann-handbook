---
title: The Kummer class
decls:
  - LateralTheory.Fix.EtaleKummerClassExplicitCocycle.holds_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kummer class

Let $X$ be a scheme and $q \geq 1$ an integer that is a unit on $X$. A unit $u$ on $X$ has a *Kummer class* $\kappa(u) \in H^1(X, \mu_q)$: the image of $u$ under the connecting map of the Kummer sequence. This section builds $\kappa(u)$ by an explicit cocycle, and [Theorem 4.2.5](/entry/etale-kummer-class-explicit-cocycle-holds-of/) proves that $\kappa$ is well defined, natural, additive, and zero on $q$-th powers. The naturality is the input to [the naturality of the Kummer class](/entry/nat-kum/), which gives the first Chern class of a line bundle.

**Theorem 4.2.1 (Kummer sequence).** Let $X$ be a scheme and let $q$ be a unit on $X$. Then the sequence of sheaves on the étale site of $X$
$$1 \to \mu_q \to \mathbb{G}_m \xrightarrow{\ v \mapsto v^q\ } \mathbb{G}_m \to 1$$
is exact. The connecting map $\delta : \Gamma(X, \mathcal{O}_X)^\times \to H^1(X, \mu_q)$ is a homomorphism. It is natural in $X$, and it is zero on $q$-th powers.

The exactness is in J. S. Milne, *Étale Cohomology*, Chapter II, §2. The rest follows from the long exact sequence of cohomology. We do not use this theorem below. We build $\kappa$ directly from an injective resolution, and the construction is the connecting map of the Kummer sequence written out with cocycles.

We use the following model of étale cohomology. A *sheaf* is a sheaf of $\mathbb{Z}/q$-modules on the category of schemes with the étale topology. Each sheaf $F$ has a fixed injective resolution $F \to I^0 \to I^1 \to \cdots$, see [[injective resolution|ZW3W6FX4PW]]. A scheme $X$ gives the simplicial presheaf $\mathrm{sch}(X)$, $U \mapsto \mathrm{Hom}(U, X)$ in each simplicial degree, with all faces and degeneracies equal to the identity. Let $\mathrm{Ch}(X)$ be its complex of chains. Then $H^n(X, F)$ is the group of homotopy classes of maps of complexes from $\mathrm{Ch}(X)$ to $I^\bullet[n]$. A cochain $\gamma$ of degree $n$ has components: for each $p \geq 0$, each scheme $U$ and each map $x : U \to X$, a section $\gamma_p(x) \in I^{n-p}(U)$, natural in $U$. For $n = 1$, only $\gamma_0(x) \in I^1(U)$ and $\gamma_1(x) \in I^0(U)$ can be nonzero.

**Definition 4.2.2 (Roots of unity and the Tate twist).** For a ring $A$ in which $q$ is a unit, a *primitive $q$-th root of unity* is a root $\zeta \in A$ of the [[cyclotomic polynomial|08KEYFAH66]] $\Phi_q$. The sheaf $\mathbb{Z}/q(1)$ is the sheaf associated to the presheaf that sends $U$ to the free $\mathbb{Z}/q$-module on the primitive roots in $\Gamma(U, \mathcal{O}_U)$, modulo the relations $[\zeta^a] = a\,[\zeta]$ for $a \in (\mathbb{Z}/q)^\times$. For a primitive root $\zeta$ we write $[\zeta] \in I^0(U)$ for the image of its class under $\mathbb{Z}/q(1) \to I^0$.

So $\mathbb{Z}/q(1)$ is a model of $\mu_q$, where $\zeta^a$ corresponds to $[\zeta^a] = a[\zeta]$. The section $[\zeta]$ is a cocycle, $d[\zeta] = 0$, because $\mathbb{Z}/q(1) \to I^0 \to I^1$ is a complex.

**Definition 4.2.3 (Kummer map).** Let $I$ be the resolution of $\mathbb{Z}/q(1)$. A *Kummer map* is a family $t$ of maps $t_U : \Gamma(U, \mathcal{O}_U)^\times \to I^0(U)$, one for each scheme $U$, such that:

1. $t_U(v)|_V = t_V(v|_V)$ for each $g : V \to U$, when $q$ is a unit on $U$;
2. $t_U(w) = t_U(v) + [\zeta]$ for all units $v, w$ on $U$ and each primitive $q$-th root of unity $\zeta$ on $U$ with $w = \zeta v$.

A Kummer map is a lift of $\mathbb{Z}/q(1) \to I^0$ to the units. If $t$ were additive, it would be an extension of $\mu_q \to I^0$ along $\mu_q \to \mathbb{G}_m$, which exists because $I^0$ is an [[injective object|5QRFTBF4PG]]. For each $q \geq 1$ we fix one family $t$, and we assume below that it is a Kummer map.

**Definition 4.2.4 (Kummer class).** Let $u$ be a unit on $X$. A *Kummer cocycle* for $u$ is a cocycle $\gamma$ of degree $1$ with values in $I$ such that $\gamma_1(x) = 0$ for each $x : U \to X$, and
$$\gamma_0(x) = d\, t_U(v)$$
for each $x : U \to X$ and each unit $v$ on $U$ with $v^q = x^*u$. The *Kummer class* $\kappa(u) \in H^1(X, \mathbb{Z}/q(1))$ is the class of a Kummer cocycle, chosen once for each $u$. If no Kummer cocycle exists, we put $\kappa(u) = 0$.

The next theorem shows that a Kummer cocycle exists when $q$ is a unit on $X$, and that all Kummer cocycles for $u$ have the same class.

**Theorem 4.2.5 (Kummer class).** Assume that for each $q \geq 1$ the fixed family $t$ is a Kummer map. Let $q \geq 1$. Then:

1. for each scheme $X$ on which $q$ is a unit and each unit $u$ on $X$, there is a Kummer cocycle for $u$ whose class is $\kappa(u)$;
2. for each map $f : Y \to X$ and each unit $u$ on $X$, with $q$ a unit on $X$, we have $f^*\kappa(u) = \kappa(f^*u)$;
3. for units $u$ and $v$ on $X$, with $q$ a unit on $X$, we have $\kappa(uv) = \kappa(u) + \kappa(v)$ and $\kappa(u^q) = 0$.

Lean: `LateralTheory.Fix.EtaleKummerClassExplicitCocycle.holds_of`.

We need two lemmas. The first is a fact on the étale topology, and the second is a fact on cochains of a scheme.

**Lemma 4.2.6 (Local roots).** Let $q \geq 1$ and let $U$ be a scheme.

1. If $q$ is a unit on $U$, then locally on $U$ there is a primitive $q$-th root of unity.
2. If $\zeta$ and $\xi$ are primitive $q$-th roots of unity on $U$, then locally $\xi = \zeta^a$ for some $a \in (\mathbb{Z}/q)^\times$.
3. If $\zeta$ is a primitive $q$-th root of unity on $U$ and $x \in \Gamma(U, \mathcal{O}_U)$ satisfies $x^q = 1$, then locally $x = \zeta^a$ for some $a \geq 0$.
4. If $q$ is a unit on $U$, then each unit on $U$ has a $q$-th root locally on $U$.

Lean: `LateralTheory.Fix.EtaleKummerClassExplicitCocycle.primLoc`.

*Proof.* For 1, let $A = \Gamma(W, \mathcal{O}_W)$ for an affine open $W \subseteq U$. Since $q$ is a unit in $A$, $\Phi_q$ divides $T^q - 1$, whose derivative $qT^{q-1}$ is a unit modulo $T^q - 1$. So $A[T]/(\Phi_q(T))$ is a standard étale algebra over $A$. Its map on spectra is surjective, since $\Phi_q$ is monic of positive degree. So these maps, for a cover of $U$ by affine opens, form an étale covering on which a primitive root exists. The same argument with $T^q - u$ proves 4.

For 3, fix a point $y \in U$ with residue field $k(y)$. The image of $\zeta$ in $k(y)$ is a primitive $q$-th root of unity, since $q \ne 0$ in $k(y)$. So the image of $x$ is the image of $\zeta^n$ for some $0 \le n < q$. Put $t = x \zeta^{q-n}$ and $s = \sum_{i=0}^{q-1} t^i$. Then $t^q = 1$, so $s(t - 1) = 0$, and so $s(x - \zeta^n) = s(t - 1)\zeta^n = 0$. The image of $t$ in $k(y)$ is $1$, so $s(y) = q \ne 0$. On an affine open neighbourhood of $y$ inside $\{s \ne 0\}$, $s$ is a unit, and so $x = \zeta^n$ there. These opens cover $U$. For 2, apply this with $x = \xi$. The image of $\xi = \zeta^n$ in $k(y)$ is again primitive, so $n$ is prime to $q$, and $a = n \bmod q$ is a unit. $\square$

**Lemma 4.2.7 (Sections and cocycles).** Let $X$ be a scheme, $I$ a complex of sheaves and $n \in \mathbb{Z}$.

1. For each $z \in I^n(X)$ with $dz = 0$ there is a cocycle $\alpha$ of degree $n$ with $\alpha_0(x) = x^*z$ for each $x : U \to X$ and $\alpha_p = 0$ for $p \geq 1$.
2. For each cocycle $\alpha$ of degree $n$, the section $a = \alpha_0(\mathrm{id}_X) \in I^n(X)$ satisfies $da = 0$, and the class of $\alpha$ is zero if and only if $a = dy$ for some $y \in I^{n-1}(X)$.

Lean: `LateralTheory.Fix.EtaleSchemeGlobalSectionCohomologyClass.intersectionNumber_baseChange`.

*Proof.* In $\mathrm{sch}(X)$ all faces are the identity. So the boundary map of $\mathrm{Ch}(X)$ from degree $p$ to degree $p - 1$ is $\sum_{i=0}^{p} (-1)^i = 0$ for $p$ odd, and the identity for $p \geq 2$ even. The coboundary of a cochain $\alpha$ in simplicial degree $p$ is $d\alpha_p \pm \alpha_{p-1} \circ \partial$.

For 1, put $\alpha_0(x) = x^*z$ and $\alpha_p = 0$ for $p \geq 1$. In simplicial degree $0$ the coboundary is $x^*dz = 0$. In degree $1$ it is $\pm \alpha_0 \circ \partial = 0$, since $\partial = 0$ there. In higher degrees all terms vanish.

For 2, the coboundary in simplicial degree $0$ is $d\alpha_0$, so $da = 0$. If $\alpha = D\beta$, then $\alpha_0 = d\beta_0$, so $a = d\beta_0(\mathrm{id}_X)$. Conversely, let $a = dy$. Let $\beta$ be the cochain of degree $n - 1$ with $\beta_0(x) = x^*y$ and $\beta_p = 0$ for $p \geq 1$. Then $\alpha - D\beta$ is a cocycle with zero component in degree $0$, because $\alpha_0(x) = x^*a$ by naturality. The complex $\mathrm{Ch}(X)$ is chain homotopy equivalent to its term in degree $0$, since in degrees $p \ge 1$ it is a sum of copies of $C \xrightarrow{\ \mathrm{id}\ } C$. So a cocycle with zero component in degree $0$ is a coboundary, and $\alpha$ has class zero. $\square$

*Proof of the theorem.* Fix $q$, $X$ and $u$, with $q$ a unit on $X$.

Existence. Let $v_1, v_2$ be two $q$-th roots of $x^*u$ on $U$. Then $v_2 = \xi v_1$ with $\xi^q = 1$. By the lemma on local roots, locally there is a primitive root $\zeta$, and locally $\xi = \zeta^a$. By the second property of $t$, applied $a$ times, $t(v_2) = t(v_1) + a[\zeta]$ locally. Since $d[\zeta] = 0$, we get $d\,t(v_2) = d\,t(v_1)$ locally, and so on $U$, because $I^1$ is a sheaf. Now take an étale covering of $X$ on which $u$ has $q$-th roots. The sections $d\,t(v)$ agree on overlaps by the first property of $t$ and by what we just proved. So they glue to $z \in I^1(X)$, and $dz = 0$ because $dz$ is locally $d\,d\,t(v) = 0$. Part 1 of the lemma on sections and cocycles gives a cocycle $\alpha$ with $\alpha_0(x) = x^*z$ and $\alpha_1 = 0$. For a root $v$ of $x^*u$ on $U$, the section $x^*z$ equals $d\,t(v)$ locally, so on $U$. So $\alpha$ is a Kummer cocycle.

Uniqueness. Two Kummer cocycles for $u$ have the same components: $\gamma_1 = 0$, and $\gamma_0(x)$ is locally $d\,t(v)$ for any local root $v$. So they are equal, and they have the same class. Hence the chosen class $\kappa(u)$ is the class of each Kummer cocycle. This proves 1.

Naturality. Let $f : Y \to X$. The pullback of a Kummer cocycle $\gamma$ for $u$ has components $\gamma_p(f \circ y)$ for $y : U \to Y$. A root $v$ of $y^*(f^*u)$ is a root of $(f \circ y)^*u$. So the pullback is a Kummer cocycle for $f^*u$, and $f^*\kappa(u) = \kappa(f^*u)$ by uniqueness.

Additivity. For units $a$, $b$ on a scheme $V$ put $D(a, b) = t(ab) - t(a) - t(b) \in I^0(V)$. If $a$ and $b$ are replaced by $\zeta a$ and $\xi b$ with roots of unity, then $D$ does not change, locally, by the second property of $t$ and the lemma on local roots. So for $x : U \to X$ the sections $D(a, b)$, with $a^q = x^*u$ and $b^q = x^*v$ on a covering, glue to a section $y(x) \in I^0(U)$. These sections are natural in $x$, so they form a cochain $y$ of degree $0$ with $y_p = 0$ for $p \ge 1$. Then $\gamma_u + \gamma_v + Dy$ has component $d\,t(a) + d\,t(b) + d\,D(a, b) = d\,t(ab)$ in simplicial degree $0$, and $0$ in degree $1$, since $y$ is constant along faces. As $(ab)^q = x^*(uv)$, this is a Kummer cocycle for $uv$. So $\kappa(uv) = \kappa(u) + \kappa(v)$. For $u^q$, the global unit $u$ is a $q$-th root. The $0$-cochain $x \mapsto t(x^*u)$ has coboundary $d\,t(x^*u)$ in degree $0$ and $0$ in degree $1$. So a Kummer cocycle for $u^q$ is a coboundary, and $\kappa(u^q) = 0$. $\square$

**Remark 4.2.8 (Formalization).** The Kummer map $t$ and the class $\kappa(u)$ are defined by choice, with the value $0$ when no object with the required property exists. The hypothesis of the theorem says that the chosen $t$ is a Kummer map for each $q \geq 1$. It is proved elsewhere from two statements: an embedding of $\mathbb{Z}/q(1)$ into a sheaf of torsors of roots, and the extension of a map into the injective sheaf $I^0$ through a monomorphism; see [EtaleKummerTorsorRootsOfUnityListTorsionExistsOf.lean](lean:Development/EtaleCohomology/TateTwists/EtaleKummerTorsorRootsOfUnityListTorsionExistsOf.lean#L19). We did not unfold these two statements. The proof of the lemma on sections and cocycles given here is our own argument; we did not open its Lean proof.
