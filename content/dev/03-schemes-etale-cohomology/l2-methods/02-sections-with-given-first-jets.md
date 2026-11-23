---
title: Sections with given first jets
decls:
  - GlobalTheory.jets_approx_sections_of_positive
  - GlobalTheory.T.exists_sections_approx_firstJets_positive
  - GlobalTheory.sections_coords_and_nonvanishing_at_finset
  - GlobalTheory.T.exists_sections_coords_nonvanishing_at_finset
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sections with given first jets

On a compact complex manifold with a positive line bundle $H$, the sections of $K_Y + G + kH$ for large $k$ can take any first jets at a finite set of points, up to a small error. This section proves this with peak sections and an $L^2$ estimate, and then picks sections that give local coordinates and do not vanish at the points. The next section uses them to build an étale map and a frame off a finite set. That map and frame are the data of the $L^2$ extension theorem of Section 5.

We first fix the setting of Sections 2 to 5. It is a [complex manifold](/learn/geometry/#complex-manifolds) with an atlas and a group of [line bundles](/learn/geometry/#line-bundles-and-divisors), each with a [[Hermitian metric|Q6X6W2N29G]] given by local weights.

**Definition 10.2.1 (Weighted atlas).** Let $Y$ be a second countable Hausdorff space and $n \ge 0$. A *weighted atlas* of dimension $n$ on $Y$ with index set $I$ and group $\mathrm{La}$ (an additive abelian group) consists of the following data.

1. Charts $\phi_i : U_i \to \mathbb{C}^n$ for $i \in I$, homeomorphisms from open sets of $Y$ onto open sets of $\mathbb{C}^n$, with holomorphic transition maps $\phi_j \circ \phi_i^{-1}$, and a choice of a chart $i(y)$ with $y \in U_{i(y)}$ for each $y \in Y$.
2. For each $\lambda \in \mathrm{La}$, transition functions $g^\lambda_{ij}$ on $U_i \cap U_j$, holomorphic and nowhere zero, with $g^\lambda_{ik} = g^\lambda_{ij} g^\lambda_{jk}$ and $g^{\lambda + \mu}_{ij} = g^\lambda_{ij} g^\mu_{ij}$.
3. For each $\lambda$ and $i$, a smooth weight $\varphi^\lambda_i$ on $U_i$, with $\varphi^{\lambda+\mu}_i = \varphi^\lambda_i + \varphi^\mu_i$ and $\varphi^\lambda_j = \varphi^\lambda_i - \log|g^\lambda_{ij}|^2$ on $U_i \cap U_j$.
4. An element $\kappa \in \mathrm{La}$ with $g^\kappa_{ij} = \det d(\phi_j \circ \phi_i^{-1})$ at $\phi_i(y)$.
5. A measure $\mu$ on $Y$ with density $e^{\varphi^\kappa_i}$ against the Lebesgue measure in the chart $\phi_i$.

A *section* of $\lambda$ on an open set $U$ is a family $s = (s_i)$ of functions with $s_i \circ \phi_i^{-1}$ holomorphic on $\phi_i(U_i \cap U)$ and $s_i = g^\lambda_{ij} s_j$ on $U_i \cap U_j \cap U$. A section on $Y$ is a *global section*. We write $s(y)$ for $s_{i(y)}(y)$, and
$$|s|^2_\lambda(y) = |s_{i(y)}(y)|^2 e^{-\varphi^\lambda_{i(y)}(y)}, \qquad |s|^2 = \sum_k |s_k|^2_\lambda$$
for one section and for a tuple $s = (s_1, \dots, s_N)$. A *frame* of $\lambda$ on $U$ is a section on $U$ with no zero on $U$.

The cocycle of $\kappa$ is the Jacobian of the chart changes, so a section of $\kappa$ is a holomorphic $n$-form and $\kappa$ is the [[canonical divisor|W05VYY4HBR]] $K_Y$. For a section $F$ of $\kappa + E$, the integral $\int_Y |F|^2_{\kappa + E}\, d\mu$ is in each chart $\int |F_i|^2 e^{-\varphi^E_i}\, dv$, the usual $L^2$ norm of an $E$-valued $n$-form. The norm $|s|^2_\lambda$ does not depend on the chart, by condition 3.

For a real function $f$ on $Y$, a chart $i$, a point $y \in U_i$ and $\xi \in \mathbb{C}^n$, let $\mathcal{L}_i f(y)(\xi)$ be the real part of the Levi form of $f \circ \phi_i^{-1}$ at $\phi_i(y)$. We say $\lambda$ is *positive* if $\mathcal{L}_i \varphi^\lambda_i(y)(\xi) > 0$ for all $i$, $y \in U_i$ and $\xi \neq 0$. This is the curvature form of an [[ample|RRK8P6TXG2]] line bundle; see [metrics, curvature and positivity](/learn/positivity-resolution/#metrics-curvature-and-positivity).

For sections $w_0, w_1, \dots, w_n$ of one bundle, the *quotient map* in the chart $i$ is $v \mapsto (w_k/w_0)(\phi_i^{-1} v)_{k=1}^n$. We say that $(w_0; w_1, \dots, w_n)$ *are coordinates at* $P$ if the quotient map in the chart $i(P)$ has nonzero Jacobian determinant at $\phi_{i(P)}(P)$.

**Theorem 10.2.2 (Sections with given first jets).** Let $Y$ be compact with a weighted atlas of dimension $n$, let $H \in \mathrm{La}$ be positive and let $T \subseteq Y$ be finite. Then there are entire functions $q_P : \mathbb{C}^n \to \mathbb{C}$ for $P \in T$ with this property. For each $G \in \mathrm{La}$, each family of entire functions $p_P$ on $\mathbb{C}^n$ and each $\varepsilon > 0$ there is $k_0$ such that for each $k \ge k_0$ there is a global section $F$ of $\kappa + G + kH$ with, for each $P \in T$, in the chart $i = i(P)$ at $v_P = \phi_i(P)$,
$$\bigl|F_i(P)\, e^{-k q_P(v_P)} - p_P(v_P)\bigr| \le \varepsilon, \qquad \bigl\| d\bigl(F_i(\phi_i^{-1} v)\, e^{-k q_P(v)} - p_P(v)\bigr)(v_P) \bigr\| \le \varepsilon.$$

Lean: `GlobalTheory.jets_approx_sections_of_positive` (also `GlobalTheory.T.exists_sections_approx_firstJets_positive`, a second name).

The functions $q_P$ are fixed before $G$. The factor $e^{-k q_P}$ is a local frame that peaks at $P$, so the theorem says that $F$ has the first jet of $p_P$ at $P$ in this frame, up to $\varepsilon$.

*Proof.* We use five facts, of which we read only the statements.

1. There is a finite cover of $Y$ by balls in charts with a smooth partition of unity subordinate to it.
2. *Peak sections.* There are $q_P$ entire, $c > 0$, $C_q$ and $r_0 > 0$ with $\varphi^H_{i(P)} - 2\operatorname{Re} q_P \le C_q |v - v_P|^2$ on the closed ball of radius $r_0$ about $v_P$, which lies in the chart. For each $G$ and $p$ there is $K$ such that for each $k$ there is a smooth global section $F_0$ of $\kappa + G + kH$, equal to $p_P e^{k q_P}$ on the ball about each $P$, with $\sum_a \int_{B_a} \sum_j |\bar\partial_j F_0|^2 e^{-\varphi} \, dv \le K e^{-ck}$ over the balls $B_a$ of the cover.
3. *A rough Hörmander estimate on the compact manifold.* There are $K'$ and $t_0$ such that if the weight of a bundle $\lambda$ has Levi form at least $t_0|\xi|^2$ on the balls of the cover, then for each smooth section $F_0$ of $\kappa + \lambda$ there is a global section $F$ with $\int |F_0 - F|^2_{\kappa+\lambda}\, d\mu \le K'$ times the $\bar\partial$ integral of item 2.
4. *Curvature on the balls.* There is $k_1$ with the Levi form of $\varphi^{G + kH}$ at least $t_0|\xi|^2$ on the balls for $k \ge k_1$.
5. *Small norm gives a small jet.* For each $P \in T$ there is $k_0(P)$ such that for $k \ge k_0(P)$ each smooth section $D$ of $\kappa + G + kH$ that is holomorphic on the ball about $v_P$ and has $\int |D|^2 d\mu \le K' K e^{-ck}$ satisfies $|D(P) e^{-k q_P(v_P)}| \le \varepsilon$ and $\|d(D e^{-k q_P})(v_P)\| \le \varepsilon$.

The third fact is a form of Hörmander's estimate on a compact manifold, with the curvature bound in place of the pointwise condition. The fifth fact is the mean value inequality for holomorphic functions on the ball, applied to $D e^{-kq_P}$ with the weight $e^{-k(\varphi^H - 2\operatorname{Re} q_P)}$, which is at least $e^{-k C_q |v - v_P|^2}$ on the ball, times a factor that does not depend on $k$.

Fix $G$, $p$ and $\varepsilon$, and take $k \ge \max(k_1, k_0(P) : P \in T)$. Let $F_0$ be the section of item 2 and $F$ the section of item 3 for $\lambda = G + kH$, which applies by item 4. Put $D = F_0 - F$. Then $\int |D|^2 d\mu \le K' K e^{-ck}$. On the ball about $v_P$ the section $F_0$ is $p_P e^{kq_P}$, which is holomorphic, so $D$ is holomorphic there. By item 5,
$$\bigl|F_i(P) e^{-kq_P(v_P)} - p_P(v_P)\bigr| = \bigl|D(P) e^{-kq_P(v_P)}\bigr| \le \varepsilon,$$
and in the same way for the derivative, because $F e^{-kq_P} - p_P = -D e^{-kq_P}$ on the ball. $\square$

From jets we get coordinates. The following elementary fact turns the approximate jets into exact conditions.

**Lemma 10.2.3 (Quotients of near jets).** For each $n$ there is $\varepsilon > 0$ with this property. Let $w_0, w_1, \dots, w_n$ be holomorphic near $v_P \in \mathbb{C}^n$ with $|w_0(v_P) - 1| \le \varepsilon$, $\|dw_0(v_P)\| \le \varepsilon$, and for each $j$, $|w_j(v_P)| \le \varepsilon$ and $\|dw_j(v_P) - dv_j\| \le \varepsilon$. Then $w_0(v_P) \neq 0$ and the map $v \mapsto (w_j/w_0)_j$ has nonzero Jacobian determinant at $v_P$.

The lemma holds because at $v_P$ the derivative of $w_j/w_0$ is $(dw_j\, w_0 - w_j\, dw_0)/w_0^2$, which is close to $dv_j$, and the determinant is continuous with value $1$ at the identity. We take this lemma as given and read only its statement.

**Theorem 10.2.4 (Coordinates and a nonvanishing section).** Let $Y$, $H$ and $T$ be as in the last theorem, and let $G \in \mathrm{La}$. Then there is $k_0$ such that for each $k \ge k_0$ there are global sections $t_0, t_1, \dots, t_n$ of $\kappa + kH$ and a global section $a$ of $\kappa + G + kH$ with, for each $P \in T$: $t_0(P) \neq 0$, $(t_0; t_1, \dots, t_n)$ are coordinates at $P$, and $a(P) \neq 0$.

Lean: `GlobalTheory.sections_coords_and_nonvanishing_at_finset` (also `GlobalTheory.T.exists_sections_coords_nonvanishing_at_finset`, a second name).

*Proof.* Let $q_P$ be the functions of the theorem on first jets for $H$ and $T$, and let $\varepsilon$ be the constant of the lemma. Apply the theorem on first jets four times.

- With $G = 0$, $p_P = 1$ and $\varepsilon$, we get $k^{(0)}$ and for $k \ge k^{(0)}$ a section $t_0$ of $\kappa + kH$.
- For each $j$, with $G = 0$, $p_P(v) = v_j - (v_P)_j$ and $\varepsilon$, we get $k^{(j)}$ and sections $t_j$ of $\kappa + kH$.
- With the given $G$, $p_P = 1$ and $\varepsilon = 1/2$, we get $k^{(a)}$ and a section $a$ of $\kappa + G + kH$.

Let $k_0$ be the largest of $k^{(0)}, k^{(a)}$ and $k^{(j)}$. Fix $k \ge k_0$ and $P \in T$, and put $w_m = t_m e^{-k q_P}$ in the chart $i(P)$. The jets of $w_0$ and $w_j$ satisfy the hypotheses of the lemma, so $w_0(v_P) \neq 0$ and the quotient map of the $w$ has nonzero Jacobian at $v_P$. The factor $e^{-k q_P}$ is nowhere zero, so $t_0(P) \neq 0$, and it cancels in $w_j/w_0 = t_j/t_0$. So $(t_0; t_1, \dots, t_n)$ are coordinates at $P$. Finally $|a(P) e^{-kq_P(v_P)} - 1| \le 1/2$ gives $a(P) \neq 0$. $\square$

**Remark 10.2.5 (Formalization).** The weighted atlas is the structure `WeightedAtlas` in PlurisubharmonicCharts/FamilyLeCoords.lean, line 14. Being coordinates is `IsCoordAt`, and positivity of $H$ is written out as the strict inequality for `leviAt` in each chart. The five facts in the proof of the first theorem are `nonempty_atlasBallPartitionCover`, `peak_sections_finite_weighted_atlas`, `rough_hormander_estimate_compact_manifold`, `curvature_lower_bound_on_cover_balls` and `peak_section_small_first_jet_normal_frame`. The lemma on quotients is `quotient_jets_fderiv_det_ne_zero`. We read the statements of these six results, not their proofs, and the descriptions of their proofs above are the standard ones. In both theorems the functions $q_P$ and $p_P$ are entire on $\mathbb{C}^n$, not only holomorphic near $v_P$. The `T.` names are second names, proved by `first | exact @…` from the main names.
