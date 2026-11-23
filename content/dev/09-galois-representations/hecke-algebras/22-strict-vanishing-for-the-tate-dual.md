---
title: Strict vanishing for the Tate dual
decls:
  - GlobalTheory.T.strict_vanishing_dual_of_literature
  - GlobalTheory.Ord2.StrictKill.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Strict vanishing for the Tate dual

This section proves the first vanishing theorem of the Euler system method for a two-dimensional representation $W$ in normal form. If $W$ has an Euler system class $y$ that is not ordinary at $\ell$, then the strict Selmer group of the Tate dual $W^*$ vanishes: a cocycle of $W^*$ that is unramified away from $\ell$ and trivial on the decomposition group at $\ell$ is a coboundary. The proof pairs $y$ with such a cocycle $z$, forms the height of Section 21, and evaluates it on two commutators that differ by an element of $N$. Sections 23 and 24 pass from this statement to the vanishing of the ordinary Selmer groups of $W^*$ and $W$.

We keep the notation of Sections 18, 20 and 21.

### Selmer conditions

Let $V$ be $W$ or $W^*$, and $c$ a cocycle for $V$.

**Definition 6.22.1 (Local conditions).** The cocycle $c$ is

1. *unramified* if for each prime $q \neq \ell$ there are a place $B$ over $q$ and $x$ with $c(s) = V(s)x - x$ for $s \in I_B$;
2. *ordinary at $A$* if there is $x \in \overline{\mathbb{Q}}_\ell$ with $c(s)_2 = V(s)_{22}\,x - x$ for $s \in D_A$;
3. *trivial at $A$* if there is $x \in \overline{\mathbb{Q}}_\ell^2$ with $c(s) = V(s)x - x$ for $s \in D_A$.

The *ordinary Selmer group of $V$ vanishes* if every unramified cocycle that is ordinary at $A$ is a coboundary. The *strict Selmer group of $V$ vanishes* if every unramified cocycle that is trivial at $A$ is a coboundary.

When $V$ is upper triangular on $D_A$, the second coordinate of $c$ on $D_A$ is a cocycle for the quotient character $V_{22}$, and "ordinary" says that its class vanishes. These are the conditions of R. Greenberg, *Iwasawa theory for p-adic representations*, in: Algebraic Number Theory (Adv. Stud. Pure Math. 17, 1989), 97 to 137. The conditions are imposed on all of $D_A$, not only on $I_A$.

**Definition 6.22.2 (Euler system datum).** An *Euler system datum* for $(W, A)$ is a coefficient datum with ring $\mathcal{O}$, a map $y$ and a finite set $S'$ of places such that the entries of $W$ lie in $\mathcal{O}$, $y$ is a cocycle for $W$ with values in $\mathcal{O}^2$, $y$ is unramified, $y$ is *not* ordinary at $A$, and $y$ has a tame class at $(w, n, \psi)$ for all $n \geq 1$, all $w \notin S'$ with $\ell^n \mid w - 1$, and all surjective $\psi : G_{\mathbb{Q}} \to \mathbb{Z}/\ell^n$ trivial on $\mathrm{Gal}(\Omega/\mathbb{Q}(\mu_w))$.

So $y$ is an Euler system class in the sense of Section 18 that is not ordinary at $A$. [The theorem on zeta classes](/entry/zeta-ur/) produces such a datum, and [the nonvanishing theorem](/entry/p-locu/) is the reason why $y$ is not ordinary.

### The theorem

**Theorem 6.22.3 (Strict vanishing).** Assume the cohomological inputs of Section 21. Let $W$ be in normal form for $(e, S, A)$, and assume that $(W, A)$ has an Euler system datum. Then the strict Selmer group of $W^*$ vanishes.

Lean: `GlobalTheory.Ord2.StrictKill.main` (also `GlobalTheory.T.strict_vanishing_dual_of_literature`, a second name).

We use the following facts.

**Lemma 6.22.4 (Scaling to integral cocycles).** Let $V$ be continuous with entries in $\mathcal{O}$ and unramified outside $S$, and let $c$ be an unramified cocycle for $V$. There are a coefficient datum with ring $\mathcal{O}' \supseteq \mathcal{O}$ and $k \geq 0$ such that $\ell^kc$ has values in $\mathcal{O}'^2$, $\ell^kc$ is the coboundary of an element of $\mathcal{O}'^2$ on $I_B$ for every place $B$ over every $q \neq \ell$, and, if $c$ is trivial (or ordinary) at $A$, then $\ell^kc$ is trivial (or ordinary) at $A$ with an integral $x$.

**Lemma 6.22.5 (Gluing local trivializations).** Let $\ell$ be odd, $\ell \in S$, and let $\xi$ be a continuous $2$-cocycle modulo $\ell^n$ with values in $\mathcal{O}(1)$ that is unramified outside $S$. If $\xi$ is a coboundary modulo $\ell^n$ on $D_B$ for a place $B$ over each $v \in S$, then there is a continuous $u : G_{\mathbb{Q}} \to \mathcal{O}$ with $u(sa) \equiv_n u(s)$ for $a \in K_S$ and $\xi \equiv_n du$.

**Lemma 6.22.6 (Cocycles on $N$).** Let $W$ be in normal form for $(e, S, A)$.

1. If a cocycle $y$ of $W$ vanishes on $N$, then $y$ is ordinary at $A$.
2. If $y$ is a cocycle of $W$ and $z$ a cocycle of $W^*$, each nonzero somewhere on $N$, then there are $g, h \in N$ with $\omega(y(h), z(g)) \neq \omega(y(g), z(h))$.
3. There is $\varphi \in [H, H]$ such that $W(\varphi)$ does not have the eigenvalue $1$.

The gluing lemma is the injectivity of the map from $H^2(G_S, \mathcal{O}/\ell^n(1))$ to the sum of the local groups $H^2(\mathbb{Q}_v, \mathcal{O}/\ell^n(1))$ for $v \in S$. By Poitou-Tate duality it follows from the fact that $\mathbb{Q}$ has no nontrivial abelian extension that is unramified at all finite places. Part 2 says that the alternating form $\omega(y(h), z(g)) - \omega(y(g), z(h))$ on $N$ is not zero. Part 3 uses the irreducibility of $W$ on $H$.

**Lemma 6.22.7 (Heights along $N$).** Let $y$ be a cocycle for $W$ and $z$ one for $W^*$, with values in $\mathcal{O}^2$, and let $u$ satisfy $y \cup z \equiv_n du$. Then for $\varphi \in H$ and $g, h \in N$,
$$
\mathrm{ht}\bigl(\varphi[g, h]\bigr) - \mathrm{ht}(\varphi) \equiv_n \det\bigl(W(\varphi) - 1\bigr)\bigl(\omega(y(h), z(g)) - \omega(y(g), z(h))\bigr),
$$
where $[g, h] = ghg^{-1}h^{-1}$.

*Proof.* On $N$ both $W$ and $W^*$ are trivial and $\varepsilon = 1$. So $y$ and $z$ are homomorphisms on $N$, and they vanish on $k = [g, h]$. Put $b(a, a') = \omega(y(a), z(a'))$, a bilinear form on $N$. The relation $y \cup z \equiv_n du$ on $N$ reads $u(aa') \equiv_n u(a) + u(a') - b(a, a')$. From it, $u(1) \equiv_n 0$ and $u(a^{-1}) \equiv_n -u(a) - b(a, a)$. A direct expansion then gives
$$
u\bigl([g, h]\bigr) \equiv_n b(h, g) - b(g, h).
$$
Now $W(\varphi k) = W(\varphi)$, and $y(\varphi k) = y(\varphi) + W(\varphi)y(k) = y(\varphi)$, and in the same way $z(\varphi k) = z(\varphi)$. Since $\varphi \in H$, $\varepsilon(\varphi) = 1$, and $u(\varphi k) \equiv_n u(\varphi) + u(k) - \omega(y(\varphi), W^*(\varphi)z(k)) = u(\varphi) + u(k)$. Hence $\mathrm{ht}(\varphi k) - \mathrm{ht}(\varphi) \equiv_n \det(W(\varphi) - 1)\,u(k)$, which is the claim. $\square$

*Proof of the theorem.* Let $z$ be an unramified cocycle of $W^*$ that is trivial at $A$, and suppose that $z$ is not a coboundary. Let $(\mathcal{O}, y, S')$ be the Euler system datum.

*Step 1: integrality.* Apply the scaling lemma to $y$, and then to $z$ over the larger ring. This gives a ring $\mathcal{O}'$ and $k_1, k_2$ such that $y' = \ell^{k_1}y$ and $z' = \ell^{k_2}z$ have values in $\mathcal{O}'^2$, have integral trivializations on inertia away from $\ell$, and $z'$ is the coboundary of some $x_A \in \mathcal{O}'^2$ on $D_A$. The representation $W^*$ is continuous, integral and unramified outside $S$, since $W$ is and $(\det W)^2 = 1$. The tame classes of $y$ give tame classes of $y'$ over $\mathcal{O}'$. The cocycle $y'$ is still not ordinary, and $z'$ is still not a coboundary.

*Step 2: the cup product is locally trivial.* Fix $n \geq 1$. The $2$-cocycle $y' \cup z'$ is unramified outside $S$. At the place $A$ it is a coboundary modulo $\ell^n$ on $D_A$, because $z'$ is trivial there. At $v \in S$ with $v \neq \ell$ it is a coboundary on $D_B$ for a place $B$ over $v$, because both classes are unramified at $v$; this uses the orthogonality of unramified classes.

*Step 3: a global trivialization.* The gluing lemma gives $u$ with $u(sa) \equiv_n u(s)$ for $a \in K_S$ and $y' \cup z' \equiv_n du$.

*Step 4: heights.* All hypotheses of the theorem of Section 21 now hold for $y'$, $z'$, $u$ and $n$. So $\det(W(\sigma) - 1)\,\mathrm{ht}(\sigma) \equiv_n 0$ for all $\sigma \in [H, H]$.

*Step 5: two elements.* If $y'$ vanished on $N$, part 1 of the lemma on $N$ would make $y$ ordinary at $A$. If $z'$ vanished on $N$, the theorem of Section 20 would make $z$ a coboundary. So part 2 gives $g, h \in N$ with $\delta' = \omega(y'(h), z'(g)) - \omega(y'(g), z'(h)) \neq 0$. Part 3 gives $\varphi \in [H, H]$ with $\delta = \det(W(\varphi) - 1) \neq 0$. These elements do not depend on $n$.

*Step 6: conclusion.* Since $N \subseteq H$, the commutator $[g, h]$ lies in $[H, H]$, and so does $\varphi[g, h]$. Also $W(\varphi[g, h]) = W(\varphi)$. Step 4 applies to $\varphi$ and to $\varphi[g, h]$: with $t_0 = \mathrm{ht}(\varphi)$ and $t_1 = \mathrm{ht}(\varphi[g, h])$, we have $\delta t_0 \equiv_n 0$ and $\delta t_1 \equiv_n 0$. The lemma on heights along $N$ gives $t_1 - t_0 \equiv_n \delta\delta'$. Write
$$
\delta^2\delta' = \delta\bigl(\delta\delta' - (t_1 - t_0)\bigr) + \delta t_1 - \delta t_0.
$$
Since $|\delta| \leq 1$, each term has absolute value at most $|\ell^n|$, and so does $\delta^2\delta'$. This holds for every $n \geq 1$, so $\delta^2\delta' = 0$. This contradicts $\delta \neq 0$ and $\delta' \neq 0$. $\square$

The argument is the Euler system bound of Kolyvagin and Rubin in a form where the bound is zero; compare K. Rubin, *Euler Systems*, Chapter 5.

**Remark 6.22.8 (Formalization).** The second name is a wrapper of the form `first | exact @… | …`. The lemmas are `GlobalTheory.T.galois_cocycle_integral_after_scaling`, `GlobalTheory.T.local_cochains_glue_global` (with the $2$-cocycle property from `GlobalTheory.T.cupProductDualTwist_isTwoCocycle_unramified`), `GlobalTheory.T.greenbergOrdinary_of_vanishing_on_cycloKernel`, `GlobalTheory.T.cocycle_pair_alternating_ne_on_cycloKernel`, `GlobalTheory.T.exists_commutator_det_nonzero` and `GlobalTheory.T.height_commutator_invariance`; the tame classes are carried over by `GlobalTheory.T.eulerSystemTameClass_scale_enlarge_coefficients`. We read them as statements; the proof of the lemma on heights along $N$ and the comments after the lemmas are ours. The facts on $W^*$ in Step 1 are proved in the file ([StrictVanishingDualOfLiterature.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/StrictVanishingDualOfLiterature.lean#L162)). In the formal definition of an Euler system datum the unramified condition on $y$ allows $x$ in $\overline{\mathbb{Q}}_\ell^2$, and the integral trivializations come only from the scaling lemma.
