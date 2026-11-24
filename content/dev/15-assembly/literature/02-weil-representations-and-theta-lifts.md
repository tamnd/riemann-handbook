---
title: Weil representations and theta lifts
decls:
  - UpperTheory.LiteratureTheorems.kudla_splitting_split_unitary_of_literature
  - UpperTheory.LiteratureTheorems.howe_duality_real_of_literature
  - UpperTheory.LiteratureTheorems.cuspidal_mirabolic_of_literature
  - GlobalTheory.T.theta_lift_general_linear
  - UpperTheory.Lit.Mix.gl_thetaLift_isClosed
  - UpperTheory.Lit.HoweDuality.thetaLift_gl_of_zelevinsky_classification
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weil representations and theta lifts

This section states the inputs on the [[theta correspondence|6WB6TKE70H]] that the proof takes from the literature: Kudla's splitting of the Weil representation for a split unitary group over a $p$-adic field, Howe duality at the archimedean places in the Fock model, Gelfand's description of cuspidal representations of $\mathrm{GL}_n$ over a finite field restricted to the mirabolic subgroup, and Mínguez's computation of the theta lift for the pair $(\mathrm{GL}_r, \mathrm{GL}_{r+t})$ over a $p$-adic field. The first three are fields of the bundle of [local theta inputs](/step/published-results-first/). The fourth is the only result of the chapter that is proved, from three other published theorems. It is used where local components of a global theta lift are matched with products of characters. Background is in [the Weil representation](/learn/theta/#the-weil-representation), [splitting characters](/learn/theta/#splitting-characters) and [the local theta correspondence](/learn/theta/#the-local-theta-correspondence).

### Kudla's splitting

Let $F$ be a non-archimedean local field of characteristic $0$, and let $E / F$ be a quadratic extension with Galois conjugation $c$ and with norm $N$. Let $\eta$ be the quadratic character of $F^\times$ attached to $E / F$. For a finite set $\nu$ let $J_\nu = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ on $E^\nu \oplus E^\nu$, and let $U(J_\nu)$ be its [[unitary group|0R9R0Y1HDK]]. It is split, of rank $|\nu|$. For $a \in \mathrm{GL}_\nu(E)$ let $m(a)$ be the element of the Siegel Levi subgroup that acts by $a$ on the first summand. For a Hermitian matrix $Q$ of size $\alpha$, the group $U(J_\nu)$ acts on $\mathcal{S}(M_{\alpha \times \nu}(E))$ through the Heisenberg group of $Q \otimes J_\nu$ and a character $\psi$ of $F$.

**Theorem 1.2.1 (Kudla).** Let $Q$ be a Hermitian matrix of size $\alpha$ over $E$. Let $\psi$ be a nontrivial continuous unitary character of $F$, and let $\chi : E^\times \to S^1$ be a continuous character with $\chi|_{F^\times} = \eta^{|\alpha|}$. Then there is a representation $\omega$ of $U(J_\nu)$ on the space $\mathcal{S}(M_{\alpha \times \nu}(E))$ of locally constant functions of compact support with these properties.

1. $\omega$ is smooth.
2. $\omega(g)$ preserves the $L^2$ norm for every Haar measure on $M_{\alpha \times \nu}(E)$.
3. For every $g$ and every $w \in M_{\alpha \times 2\nu}(E)$, the operators of the Heisenberg group satisfy $\rho(w) \, \omega(g) = \omega(g) \, \rho(w g)$.
4. For $a \in \mathrm{GL}_\nu(E)$ and $\varphi \in \mathcal{S}(M_{\alpha \times \nu}(E))$,

$$\omega(m(a)) \varphi (x) = \chi(\det a) \, |N(\det a)|_F^{|\alpha| / 2} \, \varphi(x a).$$

Lean: `UpperTheory.LiteratureTheorems.kudla_splitting_split_unitary_of_literature`.

The theorem says that the metaplectic cover of $U(J_\nu)$ splits over $U(J_\nu)$, with a splitting fixed by the character $\chi$. This is Kudla, *Splitting metaplectic covers of dual reductive pairs* (Israel J. Math. 87, 1994), for the split unitary group in the Schrödinger model.

*Proof.* We take the result from Kudla. In the development it is [Theorem 1.4.4 of Volume 12](/entry/kudla-splitting-split-unitary/). $\square$

### Howe duality at the archimedean places

Let $E / F$ be a CM extension of number fields. Let $X$ be a nondegenerate Hermitian space of dimension $n$ over $E$, and $W$ a nondegenerate skew-Hermitian space of dimension $d$. Fix a standard additive character $\psi$ of $\mathbb{A}_F / F$ and two Hecke characters $\chi_X, \chi_W$ of $E$ whose restrictions to $\mathbb{A}_F^\times$ are $\eta^n$ and $\eta^d$. Let $\omega$ be the Weil representation of $U(X) \times U(W)$ defined by these data, and fix a Cartan involution of each archimedean group. Let $\mathcal{P}$ be the space of polynomial vectors in the Fock model at the archimedean places. Call a subspace $N \subseteq \mathcal{P}$ a *theta submodule* if it is stable under the derived action of $U(W)_\infty$, stable under its maximal compact subgroup, and if every derivative along $U(X)_\infty$ and every difference $\omega(k) f - f$ with $k$ in the maximal compact subgroup of $U(X)_\infty$ lies in $N$.

**Theorem 1.2.2 (Howe duality, archimedean).** In this setting, the strictly increasing chains of theta submodules of $\mathcal{P}$ have bounded length. The sum of two proper theta submodules is proper.

Lean: `UpperTheory.LiteratureTheorems.howe_duality_real_of_literature`.

In the standard form (Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2, 1989) the theorem says that for each irreducible Harish-Chandra module $\pi$ of one member of the pair, the maximal $\pi$-isotypic quotient of $\mathcal{P}$ has a unique irreducible quotient. The two conclusions above are the finiteness and the uniqueness parts of this statement, written as a statement on the lattice of submodules.

*Proof.* We take the result from Howe. In the development it is [Theorem 1.5.10 of Volume 12](/entry/howe-duality-real-holds/). $\square$

### Cuspidal representations over a finite field

Let $k$ be a finite field and $n \geq 0$. A representation $\rho$ of $\mathrm{GL}_{n+1}(k)$ is *cuspidal* if, for every proper standard block parabolic subgroup, no nonzero vector is fixed by its unipotent radical. The mirabolic subgroup $P_{n+1}$ is the group of matrices whose last row is $(0, \dots, 0, 1)$. Let $U_{n+1} \subset P_{n+1}$ be the upper unitriangular matrices. For a nontrivial character $\psi_0$ of $k$, put $\theta(u) = \psi_0(u_{1,2} + u_{2,3} + \dots + u_{n,n+1})$. This is a generic character of $U_{n+1}$.

**Theorem 1.2.3 (Gelfand).** Let $k$ be a finite field and $n \geq 0$.

1. There is an irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$ on a finite-dimensional complex space.
2. Let $\psi_0$ be a nontrivial character of $k$. Let $\rho$ be an irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$ on a finite-dimensional complex space. Then the restriction of $\rho$ to $P_{n+1}$ is isomorphic to $\mathrm{Ind}_{U_{n+1}}^{P_{n+1}} \theta$.

Lean: `UpperTheory.LiteratureTheorems.cuspidal_mirabolic_of_literature`.

Part 1 follows from Green's construction of the cuspidal representations from regular characters of $\mathbb{F}_{q^{n+1}}^\times$. Part 2 is due to S. I. Gelfand (Mat. Sb. 1970). It is the finite-field form of the Gelfand-Kazhdan theory of the Kirillov model. See [cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments).

*Proof.* We take both parts from the literature. In the development they are [Theorem 1.6.4 of Volume 8](/entry/cuspidal-mirabolic-holds/). $\square$

### The theta lift for $(\mathrm{GL}_r, \mathrm{GL}_{r+t})$

Let $k$ be a non-archimedean local field with absolute value $|\cdot|$, and let $r, n \geq 0$. Let $\mu$ be a character of $k^\times$. The group $\mathrm{GL}_r(k) \times \mathrm{GL}_n(k)$ acts on $\mathcal{S}(M_{n \times r}(k))$ by

$$\begin{aligned}
(\omega_\mu(g, h) \Phi)(x) &= \mu(\det g) \, \mu(\det h)^{-1} \\
&\quad \cdot |\det g|^{n/2} \, |\det h|^{-r/2} \, \Phi(h^{-1} x g).
\end{aligned}$$

**Definition 1.2.4 (Theta pair).** Let $\sigma$ be a representation of $\mathrm{GL}_r(k)$ on $V$ and $\pi$ a representation of $\mathrm{GL}_n(k)$ on $W$. The pair $(\sigma, \pi)$ is a *theta pair* for $\mu$ if there is a nonzero linear map $B : \mathcal{S}(M_{n \times r}(k)) \to \mathrm{Hom}(W, V)$ with

$$B(\omega_\mu(g, h) \Phi)(\pi(h) w) = \sigma(g) \, B(\Phi)(w)$$

for all $g, h, \Phi$ and $w$.

So $B$ is a nonzero $\mathrm{GL}_r(k) \times \mathrm{GL}_n(k)$-equivariant map from $\omega_\mu \otimes \pi$ to $\sigma$. For admissible $\sigma$ and $\pi$ this means that $\sigma \otimes \pi^\vee$ is a quotient of $\omega_\mu$, so $\pi^\vee$ is in the local theta correspondence with $\sigma$, up to the twist by $\mu$.

For representations $\sigma$ of $\mathrm{GL}_r(k)$ and $\tau$ of $\mathrm{GL}_t(k)$, let $\sigma \times \tau$ be the normalised parabolic induction of $\sigma \otimes \tau$ from the standard parabolic subgroup of $\mathrm{GL}_{r+t}(k)$ with Levi factor $\mathrm{GL}_r \times \mathrm{GL}_t$. Let $\mu \circ \det_t$ be the character $h \mapsto \mu(\det h)$ of $\mathrm{GL}_t(k)$. A representation is *unitarisable* if it has a positive definite invariant Hermitian form.

We use three statements from the theory of $p$-adic $\mathrm{GL}_n$.

- (Bernstein-Zelevinsky finiteness.) Irreducible smooth representations are admissible, and the Jacquet functor and parabolic induction preserve finite length and commute with contragredients in the usual way (Bernstein and Zelevinsky).
- (Bernstein.) The product $\sigma_1 \times \sigma_2$ of irreducible unitarisable smooth representations is irreducible (Bernstein, LNM 1041, 1984).
- (Zelevinsky.) The Grothendieck ring of finite-length smooth representations of all $\mathrm{GL}_n(k)$ is the polynomial ring over $\mathbb{Z}$ on the classes of the segment representations (Zelevinsky, Ann. Sci. ÉNS 13, 1980).

**Theorem 1.2.5 (Mínguez).** Assume Bernstein-Zelevinsky finiteness and Bernstein's irreducibility theorem. Let $r < t$, let $\mu$ be a smooth unitary character of $k^\times$, let $\sigma$ be a smooth irreducible unitarisable representation of $\mathrm{GL}_r(k)$, and let $\pi$ be a smooth irreducible representation of $\mathrm{GL}_{r+t}(k)$. If $(\sigma, \pi)$ is a theta pair for $\mu$, then

$$\pi \cong \sigma \times (\mu \circ \det_t).$$

Lean: `GlobalTheory.T.theta_lift_general_linear` (also `UpperTheory.Lit.Mix.gl_thetaLift_isClosed`).

The theorem is a case of Mínguez, *Correspondance de Howe explicite: paires duales de type II* (Ann. Sci. ÉNS (4) 41, 2008). Since $r < t$ we are in the stable range, and the lift of $\sigma$ is the full induced representation, which is irreducible here.

The proof uses Zelevinsky's theorem and the following step.

**Proposition 1.2.6.** In the setting of the theorem, assume Bernstein-Zelevinsky finiteness and Zelevinsky's theorem in place of Bernstein's irreducibility theorem. Then the conclusion holds.

Lean: `UpperTheory.Lit.HoweDuality.thetaLift_gl_of_zelevinsky_classification`.

*Proof.* First, the product $\sigma \times (\mu \circ \det_t)$ is irreducible. This uses the geometric lemma of Bernstein and Zelevinsky for the Jacquet module of a product, the finiteness statements and the structure of the Grothendieck ring. Then we apply [Theorem 2.8.7 of Volume 12](/entry/lift-of-irr/), which proves the isomorphism once the product is known to be irreducible. That argument runs as follows. For $j \leq r$, say that $B$ *vanishes from rank* $j$ if $B(\Phi) = 0$ for every $\Phi$ that is zero on all matrices of rank less than $j$. If $B$ vanishes from rank $j + 1$ and $j < r$, then $B$ vanishes from rank $j$. This step uses $r < t$ and the unitarity of $\sigma$ and $\mu$. The germ of $B$ along the open set of matrices of rank $r$ is given by a linear functional $e$ on $W$, which is unique. If $e = 0$, then $B$ vanishes from rank $r$, and the step, applied $r$ times, gives $B = 0$. So $e \neq 0$. Frobenius reciprocity turns $e$ into a nonzero intertwining map $f : \pi \to \sigma \times (\mu \circ \det_t)$. Both sides are irreducible, so by Schur's lemma $f$ is an isomorphism. $\square$

*Proof of the theorem.* This is the Proposition applied to Zelevinsky's theorem, which holds. The hypothesis of Bernstein's theorem is not used. $\square$

**Remark 1.2.7 (Formalization).** Kudla's splitting, archimedean Howe duality and Gelfand's theorem take the record of open statements as an argument and do not use it. They are the terms `GlobalTheory.kudlaSplittingSplitUnitary`, `GlobalTheory.howeDualityReal_holds` and `GlobalTheory.cuspidalMirabolic_holds` ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L343), lines 343, 437, 449). The statements are at [KudlaSplittingSplitUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/KudlaSplittingSplitUnitary.lean#L223), [HoweDualityReal.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HoweDualityReal.lean#L21) and [BlockTriangularOfSubOne.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/PublishedFoundations/BlockTriangularOfSubOne.lean#L225). We did not unfold the Heisenberg operators `Heisenberg₂`, the Fock model `Model`, the polynomial space `Pol`, or the predicates `IsWeil`, `IsHecke` and `IsCartan`. In the Howe duality statement the Weil representation is a hypothesis, and the Hecke conditions on $\chi_X, \chi_W$ are not used by the proof [HoweDualityRealHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HoweDualityRealHolds.lean#L18). In Gelfand's theorem the cuspidal condition is vacuous for $\mathrm{GL}_1$, so part 1 holds there with any character. The statement of Mínguez's theorem is `ThetaLiftGeneralLinearStatement` ([ThetaLiftGeneralLinearStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftGeneralLinearStatement.lean#L9)). The two finiteness and irreducibility inputs are hypotheses of the implication, not fields of the literature bundle. The proof of the theorem has `set_option maxHeartbeats 1000000` and a `first | exact ... | ...` tactic, where the first branch suffices ([ThetaLiftGeneralLinear.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftGeneralLinear.lean#L7)). The middle theorem only applies the Proposition to `polynomialRing`, a proof of Zelevinsky's theorem; its name says nothing about closed sets ([GlThetaLiftIsClosed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/GlThetaLiftIsClosed.lean#L8)). The Proposition discards the hypothesis of Bernstein's theorem with `_` ([ThetaLiftGlOfZelevinskyClassification.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftGlOfZelevinskyClassification.lean#L10)). Irreducibility of the product comes from `UpperTheory.Lit.Mix.top` ([ImportsAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GeneralLinearGroups/ImportsAlt.lean#L19)). Representations here are plain group representations on complex vector spaces; smoothness is a separate predicate. The normalised induction takes the smooth part of the induced functions ([IsSubquotientDetRepParInd.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/IsSubquotientDetRepParInd.lean#L367)).
