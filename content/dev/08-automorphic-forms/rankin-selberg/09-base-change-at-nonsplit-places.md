---
title: Base change at non-split places
decls:
  - UpperTheory.Gal.InertialTypesAlt.L.elemPairJ_holds
  - UpperTheory.Gal.InertialTypesAlt.G.core
  - UpperTheory.Gal.InertialTypesAlt.G.varTrace
  - UpperTheory.Gal.Join.liftGood
  - UpperTheory.Gal.Desc.speh
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Base change at non-split places

This section is not about Rankin-Selberg integrals. It has the local inputs of [Base change keeps Satake parameters at ramified places](/entry/ram-sph/) for cyclic [base change](/learn/automorphic-forms/#base-change), and one statement about base change from unitary groups. The chain is a matching of Iwahori double cosets, a twisted trace identity, an identity of traces on [Jacquet modules](/learn/representations/#cuspidal-representations-and-segments), and the base change of principal series. It goes through `ramSph` and `quadLift` to the step [EveryCharacter](/step/every-character/).

Throughout, $F$ and $E$ are totally complex number fields, $E/F$ is Galois of prime degree $\ell$, and $\sigma$ generates $\mathrm{Gal}(E/F)$. Let $v$ be a finite place of $F$ that does not split in $E$. Since $\ell$ is prime, exactly one place $w$ lies over $v$, and it is inert or ramified. Write $k = F_v$, $k' = E_w$, $G = \mathrm{GL}_n(k)$ and $G' = \mathrm{GL}_n(k')$. Let $\sigma_w$ be the automorphism of $k'$ that $\sigma$ induces, acting on $G'$ entry by entry, and let $N \colon k'^\times \to k^\times$ be continuous with $N(x) = \prod_{i < \ell} \sigma_w^i(x)$ and $|N(x)|_k = |x|_{k'}$ (the predicate `IsNorm`). Let $T$ be the diagonal torus, $U$ the upper unipotent group, and $\nu$ the multiplicative valuation on $k$ or $k'$.

**Definition 8.9.1 (Matching).** For $\delta \in G'$ let $\mathcal N \delta = \delta \, \sigma_w(\delta) \cdots \sigma_w^{\ell - 1}(\delta)$. Take Haar measures on $G'$ and $G$ that give $\mathrm{GL}_n$ of the integers volume $1$. A function $\varphi$ on $G'$ and a function $f$ on $G$ *match with constant* $c \in \mathbb{C}$ if, for each $\gamma \in G$ with separable characteristic polynomial and each Haar measure on its centralizer, two conditions hold. First, for every $\delta$ with $\mathcal N \delta = \gamma$, the twisted orbital integral of $\varphi$ at $\delta$ is $c$ times the orbital integral of $f$ at $\gamma$. Second, if no such $\delta$ exists, the orbital integral of $f$ at $\gamma$ is $0$.

The predicate is `GM.MatchAt`. The *norm set* of $G$ is the set of $g$ with $\eta_v(\det g) = 1$ for every [Hecke character](/learn/class-field-theory/#hecke-characters) $\eta$ of $F$ that is trivial on norms from $E$.

**Definition 8.9.2 (Iwahori levels and exponents).** A $t \in T(k)$ is *dominant* if $\nu(t_1) \le \dots \le \nu(t_n)$, and *strictly dominant* if the inequalities are strict. A compact open subgroup $K$ of $G$ is an *Iwahori level* if $K = (K \cap U)(K \cap T)(K \cap U^-)$, and if $t (K \cap U) t^{-1} \subseteq K$ and $t^{-1} (K \cap U^-) t \subseteq K$ for every dominant $t$. Let $e_K(t)$ be the indicator function of $K t K$. For a smooth representation $\tau$ of $G$, a character $\mu$ of $T(k)$ is an *exponent* of $\tau$ if some nonzero vector of the Jacquet module $\tau_U$ is an eigenvector of $T(k)$ with character $\mu$.

**Definition 8.9.3 (Twisted trace).** Let $\tau'$ be an irreducible smooth representation of $G'$ and $I$ a linear bijection with $I \tau'(g) = \tau'(\sigma_w g) I$. A test function $\varphi$ on $G'$ has *twisted trace* $z$ if the operator $\tau'(\varphi) \circ I$ has finite trace $z$. The ordinary trace of $\tau(f)$ is the case $I = 1$.

The four theorems on $\mathrm{GL}_n$ share these hypotheses: $\pi$ is a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_F)$ and $\Pi$ one of $\mathrm{GL}_n(\mathbb{A}_E)$; $\Pi \circ g \cong \Pi$ for all $g \in \mathrm{Gal}(E/F)$; $\Pi$ is a weak base change of $\pi$, that is, the [Satake parameters](/learn/representations/#unramified-representations) agree after the power map at almost all places; and $\tau$, $\tau'$ are the local components $\pi_v$, $\Pi_w$.

**Theorem 8.9.4 (Matching of Iwahori double cosets).** Let $U' \subseteq G'$ and $U_0 \subseteq G$ be open subgroups. There are Iwahori levels $K' \subseteq U'$ and $K \subseteq U_0$, with $K'$ stable under $\sigma_w$, a constant $c \neq 0$ and a strictly dominant $t_0 \in T(k')$, such that for every dominant $t \in T(k')$ the function $e_{K'}(t_0 t)$ matches $e_K(N(t_0 t))$ with constant $c$, and $K \, N(t_0 t) \, K$ lies in the norm set.

Lean: `UpperTheory.Gal.InertialTypesAlt.L.elemPairJ_holds`.

*Proof.* The theorem is `elemPairJ` applied to `elemPair`. The statement `elemPair` says: for every radius $r < 1$ there are $r_0 < 1$ and, for $r' \le r_0$, a $c > 0$ such that, for every strictly dominant $t$, the indicator of the set $r$-near $t$ in $G'$ matches the indicator of the set $r'$-near the norms of that set, and the second set lies in the norm set. It comes from `matchOne`, `elemLoc` and `normLoc`. The steps of `elemPairJ` are as follows.

1. The data of the place give a generator $s$ of $\mathrm{Gal}(k'/k)$. A private lemma shows $\sigma_w = s$, and so $N$ is the field norm $\mathrm{N}_{k'/k}$.
2. Pick $r$ so small that the $r$-ball about $1$ lies in $U'$ and $\mathrm{diag}(N(u)) \in U_0$ for $u \in T(k')$ that is $r$-near $1$. Apply `elemPair`, and pick $r' \le r_0$ with the $r'$-ball in $U_0$.
3. The $r$-ball is an Iwahori level $K'$, and $e_{K'}(t)$ is the indicator of the set $r$-near $t$. It is stable under $\sigma_w$, which keeps the valuation. `levOf` gives a level $K \subseteq U_0$ with $e_K(N t)$ equal to the second indicator.
4. For a strictly dominant $t_0$ and dominant $t$, $t_0 t$ is strictly dominant, and `elemPair` applies. $\square$

**Theorem 8.9.5 (Twisted trace identity, carried case).** Assume also that $\Pi$ is carried by a direct summand of the $L^2$ space of the norm-one quotient of $\mathrm{GL}_n$ over $E$. Let $s$ and $I$ be as in the twisted trace. There is $c \neq 0$ with this property: if $\varphi$ and $f$ are test functions that match with constant $c_1$, $f$ is supported in the norm set, and $\mathrm{tr}\, \tau(f) = z$, then the twisted trace of $\varphi$ on $\tau'$ is $c \, c_1 \, z$.

Lean: `UpperTheory.Gal.InertialTypesAlt.G.core`.

*Proof.* The proof compares the twisted trace formula over $E$ with the trace formula over $F$, and cancels all places except $v$.

1. `pickS` gives a finite set $S$ of places with $v \in S$ and a split place $q \notin S$, with $w_0$ above $q$. `tyEx` gives a compact open subgroup and a character at each place, and a nonzero vector of the summand that transforms by them.
2. Let $t_y$ be the trace, twisted when $y$ does not split, of the type function at $y \in S$; at $v$ it is taken on $\tau'$ with $I$. Each $t_y$ is nonzero. Let $r$ be the twisted trace of $\varphi$.
3. At $w_0$, `unitTrace`, `fd_fixed` and `iwPow` give a nonempty multiset $Z_0$ of nonzero numbers such that the trace of the $j$-th Iwahori Hecke operator is the power sum $p_j(Z_0) = \sum_{z \in Z_0} z^j$.
4. For each small level at $v$ there are numbers $B_j$, which do not depend on $\varphi$ and $f$, such that $c_E \, p_j(Z_0) \prod_{y \ne v} t_y \cdot r = B_j \, c_1 z$ for all large $j$. Here $c_E \neq 0$ comes from `termEV`, and $B_j$ from `sideSum`, `fibTrace` and `ci`.
5. `matchCut` restricts the reference function at $v$ to the norm set, and `trEx` gives its trace $z_0$. Apply step 4 to $(\varphi, f)$ and to the reference pair. By `powNe`, $p_j(Z_0) \neq 0$ for infinitely many $j$. At such a $j$, divide the two identities. This gives $r \cdot c_v z_0 = t_v \cdot c_1 z$, with $c_v z_0 \neq 0$.
6. So $c = t_v / (c_v z_0)$ works. We have not unfolded `termEV`, `sideSum`, `fibTrace` or `ci`. $\square$

**Theorem 8.9.6 (Twisted trace identity).** The twisted trace identity holds without the assumption that $\Pi$ is carried by a summand.

Lean: `UpperTheory.Gal.InertialTypesAlt.G.varTrace`.

*Proof.* `exTwist` gives $z_0 \in \mathbb{C}$ such that $\Pi \otimes |\cdot|_E^{z_0}$ is carried by a summand. With $\chi = |\cdot|_F^{z_0}$ and $\chi' = |\cdot|_E^{z_0}$, `powTwist` and `weakPow` show that $\Pi \otimes \chi'$ is a Galois-invariant weak base change of $\pi \otimes \chi$, and `locTw` gives the local components $\tau \otimes \chi_v$ and $\tau' \otimes \chi'_w$. By `matchPow`, matching commutes with these twists. Apply the carried case to the twisted data and undo the twist with `trTw`. $\square$

**Lemma 8.9.7 (Trace identity on Jacquet modules).** There is a nonzero $A$ with $A \tau'(g) = \tau'(\sigma_w g) A$, with this property. For all open $U'$ and $U_0$ there are Iwahori levels $K' \subseteq U'$ and $K \subseteq U_0$, with $K'$ stable under $\sigma_w$, a constant $c \neq 0$ and $t_0$, such that for every dominant $t$
$$\mathrm{tr}\big(t_0 t \circ A \mid \mathrm{im}\, \tau'^{K'}\big) = c \cdot \mathrm{tr}\big(N(t_0 t) \mid \mathrm{im}\, \tau^{K}\big),$$
where $\mathrm{im}\, \tau^K$ is the image of the $K$-fixed vectors in the Jacquet module.

Lean: `UpperTheory.Gal.Join.coreId`.

*Proof.* `varEx` gives $s$ and an intertwiner $I$, and $s$ is the action of $\sigma_w$; take $A = I$. The matching theorem gives $K'$, $K$, $c_1$ and $t_0$. The twisted trace identity, applied to $e_{K'}(t_0 t)$ and $e_K(N(t_0 t))$, gives $c$. `casTrace`, a form of Casselman's theorem, writes the trace of $\tau(e_K(t))$ through the trace of $t$ on $\mathrm{im}\, \tau^K$; the modulus factors on the two sides agree by `normDom`. Divide by the volumes of $K$ and $K'$. $\square$

**Lemma 8.9.8 (Exponents of the lift).** If $\mu$ is an exponent of $\tau$, then $\mu \circ N$ is an exponent of $\tau'$.

Lean: `UpperTheory.Gal.Join.liftExp`.

*Proof.* Take the lemma above with $U' = G'$ and $U_0$ a level that fixes an eigenvector for $\mu$. Both traces are sums of characters of $T$, and $\mu \circ N$ occurs on the right. By `charDom` (independence of characters on the dominant cone) and `twExp`, $\tau'$ has an exponent invariant under $\sigma_w$, and `expSub` puts $\tau'$ in a principal series $I(\omega')$ with $\omega'$ invariant. Then `locDesc_holds` makes the trace of $t \circ A$ a nonzero multiple of the trace of $t$, and `charDom` again puts $\mu \circ N$ among the exponents of $\tau'$. $\square$

**Theorem 8.9.9 (Base change of principal series).** If $\tau$ is a subquotient of the principal series $I(\omega_1, \dots, \omega_n)$ for smooth characters $\omega_i$ of $k^\times$, then $\tau'$ is a subquotient of $I(\omega_1 \circ N, \dots, \omega_n \circ N)$.

Lean: `UpperTheory.Gal.Join.liftGood`.

*Proof.* The theorem takes the trace identity on Jacquet modules as a hypothesis. A private lemma shows that $\tau$ has the exponent $\omega_{p(1)} \otimes \dots \otimes \omega_{p(n)}$ for some permutation $p$. By the lemma on exponents, $\tau'$ has the exponent $(\omega_{p(i)} \circ N)_i$. By `expSub`, $\tau'$ is a subquotient of $I(\omega')$ with this exponent, and since a character of $T$ determines its components, $\omega'_i = \omega_{p(i)} \circ N$. `subPerm` removes the permutation. $\square$

The term `ramSph` is `ramSphOf locGal (liftGood (coreId varEx varTrace elemPairJ_holds))`. There $w$ is ramified and $Nw = Nv$, so each $\omega_i \circ N$ is unramified with the same value at a uniformizer.

The last theorem is of another kind. Let $E$ be a CM field such that $E/E^+$ is unramified at all finite places, and let $\mathrm{U}(n)$ be the unitary group of the standard Hermitian form, with adelic points in $\mathrm{GL}_n(\mathbb{A}_E)$. For an irreducible representation $\rho$ of $\mathrm{GL}_a(E_w)$ and $d \ge 1$, let $\mathrm{Speh}(\rho, d)$ be the representation of $\mathrm{GL}_{da}(E_w)$ that the predicate `IsSpeh` describes. For $\rho$ cuspidal it is the unique irreducible quotient of $\rho|\cdot|^{(d-1)/2} \times \dots \times \rho|\cdot|^{(1-d)/2}$.

**Theorem 8.9.10 (Speh form of base change from unitary groups).** Let $\pi$ be an automorphic representation of $\mathrm{U}(n)$, $n \ge 1$. There are positive integers $a_i, d_i$, $1 \le i \le c$, with $\sum_i d_i a_i = n$, conjugate self-dual cuspidal representations $P_i$ of $\mathrm{GL}_{a_i}(\mathbb{A}_E)$, and unitarisable local representations $\sigma_{i,w} = \mathrm{Speh}(P_{i,w}, d_i)$, such that:

1. at each place $w$ split over $E^+$, $\pi_w$ is the product of the $\sigma_{i,w}$;
2. at each place $w$ inert over $E^+$ where $\pi$ is unramified, the base change of the Satake parameters of $\pi$ is the union over $i$ and $0 \le k < d_i$ of the Satake parameters of $P_{i,w}$ times $q_w^{(d_i - 1)/2 - k}$;
3. the infinitesimal characters add up in the same Speh pattern to the one given by the weight of $\pi$, and the pairs $(d_i, P_i)$ are distinct.

Lean: `UpperTheory.Gal.Desc.speh`.

*Proof.* The term is `BaseChangeIdentities.speh` applied to [`baseChangeNB`](/entry/base-change-nb/). The proof `bcSpeh_of` makes the local products irreducible (`definiteN_of`), and then applies `AscComp`, which writes each discrete automorphic summand of $\mathrm{GL}_N$ as a Speh representation of a cuspidal one, as in Mœglin and Waldspurger. $\square$

**Remark 8.9.11 (Formalization).** The predicates `Dom`, `IwLev`, `IsExp`, `ForInert`, `ElemPairJ`, `CoreId` and `LiftGood` are in [ElemPairJ.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/JacobianTraceQuotients/ElemPairJ.lean#L19), and `Match` is in [IsNormAlong.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/SelmerRankBounds/IsNormAlong.lean#L45). `ForInert` assumes only that $v$ does not split, so the "inert" names also cover ramified places. `elemPairJ_holds` is a one-line term in [ElemPairJHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/FrobeniusLocalPairs/ElemPairJHolds.lean#L12). The proof `core` is at [line 94 of FdFixed.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/PowerMatchingTraces/FdFixed.lean#L94); it has 260 lines and `maxHeartbeats 1600000`. `varTrace` is in [VarTrace.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/PowerMatchingTraces/VarTrace.lean#L20). `liftGood` and `liftExp` are in [TorusCharComp.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/JacobianTraceQuotients/TorusCharComp.lean#L109) and take `CoreId` as a hypothesis, which only [QuadLift.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/QuadLift.lean#L10) discharges. `speh` is a one-line term in [BcBackOffT.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/BaseChangeDescent/BcBackOffT.lean#L24), and `BcSpeh` is in [IsUnitarisableTrivChar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsUnitarisableTrivChar.lean#L37).

## Notes and references

Cyclic base change for $\mathrm{GL}_n$ and the matching of orbital integrals are due to Arthur and Clozel ([base change](/learn/automorphic-forms/#base-change)). Jacquet modules are in Bernstein and Zelevinsky, and the residual spectrum of $\mathrm{GL}_n$ is in Mœglin and Waldspurger. The theory of [Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals) and [local factors](/learn/representations/#generic-representations-and-local-factors) in the earlier sections is in Jacquet, Piatetski-Shapiro and Shalika, Jacquet and Shalika, and Shahidi, and in Cogdell's lectures. The Schur functions of the unfolding are in Macdonald. The [local Langlands correspondence](/learn/galois-representations/#the-local-langlands-correspondence) and its characterization by epsilon factors of pairs are in Henniart, Harris and Taylor, and Scholze; the classification by segments is in Zelevinsky.

- J. Arthur and L. Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*, Ann. of Math. Stud. 120, Princeton University Press, 1989.
- I. N. Bernstein and A. V. Zelevinsky, Induced representations of reductive p-adic groups I, Ann. Sci. École Norm. Sup. 10 (1977), 441-472.
- J. W. Cogdell, Lectures on L-functions, converse theorems, and functoriality for $\mathrm{GL}_n$, in *Lectures on Automorphic L-functions*, Fields Inst. Monogr. 20, Amer. Math. Soc., 2004.
- M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Ann. of Math. Stud. 151, Princeton University Press, 2001.
- G. Henniart, Caractérisation de la correspondance de Langlands locale par les facteurs $\varepsilon$ de paires, Invent. Math. 113 (1993), 339-350.
- G. Henniart, Une preuve simple des conjectures de Langlands pour GL(n) sur un corps p-adique, Invent. Math. 139 (2000), 439-455.
- H. Jacquet, I. I. Piatetski-Shapiro and J. A. Shalika, Rankin-Selberg convolutions, Amer. J. Math. 105 (1983), 367-464.
- H. Jacquet and J. A. Shalika, On Euler products and the classification of automorphic representations I, Amer. J. Math. 103 (1981), 499-558; II, 777-815.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press, 1995.
- C. Mœglin and J.-L. Waldspurger, Le spectre résiduel de GL(n), Ann. Sci. École Norm. Sup. 22 (1989), 605-674.
- P. Scholze, The local Langlands correspondence for $\mathrm{GL}_n$ over p-adic fields, Invent. Math. 192 (2013), 663-715.
- F. Shahidi, On certain L-functions, Amer. J. Math. 103 (1981), 297-355.
- A. V. Zelevinsky, Induced representations of reductive p-adic groups II, Ann. Sci. École Norm. Sup. 13 (1980), 165-210.
