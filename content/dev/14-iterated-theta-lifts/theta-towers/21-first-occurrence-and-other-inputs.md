---
title: Nonvanishing at the first occurrence and other inputs
decls:
  - GlobalTheory.T.first_occurrence_theta_lift_ne_zero
  - GlobalTheory.NonVanBottom.bottom_theta_lift_ne_zero
  - GlobalTheory.RallisBottom.big_theta_norm_eq_rallis_inner_product
  - GlobalTheory.PairLift.thetaPairLift_cuspidal_of_hypotheses
  - GlobalTheory.T.real_lift_lie_second_order
  - GlobalTheory.RealLift.LieSecondPf.lie_second_order_of_real_lift
  - GlobalTheory.T.twist_regulariser_isGood
  - GlobalTheory.RegGood.regulariser_isGood
  - GlobalTheory.FramesAtReal.framesEx_of_realisation_alt
  - GlobalTheory.T.class_sum_divisor_all_alt
  - GlobalTheory.GeoTies.linked_ties_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Nonvanishing at the first occurrence and other inputs

This section collects the last inputs of the chapter. The main result is the nonvanishing of the theta integrals of a bottom triangle: at large scale, for every bottom triangle and every index $t$, both theta integrals are not identically $0$. It follows from the Rallis inner product formula for a definite bottom, which writes the norm of a bottom lift as a nonzero constant times a product of Hecke $L$-values, and from the nonvanishing of these values. The other results are the cuspidality of theta lifts along a grid, the second order term of the Lie action on the Fock model, a regulariser for theta integrals, the existence of frames at the real places, and the ties of a row of class sums. Each is a hypothesis checked in the step [the hypotheses are not empty](/step/nonempty-hyps/).

We keep the notation of Sections 8, 10 and 15. Let $X$ be a bottom triangle with index set $\mathcal T$, and let $I_t(P)(h)$ and $I'_t(P)(h)$ be its two theta integrals at $t \in \mathcal T$, a polynomial $P$ and a finite point $h$. For $t \in \mathcal T$ let $\nu_H(t)$ be the Hecke character of the bottom at $t$. Let $e_0$ and $h_0$ be the two integers of the bottom: $1 - e_0$ is the first point and $h_0$ the last point of the range of the $L$-values, and $h_0$ is at most half the rank of the bottom.

**Theorem 3.21.1 (Rallis inner product for a definite bottom).** Assume the local inputs. At large scale the following holds. Let $X$ be a bottom triangle and $t \in \mathcal T$. Then there are a polynomial $P$, a Haar measure $\nu$, a fundamental domain $\mathcal F$ and a number $c \neq 0$ such that for every Hecke $L$-function $\Lambda$ of $\nu_H(t)$,

$$\int_{\mathcal F} |I_t(P)(h)|^2 \, d\nu(h) = c \prod_{s = 1 - e_0}^{h_0} \Lambda(s).$$

Lean: `GlobalTheory.RallisBottom.big_theta_norm_eq_rallis_inner_product` (also `GlobalTheory.T.rallis_inner_product_big_theta_lift`, a second name).

*Proof.* The bottom of a triangle is definite: its space has positive signature at every real place. So the local inputs give data for the inner product formula on a definite bottom: a polynomial $P$, a Haar measure $\nu$, a fundamental domain $\mathcal F$ of nonzero volume and the comparison of the theta integral with a Petersson norm. On a definite space the quotient of the adelic group by its rational points is compact, and the theta integral is a finite sum of values of the kernel. Its squared absolute value integrated over $\mathcal F$ is the Petersson norm of the theta lift. The Rallis formula for an anisotropic bottom writes this norm as a constant $\kappa Z$ times the product of the values $\Lambda(s)$ for $1 - e_0 \le s \le h_0$, where $Z$ is a product of local zeta integrals at the bad places. Take $c = \mathrm{vol}(\mathcal F)\, \kappa\, Z$. Each factor is not $0$, so $c \neq 0$. $\square$

The classical form is the Rallis inner product formula: the Petersson norm of a theta lift is a product of local zeta integrals times a value of a standard $L$-function, which comes from the Siegel-Weil formula and the doubling method. On a definite space no regularization is needed.

**Theorem 3.21.2 (Nonvanishing at the first occurrence).** Assume the local inputs, the agreement of theta integrals and the local matching, and assume that the Hecke $L$-values on the range are not $0$. At large scale the following holds. For every bottom triangle $X$ and every $t \in \mathcal T$ there are $P$ and $h$ with $I_t(P)(h) \neq 0$, and there are $P'$ and $h'$ with $I'_t(P')(h') \neq 0$.

Lean: `GlobalTheory.NonVanBottom.bottom_theta_lift_ne_zero` (also `GlobalTheory.T.first_occurrence_theta_lift_ne_zero`, a second name).

*Proof.* Take $P$, $\nu$, $\mathcal F$ and $c$ from [Theorem 3.21.1](/entry/big-theta-norm-eq-rallis-inner-product/). The hypothesis on $L$-values gives a Hecke $L$-function $\Lambda$ of $\nu_H(t)$ with $\Lambda(s) \neq 0$ for every integer $s$ with $1 - e_0 \le s \le$ half the rank, and $h_0$ is at most half the rank. So the right side of the Rallis formula is not $0$, and

$$\int_{\mathcal F} |I_t(P)(h)|^2 \, d\nu(h) \neq 0.$$

A function whose squared absolute value has a nonzero integral is not identically $0$, so there is $h$ with $I_t(P)(h) \neq 0$. For the second integral we use the product of local factors of the bottom, which Howe duality at the real places and the three hypotheses give. It gives a match with maps $p$ and $p'$, a polynomial $P'$ with $p'(P') \neq 0$, and a linear map $J_t$ that is $0$ or injective, such that $I_t$ is a scalar times $J_t \circ p$ and $I'_t = J_t \circ p'$. Since $I_t(P)(h) \neq 0$, the map $J_t$ is not $0$, so it is injective. Then $I'_t(P') = J_t(p'(P')) \neq 0$, so there is $h'$ with $I'_t(P')(h') \neq 0$. $\square$

The name of the theorem refers to the first occurrence of a theta lift in a Witt tower. A bottom triangle sits at the first stage of the tower, and the theorem says that the lift does not vanish there. The classical criterion is that of Rallis: the lift of a cusp form to the first occurrence is nonzero, and its norm is a product of $L$-values.

**Theorem 3.21.3 (Cuspidality of theta lifts along a grid).** Assume the local inputs. Then the theta lifts along every grid are cuspidal: for every datum with sizes and every grid with a row base, the lifts up the grid, down the grid and along its columns take smooth cusp forms to smooth cusp forms.

Lean: `GlobalTheory.PairLift.thetaPairLift_cuspidal_of_hypotheses`.

*Proof.* The local inputs contain four published results: the discrete series cover, the Harish-Chandra modules of the unitary groups, the rapid decay of cusp forms, and the theorem of Casselman and Wallach on smooth globalizations. The lemma of cuspidality from functoriality turns these four facts into the cuspidality along a grid. $\square$

The next result is about the Lie action at the real places. Let $\omega$ be a Weil representation with a unitary splitting of exponent $m$, and let $\Phi \mapsto \mathrm{Fock}(\Phi)$ be the Fock map. Let $Y$ be in the Lie algebra of a unitary group at a real place $w$, and let $\mathrm{fock}_2(Y)$ be the standard second order operator of $Y$ on polynomials in the Fock model. The second order formula says that the derivative of $\omega$ in the direction $Y$ acts on the image of the Fock map as

$$\mathrm{fock}_2(Y) + \frac{m_w}{2}\, \mathrm{tr}(Y).$$

**Theorem 3.21.4 (Second order term of the real lift).** Assume the local inputs. If derivatives of the Weil representation exist, the Fock map exists, the vacuum line is stable, and the Lie action on the image of the Fock map is $\mathrm{fock}_2(Y) + c_w\, \mathrm{tr}(Y)$ for some constant $c_w$, then the second order formula holds.

Lean: `GlobalTheory.RealLift.LieSecondPf.lie_second_order_of_real_lift` (also `GlobalTheory.T.real_lift_lie_second_order`, a second name).

*Proof.* It is enough to show $c_w = m_w/2$. Double the space: the Weil representation of $\beta \oplus \beta$ is the tensor product of two copies, and its Fock vacuum is $z\, \Phi\, \overline{\Phi}$ for a constant $z$. The diagonal integral of this vacuum is not $0$. The splitting constant of the doubled space is one half at the real places, and the scalar of the Lie action on the doubled vacuum is $2 c_w$. Compare the two: $c_w\, \mathrm{tr}(Y) = (m_w/2)\, \mathrm{tr}(Y)$ for every $Y$. $\square$

Now the regulariser. Let a triple $(W, W_1, X, \alpha, \beta)$ with a Weil representation $\omega_B$ be given, and let $\mathcal F_B$ be the algebraic Fock functions of the second side. A regulariser is a finite formal combination $z = \sum_j a_j [g_j]$ of finite points $g_j$ of $U(W_1)$; it acts by $z \cdot \Psi = \sum_j a_j\, \omega_B(g_j)\Psi$, and its degree is $\sum_j a_j$.

**Theorem 3.21.5 (A good regulariser).** Assume the local inputs and the agreement of theta integrals. Let a triple with a Haar measure and a Weil representation $\omega_B$ be given, let $\Psi_1, \dots, \Psi_n \in \mathcal F_B$, and let $u_1, \dots, u_n$ be finite points of $U(W_1)$. Then there is a regulariser $z$ of nonzero degree such that each theta integral of $z \cdot \Psi_i$ has moderate growth, and for each $i$ there is $u'_i$ with $z \cdot \omega_B(u_i)\Psi_i = \omega_B(u'_i)(z \cdot \Psi_i)$.

Lean: `GlobalTheory.RegGood.regulariser_isGood` (also `GlobalTheory.T.twist_regulariser_isGood`, a second name).

*Proof.* Choose a finite place $v$ that splits in $E$ and lies outside the bad places of the two sides and outside a finite set of places that depends on the data $\Psi_i$ and $u_i$. At a split place the twisted forms lie in a regular subspace, and the lemma on regular subspaces gives a regulariser $z$ supported at $v$ with nonzero degree. At a good place the Weil representation of $z$ commutes with the points $u_i$ up to a change $u_i \mapsto u'_i$. The agreement of theta integrals gives decay of the regularised kernel, and the lemma on moderate growth of theta integrals of a bounded kernel gives the moderate growth of the integrals of $z \cdot \Psi_i$. $\square$

In the classical theory a regulariser of this kind is used by Kudla and Rallis to make a divergent theta integral converge: an element of the Hecke algebra at one place kills the terms that do not decay.

**Theorem 3.21.6 (Frames at the real places).** For every indefinite realisation $Q$ of the row data, with a normalisation, there are self-dual lattices and frames of the realisation that are normal at the level places.

Lean: `GlobalTheory.FramesAtReal.framesEx_of_realisation_alt`.

*Proof.* The character frame of the realisation gives, at each level place, a self-dual lattice and a frame that is normal there. This is the lemma on self-dual frames at level places, applied to the frame of the realisation and the level of its character. $\square$

**Theorem 3.21.7 (Ties of the class sums).** Assume the ray field condition and the existence of reciprocity data $h_L$. Let $N$ be a norm choice extension of $h_L$, $S$ an extension of sizes and $\Gamma$ a geometry, such that every choice of $N$ has a nonempty set of extensions with laws, and assume the linkage with the slot divisor condition. Then the linkage holds for a row in which, for every comparison $t$, the point summands, the pinned class sum, the compatibility conditions, the tie of reciprocity and the further condition hold at $t$.

Lean: `GlobalTheory.GeoTies.linked_ties_alt` (also `GlobalTheory.T.class_sum_divisor_all_alt`, a second name).

*Proof.* The existence of extensions with laws gives an exponent for $N$, by the lemma on exponents of layers. The exponent gives a reading of the extension, and the ties of the row part follow from the ray field condition and the core condition of the reading. Each linked bundle is a pinned point of the reading, by the linkage lemma, so the point summands hold. The ties and the further condition of the row come from the ties of the row part by induction on the construction of the row. The pinned class sums come from the divisibility of class sums of extensions with laws, and the compatibility conditions from the ties of the second kind. $\square$

**Remark 3.21.8 (Formalization).** The Rallis formula ([BigThetaNormEqRallisInnerProduct.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BigThetaNormEqRallisInnerProduct.lean#L19)) has its second name at line 47, and the nonvanishing ([FirstOccurrenceThetaLiftNeZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FirstOccurrenceThetaLiftNeZero.lean#L15)) at line 58. The cuspidality ([ThetaPairLiftCuspidalOfHypotheses.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaPairLiftCuspidalOfHypotheses.lean#L8)) has a further wrapper at line 15 under a name for twisted lifts. The second order theorem ([LieSecondOrderOfRealLift.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/LieSecondOrderOfRealLift.lean#L11)) takes the local inputs and drops them at once (line 12); the second order formula is defined in [IsFockMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsFockMap.lean#L192), and the second name is at line 60. The regulariser ([TwistRegulariserIsGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistRegulariserIsGood.lean#L18)) has its second name at line 64. The theorem on frames ([FramesExOfRealisation.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FramesExOfRealisation.lean#L14)) takes a normalisation of the realisation and does not use it (line 15). The ties ([LinkedTies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkedTies.lean#L32)) have their second name in [LinkedTiesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkedTiesStatement.lean#L22), under a name for class sum divisors. We have not unfolded the Rallis formula for an anisotropic bottom, the product of local factors, the four published results, the regular subspace, the character frame, the conditions of the linkage or the conditions of the row; the statements of the last two theorems are given here at the level of these names.
