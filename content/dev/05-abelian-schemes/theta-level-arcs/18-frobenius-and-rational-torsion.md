---
title: Frobenius and rational torsion
decls:
  - GlobalTheory.T.frobenius_counts_integral_torsion_specialFibre
  - GlobalTheory.SS.frobenius_on_integral_torsion
  - GlobalTheory.SS.isSemiAbelian_of_rational_torsion
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frobenius and rational torsion

This section proves the criterion of Grothendieck and Raynaud for semi-abelian reduction. Let $A$ be a principally polarized abelian variety over a field $K$ of characteristic $0$, and let $\ell \geq 3$ be a prime such that the Galois group of $K$ fixes the $\ell$-torsion of $A$. Let $G$ be a smooth connected group model of $A$ to which a fixed power of every rational point extends, such as the [neutral group model](/entry/exists-neutral-group-model/). Then $G$ is semi-abelian. The proof counts the $\ell$-power torsion that extends to integral points, with the weights of a Frobenius lift. The next section uses the criterion to prove potential semi-abelian reduction.

### Group schemes over a field

**Definition 6.18.1 (Smooth connected group).** A group scheme $G$ over a scheme $S$ is *smooth and connected* if it is commutative, smooth, separated, quasi-compact and geometrically connected over $S$.

Lean: `GlobalTheory.SS.SmConn`.

**Definition 6.18.2 (Frobenius of level $q$).** Let $G$ be a group scheme over a field $k$, and let $q \geq 1$. An endomorphism $F$ of $G$ is a *Frobenius of level $q$* if $F$ is a homomorphism and, for each affine open set $U$ of $G$ and each $f \in \mathcal{O}(U)$, there is $m \geq 1$ such that $U = (F^m)^{-1} U$ and $(F^m)^* f = f^{q^m}$.

Lean: `GlobalTheory.SS.FrobG`.

**Definition 6.18.3 (Ample cubical bundle).** Let $G$ be a group scheme over $S$. A line bundle $L$ on $G$ is an *ample cubical bundle* if the theta bundle $\Theta(L)$ is trivial, the bundle $\iota^* L \otimes L^{-1}$ is trivial, where $\iota$ is the inverse, and there is $n \geq 1$ such that $G$ is covered by the nonvanishing loci of sections of $L^{n}$ that are affine.

Lean: `GlobalTheory.SS.AmpleCub`.

**Definition 6.18.4 (Group model).** Let $K \to L$ and $W \to L$ be ring maps, let $A$ be a group scheme over $K$, and let $G$ be a group scheme over $W$. Then $G$ is a *group model* of $A$ over $L$ if $G_L \cong A_L$ as group schemes.

Lean: `GlobalTheory.SS.IsModel`.

### Inputs

**Theorem 6.18.5 (Frobenius on torsion).** Let $k$ be algebraically closed of characteristic $p$, let $\ell \neq p$ be prime, and let $G$ be a smooth connected group over $k$ of dimension $g$ with an ample cubical bundle. Let $F$ be a Frobenius of level $q \geq 2$. Then there are $t, a, m, C \in \mathbb{N}$, a polynomial $P \in \mathbb{Z}[X]$ and a subgroup $V$ of $G(k)$ with these properties. First, $m \geq 1$. Second, every complex root $\beta$ of $P$ has $|\beta| < q^m$. Third, $F^m x = x^{q^m}$ for $x \in V$. Fourth, for each $n$ the $\ell^n$-torsion of $G(k)$ is finite with at most $C \ell^{n(t + 2a)}$ elements, and the $\ell^n$-torsion of $V$ has at most $C \ell^{nt}$ elements. Fifth, $\prod_j (F^{mj} x)^{P_j} \in V$ for every $\ell$-power torsion point $x$. Sixth, if $g \leq t + a$, then $G$ is a torus extension.

Lean: `GlobalTheory.T.frobenius_on_torsion_alt`.

**Theorem 6.18.6 (Frobenius on the special fibre).** Let $\rho : W \to k$ with $k$ of characteristic $p$, let $r \geq 1$ with $\rho(w)^{p^r} = \rho(w)$ for all $w$, and assume that every $c \in k$ satisfies $c^{(p^r)^m} = c$ for some $m \geq 1$. For a smooth connected group $G$ over $W$, the fibre $G_k$ has a Frobenius $F$ of level $p^r$ such that, for every $k$-point $x$ and every ring map $\tau$ with $\tau(c) = c^{p^r}$, the points $F \circ x$ and $x \circ \operatorname{Spec} \tau$ have the same image in $G$.

Lean: `GlobalTheory.SS.exists_frobG_baseChange`.

**Theorem 6.18.7 (Reduction of points).** Let $W \to R \to \Omega$ with $R$ a local domain and $R \to \Omega$ injective, and let $G$ be a smooth connected group over $W$. The points of $G(\Omega)$ that extend to $R$-points form a subgroup $H_0$, with a homomorphism $\mathrm{red} : H_0 \to G_k(k)$ to the residue field $k$ of $R$ that sends a point to the reduction of its $R$-point. If $n$ is a unit in $R$, then $\mathrm{red}$ is injective on the $n$-torsion.

Lean: `GlobalTheory.RedPts.exists_reduction`.

### The transfer lemma

**Lemma 6.18.8 (Transfer).** Let $M$ be a commutative group, $H \leq M$, $r : H \to N$ a homomorphism to a group $N$, $\Phi$ an automorphism of $M$ and $\varphi_j : N \to N$ maps with $\Phi^j(H) \subset H$ and $r(\Phi^j x) = \varphi_j(r x)$. Assume that $r$ is injective on $\ell$-power torsion, that $V \leq N$ has $\varphi_1 x = x^e$ on $V$, that the $\ell^n$-torsion of $N$ is finite, and that $\prod_j \varphi_j(x)^{Q_j} \in V$ for every $\ell$-power torsion $x$ of $N$. Then there is $U \leq M$ such that the $\ell^n$-torsion of $H$ and of $U$ has at most as many elements as that of $N$ and of $V$, such that $\Phi x = x^e$ for $\ell$-power torsion $x \in U$, and such that $\prod_j (\Phi^j x)^{Q_j} \in U$ for $\ell$-power torsion $x \in H$.

Lean: `GlobalTheory.SS.SpecialCount.transfer`.

*Proof.* Let $U$ be the image in $M$ of $r^{-1}(V)$. As $r$ is injective on $\ell^n$-torsion, it embeds the $\ell^n$-torsion of $H$ and $U$ in that of $N$ and $V$. If $x \in U$ is $\ell$-power torsion, then $r(\Phi x) = \varphi_1(r x) = (r x)^e = r(x^e)$, and both $\Phi x$ and $x^e$ are $\ell$-power torsion, so $\Phi x = x^e$. For $x \in H$, the image under $r$ of $\prod_j (\Phi^j x)^{Q_j}$ is $\prod_j \varphi_j(r x)^{Q_j} \in V$. $\square$

### Frobenius counts integral torsion

**Theorem 6.18.9 (Frobenius counts integral torsion).** Let $W \to R \to \Omega$ be ring maps, with $R$ a local domain, $\Omega$ a field and $R \to \Omega$ injective, and let the residue field $k$ of $R$ be algebraically closed of characteristic $p$. Let $r \geq 1$, let $\ell$ be a prime that is a unit in $R$, and assume that every $c \in k$ satisfies $c^{(p^r)^m} = c$ for some $m \geq 1$. Let $\psi : \Omega \to \Omega$ be a ring map that fixes $W$ and that sends $R$ to $R$ with $\psi(x) \equiv x^{p^r}$ modulo the maximal ideal. Let $G$ be a smooth connected group over $W$ of relative dimension $g$, with an ample cubical bundle on $G_k$. Let $M$ be a commutative group with an isomorphism $\theta : M \to G(\Omega)$ and an automorphism $\Psi$ with $\theta(\Psi x) = \theta(x) \circ \operatorname{Spec} \psi$. Then there are $t, a, m, C \in \mathbb{N}$, $Q \in \mathbb{Z}[X]$ and subgroups $H, U \leq M$ with these properties.

1. $m \geq 1$.
2. $x \in H$ if and only if $\theta(x)$ extends to an $R$-point of $G$.
3. For each $n$, the $\ell^n$-torsion of $H$ has at most $C \ell^{n(t + 2a)}$ elements, and the $\ell^n$-torsion of $U$ has at most $C \ell^{nt}$ elements.
4. Every complex root $\beta$ of $Q$ has $|\beta| < (p^r)^m$.
5. $\Psi^m x = x^{(p^r)^m}$ for every $\ell$-power torsion $x \in U$.
6. $\prod_{j \leq \deg Q} (\Psi^{mj} x)^{Q_j} \in U$ for every $\ell$-power torsion $x \in H$.
7. If $g \leq t + a$, then $G_k$ is a torus extension.

Lean: `GlobalTheory.T.frobenius_counts_integral_torsion_specialFibre` (also `GlobalTheory.SS.frobenius_on_integral_torsion`, a second name).

*Proof.* Let $q = p^r$. Since $R \to \Omega$ is injective, $\psi$ restricts to $\sigma : R \to R$, which fixes $W$ and induces $c \mapsto c^q$ on $k$. So $\rho(w)^q = \rho(w)$ for $\rho : W \to k$. The theorem on Frobenius on the special fibre gives a Frobenius $F$ of level $q$ on $G_k$. As $\ell$ is a unit in $R$, $\ell \neq p$. Also $q \geq 2$, and $G_k$ is smooth and connected of dimension $g$. The theorem on Frobenius on torsion gives $t, a, m, C, Q$ and $V$.

The theorem on reduction of points gives $H_0$ and $\mathrm{red}$. Let $H = \theta^{-1}(H_0)$. If $s$ is the $R$-point of $\theta(x)$, then $s \circ \operatorname{Spec} \sigma$ extends $\theta(\Psi x)$. So $\Psi x \in H$, and the reduction of $\Psi x$ is $F$ applied to the reduction of $x$. By induction, the reduction of $\Psi^j x$ is $F^j$ applied to the reduction of $x$.

Apply the transfer lemma to $r = \mathrm{red} \circ \theta$, $\Phi = \Psi^m$, $\varphi_j = F^{mj}$, $e = q^m$ and $V$. The map $r$ is injective on $\ell$-power torsion, since $\ell^n$ is a unit in $R$. This gives $U$ and properties 3, 5 and 6. Properties 1, 4 and 7 come from the theorem on Frobenius on torsion. $\square$

### Rational torsion gives semi-abelian reduction

A *principally polarized abelian variety* over $K$ is an abelian scheme $A$ over $K$ of relative dimension $g$ with a symmetric rigidified line bundle that is relatively ample with trivial group $K(\mathcal{L})$, as in the earlier sections.

**Theorem 6.18.10 (Points of group models).** Let $G$ be a group model of $A$ over $L$, and let $j : L \to \Omega$ be compatible with $K$ and $W$. Then there is an isomorphism $\theta : A(\Omega) \to G(\Omega)$ that commutes with every ring map $\tau$ of $\Omega$ with $\tau \circ j = j$. If $L \to K' \to \Omega$ and $x \in A(\Omega)$ comes from a $K'$-point, then there is a $K'$-point $y'$ of $G$ with $y'^c$ mapping to $\theta(x^c)$ for all $c$.

Lean: `GlobalTheory.T.grpScheme_points_model_over_field`.

**Theorem 6.18.11 (Torsion and the Weil pairing).** Let $A$ be principally polarized of dimension $g$ over $K$ of characteristic $0$, let $\Omega$ be an algebraic closure and $\ell$ prime. Then the $\ell^n$-torsion of $A(\Omega)$ has $\ell^{2gn}$ elements. There is a Weil pairing $e_n$ on it that is bilinear, alternating, nondegenerate and compatible in $n$, with values in the $\ell^n$-th roots of unity, and $\tau(e_n(x, y)) = e_n(\tau x, \tau y)$ for $\tau$ in the Galois group.

Lean: `GlobalTheory.T.torsion_points_polarised_abelianVariety_galois`.

**Theorem 6.18.12 (Galois action on torsion).** Let $A$, $\Omega$ and $\ell$ be as above, and assume that the Galois group fixes the $\ell$-torsion. Let $\sigma, \varphi \in \operatorname{Gal}(\Omega/K)$ and $j : K' \to \Omega$ satisfy properties 3 and 4 of the theorem below, with $q$ in place of $p^{r_0}$ and with $x$ in the image of $j$ in place of $x = a/b$. Then there are a pairing $e_n$ as above and an action $\tau \mapsto \tau_*$ of the Galois group on $A(\Omega)$, by $\tau_* x = x \circ \operatorname{Spec} \tau$, such that on $\ell$-power torsion $e_n(\sigma_* x, \sigma_* y) = e_n(x, y)$, $e_n(\varphi^N_* x, \varphi^N_* y) = e_n(x, y)^{q^N}$ and $\varphi^N_* \sigma_* = \sigma_*^{q^N} \varphi^N_*$. Each $\ell$-power torsion point fixed by $\sigma_*$ comes from a $K'$-point.

Lean: `GlobalTheory.T.galois_action_torsion_pairing_tame_fixedPoints`.

**Theorem 6.18.13 (Weights and the pairing).** Let $M$ be a commutative group whose $\ell^n$-torsion has $\ell^{2gn}$ elements, with $\ell \geq 3$ and a pairing $e$ as above. Let $S$ and $\Phi$ be automorphisms with $e(Sx, Sy) = e(x, y)$, $e(\Phi x, \Phi y) = e(x, y)^q$, $\Phi S = S^{q} \Phi$ on $\ell$-power torsion and $S x = x$ on $\ell$-torsion, with $q \geq 2$. Let $H, W \leq M$ and $P$ satisfy the counts, the root bound, the Frobenius rule and the polynomial rule of the theorem above, with $\Phi$ in place of $\Psi^m$. If $x^c \in H$ for every $\ell$-power torsion $x$ fixed by $S$, then $g \leq t + a$.

Lean: `GlobalTheory.T.weight_le_add_of_torsion_pairing`.

**Theorem 6.18.14 (Torus extension in the special fibre).** Let $W$ be a discrete valuation ring with fraction field $L$, and let $G$ be a smooth connected group over $W$ with $G_L$ proper. Let $\rho : W \to k$ be an integral map to a field with kernel the maximal ideal. If $G_k$ is a torus extension, then $G$ is semi-abelian.

Lean: `GlobalTheory.T.isSemiAbelian_of_proper_generic_torusExtension_special`.

**Theorem 6.18.15 (Rational torsion).** Let $V \to K$ with $K$ of characteristic $0$ the fraction field of $V$, let $\ell \geq 3$ be prime, let $A$ be a principally polarized abelian variety over $K$ of dimension $g$, and let $\Omega$ be an algebraic closure of $K$. Assume that every $\tau \in \operatorname{Gal}(\Omega/K)$ fixes every $x \in A(\Omega)$ with $x^\ell = 1$. Let $W$ be a discrete valuation ring with fraction field $L$, and let $R$ be a local domain with fraction field $K'$, with maps $V \to W \to R \to \Omega$, $W \to R$ local and injective, $R \to \Omega$ injective, and $K \to L$ compatible with $V$. Assume that the residue field $k$ of $R$ is algebraically closed of characteristic $p$, that $\ell$ is a unit in $R$, and that $r_0, f \geq 1$ and every $c \in k$ satisfies $c^{(p^{r_0})^m} = c$ for some $m \geq 1$. Let $\sigma, \varphi \in \operatorname{Gal}(\Omega/K)$ with these properties.

1. $\varphi^f$ fixes $W$.
2. $\varphi$ sends $R$ to $R$ and $\varphi(x) \equiv x^{p^{r_0}}$ modulo the maximal ideal.
3. $\sigma \zeta = \zeta$ and $\varphi \zeta = \zeta^{p^{r_0}}$ for every $\ell$-power root of unity $\zeta$.
4. For every finite normal extension $L'$ of $K$ in $\Omega$ whose Galois group is an $\ell$-group and every $x \in L'$, $\varphi \sigma x = \sigma^{p^{r_0}} \varphi x$, and if $\sigma x = x$, then $x = a/b$ with $a, b \in R$ and $b \neq 0$.

Let $G$ be a smooth connected group model of $A$ over $W$ with relative dimension $g$ and an ample cubical bundle on $G_k$. Let $c \geq 1$ be such that $y^c$ extends to an $R$-point for every $K'$-point $y$ of $G$. Then $G$ is semi-abelian.

Lean: `GlobalTheory.SS.isSemiAbelian_of_rational_torsion`.

*Proof.* The fraction fields give maps $j' : K' \to \Omega$ and $i : L \to K'$, and $j' \circ i$ is compatible with $W$ and with $K$. The theorem on points of group models gives $\theta : A(\Omega) \to G(\Omega)$. The theorem on torsion and the Weil pairing gives the count $\ell^{2gn}$. By property 4, $\sigma$-fixed elements of $L'$ lie in the image of $K'$, so the theorem on the Galois action gives $e$ and the action.

Let $q = p^{r_0 f}$. The map $\varphi^f$ fixes $W$, hence fixes $L$, and by induction it sends $R$ to $R$ with $\varphi^f(x) \equiv x^q$. If $c^{(p^{r_0})^m} = c$, then $f$ steps of this rule give $c^{q^m} = c$. Apply the theorem on Frobenius counts with $\psi = \varphi^f$ and $\Psi = \varphi^f_*$, which $\theta$ respects. This gives $t, a, m, C, Q, H$ and $U$.

Apply the theorem on weights with $S = \sigma_*$, $\Phi = \varphi^{fm}_*$ and the level $(p^{r_0})^{fm} \geq 2$. Let $x$ be $\ell$-power torsion with $\sigma_* x = x$. Then $x$ comes from a $K'$-point of $A$, so $\theta(x)$ comes from a $K'$-point $y'$ of $G$, and $\theta(x^c)$ comes from $y'^c$, which extends to an $R$-point. So $x^c \in H$. Hence $g \leq t + a$, and $G_k$ is a torus extension.

The fibre $G_L \cong A_L$ is proper. The map $W \to k$ has the maximal ideal as kernel, since $W \to R$ is local, and it is integral, since each $z \in k$ is a root of $X^{(p^{r_0})^m} - X$. The theorem on the special fibre shows that $G$ is semi-abelian. $\square$

**Remark 6.18.16 (Formalization).** The theorems are in [FrobeniusCountsIntegralTorsionSpecialFibre.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/FrobeniusCountsIntegralTorsionSpecialFibre.lean#L112) and [PotentialSemistableOfRationalLTorsion.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/PotentialSemistableOfRationalLTorsion.lean#L44). In the first theorem $U$ need not lie in $H$, and the counts are upper bounds only. The ring $V$ of the second theorem has no hypothesis: it only links $K$ and $L$.
