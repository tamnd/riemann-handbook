---
title: Geometric coboundaries
decls:
  - GlobalTheory.K5.TopGeo.top
  - GlobalTheory.T.kummer_cocycle_twisted_coboundary
  - GlobalTheory.K5.Reb.h1_geometric_level_coboundary
  - GlobalTheory.T.geometric_level_h1_coboundary
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Geometric coboundaries

This section computes the first cohomology, modulo $p^k$, of the geometric Galois group of a $p$-adic field of Laurent series in $q$. Up to a bounded power of $p$, every cocycle is a multiple of the Kummer character of $q^{1/p^k}$ plus a coboundary, and a multiple of that character is a coboundary only when the multiplier is $0$ modulo $p^k$. The second theorem transfers this to the subgroup that fixes $q^{1/p^L}$. Both results are statements about [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology) written with explicit cochains. They are used in [the local edge congruence](/entry/edge-dlog/) of the next section, which compares an edge class of two units with its logarithmic derivative.

Fix an odd prime $p$. Let $\mathcal{O}$ be the $p$-adic completion of the ring $\mathbb{Z}_p((q))$ of Laurent series over $\mathbb{Z}_p$.

**Definition 6.11.1 (Closure and tower).** A *closure* of $\mathcal{O}$ is a field $\Omega$ with an injective ring map $\mathcal{O} \to \Omega$ such that $\Omega$ is algebraic over $\mathcal{O}$ and algebraically closed. Let $G = \mathrm{Aut}_{\mathcal{O}}(\Omega)$. A *tower* in $\Omega$ is a pair of sequences $(\zeta_n)$, $(q_n)$ with $\zeta_n$ a primitive $p^n$-th root of unity, $\zeta_{n+1}^p = \zeta_n$, $q_0 = q$ and $q_{n+1}^p = q_n$. For $L \geq 0$ let $G_L \subseteq G$ be the subgroup that fixes $\zeta_L$ and $q_L$.

**Definition 6.11.2 (Integral elements and congruences).** An element $x \in \Omega$ is *integral* if it is integral over $\mathcal{O}$. For $x, y \in \Omega$ we write $x \equiv y \pmod{p^k}$ if $x - y = p^k z$ for an integral $z$.

**Definition 6.11.3 (Geometric Galois group).** An element $x \in \Omega$ is *algebraic over $\mathbb{Z}_p$* if $P(x) = 0$ for a nonzero $P \in \mathbb{Z}_p[X]$. The *geometric Galois group* $G_{\mathrm{geo}} \subseteq G$ is the subgroup of automorphisms that fix every element algebraic over $\mathbb{Z}_p$.

The group $G_{\mathrm{geo}}$ fixes all $\zeta_n$. It moves the roots $q_n$, and it acts on them through Kummer characters.

**Definition 6.11.4 (Cochains modulo $p^k$).** Let $H \subseteq G$ be a subgroup and $k \geq 0$. A map $a : G \to \Omega$ is an *integral locally constant cochain modulo $p^k$ on $H$* if $a(g)$ is integral for $g \in H$, and for each $g \in H$ there is a finite set $S \subseteq \Omega$ with $a(h) \equiv a(g) \pmod{p^k}$ for all $h \in H$ that agree with $g$ on $S$. It is a *cocycle modulo $p^k$ on $H$* if $a(gh) \equiv a(g) + g(a(h)) \pmod{p^k}$ for $g, h \in H$. It is a *coboundary modulo $p^k$ on $H$* if there is an integral $x$ with $a(g) \equiv g(x) - x \pmod{p^k}$ for $g \in H$.

**Definition 6.11.5 (Kummer character).** Let $r \in \Omega$. A map $\kappa : G \to \mathbb{Z}/p^k$ is a *Kummer character of $r$ on $H$* if $g(r) = \zeta_k^{\kappa(g)} r$ for all $g \in H$. In cochains we identify $\kappa(g)$ with its representative in $\{0, \ldots, p^k - 1\}$.

**Theorem 6.11.6 (First cohomology of the geometric Galois group).** Let $p$ be an odd prime. There is $c \geq 0$ with the following property. Let $\Omega$ be a closure of $\mathcal{O}$ with a tower, let $k \geq 0$, and let $\kappa$ be a Kummer character of $q_k$ on $G_{\mathrm{geo}}$. Then:

1. for every integral locally constant cochain $a$ modulo $p^k$ on $G_{\mathrm{geo}}$ that is a cocycle modulo $p^k$, there is an integral $o \in \Omega$ fixed by $G_{\mathrm{geo}}$ such that $g \mapsto p^c a(g) - o\,\kappa(g)$ is a coboundary modulo $p^k$ on $G_{\mathrm{geo}}$;
2. if $o$ is integral and fixed by $G_{\mathrm{geo}}$, and $g \mapsto o\,\kappa(g)$ is a coboundary modulo $p^k$ on $G_{\mathrm{geo}}$, then $p^c o \equiv 0 \pmod{p^k}$.

Lean: `GlobalTheory.K5.TopGeo.top` (also `GlobalTheory.T.kummer_cocycle_twisted_coboundary`, a second name).

In other words, $o \mapsto o\,\kappa$ induces a map from the invariants modulo $p^k$ to $H^1(G_{\mathrm{geo}}, \cdot)$ modulo $p^k$ whose kernel and cokernel are killed by $p^c$. The proof gives $c = 3$.

*Proof.* For $k = 0$ every integral element is $\equiv 0 \pmod{1}$, and both parts hold with $o = 0$. Let $k \geq 1$. Put $\pi = \zeta_1 - 1$. The element $r = -\sum_{i < p}\sum_{m < i}\zeta_1^m$ is integral, fixed by $G_{\mathrm{geo}}$, and satisfies $p = \pi r$, since $\pi \sum_{m<i}\zeta_1^m = \zeta_1^i - 1$ and $\sum_{i<p}\zeta_1^i = 0$. So it is enough to prove both parts with $p^3$ replaced by $\pi^3$. Let $H_\infty = G_{\mathrm{geo}} \cap \bigcap_n G_n$, the subgroup that fixes all $q_n$. Five facts from the development are used.

- (A) There is $\tau \in G_{\mathrm{geo}}$ with $\tau(q_n) = \zeta_n q_n$ for all $n$.
- (B) For every $g \in G_{\mathrm{geo}}$ and finite $S \subseteq \Omega$ there are $s \geq 0$ and $h \in H_\infty$ with $\tau^s h = g$ on $S$.
- (C) The element $\pi$ kills the cohomology of $H_\infty$: if $a$ is an integral locally constant cocycle modulo $p^k$ on $H_\infty$, then $\pi a$ is a coboundary modulo $p^k$ on $H_\infty$.
- (D) If $x$ is integral and $g(x) \equiv x$ for $g \in H_\infty$, then $\pi x \equiv y$ for an integral $y$ fixed by $G_{\mathrm{geo}} \cap \mathrm{Stab}(q_N)$ for some $N$.
- (E) Such a $y$ decomposes as $\pi y = \pi o + (\tau w - w)$ with $o$ integral and fixed by $G_{\mathrm{geo}}$, and $w$ integral and fixed by $G_{\mathrm{geo}} \cap \mathrm{Stab}(q_N)$. Also, if $\tau w - w \equiv o$ for such $w$ and for $o$ fixed by $G_{\mathrm{geo}}$, then $o \equiv 0$.

*Part 1.* By (C) there is an integral $x_1$ with $\pi a(h) \equiv h(x_1) - x_1$ on $H_\infty$. Then $a_1 = \pi a - (g \mapsto g x_1 - x_1)$ is a cocycle that vanishes modulo $p^k$ on $H_\infty$. As conjugation by $\tau$ maps $H_\infty$ into itself, the value $z = a_1(\tau)$ is invariant modulo $p^k$ under $H_\infty$. By (D) and (E), $\pi z \equiv y$ and $\pi y = \pi o + (\tau w - w)$. Put
$$
b(g) = \pi^2 a_1(g) - (g w - w) - \pi o\,\kappa(g).
$$
This is a cocycle modulo $p^k$. It vanishes on $H_\infty$, as $\kappa$ and $a_1$ do and $w$ is fixed there. It vanishes at $\tau$, since $\kappa(\tau) = 1$ and $\pi^2 z \equiv \pi o + (\tau w - w)$. So it vanishes on all powers $\tau^s$ and on all products $\tau^s h$ with $h \in H_\infty$. By (B) and local constancy, $b \equiv 0$ on $G_{\mathrm{geo}}$. Multiplying by $r^3$ gives part 1 with the element $r^3 \pi o$.

*Part 2.* Let $o\,\kappa(g) \equiv g x - x$. Since $\kappa = 0$ on $H_\infty$, $x$ is invariant modulo $p^k$ under $H_\infty$. By (D), $\pi x \equiv y$ with $y$ fixed at a finite level $N$. Then $\tau y - y \equiv \pi(\tau x - x) \equiv \pi o$. By the second half of (E), $\pi o \equiv 0$, and $p^3 o = r^3\pi^2 \cdot \pi o \equiv 0$. $\square$

**Definition 6.11.7 (Reparametrization).** Let $L \geq 0$. A *reparametrization at level $L$* is an injective ring map $\psi : \mathcal{O} \to \Omega$ with $\psi(q) = q_L$, whose image is the subring generated by $\mathcal{O}$ and $q_L$, and with $\psi(b) = a$ whenever $a, b \in \mathbb{Z}_p((q))$ satisfy $b(q) = a(q^{p^L})$.

The map $\psi$ is "substitute $q_L$ for $q$". It makes $\Omega$ a closure of $\mathcal{O}$ in a second way, with the tower $(\zeta_n, q_{L+n})$. The development proves that a reparametrization exists at every level.

**Theorem 6.11.8 (Geometric coboundaries at level $L$).** Let $p$ be an odd prime. There is $c \geq 0$ with the following property. Let $\Omega$ be a closure of $\mathcal{O}$ with a tower, let $0 \leq n \leq L$, put $H = G_{\mathrm{geo}} \cap G_L$, and let $\lambda$ be a Kummer character of $q_{L+n}$ on $H$. Then:

1. for every integral locally constant cochain $a$ modulo $p^n$ on $H$ that is a cocycle modulo $p^n$ on $H$, there is an integral $o$ fixed by $H$ such that $p^c a - o\,\lambda$ is a coboundary modulo $p^n$ on $H$;
2. if $o$ is integral and fixed by $H$, and $o\,\lambda$ is a coboundary modulo $p^n$ on $H$, then $p^c o \equiv 0 \pmod{p^n}$.

Lean: `GlobalTheory.K5.Reb.h1_geometric_level_coboundary` (also `GlobalTheory.T.geometric_level_h1_coboundary`, a second name).

*Proof.* Take $c$ from the last theorem. Choose a reparametrization $\psi$ at level $L$, and let $\Omega_\psi$ be the field $\Omega$ with the $\mathcal{O}$-algebra structure given by $\psi$. The following hold.

- An element is integral over $\mathcal{O}$ for one structure if and only if it is for the other, so congruences modulo $p^n$ agree. The same holds for "algebraic over $\mathbb{Z}_p$", since $\psi$ is the identity on $\mathbb{Z}_p$.
- $\Omega_\psi$ is a closure of $\mathcal{O}$, and $(\zeta_m, q_{L+m})_m$ is a tower in it.
- An automorphism of $\Omega_\psi$ over $\mathcal{O}$ is an automorphism of $\Omega$ over $\mathcal{O}$, since the image of $\psi$ contains that of $\mathcal{O}$. An automorphism of $\Omega$ that fixes $q_L$ fixes the image of $\psi$. So the geometric Galois group of $\Omega_\psi$ is identified with $H$.

Under this identification, $\lambda$ becomes a Kummer character of the $n$-th root $q_{L+n}$ of the new tower on the geometric Galois group, and $a$ becomes an integral locally constant cocycle modulo $p^n$. Both parts now follow from the last theorem. $\square$

**Remark 6.11.9 (Formalization).** The first theorem is stated for twisted cocycles and coboundaries with a twist $\chi^j$, but with $j = 0$, so the character $\chi$ in its statement does not enter ([KummerCocycleTwistedCoboundary.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/KummerCocycleTwistedCoboundary.lean#L371)); the name "twisted coboundary" of the second name reflects this unused generality. The proof sets $c = 3$. In the second theorem the hypothesis $n \leq L$ is bound to `_` and not used ([GeometricLevelH1Coboundary.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GeometricLevelH1Coboundary.lean#L184)), and the theorem passes the zero map as $\chi$. Locally constant here is with respect to finite sets of points of $\Omega$, not a topology on $G$. The closure $\Omega$ is only required to be algebraic over $\mathcal{O}$ and algebraically closed, so $G$ is the full automorphism group over $\mathcal{O}$. Both second names are wrappers under `maxHeartbeats 1000000`. Facts (A) to (E) and the existence of a reparametrization were read as statements; their proofs are in other files of the development.
