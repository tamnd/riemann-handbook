---
title: Level prime operators at step zero
decls:
  - GlobalTheory.StepZeroNorm.integral_rdS
  - GlobalTheory.StepZeroNorm.integral_rd_eq_inner
  - GlobalTheory.T.petersson_stepZeroScalarForms_eq_pos_mul_inner
  - GlobalTheory.RamStepZero.normStepZero
  - GlobalTheory.RamStepZero.opsStepZero_norm
  - GlobalTheory.T.levelPrime_operators_stepZero_scale_norms
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Level prime operators at step zero

The space $X_0$ at the bottom of the chain is definite, so its forms live on a finite set of classes and the Petersson inner product is a finite sum. This section proves two facts. First, on the scalar forms of step zero, the Petersson inner product is a positive multiple of the inner product of the coefficient space. Second, a composite of level prime operators at distinct split places that maps scalar forms to scalar forms comes from a linear automorphism of the coefficient space that scales all norms by one positive number. The second fact is used in [the commutation of the level laws](/entry/link-comm-of-laws-alt/) of the open orbit chapter.

**Setting.** Let $D$ be a tower datum with CM extension $E/F$, a word $u$ and a chain $X_0, \dots, X_m$ of hermitian spaces, with $X_0$ positive definite at every infinite place. Let $\theta$ be an infinite family. The word gives a finite dimensional inner product space $M_u$, the *coefficient space*, and a map $\varphi \mapsto e_u(\varphi)$ from $M_u$ to the forms of step zero. Let $F$ be a step zero datum: classes $a$ of the step zero level group with representatives $y_a$, a character of the level group with values of norm $1$, and a set $Y_0$ of frames. For $\varphi \in M_u$, $y \in Y_0$ and $g \in G(\mathbb{A})$, let $r_\varphi(y, g)$ be the reading of $e_u(\varphi)$ on the step zero chart. A *volume datum* for $X_0$ is a Haar measure $\mu$ on the adelic unitary group $G(\mathbb{A})$ of $X_0$ with a fundamental domain $\mathcal{F}$ for the rational group $G(\mathbb{Q})$. The *stabilizer* of a class $a$ is the set of $\gamma \in G(\mathbb{Q})$ with $\gamma y_a = y_a \kappa$ for some $\kappa$ in the level group.

**Lemma 2.23.1 (The class sum of the Petersson integral).** Let $V$ be a hermitian space of rank $n$, positive definite at every infinite place, with a step level $S$ whose characters have norm $1$ and are trivial on the finite part of an open subgroup. Let $y_a$ represent the classes of $S$, each once. Let $\lambda$ be a dominant weight, $\mu$ a Haar measure with a fundamental domain $\mathcal{F}$, and $y$ a frame. Then there is $c > 0$ with the following property. Let $(\cdot, \cdot)_a$ be, for each class $a$, a sesquilinear form that agrees with the Fock pairing of $\lambda$ at orthonormal frames. Then for all forms $\varphi, \psi$ of level $S$ and weight $\lambda$,
$$\int_{\mathcal{F}} r_\varphi(y, g)\, \overline{r_\psi(y, g)}\, d\mu(g) = c \sum_a \frac{1}{|\mathrm{Stab}(a)|}\ (\psi_a, \varphi_a)_a.$$

Lean: `GlobalTheory.StepZeroNorm.integral_rdS`.

*Proof.* The Gram matrices of $V$ are positive definite at the infinite places, so the infinite group $K$ is compact.

1. *Class sum.* By the theorem on integrals over a definite quotient, there are $v > 0$ and a Haar measure $\nu$ on $K$ such that, for each continuous function $H$ that is left invariant under $G(\mathbb{Q})$ and right invariant under the level group, $\int_{\mathcal{F}} H\, d\mu = v \sum_a |\mathrm{Stab}(a)|^{-1} \int_K H(h_a k)\, d\nu(k)$. Here $h_a$ is an adelic point with finite part $y_a$ and trivial infinite part.
2. *Invariance.* The function $H = r_\varphi \overline{r_\psi}$ is continuous and left invariant. A level element $\kappa$ multiplies it by $\chi(\kappa) \overline{\chi(\kappa)} = 1$.
3. *Values.* The reading at $h_a k$ is $\varphi_a$ at the frame $y$ moved by the infinite part of $k$, and $\varphi_a$ lies in the space of $\lambda$.
4. *Schur averaging.* By the averaging theorem for compact groups, there is $c_1 > 0$ such that $\int_K g(k y)\, \overline{f(k y)}\, d\nu(k) = c_1 (f, g)$ for every sesquilinear form that is the Fock pairing at orthonormal frames and all $f, g$ in the space of $\lambda$.

Steps 1 to 4 give the claim with $c = v c_1$. $\square$

**Theorem 2.23.2 (Petersson norms at step zero).** Let $\theta$ be an infinite family, and assume that $X_0$ is cocompact. Let $(\mu, \mathcal{F})$ be a volume datum for $X_0$ and $y \in Y_0$. Then there is $c > 0$ such that for all $\varphi, \psi \in M_u$,
$$\int_{\mathcal{F}} r_\varphi(y, g)\, \overline{r_\psi(y, g)}\, d\mu(g) = c\, \langle \psi, \varphi \rangle.$$

Lean: `GlobalTheory.StepZeroNorm.integral_rd_eq_inner` (also `GlobalTheory.T.petersson_stepZeroScalarForms_eq_pos_mul_inner`, `GlobalTheory.RamStepZero.normStepZero`, two second names).

The inner product is linear in its second argument.

*Proof.* Apply the lemma to $X_0$, the step zero level of $F$ and its class representatives. For the forms $(\cdot, \cdot)_a$ take the inner products of the member forms at the classes $a$. They are sesquilinear, and the member data say that they are the Fock pairing at orthonormal frames. The forms $e_u(\varphi)$ are of the step zero level and weight. The stabilizer of the lemma has the size of the stabilizer in the class data. Since $e_u$ is an isometry, $\langle \psi, \varphi \rangle = \sum_a |\mathrm{Stab}(a)|^{-1} (\psi_a, \varphi_a)_a$. $\square$

**Definition 2.23.3 (Level prime operator).** Let $k$ be a nonarchimedean local field with residue field of size $q_k$, let $p$ be a split place of $E$ over $F$ with completion $k$, and let $\beta$ be a frame of $X_0$ at $p$ of full rank $n$. Let $Q$ be a lattice pair, $\varpi$ a uniformizer, $\chi$ an additive character of $k$ of conductor $1$, and $\eta$ a unit of the residue field. A function $f$ on $G(\mathbb{A})$ is *ramified at $(\beta, Q)$* if $f = \Phi(Q)$ for a ramified form $\Phi$ on lattice pairs. The *level prime operator* $\mathrm{S}(\beta, Q, \eta)$ extends $f$ to a form on pairs by the action of $\mathrm{GL}_n(k)$ through $\beta$, applies the finite Fourier operator of $\varpi$ and the residue character of $\chi$, twists by the diagonal of $\eta$, and takes the value at $Q$.

The *unitary law* says: for every such datum, every cocompact space $S$, every volume datum and all $f, f'$ ramified at $(\beta, Q)$,
$$\int_{\mathcal{F}} \mathrm{S} f\ \overline{\mathrm{S} f'}\ d\mu = q_k^{\,n} \int_{\mathcal{F}} f\, \overline{f'}\, d\mu.$$

**Theorem 2.23.4 (Level prime operators scale norms).** Let $\theta$ be an infinite family, assume the unitary law and that $X_0$ is cocompact. Let $k$ be a nonarchimedean local field, let $(p_i)_{i \in \iota}$ be split places with completion $k$ at pairwise distinct places, and let $I$ be a list of indices without repeats. Let $\varpi$ be a uniformizer, $\chi_i$ additive characters of conductor $1$, $\beta_i$ frames of $X_0$ at $p_i$ of full rank, $Q_i$ lattice pairs and $\eta_i$ residue units. Let $T$ be the composite over $I$ of the operators $\mathrm{S}(\beta_i, Q_i, \eta_i)$. Assume:

1. every $r_\varphi(y, \cdot)$ is ramified at every $(\beta_i, Q_i)$;
2. for every $\varphi \in M_u$ there is $\varphi'$ with $r_{\varphi'}(y, \cdot) = T\, r_\varphi(y, \cdot)$ for all $y \in Y_0$.

Then there are a linear automorphism $\mathrm{S}$ of $M_u$ and $r > 0$ with $\|\mathrm{S}\varphi\| = r \|\varphi\|$ and $r_{\mathrm{S}\varphi}(y, \cdot) = T\, r_\varphi(y, \cdot)$ for all $\varphi$ and $y$.

Lean: `GlobalTheory.RamStepZero.opsStepZero_norm` (also `GlobalTheory.T.levelPrime_operators_stepZero_scale_norms`, a second name).

*Proof.* Choose a volume datum $(\mu, \mathcal{F})$ for $X_0$.

1. *Empty frames.* If $Y_0$ is empty, take the identity and $r = 1$.
2. *A base frame.* Otherwise fix $y_0 \in Y_0$, and let $c > 0$ be the constant of the last theorem at $y_0$. For each $\varphi$, choose $\varphi' = \mathrm{S}\varphi$ as in hypothesis 2.
3. *Other places.* An operator at $p_j$ keeps functions ramified at $(\beta_i, Q_i)$ when $p_j$ and $p_i$ are distinct places, since the groups of $\mathrm{GL}$ at two places commute. By induction on the list, the partial composites of $T$ keep hypothesis 1.
4. *Norms of the composite.* By the unitary law and step 3, by induction on $I$,
$$\int_{\mathcal{F}} T f\ \overline{T f'}\, d\mu = q_k^{\,n |I|} \int_{\mathcal{F}} f\, \overline{f'}\, d\mu.$$
5. *Inner products.* Apply step 4 to $r_\varphi(y_0, \cdot)$ and $r_\psi(y_0, \cdot)$, and the last theorem on both sides. Cancel $c$. This gives $\langle \mathrm{S}\varphi, \mathrm{S}\psi \rangle = Q_0 \langle \varphi, \psi \rangle$ with $Q_0 = q_k^{\,n |I|}$.
6. *Linearity.* For a map with this property, $\|\mathrm{S}(x + y) - \mathrm{S}x - \mathrm{S}y\|^2$ and $\|\mathrm{S}(z x) - z\, \mathrm{S}x\|^2$ expand to $0$. So $\mathrm{S}$ is linear, and $\|\mathrm{S}\varphi\| = \sqrt{Q_0}\, \|\varphi\|$.
7. *Automorphism.* Since $Q_0 > 0$, $\mathrm{S}$ is injective. As $M_u$ is finite dimensional, $\mathrm{S}$ is an automorphism. Take $r = \sqrt{Q_0}$. $\square$

**Remark 2.23.5 (Formalization).** The lemma is at [PeterssonStepZeroScalarFormsEqPosMulInner.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/PeterssonStepZeroScalarFormsEqPosMulInner.lean#L162), with the class sum at line 184 and the averaging at line 196. The Petersson theorem is at line 239 of that file. Its cocompactness hypothesis is not used (line 240); the definiteness of $X_0$ comes from the tower datum. The second name of the Petersson theorem is in [PeterssonStepZeroScalarFormsEqPosMulInnerStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/PeterssonStepZeroScalarFormsEqPosMulInnerStatement.lean#L10), and the third name is a one line alias in [LevelPrimeOperatorsStepZeroScaleNorms.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/LevelPrimeOperatorsStepZeroScaleNorms.lean#L163). The scaling theorem is at line 208 of that file, with steps 3 and 4 at lines 176 and 184 and step 6 at lines 15 and 29. Its second name is in [LevelPrimeOperatorsStepZeroScaleNormsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/LevelPrimeOperatorsStepZeroScaleNormsStatement.lean#L10). The unitary law is a hypothesis, defined in [DoubleCollapse.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/DoubleCollapse.lean#L33); the theorem does not prove it. The operator is in [PlacesToAdeles.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlacesToAdeles.lean#L25) and ramification at a pair in [IsSumFrame.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsSumFrame.lean#L199). All places $p_i$ have the same completion $k$, the same uniformizer and the same residue size. When $Y_0$ is empty the conclusion holds vacuously with the identity (lines 212 to 214). The averaging theorem in [UnitOfUnitary.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnitOfUnitary.lean#L183) returns $c = 1$ when no Fock form exists (lines 190 to 192); its claim is then vacuous. We have read the statements, not the proofs, of the theorems on definite quotients and member forms.
