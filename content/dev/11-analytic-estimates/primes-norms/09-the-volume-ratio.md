---
title: The volume ratio of hermitian spaces
decls:
  - GlobalTheory.VolRatioFromSecondClause.volumeRatio
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The volume ratio of hermitian spaces

This section computes the ratio of the volumes of two hermitian spaces over a CM field whose ranks differ by one. Let $W$ have rank $M \geq 3$ and the same signature at every real place. Then $W$ contains a vector $x$ of length $\pm 1$, and the volume of $x^\perp$ divided by the volume of $W$ is $c(M)^f\,|d_F|^{1/2 - M}/L_\eta(M)$. Here $c(M) = (2\pi)^M/(M-1)!$ is the mass of the unit sphere of Section 7, and $L_\eta(M)$ is an Euler product over the primes of $E$. The proof assumes one clause of the Siegel-Weil formula, for the theta series of one vector. It combines that clause with [the unfolding identity](/entry/unfolding/) of Section 8 and [the measures at the real places](/entry/real-place-measures/) of Section 7. The result is the volume clause of [the record of hypotheses](/step/hyps-alt-def/), which is used in [the step on the characters of the literature](/step/every-character-of-literature/). For background see [Siegel's mass formula and Tamagawa measures](/learn/hermitian-lattices/#siegels-mass-formula-and-tamagawa-measures).

### The setting

We use the setting of Section 8. So $F$ is a totally real field of degree $f$, and $E/F$ is a CM extension that is unramified at all finite places, with complex conjugation $z \mapsto \bar{z}$ and a CM type $\Psi$ of $f$ embeddings. A hermitian space $W$ over $E$ has a nondegenerate [[Hermitian form|8NJ7XY6F1S]] $h$, a basis, a self-dual $\mathcal{O}_E$-lattice $L_0$ and a recorded signature $\mathrm{sig}(\tau)$ for each embedding $\tau : E \to \mathbb{C}$. We say that $W$ *has signature $(P, Q)$* if, for every $\tau$, the recorded signature is $(P, Q)$ and the matrix of $h$ under $\tau$ has $P$ positive and $Q$ negative eigenvalues. A compact dual normalization $(\mu_{P,Q})$ of Haar measures on the groups $U(P, Q)$ is fixed, and the normalized Haar measures on $U(W)(\mathbb{A})$ are those of Section 8.

The setting also contains a function $W \mapsto \mathrm{vol}(W) > 0$ on hermitian spaces. It is otherwise arbitrary. It is tied to the groups by the following condition.

**Definition 2.9.1 (Volume tie).** The function $\mathrm{vol}$ is *tied to the measures* if, for every hermitian space $W$ of signature $(P, Q)$, a normalized Haar measure $\mu$ on $U(W)(\mathbb{A})$ exists, a fundamental domain $\mathcal{F}$ for $U(W)(F)$ exists, and $\mu(\mathcal{F}) = \mathrm{vol}(W)$ for every normalized $\mu$ and every fundamental domain $\mathcal{F}$.

Put $v = |d_E|^{1/[E:\mathbb{Q}]}/2$, where $d_E$ is the [[discriminant|3BCYVS9E17]] of $E$. For a prime $\mathfrak{P}$ of $E$ with norm $N\mathfrak{P}$ put
$$e_M(\mathfrak{P}) = \begin{cases} \bigl(1 - (-1)^M (N\mathfrak{P})^{-M/2}\bigr)^{-1} & \text{if } \bar{\mathfrak{P}} = \mathfrak{P}, \\ \bigl(1 - (N\mathfrak{P})^{-M}\bigr)^{-1/2} & \text{if } \bar{\mathfrak{P}} \neq \mathfrak{P}, \end{cases}$$
and $L_\eta(M) = \prod_{\mathfrak{P}} e_M(\mathfrak{P})$. Group the primes of $E$ by the prime $\mathfrak{p}$ of $F$ below them, and let $q$ be the norm of $\mathfrak{p}$. The factor of an inert $\mathfrak{p}$ is $(1 - (-q)^{-M})^{-1}$, and the product of the two factors of a split $\mathfrak{p}$ is $(1 - q^{-M})^{-1}$.

**Definition 2.9.2 (One-vector Siegel-Weil formula).** Let $E/F$ be a CM extension and $J$ a nondegenerate hermitian $M \times M$ matrix over $E$, with unitary group $H = U(J)$. The *one-vector Siegel-Weil formula* $\mathrm{SW}_1(E, J)$ says the following. Let $M \geq 3$ and $\beta \in F^\times$. Let $\Phi = \Phi_\infty \cdot \Phi_f$ be a function on $(\mathbb{A}_F \otimes_F E)^M$ with values in $[0, \infty]$, with $\Phi_\infty$ measurable and $\Phi_f = \bigotimes_v \Phi_v$ a pure tensor of real nonnegative local factors. Then for some character $\psi$ of $\mathbb{A}_F/F$, and for every such character, the following holds for every Haar measure $\mu$ on $H(\mathbb{A})$, every fundamental domain $\mathcal{F}$ for $H(F)$ and every choice of self-dual measures for $\psi$ at all places. Fibre measures $\mu_{\infty, t}$ and $\mu_{v, t}$ of the self-dual measures over the level sets $\{X : h(X, X) = t\}$ exist, and for all such families the product $\prod_v \int \Phi_v\, d\mu_{v,\beta}$ converges and
$$\frac{1}{\mu(\mathcal{F})}\int_{\mathcal{F}} \sum_{\substack{0 \neq y \in E^M \\ h(y, y) = \beta}} \Phi(g^{-1}y)\, d\mu(g) = \int \Phi_\infty\, d\mu_{\infty, \beta} \cdot \prod_v \int \Phi_v\, d\mu_{v, \beta}.$$

For $\Phi_f$ the characteristic function of a lattice, the factor at $v$ is the local density of the lattice at $\beta$; see [local densities](/learn/hermitian-lattices/#local-densities). The formula is a special case of the Siegel-Weil formula for the dual pair $(U(1), U(M))$, in the convergent range. In this chapter it is a hypothesis, not a theorem.

### The inputs

Besides Sections 7 and 8, the proof uses four results that are proved elsewhere in the development.

**Theorem 2.9.3 (Unit vectors with a self-dual complement).** Let $W$ have rank $M \geq 3$ and signature $(P, Q)$. Let $\varepsilon = 1$ and $P \geq 1$, or $\varepsilon = -1$ and $Q \geq 1$, and let $(P', Q')$ be $(P - 1, Q)$ or $(P, Q - 1)$ respectively. Then there are $x \in W$ with $h(x, x) = \varepsilon$, a self-dual lattice $L$ with $x \in L$, a hermitian space $W'$ of rank $M - 1$ and signature $(P', Q')$, and an isometric embedding $\iota : W' \to W$ with image $x^\perp$, such that $\iota(L_0') = L \cap x^\perp$ and $L = \mathcal{O}_E x \oplus (L \cap x^\perp)$.

Lean: `GlobalTheory.UnitPerpObj.unitVectorPerp`.

**Theorem 2.9.4 (Volume of isometric spaces).** If $\mathrm{vol}$ is tied to the measures, then $\mathrm{vol}(W_1) = \mathrm{vol}(W_2)$ for every isometry $W_1 \to W_2$ of hermitian spaces of the same signature, whether or not it carries the lattice of $W_1$ to the lattice of $W_2$. The formal statement has two more clauses, on the transport of normalized measures and of fundamental domains along an isometry; they are not used here.

Lean: `GlobalTheory.VolIndepClosed.volIndep`.

**Theorem 2.9.5 (Local densities of a self-dual lattice).** Let $\psi$ be a character of $\mathbb{A}_F/F$, let $v$ be a finite place at which $E$ is unramified and the dual of $\mathcal{O}_v$ for $\psi_v$ is commensurable with $\mathcal{O}_v$, let $L_v$ be a self-dual lattice of rank $M \geq 1$ over $\mathcal{O}_{E,v}$, and let $\beta \in F_v$ be a unit. Then for the self-dual measures of $\psi_v$, the fibre measure of $\{X \in L_v\}$ over $\beta$ is
$$\delta_v = n_v^{1/2 - M}\bigl(1 - \eta_v^M q_v^{-M}\bigr),$$
where $q_v$ is the order of the residue field, $\eta_v = -1$ if $E \otimes F_v$ is a field and $\eta_v = 1$ otherwise, and $n_v = [\mathcal{O}_v^\vee : \mathcal{O}_v]/[\mathcal{O}_v : \mathcal{O}_v^\vee]$, a ratio of generalized indices, for the dual $\mathcal{O}_v^\vee$ of $\mathcal{O}_v$ for $\psi_v$.

Lean: `GlobalTheory.LatticeDensityClosed.selfDualLatticeDensity`.

**Theorem 2.9.6 (Euler product of the densities).** Let $E/F$ be a CM extension unramified at all finite places, and $M \geq 2$. Then $|d_F| = (2v)^f$, the product $L_\eta(M)$ converges to a positive number, and there is a character $\psi$ of $\mathbb{A}_F/F$ whose archimedean component is the standard character $x \mapsto e^{2\pi i\,\mathrm{Tr}(x)}$. Let $\psi$ be a character of $\mathbb{A}_F/F$ and $a \in F^\times$ with $\psi_\infty(x) = e^{2\pi i\,\mathrm{Tr}(ax)}$. Then all $n_v$ are finite and the $\delta_v$ are positive, the product of the $\delta_v$ converges absolutely to a positive number, and
$$|N_{F/\mathbb{Q}}(a)|^{M - 1/2}\prod_v \delta_v = \frac{(2v)^{f(1/2 - M)}}{L_\eta(M)}.$$
The formal statement also contains two clauses on the characters of $\mathbb{A}_F/F$ and on the different, which we do not use.

Lean: `GlobalTheory.DensityProductClosed.eulerProductOfDensities`.

For orientation: the factor $1 - \eta_v^M q_v^{-M}$ is the proportion of vectors of length $\beta$ in a hermitian space of dimension $M$ over the residue algebra $\mathcal{O}_{E,v}/\mathfrak{p}_v$. The factors $n_v^{1/2 - M}$ multiply to $|d_F|^{1/2 - M}$, because the different of $F$ is the conductor of the standard character.

### The theorem

**Theorem 2.9.7 (Volume ratio).** Assume $\mathrm{SW}_1(E, J)$ for every CM extension $E/F$, every $M$ and every nondegenerate hermitian $M \times M$ matrix $J$. Let the setting be given, and let $\mathrm{vol}$ be tied to the measures. Let $W$ be a hermitian space of rank $M \geq 3$ and signature $(P, Q)$. Let $\varepsilon = 1$ and $P \geq 1$, or $\varepsilon = -1$ and $Q \geq 1$. Then there are $x \in W$ with $h(x, x) = \varepsilon$, a hermitian space $W'$ with signature $(P - 1, Q)$ if $\varepsilon = 1$ and $(P, Q - 1)$ if $\varepsilon = -1$, and an isometric embedding $\iota : W' \to W$ with image $x^\perp$, such that
$$\frac{\mathrm{vol}(W')}{\mathrm{vol}(W)} = \left(\frac{(2\pi)^M}{(M - 1)!}\right)^{f} \frac{\bigl((2v)^{f}\bigr)^{1/2 - M}}{L_\eta(M)}.$$

Lean: `GlobalTheory.VolRatioFromSecondClause.volumeRatio`.

*Proof.* Put $c = c(M) = (2\pi)^M/(M-1)!$.

Step 1 (the vector). The theorem on unit vectors gives $x$, $L$, $W'$ and $\iota$ with the properties in the statement. Let $W_1$ be the space $W$ with the lattice $L$ in place of $L_0$. The identity map $W \to W_1$ is an isometry, so the theorem on isometric spaces gives $\mathrm{vol}(W) = \mathrm{vol}(W_1)$. So it is enough to prove the formula with $W_1$ in place of $W$. From now on we write $W$ for $W_1$ and $L_0$ for $L$. Then $x \in L_0$, and the lattice of $W'$ is $\iota^{-1}(L_0)$, which is the setting of the unfolding theorem.

Step 2 (the volumes). By the volume tie there are normalized Haar measures $\mu$, $\mu'$ and fundamental domains $\mathcal{F}$, $\mathcal{F}'$ for $U(W)$ and $U(W')$, and $\mu(\mathcal{F}) = \mathrm{vol}(W)$ and $\mu'(\mathcal{F}') = \mathrm{vol}(W')$. Both are finite.

Step 3 (the archimedean test function). By the measures at the real places, applied at each $\tau \in \Psi$ with the compact dual normalization, there are a measurable function $\Phi_\infty \geq 0$ on $W \otimes F_\infty$ and a real number $a$ with $0 < a < \infty$ with two properties. First, $\int \Phi_\infty\, d\mu_{\infty, \varepsilon} = a$ for every family of fibre measures of the self-dual measure at infinity. Second, the archimedean orbit integral of $\Phi_\infty$ at $x$, in the sense of Section 8, is $c^{-f}a$. The second property is the formula $(\ast)$ of Section 7, taken over the $f$ places in $\Psi$. Each place gives the factor $c(P + Q)^{-1} = c^{-1}$.

Step 4 (the Siegel-Weil formula). Let $J$ be the Gram matrix of $W$, and take $\beta = \varepsilon$, which is a unit at every place. Take $\Phi_v$ the characteristic function of $L_{0,v}$, and $\Phi = \Phi_\infty \cdot \bigotimes_v \Phi_v$. Choose $\psi$ with the standard archimedean component, as in the theorem on the Euler product. By $\mathrm{SW}_1(E, J)$ and the theorem on local densities,
$$\frac{1}{\mathrm{vol}(W)} \int_{\mathcal{F}} \sum_{\substack{y \in W \\ h(y, y) = \varepsilon}} \Phi(g^{-1}y)\, d\mu(g) = a \cdot p, \qquad p = \prod_v \delta_v.$$
Here the sum over $y \in E^M$ in the coordinates of the basis is the sum over the vectors of $W$, and $y \neq 0$ is automatic since $h(y, y) \neq 0$.

Step 5 (unfolding). By the unfolding theorem, the integral on the left is $\mathrm{vol}(W') \cdot I$, where $I$ is the archimedean orbit integral of $\Phi_\infty$ at $x$. By Step 3, $I = c^{-f}a$. So
$$\frac{\mathrm{vol}(W')\, c^{-f}\, a}{\mathrm{vol}(W)} = a\, p.$$

Step 6 (the algebra). Since $0 < a < \infty$, we can divide by $a$, and get $\mathrm{vol}(W')/\mathrm{vol}(W) = c^f p$. By the theorem on the Euler product with $a = 1$, $p = (2v)^{f(1/2 - M)}/L_\eta(M)$. $\square$

The constant $(2v)^f$ equals $|d_E|^{1/2}$, and it equals $|d_F|$ because $E/F$ is unramified at all finite places. In the standard notation $L_\eta(M)$ is the partial L-value $L(M, \eta^M)$ of the quadratic character $\eta$ of $E/F$: it is $\zeta_F(M)$ for $M$ even and $L(M, \eta)$ for $M$ odd. The theorem is the step from rank $M - 1$ to rank $M$ of the mass formula for unitary groups. Iterated down to small rank, it gives the volume of $U(W)$ as a product of special values $L(k, \eta^k)$ for $k \leq M$, times powers of $|d_F|$ and $2\pi$, as in the [mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups).

**Remark 2.9.8 (Formalization).** The theorem is stated in [VolumeRatio.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/VolumeRatio.lean#L14) and proved by `GlobalTheory.VolRatioUnfold.volumeRatio_of_unfolding` ([VolumeRatioOfUnfolding.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/VolumeRatioOfUnfolding.lean#L393)), which takes the six inputs as hypotheses. Steps 2 to 6 are the lemma `GlobalTheory.VolRatioUnfold.ratio_of_setting`, Step 3 is the lemma `arch` of the same file, the theorem on local densities is used in the form of the lemma `local_value` derived from `SelfDualLatticeDensity`, and Step 6 is `ratio_of_eq`. The hypothesis $\mathrm{SW}_1$ is [`SW1b2`](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLattice.lean#L75); it is not proved in this chapter. The conclusion `MassRatioUnderVolume D` is the implication `VolTie D → VolumeRatio₂ D` ([MassRatioUnfoldedOfTheoremTwo.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/MassRatioUnfoldedOfTheoremTwo.lean#L12)), and `VolumeRatio₂` is defined in [ThickPlacesCorollaryOfAnyTranslate.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/ThickPlacesCorollaryOfAnyTranslate.lean#L2330). The setting is the structure `Formalism.BasicNotions.D7`, in which `vol` is a positive function with no other property; the volume tie `VolTie` ([StandardLattice.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLattice.lean#L258)) is the only link between `vol` and the groups. The quantifiers "for some and for every" on $\psi$, on $\mu$ and on $\mathcal{F}$ are the predicate `AllSome`. The theorem on isometric volumes is used through its third clause `VolEqOfIsometric`, and the condition $|d_F| = (2v)^f$ is a clause of `EulerProductOfDensities`. Two callers use the theorem: `GlobalTheory.VolRatioFromSiegelWeil.volumeRatio`, which supplies $\mathrm{SW}_1$ from `SiegelWeilUnitaryConvergent`, and `CompanionTheory.HU.hU_of`, which takes it as the hypothesis `SiegelOneAll`.

## Notes and references

The chapter has two parts. The first part gives lower bounds for primes in short intervals and in arithmetic progressions. [The short interval norm theorem](/entry/short-norm/) of Volume 8 is the theorem of Section 3, and the relative error for primes in progressions of Section 6 gives [the theorem on the recursive selection](/entry/rec-s/) in Volume 7. Both enter [the step on the characters of the literature](/step/every-character-of-literature/). The second part gives the volume ratio of Section 9, which is the volume clause of [the record of hypotheses](/step/hyps-alt-def/) and enters the same step. Sections 1 to 3 follow the classical method for primes in short intervals: a zero-free region, a zero density estimate and a lower bound for an exceptional zero. Here they are applied to an axiomatic family of L-functions of the ray class group, and the dependence on the modulus is polynomial. Sections 4 to 6 follow Gallagher's proof of the log-free zero density estimate and its use in Linnik's theorem. Sections 7 to 9 follow Siegel's proof of the mass formula by the comparison of a space with the orthogonal complement of one vector, in Weil's adelic form, for unitary groups.

- H. Davenport, *Multiplicative Number Theory*, Chapters 13, 14, 16, 19, 20, 21 and 22.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*, Chapters 5, 7, 10 and 18.
- P. X. Gallagher, *A large sieve density estimate near σ = 1*, Invent. Math. 11 (1970).
- D. A. Cox, *Primes of the Form x² + ny²*, §§7 to 9.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, Chapter XXII.
- C. L. Siegel, *Über die analytische Theorie der quadratischen Formen*, Ann. of Math. 36 (1935).
- H. Braun, *Zur Theorie der hermitischen Formen*, Abh. Math. Sem. Hansischen Univ. 14 (1941).
- A. Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965).
- I. G. Macdonald, *The volume of a compact Lie group*, Invent. Math. 56 (1980).
- A. Ichino, *A regularized Siegel-Weil formula for unitary groups*, Math. Z. 247 (2004).
