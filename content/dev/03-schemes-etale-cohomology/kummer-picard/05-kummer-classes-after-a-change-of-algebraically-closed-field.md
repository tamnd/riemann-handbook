---
title: Kummer classes after a change of algebraically closed field
decls:
  - UpperTheory.baseChange_curve_functionField_comp_of_normal
  - UpperTheory.PicRigid.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kummer classes after a change of algebraically closed field

Let $C$ be a proper smooth curve over an algebraically closed field $k$, and let $L \supseteq k$ be a larger algebraically closed field. This section proves that a rational function on $C_L$ whose divisor is divisible by $q$ comes from $C$, up to a $q$-th power. In terms of divisors: every $q$-torsion class in $\operatorname{Pic}(C_L)$ comes from a $q$-torsion class on $C$. The proof is cohomological. It uses Kummer theory and the invariance of étale cohomology of a proper smooth variety under a change of algebraically closed base field. The next section uses the result to bound the $q$-torsion of Picard groups of affine curves.

### Kummer classes

Let $X$ be a scheme on which the integer $q \ge 1$ is invertible. We use the cohomology $H^n(X, \mathbb{Z}/q(i))$ of the earlier sections, with $X$ viewed as a space. Here $\mathbb{Z}/q(1)$ plays the role of the sheaf $\mu_q$ of $q$-th roots of unity ([roots of unity](/learn/algebra/#roots-of-unity)).

**Definition 6.5.1 (Kummer class).** Let $w \in \Gamma(X, \mathcal{O}_X)^\times$. The *Kummer class* $\operatorname{kum}(w) \in H^1(X, \mathbb{Z}/q(1))$ is the class of the torsor of $q$-th roots of $w$: étale locally on $X$, $w$ has a $q$-th root, and two roots differ by a $q$-th root of unity.

The Kummer class is natural in $X$ and additive: $\operatorname{kum}(w w') = \operatorname{kum}(w) + \operatorname{kum}(w')$. For $X = \mathbb{G}_m$ and $w = t$ it is the class $\kappa$ of the section on the Künneth formula. The Kummer sequence $0 \to \mu_q \to \mathbb{G}_m \xrightarrow{q} \mathbb{G}_m \to 0$ and Hilbert's Theorem 90, $H^1(X, \mathbb{G}_m) = \operatorname{Pic}(X)$, give an exact sequence
$$0 \to \Gamma(X, \mathcal{O}_X)^\times / (\Gamma(X, \mathcal{O}_X)^\times)^q \xrightarrow{\operatorname{kum}} H^1(X, \mu_q) \to \operatorname{Pic}(X)[q] \to 0$$
(Milne, *Étale Cohomology*, Chapter III, Proposition 4.9, for Hilbert 90). We use three consequences. We state them with the reason for each, and do not give the detailed proofs.

1. If $\operatorname{kum}(w) = 0$, then $w = v^q$ for a unit $v$.
2. If $\operatorname{Pic}(A)[q] = 0$ for a ring $A$ in which $q$ is a unit, then each class in $H^1(\operatorname{Spec} A, \mathbb{Z}/q(1))$ is a Kummer class. This applies to a field $A$.
3. Let $X$ be a normal integral quasi-compact scheme, with function field $K(X)$, on which $q$ is a unit and which has a primitive $q$-th root of unity. Let $F \in K(X)^\times$ be *locally a unit times a $q$-th power*: for each point $y \in X$ there are $u \in \mathcal{O}_{X,y}^\times$ and $h \in K(X)^\times$ with $F = u h^q$. Then $\operatorname{kum}(F)$, a class on $\operatorname{Spec} K(X)$, is the restriction of a class in $H^1(X, \mathbb{Z}/q(1))$.

For a normal $X$, the condition in item 3 says that the divisor of $F$ is divisible by $q$. The reason for item 3 is that the torsor of $q$-th roots of $F$ is, near $y$, the torsor of $q$-th roots of the unit $u$, and these local torsors glue.

### Change of algebraically closed field

The model of étale cohomology in this volume is built on a list of axioms. They are listed in the section of the chapter on étale cohomology that contains [Theorem 3.1.7](/entry/etale-duality-trace-isomorphism/). We write (H) for the following 27 of them: A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5, D1 to D3 and E1 to E3. Two of them matter here. Axiom E2 is proper base change: for a strictly henselian local ring $A$ and a proper scheme $X$ over $A$, the inclusion of the closed fibre into $X$ is an equivalence for each $\mathbb{Z}/q(i)$. Axiom E3 is a form of smooth base change: for a local domain $T$ that is absolutely integrally closed, with $q$ a unit in $T$, and a smooth scheme $X$ over $T$, the inclusion of the generic fibre into $X$ is an equivalence for each $\mathbb{Z}/q(i)$.

**Theorem 6.5.2 (Change of algebraically closed field).** Assume E2 and E3. Let $k \to K$ be a map of algebraically closed fields and $q \ge 1$ an integer invertible in $k$. Let $X$ be a proper smooth scheme over $k$, with base change $X_K$. Then the projection $X_K \to X$ is an equivalence for each $\mathbb{Z}/q(i)$: the pullback
$$H^n(X, \mathbb{Z}/q(i)) \to H^n(X_K, \mathbb{Z}/q(i))$$
is bijective for all $n$ and $i$.

Lean: `LateralTheory.Fin.AlgExt.etale_cohomology_algebraic_extension_invariance_of_places` (also `LateralTheory.Fin.AlgExt.intersectionNumber_baseChange`, a second name).

We do not prove this theorem here. In the classical theory it follows from proper base change and smooth base change (Milne, *Étale Cohomology*, Chapter VI, §2 and §4). We use it only for $n = 1$ and $i = 1$.

### The theorem

**Theorem 6.5.3 (Divisible divisors come from the curve).** Assume the axioms (H). Let $k \subseteq L$ be algebraically closed fields and $q$ an integer invertible in $k$. Let $C$ be an integral, proper and smooth curve over $k$ with function field $k(C)$. Let $X$ be an integral scheme with a cartesian square
$$\begin{array}{ccc} X & \xrightarrow{u} & C \\ \downarrow & & \downarrow \\ \operatorname{Spec} L & \to & \operatorname{Spec} k \end{array}$$
such that all local rings of $X$ are integrally closed. Let $\varphi : k(C) \to L(X)$ be the map of function fields induced by $u$. Let $F \in L(X)^\times$ be locally a unit times a $q$-th power. Then there are $f \in k(C)^\times$ and $h \in L(X)^\times$ with
$$F = \varphi(f) \, h^q.$$

Lean: `UpperTheory.baseChange_curve_functionField_comp_of_normal` (also `UpperTheory.PicRigid.main`, the same statement with the invariance theorem as an argument).

*Proof.* The proof has four steps.

1. *A class on $X$.* Since $L$ is algebraically closed and $q$ is a unit in $L$, the cyclotomic polynomial $\Phi_q$ has a root in $L$, a primitive $q$-th root of unity. The scheme $X$ is proper over $L$, as a base change of $C$, so it is quasi-compact. By item 3, there is a class $x \in H^1(X, \mathbb{Z}/q(1))$ whose restriction to the generic point of $X$ is $\operatorname{kum}(F)$.
2. *Descent to $C$.* The curve $C$ is proper and smooth over $k$. By the Theorem on change of algebraically closed field, which applies since (H) contains E2 and E3, $u^* : H^1(C, \mathbb{Z}/q(1)) \to H^1(X, \mathbb{Z}/q(1))$ is surjective. Choose $x_0$ on $C$ with $u^* x_0 = x$.
3. *A function on $C$.* Restrict $x_0$ to the generic point $\operatorname{Spec} k(C)$. The Picard group of a field is trivial, so by item 2 the restriction is $\operatorname{kum}(f)$ for some $f \in k(C)^\times$.
4. *Comparison.* The square of generic points commutes with $u$, so by naturality the restriction of $x$ to $\operatorname{Spec} L(X)$ is $\operatorname{kum}(\varphi(f))$. By step 1 this restriction is also $\operatorname{kum}(F)$. By additivity, $\operatorname{kum}(F \varphi(f)^{-1}) = 0$. By item 1, $F \varphi(f)^{-1} = h^q$ for some $h \in L(X)^\times$. $\square$

Here is the meaning for divisors. Let $D$ be a divisor on $X$ with $q D = \operatorname{div}(F)$. The theorem gives $q (D - \operatorname{div}(h)) = \operatorname{div}(\varphi(f))$, the pullback of $\operatorname{div}(f)$. A closed point of $C$ pulls back to a single reduced point of $X$, since $k$ is algebraically closed. So $q$ divides $\operatorname{div}(f)$, and the class of $D$ is the pullback of the $q$-torsion class of $\operatorname{div}(f)/q$. Over $\mathbb{C}$ this is the statement that the $q$-torsion points of the Jacobian of $C$ are already defined over $k$ ([line bundles and divisors](/learn/geometry/#line-bundles-and-divisors)).

**Remark 6.5.4 (Formalization).** Of the axioms (H), the proof of the Theorem on divisible divisors uses only E2 and E3, through the Theorem on change of algebraically closed field. The second name of that theorem, `intersectionNumber_baseChange`, says nothing about intersection numbers. The hypothesis that the local rings of $X$ are integrally closed follows from the smoothness of $C$, but the statement asks for it. The theorem is supplied at [FinAlgExt.lean](lean:Development/EtaleCohomology/KummerTheory/FinAlgExt.lean#L18).
