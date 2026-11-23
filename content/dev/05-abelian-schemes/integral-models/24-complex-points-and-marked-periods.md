---
title: Complex points and marked periods
decls:
  - GlobalTheory.T.complexPoints_classify_markedPeriods
  - GlobalTheory.UPel.HT.Model.fineAt_univ
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Complex points and marked periods

This section describes the complex points of a model (Definition 8.1.4) by linear algebra. Fix a map $\sigma : R \to \mathbb{C}$. A point of the model over $\sigma$ is the class of an abelian variety over $\mathbb{C}$ with extra structure, and such an abelian variety is a complex torus $\mathbb{C}^g / P(\Lambda')$ for a lattice $\Lambda'$ with a period map $P$. We show that every point arises in this way from a lattice of the right class, that every lattice of that class with a period map gives a point, and that two such data give the same point when their lattices are isometric by a map that respects the markings and the period maps. The analytic theory of complex abelian varieties enters only through the results that we quote for objects over $\operatorname{Spec} \mathbb{C}$; the work here is to move them to the universal object. The theorem is used in [the complex uniformization of the generic models](/entry/g-unif-of/).

### Period lattices and uniformization

Let $D$ be a datum (Definition 8.1.1), with ring $O$, involution $*$ and lattice $(\Lambda, E)$, and put $g = mn[F : \mathbb{Q}]/2$.

**Definition 8.24.1 (Period lattice and period map).** A *period lattice* $D'$ is an $O$-module $\Lambda'$ that is free of finite rank over $\mathbb{Z}$, with an alternating form $E' : \Lambda' \times \Lambda' \to \mathbb{Z}$ such that $E'(x, -) = 0$ only for $x = 0$ and $E'(ax, y) = E'(x, a^* y)$ for $a \in O$. Let $\rho : O \to M_g(\mathbb{C})$ be a ring map. A *period map* for $D'$ is an additive map $P : \Lambda' \to \mathbb{C}^g$ with $P(ax) = \rho(a) P(x)$, which is injective, has discrete image, has image spanning $\mathbb{C}^g$ over $\mathbb{R}$, and satisfies $E'(x, y) = \operatorname{Im} H(P x, P y)$ for some positive definite hermitian matrix $H$.

Lean: `GlobalTheory.PELU.PLat`, `GlobalTheory.PELU.IsPeriod`.

A map of period lattices $w : \Lambda' \to \Lambda''$ is a *marked isometry* of level $N$ for markings $t : \Lambda \to \Lambda'$ and $t' : \Lambda \to \Lambda''$ if it is an $O$-linear isomorphism with $E''(wx, wy) = E'(x, y)$ and $w(t a) \equiv t'(a) \bmod N \Lambda''$ for all $a \in \Lambda$.

Lean: `GlobalTheory.PELU.IsMarkedIsom`.

A *family* over $R$ is a scheme $X$ over $\operatorname{Spec} R$, an abelian scheme $A$ over $X$ that is smooth of relative dimension $g$, an action of $O$ on $A$, a relatively ample line bundle $L$ on $A$, and a map $\eta : \Lambda \to A(X)$. An object $o$ of level $N$ (Definition 8.1.3) whose abelian scheme is smooth of relative dimension $g$, and for which $\Delta^* P$ is a line bundle, gives a family with $L = \Delta^* P$.

Lean: `GlobalTheory.PELU.Fam` (also `GlobalTheory.UPel.HT.Obj.fam`).

**Definition 8.24.2 (Uniformization at a point).** Let $\mathcal{F}$ be a family over $R$, $y : \operatorname{Spec} \mathbb{C} \to X$ a point and $(D', t, P)$ a period lattice with a marking $t : \Lambda \to \Lambda'$ and a period map. A *uniformization* of $\mathcal{F}$ at $y$ by $(D', t, P)$ is a map $e$ from $\mathbb{C}^g$ to the points of $A$ over $y$ with the following properties.

1. The point $y$ lies over $\sigma$, and $P$ is a period map.
2. The map $e$ is a surjective holomorphic homomorphism whose derivative at $0$ identifies $\mathbb{C}^g$ with the tangent space of $A_y$ at $0$, and $e(z) = 0$ exactly when $z \in P(\Lambda')$.
3. $e(\rho(a) z) = a \cdot e(z)$ for $a \in O$.
4. For $k > 0$ and $a, b \in \Lambda'$, the Weil pairing of $L$ at level $k$ takes $e(P a / k)$ and $e(P b / k)$ to $\exp(-2 \pi i E'(a, b) / k)$.
5. $\eta(a)$ restricted to $y$ is $e(P(t a) / N)$ for all $a \in \Lambda$.

Lean: `GlobalTheory.PELU.UnifAt` (also `GlobalTheory.PELU.IsExp` for condition 2).

**Definition 8.24.3 (Classes of level N).** A marked period lattice $(D', t)$ is of *class* $N$ if two conditions hold. First, $t = f_N$ for a family of additive maps $f_n : \Lambda \to \Lambda'$ and integers $\nu_n$ such that, for $n$ prime to $p$, $\nu_n$ is prime to $n$ and $f_n$ is an $O$-linear similitude modulo $n$ with factor $\nu_n$, inducing a bijection $\Lambda / n \Lambda \to \Lambda' / n \Lambda'$, and the $f_n$ and $\nu_n$ are compatible modulo $n$ as $n$ grows by factors prime to $p$. Second, $E' = 2 E_1$ for a form $E_1$ such that for some $e$ prime to $p$ every linear form $f$ on $\Lambda'$ has $e f = E_1(x, -)$ for some $x$.

Lean: `GlobalTheory.UPel.HT.Datum.Cls` (also `GlobalTheory.PELU.Genus` and `GlobalTheory.UPel.HT.HalfPerf` for the two conditions).

**Definition 8.24.4 (Fine at a map to C).** A family $\mathcal{F}$ is *fine* at $\sigma$, $\rho$ and $N$ for a class $\mathcal{C}$ of marked period lattices if three conditions hold.

1. (Points.) Every $y$ over $\sigma$ has a uniformization by some $(D', t, P)$ with $(D', t)$ in $\mathcal{C}$.
2. (Occurrence.) Every $(D', t)$ in $\mathcal{C}$ with a period map $P$ gives a uniformization at some point $y$.
3. (Separation.) If $(D', t, P)$ uniformizes at $y$ and $(D'', t', P')$ at $y'$, and there are a marked isometry $w$ of level $N$ and a $\mathbb{C}$-linear isomorphism $h$ of $\mathbb{C}^g$ with $P' w = h P$, then $y = y'$.

Lean: `GlobalTheory.PELU.FineAt`.

Let $b$ be a base for $D$ over $R$ (Definition 8.1.2). The base is of *type* $(\sigma, \rho)$ if for every $c \in \mathcal{O}_F$ the trace of $\rho(c)$ is
$$
\begin{aligned}
m \Bigl( \sum_{i} \sigma(t_i(c)) &+ \sum_{\tau(\omega) \neq \sigma(\rho_b)} n \, \tau(c) \\
&- \sum_{i} \overline{\sigma(t_i(c))} \Bigr),
\end{aligned}
$$
where $\rho_b$ is the root of the base and $\tau$ runs over the embeddings $F \to \mathbb{C}$ with $\tau(\omega) \neq \sigma(\rho_b)$.

Lean: `GlobalTheory.UPel.HT.Base.IsType`.

### The theorem

**Theorem 8.24.5 (Complex points are classified by marked periods).** Let $D$ be a datum for $p$, $b$ a base over $R$, $N > 0$ prime to $p$, $\sigma : R \to \mathbb{C}$ and $\rho : O \to M_g(\mathbb{C})$ such that $b$ is of type $(\sigma, \rho)$. Let $M$ be a model of level $N$ over $b$ with universal object $u$. Then the family of $u$ is fine at $\sigma$, $\rho$ and $N$ for the class $N$.

Lean: `GlobalTheory.UPel.HT.Model.fineAt_univ` (also `GlobalTheory.T.complexPoints_classify_markedPeriods`, a second name).

We use the following results. In results 5 to 7, the objects are over $\operatorname{Spec} \sigma$, and $N > 0$ is prime to $p$ with $b$ of type $(\sigma, \rho)$ where needed.

### Inputs

1. Transfer along a cartesian map. Let $\mathcal{F}'$ and $\mathcal{F}$ be families, $f : X' \to X$ a map and $\varphi : A' \to A$ a map that makes $A'$ the pullback of $A$ as a group scheme, commutes with $O$, carries $L$ to $L'$ up to isomorphism and $\eta'$ to $\eta$. For $y'$ over $\sigma$, a triple $(D', t, P)$ uniformizes $\mathcal{F}'$ at $y'$ if and only if it uniformizes $\mathcal{F}$ at $f y'$.
2. A map of objects $o' \to o$ carries $\Delta^* P$ to $\Delta^* P'$ up to isomorphism, and maps of objects compose.
3. For every object $o$ over $s$ and every $f$ with $s f = s'$, there is an object over $s'$ with a map of objects to $o$ over $f$.
4. For every object, the abelian scheme is smooth of relative dimension $g$ and $\Delta^* P$ is a line bundle.
5. Every object over $\operatorname{Spec} \sigma$ has a uniformization at the identity by some $(D', t, P)$ of class $N$.
6. For every $(D', t)$ of class $N$ with a period map $P$ there is an object over $\operatorname{Spec} \sigma$ with a uniformization by $(D', t, P)$ at the identity.
7. If objects $o_1$ and $o_2$ over $\operatorname{Spec} \sigma$ are uniformized at the identity by $(D', t, P)$ and $(D'', t', P')$, and $w$ and $h$ are as in the separation condition, then there is a map of objects $o_1 \to o_2$ over the identity.

*Proof.* By result 4 the family of $u$, and the family of every object below, is defined. We first note a transfer step. Let $o$ be an object over $\operatorname{Spec} \sigma$ with a map of objects $o \to u$ over $y : \operatorname{Spec} \mathbb{C} \to X$, where $y$ lies over $\sigma$. A map of objects is a cartesian map that commutes with $O$ and $\eta$, and by result 2 it carries the bundle $\Delta^* P$ of $u$ to that of $o$. So result 1 applies with $y' = \mathrm{id}$: a triple uniformizes $o$ at the identity if and only if it uniformizes $u$ at $y$.

Points. Let $y$ lie over $\sigma$. Result 3 gives an object $o$ over $\operatorname{Spec} \sigma$ with a map $o \to u$ over $y$. Result 5 gives a uniformization of $o$ at the identity by some $(D', t, P)$ of class $N$, and the transfer step moves it to $u$ at $y$.

Occurrence. Let $(D', t)$ be of class $N$ with a period map $P$. Result 6 gives an object $o$ over $\operatorname{Spec} \sigma$ uniformized by $(D', t, P)$ at the identity. Since $M$ represents objects, there is a point $y$ over $\sigma$ with a map $o \to u$ over $y$. The transfer step gives a uniformization of $u$ at $y$.

Separation. Let $(D', t, P)$ uniformize at $y$ and $(D'', t', P')$ at $y'$, with $w$ and $h$ as in the condition. Result 3 gives objects $o_1$ and $o_2$ over $\operatorname{Spec} \sigma$ with maps $o_1 \to u$ over $y$ and $o_2 \to u$ over $y'$. By the transfer step, $o_1$ and $o_2$ are uniformized at the identity, and result 7 gives a map $o_1 \to o_2$ over the identity. Composing with $o_2 \to u$ (result 2) gives a map $o_1 \to u$ over $y'$. So both $y$ and $y'$ carry a map of objects from $o_1$ to $u$, and the uniqueness in the representing property gives $y = y'$. $\square$

**Remark 8.24.6 (Formalization).** The theorem is in [ComplexPointsClassifyMarkedPeriods.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComplexPointsClassifyMarkedPeriods.lean#L20), and the second name is a wrapper under a raised heartbeat limit: [ComplexPointsClassifyMarkedPeriodsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComplexPointsClassifyMarkedPeriodsStatement.lean#L9). The definitions of this section are in [IsHolPeriods.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsHolPeriods.lean#L13) and [Uniformised.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/Uniformised.lean#L30). The theorem takes as arguments the smoothness of the universal abelian scheme and the fact that $\Delta^* P$ is a line bundle; by result 4 these always hold. It needs $N > 0$ but not $N \geq 3$, while this chapter builds models only for $N \geq 3$. In condition 2 of a uniformization, the identification of tangent spaces is stated through maps from the dual numbers; in condition 4, the Weil pairing and the holomorphy of $e$ are notions we have not unfolded. Our description of the class $N$ condition summarizes its compatibilities. We read the statements of results 1 to 7, not their proofs.
