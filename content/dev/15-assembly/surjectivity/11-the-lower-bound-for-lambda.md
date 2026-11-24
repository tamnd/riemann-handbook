---
title: The lower bound for lambda
decls:
  - GlobalTheory.BigTop.lamLow_of_hypotheses_alt_alt
  - GlobalTheory.LowRow.lamLow_closing_alt
  - GlobalTheory.T.finiteness_inputs_real_data_three_alt
  - GlobalTheory.LowRowAdel.adelC_of_siegelWeil_of_doubling_alt
  - GlobalTheory.T.adelC_of_parameter_choice_stdV
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The lower bound for lambda

This section proves the second statement of Section 1: at almost all points of a family, the eigenvalues $\lambda$ of the definite side of the point are bounded below, in the sense of the relation $L_6$. The bound comes from theta lifts. A theta lift from the definite group to the indefinite one acts on each type part by a positive scalar $l$, and the inner product formula, the doubling method and the formal degree give a lower bound for $\log l$. Seven published inputs enter here, and they are used only in this section and, for rapid decay, in Section 4. The result is the other half of [the main theorem of Section 1](/proof/unitary-hypotheses/). The background is in [the Weil representation](/learn/theta/#the-weil-representation) and in [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees).

We first state the inputs. Rapid decay of cusp forms is stated in Section 4. Let $E / E^+$ be the CM host field, and $A$ and $B$ hermitian spaces over $E$ with ranks $a$ and $n$; write $r_B$ for the Witt index of $B$ and $A \oplus (-A)$ for the doubled space.

**Theorem 5.11.1 (Weil's convergence and the Siegel-Weil formula).** Let $a \ge 1$, and assume that $r_B = 0$ or $a + r_B < n$. Then the theta integral over the automorphic quotient of $U(B)$ converges absolutely, and is bounded by a continuous seminorm of the Schwartz function. For each Weil datum on the doubled space and $B$, and each theta function, the theta kernel is integrable over the quotient of $U(B)$, and the integral is a Siegel Eisenstein series on $U(A \oplus (-A))$.

Lean: `GlobalTheory.Published.WeilSiegelFormulaUnitary`.

This is Weil's theorem (*Sur la formule de Siegel dans la théorie des groupes classiques*, 1965), with the form for unitary groups of Ichino (2004).

**Theorem 5.11.2 (Siegel-Weil formula in the convergent range).** Assume $a < n \le 2a$ and $a + r_B < n$. Then for each Weil datum and each choice of Iwasawa decomposition, infinite family and Cartan involutions, the Siegel-Weil identity holds in the convergent range, with the measures of covolume one on the lattice of $\operatorname{Hom}(A, B)$.

Lean: `GlobalTheory.Published.SiegelWeilUnitaryConvergent`.

See Kudla and Rallis (1994) for the method, and Ichino (*A regularized Siegel-Weil formula for unitary groups*, 2004).

**Theorem 5.11.3 (Doubling method).** Let $V$ be a hermitian space of rank $n \ge 1$ and $\mu$ a Hecke character of $E$. For each section $\varphi$ of the degenerate principal series of $U(V \oplus (-V))$ the Siegel Eisenstein series continues meromorphically in $s$ with finite order poles, and for cusp forms $f_1$ and $f_2$ on $U(V)$ and $\operatorname{Re} s > n/2$ the basic identity of the doubling method holds: the integral of the Eisenstein series against $f_1 \otimes \bar f_2$ on $U(V) \times U(V)$ is an integral of a matrix coefficient against the section.

Lean: `GlobalTheory.Published.DoublingMethodLocalZetaIntegrals`.

This is the doubling method of Piatetski-Shapiro and Rallis (Gelbart, Piatetski-Shapiro and Rallis, *Explicit Constructions of Automorphic L-Functions*, Part A).

**Theorem 5.11.4 (Unramified doubling integral).** Let $k$ be a nonarchimedean local field of characteristic $0$, with residue field of size $q$, and $\mu$ a Haar measure on $\mathrm{GL}_n(k)$ with $\mu(\mathrm{GL}_n(\mathcal{O}_k)) = 1$. Let $\pi$ be a representation with Satake parameter $\alpha$ and $\omega$ its zonal spherical function. Then there is $s_0$ such that for $\operatorname{Re} s > s_0$ the doubling integral of the spherical section against $\omega$ converges and

$$\begin{aligned} \int_{\mathrm{GL}_n(k)} f_s\big(\iota(g, 1)\big)\, \omega(g)\, d\mu(g) &= L\big(s + \tfrac12, \alpha\big)\, L\big(s + \tfrac12, \alpha^{-1}\big) \\ &\quad \cdot c_n(q, s), \end{aligned}$$

where $c_n(q, s)$ is the inverse of the normalizing factor of the section.

Lean: `GlobalTheory.Published.UnramifiedDoublingGL`.

This is the unramified computation of Piatetski-Shapiro and Rallis in the same book.

**Theorem 5.11.5 (Bernstein-Zelevinsky).** Let $k$ be a nonarchimedean local field. Then irreducible smooth representations of $\mathrm{GL}_n(k)$ are admissible, Jacquet modules of finite length representations have finite length, parabolic induction preserves finite length, and the contragredient of an induced representation is induced from the contragredient.

Lean: `GlobalTheory.Published.BernsteinZelevinskyFiniteness`.

This is in Bernstein and Zelevinsky (*Induced representations of reductive $p$-adic groups I*, 1977).

**Theorem 5.11.6 (Formal degree).** Fix Haar measures on the groups $U(P, Q)$ that are compatible with the compact duals. Let $\lambda_1 > \dots > \lambda_N$ be a Harish-Chandra parameter, with $\lambda_a - (N - 1)/2 \in \mathbb{Z}$, and let $\sigma$ be a discrete series representation of $U(P, Q)$ with parameter $\lambda$ on a Hilbert space $H$. Then for each $w \in H$ with $w \ne 0$

$$\frac{\lVert w \rVert^{4}}{\int \lvert \langle w, \sigma(g) w \rangle \rvert^{2} \, dg} = \prod_{a < b} \frac{\lvert \lambda_a - \lambda_b \rvert}{b - a}.$$

Lean: `GlobalTheory.Published.FormalDegreeCompactDual`.

This is Harish-Chandra's formula for the formal degree (*Discrete series for semisimple Lie groups II*, 1966).

Now the target. Let $p$ be a point of a family, with level groups $V_i$ and $W_i$ at each level $i$. For an embedding $\sigma$, a type $t$ prime to the host and a level datum $P$, a *theta lift* $\theta$ of a level vector acts on the type part with eigenvalues $e$.

**Definition 5.11.7 (Adelic lower bound).** The *adelic lower bound* holds for the data $R$ and the face $F$ of a point if, at each level $i$ with the size condition at $b$, for each type $t$ prime to the host, each embedding $\sigma$ and level datum $P$, and for all Weil data, level vectors and coefficient data that fit, there is a theta lift, and each theta lift $\theta$ satisfies: for each $e$ with nonzero type part there is $l > 0$ such that $\theta$ acts on the type part by $l$ after the adjoint level map, and

$$\operatorname{main}(i, \sigma) - 8 f\, n_V^{2}\, L_p(b) \le \log l.$$

Lean: `GlobalTheory.LowRow.AdelC`.

Here $f$ and $n_V$ are the parameters of the point, $\operatorname{main}(i, \sigma)$ is the main term of the level, and $L_p(b)$ is a logarithmic size term.

**Theorem 5.11.8 (The adelic lower bound).** Assume rapid decay of cusp forms, Weil's convergence and the Siegel-Weil formula, the Siegel-Weil formula in the convergent range, the doubling method, the unramified doubling integral, Bernstein-Zelevinsky and the formal degree. If the size data of the point have a parameter choice and the standard volume condition holds, then the adelic lower bound holds.

Lean: `GlobalTheory.LowRowAdel.adelC_of_siegelWeil_of_doubling_alt` (also `GlobalTheory.T.adelC_of_parameter_choice_stdV`, a second name).

*Proof.* Fix the data of the definition and a theta lift $\theta$. The scalar $l$ comes from the inner product formula, and the bound on $\log l$ from a product of four factors. We use:

1. the harmonic module, from the decay of Fock vectors and a $\cosh$ integral; the single block local integral; and the place models of the point, which split the space of forms as a restricted tensor product. These hold with no input.
2. The adelic lift lies in the space of cusp forms, by rapid decay. So the inner product of the lift with itself is defined.
3. The inner product formula for twisted theta lifts: by rapid decay, Weil's theorem and the doubling method (through its residue part), $\langle \theta(f), \theta(f) \rangle$ is the doubling zeta integral of the matrix coefficient. With step 2 and the source level character law, the lift acts on each type part by a scalar $l > 0$.
4. The matrix coefficient of the Fock vector, from the harmonic module and the place models, and the norm of $\delta$ at each level.
5. The finite zeta integral: by rapid decay, Bernstein-Zelevinsky and the unramified doubling integral, it equals a partial $L$-value, which has an Euler product.
6. The theta level index times the Schwartz norm, from the single block integral and the place models.
7. The lower bound for the unitary mass, from the standard volume condition and orthonormal lattice frames.
8. The upper bound for the formal degree at the real places, from Harish-Chandra's formula.

The adelic lift identity takes the cusp form condition, the level law, the inner product formula, the matrix coefficient, the norms of $\delta$, the Euler product, the level index and the two bounds on the mass and on the formal degree, and gives the scalar $l$ with the bound on $\log l$. $\square$

**Theorem 5.11.9 (Closing the lower bound).** Assume the seven inputs. Let $p$ be a point with core $T$, data $R$, face $F$, weights $\kappa$, base vectors $v_0$ and objects $O$, with the conditions of its links, pins, phases and ties, the size conditions at $b$, and two bounds at each level $j$: the main term $\ell_{6, m}(j)$ of the definite side is at most the lower bound $\mathrm{low}(j, b)$, and the number $\ell_6(j)$ of the number record at $(C, C_H)$ is at most $\ell_{6, m}(j)$. If the size data have a parameter choice and the standard volume condition holds, then the definite side of $p$ satisfies $L_6$ at the number record at $(C, C_H)$.

Lean: `GlobalTheory.LowRow.lamLow_closing_alt` (also `GlobalTheory.T.finiteness_inputs_real_data_three_alt`, a second name).

*Proof.* The theorem above gives the adelic lower bound. The primitive rows give the core of the split part and its base links, and so the bad places of the base tuple are prime to the host. Now the lower bound for the lift eigenvalues, under the weak characterization of the data, gives $L_6$ from the adelic lower bound, the primality to the host, the conjugates of the rational theta lift, and the conditions of the point and the two bounds. $\square$

**Theorem 5.11.10 (The lower bound for lambda).** Assume the seven inputs. Then for each family in the closed family hypothesis, eventually at the points $p$, and for each $C$, the definite side of $p$ satisfies $L_6$ at the number record of $p$ at $(C, C_H)$.

Lean: `GlobalTheory.BigTop.lamLow_of_hypotheses_alt_alt`.

*Proof.* We may assume that the size constant $C_{\mathrm{sz}}$ of the family is at least $8$, since the closed property allows a lower bound on it. Along the family the weight sizes of theta lifts hold eventually: there is $x_0$ such that for $x \ge x_0$ the size condition holds at each level $j$ with the constant $b$ of the point. Let $p$ be a regular point beyond $x_0$, and $C$ real. Apply the closing theorem with the data of $p$. The first bound at each $j$ is the estimate of the hook log sum: a sum of log hook terms minus $C_{\mathrm{sz}} f\, n_V^{2} L_p$ is at most $\mathrm{low}(j, b)$, and this uses $C_{\mathrm{sz}} \ge 8$. The second bound is an equality, since $\ell_6(j) = \ell_{6, m}(j) - C \cdot 0$. The parameter choice comes from the parameters of the family, and the standard volume condition from the point. $\square$

**Remark 5.11.11 (Formalization).** The main theorem is in [LamLowOfPublished.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LamLowOfPublished.lean#L17). At line 33 the second bound is proved by `show _ - C * 0 ≤ _`: the constant $C$ enters $\ell_6$ only through a factor $0$, so the bound is the same for all $C$. The closing theorem and its second name are in [FinitenessInputsRealDataThree.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FinitenessInputsRealDataThree.lean#L14), at lines 14 and 35, and the adelic theorem and its second name in [FinitenessInputsRealData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FinitenessInputsRealData.lean#L13), at lines 13 and 38; both second names are one-line calls with `maxHeartbeats` set to 1000000. The Siegel-Weil formula in the convergent range is bound as `_hSWc` at line 18 and never used, and the closing theorem passes it only to the adelic theorem: this input does no work in the whole chapter. The doubling input is an abbreviation of a statement whose second clause is `True` (DmOfHyp.lean, line 18). The formal degree input is shown equal to a formula of the development by `Iff.rfl`. The adelic lower bound is in [FormalDegreeUpperC.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FormalDegreeUpperC.lean#L24), and $L_6$ in IndefSide.lean at line 325. The names "finiteness inputs real data three" and "parameter choice std V" describe files or hypotheses, not the statements. We have not unfolded the theta lift, the type parts, the main term, $L_p$, the lift identity or the weak characterization, and the statements of the published inputs above are our reading of their Lean types; the account of the Siegel-Weil statements in particular is not checked against the published theorems.
