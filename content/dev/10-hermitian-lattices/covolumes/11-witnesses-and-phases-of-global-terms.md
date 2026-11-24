---
title: Witnesses and phases of global terms
decls:
  - GlobalTheory.HL.GlobalWit.global_witnesses
  - GlobalTheory.T.globalHermitianFrames_rational_witnesses_phase
  - GlobalTheory.HL.TermSurj.term_eq_map
  - GlobalTheory.HL.TermSurj.exists_term_of_global
  - GlobalTheory.T.exists_term_of_globalTerm_strongApprox
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Witnesses and phases of global terms

The amplitude of a term is a sum over lattices that are terms at every finite place at once. This section studies such global terms. A local term at a place comes with witnesses: two unipotent isometries that move standard lattices to the term lattice. The first result shows that a global term has witnesses that are rational, that is, global unipotent isometries, and that its phase is the product of the local phases of any choice of local witnesses. The proof uses [strong approximation](/learn/groups/#strong-approximation) for the unipotent groups. The second result shows that two global terms with the same datum differ by a rational unipotent isometry. The third result lifts this to the terms of the double coset sum: every global term with the datum of a given term comes from a term in the same row. These results are used in the [next section](/entry/row-coset-sum-norm-sq/) to write the sum of the term vectors over a row and a double coset as one global amplitude.

**Setting.** Let $F$ be a number field and $E/F$ a quadratic extension with nontrivial automorphism $x \mapsto \bar x$. The places $p$ are the maximal ideals of $\mathcal{O}_F$. At each $p$ let $F_p$ be the completion, $E_p = E \otimes_F F_p$ with its involution, and $\mathcal{O}_p$ the ring of integers of $E_p$. Fix $r, k \ge 0$ and put $n = k + 2r + 1$. For a $\mathcal{O}_E$-lattice $\Lambda$ in $E^n$ let $\Lambda_p$ be the $\mathcal{O}_p$-span of its image in $E_p^n$.

**Definition 2.11.1 (Local Hermitian frames).** A system of local Hermitian frames at $p$ consists of the following data. There is a uniformizer $\varpi$ of $F_p$ and a nondegenerate [Hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) $h$ on $E_p^n$. There are $T, T' \in F_p^\times$, two flag families $f_0, \dots, f_r$ and $f'_0, \dots, f'_r$, and two dual families $e_0, \dots, e_{r-1}$ and $e'_0, \dots, e'_{r-1}$. These satisfy:

1. $h(f_a, f_b) = 0$ unless $a = b = r$, and $h(f_r, f_r) = -T$;
2. $h(f_a, e_j) = 1$ if $a = j$ and $0$ otherwise, and $h(e_i, e_j) = 0$;
3. the same with primes and $T'$;
4. the [[Gram matrix|00SPJSDT3Z]] $h(f'_b, f_a)$ is the matrix of a fixed point $w$ up to the signs $(-1)^{r-b}$, and a quantity built from its leading minors and $T T'$ is nonzero.

There is also a flag $g$. If it is set, then $E_p$ is not a field and $T$, $T'$ are units. Put $\theta = \varpi$ if the flag $g$ is set and $\theta = 1$ otherwise.

Let $X_j$ be the span of $f_0, \dots, f_{j-1}$. The unipotent group $N$ is the group of isometries $n$ of $h$ such that, for each $j < r$, $n$ preserves $X_{j+1}$ and $n v - v \in X_j$ for $v \in X_{j+1}$, and $n$ preserves $X_r^\perp$ and $n v - v \in X_r$ for $v \in X_r^\perp$. The group $N'$ is the same for the primed flag. Fix a character $\psi_0$ of $E_p$. The phase characters are
$$\psi(n) = \psi_0\Big(\theta^{-1} \sum_{j < r} h(n f_{j+1}, e_j)\Big),$$
and $\psi'$ in the same way with primes.

A *datum* is a triple $d = (A, A', \Gamma)$ of two $\mathcal{O}_p$-lattices and a set of pairs of vectors. The lattice $A$ is *inner* for $(f, e)$ if it contains $X_r$, lies in $X_r^\perp$, is self-dual inside $X_r^\perp$, contains $f_r$ with some $y \in A$ such that $h(f_r, y) = 1$, and meets the orthogonal of the $e_j$ in a finitely generated module. The *standard lattice* of $A$ is
$$\operatorname{std}(f, e, A) = \textstyle\sum_{j < r} \mathcal{O}_p f_j + \big(A \cap \{e\}^\perp\big) + \sum_{j < r} \mathcal{O}_p e_j.$$

**Definition 2.11.2 (Local term and witnesses).** Let $d = (A, A', \Gamma)$ be a datum and $\Lambda$ an $\mathcal{O}_p$-lattice. A pair $(n, n')$ is a pair of *witnesses* for the local term $(d, \Lambda)$ if $A$ is inner for $(f, e)$, $A'$ is inner for $(f', e')$, $n \in N$, $n' \in N'$, and
$$\Lambda = n \operatorname{std}(f, e, A) = n' \operatorname{std}(f', e', A'),$$
$n' f'_b - n f_b \in \theta \Lambda$ for every $b \le r$, and $\Gamma$ is the graph set of $\Lambda$. The pair $(d, \Lambda)$ is a *local term* if it has witnesses. Its *local phase* is $\psi(n)\, \psi'(n')^{-1}$ for a chosen pair of witnesses.

The local phase does not depend on the choice of witnesses; this is a result of the local theory of frames.

**Definition 2.11.3 (Global frames and global terms).** A system of global Hermitian frames consists of a Hermitian matrix $H$ over $E$, families $f, f', e, e'$ in $E^n$, scalars $c_p \in F_p^\times$, and local frames $S_p$ at every place, such that: the form of $S_p$ is $H$; $c_p^{r-a} f_{p,a}$ is the image of $f_a$, and $e_{p,a}$ is $c_p^{r-a}$ times the image of $e_a$ (the same with primes); $c_p$ is a unit for almost all $p$; and the flag $g$ of $S_p$ is set for only finitely many $p$. The global group $N$ is the group of $E$-linear maps $x$ of $E^n$ whose image at every $p$ lies in $N_p$; the same for $N'$. A *global datum* is a family $d = (d_p)_p$ of local data. A pair $(d, \Lambda)$ with $\Lambda$ a lattice in $E^n$ is a *global term* if $(d_p, \Lambda_p)$ is a local term at every $p$. Its *global phase* is the product of the local phases,
$$\omega(d, \Lambda) = \prod_p \omega_p(d_p, \Lambda_p).$$

**Lemma 2.11.4 (Close witnesses).** Let $(m, m')$ be witnesses for a local term $(d, \Lambda)$, and let $w \in N$ and $w' \in N'$. Assume that $m w^{-1} x - x \in \theta \Lambda$ and $m' w'^{-1} x - x \in \theta \Lambda$ for every $x \in \Lambda$. Then $(w, w')$ are witnesses for $(d, \Lambda)$.

*Proof.* The standard lattice of an inner lattice is self-dual, and $m$ is an isometry, so $\Lambda = m \operatorname{std}(f, e, A)$ is self-dual. Put $u = m w^{-1}$. This is an isometry, and $u x = (u x - x) + x \in \Lambda$ for $x \in \Lambda$, since $\theta \Lambda \subseteq \Lambda$. An isometry that maps a self-dual lattice into itself maps it onto itself: for $y \in \Lambda$ and $x \in \Lambda$, $h(x, u^{-1} y) = h(u x, y)$ is integral, so $u^{-1} y \in \Lambda$. So $u \Lambda = \Lambda$, and $\Lambda = w \operatorname{std}(f, e, A)$. For $z \in \operatorname{std}(f, e, A)$ we have $w z \in \Lambda$, and the hypothesis at $x = w z$ gives $m z - w z \in \theta \Lambda$. The same holds with primes. Each $f_b$ lies in $\operatorname{std}(f, e, A)$: for $b < r$ by definition, and $f_r \in A$ is orthogonal to the $e_j$. So
$$\begin{aligned}
w' f'_b - w f_b = {}& (m' f'_b - m f_b) - (m' f'_b - w' f'_b) \\
&+ (m f_b - w f_b) \in \theta \Lambda.
\end{aligned}$$
The datum and the graph set do not change. $\square$

**Theorem 2.11.5 (Rational witnesses and the phase).** Let $(S_p)$ be global Hermitian frames with $4r + 7 \le k$, and let $(d, \Lambda)$ be a global term. Then:

1. there are $n \in N$ and $n' \in N'$ such that, at every $p$, the images of $n$ and $n'$ are witnesses for $(d_p, \Lambda_p)$;
2. for every family of local witnesses $(m_p, m'_p)$ for $(d_p, \Lambda_p)$,
$$\omega(d, \Lambda) = \prod_p \psi_p(m_p)\, \psi'_p(m'_p)^{-1}.$$

Lean: `GlobalTheory.HL.GlobalWit.global_witnesses` (also `GlobalTheory.T.globalHermitianFrames_rational_witnesses_phase`, a second name).

*Proof.* First, the identity is a witness at almost all places. A lattice in $E^n$ is determined by its localizations, and $\Lambda_p$ is the coordinate lattice at almost all $p$. For $4r + 7 \le k$, at almost all $p$ the coordinate lattice is the unique local term with its datum, with witnesses $(1, 1)$. So the set of places where $(1, 1)$ are not witnesses for $(d_p, \Lambda_p)$ is finite.

At each $p$ choose witnesses $q_p = (q_{p,1}, q_{p,2})$, with $q_p = (1, 1)$ when $(1, 1)$ are witnesses. Then $q_{p,1}^{-1}$ moves $\Lambda_p$ only at finitely many places, and so does $q_{p,2}^{-1}$. The number $\theta_p$ is a unit at almost all places, since the flag $g$ is set only at finitely many places. Strong approximation for the unipotent groups $N$ and $N'$ gives $x \in N$ such that at every $p$ and for every $y \in \Lambda_p$,
$$q_{p,1}(x_p y) - y \in \theta_p \Lambda_p,$$
where $x_p$ is the image of $x$ at $p$, and similarly $x' \in N'$ for $q_{p,2}$. Put $n = x^{-1}$ and $n' = x'^{-1}$. At $p$, the images $m$ of $n$ and $m'$ of $n'$ lie in $N_p$ and $N'_p$, and $m^{-1} = x_p$. So the lemma applies to $(q_{p,1}, q_{p,2})$ and $(m, m')$, and $(m, m')$ are witnesses. This is the first claim.

For the second claim, the local phase does not depend on the choice of witnesses, so $\omega_p(d_p, \Lambda_p) = \psi_p(m_p)\, \psi'_p(m'_p)^{-1}$ at every $p$. Take the product. $\square$

**Theorem 2.11.6 (Global terms with one datum).** Let $4r + 7 \le k$, and let $(d, \Lambda)$ and $(d, \Gamma)$ be global terms with the same datum. Then $\Gamma = x \Lambda$ for some $x \in N$, and $\Gamma = x' \Lambda$ for some $x' \in N'$.

Lean: `GlobalTheory.HL.TermSurj.term_eq_map`.

*Proof.* The previous theorem gives rational witnesses $(n_0, n'_0)$ for $(d, \Lambda)$ and $(n_1, n'_1)$ for $(d, \Gamma)$. Let $m_0, m_1$ be the images of $n_0, n_1$ at $p$. Then $\Lambda_p = m_0 \operatorname{std}(f, e, A_p)$ and $\Gamma_p = m_1 \operatorname{std}(f, e, A_p)$ with the same inner lattice $A_p$, since the datum is the same. So $\Gamma_p = m_1 m_0^{-1} \Lambda_p$, and $m_1 m_0^{-1}$ is the image of $n_1 n_0^{-1}$. A lattice in $E^n$ is determined by its localizations, so $\Gamma = n_1 n_0^{-1} \Lambda$ with $n_1 n_0^{-1} \in N$. The same argument with $n'_0, n'_1$ gives $x' = n'_1 n'^{-1}_0 \in N'$. $\square$

Now we pass to the terms of the double coset sum. Let $D$ be a datum with words $u$ and $u'$ that satisfy the standing hypotheses, with $4r + 7 \le k$. A term $t$ of the double coset sum of $(u, u')$ has a lattice $\lambda_t$ for $u$, a lattice $\lambda'_t$ for $u'$, a linear isometry $\ell_t$ with $\ell_t \lambda'_t = \lambda_t$, and a row. Let $N(F_u)$ and $N(F_{u'})$ be the rational isometries that are unipotent along the flags of $u$ and $u'$. Fix a point $w$, base flags $F_{00}$ and $F'_0$ with Gram matrix given by $w$ and nonzero $G$-value, local frame pairs at the finite places that sit at the base and are relevant, global frames $(S_p)$ for these, and global coordinates for them. The coordinates attach to an isometry $\rho$ and a lattice $\lambda$ a lattice $\operatorname{lat}(\rho, \lambda)$ in the frame space, and they identify $N(F_u)$ and $N(F_{u'})$ with $N$ and $N'$. Let $t_0$ be a term, and let $\rho$ move the frame of $t_0$ to the base flags, up to unitriangular matrices. Let $d_0$ be the datum of $\operatorname{lat}(\rho, \lambda_{t_0})$.

**Theorem 2.11.7 (Global terms come from terms in the row).** In this setting, let $\Gamma$ be a lattice such that $(d_0, \Gamma)$ is a global term. Then there are a term $t$ and isometries $n \in N(F_u)$, $m \in N(F_{u'})$ such that $t$ has the row of $t_0$,
$$\ell_t = n^{-1} \ell_{t_0} m, \qquad \Gamma = \operatorname{lat}(\rho n, \lambda_t).$$

Lean: `GlobalTheory.HL.TermSurj.exists_term_of_global` (also `GlobalTheory.T.exists_term_of_globalTerm_strongApprox`, a second name).

*Proof.* The global coordinates have these properties: an isometry lies in $N(F_u)$ if and only if its image lies in $N$, and the same for $N(F_{u'})$ and $N'$; $\operatorname{lat}(\rho n, \lambda)$ is the image of $\operatorname{lat}(\rho, \lambda)$ under the image of $n$; every element of $N$ and of $N'$ is such an image; and $\operatorname{lat}(\sigma, \cdot)$ is injective. The moved lattice $\Lambda_0 = \operatorname{lat}(\rho, \lambda_{t_0})$ is a global term with datum $d_0$. Since $\ell_{t_0} \lambda'_{t_0} = \lambda_{t_0}$, also $\Lambda_0 = \operatorname{lat}(\rho \ell_{t_0}, \lambda'_{t_0})$.

By the previous theorem, $\Gamma = x \Lambda_0$ with $x \in N$ and $\Gamma = x' \Lambda_0$ with $x' \in N'$. Lift $x$ to $n \in N(F_u)$ and $x'$ to $m \in N(F_{u'})$. Then
$$\Gamma = \operatorname{lat}(\rho n, \lambda_{t_0}) = \operatorname{lat}(\rho \ell_{t_0} m, \lambda'_{t_0}).$$
Put $\gamma = n^{-1} \ell_{t_0} m$. Then $\operatorname{lat}(\rho n, \gamma \lambda'_{t_0}) = \operatorname{lat}(\rho n, \lambda_{t_0})$, so $\gamma \lambda'_{t_0} = \lambda_{t_0}$ by injectivity. The map $\gamma$ is an isometry, as a product of isometries. A lemma on local terms shows that $\gamma$ gives an admissible integral frame, so $\gamma$ defines an element of the double coset carrier of the pair of lattices $(\lambda_{t_0}, \lambda'_{t_0})$. Let $t$ be its term. The representative of its class is $\ell_t = a \gamma b$ with $a$ and $b$ in the rational unipotent stabilizers of $\lambda_{t_0}$ and $\lambda'_{t_0}$. So
$$\ell_t = (n a^{-1})^{-1} \ell_{t_0} (m b),$$
with $n a^{-1} \in N(F_u)$ and $m b \in N(F_{u'})$. Since $a$ fixes $\lambda_{t_0}$, we have $\operatorname{lat}(\rho n a^{-1}, \lambda_t) = \operatorname{lat}(\rho n, \lambda_{t_0}) = \Gamma$. Finally, two terms in this position have the same row if and only if the data of their moved lattices agree. The datum of $\Gamma$ is $d_0$, because the datum of a local term is determined by its lattice. So $t$ has the row of $t_0$. $\square$

**Remark 2.11.8 (Formalization).** The local frames are the structure `GlobalTheory.HL.Frames` and the witnesses are `IsTermW` ([ComplementReferenceCompactSubgroup.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean#L121)); the global frames, `IsTerm` and the phase `om` are in [GFrames.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/GFrames.lean#L58). The global phase is a `finprod`, so it is $1$ if infinitely many local phases differ from $1$; the second claim of the theorem compares two `finprod`s place by place. The lemma is `isTermW_of_close` and the finiteness of the bad places is `good_places` ([GlobalHermitianFramesRationalWitnessesPhase.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/GlobalHermitianFramesRationalWitnessesPhase.lean#L155)), which uses `numberField_lattice_determined_by_local_lattices` and `coordinateLattice_unique_term_almost_all_places`; the hypothesis $4r + 7 \le k$ enters only there. Strong approximation is `strong_approximation_unipotent_alt`, and witness independence is `WitIndep.witness_independence`. The last theorem uses `rational_unipotent_groups_lattices_global_coordinates`, `movedTermLattice_isGlobalTerm_phase`, `exists_admissible_integralFrame_of_localTerms` and `termRow_eq_iff_movedLatticeInnerData_eq`. The term $t$ is built by hand as a quotient class `Quot.mk _ p`, and `rel_of_eqv` extracts the elements $a$ and $b$ from the equivalence generated by the double coset relation. The second names are wrappers of the form `first | exact @X | exact X | ...`.
