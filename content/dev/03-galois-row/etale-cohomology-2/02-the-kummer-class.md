---
title: The Kummer class
decls:
  - LateralTheory.Fix.EtaleKummerClassExplicitCocycle.holds_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kummer class

Let $X$ be a scheme and $q \geq 1$ an integer that is a unit on $X$. A unit $u$ on $X$ has a *Kummer class* $\kappa(u) \in H^1(X, \mu_q)$. It is the image of $u$ under the connecting map of the Kummer sequence. This section builds $\kappa(u)$ by an explicit cocycle in the cohomology theory of the code, and it proves that $\kappa$ is natural, additive, and zero on $q$-th powers. The naturality is the input to [the naturality of the Kummer class](/entry/nat-kum/), from which the code makes the first Chern class of a line bundle.

**Theorem (Kummer sequence).** Let $X$ be a scheme and let $q$ be a unit on $X$. Then the sequence of sheaves on the étale site of $X$
$$1 \to \mu_q \to \mathbb{G}_m \xrightarrow{\ v \mapsto v^q\ } \mathbb{G}_m \to 1$$
is exact. The connecting map $\delta : \Gamma(X, \mathcal{O}_X)^\times \to H^1(X, \mu_q)$ is a homomorphism. It is natural in $X$, and it is zero on $q$-th powers.

This is J. S. Milne, *Étale Cohomology*, Chapter II, §2, for the exact sequence. The rest follows from the long exact sequence of cohomology. We do not use this theorem. The code builds $\kappa$ directly, and we follow it.

We recall the cohomology of the code. The code works on the big étale site. A *sheaf* is a sheaf of modules on the category of schemes with the étale topology. Each sheaf $F$ has a chosen injective resolution $F \to I^0 \to I^1 \to \cdots$, see [[injective resolution|ZW3W6FX4PW]]. A scheme $X$ gives the simplicial presheaf $\mathrm{sch}(X)$ that is constant in the simplicial direction, and $H^n(X, F)$ is the group of homotopy classes of maps from the chains of $\mathrm{sch}(X)$ to the resolution, shifted by $n$. A cochain $\gamma$ of degree $n$ has components: for each $p \geq 0$, each scheme $U$ and each map $x : U \to X$, a section $\gamma_p(x) \in I^{n-p}(U)$, natural in $U$. For $n = 1$, only $\gamma_0(x) \in I^1(U)$ and $\gamma_1(x) \in I^0(U)$ can be nonzero.

**Definition (Roots of unity and the Tate twist).** For a ring $A$, a *primitive $q$-th root of unity* is a root $\zeta \in A$ of the [[cyclotomic polynomial|08KEYFAH66]] $\Phi_q$, when $q$ is a unit in $A$. The sheaf $\mathbb{Z}/q(1)$ is the sheaf associated to the presheaf that sends $U$ to the free $\mathbb{Z}/q$-module on the primitive roots in $\Gamma(U, \mathcal{O}_U)$, modulo the relations $[\zeta^a] = a\,[\zeta]$ for $a \in (\mathbb{Z}/q)^\times$. For a primitive root $\zeta$ we write $[\zeta] \in I^0(U)$ for the image of its class under $\mathbb{Z}/q(1) \to I^0$.

So $\mathbb{Z}/q(1)$ is a model of $\mu_q$, where $\zeta^a$ corresponds to $[\zeta^a] = a[\zeta]$. The section $[\zeta]$ is a cocycle: $d[\zeta] = 0$, because $I^0 \to I^1$ kills the image of $\mathbb{Z}/q(1)$.

**Definition (Kummer map).** Let $I$ be the resolution of $\mathbb{Z}/q(1)$. A *Kummer map* is a family $t$ of maps $t_U : \Gamma(U, \mathcal{O}_U)^\times \to I^0(U)$, one for each scheme $U$, such that:

1. $t_U(v)|_V = t_V(v|_V)$ for each $g : V \to U$, when $q$ is a unit on $U$;
2. $t_U(\zeta v) = t_U(v) + [\zeta]$ for each primitive $q$-th root of unity $\zeta$ on $U$.

A Kummer map is a lift of $\mathbb{Z}/q(1) \to I^0$ to the units. If $t$ were additive, it would be an extension of $\mu_q \to I^0$ along $\mu_q \to \mathbb{G}_m$, which exists because $I^0$ is an [[injective object|5QRFTBF4PG]]. The code fixes one Kummer map $t$ by choice.

**Definition (Kummer class).** Let $u$ be a unit on $X$ and let $q$ be a unit on $X$. A *Kummer cocycle* for $u$ is a cocycle $\gamma$ of degree $1$ with values in $I$ such that $\gamma_1(x) = 0$ for each $x : U \to X$, and
$$\gamma_0(x) = d\, t_U(v)$$
for each $x : U \to X$ and each unit $v$ on $U$ with $v^q = x^*u$. The *Kummer class* $\kappa(u) \in H^1(X, \mathbb{Z}/q(1))$ is the class of a Kummer cocycle.

The definition in the code chooses a class with this property. The next theorem shows that such a class exists and is unique, so $\kappa(u)$ is well defined.

**Theorem (Kummer class).** Assume that $t$ is a Kummer map for each $q \ne 0$. Let $q \ne 0$. Then:

1. for each scheme $X$ on which $q$ is a unit and each unit $u$ on $X$, there is a Kummer cocycle for $u$, and its class is $\kappa(u)$;
2. for each map $f : Y \to X$ and each unit $u$ on $X$, with $q$ a unit on $X$, we have $f^*\kappa(u) = \kappa(f^*u)$;
3. for units $u$ and $v$ on $X$, with $q$ a unit on $X$, we have $\kappa(uv) = \kappa(u) + \kappa(v)$ and $\kappa(u^q) = 0$.

Lean: `LateralTheory.Fix.EtaleKummerClassExplicitCocycle.holds_of`.

We need two lemmas. The first is a fact on the étale topology, and the second is a fact on cochains of a scheme.

**Lemma (Local roots).** Let $q$ be a unit on $U$. Then locally on $U$ there is a primitive $q$-th root of unity, and each unit on $U$ has a $q$-th root locally on $U$. If $\zeta$ is a primitive $q$-th root of unity on $V$ and $\xi^q = 1$, then locally $\xi = \zeta^a$ for some $a$.

Lean: `LateralTheory.Fix.EtaleKummerClassExplicitCocycle.primLoc`.

*Proof.* The code adjoins a root of $\Phi_q$ to a ring $A$ in which $q$ is a unit. Since $q$ is a unit, $\Phi_q$ divides $T^q - 1$, whose derivative $qT^{q-1}$ is a unit modulo $T^q - 1$. So $A[T]/(\Phi_q(T))$ is a standard étale algebra over $A$. Its map on spectra is surjective, since $\Phi_q$ is monic of positive degree. So it gives an étale covering on which a primitive root exists. The same argument with $T^q - u$ gives the $q$-th roots of $u$. For the last claim, put $e_a = q^{-1} \sum_{b} \zeta^{-ab} \xi^b$ for $a$ in $\mathbb{Z}/q$. Since $\Phi_q(\zeta) = 0$ and $q$ is a unit, $\sum_b \zeta^{cb} = 0$ for $c \ne 0$ in $\mathbb{Z}/q$. So the $e_a$ are orthogonal idempotents with sum $1$, and $\xi e_a = \zeta^a e_a$. On the open and closed piece where $e_a = 1$ we have $\xi = \zeta^a$. We give this argument for the last claim; we did not open its proof in the code. $\square$

**Lemma (Sections from cocycles).** Let $X$ be a scheme, $I$ a complex and $z \in I^n(X)$ with $dz = 0$. Then there is a cocycle $\alpha$ of degree $n$ with $\alpha_0(x) = x^*z$ for each $x : U \to X$ and $\alpha_p = 0$ for $p \geq 1$. A cocycle of this form has class zero if and only if $z = dy$ for some $y \in I^{n-1}(X)$.

Lean: `LateralTheory.Fix.EtaleSchemeGlobalSectionCohomologyClass.intersectionNumber_baseChange`.

*Proof.* We did not open the proof in the code; here is the argument. Put $\alpha_0(x) = x^*z$ and $\alpha_p = 0$ for $p \ge 1$. In $\mathrm{sch}(X)$ all faces of a simplex $x$ are equal to $x$. So the simplicial part of the coboundary of $\alpha$ on a $1$-simplex is $\alpha_0(x) - \alpha_0(x) = 0$, and the part from $I$ is $x^*dz = 0$. $\square$

*Proof of the theorem.* Fix $q$, $X$ and $u$, and let $t$ be the Kummer map.

Existence. Let $v_1, v_2$ be two $q$-th roots of $x^*u$ on $U$. Then $v_2 = \xi v_1$ with $\xi^q = 1$. By the lemma on local roots, locally $\xi = \zeta^a$ for a primitive root $\zeta$. By the second property of $t$, applied $a$ times, $t(v_2) = t(v_1) + a[\zeta]$ locally. Since $d[\zeta] = 0$, we get $d\,t(v_2) = d\,t(v_1)$ locally, and so on $U$, because $I^1$ is a sheaf. Now take an étale covering of $X$ on which $u$ has $q$-th roots. The sections $d\,t(v)$ agree on overlaps by the first property of $t$ and by what we just proved. So they glue to $z \in I^1(X)$, and $dz = 0$ because $dz$ is locally $d\,d\,t(v) = 0$. The lemma on sections gives a cocycle $\alpha$ with $\alpha_0(x) = x^*z$ and $\alpha_1 = 0$. For a root $v$ of $x^*u$ on $U$, the section $x^*z$ equals $d\,t(v)$ locally, so on $U$. So $\alpha$ is a Kummer cocycle.

Uniqueness. Two Kummer cocycles for $u$ have the same components: $\gamma_1 = 0$, and $\gamma_0(x)$ is locally $d\,t(v)$ for any local root $v$. So they are equal, and they have the same class. Hence $\kappa(u)$ is the class of each Kummer cocycle.

Naturality. Let $f : Y \to X$. The pullback of a Kummer cocycle $\gamma$ for $u$ has components $\gamma_p(f \circ y)$ for $y : U \to Y$. A root $v$ of $y^*(f^*u)$ is a root of $(f \circ y)^*u$. So the pullback is a Kummer cocycle for $f^*u$, and $f^*\kappa(u) = \kappa(f^*u)$ by uniqueness.

Additivity. For units $a$, $b$ on a scheme $V$ put $D(a, b) = t(ab) - t(a) - t(b) \in I^0(V)$. If $a$ and $b$ are replaced by $\zeta a$ and $\xi b$ with roots of unity, then $D$ does not change, locally, by the second property of $t$. So for $x : U \to X$ the sections $D(a, b)$, with $a^q = x^*u$ and $b^q = x^*v$ on a covering, glue to a section $Y(x) \in I^0(U)$. These sections are natural in $x$, so they form a cochain $y$ of degree $0$. Then $\gamma_u + \gamma_v + dy$ has component $d\,t(a) + d\,t(b) + d\,D(a, b) = d\,t(ab)$ in simplicial degree $0$, and $0$ in degree $1$, since $y$ is constant along faces. As $(ab)^q = x^*(uv)$, this is a Kummer cocycle for $uv$. So $\kappa(uv) = \kappa(u) + \kappa(v)$. For $u^q$, the global unit $u$ is a $q$-th root. The $0$-cochain $x \mapsto t(x^*u)$ has coboundary $d\,t(x^*u)$ in degree $0$ and $0$ in degree $1$. So a Kummer cocycle for $u^q$ is a coboundary, and $\kappa(u^q) = 0$. $\square$

**Remark.** The code defines $t$ and $\kappa$ by choice: $t$ is a chosen map with the two properties of a Kummer map, and $\kappa(u)$ is a chosen class with a Kummer cocycle. When no such object exists, the choice is an arbitrary default, and nothing can be said. The hypothesis of the theorem, that the chosen $t$ is a Kummer map, removes this problem for $t$. The theorem itself removes it for $\kappa$. In the code, the hypothesis is proved in another file from two statements: an embedding of $\mathbb{Z}/q(1)$ into a sheaf of torsors of roots, and the extension of a map into the injective sheaf $I^0$ through a mono. We did not unfold these two statements. See [EtaleKummerTorsorRootsOfUnityListTorsionExistsOf.lean](lean:Development/EtaleCohomology/TateTwists/EtaleKummerTorsorRootsOfUnityListTorsionExistsOf.lean#L19).

**Remark.** The parent result in the code, the naturality of the Kummer class, uses only the second part of the theorem. The first part is the reason that $\kappa$ is the usual Kummer class: the cocycle $d\,t(v)$ is the image of $u$ under the connecting map of the Kummer sequence, computed with the resolution $I$. The proof of the theorem in the code also uses a lemma on the gluing of sections and a lemma on the local exactness of the resolution. Both are general facts on sheaves, and the code proves them in the same folder.
