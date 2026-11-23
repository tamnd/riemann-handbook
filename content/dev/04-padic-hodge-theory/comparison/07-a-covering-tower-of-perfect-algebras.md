---
title: A covering tower of perfect algebras
decls:
  - CrystallineSemistableComparison.D.cov_tower
  - CrystallineSemistableComparison.D.Leaf.cov_tower
  - CrystallineSemistableComparison.D.powers_good
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A covering tower of perfect algebras

The local comparison of [Theorem 2.6.9](/entry/local-of/) has one hypothesis: three functors on perfect algebras have descent to test algebras up to each element of $W(\mathfrak{m}^\flat)$. This section and the next prove that hypothesis. The method is the usual one for descent: cover a perfect algebra $A$ by a large algebra $B$, compute the Čech complex of $B$ over $A$, and show that it is exact up to small elements. The difficulty is to find $B$. It must be perfect, faithfully flat over $A$ in a weak sense, algebraically closed and of valuation type, and each map from $A$ to a test algebra must extend to $B$. We build such a $B$ as the colimit of a tower in which each step adjoins solutions of polynomial equations ([Theorem 2.7.6](/entry/d-cov-tower/)). Then we show that $B$ and its tensor powers give the data that the descent criterion of the next section needs ([Theorem 2.7.9](/entry/powers-good/)). The idea is close to the use of $v$-covers and $\mathrm{arc}$-covers of perfect rings, but here every step is elementary.

We keep the notation of the earlier sections. So $\ell$ is a prime, $\mathcal{O}_{\mathbb{C}_\ell}^\flat$ is the tilt of $\mathcal{O}_{\mathbb{C}_\ell}$ (see the Background on [period rings](/learn/galois-representations/#period-rings)), and $\pi \in \mathcal{O}_{\mathbb{C}_\ell}^\flat$ is the element with $\pi^\sharp = \ell$. In the first part of the section, $p$ is a prime, all rings are commutative, and $r = (r_0, r_1, \ldots)$ is a sequence in a ring $A$.

**Definition 2.7.1 (Perfect ring and root system).** A ring $A$ is *perfect* (of characteristic $p$) if $p = 0$ in $A$ and $x \mapsto x^p$ is a bijection of $A$. A sequence $r$ in $A$ is a *root system* if $r_{k+1}^p = r_k$ for all $k$.

In a perfect ring each element has a unique system of $p$-power roots. In $\mathcal{O}_{\mathbb{C}_\ell}^\flat$ we write $r_k = \pi^{1/\ell^k}$. This is the root system of the rest of the chapter.

**Definition 2.7.2 (Good map and covering up to roots).** Let $A$ be a ring with a root system $r$.

1. An $A$-linear map $d : K_1 \to K_0$ is *good* if for every perfect $A$-algebra $C$ and every $w \in C \otimes_A K_1$ with $(C \otimes d)(w) = 0$, each $r_k w$ lies in the image of $C \otimes_A \ker d$.
2. An $A$-algebra $B$ is a *covering up to roots* if for all perfect $A$-algebras $K_1$ and $K_0$, every good $A$-linear map $d : K_1 \to K_0$, and every $z \in K_0$ such that $1 \otimes z$ lies in the image of $B \otimes d$, each $r_k z$ lies in the image of $d$.

A good map is one whose kernel commutes with base change to perfect algebras, up to the roots. The second condition is the part of faithful flatness that descent uses: an equation that has a solution after base change to $B$ has a solution over $A$ after multiplication by a root. If $B$ is faithfully flat over $A$, then $B$ is a covering up to roots, because $\operatorname{coker}(d) \to B \otimes_A \operatorname{coker}(d)$ is injective.

**Definition 2.7.3 (Algebraically closed and of valuation type).** Let $T$ be a ring and $\varpi \in T$.

1. $T$ is *algebraically closed* if every monic polynomial over $T$ of positive degree has a root in $T$.
2. $T$ is *of valuation type for $\varpi$* if for all $f, g \in T$ such that some power $\varpi^N$ lies in the ideal $(f, g)$, there is an idempotent $e \in T$ with $e f \in (g)$ and $(1 - e) g \in (f)$.

For a map $\varphi : A \to B$ there are relative forms: every monic polynomial over $A$ of positive degree gets a root in $B$, and the idempotent of the second condition exists in $B$ for $\varphi(f)$ and $\varphi(g)$.

The second condition says that, away from $\varpi = 0$, the ring is locally a valuation ring: on the part where $e = 1$, $g$ divides $f$, and on the other part $f$ divides $g$. For example, a valuation ring $V$ with $\varpi$ in its maximal ideal is of valuation type with $e \in \{0, 1\}$, and so is a finite product of such rings.

**Definition 2.7.4 (Splitting of points).** Let $\varphi : A \to B$ be a map of rings and $\varpi \in A$. Then $\varphi$ *splits points* for $\varpi$ if every map $x : A \to T$ to a perfect ring $T$ that is algebraically closed and of valuation type for $x(\varpi)$ extends through $\varphi$: there is $y : B \to T$ with $y \circ \varphi = x$.

**Lemma 2.7.5 (One step).** Let $A$ be a perfect ring and $r$ a root system in $A$. Then there is a perfect $A$-algebra $B$ that is a covering up to roots, such that $A \to B$ is algebraically closed and of valuation type for $r_0$ in the relative sense, and such that $A \to B$ splits points for $r_0$.

Lean: `CrystallineSemistableComparison.D.cov_step`.

*Proof.* Consider the systems of polynomial equations over $A$ of two kinds: $P(X) = 0$ for each monic $P$ of positive degree; and $E^2 = E$, $E f = Y g$, $(1 - E) g = Z f$ for each pair $f, g$ with $r_0^N \in (f, g)$ for some $N$. For one system, a covering up to roots with a solution exists: for the first kind, a root of $P$ can be adjoined in a covering up to roots; for the second kind, the idempotent can be adjoined in a covering up to roots, since $(f, g)$ contains a power of $r_0$. Iterating gives a covering for any finite set of systems. A limit argument then gives one perfect covering $B$ up to roots in which all systems have solutions, and such that each map $x : A \to T$ to a perfect ring in which all the systems have solutions extends to $B$. If $T$ is algebraically closed and of valuation type for $x(r_0)$, then all systems have solutions in $T$, so $A \to B$ splits points. $\square$

**Theorem 2.7.6 (Covering tower).** Let $A$ be a perfect ring and $r$ a root system in $A$. Then there is an $A$-algebra $B$ such that:

1. $B$ is perfect;
2. $B$ is a covering of $A$ up to roots;
3. $B$ is algebraically closed and of valuation type for the image of $r_0$;
4. the map $A \to B$ splits points for $r_0$.

Lean: `CrystallineSemistableComparison.D.cov_tower` and `CrystallineSemistableComparison.D.Leaf.cov_tower` (a second name for `CrystallineSemistableComparison.D.cov_tower`).

*Proof.* We build a sequence $A = G_0 \to G_1 \to G_2 \to \cdots$ and take $B$ as its colimit.

1. *The tower.* The identity of $A$ is a covering up to roots. Given $G_n$, perfect and a covering of $A$ up to roots, let $G_{n+1}$ be the algebra that the one-step lemma gives for $G_n$ and the image of $r$. A composite of coverings up to roots is a covering up to roots, so $G_{n+1}$ is again a perfect covering of $A$ up to roots.
2. *Perfect.* A colimit of perfect rings is perfect, so $B = \varinjlim G_n$ is perfect.
3. *Covering.* Let $d$ and $z$ be as in the definition, with $1 \otimes z$ in the image of $B \otimes d$. A preimage in $B \otimes K_1$ is a finite sum, so its coordinates lie in the image of some $G_n$, and $1 \otimes z$ lies in the image of $G_n \otimes d$. Since $G_n$ is a covering up to roots, each $r_k z$ lies in the image of $d$.
4. *Closure.* A monic polynomial over $B$ has its coefficients in the image of some $G_n$, and it gets a root in $G_{n+1}$. The same holds for the idempotent of the valuation condition. So $B$ is algebraically closed and of valuation type for $r_0$.
5. *Splitting.* Let $x : A \to T$ be a map to a perfect ring that is algebraically closed and of valuation type for $x(r_0)$. Put $y_0 = x$. If $y_n : G_n \to T$ extends $x$, the splitting property of $G_n \to G_{n+1}$ gives $y_{n+1} : G_{n+1} \to T$ that extends $y_n$. The compatible family $(y_n)$ defines a map $B \to T$ that extends $x$.

This proves the four properties. $\square$

The covering tower gives the input for the descent criterion. That criterion uses the following structure. Let $j : \mathcal{T} \to \mathcal{C}$ be a functor (below, the inclusion of test algebras into perfect algebras), and let $A$ be an object of $\mathcal{C}$.

**Definition 2.7.7 (Powers of a cover).** A *system of powers* of $A$ consists of a map $f : A \to B$ in $\mathcal{C}$, objects $K_n$ with maps $a_n : A \to K_n$ and $\iota_{n,i} : B \to K_n$ for $i < n$ that agree on $A$, and face maps $\delta_{n,k} : K_n \to K_{n+1}$ for $k \leq n$ with the simplicial relations, such that $a_0$ and $\iota_{1,0}$ are isomorphisms and such that $K_n$ has the universal property of the $n$-fold tensor power of $B$ over $A$ for maps into objects $j(t)$: maps $K_n \to j(t)$ correspond to $n$-tuples of maps $B \to j(t)$ that agree on $A$.

For a functor $F$ from $\mathcal{C}$ to modules over a ring $R$, the face maps give the Čech complex
$$F(K_0) \to F(K_1) \to F(K_2) \to \cdots, \qquad d_n = \sum_{k \leq n} (-1)^k F(\delta_{n,k}).$$
Since $K_0 \cong A$ and $K_1 \cong B$, it starts with $F(A) \to F(B)$.

**Definition 2.7.8 (Good powers).** Let $I$ be an ideal of $R$. A system of powers of $A$ is *good* for $F$ and $I$ if:

1. every map $A \to j(t)$ extends through $f : A \to B$;
2. for every $s \in I$, the Čech complex is injective up to $s$ at $F(K_0)$ and exact up to $s$ at each later term;
3. there are an object $t_0$ of $\mathcal{T}$ and a map $g : B \to j(t_0)$ such that every map $B \to j(t)$ factors as $j(u) \circ g$ for a unique $u : t_0 \to t$, and such that $F(g)$ is an isomorphism up to each $s \in I$.

The words "injective up to $s$", "exact up to $s$" and "isomorphism up to $s$" have the meaning of section 6. The first and third conditions say that $B$ is close to a test algebra. The second is the Čech exactness that descent along $A \to B$ needs.

**Theorem 2.7.9 (Good powers for tensor functors).** Assume that $\mathcal{O}_{\mathbb{C}_\ell}^\flat$ is a valuation domain, that each nonzero $a$ divides some power $\pi^M$, and that each non-unit is divisible by some $r_k$. Let $N$ be an $\mathcal{O}_{\mathbb{C}_\ell}^\flat$-module and $M \geq 0$ with $\pi^M N = 0$, and let $F$ be the functor $A \mapsto N \otimes A$ on perfect $\mathcal{O}_{\mathbb{C}_\ell}^\flat$-algebras. Then each perfect $\mathcal{O}_{\mathbb{C}_\ell}^\flat$-algebra $A$ has a system of powers, relative to the inclusion of test algebras, that is good for $F$ and for the ideal generated by the $r_k$.

Lean: `CrystallineSemistableComparison.D.powers_good`.

*Proof.* The images of the $r_k$ in $A$ form a root system, so the covering tower gives an algebra $B$ over $A$ with the four properties of [Theorem 2.7.6](/entry/d-cov-tower/). Let $K_n$ be the $n$-fold tensor power of $B$ over $A$, with the usual face maps.

1. *Čech exactness.* Since $B$ is perfect and a covering of $A$ up to roots, the Čech complex of $N \otimes B$ over $N \otimes A$ is injective up to each element of the ideal of the roots at the first term, and exact up to these elements at each later term. The assumptions on $\mathcal{O}_{\mathbb{C}_\ell}^\flat$ and the bound $\pi^M N = 0$ reduce an element of this ideal to a single root $r_k$.
2. *Extension of points.* A map from $A$ to a test algebra $T$ is a map to a perfect ring that is algebraically closed and of valuation type for $\pi$. By the splitting property it extends to $B$.
3. *The test algebra of $B$.* Let $t_0$ be the $r_0$-adic completion of $B$. Since $B$ is algebraically closed and of valuation type, $t_0$ is a test algebra. Each map from $B$ to a test algebra factors in a unique way through $t_0$, because a test algebra is complete. The map $N \otimes B \to N \otimes t_0$ is an isomorphism up to the roots.

With these three facts, $B$ and the $K_n$ form a good system of powers. $\square$

**Remark 2.7.10 (Formalization).** The definitions are in [IsCompl.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/WittExactSequences/IsCompl.lean#L11), and the systems of powers in [CechAugRow.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/CechPairings/CechAugRow.lean#L135). `D.Leaf.cov_tower` in TestOfPre.lean is a second name, as are `test_of_pre` and `cech_tens` there and `cov_cmp`, `cov_mono`, `cov_comp`, `colim_ex`, `colim_pf`, `colim_test` in TensCompl.lean; the proofs behind the last six are in `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`, a folder whose name has no relation to this content. We did not open those proofs, nor `cov_root`, `cov_blow`, `fin_step` and `big_step` in the proof of the one-step lemma, nor `cech_tens`, `powers_abs` and `test_clause`. So the reasons in step 1 of the last proof and in step 3 ("because a test algebra is complete") follow the statements of these lemmas, not a check of their proofs.
