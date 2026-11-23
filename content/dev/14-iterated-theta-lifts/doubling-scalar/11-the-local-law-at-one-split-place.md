---
title: The local law at one split place
decls:
  - GlobalTheory.T.splitPlaceDoubleStepLocalIteratedIntegral_proof
  - GlobalTheory.ValOneAt.valOne_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local law at one split place

The section on [the double step at finitely many split places](/entry/val-q/) reduced the iterated integral of a double step at $r$ split places to the case of one place, and left that case open. This section proves it. At one split place the two Weil representations of the double step become linear models of general linear groups. The double step value becomes a trilinear form in two Schwartz-Bruhat functions and one automorphic function, and the iterated quotient integral becomes the double integral of [the last section](/entry/one-dbl-iff-sum/). The cell sum of that section then gives the value. The result is used in [the inner theorem of the double step](/entry/inner-val-iter2/), where one place is removed from a family of places.

**Setting.** We keep the notation of the section on the double step. Fix an additive character $\psi$ of the adeles of the standard kind, an integer $\sigma \geq 0$ and a double step $S$ with spaces $B, J, B'$ and small spaces $B_A, J_0, B'_A$. Its value is
$$\mathrm{val}(c_1, c_2, f_1, f_2, \varphi, f;\ g, h_1, h_2) = \mathrm{per}\Big(\mathrm{bl}\big(\varphi, c_1, c_2, \mathrm{ctr}(\omega(g, h_1)f_1, \omega(h_1, h_2)f_2)\big),\ R(h_2)f\Big),$$
where $\mathrm{ctr}$ contracts the two flattened theta functions, $\mathrm{bl}$ lifts $\varphi$ against the bi-combination of the contraction with $c_1, c_2$, and $\mathrm{per}$ is the period of the Bessel subgroup. Let $Q$ be a split place datum of $S$, as defined in that section. In addition to the data listed there, $Q$ has:

- characters $\mu_1, \mu_2$ of $k^\times$ with open kernel, which are the local components of $\chi_1^{-1}$ and $\chi_2^{-1}$;
- levels $L_0, L_1, L_2$ of the three local groups, with $J_1$ and $J_2$ compact open and contained in the integral subgroups;
- Schwartz-Bruhat functions $\Phi_1, \Phi_2$ with types $(L_0, L_1)$ and $(L_1, L_2)$ for $\mu_1, \mu_2$, and the operators $D_1, D_2$ of the datum represent $\Phi_1, \Phi_2$ in every local model;
- an element $\alpha$ and finite sets $A_1, A_2$ which cover the flattened functions of $\Phi_1$ at $\alpha$ and of $\Phi_2$ at each $\gamma \in A_1$, at position one;
- coefficients $d_1(\gamma)$ and $d_2(\gamma, \beta)$ which represent the cell entries $\xi(J_1, 1, \alpha, \gamma)$ and $\xi(J_2, 1, \gamma, \beta)$ in the local models;
- a one-step combination $e_0$ at $\alpha$ for $L_0$ and position $\sigma + 2$, and one-step combinations $e_2(\beta)$ at $\beta$ for $L_2$ and position $\sigma + 1$;
- Haar measures $m_1, m_2$ on $\mathrm{GL}_{n_1}(k)$ and $\mathrm{GL}_{n_2}(k)$.

The weights are the cell weights $w_1(\gamma) = m_1(\mathrm{pr}_X C(J_1, \gamma))^{-1}$ and $w_2(\beta) = m_2(\mathrm{pr}_X C(J_2, \beta))^{-1}$, and the volume is $\mathrm{vol}_J = ([K_1 : J_1][K_2 : J_2])^{-1}$. A pair $(f_1, f_2)$ is *vacuum* at $Q$ if $f_i = T_i(O_i)$ for a local model $T_i$ of the Weil representation at the place and the unit vector $O_i$ of the model. A coefficient is *away* from $Q$ if its points are half integral at the place. A function $f$ is *typed* if $R(\mathrm{gl}_2(j)) f = \lambda_2(j) f$ for $j \in J_2$.

**Theorem 2.11.1 (Local law at one split place).** Let $Q$ be a split place datum of $S$. Let $\mu_1^G, \mu_2^G$ be Haar measures on $\mathrm{GL}_{n_1 \sqcup c+2}(k)$ and $\mathrm{GL}_{n_2 \sqcup c+1}(k)$ which give volume one to the integral subgroups. Let $c_1, c_2$ be away from $Q$, let $(f_1, f_2)$ be vacuum at $Q$, let $\varphi$ and $f$ be continuous automorphic with $f$ typed, and let $g, h_1, h_2$ be adelic points that are trivial at the place of $Q$. Then there is a function $u$ on $\mathrm{GL}_{n_1 \sqcup c+2}(k)$ such that:

1. for every $x$, the function
$$y \mapsto \sum_a e_0(a)\, \mathrm{val}\big(c_1, c_2, D_1 f_1, D_2 f_2, \varphi, f;\ g\, \mathrm{gl}_0(a),\ h_1 \mathrm{gl}_1(x),\ h_2 \mathrm{gl}_2(y)\big)$$
has quotient integral $u(x)$ at position $\sigma + 1$ for the measures $m_2, \mu_2^G$;
2. the function $u$ has Fourier-Jacobi quotient integral at position $\sigma + 1$ for $m_1, \mu_1^G$ equal to
$$\mathrm{vol}_J \sum_{\gamma \in A_1} \sum_{\beta \in A_2} w_1(\gamma)\, w_2(\beta)\, \mathrm{val}\big(c_1 * d_1(\gamma),\ c_2 * d_2(\gamma, \beta),\ f_1, f_2, \varphi,\ e_2(\beta) \cdot f;\ g, h_1, h_2\big).$$

Lean: `GlobalTheory.ValOneAt.valOne_all` (also `GlobalTheory.T.splitPlaceDoubleStepLocalIteratedIntegral_proof`, a second name).

*Proof.* We move the points $g, h_1, h_2$ into the functions, pass to the linear models at the place, and apply the cell sum.

1. *Preparation.* Write $f_i = T_i(O_i)$ by the vacuum condition. The Bessel data of $S$ give $c + 2 = 2(\sigma + 1)$, so the theorems of the last section apply with $\rho = \sigma + 1$. The local character has conductor one, so it is continuous and not trivial, and $\nu$ is self-dual for it.
2. *Commuting points.* The local groups embed at the place of $Q$, and their images commute with the adelic points that are trivial at that place. Hence $\omega(g, h_1) T_1$ and $\omega(h_1, h_2) T_2$ are again local models at the place, and $R(h_2) f$ is again continuous automorphic and typed.
3. *The trilinear form.* By the lemma on the trilinear form of a split double step, there are a smooth representation $\tau$ of $\mathrm{GL}_{n_2 \sqcup c+1}(k)$ on a space $A$ of functions, acting by right translation through $\mathrm{gl}_2$, and a trilinear form $T$ with these properties. Every continuous automorphic typed function lies in $A$. The form $T$ is positive of position $\sigma + 1$ for the local characters $\mu_1, \mu_2$. Its tensor value at the flattened $\Phi_1'$ is $\mathrm{val}(c_1, c_2, T_1\Phi_1', T_2\Phi_2', \varphi, F; 1, 1, 1)$, for all Schwartz-Bruhat $\Phi_1', \Phi_2'$ and $F \in A$. And if $d_1, d_2$ represent Schwartz-Bruhat functions $\Xi_1, \Xi_2$ in the local models, then
$$T(\Xi_1, \Xi_2, F) = \mathrm{val}(c_1 * d_1, c_2 * d_2, T_1 O_1, T_2 O_2, \varphi, F; 1, 1, 1).$$
Apply it to the models of step 2, and put $F = R(h_2) f \in A$.
4. *The integrand.* For local points $a, x, y$, let
$$v(a, x, y) = \mathrm{val}\big(c_1, c_2,\ \omega(g, h_1) T_1(\omega_{\mu_1}(a, x)\Phi_1),\ \omega(h_1, h_2) T_2(\omega_{\mu_2}(x, y)\Phi_2),\ \varphi, \tau(y)F;\ 1, 1, 1\big).$$
The integrand of item 1 at $(a, x, y)$ equals $v(a, x, y)$. Indeed $D_i(T_i O_i) = T_i \Phi_i$ by the datum. The value is invariant under moving the points into the functions. The Weil operators of $g\, \mathrm{gl}_0(a)$ and $h_1 \mathrm{gl}_1(x)$ split as products, by step 2. Finally, the lemma on the cancellation of the line characters identifies the Weil action of the local points with the linear model action.
5. *Symmetric double integrals.* For each $a$, the symmetric double integral of $(T, F, \omega_{\mu_1}(a, 1)\Phi_1, \Phi_2)$ exists and is unique. Call its value $z(a)$.
6. *A finite combination.* The lemma on finite combinations of symmetric double integrals, applied to $e_0$, $z$ and $v$, gives a function $u$ with the inner quotient integrals of item 1 for the function $y \mapsto \sum_a e_0(a) v(a, x, y)$, and with Fourier-Jacobi quotient integral $\sum_a e_0(a) z(a)$. Its hypothesis on $v$ is the tensor value of step 3. By step 4 this proves item 1.
7. *The cell sum.* [The symmetric cell sum](/entry/comb-eq-sum-cells/) applies to the data of $Q$, with the one-step combinations $e_0$ and $e_2(\beta)$, and the vector $F$ of type $L_2$. It gives
$$\sum_a e_0(a) z(a) = \mathrm{vol}_J \sum_{\gamma, \beta} w_1(\gamma)\, w_2(\beta) \sum_b e_2(\beta)(b)\, T(\xi_1(\alpha, \gamma), \xi_2(\gamma, \beta))(\tau(b)F).$$
8. *The cell terms.* The cell entries are Schwartz-Bruhat functions, and $d_1(\gamma)$ and $d_2(\gamma, \beta)$ represent them. By linearity of $T$ in the third variable and the last property of step 3, the inner sum over $b$ equals
$$\mathrm{val}\big(c_1 * d_1(\gamma), c_2 * d_2(\gamma, \beta), T_1 O_1, T_2 O_2, \varphi, \textstyle\sum_b e_2(\beta)(b)\tau(b)F; 1, 1, 1\big).$$
The local points of $e_2(\beta)$ commute with $h_2$, so $\sum_b e_2(\beta)(b)\, \tau(b) F = R(h_2)(e_2(\beta) \cdot f)$. Moving $g, h_1, h_2$ back out of the functions gives the term of item 2.
9. Steps 6, 7 and 8 together prove item 2. $\square$

The proof does not integrate anything by hand. All analysis is in the lemmas on the trilinear form, the existence of the symmetric double integrals and their finite combinations, and in the cell sum of the last section.

**Remark 2.11.2 (Formalization).** The theorem is at [SplitPlaceDoubleStepLocalIteratedIntegralProof.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SplitPlaceDoubleStepLocalIteratedIntegralProof.lean#L56), with the translation lemma of step 4 at line 25 and the commutation of step 8 at line 35 of the same file. The second name is a restatement in [SplitPlaceDoubleStepLocalIteratedIntegralProofStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SplitPlaceDoubleStepLocalIteratedIntegralProofStatement.lean#L12). The statement, the double step, its value, the split place datum, the weights, the volume and the conditions of being vacuum, away and typed are in [IsOneComb.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsOneComb.lean#L170). The proof does not use the normalisations $m_1(\mathrm{GL}_{n_1}(\mathcal{O})) = 1$ and $m_2(\mathrm{GL}_{n_2}(\mathcal{O})) = 1$ of the datum. We have read the statements, not the proofs, of the closed embedding of the local groups, the persistence of local models, the trilinear form of a split double step, the cancellation of the line characters, the existence of symmetric double integrals, the finite combination lemma and the Schwartz-Bruhat property of the cell entries. We have not unfolded the local models, the half integral condition, the Fourier-Jacobi quotient integral and the tensor value; their descriptions above follow their names and the statements that use them.
