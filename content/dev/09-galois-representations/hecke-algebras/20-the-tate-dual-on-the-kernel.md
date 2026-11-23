---
title: The Tate dual on the kernel of a representation
decls:
  - GlobalTheory.T.exists_ker_rep_cyclotomic_ne_one_normalForm
  - GlobalTheory.Ord2.exists_ker_eps_ne_one
  - GlobalTheory.T.tateDual_cocycle_coboundary_of_vanish_on_fixing
  - GlobalTheory.Ord2.h1dual_of_vanish_fix
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Tate dual on the kernel of a representation

The last five sections prove that the Bloch-Kato Selmer group of a two-dimensional ordinary representation $W$ vanishes when $W$ has an Euler system class. They work with $W$ and with its Tate dual $W^*$. This section fixes the setting and the normal form of $W$, and proves two facts about the kernel of $W$. First, the [[cyclotomic character|XSGB5K2KEG]] is not trivial on this kernel. Second, a cocycle of $W^*$ that vanishes on the common kernel of $W$ and of the cyclotomic character is a coboundary. The second fact is used in the proof of strict vanishing in Section 22.

### Setting

Let $\ell$ be a prime, $\Omega$ an algebraic closure of $\mathbb{Q}$ and $G_{\mathbb{Q}} = \mathrm{Gal}(\Omega/\mathbb{Q})$. Let $\varepsilon : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^\times$ be the cyclotomic character, and $\chi : G_{\mathbb{Q}} \to \mathbb{Z}_\ell^\times$ the same character with values in $\mathbb{Z}_\ell^\times$. Let $W : G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ be a homomorphism. We keep the notation of Section 18 for places: $D_A$ and $I_A$ are the decomposition and inertia groups of a valuation ring $A$ of $\Omega$, and a place $q$ of $\mathbb{Q}$ is also its prime number. For $x, y \in \overline{\mathbb{Q}}_\ell^2$ put $\omega(x, y) = x_1y_2 - x_2y_1$.

**Definition 6.20.1 (Tate dual).** The *Tate dual* of $W$ is $W^* = W \otimes \varepsilon\,(\det W)^{-1}$, that is, $W^*(s) = \varepsilon(s)\det W(s)^{-1}\,W(s)$. Put
$$
H = \ker\varepsilon \cap \ker\det W, \qquad N = \ker\varepsilon \cap \ker W.
$$

For a $2 \times 2$ matrix $M$ we have $\omega(Mx, My) = \det M\,\omega(x, y)$. So $\omega(W(s)x, W^*(s)y) = \varepsilon(s)\,\omega(x, y)$, and $\omega$ identifies $W^*$ with $\mathrm{Hom}(W, \overline{\mathbb{Q}}_\ell(1))$, the Tate dual in the usual sense. On $N$ both $W$ and $W^*$ are trivial, and $N \subseteq H$.

A *cocycle* for $W$ is a continuous map $y : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^2$ with $y(st) = y(s) + W(s)y(t)$. It is a *coboundary* if $y(s) = W(s)x - x$ for some $x$.

**Definition 6.20.2 (Normal form).** Let $e \geq 0$, $S$ a finite set of places of $\mathbb{Q}$ and $A$ a valuation ring of $\Omega$. Then $W$ is in *normal form for $(e, S, A)$* if:

1. $\ell \neq 2$ and $e \geq 1$;
2. $W$ is continuous, and its entries lie in $\mathcal{O}$ for the ring $\mathcal{O}$ of some coefficient datum;
3. $S$ contains the place $\ell$, and $I_B \subseteq \ker W$ for each place $w \notin S$ and each $B$ over $w$;
4. $(\det W)^2 = 1$, and $\det W(s) = -1$ for each complex conjugation $s$;
5. the restriction of $W$ to $H$ is irreducible;
6. $A$ lies over $\ell$, and $W(s)_{21} = 0$ for $s \in D_A$;
7. there is $m \geq 1$ with $W(s)_{11}^m = \varepsilon(s)^{em}$ for $s \in I_A$;
8. there is $s \in D_A$ with $W(s)_{11} \neq \varepsilon(s)$.

So $W$ is odd, unramified outside $S$, and ordinary at $A$: on $D_A$ it has a line on which inertia acts by $\varepsilon^e$ up to a character of finite order, and, since $\det W = \pm 1$, inertia acts on the quotient by $\varepsilon^{-e}$ up to a character of finite order. The determinant condition makes $W^*(s) = \varepsilon(s)\det W(s)\,W(s)$. This is the form in which [the theorem on zeta classes](/entry/zeta-ur/) states its hypothesis.

### The cyclotomic character on the kernel

We use one fact on compact groups.

**Lemma 6.20.3 (Homomorphisms to $\mathbb{Z}_\ell$).** Let $\Gamma$ be a compact group and $r : \Gamma \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ a continuous irreducible representation with entries in $\mathcal{O}$ and $(\det r)^2 = 1$. Let $\lambda : \Gamma \to \mathbb{Z}_\ell$ be a continuous homomorphism with $\ker r \subseteq \ker\lambda$. Then $\lambda = 0$.

The map $\lambda$ factors through the image $r(\Gamma)$, a compact $\ell$-adic Lie group with determinant $\pm 1$. Its Lie algebra is a subalgebra of $\mathfrak{sl}_2$. If it is $\mathfrak{sl}_2$, the commutator subgroup is open. If it is a Borel or a nilpotent subalgebra, $r$ fixes a line, which irreducibility excludes. If it is a Cartan subalgebra, an element outside the torus inverts the torus, so $2\lambda = 0$ on an open subgroup. In all cases $\lambda$ vanishes on an open subgroup, and $\mathbb{Z}_\ell$ has no nonzero finite subgroups.

**Theorem 6.20.4 (The kernel moves the roots of unity).** Let $W$ be in normal form for $(e, S, A)$. Then there is $a \in \ker W$ with $\varepsilon(a) \neq 1$.

Lean: `GlobalTheory.Ord2.exists_ker_eps_ne_one` (also `GlobalTheory.T.exists_ker_rep_cyclotomic_ne_one_normalForm`, a second name).

*Proof.* Suppose that $\varepsilon(a) = 1$ for all $a \in \ker W$. Since $\ell$ is odd, the $\ell$-adic logarithm maps $\mathbb{Z}_\ell^\times$ continuously and homomorphically to $\mathbb{Z}_\ell$. Put $\lambda = \log\circ\chi$. Then $\lambda : G_{\mathbb{Q}} \to \mathbb{Z}_\ell$ is a continuous homomorphism, and $\ker W \subseteq \ker\chi \subseteq \ker\lambda$. The restriction of $W$ to $H$ is irreducible, so $W$ is irreducible. By the lemma, with $\Gamma = G_{\mathbb{Q}}$, $\lambda = 0$.

Now let $\sigma$ be a Frobenius element at a place over $2$. Since $\ell \neq 2$, $\chi(\sigma) = 2$. Then $\chi(\sigma^{\ell-1}) = 2^{\ell-1}$. This number is $\equiv 1 \pmod{\ell}$ by Fermat's theorem, and it is not $1$. On $1 + \ell\mathbb{Z}_\ell$ the logarithm is injective, since $\ell$ is odd. So $\lambda(\sigma^{\ell-1}) = \log(2^{\ell-1}) \neq 0$, a contradiction. $\square$

Thus the field cut out by $\ker W$ does not contain all $\ell$-power roots of unity. Only conditions 1, 2, 4 and 5 of the normal form are used.

### Cocycles of the dual that vanish on the kernel

**Theorem 6.20.5 (Vanishing on the kernel).** Let $W$ be in normal form for $(e, S, A)$. Let $z$ be a cocycle for $W^*$ with $z(g) = 0$ for all $g \in N$. Then $z$ is a coboundary.

Lean: `GlobalTheory.Ord2.h1dual_of_vanish_fix` (also `GlobalTheory.T.tateDual_cocycle_coboundary_of_vanish_on_fixing`, a second name).

*Proof.* By the previous theorem there is $a \in \ker W$ with $\varepsilon(a) \neq 1$. Since $W(a) = 1$, $W^*(a) = \varepsilon(a)\det W(a)^{-1}W(a) = \varepsilon(a)$, a scalar.

Let $g \in G_{\mathbb{Q}}$ and put $k = (ga)^{-1}(ag)$. Then $W(k) = W(a)^{-1}W(g)^{-1}W(a)W(g) = 1$, and $\varepsilon(k) = 1$ since $\varepsilon$ has abelian image. So $k \in N$ and $z(k) = 0$. The cocycle relation gives $z(ag) = z(ga\cdot k) = z(ga) + W^*(ga)z(k) = z(ga)$. Expand both sides:
$$
\begin{aligned}
z(ag) &= z(a) + W^*(a)z(g) = z(a) + \varepsilon(a)z(g),\\
z(ga) &= z(g) + W^*(g)z(a).
\end{aligned}
$$
Hence $(\varepsilon(a) - 1)\,z(g) = W^*(g)z(a) - z(a)$. Put $x = (\varepsilon(a) - 1)^{-1}z(a)$. Then $z(g) = W^*(g)x - x$ for all $g$. $\square$

This is the argument known as Sah's lemma: a central element that acts by a scalar different from $1$ kills the first cohomology. Here the group is $G_{\mathbb{Q}}/N$, through which $z$ factors, and the central element is the image of $a$. The theorem says that the restriction map from $H^1(G_{\mathbb{Q}}, W^*)$ to $\mathrm{Hom}(N, \overline{\mathbb{Q}}_\ell^2)$ is injective.

**Remark 6.20.6 (Formalization).** The second names are wrappers of the form `first | exact @… | …`. The lemma on homomorphisms to $\mathbb{Z}_\ell$ is `GlobalTheory.T.hom_padicInt_trivial_of_irreducible_compact_rep`; we read it as a statement, and the sketch after it is ours. In the formal proof the Frobenius element at $2$ comes from a place over $2$ whose residue field has $n \geq 2$ elements, and the contradiction uses only $n^{\ell-1} \neq 1$. The first theorem uses only the fields `l_odd`, `cont`, `int`, `det2` and `irr` of the normal form ([ExistsKerRepCyclotomicNeOneNormalForm.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsKerRepCyclotomicNeOneNormalForm.lean#L138)). The second theorem uses the normal form only through the first ([TateDualCocycleCoboundaryOfVanishOnFixing.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/TateDualCocycleCoboundaryOfVanishOnFixing.lean#L10)).
