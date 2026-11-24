---
title: Lower bounds near the boundary and the Stokes limit
decls:
  - LevelTowerAlt.lower_centre
  - LevelTowerAlt.limit_strong
  - LevelTowerAlt.good_origin_tower_height
  - ModelDimension.abelian_cm_stokes_identity
  - ModelDimension.OrbitMargin.stokes_of_model
  - ModelDimension.OrbitMargin.stokes_of_statements
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lower bounds near the boundary and the Stokes limit

This section collects three results that the chapter on good towers uses near the boundary of a toroidal chart. The first is a lower bound for the log determinant of a family of CM lattices plus its cusp weight, uniform near the centre of the chart. It is the input of [the near boundary bound](/entry/near-bdd/). The second gives the height of a good origin tower as a limit of intersection numbers. It feeds [the good origin relay](/entry/relay-good-origin-intersection-relay/). The third is the Stokes inequality for abelian CM models, which feeds [the final intersection estimate](/entry/relay-intersection-final-estimate/).

### Families of lattices over a log cover

Let $E$ be a CM field with a CM type $\Psi$, and let $\sigma_\tau$ for $\tau \in \Psi$ be the embeddings of the type. Fix integers $n$, $a \leq n$ and $g$. The log cover is the set of $w \in \mathbb{C}^n$ with $\operatorname{Re} w_i < 0$ for $i < a$ and $\lvert w_k\rvert < 1$ for $k \geq a$. The map $\exp_a$ sends $w$ to the point whose first $a$ coordinates are $\exp(w_i)$ and whose other coordinates are $w_k$. So $\exp_a$ maps the log cover into the unit polydisc, and the centre $0$ of the polydisc is the deepest point of the boundary.

A family of Riemann lattices over the log cover is a lattice $\Lambda$ with an action of $\mathcal{O}_E$ and, for each $w$, an injective period map $\Lambda \to \mathbb{C}^g$ with a Riemann form. The periods depend holomorphically on $w$, and the action of $\mathcal{O}_E$ on $\mathbb{C}^g$ extends continuously to the centre. A family of eigenframes is a choice of vectors $b_{\tau,1}, \dots, b_{\tau,m}$ in $\mathbb{C}^g$, holomorphic on the unit ball, such that $\mathcal{O}_E$ acts on $b_{\tau,i}$ by $\sigma_\tau$, and the frames span the eigenspaces.

For a lattice $R$ in the family, the log determinant $\ell(R; b)$ is the log of the determinant of the Gram matrix of the frames $b$ for the Riemann form of $R$. The cusp weight $w(R)$ measures the short vectors of $R$ in the directions that degenerate, as in Section 9. For a saturated submodule $I$ of $\Lambda$ let $\operatorname{nz}_R(I)$ be the norm of the first nonzero vector of $I$ under $R$.

### The strong limit

**Theorem 10.18.1 (Strong limit at the centre).** Let $R_w$ be a family of Riemann lattices over the log cover with eigenframes $b$ for a CM type. Then there are the following objects.

1. A submodule $W \subseteq \Lambda$ of the vectors whose periods extend continuously to the centre.
2. The radical $I$ of $W$ for the Riemann form, which is saturated and stable under $\mathcal{O}_E$.
3. An injective $\mathcal{O}_E$ linear period map $\operatorname{per} : W \to \mathbb{C}^g$ at the centre.
4. An invertible matrix $T$ with $\operatorname{per}(x) = T u(x)$ for $x \in I$, where $u$ is a fixed coordinate map on $I$.

For every $\nu$ that is the period norm of these data at the centre, $\nu > 0$ and
$$
\ell(R_w; b(\exp_a w)) - \log \operatorname{nz}_{R_w}(I) - \log \nu \to 0
$$
as $\exp_a w \to 0$.

Lean: `LevelTowerAlt.limit_strong`.

The period norm is the product
$$
\nu = [\Lambda : W] \prod_{\tau \in \Psi} \frac{\kappa^r \det \operatorname{Gram}(q_\tau)}{\lvert \det T_\tau\rvert^2},
$$
where $q_\tau$ is the period map of $W/I$ in the eigenspace of $\tau$, $T_\tau$ is the block of $T$ for $\tau$, $r$ is the rank of $I$ over $\mathcal{O}_E$ and $\kappa$ is a normalizing constant of the Riemann form.

*Proof.* Step 1: charts. The family has a chart near the centre: a basis of $\Lambda$, a block form of the periods and a projection to the kernel of the degenerate part. In this chart the vectors with continuous periods form a saturated submodule $W$, and each has a continuous section of periods.

Step 2: the form. The Riemann form restricted to $W$ extends continuously to the centre. It is hermitian there, its imaginary part is real on $W$, and its radical is the submodule $I$. Off $I$ it is positive.

Step 3: the action. The action of $\mathcal{O}_E$ keeps $W$, since the action extends continuously to the centre. Complex conjugation on $E$ keeps $I$, so $I$ is an $\mathcal{O}_E$ module, and $\operatorname{per}$ is $\mathcal{O}_E$ linear.

Step 4: the limit. Split the Gram determinant of the eigenframes into a part along $I$ and a part along $W/I$. The part along $W/I$ tends to the product of the Gram determinants of the $q_\tau$, divided by the index. The part along $I$ grows, and its size is the size of the first nonzero vector of $I$, up to the factor $\lvert\det T\rvert^2$. Taking logs, the difference in the theorem tends to $0$. Positivity of $\nu$ comes from the positivity of the form on $W/I$. $\square$

### The lower bound at the centre

**Theorem 10.18.2 (Lower bound at the centre).** Let $R_w$ be a family of Riemann lattices over the log cover with eigenframes $b$ of size $m \geq 1$ for a CM type. Then there are $\delta > 0$ and $C$ such that
$$
\ell(R_w; b(\exp_a w)) + w(R_w) \geq -C
$$
for every $w$ in the log cover with $\lVert \exp_a w\rVert < \delta$.

Lean: `LevelTowerAlt.lower_centre`.

*Proof.* Step 1: the type is not empty. If $\Psi$ were empty, then no embedding of $E$ would lie in the type or its conjugate, which is false for a CM type.

Step 2: the limit. Apply the strong limit. A period norm $\nu$ exists: the eigenframes are independent, so the Gram matrices in the formula are defined, and the image of an isotropic family of $I$ under $\operatorname{per}$ gives the matrix $T$. So $\nu > 0$, and there is $\delta > 0$ such that the difference in the strong limit is at least $-1$ when $\lVert \exp_a w\rVert < \delta$.

Step 3: the cusp weight. The first minimum bound for the cusp weight gives $w(R_w) \geq -\log \operatorname{nz}_{R_w}(I)$. If $I = 0$, we put $\operatorname{nz} = 1$, and the bound is $w \geq 0$.

Step 4: the constant. Add the two bounds. With $C = 1 - \log \nu$ we get the claim. $\square$

The bound is uniform, but it is not explicit. The constant depends on the limit periods at the centre through $\nu$.

### The height of a good origin tower

A good origin tower is a tower of hermitian lines on a model whose origin is a CM point, with the regularity and uniform integrability of Section 12. The height of the tower is a limit of arithmetic intersection numbers on a family of block maps, as in Sections 14 and 17.

**Theorem 10.18.3 (Height of a good origin tower).** Assume the inputs: the agreement and positivity statements, proportionality, the comparison statement, the given facts of the chapter, integrability of points, the global statement and the extra statement. Let $I$ be a full system of intersection numbers. Let $p, q \geq 1$, $2 \leq B \leq B_1$ and $q \leq p$, with the conditions on the orbit data. Then there are block maps to an arithmetic variety $P_3$ of dimension $n + 1 + e$ with lines $M_t$, pulled back from the regularized metric $\mu$, and lines $N_{t,m}$, such that
$$
\lim_{t} \sum_m c_m \, I(M_t^{n+1}, N_{t,m}) = \delta \cdot \operatorname{PP}_c(f) ,
$$
where $f$ is the test polynomial and $\delta = \lvert\Psi\rvert \binom N2$. The integrals of the log norms equal $\delta$ times the geometric function of $\mu^{\dim X}$ on the fibre class.

Lean: `LevelTowerAlt.good_origin_tower_height`.

*Proof.* The comparison theorem on ties, applied to the common level free part of the Hodge metric $\mu$, gives the claim. Its replacement step is the replacement of the given metric by the regularized one, and its base step is the base side of the regularization and uniform integrability of Section 12. $\square$

### The Stokes inequality on abelian CM models

Let $E$ be an abelian CM field, let $X$ be a model of a moduli space for $E$ with a boundary, and let $U$ be a cusp weight on $X$ with a positive cusp bundle. For a real number $a$, the Stokes hypothesis at $a$ says that the regularized metric of weight $a$ has a limit as the truncation goes to the boundary. Write $\overline{U}$ for the mean value of $U$, $\deg \mu$ for the degree of the Hodge metric, and $\Lambda$ for the limit of the arithmetic intersection numbers.

**Theorem 10.18.4 (Stokes inequality on abelian CM models).** Assume the inputs, the analytic provisions, resolution of singularities, the GAGA statement for sections and the extension of homomorphisms of semiabelian schemes. Let $I$ be a full system of intersection numbers, let the model be admitted, and let $U$ be a cusp weight with a positive cusp bundle. Let $4f + 2 \leq B$, where $f = \lvert\Psi\rvert$ is the size of the CM type, and assume the limit $\Lambda$ exists. Then for every $a$ with the Stokes hypothesis,
$$
(n + 1)\bigl(a - \tfrac12 \overline{U}\bigr) \deg \mu \leq \Lambda .
$$

Lean: `ModelDimension.abelian_cm_stokes_identity` (also `ModelDimension.OrbitMargin.stokes_of_model`, a second name).

*Proof.* Apply the lemma below to the seven statements on local charts, all of which are proved: local orbit charts, regularity of Levi charts, the chart margin, integrability of points on the model, the mixed limit of top powers, the Stokes limit for the vertical part, and the limit of the measures of $\mu$. The chart margin follows from the local orbit charts. $\square$

**Lemma 10.18.5 (Stokes inequality from local statements).** Assume the seven local statements. Then the Stokes inequality holds on every admitted abelian CM model under the hypotheses of the theorem.

Lean: `ModelDimension.OrbitMargin.stokes_of_statements`.

*Proof.* Step 1: integrability. Resolution gives the analytic form of resolution, so the integrals over points are finite and absolutely finite.

Step 2: telescoping. A Stokes step on each chart gives the telescoping formula: the intersection number at truncation $t$ is a sum of a boundary term and integrals of $\log$ norms against the Chern forms.

Step 3: smoothness. The Hodge extension, the smooth projections along orbits and the vertical factor give smoothness and semipositivity of $\overline{N}$ and of the metric $\mu$ on the model. Semipositivity of $\overline{N}$ uses the Levi charts and the margin.

Step 4: the four limits. The integrand of the boundary term has a limit, since the boundary points are null and the cusp part is integrable. This gives the limit $T_p$. The mixed limit of top powers gives the limit $T$ of the main term. The limit of the measures of $\mu$ gives the error limit $\varepsilon$.

Step 5: positivity. The positivity statement for Stokes limits combines the telescoping formula and the three limits with the generic degree. The boundary term is at least $(n + 1)(a - \overline{U}/2) \deg \mu$, and the error term is nonnegative in the limit. $\square$

**Remark 10.18.6 (Formalization).** The strong limit and the lower bound are at `Development/WeilBound/CoreStatements/PlurisubharmonicCones/ExistsPhiNormSq.lean:13` and `:289`. The period norm is `PhiNormSq` (`ExistsIntSmulIsAdicIntegralInTensorBasis.lean:33` in the same folder), and its existence is `exists_phiNormSq` at line 250; independence of the frames and the image of the isotropic family are `eig_indep` (line 134) and `oFamily_image` (line 198). The lower bound proves that the CM type is not empty by contradiction at lines 296 to 300, although a CM type is never empty. The tower height is one term at `GoodOriginTowerHeight.lean:30`: `Comparison₂.tie_of` applied to `common levelFree muHodge`, `replace` and `baseSide regUnif`. The Stokes theorem is at `Development/WeilBound/CoreStatements/CommonZeroEvaluation/AbelianCmStokesIdentity.lean:119`; it only applies `stokes_of_model` (line 114), which only applies `stokes_of_statements` (line 83) to seven proved statements. The lemma takes the chart margin as a hypothesis, but the margin follows from the orbit charts (`margin_of_orbit`, line 73), and `stokes_of_model` passes it that way. In the lemma the hypotheses on the analytic provisions, on GAGA, on semiabelian extension, on admission and on the cusp weight are introduced at line 86 and not used again. The conclusion is `StokesAt` (`HasBaseDegreeSettingStrict.lean:9`).
