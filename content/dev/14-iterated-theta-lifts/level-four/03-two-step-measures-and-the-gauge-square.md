---
title: Two-step measures and the gauge square
decls:
  - GlobalTheory.GaugeEx.twoStep_adelic_swap
  - GlobalTheory.T.adelicTwoStepMeasure_orthogonalBases_plane_compare
  - GlobalTheory.GaugeSquare.square
  - GlobalTheory.T.unitaryStabilizer_measure_independent_of_path
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Two-step measures and the gauge square

A gauge on a unitary group is a Haar measure that we build from a smaller unitary group. We remove one vector of positive length at a time: the measure on $U(J)$ is the measure on the stabilizer of a vector $x$ integrated over the orbit of $x$. In this section we remove two vectors in two steps, and we show that the result does not depend on the two vectors that we choose. The main tool is a comparison of two-step measures on pairs of vectors. It reduces to a local comparison at each place and to the product formula for a nonzero element of $E$. The background is in Volume 1, at [unitary groups](/learn/groups/#unitary-groups), [Haar measure](/learn/analysis/#haar-measure) and [adeles and ideles](/learn/number-fields/#adeles-and-ideles).

**Setting.** Let $E/F$ be a CM extension of number fields with complex conjugation $\sigma$. Let $b$ be an $F$-basis of $E$. For a ring $R$ over $F$, write $R_E = R \otimes_F E$. Let $\mathbb{A}_\infty$ be the archimedean part of the adeles of $F$, and let $F_v$ be the completion at a finite place $v$. For a hermitian matrix $J$ of size $n$ over $E$, write
$$h_J(x, y) = x^{\mathsf T} J\, \sigma(y), \qquad q_J(x) = h_J(x, x),$$
and write $U_R(J)$ for the unitary group of $J$ over $R_E$. For a pair $X = (X_0, X_1)$ of column vectors and a $2 \times 2$ matrix $\gamma$, the pair $X\gamma$ has columns $(X\gamma)_a = \sum_c X_c\, \gamma_{ca}$.

**Definition 1.3.1 (Standard measures).** A *standard measure system* $s$ for $b$ is a choice of additive Haar measures $\lambda_\infty$ on $\mathbb{A}_{\infty, E}$ and $\lambda_v$ on $F_{v,E}$, and $\nu_\infty$ on $\mathbb{A}_\infty$ and $\nu_v$ on $F_v$, such that, for each finite $v$, $\lambda_v$ gives volume $1$ to the $\mathcal{O}_v$-span of $b$ and $\nu_v$ gives volume $1$ to $\mathcal{O}_v$.

**Definition 1.3.2 (Fibre measure).** Let $R$ be $\mathbb{A}_\infty$ or $F_v$, and let $\beta \in F^\times$. A measure $m$ on $R_E^n$ is the *fibre measure* at $\beta$ when there is a family of measures $m_c$, for $c \in R^\times$, that disintegrates the product Haar measure $\lambda^n$ along $q_J$ against $\nu$, with $m_\beta = m$. A measure $\nu$ on $\mathbb{A}_E^n$ is the *standard fibre measure* of $(J, \beta)$ when it is the restricted product of fibre measures at $\beta$ at all places.

The restricted product condition says this. Let $\nu_\infty$ and $\nu_v$ be the local factors, with $\nu_v$ of volume close to $1$ on the standard lattice, in the sense that $\sum_v \lvert \nu_v(\mathrm{lat}_v) - 1 \rvert$ converges. Then, for each finite set $S$ of places and measurable functions $f_\infty$ and $f_v$, the integral of $f_\infty \prod_{v \in S} f_v$ over the set where the coordinates at $v \notin S$ lie in the lattice is
$$\int f_\infty\, d\nu_\infty \cdot \prod_{v \in S} \int f_v\, d\nu_v \cdot \prod_{v \notin S} \nu_v(\mathrm{lat}_v).$$

**Definition 1.3.3 (Step data).** Let $J$ have size $n + 1$. *Step data* $(x, \beta, B, J')$ for $J$ is a vector $x \in E^{n+1}$, a scalar $\beta \in F^\times$, and a matrix $B$ of size $(n+1) \times n$, such that $J$ is hermitian and nondegenerate, $q_J(x) = \beta$, each column of $B$ is orthogonal to $x$, and $J' = B^* J B$ is hermitian and nondegenerate.

**Definition 1.3.4 (Two-step measure).** Let $(x, \beta, B, J')$ be step data. Let $m$ be a measure on vectors of length $n + 1$ and $m'$ a measure on vectors of length $n$, over a ring $R$. A measure $N$ on pairs of vectors is the *two-step measure* of $(m, m')$ when, for each measurable $f \geq 0$ and each section $g$ of the orbit map $U_R(J) \to U_R(J)\, x$,
$$\int f\, dN = \int\!\!\int f\bigl(y,\ g(y)\, B\, y'\bigr)\, dm'(y')\, dm(y).$$

So a two-step measure first picks $y$ in the orbit of $x$, and then a vector in the orthogonal complement of $y$, which is $g(y) B$ applied to a vector $y'$ for $J'$.

**Theorem 1.3.5 (Two-step measures under a change of plane basis).** Let $s$ be a standard measure system. Let $(x_1, a_1, B_1, J_1')$ and $(x_2, a_2, B_2, J_2')$ be step data for the same $J$. Let $y_i$ be vectors with $q_{J_i'}(y_i) = b_i \neq 0$, for $i = 1, 2$. Let $\gamma \in \mathrm{GL}_2(E)$ with
$$\bigl(x_2,\ B_2 y_2\bigr) = \bigl(x_1,\ B_1 y_1\bigr)\, \gamma.$$
Let $\nu_i$ be the standard fibre measure of $(J, a_i)$, let $\nu_i'$ be the standard fibre measure of $(J_i', b_i)$, and let $N_i$ be the two-step measure of $(\nu_i, \nu_i')$ over $\mathbb{A}_F$. Then $N_2$ is the image of $N_1$ under $X \mapsto X\gamma$.

Lean: `GlobalTheory.GaugeEx.twoStep_adelic_swap` (also `GlobalTheory.T.adelicTwoStepMeasure_orthogonalBases_plane_compare`, a second name).

*Proof.* We work in four steps.

*Step 1: the local comparison.* By the local swap theorem there is $u \in E^\times$ with this property. Let $R$ be $\mathbb{A}_\infty$ or some $F_v$. Let $m_i$ and $m_i'$ be the fibre measures over $R$ for the same data as $\nu_i$ and $\nu_i'$, and let $N_{i,R}$ be their two-step measure. Then
$$N_{2,R} = \lvert u \rvert_R \cdot (\cdot\, \gamma)_* N_{1,R},$$
where $\lvert u \rvert_R$ is the modulus of multiplication by $u$ on $R_E$. The element $u$ does not depend on $R$. Both $\mathbb{A}_\infty$ and $F_v$ satisfy the conditions of the local theorem (they are reduced Artinian rings with open units and a continuous square root near $1$).

*Step 2: the global measures are restricted products.* Fix $i$. By the definition of the standard fibre measure, $\nu_i$ and $\nu_i'$ have local factors $m_{i,R}$ and $m_{i,R}'$ that are fibre measures. The orbit of $x_i$ under each local unitary group has full measure, and the local fibre measures are finite and nonzero on the orbit. So the unique two-step measure $N_{i,R}$ of $(m_{i,R}, m_{i,R}')$ exists at each place. The restricted product theorem for two-step measures then says that $N_i$ is the restricted product of the $N_{i,R}$.

*Step 3: the action of $\gamma$.* The matrix $\gamma$ is rational, so the action $X \mapsto X\gamma$ is the product of the local actions. Thus $(\cdot\,\gamma)_* N_1$ is the restricted product of the local images $(\cdot\,\gamma)_* N_{1,R}$.

*Step 4: the product formula.* By the product formula for the nonzero element $u$ of $E$, the modulus $\lvert u \rvert_v$ is $1$ for all but finitely many $v$, and
$$\lvert u \rvert_\infty \prod_v \lvert u \rvert_v = 1.$$
If we scale the local factors of a restricted product by constants with product $1$, the restricted product does not change. By step 1 the factors of $N_2$ are the scaled factors of $(\cdot\,\gamma)_* N_1$. So $N_2$ and $(\cdot\,\gamma)_* N_1$ are restricted products of the same local measures. A restricted product is unique, so $N_2 = (\cdot\,\gamma)_* N_1$. $\square$

### The gauge square

**Definition 1.3.6 (Step relation).** Let $(x, \beta, B, J')$ be step data for $J$, and let $\mu$ and $\mu'$ be measures on $U_{\mathbb{A}}(J)$ and $U_{\mathbb{A}}(J')$. The *step relation* $\mathrm{Step}(\mu, \mu')$ holds when this is true for each standard fibre measure $\nu$ of $(J, \beta)$ and each isomorphism $e$ from the stabilizer $\mathrm{Stab}(x)$ of $x$ in $U_{\mathbb{A}}(J)$ onto $U_{\mathbb{A}}(J')$ with $g B = B\, e(g)$ for all $g$. The measure $\mu$ is the measure $e^{-1}_* \mu'$ on the stabilizer integrated against $\nu$ on the orbit of $x$.

When the step relation holds, we say that $\mu$ is built from $\mu'$ along $(x, B)$.

**Theorem 1.3.7 (The gauge square).** Let $s$ be a standard measure system and let $M \geq 2$. Let $J$ have size $M + 2$ and let $J_0$ have size $M$. Assume that there are two paths of step data from $J$ to $J_0$,
$$\begin{aligned} &(x_1, a_1, B_1, J_1), \quad (y_1, b_1, C_1, J_0), \\ &(x_2, a_2, B_2, J_2), \quad (y_2, b_2, C_2, J_0), \end{aligned}$$
with $B_1 C_1 = B_2 C_2$. Let $\mu_0$ be a Haar measure on $U_{\mathbb{A}}(J_0)$. For $i = 1, 2$, let $\mu_i$ be built from $\mu_0$ along $(y_i, C_i)$, and let $\tau_i$ be built from $\mu_i$ along $(x_i, B_i)$. Then $\tau_1 = \tau_2$.

Lean: `GlobalTheory.GaugeSquare.square` (also `GlobalTheory.T.unitaryStabilizer_measure_independent_of_path`, a second name).

*Proof.* *Step 1: the frames.* For each step of each path, the frame step theorem gives three things. The square matrix $(x \mid B)$ with first column $x$ and other columns $B$ is invertible. There is an isomorphism $e$ from $\mathrm{Stab}(x)$ onto the smaller unitary group with $g B = B\, e(g)$. Its inverse is continuous. Write $e_i$ and $e_i'$ for the isomorphisms of the two steps of path $i$, and put
$$\iota_i = e_i^{-1} \circ e_i'^{-1} \colon U_{\mathbb{A}}(J_0) \to U_{\mathbb{A}}(J).$$

*Step 2: the measures on vectors.* Each of $J$, $J_1$ and $J_2$ has rank at least $3$, because $M \geq 2$. So the standard fibre measures $\nu_i$ of $(J, a_i)$ and $\nu_i'$ of $(J_i, b_i)$ exist. They are invariant, they give full measure to the orbits of $x_i$ and $y_i$, and they are finite and nonzero on these orbits. Let $N_i$ be the two-step measure of $(\nu_i, \nu_i')$.

*Step 3: the change of basis.* Let $W$ be the image of $B_1 C_1 = B_2 C_2$. The vectors $x_1$ and $B_1 y_1$ are orthogonal to $W$ and independent. Since $(x_1 \mid B_1)$ and $(y_1 \mid C_1)$ are invertible, each vector orthogonal to $W$ is a combination of $x_1$ and $B_1 y_1$. The vectors $x_2$ and $B_2 y_2$ are orthogonal to $W$, so there is a $2 \times 2$ matrix $\gamma$ with $(x_2, B_2 y_2) = (x_1, B_1 y_1)\gamma$. Its determinant is not zero. If $\gamma v = 0$ for some $v \neq 0$, then $v_0 x_2 + v_1 B_2 y_2 = 0$, and this is false because $(x_2 \mid B_2)$ is invertible and $y_2 \neq 0$. So $\gamma \in \mathrm{GL}_2(E)$.

*Step 4: the two-step measures.* By the theorem on a change of plane basis, $N_2 = (\cdot\,\gamma)_* N_1$.

*Step 5: the unfolding.* Let $t$ be a measurable section of the orbit map of $U_{\mathbb{A}}(J)$ through the pair $(x_i, B_i y_i)$. If we apply the two step relations in turn, then for each measurable $f \geq 0$ we get
$$\int f\, d\tau_i = \int\!\!\int f\bigl(t(X)\, \iota_i(h)\bigr)\, d\mu_0(h)\, dN_i(X).$$
In this step we use that $\mu_0$ is left invariant, so that the choice of section in each fibre does not change the inner integral. We also use that $\iota_i$ maps $U_{\mathbb{A}}(J_0)$ onto the stabilizer of the pair.

*Step 6: the two embeddings agree.* Let $h \in U_{\mathbb{A}}(J_0)$. The element $\iota_2(h)$ fixes the pair $(x_2, B_2 y_2)$. Since this pair is $(x_1, B_1 y_1)\gamma$ with $\gamma$ invertible, $\iota_2(h)$ also fixes $(x_1, B_1 y_1)$, so $\iota_2(h) = \iota_1(h')$ for some $h'$. The frame relations give
$$\iota_2(h)\, B_2 C_2 = B_2 C_2\, h, \qquad \iota_1(h')\, B_1 C_1 = B_1 C_1\, h'.$$
The matrix $B_1 C_1 = B_2 C_2$ has a left inverse, because $(x_1 \mid B_1)$ and $(y_1 \mid C_1)$ are invertible. So $h' = h$, and $\iota_1 = \iota_2$.

*Step 7: the conclusion.* Let $t_1$ be a measurable section for the pair of path 1, and put $t_2(Y) = t_1(Y \gamma^{-1})$. Then $t_2$ is a measurable section for the pair of path 2. By steps 4, 5 and 6,
$$\begin{aligned} \int f\, d\tau_2 &= \int\!\!\int f\bigl(t_1(X\gamma\gamma^{-1})\, \iota_1(h)\bigr)\, d\mu_0\, dN_1(X) \\ &= \int f\, d\tau_1. \end{aligned}$$
A measure is fixed by its integrals of measurable functions $f \geq 0$, so $\tau_1 = \tau_2$. $\square$

The gauge square says that a gauge built in two steps depends only on the composite frame $B C$. In the next section this is what lets us compare gauges built from different orthogonal bases.

**Remark 1.3.8 (Formalization).** The theorem on a change of plane basis takes its global measures $\nu_i$, $\nu_i'$ and $N_i$ as hypotheses, and proves the restricted product structure from them through the helper `twoStep_isProd_of_isStdX` in the same file ([AdelicTwoStepMeasureOrthogonalBasesPlaneCompare.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AdelicTwoStepMeasureOrthogonalBasesPlaneCompare.lean#L18)). The conditions on the rings $\mathbb{A}_\infty$ and $F_v$ come from `nice_ainf_fv`. In the gauge square, the condition $M \geq 2$ is used only to get rank at least $3$ for the existence of standard fibre measures. The unfolding and the agreement of embeddings are the helpers `unfold_two` and `emb_fix`, `emb_surj`, `emb_rel` ([UnitaryStabilizerMeasureIndependentOfPath.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/UnitaryStabilizerMeasureIndependentOfPath.lean#L403)). The frame step theorem, the local swap theorem, the restricted product theorem and the product formula are cited through statement files.
