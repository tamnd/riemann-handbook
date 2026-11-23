---
title: The theta kernel at split places
decls:
  - GlobalTheory.KJInf.CoreG.thetaKernel_eq_jet_thC
  - GlobalTheory.T.thetaKernel_splitPlaces_eq_jet_classicalTheta
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta kernel at split places

The theta kernel of a step of a column chain is the value at $0$ of a Weil translate of a theta function, after a polynomial in the creation operators has acted on it. This section computes this value when the theta function comes from a Schwartz-Bruhat function at a finite set of split places. The answer is a jet at $0$ of the classical theta function of [the last section](/entry/reads-datum-eq-th-c/), times the scalar that relates the reading of the moved vacuum to a fixed function. The result is used in [the theta kernel identity at every tuple](/entry/kernel-identity-tuple/), and through it in the core law of [the kernel class datum](/entry/cls-kl-is/).

**Setting.** We keep the notation of [the last section](/entry/reads-datum-eq-th-c/): the CM extension $E/F$ with CM type $\Sigma$, a standard pair $(\theta, S, T, \delta, s_c, \psi)$, the Weil space $W$ with its Heisenberg translates, the reading $\xi$ and the classical theta function $\mathrm{th}_C$. Let $G_S$ and $G_T$ be the adelic unitary groups of $S$ and $T$, and let $G_S^{f}$ and $G_T^{f}$ be their subgroups of elements with trivial component at the infinite places.

A *Weil datum* for a character $\mu$ of $\mathbb{A}_E^\times$ with values in the circle is a representation $\omega$ of $G_S \times G_T$ on functions on $W$ that is [the Weil representation](/learn/theta/#the-weil-representation) of the pair with splitting characters $\mu$ and $\mu$, for the standard character $\psi$. The group acts on $W$ by $(g, h) \cdot x = h x g^{-1}$. For $g \in G_S^f$ and an $\mathcal{O}_E$-lattice $N \subset E^a$, we say that $g$ *moves* the integral lattice to $N$ if $x \in N$ exactly when $g^{-1} x$ is integral at every finite place. The same applies to $h \in G_T^f$ and $N' \subset E^b$.

For a function $f$ on $W$ and a polynomial $P$ in the variables of the infinite places, let $P \cdot f$ be the *pure tensor* of $f$ and $P$: the function that the creation operators of the Fock model at the infinite places, in the monomials of $P$, give from $f$, with unit scalars. The *theta kernel* of $f$ at $(g, h)$ is
$$\theta_K(\omega, g, h)(f) = \big(\omega(g, h) f\big)(0).$$

**Definition 2.20.1 (Jet).** For $s \in \mathbb{C}$, a function $G$ on $V$ and a polynomial $P = \sum_k P_k z^k$ in the coordinates of $V$, the *jet* of $G$ at $P$ is
$$j_s(G, P) = \sum_k P_k\, s^{|k|}\, \partial^k G(0).$$

The jet is the value at $0$ of the differential operator $P(s\, \partial)$ applied to $G$. In the Fock model the creation operators act on readings by multiplication, so their pairing with the vacuum is a jet of the reading. We take this as a hypothesis on $s$.

**Theorem 2.20.2 (The theta kernel is a jet of the classical theta function).** Let $(\theta, S, T, \delta, s_c, \psi)$ be a standard pair. Let $s \in \mathbb{C}$ be such that $(P \cdot f)(0) = j_s(\xi(f), P)$ for every holomorphic $f$ and every $P$. Let $\omega$ be a Weil datum for a character $\mu$. Let $e$ be the sum of idempotents of the places of a finite set $SS$ of places of $E$, with $e \bar{e} = 0$. Let $f_0$ be a vacuum for the integral lattices with unit scalars, let $\Phi$ be half at $e$ for the standard lattice, and let $w$ be the theta function at $e$ of $\Phi$ with vacuum $f_0$. Let $g \in G_S^f$ and $h \in G_T^f$ move the integral lattices to $N$ and $N'$. Let $c > 0$ be odd, with $Q_S\, q\, d \notin Q$ for $Q \in SS$, and assume the lattice facts for $N$ and $N'$. Let $\Xi$ be a function on the maps $E^a \to E^b$ with:

1. $\Phi(h^{-1} (e\gamma) g) = \Xi(\gamma)$ for every rational matrix $\gamma$;
2. $\Xi(x) \neq 0$ implies that $c x$ maps $N_P$ into $N'_P$ for every $P \in SS$;
3. $\Xi(x + c y) = \Xi(x)$ for every $y$ that maps $N_P$ into $N'_P$ for every $P \in SS$.

Let $\kappa \in \mathbb{C}$ and let $\mathcal{E}$ be a function on $V$ with $\xi(\omega(g, h) f_0) = \kappa\, \mathcal{E}$. Then for every polynomial $P$,
$$\theta_K(\omega, g, h)(P \cdot w) = \kappa\ j_s\big(\mathrm{th}_C(\Xi, \mathcal{E}), P\big).$$

Lean: `GlobalTheory.KJInf.CoreG.thetaKernel_eq_jet_thC` (also `GlobalTheory.T.thetaKernel_splitPlaces_eq_jet_classicalTheta`, a second name).

We first record three small facts.

**Lemma 2.20.3.** (1) $\omega(g^{-1}, h^{-1})\, \omega(g, h) f = f$ for all $f$. (2) If $S$ has Gram matrix $1$ and $g$ moves the integral lattice to $N$, then $N$ gives a self dual lattice of $S$. (3) $\mathrm{th}_C(\Xi, \kappa \mathcal{E}) = \kappa\, \mathrm{th}_C(\Xi, \mathcal{E})$.

Lean: `GlobalTheory.KJInf.CoreG.om_inv_om` (also `GlobalTheory.KJInf.CoreG.selfDual_latFr`, `GlobalTheory.KJInf.CoreG.thC_const_mul`).

*Proof.* (1) holds since $\omega$ is a homomorphism and $(g^{-1}, h^{-1})(g, h) = 1$. (2) is the theorem that a lattice moved by a group element from the integral lattice of a space with Gram matrix $1$ is self dual. (3) holds since $\mathrm{th}_C(\Xi, \vartheta)$ is a finite sum of terms $U_x U_y \vartheta$ with coefficients, and each $U_x$ is linear. $\square$

*Proof of the theorem.* We move the data by $(g, h)$, apply the last section, and then commute the Weil action with the creation operators.

1. *Moved theta function.* The vacuum $f_0$ is a theta function and a vacuum for the standard lattice. By the theorem on moved theta functions, the function $x \mapsto \Phi(h^{-1} x g)$ is half at $e$ for the lattice $L$ of $(N, N')$, and $\omega(g, h) w$ is its theta function at $e$, with vacuum $\omega(g, h) f_0$.
2. *Moved vacuum.* By the theorem on moved Weil vacua, $\omega(g, h) f_0$ is a vacuum for the lattice pair $(N, N')$ with unit scalars.
3. *The reading.* By part (2) of the lemma, $N$ and $N'$ give self dual lattices of $S$ and $T$. The hypotheses of [the reading theorem](/entry/reads-datum-eq-th-c/) now hold for $\omega(g, h) w$, $\omega(g, h) f_0$ and $\Xi$, by steps 1 and 2 and hypotheses 1 to 3. So $\omega(g, h) w$ is holomorphic and
$$\xi(\omega(g, h) w) = \mathrm{th}_C\big(\Xi, \xi(\omega(g, h) f_0)\big).$$
4. *$w$ is holomorphic.* By the theorem on finite commutation with creation, $\omega(g^{-1}, h^{-1})$ maps holomorphic functions to holomorphic functions. Apply it to $\omega(g, h) w$ and use part (1) of the lemma.
5. *Commutation.* The same theorem gives $\omega(g, h)(P \cdot w) = P \cdot (\omega(g, h) w)$, since $w$ is holomorphic and $g$ and $h$ have trivial infinite components.
6. *Entire function.* By step 3, the hypothesis on $\mathcal{E}$ and part (3) of the lemma, $\kappa\, \mathrm{th}_C(\Xi, \mathcal{E}) = \xi(\omega(g, h) w)$. The reading of a holomorphic function is entire, so this function is differentiable on $V$.
7. *Conclusion.* By step 5 and the hypothesis on $s$,
$$\begin{aligned} \theta_K(\omega, g, h)(P \cdot w) &= \big(P \cdot \omega(g, h) w\big)(0) = j_s\big(\xi(\omega(g, h) w), P\big) \\ &= j_s\big(\kappa\, \mathrm{th}_C(\Xi, \mathcal{E}), P\big) = \kappa\ j_s\big(\mathrm{th}_C(\Xi, \mathcal{E}), P\big). \end{aligned}$$
The last equality holds term by term: the derivatives at $0$ of $\kappa G$ are $\kappa$ times those of $G$ when $\kappa G$ is differentiable, by step 6. $\square$

The scalar $\kappa$ is free. In the use of the theorem, $\mathcal{E}$ is a fixed Gaussian and $\kappa$ is the constant of the moved vacuum.

**Remark 2.20.4 (Formalization).** The theorem is at [ThetaKernelSplitPlacesEqJetClassicalTheta.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelSplitPlacesEqJetClassicalTheta.lean#L46), with the three parts of the lemma at lines 20, 25 and 32. The second name is in [ThetaKernelSplitPlacesEqJetClassicalThetaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelSplitPlacesEqJetClassicalThetaStatement.lean#L13), by a `first | exact` block under one million heartbeats. The moved theta function of step 1 is in [IntSubIsLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/IntSubIsLattice.lean#L280), the moved vacuum of step 2 in [MovedWeilVacuumEqVacuumOfMovedLattices.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MovedWeilVacuumEqVacuumOfMovedLattices.lean#L103), the commutation of steps 4 and 5 in [FiniteCommCreation.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FiniteCommCreation.lean#L13) and the entire reading of step 6 in [GaussianTwistedRealReadingEntireAndInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/GaussianTwistedRealReadingEntireAndInjective.lean#L179). The kernel and the pure tensor are in [LocalNewformFunction.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean#L77) and [DatumVec.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/DatumVec.lean#L130), and the jet in [SplitPart.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/SplitPart.lean#L29). The hypothesis on $s$ is an input: the theorem does not prove that the creation operators act by jets. Step 2 also gives that the reading of the moved vacuum is a nonzero classical theta function for $\Lambda$; the proof does not use this. We have read the statements of the four cited theorems, not their proofs, and we have not unfolded the creation operators or the Weil datum beyond its standard character.
