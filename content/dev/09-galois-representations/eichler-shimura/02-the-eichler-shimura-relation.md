---
title: The Eichler-Shimura relation
decls:
  - UpperTheory.Gal.Mod.esGen_holds
  - UpperTheory.Gal.Mod.esGen_all
  - UpperTheory.Gal.Mod.towES_holds
  - UpperTheory.Gal.Mod.esStep_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Eichler-Shimura relation

At a place $w \nmid \ell$ of good reduction, a Galois piece is unramified, and a Hecke polynomial kills its Frobenius. This is the Eichler-Shimura relation. We prove it in three steps: first for a smooth proper scheme over a discrete valuation ring with correspondences that satisfy a congruence relation on the special fibre, then for the piece of a Hecke tower, and last for its graded part.

**Definition 3.2.1 (Hecke polynomial).** Let $A$ be a commutative ring, $q, n \in \mathbb{N}$ and $\vartheta_0, \dots, \vartheta_n \in A$. Put $c_q(j) = (-1)^j q^{\binom{j}{2}}$. The *Hecke polynomial* is
$$P_{q,n,\vartheta}(X) = \sum_{j=0}^{n} c_q(j)\, \vartheta_j\, X^{n-j} \in A[X].$$
For a finite multiset $R$ in $A$ write $\operatorname{root}_R(X) = \prod_{r \in R}(X - r)$.

Lean: `UpperTheory.Gal.crystallineComparison.heckePol` (also `UpperTheory.Gal.crystallineComparison.rootPol`, `UpperTheory.Gal.Mod.co`).

For $\mathrm{GL}_n$ over a local field with residue field of order $q$, and $\vartheta_j$ the eigenvalue of the Hecke operator of $\operatorname{diag}(\varpi, \dots, \varpi, 1, \dots, 1)$ with $j$ entries $\varpi$, this is the classical Hecke polynomial. For the modular curve the relation $P_{p,2,\vartheta}(\mathrm{Frob}) = 0$ on $H^1$ follows from the congruence relation $T_p = F + V$ on the reduction mod $p$ (G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Chapter 7).

**Definition 3.2.2 (good model with a congruence relation).** Let $H$ be a Hecke tower over a field $K$, let $L$ be a field and $\theta : \Gamma \to L$. Let $O \subseteq K$ be a ring. A *good model* $C$ of $(H, \theta)$ over $O$ consists of the following data.

1. A smooth projective scheme $p : Y \to \operatorname{Spec} O$, of some relative dimension.
2. A map $\pi : Z \to Y$ over $O$ such that $Z \to Y_K$ is finite étale.
3. A finite group $\Delta$ that acts on $Z$, such that $\coprod_{\delta \in \Delta} Z \cong Z \times_{Y_K} Z$ through the action. For each $\delta$ there is $g \in \Gamma$ with $s_g$ an isomorphism, $t_g = \delta \circ s_g$ and $\theta(g) = 1$.

The model is *onto* if $Z \to Y_K$ is surjective. Then $Z \to Y_K$ is a Galois cover with group $\Delta$. A correspondence $(s, t)$ on $Y$ *lies under* $g \in \Gamma$ with degree $m > 0$ if there is a map $\kappa$ from $Y_g$ to the source of $s$ and $t$ with $\pi \circ s_g = s \circ \kappa$ and $\pi \circ t_g = t \circ \kappa$, such that the induced map $Y_g \to Z \times_Y (\text{source})$ is finite étale of degree $m$. Let $p$ be a prime, $q = p^f$ and $\varpi$ a uniformizer of $O$. The model satisfies the *congruence relation* for $(p, f, n, \vartheta)$ if there are correspondences $T_0, \dots, T_n$ on $Y$ over $O$, finite and étale after inverting $p$, and $\gamma_j \in \Gamma$, $m_j > 0$, such that $T_j$ lies under $\gamma_j$ with degree $m_j$, $\theta(\gamma_j) = m_j \vartheta_j$, and at each generic point of the special fibre the $q$-power Frobenius $F$ satisfies the identity of zero-cycles
$$\sum_{j=0}^{n} c_q(j)\, F^{\,n-j} \circ T_j = 0.$$

Lean: `UpperTheory.Gal.Int.Geo.Cover`, `UpperTheory.Gal.Int.Geo.Cover.Onto`, `UpperTheory.Gal.Int.Geo.Cover.Lies`, `UpperTheory.Gal.Int.Geo.Cover.Cong` (also `UpperTheory.Gal.crystallineComparison.PtId`, `UpperTheory.Gal.Int.Geo.CongAt`).

For a number field $E$ and a finite place $w$, let $O_w \subset E$ be the valuation ring of $w$. We say that $(H, \theta)$ has a *congruence model at $w$* with data $(n, \vartheta)$ if it has an onto good model over $O_w$ that satisfies the congruence relation for the prime $p$ under $w$ and $p^f = N(w)$.

**Theorem 3.2.3 (smooth and proper base change).** Let $O$ be a discrete valuation ring with fraction field $K$ and residue field $\kappa$, and let $Y$ be smooth and proper over $O$. Let $\ell$ be a prime invertible in $\kappa$. Then the specialization map $H^n(Y_{\bar\kappa}, \mathbb{Q}_\ell) \to H^n(Y_{\bar K}, \mathbb{Q}_\ell)$ is an isomorphism compatible with the Galois actions. In particular inertia acts trivially on $H^n(Y_{\bar K}, \mathbb{Q}_\ell)$ (SGA 4, XII and XVI; J. S. Milne, *Étale Cohomology*, Chapter VI, §4).

Lean: `GlobalTheory.EtC.SpecGood` (the statement; it also asks for equivalences on torsion coefficients).

In this chapter the theorem is a hypothesis, derived in another chapter from [proper base change](/entry/proper-base-change/) and an [étale base change theorem](/entry/etale-base-change-of-duality/).

**Theorem 3.2.4 (Eichler-Shimura on a good model).** Let $p$ be a prime, $q = p^f$, $n \in \mathbb{N}$ and $\ell$ a prime. Let $O$ be a discrete valuation ring with a uniformizer $\varpi$, such that $p$ is not a unit in $O$. Let $K$ be a field over $O$ with $p \neq 0$ in $K$, and $\kappa$ a field over $O$ in which $\varpi$ maps to $0$ and with $a^{q} = a$ for all $a \in \kappa$. Let $\Omega$ be an algebraically closed field over $K$ and $V \subseteq \Omega$ a valuation ring containing the image of $O$. Let $\bar\kappa$ be an algebraically closed field over $\kappa$ with a surjective ring map $r : V \to \bar\kappa$ that agrees with $O \to \kappa \to \bar\kappa$ on $O$, and suppose that $\ell$ is a unit in $\bar\kappa$. Let $Y$ be smooth and proper over $O$, with correspondences $T_0, \dots, T_n$ on $Y$ over $O$ that satisfy the congruence relation, and let $c_j$ be the base change of $T_j$ to $Y_\Omega = (Y_K)_\Omega$. Let $\sigma \in \operatorname{Aut}(\Omega/K)$ preserve $V$, and let $k \in \mathbb{Z}$. Then, on $H^k(Y_\Omega, \mathbb{Q}_\ell)$:

1. if $r(\sigma v) = r(v)$ for all $v \in V$, then $\sigma$ acts trivially;
2. if $r(\sigma v) = r(v)^q$ for all $v \in V$, then
$$\sum_{j=0}^{n} c_q(j)\, c_j \circ (\sigma^{-1})^{n-j} = 0.$$

Lean: `UpperTheory.Gal.Mod.esGen_all` (also `UpperTheory.Gal.Mod.esGen_holds`, the same statement with the specialization theorem as a hypothesis).

*Proof.* By the specialization theorem we may compute on the special fibre $Y_{\bar\kappa}$, and $\sigma$ acts there through its image in $\operatorname{Gal}(\bar\kappa/\kappa)$. Part 1 follows at once. For part 2, let $\tau$ be the image of $\sigma$, so $\tau(x) = x^q$. On $Y_{\bar\kappa}$ the relative Frobenius $\mathrm{Fr}$ composed with the Galois automorphism $\tau$ of the base is the absolute $q$-power Frobenius. The absolute Frobenius acts as the identity on étale cohomology with coefficients prime to $p$. So $\tau^{-1}$ acts on cohomology as $\mathrm{Fr}^*$. The congruence relation is an identity of zero-cycles at generic points of the special fibre. These points are dense in the special fibre, $Y$ is normal, and the correspondences commute with base change, so the identity becomes the operator identity $\sum_j c_q(j)\, c_j \circ (\mathrm{Fr}^*)^{n-j} = 0$. $\square$

**Theorem 3.2.5 (Eichler-Shimura for a tower).** Let $\ell$ and $p$ be primes, $q = p^f$ and $n \in \mathbb{N}$. Let $O$ be a discrete valuation ring in which $p$ is not a unit and whose residue field satisfies $a^q = a$ for all $a$. Let $K$ be a field over $O$ with $p \neq 0$ in $K$, $\Omega$ an algebraically closed field over $K$, and $V \subseteq \Omega$ a valuation ring that contains the image of $O$, such that the maximal ideal of $O$ maps into the maximal ideal of $V$ and $\ell$ is a unit in $V$. Let $L$ be a field over $\mathbb{Q}_\ell$ and $H$ a nice Hecke tower over $K$ with $\theta : \Gamma \to L$. Let $C$ be a good model of $(H, \theta)$ over $O$ that satisfies the congruence relation for $(p, f, n, \vartheta)$, and suppose that $\Pi_\theta$ is stable under $\operatorname{Aut}(\Omega/K)$. Let $\sigma \in \operatorname{Aut}(\Omega/K)$ preserve $V$, and let $x \in \Pi_\theta$. Then:

1. if $\sigma$ is in the inertia group of $V$, then $\sigma x = x$;
2. if $\sigma$ is a Frobenius element of $V$, that is $\sigma(v) \equiv v^q$ modulo the maximal ideal for all $v \in V$, then
$$\sum_{j=0}^{n} c_q(j)\, \vartheta_j\, (\sigma^{-1})^{n-j} x = 0.$$

Lean: `UpperTheory.Gal.Mod.towES_holds`.

*Proof.* The group $\Delta$ acts on $Z$ through Hecke correspondences with eigenvalue $1$, so $\Pi_\theta$ lies in the $\Delta$-invariants of $H^*(Z_\Omega)$. These are the pullback of $H^*(Y_{K,\Omega})$, because $Z \to Y_K$ is a Galois cover with group $\Delta$. If $T_j$ lies under $\gamma_j$ with degree $m_j$, then pullback to $Z$ carries the action of $c_j$ to $m_j^{-1}$ times the Hecke operator $T_{\gamma_j}$. This uses that the Hecke operators of a nice tower are correspondence operators, which holds when $\ell$ is invertible. So $c_j$ acts on $\Pi_\theta$ by $\theta(\gamma_j)/m_j = \vartheta_j$. Now apply the previous theorem on $Y$ and pull back to $Z$. $\square$

**Theorem 3.2.6 (Eichler-Shimura step).** Let $E$ be a number field, $\Omega$ an algebraic closure, $\ell$ a prime and $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. Let $H$ be a nice Hecke tower over $E$, $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$, and $\rho$ a continuous Galois piece of $(H, \theta)$. Let $w$ be a finite place with $\ell \notin w$. Suppose that $(H, \theta)$ has a congruence model at $w$ with data $(n, \vartheta)$, that $\vartheta_0 \neq 0$, and that
$$\iota\, P_{N(w), n, \vartheta}(X) = \iota(\vartheta_0)\, \operatorname{root}_R(X)$$
for a multiset $R$ in $\mathbb{C}$. Then at every place of $\Omega$ over $w$, $\rho$ is trivial on inertia, and $\operatorname{root}_{\iota^{-1}R}$ kills $\rho(\sigma^{-1})$ for every Frobenius element $\sigma$.

Lean: `UpperTheory.Gal.Mod.esStep_holds`.

*Proof.* The valuation ring $O_w$ and a place $A$ of $\Omega$ over $w$ satisfy the hypotheses of the previous theorem: the residue field of $O_w$ has $N(w)$ elements, the maximal ideal of $O_w$ maps into that of $A$, and $\ell$ is a unit in $A$ since $\ell \notin w$. The piece $\Pi_\theta$ is Galois stable by [Theorem 3.1.6](/entry/rep-ex-holds/). So for a matrix form $\rho_0$, $\rho_0$ is trivial on inertia and the polynomial $P_{N(w), n, \vartheta}$ kills $\rho_0(\sigma^{-1})$. Divide by $\vartheta_0$ and apply $\iota^{-1}$: then $\operatorname{root}_{\iota^{-1}R}$ kills $\rho_0(\sigma^{-1})$. A polynomial that kills a block triangular matrix kills its block diagonal part, and the block diagonal part of the identity is the identity. So the same holds for $\rho$. $\square$

**Remark 3.2.7.** The conclusion of the last theorem says that $\operatorname{root}_{\iota^{-1}R}$ kills the Frobenius. It does not say that the characteristic polynomial of Frobenius equals a power of $\operatorname{root}_{\iota^{-1}R}$. The relation is for the inverse $\sigma^{-1}$ of an arithmetic Frobenius, that is a geometric Frobenius. Here $O_w$ is the valuation ring of $w$ inside $E$, not its completion, so a congruence model at $w$ is a model over a localization of $\mathcal{O}_E$.

**Remark 3.2.8 (Formalization).** The conclusion of Theorem 3.2.6 is the predicate `ESAt`, and $O_w$ is `UpperTheory.Gal.Int.Geo.Ow`. `UpperTheory.Gal.Mod.esGen_all` is `UpperTheory.Gal.Mod.esGen_holds` applied to the specialization theorem `GlobalTheory.EtC.SpecGood`, which another chapter derives from `UpperTheory.Et.proper_base_change` and `UpperTheory.Et.etale_base_change_of_duality`. The density and normality facts in the proof of Theorem 3.2.4 are the inputs `DenseGen` and `BaseFacts`, and the step from zero-cycles to cohomology is the input `esPt_holds`.
