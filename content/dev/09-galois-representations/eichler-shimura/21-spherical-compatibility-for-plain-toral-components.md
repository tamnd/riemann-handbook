---
title: Compatibility for plain toral components from spherical places
decls:
  - GalTw.GlobalTheory.RoadU.exists_sph_lift_of_toral
  - GalTw.GlobalTheory.DeRhamOfPlainTorus.galoisCompat_unlinkedSupport_of_spherical
  - UpperTheory.Gal.ToralGalois.galoisCompat_unlinkedSupport_of_spherical
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Compatibility for plain toral components from spherical places

The proof of [the Galois row from the spherical Galois row](/entry/rest/) needs compatibility for plain toral components (Definition 3.17.3). This section proves it from the spherical Galois row (Definition 3.18.2). The idea is a base change to a solvable CM extension $M/E$ with a place $u$ above $w$ where the lift is spherical. At $u$ the spherical Galois row gives the Frobenius eigenvalues and the crystalline and de Rham properties, which descend to $E$. One extension gives the statement only for one $g$ of nonzero degree, as $g$ must fix $M$; traces then give it for all elements.

We keep the notation of Section 17. $E$ is a CM field, $\Omega$ an algebraic closure of $E$, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ and $n \geq 1$. The cuspidal representation $\pi$ of $\mathrm{GL}_n(\mathbb{A}_E)$ is *in scope* if it is regular algebraic and polarized by a Hecke character $\chi$ of $E^+$. The representation $r : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ is attached to $\pi$, and $\sigma^\circ = \sigma \otimes |\det|^{(1-n)/2}$ for a local component $\sigma$. For a valuation ring $A$ of $\Omega$ over a place $w$ we write $W_A$ for the Weil group at $A$ and $\deg : W_A \to \mathbb{Z}$ for its degree map. A *local Artin map* is a homomorphism $a : W_A \to E_w^\times$ with the properties of the reciprocity map of local class field theory. For a multiset $B$ of nonzero complex numbers, $\mathrm{WD}^{\mathrm{sat}}_u(B)$ is the unramified Weil-Deligne representation built from $B^{-1} = \{\beta^{-1} : \beta \in B\}$ and twisted by $|\cdot|^{(1-n)/2}$, as in item 2 of Definition 3.18.2.

### Lifts and the local inputs

**Definition 3.22.1 (Lift and character lift).** Let $K \subseteq M$ be totally complex number fields and let $\pi_K$, $\pi_M$ be cuspidal representations of $\mathrm{GL}_n(\mathbb{A}_K)$ and $\mathrm{GL}_n(\mathbb{A}_M)$. Then $\pi_M$ is a *lift* of $\pi_K$ if:

1. for every finite place $u$ of $M$ with $N(u) = N(v)^f$, where $v$ is the place under $u$, Satake parameters $B$ of $\pi_K$ at $v$ give Satake parameters $B^f = \{\beta^f : \beta \in B\}$ of $\pi_M$ at $u$;
2. the infinitesimal character of $\pi_M$ at an embedding $\tau : M \to \mathbb{C}$ is that of $\pi_K$ at $\tau|_K$;
3. if $i : K_v \cong M_u$ is a continuous isomorphism compatible with $K \to M$, then the local components of $\pi_K$ at $v$ and of $\pi_M$ at $u$ correspond under $i$.

It is a *character lift* if in addition, for every $u$ over $v$, local components $\tau$ of $\pi_K$ at $v$ and $T$ of $\pi_M$ at $u$, and smooth characters $\xi_1, \dots, \xi_n$ of $K_v^\times$: if $\{\xi_j\}$ is a support of $\tau$, then $\{\xi_j \circ N_{M_u/K_v}\}$ is a support of $T$.

Lean: `GlobalTheory.RoadU.CharLift` (also `GlobalTheory.RoadU.IsLift`).

**Definition 3.22.2 (The local inputs).** The *local inputs* are eleven published results and one more statement. The results include rigidity of Jacquet and Shalika, the exhaustion of the local Langlands correspondence for $\mathrm{GL}_n$, the theorem of Zelevinsky, the generic unitary dual of $\mathrm{GL}_n$, the strong trace comparison of Arthur and Clozel, and potential semistability of de Rham representations. The extra statement is: if $K \subseteq M$ are totally complex, $M/K$ is Galois of prime degree, $a \geq 1$, and $\pi_M$ is a lift of a cuspidal $\pi_K$ on $\mathrm{GL}_a$, then $\pi_M$ is a character lift of $\pi_K$.

Lean: `UpperTheory.Gal.ToralGalois.Inq` (also `UpperTheory.Gal.Int.Inp.Inp`, `UpperTheory.Gal.ToralGalois.inq_holds`).

All twelve statements are proved in the development. We use the local inputs as a hypothesis and drop it at the end.

### The spherical lift

**Theorem 3.22.3 (Spherical lift of a toral component).** Assume the local inputs. Let $\pi$ be in scope with $\chi$, let $r$ be attached to $\pi$, let $A$ lie over a place $w$ of $E$, and let $\sigma$ be a local component of $\pi$ at $w$. Let $\xi_1, \dots, \xi_n$ be smooth characters of $E_w^\times$ such that $\{\xi_j\}$ is an unlinked support of $\sigma^\circ$. Let $a$ be a local Artin map at $A$ and let $g \in W_A$ with $\deg g \neq 0$. Then there are a CM field $M$ with $E \subseteq M \subseteq \Omega$, a place $u$ of $M$ under $A$, and a cuspidal representation $P$ of $\mathrm{GL}_n(\mathbb{A}_M)$ in scope with some $\chi'$, such that:

1. $P$ is a lift of $\pi$;
2. $g$ fixes $M$;
3. $P$ has Satake parameters $B$ at $u$ such that, for all $g_0 \in W_A$ over $E$ and $g' \in W_A$ over $M$ that act in the same way on $\Omega$,
$$\operatorname{charpol}_{g'} \mathrm{WD}^{\mathrm{sat}}_u(B) = \prod_{j=1}^{n} \bigl(X - \xi_j(a(g_0))\bigr).$$

Lean: `GalTw.GlobalTheory.RoadU.exists_sph_lift_of_toral`.

*Proof.* Put $\xi^0_j = \xi_j |\cdot|^{(n-1)/2}$. Then $\{\xi^0_j\}$ is a support of $\sigma$.

First we construct $M$. Since $r$ is continuous, there is an open subgroup $N_0$ of $G_E$ on which the trace of $r$ has no zero. There is a solvable CM extension $M_0/E$ that is disjoint from $N_0$ in this sense: $M_0/E$ is Galois with solvable group, and every element of $G_E$ is the restriction of an element of $G_{M_0}$ times an element of $N_0$. We can choose $M_0$ so that $D_A(E)$ fixes $M_0$ and $D_A(M_0^+)$ fixes $M_0$. Since $M_0/E$ is solvable, it is reached by a tower of Galois extensions of prime degree. Cyclic base change of prime degree along this tower, with the strong trace comparison, gives a cuspidal $\pi_0$ on $\mathrm{GL}_n(\mathbb{A}_{M_0})$ in scope that is a lift of $\pi$. The extra local input makes each step a character lift, and character lifts compose, so $\pi_0$ is a character lift of $\pi$.

Now let $v_0$ be the place of $M_0$ under $A$, with a local Artin map $a_0$. Since $D_A(E)$ fixes $M_0$, $g$ is an element $g_0$ of the Weil group of $M_0$ at $A$, with the same nonzero degree. There is an open subgroup $V$ of $D_A(M_0)$ that contains the commutator subgroup and $g_0$, such that each $\xi^0_j \circ N \circ a_0$ is trivial on the inertia elements of $V$. Class field theory gives a solvable CM extension $M_1/M_0$ such that an element of $D_A(M_0)$ fixes $M_1$ exactly when it lies in $V$. With an open subgroup $N_1$ of $G_{M_0}$ on which the trace of $r$ has no zero, we can choose $M_1$ disjoint from $N_1$. A second base change gives $P$ on $\mathrm{GL}_n(\mathbb{A}_{M_1})$ in scope with some $\chi'$, and $P$ is a character lift of $\pi_0$, so of $\pi$. Put $M = M_1$. Then $g$ fixes $M$, and every element $t$ of degree $0$ that fixes $M$ has $\xi^0_j(a(t)) = 1$, by the compatibility of local Artin maps with norms. This proves 1 and 2.

Let $u$ be the place of $M$ under $A$. The characters $\xi^0_j \circ N_{M_u/E_w}$ are unramified, since they kill the inertia group. Let $T$ be the local component of $P$ at $u$. Because $P$ is a character lift of $\pi$, $\{\xi^0_j \circ N\}$ is a support of $T$. This support is unlinked: the generic unitary dual and the weight of $\pi$ give $|\xi_j| = |\cdot|^{e_j - \mathrm{wt}/2}$ with $|e_j| < 1/2$, and composition with the norm keeps two such characters from being linked. An unramified unlinked support makes $T$ a full unramified principal series, so $P$ has Satake parameters $B$ at $u$, and $\mathrm{WD}^{\mathrm{sat}}_u(B)$ is the sum of the characters $\xi_j \circ N \circ a'$ for a local Artin map $a'$ at $u$. Compatibility of local Artin maps with the norm gives $N(a'(g')) = a(g_0)$ when $g_0$ and $g'$ act in the same way. This gives 3. $\square$

The field $M$ depends on $g$, so the theorem controls one element of nonzero degree at a time. The next lemma is enough to go further.

**Lemma 3.22.4 (Nonzero degree suffices).** Let $x$ and $y$ be Weil-Deligne representations at $A$. If $\operatorname{charpol}_g x = \operatorname{charpol}_g y$ for every $g \in W_A$ with $\deg g \neq 0$, then $\operatorname{charpol}_g x = \operatorname{charpol}_g y$ for every $g \in W_A$.

Lean: `GlobalTheory.AboveL.charPol_eq_of_deg_ne_zero` (also `GlobalTheory.AboveL.trace_eq_of_trace_mul_pow`).

*Proof.* Let $\varphi$ be a Frobenius element, so $\deg \varphi = 1$. The polynomials at $\varphi$ are equal, so $x$ and $y$ have the same dimension. Let $X_g$ and $Y_g$ be the matrices of $g$. If $\deg g \neq 0$, the traces of $X_g$ and $Y_g$ are equal.

Let $\deg g = 0$. For $i \geq 1$, $\deg(g \varphi^i) = i \neq 0$, so $\operatorname{tr}(X_g X_\varphi^i) = \operatorname{tr}(Y_g Y_\varphi^i)$. Let $Q = \chi_{X_\varphi} \chi_{Y_\varphi} = \sum_i c_i T^i$, the product of the characteristic polynomials. Then $Q(X_\varphi) = 0$ and $Q(Y_\varphi) = 0$ by Cayley-Hamilton, so
$$\sum_i c_i \operatorname{tr}(X_g X_\varphi^i) = 0 = \sum_i c_i \operatorname{tr}(Y_g Y_\varphi^i).$$
The terms with $i \geq 1$ are equal, so $c_0 \operatorname{tr} X_g = c_0 \operatorname{tr} Y_g$. Here $c_0 = \pm \det X_\varphi \det Y_\varphi \neq 0$. So $\operatorname{tr} X_g = \operatorname{tr} Y_g$ for all $g$. Then $\operatorname{tr} X_g^k = \operatorname{tr} Y_g^k$ for all $k$, and in characteristic $0$ the traces of the powers determine the characteristic polynomial. $\square$

### Away from $\ell$ and above $\ell$

**Lemma 3.22.5 (Toral components away from $\ell$).** Assume the local inputs and item 2 of Definition 3.18.2 at places $u \nmid \ell$. Let $\pi$, $r$, $A$ over $w$, $\sigma$, $\xi$ and $a$ be as in [Theorem 3.22.3](/entry/exists-sph-lift-of-toral/), and let $w \nmid \ell$. Then $\mathrm{WD}_w(r)$ has zero monodromy and $\operatorname{charpol}_g \mathrm{WD}_w(r) = \prod_j (X - \xi_j(a(g)))$ for all $g \in W_A$. If also $\sigma^\circ$ is plain toral, then $\mathrm{WD}_w(r) = \mathrm{rc}(\sigma^\circ)$ for every reciprocity map $\mathrm{rc}$ that satisfies the laws of [the local reciprocity step](/step/is-rect-def/).

Lean: `GalTw.GlobalTheory.RoadU.toralGal_of_holds` (also `GlobalTheory.RoadU.ToralGal`, `GalTw.GlobalTheory.RoadU.away_eq_of_plainTor`).

*Proof.* Let $\deg g \neq 0$ and take $M$, $u$, $P$ and $B$ from [Theorem 3.22.3](/entry/exists-sph-lift-of-toral/). Since $\ell \notin w$, also $u \nmid \ell$. The restriction $r|_{G_M}$ is attached to $P$, because $P$ is a lift of $\pi$. Item 2 of Definition 3.18.2 at $u$ gives the Frobenius eigenvalues of $r|_{G_M}$ at $u$ in terms of $B$, and $r|_{G_M}$ is unramified at $u$. So $\mathrm{WD}_u(r|_{G_M}) = \mathrm{WD}^{\mathrm{sat}}_u(B)$, which has zero monodromy. The Weil-Deligne representation of $r|_{G_M}$ at $u$ is the restriction of $\mathrm{WD}_w(r)$. Restriction to an open subgroup keeps the monodromy and the characteristic polynomials of common elements. So $\mathrm{WD}_w(r)$ has zero monodromy. Since $g$ fixes $M$, it is an element $g'$ of the Weil group at $u$, and item 3 of the theorem gives $\operatorname{charpol}_g \mathrm{WD}_w(r) = \prod_j (X - \xi_j(a(g)))$.

The sum $y$ of the characters $\xi_j \circ a$ has the same polynomial at every $g$. So $\mathrm{WD}_w(r)$ and $y$ have equal polynomials at all $g$ of nonzero degree, and the last lemma gives them at all $g$.

Let $\sigma^\circ$ be plain toral, with unlinked support $\{\xi_j\}$ of size $1$ members. By the exhaustion of the local Langlands correspondence and the theorem of Zelevinsky, $\sigma^\circ$ comes from a multisegment with a support that equals $\{\xi_j\}$, by the uniqueness of supports. The laws of $\mathrm{rc}$ then give that $\mathrm{rc}(\sigma^\circ)$ has zero monodromy and $\operatorname{charpol}_g \mathrm{rc}(\sigma^\circ) = \prod_j (X - \xi_j(a(g)))$. Two Weil-Deligne representations with zero monodromy and equal characteristic polynomials at all $g$ are equal. $\square$

**Lemma 3.22.6 (Toral components above $\ell$).** Assume the local inputs and item 2 of Definition 3.18.2 at places $u \mid \ell$. Let $\pi$, $r$, $A$ over $w$, $\sigma$, $\xi$ and $a$ be as in [Theorem 3.22.3](/entry/exists-sph-lift-of-toral/), and let $w \mid \ell$. Then for all comparison data, $r$ is potentially semistable at $w$, $\mathrm{WD}_w(r)$ has zero monodromy, and $\operatorname{charpol}_g \mathrm{WD}_w(r) = \prod_j (X - \xi_j(a(g)))$ for all $g \in W_A$. If $\sigma^\circ$ is plain toral, then $r$ is de Rham at $w$ with Hodge-Tate jumps $\mathrm{HT}(\tau)$ at each $\tau$ that induces $w$.

Lean: `GalTw.GlobalTheory.RoadU.toralAbove_of_holds` (also `GalTw.GlobalTheory.DeRhamOfPlainTorus.deRham_of_plainTor`).

*Proof.* Let $\deg g \neq 0$ and take $M$, $u$, $P$ and $B$ from [Theorem 3.22.3](/entry/exists-sph-lift-of-toral/). The local component of $P$ at $u$ has Satake parameters, so it is spherical. Item 2 of Definition 3.18.2 at $u$ gives that $r|_{G_M}$ is crystalline at $u$. A crystalline representation is semistable, so it is potentially semistable, and potential semistability descends from $D_A(M)$ to $D_A(E)$. The Weil-Deligne representation at $u$ is the restriction of the one at $w$, and the crystalline property gives zero monodromy at $u$, so at $w$. The Frobenius clause of item 2 gives $\operatorname{charpol}_{g'} \mathrm{WD}_u(r|_{G_M}) = \operatorname{charpol}_{g'} \mathrm{WD}^{\mathrm{sat}}_u(B)$, and item 3 of the theorem gives the product at $g$. The last lemma extends the equality to all $g$, as in the lemma away from $\ell$.

For the de Rham statement, take $g = \varphi$, a Frobenius element. The de Rham clause of item 2 at $u$ gives that $r|_{G_M}$ is de Rham at $u$ with Hodge-Tate jumps given by the infinitesimal character of $P$. The de Rham property descends from $M_u$ to $E_w$. By item 2 of the definition of a lift, the infinitesimal character of $P$ at an embedding of $M$ is that of $\pi$ at its restriction to $E$. So the jumps at an embedding $\tau$ of $E$ are $\mathrm{HT}(\tau)$. $\square$

### The two theorems

**Theorem 3.22.7 (Compatibility for plain toral components, with the local inputs).** If the local inputs hold and the spherical Galois row holds, then compatibility for plain toral components holds.

Lean: `GalTw.GlobalTheory.DeRhamOfPlainTorus.galoisCompat_unlinkedSupport_of_spherical`.

*Proof.* Let $\sigma^\circ$ be plain toral. Its supports have members of size $1$, so we can write an unlinked support as $\{\xi_1, \dots, \xi_n\}$ with smooth characters $\xi_j$ of $E_w^\times$. Take a valuation ring $A$ over $w$ and a local Artin map $a$ at $A$; both exist.

If $w \nmid \ell$, item 1 of Definition 3.17.3 is the last statement of the lemma away from $\ell$, applied with the unramified part of the spherical Galois row.

Let $w \mid \ell$. The de Rham statement is the last statement of the lemma above $\ell$. Fix comparison data. The lemma above $\ell$ gives potential semistability and zero monodromy. For a reciprocity map $\mathrm{rc}$ with the laws of the local reciprocity step, the laws hold with some local Artin map $a$. The lemma gives $\operatorname{charpol}_g \mathrm{WD}_w(r) = \prod_j (X - \xi_j(a(g)))$, and the argument at the end of the lemma away from $\ell$ gives the same polynomial for $\mathrm{rc}(\sigma^\circ)$. This is item 2 of Definition 3.17.3. $\square$

**Corollary 3.22.8 (Compatibility for plain toral components).** If the spherical Galois row holds, then compatibility for plain toral components holds.

Lean: `UpperTheory.Gal.ToralGalois.galoisCompat_unlinkedSupport_of_spherical`.

*Proof.* The local inputs hold. Apply [Theorem 3.22.7](/entry/de-rham-of-plain-torus-galois-compat-unlinked-support-of-spherical/). $\square$

This corollary is the first step of the proof of [the Galois row from the spherical Galois row](/entry/rest/), together with Theorem 3.17.12.

**Remark 3.22.9 (Formalization).** The corollary in [GaloisCompatUnlinkedSupportOfSpherical.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/GaloisCompatUnlinkedSupportOfSpherical.lean#L10) is the theorem applied to `inq_holds`, which pairs `Inp.inp_holds` with `GamX.charLiftPrime_holds`. The lemmas away from and above $\ell$ call the spherical lift through `GlobalTheory.T.frobenius_charpoly_of_unlinked_unramified_support` in [FrobeniusCharpolyOfUnlinkedUnramifiedSupport.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/ToralDeRham/FrobeniusCharpolyOfUnlinkedUnramifiedSupport.lean#L57), a copy of the statement whose proof is a `first | exact ...` wrapper. The de Rham part calls `exists_sph_lift_of_toral` directly. The same kind of wrapper is at [WeaklyAttachedToralOfCmLift.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/ToralDeRham/WeaklyAttachedToralOfCmLift.lean#L101) and [FrobeniusCharpolyEqSatakeOfPlaceAbove.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/ToralDeRham/FrobeniusCharpolyEqSatakeOfPlaceAbove.lean#L102). The construction of $M$ is `exists_cm_lift_fix_charKer`, and the computation at $u$ is `hasSat_charPol_above`; we opened both proofs. We did not open the proofs of the solvable extension lemmas, of the cyclic base change `upWeak`, of `window`, of `hasSat_of_unlinked_unr`, or of the descent lemmas `deRham_descends`, `jumps_descend` and `isPstAt_of_resTo`; for these steps the text follows their statements only.
