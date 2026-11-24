---
title: The carrier side and joint tensors
decls:
  - Formalism.L2.SG.Pf.CarrierXAll.jointTensorAt_carrierInOf
  - Formalism.L2.SG.Pf.CarrierXAll.jointTensorAt_ITcMo
  - Formalism.L2.SG.Pf.CarrierXAll.jointTensor_compact_test
  - Formalism.L2.SG.Pf.CarrierXAll.carrierDataBuilt_of_hyp
  - Formalism.L2.SG.Pf.CarrierXAll.carrierXSideP_of_leaves
  - Formalism.L2.SG.SpectralTiesReal.carrierP_of_compact_model
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The carrier side and joint tensors

This section proves the two steps of [the carrier bound](/entry/carrier-p/) that the ninth section takes as given. The first step is the joint tensor property: the global orbital operator of a pair of words is a tensor product of local orbital vectors at the real places. The second step is the positive side bound for $C_b$, which builds the carrier data from the leaves of the side and the lift property at level $3$. The last theorem turns the positive side bound and the carrier inputs into the carrier bound, which is a hypothesis of Theorem S in the thirteenth section.

### Joint tensors

Let $X$ be a Hida setting for a datum $D$, let $u, u'$ be words and let $e$ be a bijection from the infinite places of $E$ to the index set of $D$ that is tied to the places of $X$. At each real place $j$ let $V_j(u)$ and $V_j(u')$ be the local representation spaces of $X$. A *carrier input* for $(u, u')$ consists of the constant $C_A$, the words $d_e, d_e'$, an index $l$, grids, level towers $T_j$ whose base points have the levels $T(u)$ and $T(u')$, local coefficient maps $f_j$, a cut function $\chi$, signs, local points $\nu'_j$ and matrices $m_{0,j}$, top functions and a threshold $A_0$. A model for the input fixes local level data and model constants.

Let $\nu_q$ be a family of measures on the real points of the group. It is *pinned* if $\nu_q$ is the archimedean measure $\mu_\infty$ at each regular point, and if there is a Haar measure on the stabilizer with quotient measure $\nu_q$ whose image in coordinates is the stabilizer measure of the local volumes.

**Definition 3.14.1 (Joint tensor property).** The *joint tensor property* holds for $X$, $(u,u')$, a carrier input with a model, a scale $s > 0$ and $\nu_q$ if the following holds for each rational point $p$ with an orbit representative $w$, positive Gram values at all real places and dual frames $h$, $h'$. Let $\mathcal O$ be the quotient integral operator for $\nu_q$. Then
$$\pi_u(h)^{-1}\, \mathcal O\bigl(\pi_{u'}(h')\, x\bigr)$$
is the tensor product over the real places $j$ of the local vectors $s^{-1}\, v_j(T_j, \nu'_j, m_{0,j}, f_j)$ at the standard point, moved by the local identifications $e_P$ and $e_Q$.

So the global orbital operator splits as a tensor product of local orbital vectors.

**Theorem 3.14.2 (Joint tensor at a carrier input).** Let $\nu_q$ be pinned and assume the standard geometry of the pair. Assume that the local quotient integral of the model equals the local orbital operator, conjugated by $e_P$ and $e_Q$. Assume $s > 0$, that the carrier comes from $X$, that its base agrees with $i_0$ and $i_0'$, that its embeddings are those of $X$, and that it is built. Then the joint tensor property holds.

Lean: `Formalism.L2.SG.Pf.CarrierXAll.jointTensorAt_carrierInOf`.

*Proof.*

1. The pinned measure gives the measure pin at each real place.
2. The trace relation of the carrier and the orbital vectors of the carrier hold for each carrier input.
3. The standard geometry gives the local unipotent relations and the global product formula of the quotient. The open bridge gives a joint bridge.
4. The joint tensor of a pin, applied to steps 1 to 3 and to the hypotheses, gives the joint tensor property. $\square$

A *tower carrier input* is the carrier input built from a choice of data at $X$, the level towers of $X$, a top lift $\Theta_j$ and a type projector $P_j$ at each real place, and the cut $c$. Its local points and matrices are those of the towers.

**Theorem 3.14.3 (Joint tensor at a tower carrier input).** Let $i_0 = i_0'$, let $\nu_q$ be pinned, and let $s > 0$. For a tower carrier input with a model, if the local quotient integrals equal the local orbital operators and the carrier is built, then the joint tensor property holds.

Lean: `Formalism.L2.SG.Pf.CarrierXAll.jointTensorAt_ITcMo`.

*Proof.* For a tower carrier input the other hypotheses of the last theorem hold. The section of standard vectors gives the standard geometry. The carrier comes from $X$, since the coefficient system is transported. The base agrees with $i_0$ and $i_0'$ because $i_0 = i_0'$. The embeddings are those of $X$ by construction. The last theorem applies. $\square$

**Theorem 3.14.4 (Joint tensor with the standard models).** The last theorem holds with the standard models of the tower carrier input: the local level data given by the existence of levels, and all other model constants $0$, with the standard cut.

Lean: `Formalism.L2.SG.Pf.CarrierXAll.jointTensor_compact_test`.

*Proof.* This is the last theorem at the standard models. $\square$

### The carrier data

The *lift property at level $3$* for $C_b$ says this. For real place data, an operator family, a measure, level data, a start and $1 \le l_0 \le k$, each top function at level $3$ lifts to the level tower with a norm bound in terms of $C_b$. A *leaf* at $(u,u')$ is a choice of data with local vectors $a_j$, $b_j$, $\xi_j$, $\xi'_j$ and constants $c_j$ such that the coefficient maps of the tower carrier input give the integral of the mass data.

The *carrier data bound* for constants $C_6$, $C_c$ and $C_b$ gives local spaces, an abstract Hida setting with places, coefficient maps, a cut, the type data and the identifications $e_P$ and $e_Q$. It requires the equalities of constants and data, the compatibility, the bound on the parts, the size bounds, the cut bounds, the joint vectors and the norm identity with the value $j_n$.

**Theorem 3.14.5 (Carrier data from a leaf).** Assume the lift property at level $3$ for $C_b$ and the cap property of the coefficients. Assume the standing hypotheses with $C_l \ge 1000$ and $k \ge 1801$, and a leaf at $(u,u')$. Assume that the words $d_e$, $d_e'$ are those of $D$, that $1 \le l$, $l + 2 \le k$ and $d_e(l) \ne d_e'(l)$. Let $K = 4 K_\ast (r_S + 1)$. Assume that $C_c$, $C_d$, $C_6$, $C_e$ and the Fourier decay constant, each times a polynomial in $k$, $K$ and $r_S + 1$, are at most $\Delta/2 - 5/2$, and that $C_c, C_d, C_e \le C_A$. Let $h$ be a gap of the Harish-Chandra parameters at all real places with $h$ large and $h/2$ above the decay threshold. Let $i_0 = i_0'$, let a point representative exist, let $s > 0$ and let $\nu_q$ be pinned. If each tower carrier input is built with the norm value $j_n$, then the carrier data bound holds for $C_6$, $C_c$ and $C_b$.

Lean: `Formalism.L2.SG.Pf.CarrierXAll.carrierDataBuilt_of_hyp`.

*Proof.*

1. The coefficient maps of the leaf are smooth. The parameters and types at each real place are those of the words, and type projectors $P_j$ exist.
2. Build the tower carrier input first with the identity top lift. This gives the threshold $A_0$, the coefficient bound and the built places, and the constants of the leaf data.
3. The lift property at level $3$ for the towers gives the real top lifts $\Theta_j$. Build the tower carrier input again with $\Theta_j$.
4. The cap property gives the coefficient cap of this input, and the weights are tied.
5. The joint tensor with the standard models gives the joint vectors. The level zero part, the point part and the remainder are $0$ or given.
6. The carrier data bound for towers gives the result. $\square$

The *leaves of the side* say that, for all constants and data with $u \ne u'$, $c_b, c_{Tf} > 0$, ties, $C' \ge 29$, $C_l \ge 1000 + |C_{\mathrm{orb}}|$ (with $C_{\mathrm{orb}}$ the constant of the convergence of orbital integrals), $k \ge 1801$, the size hypotheses, $i_0 = i_0'$, a point representative and pinned $\nu_q$, there is a leaf at $(u, u')$. The *positive side bound for $C_b$* says that for $C_6 > 0$ and $C_c$ there is $C_{A,0}$ such that, for $C_A \ge \max(C_{A,0}, 1)$ and the constants of Theorem S, there are $k_0$, $C'_0$ and $C_{l,0}$ above which the carrier data bound holds at each pair of words.

**Theorem 3.14.6 (Positive side bound).** The lift property at level $3$ for $C_b$ and the leaves of the side give the positive side bound for $C_b$.

Lean: `Formalism.L2.SG.Pf.CarrierXAll.carrierXSideP_of_leaves`.

*Proof.*

1. Take $C_{A,0} = \max(C_c, C_d, C_e, 1)$ and
$$C_q = 8400\,\bigl(|C_c| + |C_d| + |C_6| + |C_e| + |C_F|\bigr) + 48120,$$
with $C_F$ the Fourier decay constant.
2. A bound on lengths gives $k_1$ with the length conditions for $k \ge k_1$. Put $k_0 = \max(k_1, 1801)$ and $C'_0 = 29$. Put
$$\begin{aligned}
C_{l,0} = \max\bigl(&1000,\ 25000 + 21(|C_c| + |C_d| + |C_e|),\\
&1000 + |C_{\mathrm{orb}}|\bigr).
\end{aligned}$$
3. For a pair of words above these thresholds, the leaves of the side give a leaf. The size hypotheses give the word conditions, the gap $h$ and the length conditions.
4. The carrier data from a leaf gives the carrier data bound. $\square$

### The carrier bound

**Theorem 3.14.7 (Carrier bound from the compact model).** Assume Theorem P in compact form, the model lemma, the model places and the built bounds in compact form. If the positive side bound holds for some $C_b$, then the carrier bound holds.

Lean: `Formalism.L2.SG.SpectralTiesReal.carrierP_of_compact_model`.

*Proof.*

1. The real inputs with compact support follow from Theorem P in compact form, the model lemma, the model places, the built bounds and $C_b$. This gives $C_6 > 0$, $C_c$ and $C_4 \ge 1$.
2. The positive side bound at $C_6$ and $C_c$ gives $C_{A,0}$, and then $k_0$, $C'_0$ and $C_{l,0}$. Take these as the constants of the carrier bound.
3. For a pair of words, the positive side bound gives the carrier data. Unfold the full carrier condition. Its places, local points and matrices are those of the abstract setting.
4. The real inputs of step 1, at the data of step 3, give the real inputs of the full carrier condition with the norm value $j_n$. $\square$

**Remark 3.14.8 (Formalization).** The joint tensor property is `JointTensorAt` (CarrierXJoint.lean, line 17), the pinned measure is `NuQPin` (RealObj.lean, line 378), and the pin cover is `PinCov` (CarrierJointPin.lean, line 31). The three joint tensor theorems are in CarrierXJointAt.lean, lines 40, 84 and 149; the last two run under `set_option maxHeartbeats 4000000` (lines 82 and 147). The standard models are `modelsOf` (line 133). Only its level field is real, a `.choose` of `level_exists_alt`; the fields `j`, `lam`, `Cm`, `σ`, `Lw`, `Ll` and `Ll'` are all `0`. The name `jointTensor_compact_test` reads like a test, but the carrier data use it. The carrier data from a leaf is `carrierDataBuilt_of_hyp` (CarrierXAll.lean, line 666), with `LiftAt3` at line 597 and `CarrierDataBound` in CarrierInputExistsBuilt.lean, line 44. It has an instance argument `[Fact CoefCapAll]` from a `variable` line (CarrierXAll.lean, line 664), so the cap property enters as a hidden hypothesis; the same line is at CarrierXPinsP.lean, line 49. The proof first builds the carrier with the identity top lift `liftId` (CarrierXAll.lean, line 657, used at line 707) only to get the threshold and constants. The positive side bound is `carrierXSideP_of_leaves` (CarrierXPinsP.lean, line 51), with `XLeavesP` at line 29 and `CarrierSideBoundPositive` in CarrierPOfRepairedModel.lean, line 15. Its constants 8400, 48120, 1801, 29 and 25000 are written out, and $C_{\mathrm{orb}}$ is `orbital_integral_converges.choose`, a constant taken from an existence proof. The parameter `Cb` of `CarrierSideBoundPositive` is passed only to `CarrierDataBound`. The carrier bound from the compact model is in CarrierInputExistsCompact.lean, line 27. Lines 11 to 17 of that file are a namespace block with only an `open` and a local instance, so it has no effect. The proof drops one finite dimension instance when it unfolds `CarrierFull`. A near copy of this proof, `carrierP_of_repaired_model` (CarrierPOfRepairedModel.lean, line 35), takes the forms of Theorem P and the built bounds without compact support. The wrappers `carrierP_of_kfin4` and `carrierP_of_dense4` (CarrierXPinsP.lean, lines 318 and 404) call the compact version with `liftAt3_exists` and the leaves of the side.
