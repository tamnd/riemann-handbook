---
title: Geometry of unitary groups at infinity
decls:
  - GlobalTheory.T.GeometricStatement
  - GlobalTheory.CompanionTheory.UGeo.geo
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Geometry of unitary groups at infinity

This section covers the region where the real group $U(p, q)$ goes to infinity by finitely many parabolic charts. On each chart a height function grows linearly along a one-parameter subgroup, controls the Hilbert-Schmidt norm, and measures how fast conjugation contracts the nilradical. These are the geometric facts that the decay estimate for discrete series in [Proposition 3.9.8](/entry/back-of-inputs/) needs. The proof is linear algebra in the eigenspaces of a grading matrix, together with an eigenvalue gap argument for the covering. For background see [representations of real groups](/learn/representations/#representations-of-real-groups).

### Parabolic charts of U(p, q)

Let $n \geq 0$, $\varepsilon \in \{\pm 1\}^n$ and $J = \operatorname{diag}(\varepsilon_1, \dots, \varepsilon_n)$. Let $G = \{g \in \mathrm{GL}_n(\mathbb{C}) : g^H J g = J\}$, a group $U(p, q)$, and $K$ the set of unitary matrices in $G$ that commute with $J$. For a complex matrix $M$ let $\|M\|^2 = \sum_{a,b} |M_{ab}|^2$, the squared Hilbert-Schmidt norm, and for a vector $y$ let $|y|^2$ be its squared length.

**Definition 1.22.1 (Graded matrix).** A matrix $A$ is *graded* if $A^H J + J A = 0$, $A^H = A$, $A^3 = A$ and $A \neq 0$. For graded $A$ put $P_- = (A^2 - A)/2$, $P_0 = 1 - A^2$, $P_+ = (A^2 + A)/2$ and $a(t) = \exp(tA)$ for $t \in \mathbb{R}$. Let $P_A \subseteq G$ be the subgroup of $g$ with $g V_- = V_-$ and $g V_{\leq 0} = V_{\leq 0}$, where $V_-$ is the image of $P_-$ and $V_{\leq 0}$ the kernel of $P_+$. Let $\mathfrak{n}_A$ be the set of $Y_1 + Y_2$ with $AY_1 - Y_1A = -Y_1$ and $AY_2 - Y_2A = -2Y_2$.

A graded $A$ is a hermitian element of $\mathfrak{p}$ with eigenvalues in $\{-1, 0, 1\}$. The matrices $P_-, P_0, P_+$ are the orthogonal projections on its eigenspaces, and $P_A$ is the parabolic subgroup of the flag $V_- \subseteq V_{\leq 0}$.

**Theorem 1.22.2 (Geometry at infinity).** For all $n$ and $\varepsilon$ there are $m \in \mathbb{N}$, graded matrices $A_1, \dots, A_m$ with groups $P_j = P_{A_j}$ and subgroups $a_j(t)$, continuous functions $\tau_1, \dots, \tau_m : G \to \mathbb{R}$, and real numbers $c_1 > 0$, $R_0$, $C$, such that for every $j$:

1. if $x, y \in P_j$, $k \in K$ and $y = xk$, then $\tau_j(y) = \tau_j(x)$;
2. $x\, a_j(t) \in P_j$ for $x \in P_j$ and $t \in \mathbb{R}$;
3. if $x, y \in P_j$ and $y = x\, a_j(t)$, then $\tau_j(y) = \tau_j(x) + t$;
4. there are measurable sets $U_1, \dots, U_m \subseteq G$ with $U_j K = U_j$, such that every $g$ with $\|g\|^2 > R_0$ lies in some $U_j$, and $c_1 \log \|x\|^2 \leq \tau_j(x)$ for $x \in P_j \cap U_j$;
5. if $x \in P_j$, $\tau_j(x) \geq 0$ and $t \geq 0$, then $C^{-1} e^{2t} \|x\|^2 \leq \|x\, a_j(t)\|^2 \leq C e^{2t} \|x\|^2$;
6. if $x \in P_j$, $\tau_j(x) \geq 0$ and $Y \in \mathfrak{n}_{A_j}$, then $\|x Y x^{-1}\|^2 \leq C e^{-2\tau_j(x)} \|Y\|^2$.

Lean: `GlobalTheory.T.GeometricStatement` (also `GlobalTheory.CompanionTheory.UGeo.geo`).

**Theorem 1.22.3 (Inputs on U(p, q)).**
1. $K$ is compact.
2. (Iwasawa.) For graded $A$, every $g \in G$ is $xk$ with $x \in P_A$ and $k \in K$.
3. (Gram eigenvalues.) For $g \in G$ the eigenvalues $\lambda_i$ of $T = (g^{-1})^H g^{-1}$ are positive, and $\sum_i \lambda_i = \|g\|^2$.
4. (Graded matrix from eigenvalues.) Let $f : (0, \infty) \to \{-1, 0, 1\}$ with $f(\lambda^{-1}) = -f(\lambda)$. Let $\alpha \leq \lambda_i$ when $f(\lambda_i) = -1$, $\beta^{-1} \leq \lambda_i$ when $f(\lambda_i) = 0$, and $f(\lambda_i) \neq 0$ for some $i$. Then there is a graded $A'$ with $\alpha |P_-(A') y|^2 + \beta^{-1} |P_0(A') y|^2 \leq |g^{-1} y|^2$ for all $y$.
5. (Finite net.) There are graded $A_1, \dots, A_m$ such that every graded $A'$ has a $j$ with $\|P_\pm(A_j) - P_\pm(A')\|^2 \leq 1/4$ for both signs.
6. (Gap.) If $0 \leq l_i \leq L$ for $i \leq n$, $L > 0$ and some $l_i = L$, then there is $r < n$ such that no $l_i$ lies in $[rw, (r+1)w)$, where $w = L/(n+1)$.
7. (Projection bound.) Let $A_0$ and $A'$ be graded as in item 5, $1 \leq \beta \leq \alpha$, $x \in P_{A_0}$ and $k \in K$. If $\alpha |P_-(A')y|^2 + \beta^{-1}|P_0(A')y|^2 \leq |(xk)^{-1}y|^2$ for all $y$, then $\|x P_-(A_0)\|^2 \leq 4n/\alpha$ and $\|x P_0(A_0)\|^2 \leq 4n\beta$.

Items 1 and 2 are the Cartan and Iwasawa decompositions, Knapp, Chapter V. Items 3, 4 and 7 are linear algebra with the spectral theorem for $T$. Item 5 holds because the graded matrices form a compact set. Item 6 is the pigeonhole principle.

Lean: `GlobalTheory.T.unitary_maximal_compact_is_compact` (also `GlobalTheory.T.iwasawa_parabolic_compact_factorization`, `GlobalTheory.T.inverse_gram_eigenvalues_sum_hs`, `GlobalTheory.T.exists_graded_matrix_eigen_bound`, `GlobalTheory.T.finite_net_of_graded_projections`, `GlobalTheory.T.exists_gap_interval_avoiding_finite_family`, `GlobalTheory.T.hilbert_schmidt_projection_bound`).

*Proof.* Step 1: projections. For graded $A$ we have $P_- + P_0 + P_+ = 1$ and $\|M\|^2 = \|MP_-\|^2 + \|MP_0\|^2 + \|MP_+\|^2$. Also $a(t) = e^{-t}P_- + P_0 + e^tP_+$. From $AJ = -JA$ we get $P_+J = JP_-$ and $P_0J = JP_0$. Since $x^{-1} = Jx^HJ$ for $x \in G$, this gives $\|P_+x^{-1}\| = \|xP_-\|$ and $\|P_0x^{-1}\| = \|xP_0\|$.

Step 2: the height. Put $\tau_A(x) = -\frac12 \log\bigl(\|xP_-\|^2 (1 + \|xP_0\|^2)\bigr)$. Here $P_- \neq 0$, since $J$ exchanges the $\pm 1$ eigenspaces, so $\|xP_-\| > 0$, and $\tau_A$ is continuous. Let $\tau_j = \tau_{A_j}$ and $C = 6$. Since $a(t)P_- = e^{-t}P_-$ and $a(t)P_0 = P_0$, we get item 3. The matrix $a(t)$ lies in $G$ and keeps each eigenspace, which gives item 2. For item 1, $k = x^{-1}y$ lies in $K \cap P_A$. A unitary matrix that keeps $V_-$ and $V_{\leq 0}$ commutes with the three projections, so $\|yP_\ast\| = \|xP_\ast k\| = \|xP_\ast\|$.

Step 3: item 5. Write $a = \|xP_-\|^2$, $b = \|xP_0\|^2$, $c = \|xP_+\|^2$. Then $\tau_A(x) \geq 0$ means $a(1 + b) \leq 1$. Since $P_+ = (P_+x^{-1})(xP_+)$ and $\|P_+\|^2 \geq 1$, submultiplicativity and Step 1 give $1 \leq ac$. So $a \leq 1 \leq c$ and $b \leq (ab)c \leq c$, hence $\|x\|^2 = a + b + c \leq 3c$. Now $\|x\,a(t)\|^2 = e^{-2t}a + b + e^{2t}c$, which for $t \geq 0$ lies between $e^{2t}\|x\|^2/3$ and $e^{2t}\|x\|^2$.

Step 4: item 6. An element of $\mathfrak{n}_A$ lowers the eigenvalue of $A$, so $Y = P_-YP_0 + P_0YP_+ + P_-YP_+$. Then $xYx^{-1}$ is the sum of $(xP_-)Y(P_+x^{-1})$, $(xP_0)Y(P_+x^{-1})$ and $(xP_-)Y(P_0x^{-1})$. By Step 1 and $\|U + V\|^2 \leq 2\|U\|^2 + 2\|V\|^2$,
$$\|xYx^{-1}\|^2 \leq (4a^2 + 6ab)\|Y\|^2 \leq 6a(1 + b)\|Y\|^2 = 6e^{-2\tau_A(x)}\|Y\|^2,$$
using $a \leq 1$.

Step 5: a graded matrix for each large $g$. Let $\|g\|^2 > n$. By input 3, some $\lambda_i \geq \|g\|^2/n$. Put $l_i = |\log \lambda_i|$ and $L = \max_i l_i \geq \log(\|g\|^2/n) > 0$. Take $r$ from input 6. Let $f(\lambda) = -1$ if $\log\lambda \geq (r+1)w$, $f(\lambda) = 1$ if $\log\lambda \leq -(r+1)w$, and $f(\lambda) = 0$ otherwise. Put $\alpha = e^{(r+1)w}$ and $\beta = e^{rw}$. By the gap, input 4 applies and gives a graded $A'$ with $\log\alpha - \log\beta = w \geq \log(\|g\|^2/n)/(n+1)$.

Step 6: item 4 of the theorem. Take $A_1, \dots, A_m$ from input 5, $c_1 = 1/(4(n+1))$ and $R_0 = n + e^E$, where $E = 2(n+1)\log(20n^2) + 2\log n$. Let $\|g\|^2 > R_0$, take $A'$ from Step 5, $j$ with $A_j$ near $A'$, and $g = xk$ with $x \in P_j$ by input 2. Then $\|x\| = \|g\|$. Input 7 gives $a \leq 4n/\alpha$ and $b \leq 4n\beta$, so $a(1+b) \leq 20n^2\beta/\alpha$. Therefore
$$-2\tau_j(x) \leq \log(20n^2) - \frac{\log(\|x\|^2/n)}{n+1},$$
and the choice of $R_0$ gives $c_1\log\|x\|^2 \leq \tau_j(x)$. Let $E_j$ be the set of $x \in P_j$ with $c_1\log\|x\|^2 \leq \tau_j(x)$. It is closed, and $U_j = E_jK$ is closed by input 1, so it is measurable. We just showed that the $U_j$ cover $\|g\|^2 > R_0$. For $x = x'k \in P_j \cap U_j$ with $x' \in E_j$, item 1 of the theorem and $\|x\| = \|x'\|$ give the inequality. $\square$

**Classical form.** Write $G = KA^+K$ with $A^+$ the dominant part of a maximal split torus. The theorem replaces $A^+$ by finitely many one-parameter subgroups $a_j(t)$ and the radial coordinate by $\tau_j$. On the chart $j$, $\|g\|^2$ grows like $e^{2\tau_j}$, and $\mathrm{Ad}(x)$ contracts the nilradical of $P_j$ by $e^{-2\tau_j(x)}$. These are the estimates behind the asymptotics of matrix coefficients in Knapp, Chapter VIII, and in Casselman and Miličić (1982).

**Remark 1.22.4 (Formalization).** The statement is `CompanionTheory.RgExh.Dec.L.Geo`, defined in [AbsoluteL2Bound.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/AbsoluteL2Bound.lean#L85), the module of the $L^2$ bound that uses it. The proof is in [GeometricStatement.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/GeometricStatement.lean#L444). The height is `tauG` and $C = 6$. Steps 3 to 6 are `hs_lines` (L134), `contraction` (L236), `gap` (L267) and `cover` (L382); `hs_lines` gives the constant $3$, which is then weakened to $6$ to match `contraction`. The statement does not require $C > 0$. The input `exists_gap_interval_avoiding_finite_family` sits in a module named `EigenvalueGapExistsStatement`. The norm $\|\cdot\|^2$ is `Formalism.REAL.hs`; a second definition with the same body exists in the namespace `ReciprocityTheory.ChartRestriction.DS`, and $K$ is also defined twice. The wrapper `GlobalTheory.T.GeometricStatement` runs under `maxHeartbeats 1000000` and closes the goal with `first | exact`. We did not unfold `S7.UJ` beyond its defining equation, and we read the statements of the inputs, not their proofs.
