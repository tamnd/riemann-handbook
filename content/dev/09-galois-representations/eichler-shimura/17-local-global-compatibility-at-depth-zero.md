---
title: Local-global compatibility at depth zero
decls:
  - UpperTheory.Gal.InertialTypesAlt.suppBC_holds
  - UpperTheory.Gal.InertialTypesAlt.suppBC_outright
  - UpperTheory.Gal.ToralGalois.R2.toTor_holds
  - UpperTheory.Gal.ToralGalois.R2.localGlobalCompatAtIwahoriFixed_of_unlinked
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local-global compatibility at depth zero

This section proves the local statement behind clauses 3 and 4 of Theorem 3.7.5 at places where $\sigma$ has depth zero. The method is base change: along a chain of cyclic extensions in which $w$ has no inertia, the local component becomes a principal series of tame characters with no two linked, and there the compatibility is known. The result, Theorem 3.17.12, is one of the three inputs of [the theorem that builds the Galois row](/entry/rest/).

Throughout, $E$ is a CM field, $\Omega$ an algebraic closure of $E$, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ and $n \geq 1$. Let $\pi$ be a regular algebraic cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ polarized by a Hecke character $\chi$ of $E^+$, as in Theorem 3.7.5. Let $r : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ be a continuous representation *attached* to $\pi$: clauses 1 and 2 of Theorem 3.7.5 hold for $r$, and at almost all places the Frobenius eigenvalues of $r$ are the Satake parameters of $\pi$ through $\iota$. For a local component $\sigma$ of $\pi$ at $w$ we write $\sigma^\circ = \sigma \otimes |\det|^{(1-n)/2}$, so that $y_\sigma = \mathrm{rc}(\sigma^\circ)$ for a reciprocity map $\mathrm{rc}$ as in Section 07.

### Supports

Let $F$ be a nonarchimedean local field with ring of integers $\mathcal{O}$, maximal ideal $\mathfrak{p}$ and residue field $k$. Put $K_1 = \ker\bigl(\mathrm{GL}_m(\mathcal{O}) \to \mathrm{GL}_m(k)\bigr)$. Every irreducible smooth representation $x$ of $\mathrm{GL}_m(F)$ is a subquotient of a representation induced from a supercuspidal representation $y_1 \otimes \dots \otimes y_s$ of a Levi subgroup $\mathrm{GL}_{m_1} \times \dots \times \mathrm{GL}_{m_s}$; the multiset $\{y_1, \dots, y_s\}$ is a *support* of $x$, and $m_i$ is the *size* of $y_i$.

**Definition 3.17.1 (depth zero and plain toral representations).** Let $x$ be an irreducible smooth representation of $\mathrm{GL}_m(F)$.

1. $x$ has *depth zero* if $x^{K_1} \neq 0$.
2. A multiset $s$ of supercuspidal representations is *unlinked* if there are no $y, z \in s$ with $y \cong z \otimes |\det|$.
3. $x$ is *plain toral* if it has an unlinked support whose members all have size $1$, that is, $x$ is a full induced representation from characters $\xi_1, \dots, \xi_m$ of $F^\times$ with $\xi_i \neq \xi_j |\cdot|$ for all $i, j$.

Lean: `GlobalTheory.RoadU.PlainTor` (also `GlobalTheory.RoadU.Unlinked`, `UpperTheory.Zero.LLC.DZ`).

Two supercuspidal representations $y, z$ are *unramified twists* of each other if $y \cong z \otimes (\mu \circ \det)$ for an unramified character $\mu$.

**Definition 3.17.2 (apart and mixed).** An irreducible smooth representation $x$ of $\mathrm{GL}_m(F)$ is *apart* if, for every support $s$ of $x$, any two members of $s$ of size at least $2$ are not unramified twists of each other. It is *mixed* if it has depth zero and some support $s$ of $x$ is unlinked and has this property.

Lean: `UpperTheory.Gal.InertialTypesAlt.Mixed` (also `UpperTheory.Gal.ToralGalois.R2.Apart`).

Twisting by $|\det|^c$ twists the supports and preserves both conditions, so $\sigma$ is apart if and only if $\sigma^\circ$ is apart.

### The two compatibility statements

Write $\mathrm{WD}_w(r)$ for the Weil-Deligne representation of $r$ at $w$; for $w \mid \ell$ it is defined through the comparison data of [[potentially semistable|6YDZNXR19H]] representations. We write $\operatorname{charpol}_t$ for the characteristic polynomial of an element $t$ of the Weil group.

**Definition 3.17.3 (compatibility for plain toral components).** *Compatibility for plain toral components* holds if, for all data $E, \ell, \iota, n, \pi, \chi, r$ as above, every place $w$ and every local component $\sigma$ of $\pi$ at $w$ with $\sigma^\circ$ plain toral:

1. if $w \nmid \ell$, then $\mathrm{WD}_w(r)$ has zero monodromy and equals $\mathrm{rc}(\sigma^\circ)$ for every reciprocity map $\mathrm{rc}$;
2. if $w \mid \ell$, then $r$ is de Rham at $w$ with Hodge-Tate jumps $\mathrm{HT}(\tau)$ at each $\tau$ inducing $w$, and for all comparison data $r$ is potentially semistable at $w$, $\mathrm{WD}_w(r)$ has zero monodromy, and $\operatorname{charpol}_g \mathrm{WD}_w(r) = \operatorname{charpol}_g \mathrm{rc}(\sigma^\circ)$ for every reciprocity map and every $g$ in the Weil group.

Lean: `GlobalTheory.DeRhamOfPlainTorus.R1`.

**Definition 3.17.4 (compatibility at depth zero).** *Compatibility at depth zero* holds if, for all data as above, every place $w$ and every local component $\sigma$ of $\pi$ at $w$ such that $\sigma$ has depth zero, and either $\sigma^\circ$ is plain toral, or $E_w \cong \mathbb{Q}_g$ for a prime $g$ and $\sigma^\circ$ is apart, the following holds for every reciprocity map $\mathrm{rc}$ such that $\mathrm{rc}(\sigma^\circ)$ has zero monodromy:

1. if $w \nmid \ell$, then $\mathrm{WD}_w(r)$ has zero monodromy, and $\operatorname{charpol}_t \mathrm{WD}_w(r) = \operatorname{charpol}_t \mathrm{rc}(\sigma^\circ)$ for every $t$ in inertia;
2. if $w \mid \ell$, then $r$ is de Rham at $w$ with Hodge-Tate jumps $\mathrm{HT}(\tau)$, and for all comparison data $r$ is potentially semistable at $w$, $\mathrm{WD}_w(r)$ has zero monodromy, and the same equality of characteristic polynomials holds for every $t$ in inertia.

Lean: `UpperTheory.Gal.ToralGalois.R2.LocalGlobalCompatAtIwahoriFixedPlaces`.

### Base change along a chain

**Definition 3.17.5 (chain of base changes).** A *point* over $E$ is a pair $(K, \pi_K)$ of a totally complex number field $E \subseteq K \subseteq \Omega$ and a cuspidal representation $\pi_K$ of $\mathrm{GL}_n(\mathbb{A}_K)$. A *step* $(K, \pi_K) \to (M, \pi_M)$ is a pair of points with $K \subseteq M$, $M/K$ Galois of prime degree, and $\pi_M$ a weak base change of $\pi_K$: at almost all places $u$ of $M$, if $B$ is a multiset of Satake parameters of $\pi_K$ at the place under $u$ and $f$ is the residue degree, then $B^f = \{\beta^f : \beta \in B\}$ is a multiset of Satake parameters of $\pi_M$ at $u$. A *chain* from $(E, \pi)$ to $(K, \pi_K)$ is a finite sequence of steps.

Lean: `UpperTheory.Gal.InertialTypesAlt.Lifts`.

A character $\xi$ of $F^\times$ is *tame* if it is trivial on $1 + \mathfrak{p}$.

**Definition 3.17.6 (toral over).** Let $(K, \pi_K)$ be a point, $A$ a valuation ring of $\Omega$ over a place $v$ of $E$ and a place $w$ of $K$, $x$ an irreducible representation of $\mathrm{GL}_n(E_v)$, $\tau'$ a representation of $\mathrm{GL}_n(K_w)$, and $\xi_1, \dots, \xi_n$ smooth characters of $K_w^\times$. Then $\tau'$ is *toral over* $x$ with $\xi$ if:

1. each $\xi_j$ is tame;
2. $\{\xi_1, \dots, \xi_n\}$ is a support of $\tau'$;
3. for every reciprocity map $\mathrm{rc}$ at $v$, every local Artin map $a'$ at $w$ and every $t$ in the inertia group of $A$ over $K$, viewed in the inertia group over $E$,
$$\operatorname{charpol}_t \mathrm{rc}(x) = \prod_{j=1}^n \bigl(X - \xi_j(a'(t))\bigr).$$

Lean: `UpperTheory.Gal.InertialTypesAlt.ToralOver`.

**Definition 3.17.7 (inflation matching).** *Inflation matching* holds if, for every unramified extension $K/k$ of $p$-adic fields with residue fields $\kappa_K/\kappa_k$ and every $s \in \operatorname{Gal}(K/k)$ that reduces to the Frobenius: for a class function $\phi$ on $\mathrm{GL}_n(\kappa_k)$, let $f$ be its inflation to $\mathrm{GL}_n(\mathcal{O}_k)$ and $f'$ the inflation of its Shintani lift to $\mathrm{GL}_n(\mathcal{O}_K)$. Then the twisted orbital integral of $f'$ at $\delta$ equals the orbital integral of $f$ at $\gamma$ whenever the norm $\delta\, s(\delta) \cdots s^{f-1}(\delta)$ is regular semisimple with the characteristic polynomial of $\gamma$, and every regular semisimple $\gamma$ at which the orbital integral of $f$ is nonzero comes from a norm.

Lean: `GlobalTheory.DZA.InflMatching`.

**Theorem 3.17.8 (depth-zero components after base change).** Assume inflation matching. Let $E$ be totally complex, $\pi$ cuspidal on $\mathrm{GL}_n(\mathbb{A}_E)$ with $n > 0$, and $(K, \pi_K)$ reached from $(E, \pi)$ by a chain. Let $A$ lie over places $v$ of $E$ and $w$ of $K$, with $E_v \cong \mathbb{Q}_g$ and $K$ fixed by the inertia group of $A$ over $E$. Let $\tau = \pi_v$ and $\tau' = \pi_{K,w}$, and suppose that $\tau$ has depth zero and that $N(w) = g^f$ where $f$ is divisible by the size of each member of each support of $\tau$. Then there are characters $\xi_1, \dots, \xi_n$ of $K_w^\times$ such that $\tau'$ is toral over $\tau$ with $\xi$, and if $\tau$ is mixed, then $\{\xi_1, \dots, \xi_n\}$ is unlinked.

Lean: `UpperTheory.Gal.InertialTypesAlt.suppBC_holds` (also `UpperTheory.Gal.InertialTypesAlt.SuppBC`).

*Proof.* Since $\tau$ has depth zero, $\tau^{K_1}$ is a nonzero representation of $\mathrm{GL}_n(\mathbb{F}_g)$, and its members of each support are depth-zero supercuspidal representations whose reductions are cuspidal representations of $\mathrm{GL}_{m_i}(\mathbb{F}_g)$. A cuspidal representation of $\mathrm{GL}_m(\mathbb{F}_g)$ comes from a character of $\mathbb{F}_{g^m}^\times$ in general position, and its Shintani lift to $\mathbb{F}_{g^f}$ with $m \mid f$ is a principal series. The proof carries this along the chain.

First, inflation matching gives the following trace statement across one step of the chain at a place without inertia: if a class function on $\mathrm{GL}_n$ of the residue field pairs nonzero with the trace of $\tau^{K_1}$, then its Shintani lift acts nonzero on $\tau'^{K_1}$.

Second, by induction along the chain on combinatorial labels of the constituents of $\tau^{K_1}$, the trace statement shows that $\tau'$ has depth zero with a support of tame characters $\xi_1, \dots, \xi_n$, and that these characters, through the local Artin map at $w$ and the norm, restrict on inertia to the characters that give the inertia of $\mathrm{rc}(\tau)$. Since $K$ is fixed by inertia over $E$, an element $t$ of inertia over $K$ is an element of inertia over $E$, and this gives item 3 of Definition 3.17.6.

Third, if $\tau$ is mixed, the trace statement shows that a parahoric subgroup of $\mathrm{GL}_n(K_w)$ acts on a vector of $\tau'$ by a character built from pairwise distinct characters of $\mathbb{F}_w^\times$. Since $\tau'$ is generic, a type of this form forces the support to be unlinked. The two parts together give the theorem. $\square$

**Theorem 3.17.9 (depth-zero components after base change, unconditional).** The conclusion of Theorem 3.17.8 holds without the hypothesis.

Lean: `UpperTheory.Gal.InertialTypesAlt.suppBC_outright`.

*Proof.* Inflation matching is proved in the development, for the inflated functions of depth zero of Definition 3.17.7 (Remark 3.17.13). Apply [Theorem 3.17.8](/entry/supp-bc-holds/). $\square$

### From mixed to plain toral

**Definition 3.17.10 (the toral step).** The *toral step* holds if, for all data $E, \ell, \iota, n, \pi, \chi, r$ as above, every place $w$ with $E_w \cong \mathbb{Q}_g$, every mixed local component $\sigma$ of $\pi$ at $w$, every valuation ring $A$ over $w$ and every reciprocity map $\mathrm{rc}$, there are an abelian CM extension $K/E$ in $\Omega$, a place $u$ of $K$ under $A$, a cuspidal representation $P$ of $\mathrm{GL}_n(\mathbb{A}_K)$ polarized by a character $\chi'$, a local component $T$ of $P$ at $u$, and a reciprocity map $\mathrm{rc}'$ at $u$, such that:

1. $(P, \chi')$ satisfies the hypotheses of Theorem 3.7.5, and $r|_{\operatorname{Gal}(\Omega/K)}$ is attached to $P$;
2. the infinitesimal character of $P$ at $\tau$ equals that of $\pi$ at $\tau|_E$ for every $\tau : K \to \mathbb{C}$;
3. $T^\circ$ is plain toral;
4. every $t$ in inertia over $E$ agrees on $\Omega$ with some $t'$ in inertia over $K$, and $\operatorname{charpol}_{t'} \mathrm{rc}'(T^\circ) = \operatorname{charpol}_t \mathrm{rc}(\sigma^\circ)$.

Lean: `UpperTheory.Gal.ToralGalois.R2.ToTor`.

**Theorem 3.17.11 (the toral step).** The toral step holds.

Lean: `UpperTheory.Gal.ToralGalois.R2.toTor_holds`.

*Proof.* Since $E_w \cong \mathbb{Q}_g$, the place $w$ is split over $E^+$ and has norm $g$. Choose an abelian CM extension $K/E$ in which the inertia groups at $w$ and at the non-split places act trivially and each place over $w$ has norm $g^{n!}$, with $n!$ divisible by every size; such a field exists by [the splitting criterion](/entry/unr-field-holds/). Write $K/E$ as a tower of cyclic extensions of prime degree. Cyclic base change along this tower gives a chain from $(E, \pi)$ to a point $(K, P)$, and each step keeps the polarization, the regularity and the attached representation, so $P$ satisfies item 1. The infinitesimal characters along each step are compositions of those below, which gives item 2.

Let $T = P_u$. The inertia groups of $A$ over $E$ and over $K$ coincide, since $K$ has no inertia at $w$, and the local Artin maps correspond through the norm. Theorem 3.17.9 gives tame characters $\xi_1, \dots, \xi_n$ that form a support of $T$, unlinked since $\sigma$ is mixed, with
$$\operatorname{charpol}_t \mathrm{rc}(\sigma) = \prod_j \bigl(X - \xi_j(a'(t))\bigr).$$
Twisting by $|\det|^{(1-n)/2}$ does not change unlinkedness, and $|\cdot|$ is trivial on inertia, so $T^\circ$ is plain toral and the identity holds for $\sigma^\circ$. A reciprocity map $\mathrm{rc}'$ at $u$ exists by [the existence of reciprocity maps](/entry/rec-texists/), and on a plain toral representation it is the sum of the characters $\xi_j \circ (a')^{-1}$, up to the same twist. Comparing the two products gives item 4. $\square$

**Theorem 3.17.12 (compatibility at depth zero).** If compatibility for plain toral components holds, then compatibility at depth zero holds.

Lean: `UpperTheory.Gal.ToralGalois.R2.localGlobalCompatAtIwahoriFixed_of_unlinked`.

*Proof.* Fix the data, $w$, $\sigma$ and $\mathrm{rc}$. If $\sigma^\circ$ is plain toral, Definition 3.17.3 gives more than we need: an equality of Weil-Deligne representations away from $\ell$, and of characteristic polynomials on the whole Weil group above $\ell$.

Otherwise $E_w \cong \mathbb{Q}_g$ and $\sigma^\circ$ is apart. Then $\sigma$ is apart. The component $\sigma^\circ$ is generic, as a twist of a local component of a cuspidal representation. An irreducible generic representation is a product of pairwise unlinked segments, and $\mathrm{rc}(\sigma^\circ)$ has zero monodromy, so all segments have length $1$, and the support of $\sigma^\circ$ is unlinked. Twisting back, $\sigma$ has an unlinked support, and since $\sigma$ has depth zero it is mixed.

Theorem 3.17.11 gives $K$, $u$, $P$, $T$ and $\mathrm{rc}'$. Apply Definition 3.17.3 over $K$ to $P$, $r|_{\operatorname{Gal}(\Omega/K)}$ and $T$. For $w \nmid \ell$, the place $u$ is prime to $\ell$, and $\mathrm{WD}_u(r|_K)$ is the restriction of $\mathrm{WD}_w(r)$ to the Weil group of $K_u$. Restriction preserves zero monodromy in both directions, and the characteristic polynomials on the common inertia group. So item 4 of Definition 3.17.10 gives item 1 of Definition 3.17.4.

For $w \mid \ell$, $r|_K$ is de Rham at $u$ with the jumps of $P$, which by item 2 of Definition 3.17.10 are those of $\pi$; since de Rham descends along the finite extension $K_u/E_w$, $r$ is de Rham at $w$ with these jumps. Potential semistability is a property of the restriction to an open subgroup, so it passes from $u$ to $w$, and the Weil-Deligne representation of $r$ at $w$ restricts to that of $r|_K$ at $u$. The argument away from $\ell$ then gives item 2. $\square$

**Remark 3.17.13 (Formalization).** The proof of `localGlobalCompatAtIwahoriFixed_of_unlinked` is `r2g mixedOf toTor_holds drDesc recTExists`, with the case split in `r2g`; the hypothesis $R1$ is supplied later, in `rest`, by `galoisCompat_unlinkedSupport_of_spherical`. `toTor_holds` passes `suppBC_outright`, `unrField_holds`, `NearKilling.allLift_holds`, `NearKilling.ineNorm`, `infLifts (infStep stableOf)`, `recChars suppIne` and `recTExists` to the lemma `toTor`. `suppBC_holds h` is `suppBC_of_mix (suppAny_holds h) (mixUnlinked (mixType_holds h))`, where both halves go through `L.finTrace_of_matching`, and `suppBC_outright` is `suppBC_holds L.inflMatch`. We did not open the proofs of `toTor`, `finTrace_of_matching`, `suppAny_of`, `mixType_of`, `inflMatch` or the restriction lemmas, so those steps above are summaries. Some points differ from the names. The hypothesis of `LocalGlobalCompatAtIwahoriFixedPlaces` is a vector fixed by `KOne`, the kernel of reduction, not by an Iwahori subgroup. Zero monodromy of `rc (algNorm σ)` is a hypothesis that is carried to $r$, not proved. The conclusion compares characteristic polynomials only on inertia (`Ine`), while `R1` gives equality away from $\ell$ and the whole Weil group above $\ell$. In `ToralOver` the inertia polynomial is that of `rc x` for $x = \tau$ itself, not of the twist `algNorm`; `ToTor` uses `algNorm σ`. `suppBC_outright` removes only the hypothesis `InflMatching`, by `L.inflMatch`.
