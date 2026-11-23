---
title: The Galois row from geometry
decls:
  - UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one
  - UpperTheory.Gal.Int.Geo.geoOne_holds
  - UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift
  - UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Galois row from geometry

This section puts the local steps together. A space of automorphic forms on a unitary group gives a Hecke tower of Kuga-Sato varieties over Shimura varieties, and the Galois piece of that tower, twisted by a character, is the wanted Galois representation. This gives the Galois row in weight one. Then a theta lift moves a general cuspidal representation to a unitary group where this case applies, and we get the Galois row that the main proof needs.

Throughout, $E$ is a CM field, $\Omega$ an algebraic closure, $\ell$ a prime and $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. For a finite place $w$ and a multiset $B$ of Satake parameters, put $\operatorname{sat}_a(B) = \{ N(w)^{(a-1)/2} \beta : \beta \in B \}$.

**Definition 3.7.1 (Galois row in weight one).** Let $a$ be odd. Let $d > 0$ be an integer and $x \in E$ with $x^2 = -d$, such that $-d$ is a square in $\mathbb{Q}_\ell$, the degree $[E^+ : \mathbb{Q}]$ of the maximal totally real subfield is even, and every place of $E$ that is not split over $E^+$ is prime to $\ell$ and unramified over $E^+$. Call a split place $w$ *usable* if $-d$ is a square in $\mathbb{Q}_q$ for the prime $q$ below $w$. Let $T$ be a finite set of non-split places, and let $w_0, v'$ be places above $\ell$ that lie over different places of $E^+$ and over the same place of $\mathbb{Q}(x)$. Let $S$ be a finite set of places, and let $U$ be a space of automorphic forms on the unitary group $\mathrm{U}(a)(\mathbb{A}_E)$ such that:

- $U$ is automorphic and unramified at the non-split places outside $T$;
- $U$ has the type of [the step that defines it](/step/geo-one-def/) at $w_0$;
- $U$ has Satake parameters at every split place that lies over a place of $E^+$ different from those under $w_0$ and under the places of $S$;
- $U$ has Satake parameters at $v'$ and a lacunary weight at some embedding above $v'$, that is, a weight whose jumps have pairwise different averages over disjoint nonempty subsets.

A continuous semisimple $\rho : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_{n}(\overline{\mathbb{Q}}_\ell)$, for some $n$, is *attached to* $U$ if:

- there is a finite set $X$ such that at every usable place $w \notin X$ with $w \nmid \ell$, for all Satake parameters $B$ of $U$ at $w$, the Eichler-Shimura relation holds at $w$ with the roots $\operatorname{sat}_a(B)$;
- at some place $w \mid \ell$ and some embedding $\tau$, the Hodge-Tate jumps of $\rho$ contain a lacunary set of $a$ integers.

The *Galois row in weight one* says that for all such data:

1. some $\rho$ is attached to $U$;
2. for each usable place $w \nmid \ell$ where $U$ has Satake parameters, some $\rho$ attached to $U$ satisfies the Eichler-Shimura relation at $w$ itself with the roots $\operatorname{sat}_a(B)$, for all Satake parameters $B$ of $U$ at $w$;
3. for each place $w \mid \ell$ over the same place of $\mathbb{Q}(x)$ as $v'$, over a place of $E^+$ different from those under $w_0$ and $v'$, and where $U$ has Satake parameters:
   - some $\rho$ attached to $U$ is crystalline at $w$, and for each embedding $\tau$ inducing $w$ and each weight $\lambda$ of $U$ at $\iota \circ \tau$, the multiset $\{ \tfrac{a-1}{2} - z \}$, for $z$ in the infinitesimal character of $\lambda$, is contained in the Hodge-Tate jumps of $\rho$ at $\tau$;
   - some $\rho'$ attached to $U$ is crystalline at $w$, and for each Satake parameter $B$ of $U$ at $w$ there are an element $g$ of degree $-1$ of the Weil group and $m \geq 0$ such that the characteristic polynomial of $g$ on the Weil-Deligne representation of $\rho'$ at $w$ divides the $m$-th power of the characteristic polynomial of $g$ on the unramified representation with parameters $\operatorname{sat}_a(B)$.

Lean: `UpperTheory.Gal.Int.Geo.GeoOne`.

This is the Galois representation attached to a cohomological automorphic representation of a unitary group, with local-global compatibility at good places (M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, 2001; G. Chenevier and M. Harris, Construction of automorphic Galois representations II, Cambridge J. Math. 1 (2013)).

The proof uses three inputs that are proved elsewhere. The first is the holomorphic Lefschetz formula.

**Theorem 3.7.2 (holomorphic Lefschetz formula; Atiyah-Bott).** Let $Z$ be a smooth projective variety of dimension $d$ over $\mathbb{C}$, let $Y$ be a scheme over $\mathbb{C}$, and let $c_1, c_2 : Y \to Z$ be finite étale morphisms over $\mathbb{C}$. Suppose that the set $F$ of complex points $y$ of $Y$ with $c_1(y) = c_2(y)$ is finite and that at each $y \in F$ the tangent map is a matrix $A_y$ with $\det(1 - A_y) \neq 0$. Then each $H^b(Z, \Omega^a)$ is finite-dimensional, and
$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}$$
(M. F. Atiyah and R. Bott, A Lefschetz fixed point formula for elliptic complexes II, Ann. of Math. 88 (1968)).

Lean: `LocalSmoothExtension.HolomorphicLefschetzFormula`.

It is proved as [Theorem 5.7.3 of Volume 3](/entry/t-lefschetz-fixed-point-finite-etale-correspondence/).

This is the holomorphic form of the [[Lefschetz fixed-point theorem|G44NQXCWT9]]. The second input is a list of six facts about the tower of Kuga-Sato varieties, the fibre powers of the universal abelian scheme over the unitary Shimura varieties, proved in [Theorem 3.12.7](/entry/kodaira-spencer-of-weight-one/). Five of them are unconditional. The sixth says that each Hecke eigensystem of the given weight occurs in the Hodge cohomology of the tower in the expected degrees, and it is proved from the Lefschetz formula by [Theorem 3.12.6](/entry/ks-hodge-of-geo/). The third input is the existence of plans, [Theorem 3.16.6](/entry/plan-ex-holds/): for each $U$ as above there is a group datum, a level, a Hecke eigensystem, an algebraic Hecke character $\kappa$ with infinity type $m$, and a test function, with the right behaviour at $v'$ and at the place in question.

**Theorem 3.7.3 (the Galois row in weight one, given the Lefschetz formula).** If the holomorphic Lefschetz formula holds, then the Galois row in weight one holds.

Lean: `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one`.

*Proof.* By [the previous section](/entry/steps-holds/), the seventeen local steps hold. Let $U$ be as in the definition.

First, make packs. By the existence of plans and the six facts on the Kuga-Sato tower, each plan gives a *pack*: a nice Hecke tower $H$ over $E$ with an eigensystem $\theta$, an algebraic Hecke character $\kappa$ with infinity type $m$, and the property that, at almost all usable places $w \nmid \ell$ with Satake parameters $B$, the pair $(H, \theta)$ has a good model with a congruence relation whose Hecke polynomial has the roots $\operatorname{sat}_a(B)$ divided by $\kappa(w)$. A pack is *Hodge-Tate at* $v \mid \ell$ if $\kappa$ is unramified at $v$, $(H, \theta)$ has a good model at $v$, and the weights $j$ of $U$ at each embedding $\tau$ above $v$ give Hodge jumps $j + m(\tau)$ of $(H, \theta)$ at $\tau$, up to an automorphism of $\mathbb{C}$. The six facts on the tower give these Hodge jumps.

Second, from a pack $P$ that is Hodge-Tate at $v'$, build a representation. Let $\rho$ be a Galois piece of $(H, \theta)$, which exists by item 1 of the local steps. Let $L_\kappa$ be the Galois character of $\kappa$ (item 15), and put $\rho' = \rho \otimes L_\kappa$. Then:

- at usable places $w \nmid \ell$, the Eichler-Shimura step and the twist lemma give the relation for $\rho'$ with the roots $\operatorname{sat}_a(B)$, since the twist multiplies the roots by $\kappa(w)$;
- at places $w \mid \ell$ where the pack is Hodge-Tate, the crystalline step and the jump step give that $\rho$ is crystalline with the Hodge jumps among its Hodge-Tate jumps; the twist keeps crystallinity and shifts the jumps by $-m$, which gives the weights of $U$;
- at places $w \mid \ell$ with a congruence model, the Frobenius step and the twist lemma give the divisibility for $\rho'$.

Continuity and semisimplicity pass to $\rho'$ (items 16 and 17). The jumps at $v'$ and the lacunary weight of $U$ there give a lacunary set of $a$ Hodge-Tate jumps at $v'$ (item 14). So $\rho'$ is attached to $U$.

Third, prove the three clauses. Clause 1 uses the pack that is Hodge-Tate at $v'$. Clause 2 uses a pack that is Hodge-Tate at $v'$ and has a congruence model at $w$. Clause 3 uses one pack that is Hodge-Tate at $v'$ and at $w$ for the crystalline statement, and a second pack that is Hodge-Tate at $v'$ and has a congruence model at $w$ for the Frobenius statement. $\square$

**Corollary 3.7.4 (Galois row in weight one).** The Galois row in weight one holds.

Lean: `UpperTheory.Gal.Int.Geo.geoOne_holds`.

*Proof.* Apply the last theorem with the [holomorphic Lefschetz formula](/entry/t-lefschetz-fixed-point-finite-etale-correspondence/). $\square$

Now we reach the statement that the main proof uses. A cuspidal automorphic representation $\pi$ of $\mathrm{GL}_a(\mathbb{A}_E)$ is *regular algebraic* if its infinitesimal character is regular and integral, and *polarized* by a Hecke character $\chi$ of $E^+$ if $\pi^\vee \cong \pi^c \otimes (\chi \circ \mathrm{N}_{E/E^+})$. The local condition uses Weil-Deligne representations. For a place $w$, a *reciprocity map* is a map $\mathrm{rc}$ from irreducible representations of $\mathrm{GL}_a(E_w)$ to Weil-Deligne representations of $E_w$ that satisfies the laws of [the local reciprocity step](/step/is-rect-def/). For a local component $\sigma$ of $\pi$ at $w$, put $y_\sigma = \mathrm{rc}(\sigma \otimes |\det|^{(1-a)/2})$. A Weil-Deligne representation $y$ is

- *toral* if every commutator of the Weil group acts unipotently on $y$;
- *tame* if every element of wild inertia acts unipotently on $y$;
- *square-free* if, for each $\gamma$ in inertia that topologically generates inertia together with wild inertia, every root $z$ of multiplicity at least $2$ of the characteristic polynomial of $\gamma$ on $y$ satisfies $z^{N(w)-1} = 1$.

Say $w$ is *big for* $n$ if $E_w \cong \mathbb{Q}_g$ for a prime $g$ with $n = 1$ or $16 n^2 < g$. Two Weil-Deligne representations $x, y$ at $w$ *match* if they have the same dimension, $x = y$ when $y$ is toral with zero monodromy, and, when $w$ is big for $\dim y$ and $y$ is tame and square-free with zero monodromy, $x$ has zero monodromy and the same characteristic polynomial as $y$ on every element of degree $0$ of the Weil group.

**Theorem 3.7.5 (Galois representations of regular algebraic polarized representations).** Let $a \geq 1$ and let $\pi$ be a regular algebraic cuspidal representation of $\mathrm{GL}_a(\mathbb{A}_E)$, polarized by a Hecke character $\chi$ of $E^+$. Then there are a [[Galois representation|QW17YJ6ZCT]] $\rho_\pi : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$, an integer $\mathrm{wt}$ and, for each embedding $\tau : E \to \overline{\mathbb{Q}}_\ell$, a multiset $\mathrm{HT}(\tau)$ of integers, such that:

1. $\rho_\pi$ is continuous and semisimple;
2. $\mathrm{HT}(\tau) = \{ \tfrac{a-1}{2} - z \}$ for $z$ in the infinitesimal character of $\pi$ at $\iota \circ \tau$, and $\mathrm{HT}(\tau \circ c) = \{ \mathrm{wt} - j : j \in \mathrm{HT}(\tau) \}$;
3. at each place $w \nmid \ell$, for each reciprocity map and each local component $\sigma$ of $\pi$ at $w$, the Weil-Deligne representation of $\rho_\pi$ at $w$ matches $y_\sigma$;
4. at each place $w \mid \ell$ and each local component $\sigma$ of $\pi$ at $w$:
   - if $\sigma$ is spherical, then $\rho_\pi$ is crystalline and de Rham at $w$, with Hodge-Tate jumps $\mathrm{HT}(\tau)$ at each $\tau$ inducing $w$;
   - for each reciprocity map, if $y_\sigma$ has zero monodromy and is either toral, or tame and square-free with $w$ big for $a$, then $\rho_\pi$ is de Rham and [[potentially semistable|6YDZNXR19H]] at $w$, with Hodge-Tate jumps $\mathrm{HT}(\tau)$ at each $\tau$ inducing $w$, and its Weil-Deligne representation at $w$ matches $y_\sigma$.

This is a weak form of the standard theorem, which says that the Frobenius semisimplification of the Weil-Deligne representation of $\rho_\pi$ at every place $w$ corresponds to $\pi_w$ under the local Langlands correspondence, and that $\rho_\pi$ is potentially semistable at every $w \mid \ell$ (M. Harris and R. Taylor, 2001; S. W. Shin, Galois representations arising from some compact Shimura varieties, Ann. of Math. 173 (2011); G. Chenevier and M. Harris, 2013; A. Caraiani, Local-global compatibility and the action of monodromy on nearby cycles, Duke Math. J. 161 (2012); T. Barnet-Lamb, T. Gee, D. Geraghty and R. Taylor, Local-global compatibility for $l = p$, II, Ann. Sci. ÉNS 47 (2014)). The statement as it is used is [the Galois row hypothesis](/step/row0b-def/).

Lean: `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` (also `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift`, the same statement with the theta lift as a hypothesis).

The theta lift hypothesis is the following statement about the [[theta correspondence|6WB6TKE70H]] for a unitary dual pair, proved in [Theorem 6.6.6 of Volume 12](/entry/t-lift-k/). For a hermitian space $X$ of dimension $n$ and skew-hermitian spaces $W$ of dimension $d$, and suitable Hecke characters $\chi_X, \chi_W$, every automorphic representation of the [[unitary group|0R9R0Y1HDK]] $\mathrm{U}(X)$ with weights large compared with $d$ has a nonzero theta lift to $\mathrm{U}(W)$ for all $d$ beyond some $d_0$.

*Proof.* By [the theorem that builds the row from geometry and a lift](/entry/galois-local-global-strong-of-geometry-lift/), the Galois row in weight one and the theta lift statement together give the theorem. Apply it with the corollary above and the [theta lift theorem](/entry/t-lift-k/). This is the [written step](/step/galois-representations-of-theta-lift/). $\square$

**Remark 3.7.6.** In clause 3 of the Galois row in weight one, the crystalline statement and the Frobenius statement come from two different packs, so they may concern two different representations $\rho$ and $\rho'$. Both are attached to $U$, but the definition does not say that they are isomorphic. The dimension $n$ of an attached representation is also not fixed to be $a$. Theorem 3.7.5 asks less than the standard theorem: away from $\ell$ it gives full agreement with $y_\sigma$ only in the toral case, and above $\ell$ it gives potential semistability only in the special cases listed.

**Remark 3.7.7 (Formalization).** The names of two theorems are swapped: `UpperTheory.Gal.Int.Geo.weight_one_geometric_realization` is the holomorphic Lefschetz formula, and `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one` builds the Galois row from it, as `geoOne_of_parts steps_holds (kodaira_spencer_of_weight_one hW) Pl.planEx_holds`. The name `kodaira_spencer_of_weight_one` refers to Kuga-Sato varieties, not to a Kodaira-Spencer map. The packs are the statement `PackEx`, and the three clauses are proved in `UpperTheory.Gal.Int.Geo.geoOne_of`. The twist uses the Galois character `L κ m` from `UpperTheory.Gal.TP.Sub.CharEx`, and the factor $\kappa(w)^{-1}$ is cancelled by `UpperTheory.Gal.Int.Geo.map_inv_mul`. Despite the word "strong", `galoisLocalGlobalStrong_recParameter` has type `UpperTheory.GalStar.Row0b recT`, where `recT` is the condition `IsRecT` on reciprocity maps. The proof is `galoisRepresentations_of_thetaLift UpperTheory.TP.K.tLiftK`. Toral, tame and square-free are `Tor`, `TmW` and `Sqf`, big is `IsQpBig`, and matching is `AwayB`.
