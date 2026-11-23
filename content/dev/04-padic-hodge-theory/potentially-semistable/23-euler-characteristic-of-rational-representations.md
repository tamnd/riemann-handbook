---
title: The Euler characteristic formula for rational representations
decls:
  - GlobalTheory.T.finrank_H1_dual_pair
  - GlobalTheory.EulerCharH1.finite_and_finrank_H1V
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Euler characteristic formula for rational representations

This section computes the dimension of the first continuous cohomology of a finite-dimensional representation of $G_K$ over a finite extension $L$ of $\mathbb{Q}_\ell$. Let $V$ be such a representation and let $V'$ be a representation in perfect duality with $V$ into $L(1)$. Then $H^1(G_K, V)$ is finite-dimensional and
$$\dim_L H^1(G_K, V) = \dim_L V^{G_K} + \dim_L V'^{G_K} + [K : \mathbb{Q}_\ell] \dim_L V.$$
This is Tate's Euler characteristic formula for $V$, with $H^2(G_K, V)$ replaced by its dual $H^0(G_K, V')$. We deduce it from the two theorems of Tate on finite modules: local duality and the Euler characteristic formula. The section that follows uses the finiteness of $H^1$ in the proof of Hyodo's theorem.

We keep the notation of section 15: $\ell$ is a prime, $K$ is a finite extension of $\mathbb{Q}_\ell$ inside the fixed algebraic closure, $G_K$ is its absolute Galois group with the profinite topology, and $\chi$ is the cyclotomic character of the period data. For the background on continuous cohomology see [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology), [[Galois cohomology|9MPCZ3EAJM]] and [local fields](/learn/galois-cohomology/#local-fields).

**Definition 6.23.1 (Coefficients and representations).** A *coefficient pair* $(L, \mathcal{O})$ is a field $L$ that is a finite extension of $\mathbb{Q}_\ell$, with the topology of a finite-dimensional $\mathbb{Q}_\ell$-vector space, together with a discrete valuation ring $\mathcal{O}$ with fraction field $L$ whose image is open in $L$. A *rational representation* of $G_K$ over $L$ is a finite-dimensional $L$-vector space $V$, with its natural topology, and a homomorphism $\rho : G_K \to \mathrm{GL}_L(V)$ such that $g \mapsto \rho(g)x$ is continuous for each $x \in V$.

Lean: `Formalism.MainNotions.N.GoodO` (also `Formalism.MainNotions.N.GRep`, the representations).

For a rational representation $V$, let $H^0(V) = V^{G_K}$ be the subspace of invariants. Let $Z^1(V)$ be the $L$-space of continuous maps $c : G_K \to V$ with $c(gh) = c(g) + \rho(g) c(h)$, and $B^1(V)$ the subspace of maps $g \mapsto \rho(g)x - x$ with $x \in V$. Put $H^1(V) = Z^1(V) / B^1(V)$.

**Definition 6.23.2 (Duality into the Tate twist).** Let $V$ and $V'$ be rational representations over $L$ and $P : V \times V' \to L$ an $L$-bilinear map. We say that $P$ is a *perfect duality into $L(1)$* if
1. $P(\rho(g)x, \rho'(g)y) = \chi(g) P(x, y)$ for all $g \in G_K$, $x \in V$, $y \in V'$;
2. $P(x, y) = 0$ for all $y$ implies $x = 0$, and $P(x, y) = 0$ for all $x$ implies $y = 0$;
3. $\dim_L V = \dim_L V'$.

Lean: `Formalism.MainNotions.N.IsDual1`.

Conditions 2 and 3 say that $P$ identifies $V'$ with the dual of $V$; condition 1 says that this identification is $V' \cong \mathrm{Hom}_L(V, L(1))$ as representations.

**Definition 6.23.3 (Lattices).** Let $V$ be a rational representation. A *lattice* in $V$ is a finitely generated free $\mathcal{O}$-submodule $T \subseteq V$ that spans $V$ over $L$ and is stable under $G_K$. Its cohomology $H^1(T)$ is the $\mathcal{O}$-module of continuous cocycles $c : G_K \to V$ with values in $T$, modulo the maps $g \mapsto \rho(g) x - x$ with $x \in T$. For $r \geq 0$ the quotient $T / \ell^r T$ is a finite discrete $G_K$-module, and $H^1(T / \ell^r T)$ is the group of locally constant cocycles $G_K \to T / \ell^r T$ modulo coboundaries. Two lattices $T \subseteq V$ and $T' \subseteq V'$ are *dual* under $P$ if $P$ is a perfect duality into $L(1)$ and $T' = \{ y \in V' : P(x, y) \in \mathcal{O} \text{ for all } x \in T \}$.

Lean: `Formalism.WeaklyAdmissibleFiltrations.Lattice` (also `Formalism.WeaklyAdmissibleFiltrations.LatticeCohomology`, `Formalism.WeaklyAdmissibleFiltrations.QuotientCohomology` and `Formalism.MainNotions.N.IsDualLat1`).

### Tate's theorems on finite modules

For $r > 0$ let $\mu_{\ell^r}$ be $\mathbb{Z}/\ell^r$ with $G_K$ acting through the cyclotomic character modulo $\ell^r$. For a finite $\mathbb{Z}/\ell^r$-module $M$ with a continuous action of $G_K$ (for the discrete topology on $M$), let $M^\vee(1) = \mathrm{Hom}(M, \mu_{\ell^r})$ and let $H^i(M)$ be the continuous cohomology.

**Theorem 6.23.4 (Tate local duality).** Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r > 0$, and $M$ a finite $\mathbb{Z}/\ell^r$-module with a continuous action of $G_K$. Then $H^2(\mu_{\ell^r}) \cong \mathbb{Z}/\ell^r$, and the cup products
$$H^i(M) \times H^{2-i}(M^\vee(1)) \to H^2(\mu_{\ell^r}) \cong \mathbb{Z}/\ell^r, \qquad i = 0, 1, 2,$$
are perfect pairings.

Lean: `Formalism.GaloisCohomology.LocalTateDualityK`.

**Theorem 6.23.5 (Tate local Euler characteristic).** Under the same assumptions,
$$\# H^1(M) = \# H^0(M) \cdot \# H^2(M) \cdot (\# M)^{[K : \mathbb{Q}_\ell]}.$$

Lean: `Formalism.GaloisCohomology.LocalEulerCharK`.

These are J. Tate's theorems; see J.-P. Serre, *Galois Cohomology*, Chapter II, §5.2, Theorem 2, and §5.7, Theorem 5. We take both as given.

### The dimension of $H^1$

**Theorem 6.23.6 (Euler characteristic of a rational representation).** Assume Tate local duality and the Tate local Euler characteristic formula. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $(L, \mathcal{O})$ a coefficient pair, $V$ and $V'$ rational representations of $G_K$ over $L$, and $P : V \times V' \to L$ a perfect duality into $L(1)$. Then $H^1(V)$ is finite-dimensional over $L$ and
$$\dim_L H^1(V) = \dim_L H^0(V) + \dim_L H^0(V') + [K : \mathbb{Q}_\ell] \dim_L V.$$

Lean: `GlobalTheory.EulerCharH1.finite_and_finrank_H1V` (also `GlobalTheory.T.finrank_H1_dual_pair`, a second name).

The proof counts points modulo $\ell^r$. Let $q = \# \mathcal{O} / \ell \mathcal{O}$. A finitely generated $\mathcal{O}$-module of rank $a$ has about $q^{ra}$ elements modulo $\ell^r$. So it suffices to show that, as functions of $r$, the four numbers $\# H^1(T)/\ell^r$, $\# H^1(T/\ell^r T)$, $\# H^0(T/\ell^r T) \cdot \# H^0(T'/\ell^r T') \cdot q^{rd}$ and $q^{r(h^0 + h'^0 + d)}$ agree up to bounded factors. We use the following results, proved elsewhere in this development, for a lattice $T$ in a rational representation $V$.

1. (Dual lattices.) Under the hypotheses of the Theorem there are lattices $T \subseteq V$ and $T' \subseteq V'$ that are dual under $P$, and $T$ is dual to $T'$ under the flipped pairing.
2. (Finiteness.) Assuming Tate local duality, $H^1(T)$ is a finitely generated $\mathcal{O}$-module.
3. (Rank.) If $H^1(T)$ is finitely generated, then $H^1(V)$ is finite-dimensional, and there is $C_1 > 0$ with $q^{r h^1} \leq \# H^1(T)/\ell^r H^1(T) \leq C_1 q^{r h^1}$ for all $r$, where $h^1 = \dim_L H^1(V)$.
4. (Reduction.) Assuming Tate local duality, for dual lattices there is $C_2 > 0$ with $\# H^1(T)/\ell^r H^1(T) \leq \# H^1(T / \ell^r T) \leq C_2 \cdot \# H^1(T)/\ell^r H^1(T)$ for all $r$.
5. (Finite level.) Assuming both theorems of Tate, for dual lattices and all $r$,
$$\# H^1(T / \ell^r T) = \# H^0(T / \ell^r T) \cdot \# H^0(T' / \ell^r T') \cdot q^{r d}, \qquad d = [K : \mathbb{Q}_\ell] \dim_L V.$$
6. (Invariants.) There is $C > 0$ with $q^{r h^0} \leq \# H^0(T / \ell^r T) \leq C q^{r h^0}$ for all $r$, where $h^0 = \dim_L H^0(V)$.

Result 5 is the Euler characteristic formula for $M = T/\ell^r T$, with $\# H^2(M) = \# H^0(M^\vee(1))$ by duality and $M^\vee(1) \cong T'/\ell^r T'$ because the lattices are dual; here $\# M = q^{r \dim V}$ and $(\# M)^{[K:\mathbb{Q}_\ell]} = q^{rd}$.

**Lemma 6.23.7 (Comparing exponents).** Let $q \geq 2$ and $a, b, C$ be natural numbers with $q^{ra} \leq C q^{rb}$ for all $r$. Then $a \leq b$.

Lean: `GlobalTheory.EulerCharH1.le_of_pow_le` (also `GlobalTheory.EulerCharH1.eq_of_bounds`, the comparison of the four counts).

*Proof.* If $a > b$, then $q^{rb} q^r \leq q^{ra} \leq C q^{rb}$, so $q^r \leq C$ for all $r$. At $r = C$ this gives $2^C \leq q^C \leq C$, which is false. $\square$

*Proof of the Theorem.* Take dual lattices $T \subseteq V$ and $T' \subseteq V'$ by result 1. By result 2, $H^1(T)$ is finitely generated, so result 3 shows that $H^1(V)$ is finite-dimensional and gives $C_1$. The submodules $\ell^r T$ and $\ell^r T'$ are stable under $G_K$, since the action is $\mathcal{O}$-linear, so the finite modules $T / \ell^r T$ and $T' / \ell^r T'$ are defined. Let $h^1 = \dim H^1(V)$, $h^0 = \dim H^0(V)$, $h'^0 = \dim H^0(V')$ and $d = [K : \mathbb{Q}_\ell] \dim V$. Write $X_r = \# H^1(T)/\ell^r$, $Y_r = \# H^1(T/\ell^r T)$, $H_r = \# H^0(T/\ell^r T)$ and $H'_r = \# H^0(T'/\ell^r T')$. Results 3 to 6 give, for all $r$,
$$\begin{aligned} q^{r h^1} &\leq X_r \leq Y_r = H_r H'_r q^{rd} \leq C C' q^{r(h^0 + h'^0 + d)}, \\ q^{r(h^0 + h'^0 + d)} &\leq H_r H'_r q^{rd} = Y_r \leq C_2 X_r \leq C_2 C_1 q^{r h^1}, \end{aligned}$$
where $C$ and $C'$ are the constants of result 6 for $T$ and $T'$.

The residue field $\mathcal{O}/\ell\mathcal{O}$ is finite and nonzero: $\ell$ is not a unit in $\mathcal{O}$, because $1/\ell$ is not integral over $\mathbb{Z}_\ell$ and $\mathcal{O}$ is integral over $\mathbb{Z}_\ell$. So $q \geq 2$. The Lemma, applied to both rows, gives $h^1 \leq h^0 + h'^0 + d$ and $h^0 + h'^0 + d \leq h^1$. $\square$

In the classical form, $V'$ is the Tate dual $V^*(1)$ and $\dim H^0(V')$ is $\dim H^2(V)$ by duality, so the Theorem reads $\dim H^1(V) = \dim H^0(V) + \dim H^2(V) + [K : \mathbb{Q}_\ell] \dim V$. The next section applies it to a representation of $G_K$ on $\mathbb{Q}_\ell^d$ and its Tate dual, to know that the space of continuous cocycles is finite-dimensional.

**Remark 6.23.8 (Formalization).** The two theorems of Tate enter as hypotheses of the statement ([FinrankH1DualPairStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FinrankH1DualPairStatement.lean#L9)); in this chapter they are used only to get finiteness for Hyodo's theorem. The ring $\mathcal{O}$ is not required to be the ring of integers of $L$, only a discrete valuation ring with fraction field $L$ and open image; the integrality of $\mathcal{O}$ over $\mathbb{Z}_\ell$ and the finiteness of $\mathcal{O}/\ell^r$ come from a lemma proved elsewhere. Results 1 to 6 are `GlobalTheory.T.exists_mutuallyDual_stable_lattices`, `GlobalTheory.T.finite_H1_period_datum`, `GlobalTheory.T.H1_lattice_rank_growth_of_goodO`, `GlobalTheory.T.H1_reduction_index_bound_of_tateDuality`, `GlobalTheory.T.H1_lattice_index_growth_of_tateDuality_eulerChar` and `GlobalTheory.T.growth_galois_invariants_mod_prime_power_lattice`; we read their statements, not their proofs. Tate duality is stated as the bijectivity of the maps from $H^i(M)$ to the dual of $H^{2-i}(M^\vee(1))$, for $i = 0$ and $i = 2$, and for both sides of $H^1 \times H^1$. The cohomology of $T / \ell^r T$ uses locally constant cochains, while $H^1(V)$ and $H^1(T)$ use continuous ones.
