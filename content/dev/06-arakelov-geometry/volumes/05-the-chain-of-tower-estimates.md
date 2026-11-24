---
title: The chain of tower estimates
decls:
  - GlobalTheory.CompanionTheory.Ar.Top.chain_tower
  - GlobalTheory.T.tower_weil_inputs_combined
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The chain of tower estimates

This section proves the main estimates of a root tower from its conditions. If a tower satisfies the conditions of [the tower conditions](/entry/full-intersection-tower-i8-identity/), then its top intersection numbers converge along the twisted lines (T1), they are given by the arithmetic flag height up to two shift terms and an error $C \log B / B$ (Theorem B), and they are bounded below by $-C$ times the volume, the flag degree and the bracket (T2); the same holds for the mean slope. The proof is a chain of steps, most of them taken from the chapters on heights and on arithmetic intersection theory. The result is used in [the volume theorem](/entry/volume-theorem-x-of-inputs/), where the conditions are checked for good towers.

We keep the notation of the previous sections. In particular $h_{\mathrm{Fl}}$ is the arithmetic flag height: for a monomial $m$ it is $(-1)^{\deg m}$ times the arithmetic intersection number of the standard hermitian lines of $m$ on the model of the flag variety over $\mathbb{Z}$.

The chain uses six inputs. We state them in words; their exact forms are in the chapters on heights and on arithmetic intersection theory.

1. The flag height statement and the inputs of the proof theory, the same inputs as in the [flag degree theorem](/entry/t-flag-degree-polynomial-eval/) of the first section.
2. The lower bound of successive minima. Let $\overline{A}$ be a hermitian line on an arithmetic variety $X$ of dimension $D + 1$ that is semipositive and nef on the fibres. If every closed point $W$ has height at least $e$, then $\widehat{\deg}(\overline{A}^{D+1}) \ge (D + 1)\, e \deg(A_{\mathbb{Q}}^D)$.
3. The upper bound of successive minima. In the same setting, if a Zariski dense set of points has heights at most $e'$, then $\widehat{\deg}(\overline{A}^{D+1}) \le (D + 1)\, e' \deg(A_{\mathbb{Q}}^D)$.
4. The antisymmetric perturbation statement: a polynomial that is close, on compact pieces of the walls, to a multiple of a polynomial vanishing on those pieces, is close, coefficient by coefficient, to that multiple plus the Weyl denominator times an invariant polynomial.
5. The height bound for Grassmannians, which bounds the flag height of the test polynomial.

The successive minima inequalities are due to Zhang, for semipositive lines; see the notes at the end of the chapter and [heights](/learn/arakelov/#heights).

**Theorem 9.5.1 (Chain of tower estimates).** Assume the six inputs above. Let $\mathrm{II}$ be a full intersection system, let $\Psi$ be nonempty, let $T$ be a root tower of type $(\Psi, N)$ with bad primes $\mathcal{B}$, and let $\mathrm{frob}$ be a label map of Frobenius shape. Let $C, C' \ge 0$, $\mathrm{rd} \ge 1$ and $L \in \mathbb{R}$. Assume that $T$:

1. is proportional and has equal volumes;
2. satisfies I1, I2, A1, M1, M2, ANef, I5, I6 and I7;
3. satisfies I8 for $h_{\mathrm{Fl}}$;
4. satisfies Proposition 6 for $\mathrm{frob}$, Proposition A, and Proposition F with $C'$, $\mathrm{rd}$, $L$;
5. has the slope lower bound with $C$.

Then $T$ satisfies T1 and Theorem B for $h_{\mathrm{Fl}}$, and T2 and the mean slope bound with the constant $2C + 3C' + 5$ and $\mathrm{rd}$, $L$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.chain_tower` (also `GlobalTheory.T.tower_weil_inputs_combined`, a second name)

*Proof.* From $1 \le j < N$ we get $N \ge 2$. The proof has nine steps.

Step 1 (I3). The conditions A1, M1, M2 and ANef give I3. The idea is that nefness on the fibres is a convex condition in the weight: the line $L_{\lambda_s, s}$ is a combination of the line of a dominant weight, nef on the fibres at the primes of $S_B$ by M1 and at the other primes under the nef threshold by M2, and the line of $(0, 1)$, nef by ANef. Semipositivity comes from A1.

Step 2 (T1). Proportionality, I2 and I3 give T1. By I3 the twisted line is nef and semipositive for small $s$. By I2 its top number differs from $\mathrm{PP}_{B,c}(L_{u_s, s}^{\,d+1})$ by at most $C s$, and the polynomial $L_{u_s, s}^{\,d+1}$ tends to $\ell_u^{\,d+1}$ as $s \to 0$. By proportionality the geometric degree $m_B(c, u, s)$ is $\operatorname{vol}(c)\deg_{\mathrm{Fl}}(u_s) + O(s)$, which tends to $\operatorname{vol}(c)\deg_{\mathrm{Fl}}(u) > 0$, since $u$ is regular dominant. The ratio converges to the slope.

Step 3 (Theorem W). The successive minima bounds, with I1, I2, I3, I5, I6, I7, proportionality and parts of the inputs, give Theorem W: on a wall, $|\mathrm{PB}_B(\lambda)| \le C \log B / B$. The lower bound I5 for heights of points gives, by the first successive minima inequality, a lower bound for the top number; the Zariski dense set of I6 gives the upper bound by the second. On a wall the flag degree of the weight vanishes, so the main terms cancel and only the errors are left.

Step 4 (I9 for the flag height). The flag height $h_{\mathrm{Fl}}$ satisfies I9: it vanishes on the top powers of dominant weights with a wall, is nonnegative on the top powers of dominant weights, and vanishes on $p_1^\tau Q$.

Step 5 (Theorem B). The antisymmetric perturbation statement, Theorem W, I8 and I9 give Theorem B for $h_{\mathrm{Fl}}$. By I8 the difference $\mathrm{PP}_{B,c} - \operatorname{vol}(c) h_{\mathrm{Fl}}$, as a polynomial in the weight, is antisymmetric under the simple reflections at $a$ with $a + 1 \ne j$. By Theorem W and I9 it is small on the walls at $j$. The perturbation statement then writes it, up to $C \log B / B$, as the Weyl denominator times an invariant polynomial, and in degree $d + 1$ the only such terms are the two shift functionals with coefficients $\alpha_\tau$ and $\beta_\tau$.

Step 6 (the averaged form). The flag model of $\mathrm{Fl}$ over $\mathbb{Z}$ has dimension $d + 1$. With this, $h_{\mathrm{Fl}}$ is invariant under the permutations of $\Psi$, since the flag model is a product of identical factors. Proposition A gives a transitive group of symmetries of $\mathrm{PP}_B$. Averaging the identity of Theorem B over this group makes $\alpha$ and $\beta$ constant.

Step 7 (the base level). The Grassmannian height bound gives

$$
h_{\mathrm{Fl}}(F_T) \le (D + 1)\,\delta\,|\Psi|\,\frac{m}{2}\log(N + 1),
$$

with $F_T$, $D$, $\delta$ and $m = \min(j, N - j)$ as in [the remainder over the primes](/entry/finite-bound/). By the [lower bound at the base](/entry/test-height-bound-slope-flat/), with proportionality, I9, Proposition F and the slope lower bound, the tower has the lower bound at the base with the constant $K = 2(C + C') + 3$.

Step 8 (T2). Proposition 6, the averaged Theorem B, Proposition F, the Frobenius shape and step 7 give T2 with the constant $K + C' + 2 = 2C + 3C' + 5$. The power sum formula moves $\mathrm{PP}_B$ of the top power of $\ell_u$ to the base level $B_0$; the averaged Theorem B, applied at the top, gives the shift coefficients there; and the lower bound at the base controls the coefficient $A_0$. The Frobenius shape is needed to compare the shift terms for different $\tau$.

Step 9 (mean slope). Proportionality, equal volumes and T2 give the mean slope bound with the same constant. Since all volumes are equal, $\operatorname{vol}(T) = |\mathrm{Comp}| \operatorname{vol}(c)$ for every $c$, and

$$
\frac{1}{|\mathrm{Comp}|}\sum_c \operatorname{slope}_B(c, u) = \frac{\mathrm{PB}_B(u)}{(d + 1)\operatorname{vol}(T)\deg_{\mathrm{Fl}}(u)}.
$$

T2 bounds the right side below by $-(2C + 3C' + 5)\beta_B(u)$. $\square$

The order of the steps is forced: Theorem B needs Theorem W, which needs I3, and T2 needs both the averaged Theorem B and the lower bound at the base. The constants are explicit at the end, but Theorem W and Theorem B have constants that are only known to exist.

**Remark 9.5.2 (Formalization).** All hypotheses are used. The proofs of steps 1 to 6, 8 and 9 are separate statements of the development, and we have not unfolded them; the explanations given with these steps are our reading of their statements, not of their proofs. Step 3 takes the sixth part of the inputs of the proof theory by position. The dimension $d$ appears in two forms, as the degree of the antisymmetric polynomials and as the dimension of the flag variety, and the proof checks that they are equal. The second name is a statement file with the same statement ([TowerWeilInputsCombined.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TowerWeilInputsCombined.lean#L22)).
