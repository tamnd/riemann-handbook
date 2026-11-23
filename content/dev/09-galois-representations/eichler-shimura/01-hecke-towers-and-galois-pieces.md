---
title: Hecke towers and their Galois pieces
decls:
  - UpperTheory.Gal.Int.Geo.repEx_holds
  - UpperTheory.Gal.Int.Geo.repEx_core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke towers and their Galois pieces

The Galois representations of this chapter live in the $\ell$-adic cohomology of a smooth projective variety $Z$ that carries Hecke correspondences. We cut the cohomology by a system of Hecke eigenvalues, write the Galois action on the cut piece as a matrix, and take a semisimple graded part. This section sets up these objects and proves that such a representation always exists. The later sections prove its local properties.

**Definition 3.1.1 (Hecke tower).** Let $k$ be a field. A *Hecke tower* $H$ over $k$ consists of an index set $\Gamma$, a $k$-scheme $q : Z \to \operatorname{Spec} k$, and for each $g \in \Gamma$ a scheme $Y_g$ with two maps $s_g, t_g : Y_g \to Z$ such that $q \circ s_g = q \circ t_g$. For a field extension $K/k$, the *base change* $H_K$ has the same index set, the scheme $Z_K = Z \times_k K$ and the maps $s_g, t_g$ base changed to $K$. For a field map $\tau : k \to K$ we write $H_\tau$ for the base change along $\tau$.

Lean: `GlobalTheory.GalV.HTower` (also `UpperTheory.Gal.Int.Geo.bc`, `UpperTheory.Gal.Int.Geo.bcAlong`).

So each pair $(s_g, t_g)$ is a correspondence from $Z$ to itself in the sense of [Volume 1](/learn/geometry/#tale-cohomology).

**Definition 3.1.2 (finite étale of degree $d$; nice tower).** A map $f : Y \to X$ of schemes is *finite étale of degree $d$* if it is [[finite|N9C4X7XKE4]] and étale, and each point $\operatorname{Spec} K \to X$ with $K$ an algebraically closed field has exactly $d$ lifts to $Y$. A Hecke tower $H$ is *nice* if $q$ is smooth and projective and each $s_g$ is finite étale of some degree.

Lean: `UpperTheory.Gal.Int.Geo.FEt`, `UpperTheory.Gal.Int.Geo.Nice`.

Fix a prime $\ell$ and an algebraically closed field $\Omega$ over $k$. Write $Z_\Omega$ for the geometric fibre and
$$H^*(Z_\Omega) = \bigoplus_n H^n(Z_\Omega, \mathbb{Q}_\ell)$$
for its total [[étale cohomology|7YX76G0838]]. The group $\operatorname{Gal}(\Omega/k)$ acts on $H^*(Z_\Omega)$ by transport of structure.

**Definition 3.1.3 (correspondence operator).** Let $s : Y \to Z$ and $t : Y \to Z$ be maps of $\Omega$-schemes. A linear map $T$ on $H^*(Z_\Omega)$ is a *correspondence operator* for $(s, t)$ if there are a finite étale Galois cover $c : W \to Z$ with a finite group $G$, and maps $\sigma_j : W \to Y$ ($j$ in a finite set $J$) with $s \circ \sigma_j = c$ that split the pullback, $\coprod_{j \in J} W \cong W \times_Z Y$, such that
$$c^*(T x) = \sum_{j \in J} (t \circ \sigma_j)^* x \quad \text{for all } x.$$
For a Hecke tower, the *Hecke operator* $T_g$ is a correspondence operator for $(s_g, t_g)$ over $\Omega$ when one exists, and $0$ otherwise.

Lean: `GlobalTheory.GalV.IsCorrOp` (also `GlobalTheory.GalV.hop`).

When $s$ is finite étale, the operator $s_* t^*$ of [Volume 1](/learn/geometry/#tale-cohomology) is a correspondence operator: over a Galois cover that splits $s$, the trace $s_*$ becomes a sum over the sheets. Since $c^*$ is injective on rational cohomology for a finite étale surjective $c$, the formula determines $T$.

**Definition 3.1.4 (Hecke eigen-piece).** Let $L$ be a field over $\mathbb{Q}_\ell$ and $\theta : \Gamma \to L$ a function. The *$\theta$-piece* of $H$ is the subspace
$$\Pi_\theta = \bigcap_{g \in \Gamma} \ker\bigl(T_g \otimes 1 - \theta(g)\bigr) \subseteq L \otimes_{\mathbb{Q}_\ell} H^*(Z_\Omega).$$

Lean: `UpperTheory.Gal.Int.Geo.piece`.

**Definition 3.1.5 (matrix form, graded part, Galois piece).** Let $\rho_0 : \operatorname{Gal}(\Omega/k) \to \mathrm{GL}_d(L)$ be a homomorphism. It is a *matrix form* of $\Pi_\theta$ if some basis $b_1, \dots, b_d$ of $\Pi_\theta$ satisfies $\sigma(b_j) = \sum_i \rho_0(\sigma)_{ij}\, b_i$ for all $\sigma$ and $j$. A homomorphism $\rho$ of the same size is a *graded part* of $\rho_0$ if there is a function $c : \{1, \dots, d\} \to \mathbb{N}$ such that each $\rho_0(\sigma)$ is block upper triangular for the blocks $c^{-1}(m)$, and $\rho(\sigma)$ is the block diagonal part of $\rho_0(\sigma)$. Finally, $\rho$ is a *Galois piece* of $(H, \theta)$ if it is a graded part of some matrix form of $\Pi_\theta$.

Lean: `UpperTheory.Gal.Int.Geo.IsMat`, `UpperTheory.Gal.Int.Geo.IsGr`, `UpperTheory.Gal.Int.Geo.IsPiece`.

A graded part of $\rho_0$ is the direct sum of the subquotients of a $\rho_0$-stable flag. If the flag is a composition series, the graded part is the semisimplification of $\rho_0$. Every matrix form is a graded part of itself (take $c$ constant).

**Theorem 3.1.6 (Galois pieces exist).** Let $E$ be a [[number field|WXGM3VWEK6]], $\Omega$ an algebraic closure of $E$ and $\ell$ a prime. Let $H$ be a nice Hecke tower over $E$ and $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$ a function. Then there are $d \geq 0$ and a continuous semisimple homomorphism $\rho : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ that is a Galois piece of $(H, \theta)$.

Lean: `UpperTheory.Gal.Int.Geo.repEx_holds` (also `UpperTheory.Gal.Int.Geo.repEx_core`, the same statement under five inputs from étale cohomology).

*Proof.* The proof has four steps.

First, $H^*(Z_\Omega)$ is finite-dimensional. For $Z$ smooth and projective over an algebraically closed field, each $H^n(Z_\Omega, \mathbb{Q}_\ell)$ is finite-dimensional and vanishes for $n$ outside a bounded range. The proof uses Poincaré duality, the projective bundle formula and proper base change. These come from five inputs: the [vanishing of $H^n$ for $n \geq 2$ on smooth affine curves](/entry/et-c-c2/) over an algebraically closed field, a base change theorem for étale algebras over polynomial rings, [homotopy invariance](/entry/homotopy-invariance-etale/), the [vanishing for Laurent polynomial rings over strictly henselian rings](/entry/laurent-polynomial-cohomology-strictly-henselian-vanishing/), and the [projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/). So $\Pi_\theta$ is a finite-dimensional $\overline{\mathbb{Q}}_\ell$-space. Let $d$ be its dimension.

Second, $\Pi_\theta$ is stable under $\operatorname{Gal}(\Omega/E)$. The correspondence operator of $(s_g, t_g)$ is unique when it exists, by the injectivity of $c^*$. For $\sigma \in \operatorname{Gal}(\Omega/E)$ the conjugate $\sigma T_g \sigma^{-1}$ is again a correspondence operator for $(s_g, t_g)$, because $s_g$ and $t_g$ are defined over $E$. So $\sigma$ commutes with $T_g$ and preserves each eigenspace.

Third, choose a basis of $\Pi_\theta$. The Galois action in this basis is a matrix form $\rho_0$. It is continuous: the matrix coefficients of the Galois action on each $H^n(Z_\Omega, \mathbb{Q}_\ell)$ are continuous, because the action on each finite level $H^n(Z_\Omega, \mathbb{Z}/\ell^m)$ factors through a finite quotient, and continuity passes to the finite sum and to the extension of scalars.

Fourth, take a composition series of $\rho_0$ and a basis adapted to it. In this basis the new matrix form $P \rho_0 P^{-1}$ is block upper triangular, and its block diagonal part $\rho$ is semisimple. A change of basis of $\Pi_\theta$ gives a new matrix form, so $\rho$ is a graded part of a matrix form. The block diagonal part of a continuous representation is continuous. $\square$

**Remark 3.1.7.** For a nice tower over a field of characteristic $0$, a correspondence operator always exists; this is proved in [the crystalline step](/entry/crys-step-of/). The theorem above holds for every $\theta$. When $\Pi_\theta = 0$ it gives $d = 0$, so the content is in the later local statements. Since a matrix form is indexed by a basis of $\Pi_\theta$, the integer $d$ is always $\dim \Pi_\theta$.

**Remark 3.1.8 (Formalization).** The Hecke operator is chosen classically, with value $0$ when no correspondence operator exists ([IdTower.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IdTower.lean#L28)). `UpperTheory.Gal.Int.Geo.repEx_core` takes as hypothesis a record `UpperTheory.Gal.KunnethLefschetz.Core` with five fields `c2`, `c3`, `c4`, `c5`, `d1`, the five inputs named in the proof, and `UpperTheory.Gal.Int.Geo.repEx_holds` supplies it by `UpperTheory.Gal.KunnethLefschetz.core_holds`. The descriptions of the second, third and fourth inputs follow their names (`etale_cohomology_ind_etale_base_change`, `homotopy_invariance_etale`, `laurentPolynomial_cohomology_strictlyHenselian_vanishing`). The inputs are used only through the finiteness of $H^*(Z_\Omega)$.
