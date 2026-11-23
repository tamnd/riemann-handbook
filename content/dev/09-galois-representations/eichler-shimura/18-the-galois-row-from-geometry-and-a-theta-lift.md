---
title: The Galois row from geometry and a theta lift
decls:
  - UpperTheory.Gal.Int.Geo.weight_one_geometric_realization
  - UpperTheory.Gal.Int.rest
  - UpperTheory.Gal.Int.galoisLocalGlobal_of_geometry_lift
  - UpperTheory.Gal.Int.galoisLocalGlobalStrong_of_geometry_lift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Galois row from geometry and a theta lift

This section joins the parts of the chapter. The Galois row in weight one (Definition 3.7.1) gives Galois representations for spaces of automorphic forms on unitary groups in an odd number of variables. A theta lift for unitary dual pairs carries these to all regular algebraic polarized cuspidal representations of $\mathrm{GL}_a$, with the right behaviour at spherical places. The compatibility at depth zero of Section 17 then gives the local clauses of Theorem 3.7.5. The main result, Theorem 3.18.5, is the input of the proof of Theorem 3.7.5 and of [the written step](/step/galois-local-global-strong-of-geometry-lift/).

We keep the notation of Section 07 and Section 17: $E$ is a CM field, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, and $\pi$ is a regular algebraic cuspidal representation of $\mathrm{GL}_a(\mathbb{A}_E)$ polarized by a Hecke character $\chi$ of $E^+$. For a local component $\sigma$ at $w$ and a reciprocity map $\mathrm{rc}$, $y_\sigma = \mathrm{rc}(\sigma \otimes |\det|^{(1-a)/2})$.

### The Lefschetz formula

The first input of Theorem 3.7.3 is the holomorphic Lefschetz formula, Theorem 3.7.2.

**Theorem 3.18.1 (the holomorphic Lefschetz formula holds).** Let $Z$ be a smooth projective variety of dimension $d$ over $\mathbb{C}$, and let $c_1, c_2 : Y \to Z$ be finite étale morphisms over $\mathbb{C}$ such that the set $F$ of points $y$ with $c_1(y) = c_2(y)$ is finite and $\det(1 - A_y) \neq 0$ for the tangent map $A_y$ at each $y \in F$. Then each $H^b(Z, \Omega^p)$ is finite-dimensional, and
$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^p)\bigr) = \sum_{y \in F} \frac{[t^p] \det(1 + t A_y)}{\det(1 - A_y)}.$$

Lean: `UpperTheory.Gal.Int.Geo.weight_one_geometric_realization`.

*Proof.* This is [Theorem 5.7.3 of Volume 3](/entry/t-lefschetz-fixed-point-finite-etale-correspondence/), the [[Lefschetz fixed-point theorem|G44NQXCWT9]] for the Dolbeault complex and a finite étale correspondence. $\square$

With Theorem 3.7.3 this gives Corollary 3.7.4: the Galois row in weight one holds.

### Two forms of the Galois row

The general case passes through two statements. The first one describes the representation at spherical places only.

**Definition 3.18.2 (the spherical Galois row).** The *spherical Galois row* holds if, for every CM field $E$, prime $\ell$, $\iota$, $a \geq 1$ and every regular algebraic cuspidal $\pi$ of $\mathrm{GL}_a(\mathbb{A}_E)$ polarized by $\chi$:

1. there is a continuous representation $r : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ attached to $\pi$ in the sense of Section 17;
2. for each such $r$ and each place $w$ at which $\pi$ has Satake parameters $B$: if $w \nmid \ell$, the Frobenius eigenvalues of $r$ at $w$ are given by $B$ through $\iota$; if $w \mid \ell$, then $r$ is crystalline and de Rham at $w$ with Hodge-Tate jumps $\mathrm{HT}(\tau)$, and the characteristic polynomial of the crystalline Frobenius is that of the unramified Weil-Deligne representation with parameters $B$.

Lean: `GlobalTheory.RoadU.CoreAll`.

The second statement is Theorem 3.7.5 with a weaker condition on the place in the tame case.

**Definition 3.18.3 (the Galois row at all $\mathbb{Q}_g$ places).** The *Galois row at all $\mathbb{Q}_g$ places* holds if the conclusion of Theorem 3.7.5 holds for all data, for reciprocity maps that satisfy the laws of [the local reciprocity step](/step/is-rect-def/), with these two changes:

1. in clause 3, *match* means matching in the sense of Section 07 with "$w$ is big for $\dim y$" replaced by "$E_w \cong \mathbb{Q}_g$ for a prime $g$";
2. in clause 4, the tame and square-free case asks only $E_w \cong \mathbb{Q}_g$, not that $w$ is big for $a$.

Lean: `UpperTheory.GalStar.Row0` (also `UpperTheory.GalStar.Row0b`, the form with $w$ big, which is the statement of Theorem 3.7.5).

A place that is big for $n$ has $E_w \cong \mathbb{Q}_g$ by definition. So the Galois row at all $\mathbb{Q}_g$ places asks the tame clause at more places than Theorem 3.7.5.

### From spherical places to all places

**Theorem 3.18.4 (the Galois row from the spherical Galois row).** If the spherical Galois row holds, then the Galois row at all $\mathbb{Q}_g$ places holds.

Lean: `UpperTheory.Gal.Int.rest` (also `UpperTheory.Gal.Int.Row.galoisLocalGlobal_of_localGlobalCompatibility`).

*Proof.* The spherical Galois row implies compatibility for plain toral components (Definition 3.17.3), by [the theorem on unlinked supports](/entry/toral-galois-galois-compat-unlinked-support-of-spherical/). Then Theorem 3.17.12 gives compatibility at depth zero.

Fix the data. Item 1 of Definition 3.18.2 gives $r$, and the weights give $\mathrm{wt}$ and $\mathrm{HT}(\tau)$ as in clause 2 of Theorem 3.7.5. Clauses 1 and 2 hold since $r$ is attached to $\pi$. We use four local facts. Let $\sigma$ be a local component of $\pi$ at $w$.

1. $\sigma \otimes |\det|^{(1-a)/2}$ is generic, as a twist of a local component of a cuspidal representation.
2. If $y_\sigma$ is toral with zero monodromy, then $\sigma \otimes |\det|^{(1-a)/2}$ is plain toral.
3. If $E_w \cong \mathbb{Q}_g$ and $y_\sigma$ is tame and square-free with zero monodromy, then $\sigma$ has depth zero and $\sigma \otimes |\det|^{(1-a)/2}$ is apart.
4. Each element of degree $0$ of the Weil group lies in inertia. So two Weil-Deligne representations with the same characteristic polynomials on inertia have the same characteristic polynomials on every element of degree $0$, and the same dimension.

Facts 2 and 3 use fact 1 and the laws of the reciprocity map; we take them from the development (Remark 3.18.7). Behind fact 3 is the following picture. A depth-zero supercuspidal member of size $m \geq 2$ gives on inertia eigenvalues outside the $(g-1)$-th roots of unity, and two members that are unramified twists of each other give the same eigenvalues, so they give roots of multiplicity at least $2$ that square-freeness excludes.

Clause 3, at $w \nmid \ell$. The dimensions agree by the laws of $\mathrm{rc}$. If $y_\sigma$ is toral with zero monodromy, fact 2 and item 1 of Definition 3.17.3 give $\mathrm{WD}_w(r) = y_\sigma$. If $E_w \cong \mathbb{Q}_g$ and $y_\sigma$ is tame and square-free with zero monodromy, fact 3 and item 1 of Definition 3.17.4 give zero monodromy for $\mathrm{WD}_w(r)$ and the same characteristic polynomials on inertia, and fact 4 gives them on every element of degree $0$.

Clause 4, at $w \mid \ell$. If $\sigma$ is spherical, it has Satake parameters, and item 2 of Definition 3.18.2 gives the crystalline and de Rham statements. If $y_\sigma$ is toral with zero monodromy, fact 2 and item 2 of Definition 3.17.3 give potential semistability, zero monodromy and equal characteristic polynomials on the whole Weil group; two Weil-Deligne representations with zero monodromy and Frobenius semisimple with equal characteristic polynomials everywhere are isomorphic, so $\mathrm{WD}_w(r) = y_\sigma$. In the tame and square-free case, fact 3 and item 2 of Definition 3.17.4 give the statement, with fact 4 for the elements of degree $0$. $\square$

### The two inputs

Theorem 3.18.4 reduces the general case to the spherical Galois row. Two statements give it.

The first is the Galois row in weight one (Definition 3.7.1). Its representations have some dimension and only satisfy a divisibility at good places, and the representations they give live on unitary groups. By [the seed theorem](/entry/seed-fin-odd-of-geo-one/), the Galois row in weight one gives, for each space $U'$ on $\mathrm{U}(a)$ with $a$ odd and the extra conditions at the auxiliary places, a continuous semisimple $r$ of dimension $a$ whose characteristic polynomials of Frobenius are the Satake polynomials of $U'$. By [the congruence theorem](/entry/cong-fin-odd-of-ex/) and the existence of lacunary weights, the Hecke eigenvalues of a general $U$ are limits of those of such $U'$.

The second is the theta lift statement [TLiftK](/step/tlift-k-def/) for the [[theta correspondence|6WB6TKE70H]], stated after Theorem 3.7.5: forms on a [[unitary group|0R9R0Y1HDK]] of large weight have nonzero theta lifts to all larger unitary groups beyond some point. It carries the result from odd $a$ to all $a$.

From the seed, the congruence and the theta lift, [the theorem of the main line](/entry/core-all-of/) proves the spherical Galois row: a limit argument gives representations for all $U$ on $\mathrm{U}(a)$ with $a$ odd, the theta lift passes to all $a$, and a descent from unitary groups and a base change to CM extensions reach all $\pi$.

**Theorem 3.18.5 (the Galois row from geometry and a theta lift).** If the Galois row in weight one holds and the theta lift statement holds, then the Galois row at all $\mathbb{Q}_g$ places holds.

Lean: `UpperTheory.Gal.Int.galoisLocalGlobal_of_geometry_lift`.

*Proof.* The Galois row in weight one gives the seed statement by [the seed theorem](/entry/seed-fin-odd-of-geo-one/). The existence of lacunary weights, [which holds](/entry/wt-lac-ex-holds/), gives the congruence statement by [the congruence theorem](/entry/cong-fin-odd-of-ex/). With the theta lift statement, [the theorem of the main line](/entry/core-all-of/) gives the spherical Galois row, and Theorem 3.18.4 gives the Galois row at all $\mathbb{Q}_g$ places. $\square$

**Theorem 3.18.6 (Theorem 3.7.5 from geometry and a theta lift).** If the Galois row in weight one holds and the theta lift statement holds, then the conclusion of Theorem 3.7.5 holds.

Lean: `UpperTheory.Gal.Int.galoisLocalGlobalStrong_of_geometry_lift` (also `UpperTheory.GalStar.Row0.row0b`).

*Proof.* Theorem 3.18.5 gives the Galois row at all $\mathbb{Q}_g$ places. Clauses 1, 2 and the spherical part of clause 4 are the same in both statements. For the matching in clause 3 and for the tame case of clause 4, a place $w$ that is big for $a$ has $E_w \cong \mathbb{Q}_g$, so the hypothesis of the weaker statement implies that of the stronger one, and the conclusions agree. $\square$

With Corollary 3.7.4 and [the theta lift theorem](/entry/t-lift-k/), Theorem 3.18.6 gives Theorem 3.7.5, as in its proof in Section 07.

**Remark 3.18.7 (Formalization).** The names of the Lefschetz theorem and of the construction of the Galois row are swapped, as Remark 3.7.7 says: `weight_one_geometric_realization` has type `LocalSmoothExtension.HolomorphicLefschetzFormula`, and its proof is `unfold` followed by `exact GlobalTheory.T.lefschetz_fixedPoint_finite_etale_correspondence`; `geoOne_holds` is `geometric_realization_of_weight_one weight_one_geometric_realization`. The proof of `rest` writes the term `galoisCompat_unlinkedSupport_of_spherical h` twice, once for `R1` and once inside `localGlobalCompatAtIwahoriFixed_of_unlinked`, instead of naming it once. `galoisCompat_unlinkedSupport_of_spherical` is the version with `inq_holds` applied, which we did not open. The assembly `galoisLocalGlobal_of_localGlobalCompatibility` goes through `localGlobalAtPlaceClass_of_localGlobal` with the trivial place class, and the lemmas `away`, `above`, `crys`, `guard_tame`, `charPol_of_ine` and `dim_of_ine`, which we read; facts 2 and 3 are `plainTor_of_tor` and `mixed_of_tame`, which we did not open, and neither `exists_weights` nor `WeakTheRep.eq_of_mono0_charPol`. Despite the word "Strong", `galoisLocalGlobalStrong_of_geometry_lift` has type `Row0b recT`, the weaker statement, and is `Row0.row0b recT` applied to `galoisLocalGlobal_of_geometry_lift`, whose type `Row0 recT` is the stronger one. The same file has the alternatives `galois_realisation_of_rank_two`, with the place class `IsQpBig`, and `galois_realisation_of_top`. Here `recT` is the condition `IsRecT`, and the existence of such maps is the local Langlands correspondence, used as a hypothesis from the literature.

## Notes and references

The chapter feeds [the Galois row](/proof/galois-row/). Its geometric part is the step [GeoOne holds](/step/geo-one-holds/), and its top result, Theorem 3.18.6 with the theta lift, is the step [the Galois row from a theta lift](/step/galois-representations-of-theta-lift/). It gives the hypothesis [Row0b](/step/row0b-def/) of the step [the Galois row holds](/step/galois-row-holds/), which the main proof uses for [every character](/step/every-character/).

The standard theorem behind Theorem 3.7.5, with the sources listed after it in Section 07, asks the full local-global compatibility at all places. Here the compatibility away from $\ell$ is full only in the toral case, and in the tame and square-free case it holds for characteristic polynomials on elements of degree $0$ at places with $E_w \cong \mathbb{Q}_g$. The Galois representations are built from unitary Shimura varieties in weight one and a theta lift, not from the cohomology of Shimura varieties of all weights.

- M. F. Atiyah and R. Bott, *A Lefschetz fixed point formula for elliptic complexes II. Applications*, Ann. of Math. 88 (1968), §4, for the holomorphic Lefschetz formula.
- J. Arthur and L. Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*, Ann. of Math. Stud. 120 (1989), Chapter 3, for cyclic base change of prime degree.
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II. On irreducible representations of GL(n)*, Ann. Sci. ÉNS 13 (1980), §9, for generic representations as products of unlinked segments.
