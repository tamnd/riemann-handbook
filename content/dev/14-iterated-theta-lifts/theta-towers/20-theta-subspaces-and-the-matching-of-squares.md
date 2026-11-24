---
title: Theta subspaces and the local matching of squares
decls:
  - GlobalTheory.SquareLM.twisted_square_local_matching
  - GlobalTheory.T.twisted_quotient_real
  - GlobalTheory.RealQuot.twist_quotient_isReal
  - GlobalTheory.T.theta_subspace_kernel_maximal
  - GlobalTheory.SquareAgree.kernel_maximal_theta_subspace
  - GlobalTheory.T.thetaSubspace_eq_ker_projDerivation_of_square
  - GlobalTheory.SquareAgree.exists_ker_projDerivation_thetaSubspace
  - GlobalTheory.T.triple_assembly_inverse_finite
  - GlobalTheory.TripleAssembly.triple_map_comp_inverse_finite
  - GlobalTheory.T.local_action_finite_places
  - GlobalTheory.LocActV.finite_adele_acts_placewise
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta subspaces and the local matching of squares

A square of the grid is a seesaw: two Hermitian spaces $W$ and $W_1$ with $W \oplus W_1$ of the rank of a third space $X$, and two Weil representations, of $U(W) \times U(X)$ and of $U(W_1) \times U(X)$. A match of a square is an irreducible module $\Pi$ with two maps from the algebraic Fock vectors onto $\Pi$. This section proves four facts about matches. The kernel of a match, read on the local Schwartz space, is a maximal theta subspace. The kernel on the second side is a proper theta subspace. The real part of every match is one irreducible quotient of the polynomial Fock space, and every match factors as this real quotient times a finite part. Finally, the theta lift of a matched triple is invariant under the finite points of the first groups, because the finite adeles act place by place. These facts are hypotheses checked in the step [the hypotheses are not empty](/step/nonempty-hyps/), and the factorization feeds the minor matching of [Section 3.11.4](/entry/rallis-bottom-minor-matching/).

We keep the notation of Sections 14 and 15. Let $E/F$ be the CM extension of the datum, $\psi$ a standard character and $\theta$ an admissible family at the real places. Let $W$, $W_1$, $X$ be Hermitian spaces with frames $A$, $A_1$, $B$, and let $\alpha$, $\beta$ be Hecke characters such that $(W, W_1, X, \alpha, \beta)$ is a triple. Let $\omega_A$ and $\omega_B$ be the Weil representations of the two pairs, with the characters of the triple, on functions on $W \otimes X$ and $W_1 \otimes X$. Let $\mathcal F_A$ and $\mathcal F_B$ be the spaces of algebraic Fock functions on the two sides: the spans of the Fock functions $\mathrm{Fock}(f, P)$ of a finite Fock function $f$ and a polynomial $P$ at the real places.

**Definition 3.20.1 (Match).** A match of the triple is a complex vector space $\Pi$ with an action $\rho_f$ of the finite points of $U(X)$ and an action $\rho_l$ of the Lie algebras of $U(X)$ at the real places, and two linear maps $p : \mathcal F_A \to \Pi$ and $p' : \mathcal F_B \to \Pi$, such that: $\Pi \neq 0$ and every subspace stable under $\rho_f$ and $\rho_l$ is $0$ or $\Pi$; $p$ and $p'$ are onto; $p$ and $p'$ are invariant under the finite points of $U(W)$ and $U(W_1)$; and $p$ and $p'$ are equivariant for the finite points and the Lie algebra of $U(X)$.

A match is the global form of a $\Theta$-correspondence: $\Pi$ is a common quotient of the two Weil representations, coinvariant for the first groups. The local side uses a model. Let a local triple consist of a base, a geometry with spaces $V$, $V'$ and a symplectic space, characters and two Weil representations $\omega$, $\omega'$ on the Schwartz space of a Darboux model, and let it lie over the Hermitian data. Let $\mathcal S_{\mathrm{alg}}$ and $\mathcal S'_{\mathrm{alg}}$ be the algebraic vectors of the two models. A local function $\Phi_D$ and a global function $\Phi$ form a datum if $\Phi(c(u)) = \Theta(\rho(u)\Phi_D)$ for every $u$, where $\rho$ is the Heisenberg action, $c$ the identification of coordinates and $\Theta$ the theta sum.

**Definition 3.20.2 (Theta subspace).** A theta subspace of $\mathcal S_{\mathrm{alg}}$ is a subspace $K$ that contains $\omega(g, 1)\Phi_D - \Phi_D$ for every finite point $g$ of $U(V)$ and every $\Phi_D \in \mathcal S_{\mathrm{alg}}$, contains $\omega(k, 1)\Phi_D - \Phi_D$ for every $k$ in the maximal compact subgroup at the real places, contains the vectors annihilated by the line operators of the first group, and is stable under the finite points, the maximal compact subgroup and the line derivatives of the second group.

**Theorem 3.20.3 (The kernel of a match is a maximal theta subspace).** Assume the local inputs. Let a local triple lie over the triple, and let $(\Pi, p, p')$ be a match. Then there is a theta subspace $K \subsetneq \mathcal S_{\mathrm{alg}}$ such that every theta subspace $N \supseteq K$ is $K$ or $\mathcal S_{\mathrm{alg}}$, and for every datum $(\Phi_D, \Phi)$ with $\Phi \in \mathcal F_A$ and $\Phi_D \in \mathcal S_{\mathrm{alg}}$,

$$\Phi_D \in K \iff p(\Phi) = 0.$$

Lean: `GlobalTheory.SquareAgree.kernel_maximal_theta_subspace` (also `GlobalTheory.T.theta_subspace_kernel_maximal`, a second name).

*Proof.* Let $d(\Phi_D)$ be the function $x \mapsto \Theta(\rho(c^{-1}x)\Phi_D)$. Then $(\Phi_D, d(\Phi_D))$ is a datum, every datum has this form, and $d$ is linear. It is injective: a Schwartz function whose theta sums vanish at all Heisenberg translates is $0$. Since the triple lies over the data, $d$ maps $\mathcal S_{\mathrm{alg}}$ into $\mathcal F_A$, and a Schwartz function with $d(\Phi_D) \in \mathcal F_A$ lies in $\mathcal S_{\mathrm{alg}}$. Put

$$K = \{\Phi_D \in \mathcal S_{\mathrm{alg}} : p(d(\Phi_D)) = 0\}.$$

The Weil representations of the model and of the triple agree under $d$, by the transport of the Weil representation. So the invariance of $p$ under the finite points of $U(W)$ puts the relations $\omega(g, 1)\Phi_D - \Phi_D$ into $K$. The equivariance of $p$ for the finite points of $U(X)$ makes $K$ stable under them, and the stability under the compact subgroup and the line derivatives comes from the corresponding lemmas of the local inputs. So $K$ is a theta subspace.

If $K = \mathcal S_{\mathrm{alg}}$, then $p$ vanishes on $\mathcal F_A$, which contradicts $p$ onto $\Pi \neq 0$. Let $N \supseteq K$ be a theta subspace. The image $p(d(N))$ is a subspace of $\Pi$ stable under $\rho_f$ and $\rho_l$, so it is $0$ or $\Pi$. If it is $0$, then $N \subseteq K$, so $N = K$. If it is $\Pi$, then for $\Phi_D \in \mathcal S_{\mathrm{alg}}$ there is $\Psi_D \in N$ with $p(d(\Phi_D)) = p(d(\Psi_D))$, so $\Phi_D - \Psi_D \in K \subseteq N$ and $\Phi_D \in N$. The last claim is the definition of $K$. $\square$

**Theorem 3.20.4 (The kernel on the second side).** Under the same assumptions there is a subspace $N$ of $\mathcal S'_{\mathrm{alg}}$ with

$$N = \{\Phi_{0,D} \in \mathcal S'_{\mathrm{alg}} : \exists\, \Phi_0 \in \mathcal F_B \text{ with } (\Phi_{0,D}, \Phi_0) \text{ a datum and } p'(\Phi_0) = 0\},$$

such that $N$ is a theta subspace for the second model, in the sense of a subspace that is finite in each type and stable under the Lie algebra, the compact subgroup and the stabilizer, and $N \neq \mathcal S'_{\mathrm{alg}}$.

Lean: `GlobalTheory.SquareAgree.exists_ker_projDerivation_thetaSubspace` (also `GlobalTheory.T.thetaSubspace_eq_ker_projDerivation_of_square`, a second name).

*Proof.* Take for $N$ the kernel of the polarization projection of $p'$. Its finiteness and its stability under the Lie algebra, the compact subgroup and the stabilizer are lemmas of the local inputs on the polarization kernel. If $N = \mathcal S'_{\mathrm{alg}}$, take $x \neq 0$ in $\Pi$ and $\Phi_0 \in \mathcal F_B$ with $p'(\Phi_0) = x$. It has a datum $\Phi_{0,D}$, which then lies in $N$, so $p'(\Phi_1) = 0$ for some $\Phi_1$ with the same datum. A datum determines its global function, so $\Phi_1 = \Phi_0$ and $x = 0$, a contradiction. $\square$

The next result is the real part of Howe duality. For a module $Q$ of the Lie algebras with a subspace $C$ of relations, the Howe condition says that the sum of all proper stable subspaces of $Q$ that contain $C$ is again proper. We assume it for the coinvariants of the polynomial Fock spaces at the real places, as a hypothesis of Howe duality at the real places.

**Theorem 3.20.5 (The real quotient).** Assume Howe duality at the real places, the local inputs, the agreement of theta integrals and the local matching. Then for the data $W$, $W_1$, $X$, $A$, $A_1$, $B$ there are a complex vector space $P_r$ of countable dimension, an irreducible action $\rho$ of the Lie algebras of $U(X)$ at the real places on $P_r$, and maps $q$, $q'$ from the polynomial Fock spaces of the two sides onto $P_r$, with this property. Fix exponents $a_\tau$ and $b_\tau$ at the real places $\tau$. For every triple $(\alpha, \beta)$ whose characters have the exponents $a$ and $b$ at the real places, every match $(\Pi, p, p')$ and every finite Fock function $f$ of the first side there is a linear map $\varphi : P_r \to \Pi$ that intertwines $\rho$ with $\rho_l$ and satisfies

$$p(\mathrm{Fock}(f, P)) = \varphi(q(P))$$

for every polynomial $P$; and the same holds on the second side with $q'$ and $p'$.

Lean: `GlobalTheory.RealQuot.twist_quotient_isReal` (also `GlobalTheory.T.twisted_quotient_real`, a second name).

*Proof.* If no triple with these exponents has a match, take $P_r = 0$. Otherwise fix one match $(\Pi_0, p_0, p'_0)$. Let $C$ be the subspace of coinvariant relations of the first group in the polynomial Fock space of the first side, and let $R$ be the sum of all proper subspaces that are stable under the Lie algebras of $U(X)$ and contain $C$. For a finite function $f$, the map $P \mapsto p_0(\mathrm{Fock}(f, P))$ is equivariant, vanishes on $C$ by the invariance of $p_0$, and is not $0$ for some $f$, since $p_0$ is onto. Its kernel is a proper stable subspace that contains $C$, so the Howe condition gives $R \neq$ the whole space. By its definition $R$ is maximal among proper stable subspaces, so $P_r = Q/R$ is irreducible, with $q$ the quotient map. It has countable dimension, since the monomials form a countable basis of the polynomial space. The same construction on the second side gives a second simple quotient, and the two are isomorphic, since both map onto $\Pi_0$ compatibly; this gives $q'$. For an arbitrary match, the theta lifts of $\Pi$ have a stable complement, so $R$ lies in the kernel of $P \mapsto p(\mathrm{Fock}(f, P))$, and this map factors through $q$ as $\varphi$. $\square$

**Theorem 3.20.6 (Local matching of squares).** Assume Howe duality at the real places, the local inputs, the agreement of theta integrals and the local matching. Then the local matching of squares holds: for the data $W$, $W_1$, $X$, $A$, $A_1$, $B$ there are $P_r$ and $q$, $q'$ onto $P_r$ such that every triple $(\alpha, \beta)$ with the exponents $a$ and $b$ matches locally, and for every match $(\Pi, p, p')$ there are a space $\Pi_f$, maps $r$, $r'$ from the finite Fock functions of the two sides onto $\Pi_f$ and a linear map $e$ with

$$p(\mathrm{Fock}(f, P)) = e\bigl(q(P) \otimes r(f)\bigr)$$

for all $f$ and $P$, and the same with $p'$, $q'$, $r'$.

Lean: `GlobalTheory.SquareLM.twisted_square_local_matching`.

*Proof.* Take $P_r$, $\rho$, $q$ and $q'$ from [Theorem 3.20.5](/entry/twist-quotient-is-real/). The local match of each triple is a lemma of the local inputs. The commutant of $\rho$ is $\mathbb C$, by the lemma of Dixmier: an endomorphism $T$ of an irreducible module of countable dimension that commutes with the action is a scalar, since otherwise $\mathbb C(T)$ would be a field of uncountable dimension inside the commutant. So for fixed $f$ the map $\varphi_f$ of the previous theorem is unique up to a scalar, and $f \mapsto \varphi_f$ is linear into $\mathrm{Hom}_\rho(P_r, \Pi)$. The images of the $\mathrm{Fock}(f, P)$ span $\Pi$, since $p$ is onto. The product form of a bilinear map of this kind gives $\Pi_f$, $r$ and $e$. The second side is the same. $\square$

The last two results are about the finite places. Let $\omega$ be one of the two local Weil representations of a local triple. For a place $v$ let $\mathrm{aug}_v(\omega)$ be the augmentation subspace of $\omega$ at $v$, a subspace of the Schwartz-Bruhat space at $v$. A pure tensor is $f \otimes \bigotimes_v \varphi_v$ with $f$ an archimedean Schwartz function and $\varphi_v$ Schwartz-Bruhat functions with $\varphi_v = \phi_{0,v}$, the local vacuum, for almost all $v$.

**Theorem 3.20.7 (The finite adeles act place by place).** Assume the local inputs, and let a local triple be given. Let $g$ be an adelic point of $U(V)$ whose archimedean component is $1$, and let $f \otimes \bigotimes_v \varphi_v$ be a pure tensor. Then there are Schwartz-Bruhat functions $\varphi'_v$ with $\varphi'_v = \phi_{0,v}$ for almost all $v$ and $\varphi'_v - \varphi_v \in \mathrm{aug}_v(\omega)$ for every $v$, such that

$$\omega(g, 1)\Bigl(f \otimes \bigotimes_v \varphi_v\Bigr) = f \otimes \bigotimes_v \varphi'_v.$$

The same holds for $U(V')$ and $\omega'$.

Lean: `GlobalTheory.LocActV.finite_adele_acts_placewise` (also `GlobalTheory.T.local_action_finite_places`, a second name).

*Proof.* The local inputs give a finite set $S_0$ of places outside which the stabilizers of the lattices fix the vacuum. Let $S_1$ be a finite set outside which $g$ preserves the lattice, and let $S$ be the union of $S_0$, $S_1$ and the places where $\varphi_v \neq \phi_{0,v}$. Write $g = g_S\, k$ with $g_S$ supported in $S$ and $k$ in the stabilizers of the lattices off $S$ and trivial in $S$ and at the real places. Then $k$ fixes the pure tensor, since it fixes each vacuum factor off $S$. The point $g_S$ acts on the factors in $S$ only, and replaces them by $\varphi'_v$ with $\varphi'_v - \varphi_v$ in the augmentation. $\square$

**Theorem 3.20.8 (Invariance of the assembled lift).** Assume Howe duality at the real places and the local inputs. Let $(W, W_1, X, \alpha, \beta)$ be a triple with Weil representations $\omega_A$, $\omega_B$, read by a local triple whose Weil representations transport to $\omega_A$ and $\omega_B$, and let the local triple be matched with real maps $R$ and finite maps $R_f$. Let $m_A$ and $m_B$ be the assembled maps: the theta lifts of the local data followed by $R$ and $R_f$. Then for every finite point $g$ of $U(W)$ and every $\Phi \in \mathcal F_A$, $m_A(\omega_A(g, 1)\Phi) = m_A(\Phi)$, and the same for $U(W_1)$, $\omega_B$ and $m_B$.

Lean: `GlobalTheory.TripleAssembly.triple_map_comp_inverse_finite` (also `GlobalTheory.T.triple_assembly_inverse_finite`, a second name).

*Proof.* Every $\Phi \in \mathcal F_A$ is the transport of an algebraic vector $\Psi$ of the Darboux model, by the surjectivity of the invariant theta lift; so $\omega_A(g, 1)\Phi$ is the transport of $\omega(g', 1)\Psi$, where $g'$ is $g$ conjugated to the model. The archimedean component of $g'$ is $1$. By induction on the span it is enough to treat a pure tensor. By [Theorem 3.20.7](/entry/finite-adele-acts-placewise/), $\omega(g', 1)$ changes each finite factor $\varphi_v$ by an element of the augmentation at $v$. The matched finite maps kill the augmentation at every place, so the lift of the pure tensor does not change. $\square$

**Remark 3.20.9 (Formalization).** The real quotient ([TwistedQuotientReal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedQuotientReal.lean#L17)) takes the agreement of theta integrals and the local matching and uses neither; its second name is at line 180. The local matching of squares ([TwistedSquareLocalMatching.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareLocalMatching.lean#L18)) has a further wrapper at line 88 under the name of matching local factors. The name of the invariance theorem ([TripleMapCompInverseFinite.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TripleMapCompInverseFinite.lean#L20)) speaks of a composition with an inverse, but it states invariance under finite points. The name of the theorem on the second side ([ThetaSubspaceEqKerProjDerivationOfSquare.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaSubspaceEqKerProjDerivationOfSquare.lean#L21)) speaks of a derivation, but no derivation appears in the statement. The two theorems on theta subspaces use two different notions of theta subspace, one for each side. We read the shape of the conclusion of the local matching of squares from its proof and did not unfold its definition, the product form, the augmentation, the Howe conditions or the lemmas on the polarization kernel.
