---
title: Constant terms at split places
decls:
  - GlobalTheory.LeviDesc.twistedOrbitalIntegral_parabolic_unfolding
  - GlobalTheory.T.twistedOrbitalIntegral_parabolic_unfold_levi
  - GlobalTheory.LeviDesc.orbInt_descent
  - GlobalTheory.T.twisted_orbital_integral_levi_constant_term
  - GlobalTheory.BCT.SplitCtMatch.match_ctMu_of_isSplitAt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Constant terms at split places

This section gives the transfer of test functions at a place that splits in the CM field. At such a place the unitary group is $\mathrm{GL}_n$, and the endoscopic group $\mathrm{U}(a) \times \mathrm{U}(b)$ becomes the Levi subgroup $\mathrm{GL}_a \times \mathrm{GL}_b$. The transfer of a function on $\mathrm{GL}_n$ is its constant term along the block upper triangular parabolic, multiplied by a character. The proof is the descent formula for orbital integrals: the orbital integral of the constant term at an element of the Levi subgroup is the orbital integral on $\mathrm{GL}_n$, multiplied by the square root of a discriminant ratio. With [the inert places](/entry/match-principal-congruence-inert/), this gives matching test functions at all finite places, which are used in the comparison of trace formulas on the way to the step [every character](/step/every-character/). For the background, see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module) and [Haar measure](/learn/analysis/#haar-measure).

### Setting

Let $F$ be a finite extension of $\mathbb{Q}_p$, here the completion $E_w$ of a number field at a finite place, with ring of integers $\mathcal{O}$ and normalized absolute value $|\cdot|$. Let $n = a + b$, $G = \mathrm{GL}_n(F)$ and $K = \mathrm{GL}_n(\mathcal{O})$. Let $P = MN$ be the block upper triangular parabolic subgroup with blocks of sizes $a$ and $b$: $M = \mathrm{GL}_a(F) \times \mathrm{GL}_b(F)$ and $N$ the group of matrices
$$n(X) = \begin{pmatrix} 1 & X \\ 0 & 1 \end{pmatrix}, \qquad X \in M_{a \times b}(F).$$
For $m = (m_1, m_2) \in M$ write $m$ also for the block diagonal matrix. Put $K_M = \mathrm{GL}_a(\mathcal{O}) \times \mathrm{GL}_b(\mathcal{O})$ and $K_P = K \cap P$. Let $dX$ be the Haar measure on $M_{a \times b}(F)$ that gives $M_{a \times b}(\mathcal{O})$ volume $1$.

A function $f$ on $G$ is a *Hecke function* for an open subgroup $K'$ if it has compact support and is bi-$K'$-invariant. For a group $H$ with a compact open subgroup $K_H$, the orbital integral $O^H_h$ is the one of [the inert places section](/entry/kap-orb-congruence-eq-kap-sum/) with trivial twist and with $K_H$ as the compact subgroup. For a function $f$ on $G$ let $\bar f(x)$ be the average of $f(k^{-1} x k)$ over $k \in K$.

**Definition 2.9.1 (Constant term).** For a function $f$ on $G$ and $m \in M$,
$$f^{(P)}(m) = \delta_P(m)^{1/2} \int_{M_{a \times b}(F)} \bar f\big(m\, n(X)\big)\, dX, \qquad \delta_P(m) = \left|\frac{\det(m_1)^b}{\det(m_2)^a}\right|.$$
Let $Q_1$ and $Q_2$ be the characteristic polynomials of $m_1$ and $m_2$. The element $m$ is *regular* if $Q_1 Q_2$ is separable. For regular $m$ put
$$D(m) = \frac{\mathrm{Res}(Q_1, Q_2)^2}{\det(m_1)^{b}\, \det(m_2)^{a}}.$$

The quantity $D(m)$ is the ratio of the Weyl discriminants of $m$ in $G$ and in $M$. If $x_i$ and $y_j$ are the eigenvalues of $m_1$ and $m_2$, then $D(m) = \prod_{i, j}(x_i - y_j)^2 / (x_i y_j) = \prod_{i, j} (1 - x_i/y_j)(1 - y_j/x_i)$ up to the sign $(-1)^{ab}$, which does not change the absolute value.

### Descent of orbital integrals

**Proposition 2.9.2 (Unfolding along the parabolic).** Let $f$ be a Hecke function on $G$ for some open subgroup, and let $m \in M$ be regular. Then
$$O^P_m\big(\bar f|_P\big) = O^M_m\Big(m' \mapsto \int_{M_{a \times b}(F)} \bar f\big(n(X)^{-1} m'\, n(X)\big)\, dX\Big),$$
where the left side is the orbital integral on $P$ with compact subgroup $K_P$.

Lean: `GlobalTheory.LeviDesc.twistedOrbitalIntegral_parabolic_unfolding` (also `GlobalTheory.T.twistedOrbitalIntegral_parabolic_unfold_levi`, a second name).

*Proof.* The group $P$ is the semidirect product of $M$ and $N$, and $K_P$ is the semidirect product of $K_M$ and $K \cap N$. Since $m$ is regular, its centralizer in $P$ is its centralizer in $M$, a product of tori. The compact part of the centralizer in $P$ consists of block diagonal elements, and the double coset sum is finite on the support of $\bar f$. Write $x \in P$ as $x = n\, m''$ with $n \in N$, $m'' \in M$. The sum over $P_m \backslash P / K_P$ is then a sum over $M_m \backslash M / K_M$ of an integral over $N$, with the same weights. $\square$

**Lemma 2.9.3 (Constant term and the unipotent integral).** Let $f$ be a Hecke function on $G$ for some open subgroup, and $m \in M$ regular. Then
$$f^{(P)}(m) = |D(m)|^{1/2} \int_{M_{a \times b}(F)} \bar f\big(n(X)^{-1} m\, n(X)\big)\, dX.$$

*Proof.* We have $n(X)^{-1} m\, n(X) = m\, n(Y)$ with $Y = X - m_1^{-1} X m_2$. The map $X \mapsto X - m_1^{-1} X m_2$ is linear with eigenvalues $1 - y_j/x_i$, so it is invertible for regular $m$, and its determinant has absolute value $|\mathrm{Res}(Q_1, Q_2)| / |\det m_1|^b$. The change of variables gives
$$\int \bar f(m\, n(Y))\, dY = \frac{|\mathrm{Res}(Q_1, Q_2)|}{|\det m_1|^{b}} \int \bar f\big(n(X)^{-1} m\, n(X)\big)\, dX.$$
Multiply by $\delta_P(m)^{1/2} = |\det m_1|^{b/2} |\det m_2|^{-a/2}$. $\square$

**Theorem 2.9.4 (Descent to the Levi subgroup).** Let $f$ be a Hecke function on $G$, for $K$ or for some open subgroup, and let $m \in M$ be regular. Then
$$O^M_m\big(f^{(P)}\big) = |D(m)|^{1/2}\, O^G_m(f).$$

Lean: `GlobalTheory.LeviDesc.orbInt_descent` (also `GlobalTheory.T.twisted_orbital_integral_levi_constant_term`, a second name).

*Proof.* The values $Q_1$, $Q_2$, $\det m_1$ and $\det m_2$ do not change under conjugation in $M$, so $|D|$ is constant on the class of $m$. By the Lemma, applied at each conjugate, $O^M_m(f^{(P)}) = |D(m)|^{1/2}\, O^M_m(m' \mapsto \int \bar f(n(X)^{-1} m' n(X))\, dX)$. By the Proposition, this is $|D(m)|^{1/2}\, O^P_m(\bar f|_P)$. Finally $G = PK$, $P$ is closed, and the centralizer of $m$ in $G$ lies in $P$, since $m$ is regular. So the orbital integral of $f$ on $G$ with compact subgroup $K$ equals the orbital integral on $P$ of the $K$-average $\bar f$ with compact subgroup $K_P$. $\square$

This is the classical descent formula of Harish-Chandra: with Haar measures normalized by $K$ and $K_M$, $|D^G(m)|^{1/2} O^G_m(f) = |D^M(m)|^{1/2} O^M_m(f^{(P)})$, where $D^G$ and $D^M$ are the Weyl discriminants. Here $D(m) = D^G(m)/D^M(m)$ up to sign.

### Matching at split places

Now let $E$ be a CM field and $w$ a finite place of $E$ that splits over $E^+$. Then the local unitary group is $\mathrm{GL}_n(E_w)$, with maximal compact subgroup $K$; the twist and the norm of [the inert places section](/entry/kap-orb-congruence-eq-kap-sum/) are trivial, the sign $\epsilon_{Q_1}$ is $1$, and the $\kappa$-orbital integral is the sum of the ordinary orbital integrals over the classes with characteristic polynomial $Q_1 Q_2$. A function $f$ on $\mathrm{GL}_n(E_w)$ and a function $\varphi$ on $M$ *match* for a character $\mu$ of $E_w^\times$ if, for all monic $Q_1$, $Q_2$ of degrees $a$, $b$ with $Q_1 Q_2$ separable,
$$SO_{Q_1, Q_2}(\varphi) = \mu\big((-1)^{ab} d\big)\, \left|\frac{\mathrm{Res}(Q_1, Q_2)^2}{d}\right|^{1/2} O^\kappa_{Q_1, Q_2}(f), \qquad d = \big((-1)^a Q_1(0)\big)^b \big((-1)^b Q_2(0)\big)^a,$$
where the left side is the sum of orbital integrals on $M$ over the classes of $(y_1, y_2)$ with characteristic polynomials $Q_1$, $Q_2$. The factor $\mu((-1)^{ab} d)$ is taken to be $0$ when $d = 0$. For $m$ with characteristic polynomials $Q_1$, $Q_2$ we have $d = \det(m_1)^b \det(m_2)^a$.

**Theorem 2.9.5 (Matching of constant terms at split places).** Let $E$ be a CM field, $w$ a finite place that splits over $E^+$, $n = a + b$, and $\mu$ a character of $E_w^\times$. Let $K' \subseteq K$ be an open subgroup and $f$ a Hecke function for $K'$ on $\mathrm{GL}_n(E_w)$. Put
$$\varphi(m) = \mu\big((-1)^{ab} \det(m_1)^b \det(m_2)^a\big)\, f^{(P)}(m).$$
Then $f$ and $\varphi$ match for $\mu$.

Lean: `GlobalTheory.BCT.SplitCtMatch.match_ctMu_of_isSplitAt`

*Proof.* Let $Q_1$, $Q_2$ be monic of degrees $a$, $b$ with $Q_1 Q_2$ separable. If $Q_1(0) = 0$ or $Q_2(0) = 0$, then no invertible matrix has characteristic polynomial $Q_1$, $Q_2$ or $Q_1 Q_2$, so both sides are $0$. Otherwise choose $x_1 \in \mathrm{GL}_a(E_w)$ and $x_2 \in \mathrm{GL}_b(E_w)$ with these characteristic polynomials, for example companion matrices. Since $Q_1$ and $Q_2$ are separable, every pair with characteristic polynomials $Q_1$, $Q_2$ is conjugate to $m = (x_1, x_2)$ in $M$, and every element of $\mathrm{GL}_n(E_w)$ with characteristic polynomial $Q_1 Q_2$ is conjugate to the block diagonal matrix $m$. So both sides are single orbital integrals. The character factor is constant on the class of $m$ and equals $\mu((-1)^{ab} d)$. By the Theorem on descent,
$$SO_{Q_1, Q_2}(\varphi) = \mu\big((-1)^{ab} d\big)\, O^M_m\big(f^{(P)}\big) = \mu\big((-1)^{ab} d\big)\, |D(m)|^{1/2}\, O^G_m(f),$$
and $D(m) = \mathrm{Res}(Q_1, Q_2)^2/d$. $\square$

The theorem holds for every Hecke function, not only for indicators: at a split place the transfer is explicit for the whole Hecke algebra. This is the reason why the comparison needs work only at the inert places, where the transfer of [principal congruence functions](/entry/match-principal-congruence-inert/) comes from the fundamental lemma.

**Remark 2.9.6 (Formalization).** At a split place the formal definitions make the twist and the norm the identity and the sign $\epsilon$ equal to $1$, and the unitary group equal to all of $\mathrm{GL}_n(E_w)$ ([SimpleTwistedTraceFormulaStable.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SimpleTwistedTraceFormulaStable.lean#L95)); the matching theorem uses these four facts at the start of its proof. Its two conjugate self-reciprocal hypotheses are not used, and they hold anyway at a split place ([SplitPlaceTwistedConstantTermMatches.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SplitPlaceTwistedConstantTermMatches.lean#L291)). The names of the Proposition and of the descent Theorem speak of twisted orbital integrals, but both are stated with the trivial twist. The descent Theorem asks that $f$ be a Hecke function for $K$ or for some open subgroup; the first case is contained in the second, and the proof reduces to it at once ([TwistedOrbitalIntegralLeviConstantTerm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwistedOrbitalIntegralLeviConstantTerm.lean#L148)). The block matrix $m\, n(X)$ is built by a function that returns $1$ if the block matrix is not invertible, which never happens here ([IsUnifAt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsUnifAt.lean#L87)). The integral over $N$ is a normalized sum over cosets of the subgroup generated by the integral matrices ([ParP.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ParP.lean#L37)), and the Lemma is a separate result in the file of the descent Theorem ([TwistedOrbitalIntegralLeviConstantTerm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwistedOrbitalIntegralLeviConstantTerm.lean#L108)). The Proposition is proved from a general unfolding result for semidirect products, which we did not unfold ([TwistedOrbitalIntegralParabolicUnfoldLevi.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwistedOrbitalIntegralParabolicUnfoldLevi.lean#L29)). The second names are restatements by `first | exact …`.
