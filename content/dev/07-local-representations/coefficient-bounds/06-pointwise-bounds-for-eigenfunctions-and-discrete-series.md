---
title: Pointwise bounds for eigenfunctions and discrete series
decls:
  - GlobalTheory.BpEigen.pointwise_bound_eigenfunction
  - GlobalTheory.T.pointwiseBound_capelli_eigenfunction
  - GlobalTheory.BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries
  - GlobalTheory.T.pointwiseBound_discreteSeries_coefficients
  - GlobalTheory.discreteSeriesCoef_pointwiseBound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pointwise bounds for eigenfunctions and discrete series

This section proves the main results of the chapter. First, a coefficient that is an eigenfunction of the Capelli operators, decays and is regular on the big cell satisfies the pointwise bound, under explicit numerical conditions on the parameters. The proof splits into two cases, by whether the two types of the place are equal or not, and each case applies the [bound from three places](/entry/eigen-three-places-main/). Second, a $K$-finite [[matrix coefficient|J85Q7QGGHS]] of a [[discrete series|9AB7HYGPEK]] representation satisfies these conditions, so it satisfies the pointwise bound. Third, the two analytic inputs, Ξ-integrability and the compact class theorem, are proved, so the bound for discrete series holds without hypotheses. It is used by the step [the hypotheses are not empty](/step/nonempty-hyps/).

### Numerical conditions

We keep the place data of the earlier sections, with $n = 2r + k + 1$. A *parameter* is a vector $\lambda = (\lambda_0, \dots, \lambda_{n-1}) \in \mathbb{R}^n$.

**Definition 5.6.1 (Harish-Chandra parameter).** A parameter $\lambda$ is a *Harish-Chandra parameter* if $\lambda_0 > \lambda_1 > \dots > \lambda_{n-1}$ and each $\lambda_s - \frac{n-1}{2}$ is an integer.

This is the parametrization of the discrete series by regular integral weights; see [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees).

**Definition 5.6.2 (Standard numbers).** Let $C, b, c \in \mathbb{R}$, let $P = (k, r, u, u', T, T')$ be a parameter of a place and $\lambda$ a parameter. The *standard numbers* hold for $(C, b, c, P, \lambda)$ if:

1. for each $l$ with $1 \le l \le k$: $1 \le c$, $c + 2 \le b$, $k \le b$, $|u_l| \le b$, $|u'_l| \le b$, $|\lambda_s| \le b$ for all $s$, $\lambda_t + 2c \le \lambda_s$ for all $s < t$, and $b^{-C(2r+2)} \le T$, $b^{-C(2r+2)} \le T'$;
2. for each $s$ with $s + 2 \le k$,
$$u_{s+2} + \tfrac12 \le \lambda_s \le u_{s+1} - \tfrac12, \qquad u'_{s+2} + \tfrac12 \le \lambda_s \le u'_{s+1} - \tfrac12 .$$

Condition 2 says that the first $k - 1$ entries of $\lambda$ interlace the parameters of the two types, with room $\frac12$. Condition 1 bounds every number by $b$ and separates the entries of $\lambda$ by $2c$.

**Definition 5.6.3 (Type cases).** Let $n_0 \in \mathbb{N}$. The pair $(P, n_0)$ is in a *type case* if one of these holds:

1. (different types) $n_0 = 0$, and there is $l$ with $1 \le l \le k$ and $30(r+1)^2 + 6 \le |u_l - u'_l|$;
2. (equal types) $n_0 = 30(r+1)^2 + 6$, $u_i = u'_i$ for $1 \le i \le k$, and there is $l$ with $1 \le l < k$ and $2n_0 + 1 \le u'_l - u'_{l+1}$.

**Definition 5.6.4 (Decaying Capelli eigenfunction).** Let $A \in \mathbb{R}$ and $\mu \in \mathbb{R}^n$. A coefficient $f$ is a *decaying Capelli eigenfunction with order $A$ and eigenvalue parameter $\mu$* if $f$ is smooth on $G$, $f$ lies in the decay class of order $A$ and depth $m$ for every $m$, and for every real $y$ and every $g \in G$,
$$\mathcal{C}(y) f(g) = \prod_{s} (y + \mu_s)\, f(g).$$

### Capelli eigenfunctions

**Theorem 5.6.5 (Pointwise bound for Capelli eigenfunctions).** Assume Ξ-integrability and the compact class theorem. For all $C, C_3, C_0 \ge 0$ there are $C_4$ and $C_c$ with this property. Let $p$ be a place datum with parameter $P$, $f$ a coefficient, $b, c, A_0 \in \mathbb{R}$, $n_0, p_0 \in \mathbb{N}$ and $\lambda, \lambda' \in \mathbb{R}^n$. Put $e = (2r+2)p_0 + n_0(r+1)$. Assume:

1. the standard numbers hold for $(C, b, c, P, \lambda)$, and $(P, n_0)$ is in a type case;
2. $3(r+1) \le 2p_0$ and $p_0 \le C_0 (r+1)^2$;
3. $f$ is a decaying Capelli eigenfunction with order $A_0$ and eigenvalue parameter $\lambda'$;
4. $C_c\,(r+1)^4\,\bigl(3(r+1) n^2 + n^3\bigr) \le A_0 - e$;
5. $|\lambda'_s - \lambda_s| + e \le c - 1$ for every $s$;
6. $f$ is regular on the big cell with constants $(b, C_3, 2p_0 + n_0)$.

Then $f$ satisfies the pointwise bound with constants $(b, C_4, n_0, p_0)$.

Lean: `GlobalTheory.BpEigen.pointwise_bound_eigenfunction` (also `GlobalTheory.T.pointwiseBound_capelli_eigenfunction`, a second name).

*Proof.* Domination holds for all places, by [Theorem 5.4.7](/entry/top-density-cut-dominated-all/). Each type case gives a pair of constants $(C_4^{(i)}, C_c^{(i)})$, and we take $C_4$ and $C_c$ to be the maxima. In both cases the proof applies the bound from three places with $C_\Lambda = 7 + C$, $\Lambda = b^{(7+C)(2r+2)}$, $K = 3$, $N = 3(r+1)$, $d = n_0(r+1)$, the spacing $c$, and
$$\nu_+(y) = \nu_-(y) = \prod_s \bigl(|y + \lambda_s| + c\bigr).$$
So condition 8 of that theorem holds with equality, its condition 7 follows from the separation $\lambda_t + 2c \le \lambda_s$ and from condition 5, and the bound $N \le 2p_0$ is condition 2. A lemma on grids at a place with a long cut gives the wave and lift grid conditions, from the standard numbers at $l$ and the gap $30(r+1)^2 + 6$ between the two parameters at $l$.

Different types. Here $n_0 = 0$ and $d = 0$. A lemma gives a place $q$ with the same parameter, the same vectors and the same right type as $p$, at the level $l$ of the type case, which satisfies the decomposition condition. The proof takes $p_+ = p_- = q$, and a lemma on linked places gives polynomial maps $A_\pm$ that link $q$ to $p$ through $f$.

Equal types. Here $u = u'$ and the gap at $l$ is at least $2n_0 + 1$. A lemma on shifted places, built from the [shifted types](/entry/exists-shifted-types-lower-bound/), gives places $p_+$ and $p_-$ in which $u'_{l+1}$ is raised by $n_0$ and $u'_l$ is lowered by $n_0$, linked to $p$ through $f$ with polynomial maps of degree $n_0(r+1)$. At these places the two parameters differ by $n_0 = 30(r+1)^2 + 6$ at one index, which is the long cut that the grid lemma needs.

In both cases the margin of the three places theorem follows from condition 4, since $N = 3(r+1)$. Finally the standard numbers give $1 \le c$ and $c + 2 \le b$, so $b \ge 1$, and the pointwise bound with a constant $C_4^{(i)}$ implies the bound with any larger constant. $\square$

### Coefficients of discrete series

Let $\sigma$ be a [[unitary representation|74BPYJNZTM]] of $G$ on a Hilbert space $\mathcal{H}$. A vector $v \in \mathcal{H}$ is *$K$-finite* if it is finite under the maximal compact subgroup of $G$; we have not unfolded this condition. See [admissible representations](/learn/real-groups/#admissible-representations-and-mathfrakg-k-modules).

**Definition 5.6.6 ($K$-finite coefficient).** A coefficient $f : G \to \mathrm{Hom}(W_q, W_p)$ is a *$K$-finite coefficient of $\sigma$* if there are $a, a' \in G$ and bounded maps $L : \mathcal{H} \to W_p$ and $M : W_q \to \mathcal{H}$ such that $M w$ and $L^* x$ are $K$-finite for all $w$ and $x$, and $f(a g a') = L\, \sigma(g)\, M$ for all $g$.

**Definition 5.6.7 (Discrete series hypotheses).** Let $\varepsilon$ be the fixed signature attached to $(k, r)$. The representation $\sigma$ is a *discrete series representation with parameter $\lambda'$* if $\lambda'$ is a Harish-Chandra parameter and $\sigma$ is in the discrete series of $G$ with Harish-Chandra parameter $\lambda'$ for the signature $\varepsilon$.

**Definition 5.6.8 (Standard hypotheses).** Let $C_h, C_g, \kappa, b \in \mathbb{R}$. For the place parameter $P$ and a parameter $\lambda$, put $\tilde T = T\kappa^{-2r}$ and $\tilde T' = T'\kappa^{-2r}$. The *standard hypotheses* hold if:

1. $\lambda$ is a Harish-Chandra parameter, and the vectors $(u_1, \dots, u_k)$ and $(u'_1, \dots, u'_k)$ interlace $\lambda$;
2. $0 < \kappa \le b^{C_h}$ and $\kappa^{-1} \le b^{C_h}$;
3. $1 \le \tilde T, \tilde T' \le b^{C_h(2r+2)}$;
4. $|\lambda_s|, |u_i|, |u'_i| \le b$ for all $s$ and $i$;
5. $|\lambda_s - \lambda_t| \ge C_g (2r+2)^3$ for $s \ne t$, and $|\lambda_s - \lambda_t| \ge C_g (2r+2)^{9/2} \bigl(3(r+1) n^2 + n^3\bigr)$ when $\varepsilon_s \ne \varepsilon_t$;
6. there is $b_v \ge C_g n^7$ such that $\lambda$ has shape $b_v$ relative to $u$;
7. either $u = u'$ and $u$ has a separating gap of length $2C_g(r+1)^2 + 1$ relative to $\lambda$, or $u \ne u'$ and $u, u'$ have a cut of length $C_g(r+1)^2$.

We have not unfolded the interlacing, the shape, the separating gap or the cut.

**Theorem 5.6.9 (Pointwise bound for discrete series coefficients).** Assume Ξ-integrability and the compact class theorem. For all $C_h$ and all $C_0 \ge 0$ there are $C_4 \ge 0$ and $C_{g,0}$ with this property. Let $C_g \ge C_{g,0}$, let $p$ be a place datum with parameter $P$, let $\lambda, \lambda' \in \mathbb{R}^n$, $\kappa, b \in \mathbb{R}$, $n_0, p_0 \in \mathbb{N}$, let $\sigma$ be a unitary representation and $f$ a coefficient. Assume:

1. the standard hypotheses hold for $(C_h, C_g, \lambda, u, u', \kappa, b)$;
2. $|\lambda_s - \lambda_t| \ge 200 \sum_a |\lambda'_a - \lambda_a|$ for $s \ne t$;
3. $\sigma$ is a discrete series representation with parameter $\lambda'$, and $f$ is a $K$-finite coefficient of $\sigma$;
4. if $u_i = u'_i$ for $1 \le i \le k$ then $n_0 = 30(r+1)^2 + 6$, and otherwise $n_0 = 0$;
5. $3(r+1) \le 2p_0$ and $p_0 \le C_0 (r+1)^2$.

Then $f$ satisfies the pointwise bound with constants $(b, C_4, n_0, p_0)$.

Lean: `GlobalTheory.BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries` (also `GlobalTheory.T.pointwiseBound_discreteSeries_coefficients`, a second name).

*Proof.* Apply the pointwise bound for Capelli eigenfunctions with $C = 2|C_h|$, $C_3 = |C_h| + 6$ and $C_0$, which gives $C_4$ and $C_c$. Three numerical lemmas give thresholds $G_1, G_2, G_3$, and $C_{g,0} = \max(G_1, G_2, G_3)$; the constant is $\max(C_4, 0)$.

Step 1. Since the types of $p$ have parameters $u$ and $u'$ and $T, T' > 0$, each $u_i$ and $u'_i$ lies in $\mathbb{Z} + \frac{k-1}{2}$. Since $\lambda$ and $\lambda'$ are Harish-Chandra parameters, $\lambda' - \lambda$ is integral, and $\delta = \sum_a |\lambda'_a - \lambda_a| \ge 0$.

Step 2. The grid lemma, with $G_2$, gives the standard numbers for $(2|C_h|, b, c, P, \lambda)$ with a spacing $c$, the bounds $b^{-2|C_h|(2r+2)} \le T, T'$, and the type case of $(P, n_0)$ from condition 4. The margin lemma, with $G_3$, and the numerical family lemma, with $G_1$, give a number $h$ such that, with Step 1, conditions 4 and 5 of the eigenfunction bound hold for $A_0 = h/2$.

Step 3. A $K$-finite coefficient of a discrete series representation with parameter $\lambda'$ is a decaying Capelli eigenfunction with order $h/2$ and eigenvalue parameter $\lambda'$. An expansion bound for discrete series coefficients on a ball, with the regularity lemma at a place, gives that $f$ is regular on the big cell with constants $(b, |C_h| + 6, 2p_0 + n_0)$.

Step 4. Now apply the eigenfunction bound, and pass from $C_4$ to $\max(C_4, 0)$, using $b \ge 1$. $\square$

**Theorem 5.6.10 (Pointwise bound for discrete series coefficients, unconditional).** The conclusion of the pointwise bound for discrete series coefficients holds without the assumptions of Ξ-integrability and the compact class theorem.

Lean: `GlobalTheory.discreteSeriesCoef_pointwiseBound` (also `GlobalTheory.T.discreteSeriesCoef_pointwiseBound_unconditional`, a second name).

*Proof.* This is Theorem (Pointwise bound for discrete series coefficients) applied to [Theorem 3.5](/entry/xi-exists/) for Ξ-integrability and [Theorem 1.1 of Volume 11](/entry/actual-compact-theorem/) for the compact classes. $\square$

**Remark 5.6.11 (Formalization).** The eigenfunction bound is in [PointwiseBoundCapelliEigenfunction.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundCapelliEigenfunction.lean#L25). Its second name, in `PointwiseBoundCapelliEigenfunctionStatement.lean` at line 10, opens both `BpJoin` and `CutBP2`, and each has a definition `EigDec`; the statement uses `BpJoin.EigDec`, which is the definition above. The monotonicity lemma `pointwise_bound_mono` (line 14) is proved again as `thmBpAt_mono` in [PointwiseBoundDiscreteSeriesCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundDiscreteSeriesCoefficients.lean#L20). The three places theorem is called by the two case theorems, `CapelliEigenfunctionPointwiseBoundOfDifferentTyp.lean` (line 37) and `CapelliEigenfunctionPointwiseBoundOfEqualTypes.lean` (line 44), not by the eigenfunction bound itself. In the different types case the two shifted places are one place $q$, so the three places are in fact two. We have not opened the grid, margin, numerical family, expansion and regularity lemmas; the proof above follows their statements. We have not unfolded the Capelli operator `Q.CV`, the discrete series condition `IsDSHpk`, `IsKFinHpk`, `InterlaceS`, `ShapeS`, `HasSeparatingGap` or `HasCut`.
