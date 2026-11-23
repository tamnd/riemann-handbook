---
title: Ordinary points of the integral models
decls:
  - UpperTheory.Gal.Ord.point
  - UpperTheory.Gal.Ord.ordGen
  - UpperTheory.Gal.crystallineComparison.Mod.ordGen_link
  - UpperTheory.Gal.crystallineComparison.Mod.eW_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ordinary points of the integral models

Section 02 proved the Eichler-Shimura relation for a Hecke tower that has a congruence model: a good integral model on which the Hecke correspondences $T_0, \dots, T_n$ satisfy $\sum_j c_q(j) F^{n-j} \circ T_j = 0$ at the generic points of the special fibre, with $c_q(j) = (-1)^j q^{\binom{j}{2}}$. This section and the next prove that the Kuga-Sato varieties have such models, by the classical argument. Here we show that the generic points of the special fibre are ordinary, and that at an ordinary point the correspondences $T_j$ are read off from the subspaces of a vector space over the residue field of $w$. Section 11 turns this into a count of subspaces.

We keep the moduli problem of Section 08, with $m = 1$. Let $\omega$ be the generator of the imaginary quadratic order fixed there. For an integer $r$ write $\mathfrak{u}_r = (p, \omega - r)$, an ideal of $\mathcal{O}_F$. For an object $o$ of level $N$ over a scheme, $A_o$ is its abelian scheme and $A_o[w]$ the subgroup killed by an ideal $w$ of $\mathcal{O}_F$.

**Definition 3.10.1 ($w$-ordinary).** Let $k$ be an algebraically closed field and $o$ an object over $k$. Then $o$ is *$w$-ordinary* if $k$ has characteristic $p$, $w$ is a prime ideal containing $p$, and the group $A_o[w](k)$ has exactly $N(w)^{n-1}$ elements.

For signature $(1, n-1)$ the group scheme $A_o[w]$ has rank $n$ over $\mathcal{O}_F/w$ and its connected part has rank at least $1$, so $o$ is $w$-ordinary when the étale part is as large as it can be.

**Definition 3.10.2 (splitting datum).** Let $w$ be an ideal of $\mathcal{O}_F$ and $f \geq 1$. A *splitting datum* for $(w, f)$ is a tuple $(\varepsilon, a, g, c, c', s)$ of elements of $\mathcal{O}_F$ such that, with congruences modulo $p\mathcal{O}_F$:

1. $\varepsilon^2 \equiv \varepsilon$, $\varepsilon - 1 \in w$, and $\varepsilon \in w'$ for every other maximal ideal $w'$ containing $p$;
2. $a \in w$, $a(1 - \varepsilon) = p^f s$, $ag = pc$, $c'c\varepsilon \equiv \varepsilon$, $\varepsilon g \equiv g$, and $a^e \varepsilon \equiv 0$ for some $e$;
3. for every $x \in w$ there is $u$ with $\varepsilon x \equiv au$;
4. if $gx \equiv 0$ then $x \equiv au + (1 - \varepsilon)v$ for some $u, v$;
5. if $ax \equiv 0$ then $\varepsilon x \equiv gu$ for some $u$.

So $\varepsilon$ is the idempotent of $\mathcal{O}_F/p$ for $w$, and $a$ and $g$ cut the $w$-part of a module over $\mathcal{O}_F/p$ into the parts killed by $w$ and by the complementary factor. For an object $o$ over a field $k$ of characteristic $p$ and $x \in \mathcal{O}_F$, write $x_*$ for the action of $x$ on the primitive de Rham classes of $A_o$, and $F_{\mathrm{dR}}$ for the Frobenius on these classes.

**Lemma 3.10.3 (ordinary or Hasse).** Let $N \geq 3$ be prime to $p$. Let $R$ be a ring with a base, $k$ an algebraically closed field with $p = 0$ in $k$, $\beta : R \to k$, and $o$ an object of level $N$ over $k$ through $\beta$. Let $i$ be an index, $w$ an ideal of $\mathcal{O}_F$ and $f > 0$ with $\ker(\beta \circ t_i) = w$ and $N(w) = p^f$, and let $(\varepsilon, a, g, c, c', s)$ be a splitting datum for $(w, f)$. Then $o$ is $w$-ordinary, or for every primitive de Rham class $x$ of $A_o$
$$\varepsilon_* x \in \operatorname{span}_k \{ g_*(F_{\mathrm{dR}}^f y) : y \text{ primitive} \}.$$

Lean: `UpperTheory.Gal.Ord.point`.

We call the second alternative the *Hasse condition* at $o$.

*Proof.* Count the $w$-torsion. If $A_o[w](k)$ has $N(w)^{n-1}$ elements, $o$ is $w$-ordinary. Otherwise the count gives a nonzero vector in the Dieudonné module of $A_o[w]$ on which Frobenius is nilpotent. Since $p = 0$ in $k$, multiplication by $p$ is $0$ on primitive classes, so it factors as $V \circ F$ with $V$ semilinear of a rank fixed by the count. The action of $\mathcal{O}_F$ on primitive classes is $k$-linear through $\beta \circ t_i$, with $w$ as kernel. Linear algebra over $\mathcal{O}_F / w$ with the elements of the splitting datum then writes each $\varepsilon_* x$ as $g_*(F_{\mathrm{dR}}^f y)$ for a primitive class $y$. $\square$

**Theorem 3.10.4 (density of the ordinary locus).** Let $R$ be a discrete valuation ring of characteristic $0$ with a base and with $p$ in its maximal ideal, let $N \geq 3$ be prime to $p$, and let $m = 1$. Let $i$ be an index and $w = t_i^{-1}(\mathfrak{m}_R)$. Let $M$ be a model of level $N$ over $R$ and $z$ a point of $M$ over the closed point of $R$ such that every point $z'$ over the closed point that specializes to $z$ equals $z$. Then for every algebraically closed field $k$ and every $y : \operatorname{Spec} k \to M$ with image $z$, the pullback of the universal object along $y$ is $w$-ordinary.

Lean: `UpperTheory.Gal.Ord.ordGen` (also `UpperTheory.Gal.crystallineComparison.Mod.ordGen_link`).

This is the density of the ordinary locus in the special fibre (T. Wedhorn, Ordinariness in good reductions of Shimura varieties of PEL-type, Ann. Sci. École Norm. Sup. 32 (1999)).

*Proof.* The closed point of $R$ is the image of $y$, so $k$ has characteristic $p$ and $\ker(\beta \circ t_i) = w$, where $\beta : R \to k$ is the map under $y$. So $w$ is prime and contains $p$, hence is maximal with $N(w) = p^f$ for some $f > 0$, and it has a splitting datum. Suppose $y$ is not $w$-ordinary. By the lemma the Hasse condition holds. Then there is a linear form $\lambda$ on the primitive classes, fixed by $\varepsilon$, that vanishes on every $g_*(F^f_{\mathrm{dR}} y)$ but not on every class; it lies in the Hodge filtration. The de Rham pairing of the moduli problem makes the Kodaira-Spencer map onto, so there is a direction in which the filtration moves off $\lambda$, and a lift $o'$ of the object over the dual numbers $k[\epsilon]$ along it. The lift is a $k[\epsilon]$-point of $M$ whose closed point is $z$. Since $z$ is generic in the special fibre, the Hasse condition holds on this point as well, while the choice of direction makes it fail. This is a contradiction. $\square$

We now fix the Hecke correspondences at $w$. Say that a ring $O$ with a base is *standard* for $(f, N, r, w)$ if $O$ is a discrete valuation ring of characteristic $0$ with $p \in \mathfrak{m}_O$ and residue field of order $p^f$, $N \geq 3$ is prime to $p$, $a = m = 1$, $\mathfrak{u}_r \subseteq w$, $N(w) = p^f$, and $t_1(w) \subseteq \mathfrak{m}_O$.

**Definition 3.10.5 (Hecke correspondence of type $j$).** Let $M$ be a model of level $N$ over $O$ and $c \in \mathbb{N}$. A *Hecke correspondence of type $j$ and factor $c$* on $M$ is a scheme $Y$ with maps $s, t : Y \to M$ over $O$, objects $o, o'$ over $Y$ that are the pullbacks of the universal object along $s$ and $t$, and a map $\psi : A_o \to A_{o'}$, such that:

1. $s$ is finite, and étale over the locus where $p$ is invertible;
2. $c$ is a power of $p$; $\psi$ is an $\mathcal{O}$-linear homomorphism that preserves the level structure; the polarization of $o'$ pulls back to $c$ times that of $o$; and there is $\psi'$ with $\psi\psi' = c$ and $\psi'\psi = c$;
3. at each geometric point of characteristic $0$, the points of $\ker \psi$ killed by a power of $\mathfrak{u}_r$ are killed by $w$, and $\ker \psi$ has $N(w)^j$ points killed by $w$;
4. $(Y, \psi)$ is universal for such isogenies over schemes on which $p$ is invertible.

A correspondence of this kind carries a point $u$ of $A_o$ over $s(y)$ to the point $\psi(u)$ of $A$ over $t(y)$; we call it the *image* of $u$.

**Theorem 3.10.6 (Hecke correspondences at ordinary points).** Let $O$ be standard for $(f, N, r, w)$ with $w$ maximal, let $M$ be a model of level $N$ over $O$, and for $j = 0, \dots, n$ let $T_j$ be a Hecke correspondence of type $j$ and factor $p^{fj}$. Let $V$ be a valuation ring with algebraically closed fraction and residue fields and $p \neq 0$ in $V$. Let $x : \operatorname{Spec} V \to M$ have its closed point over the closed point of $O$, with $w$-ordinary residue point, and let $\varphi$ be the $p^f$-power map of the residue field. Then there are a finite $\mathcal{O}_F/w$-module $H$ of rank $n$, a submodule $C$ of rank $1$, and for each $j$ a bijection $z \mapsto D_z$ from the $V$-points $z$ of $T_j$ with $s \circ z = x$ to the $j$-dimensional subspaces of $H$, with these properties. Write $\bar D$ for the image of $D$ in $H/C$ and $\bar z$ for the residue point of $z$.

1. If $z, z'$ are points of $T_j$ with $C \not\subseteq D_z$, $C \not\subseteq D_{z'}$ and $\bar D_z = \bar D_{z'}$, then $t(\bar z) = t(\bar z')$, and the images of each point of $A$ under $\bar z$ and $\bar z'$ agree.
2. If $z$ is a point of $T_j$ and $z'$ a point of $T_{j-1}$ with $C \subseteq D_z$, $C \not\subseteq D_{z'}$ and $\bar D_z = \bar D_{z'}$, then $t(\bar z) = \varphi^* t(\bar z')$, and the same holds for the images of points of $A$.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.eW_holds`.

This is the classical description of Hecke correspondences at ordinary points (G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, 1990, Chapter VII).

*Proof.* Let $H$ be the $w$-torsion of the generic fibre of $A_x$, of rank $n$ over $\mathcal{O}_F/w$, and let $C$ be the line that reduces into the connected part of the $w$-torsion of the special fibre; it is a line because $x$ is $w$-ordinary. A $V$-point of $T_j$ over $x$ is an isogeny of the kind in the definition, so by universality it is the quotient by a $j$-dimensional subspace $D$ of $H$; this gives the bijection. Over the residue field the quotient by $D$ depends only on the étale part of the kernel, which is $\bar D$ when $C \not\subseteq D$; this gives 1. If $C \subseteq D$, the quotient by $D$ is the quotient by $D'$ followed by the quotient by the connected subgroup of order $q = p^f$ given by $C$, and that quotient is the $q$-power Frobenius twist; this gives 2. The quotients are objects of the moduli problem by [the theorem on quotients by subgroup schemes](/entry/exists-p-isogeny-kernel-eq-subgroup-scheme/). $\square$

**Remark 3.10.7 (Formalization).** The Hasse condition is `UpperTheory.Gal.Ord.NOo`, and the splitting datum is `Par`. The proof of the density theorem obtains $w$-ordinarity of $y$ from `UpperTheory.Gal.Ord.point` applied to a pullback of the universal object, and the existence of a splitting datum from `par`. The Hecke correspondences of Definition 3.10.5 are the structure `TjD`, and the standard condition is `Std`. The namespace `crystallineComparison.Mod` of `eW_holds` has no crystalline content.
