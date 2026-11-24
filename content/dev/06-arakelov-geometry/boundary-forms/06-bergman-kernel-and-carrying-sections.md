---
title: The Bergman kernel and carrying sections
decls:
  - GlobalTheory.ThickBerg.exp_neg_B_le_bergOn_of_mem_framesOn
  - GlobalTheory.T.exp_neg_B_le_bergOn_of_la1sq_bound
  - GlobalTheory.CovHt.KeySection.theta_function_le_bergman_kernel_alt
  - GlobalTheory.CovHt.KeySection.cover_height_section_bound_alt
  - GlobalTheory.T.exists_section_bounded_by_bergman_kernel_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Bergman kernel and carrying sections

The height lower bound compares the lattice of cusp forms of a weight $u_1$ with the lattice of cusp forms of a smaller weight $u_1'$. The comparison uses a *carrying section* $\theta$: a modular form such that multiplication by $\theta^k$ maps cusp forms of weight $8k u_1'$ to cusp forms of weight $8k u_1$. To control heights, $\theta$ must be integral up to a small error at every finite place, and its norm must be small compared with the Bergman kernel at every infinite place. This section constructs such a section from a theta function. The main steps are a lower bound for the Bergman kernel on the thick part of the frames, an upper bound for the norm of a theta function, and a comparison of the two. The result is the multiplicity input of [the height lower bound](/entry/height-lower-bound-general-alt/).

We fix a family, a point $p$, a level $i$ with $i + 1 < m$, a good cover $Y$ at level $i + 1$ with moduli space $X^\circ$ over the coefficient field $F$, and a quotient weight $u_1$ (as in [the reference bound](/entry/refined-sum-weight-of-size-alt/)). Let $T$ be the length, $E$ the unit of error and $M$ the level of $Y$. For a complex embedding $\sigma$ of $F$ that is good, $Y$ has a uniformization $U_\sigma$. Its framed points $y$ have a lattice with a frame, and $\lambda_1(y)$ is the first minimum of that lattice ([hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes)). For a component $Z$, the frames on $Z$ are the frames of the points over $Z$.

We use the following analytic objects, which we do not unfold.

- The *Bergman function* $\beta_Z(y) \in [0, \infty]$ of the weight $u_1$ on $Z$ at the framed point $y$, for the hermitian structure of the cover at $\sigma$. By its name and its use, this is the Bergman kernel on the diagonal: the largest value of $|f(y)|^2$ over cusp forms $f$ of norm $1$.
- The *pointwise norm* $\|f\|_y$ of a modular form $f$ of a given weight at a frame $y$.
- *Theta rules*: for a family $x = (x_1, \dots, x_{p+q})$ of vectors in the lattice modulo $5^4$, the rules $f$ that are theta functions of $x$ with the parameter $5$.

**Theorem 2.6.1 (Bergman kernel on the thick part).** Assume the published Hodge bundle theorems, the inputs on toroidal compactifications, deep goodness, the size condition and the flat degree condition. Then the following cover statement holds. For every quotient weight $u_1$ there is $B \ge 0$ with $T B \le C E$ such that for every component $Z$, every good embedding $\sigma$ and every framed point $y$ whose frame lies on $Z$ and satisfies
$$b \le M \lambda_1(y)^2,$$
we have
$$e^{-B} \le \beta_Z(y).$$

Lean: `GlobalTheory.ThickBerg.exp_neg_B_le_bergOn_of_mem_framesOn` (also `GlobalTheory.T.exp_neg_B_le_bergOn_of_la1sq_bound`, a second name).

The condition $b \le M \lambda_1(y)^2$ says that $y$ lies in the thick part: the lattice at $y$ has no short vectors at the scale $b / M$.

*Proof.* There is a constant $C_0 \ge 0$, from a peak section lemma: at each frame of an injective chart there is a cusp form that peaks at $y$, with norm controlled by $C_0$. Put
$$B = C_0 \bigl( \ell_1(u_1) + (f r)^8 \bigr),$$
where $\ell_1(u_1) = \sum_{\tau, k} |u_{1, \tau, k}|$. The size condition gives a lower bound for the length $T$ in terms of the weights of the quotient, and the host numerics bound the remaining parameters; together they give $T B \le C E$. On the thick part, a ball around $y$ of a fixed radius injects into the quotient. The peak section at $y$, restricted to the component, is a cusp form whose value at $y$ is at least $e^{-B}$ times its norm. The cusp form lower bound for the Bergman function then gives $e^{-B} \le \beta_Z(y)$; the orthogonal transfer between the model weight and the weight $u_1$ keeps the shape of the bound. $\square$

The next result compares a theta function with the Bergman function at every point, thick or thin.

**Theorem 2.6.2 (Theta functions and the Bergman kernel).** Under the same hypotheses, the following cover statement holds. For every quotient weight $u_1$ there is $\beta \ge 0$ with $T \beta \le C E$ such that for every component $Z$, every family $x$ of $p + q$ vectors of the lattice modulo $5^4$ that spans it over $\mathcal{O}_E$, every theta rule $f$ of $x$, every good embedding $\sigma$ and every framed point $y$ whose frame lies on $Z$:
$$\|f^2\|_y \le e^{\beta}, \qquad \|f^2\|_y^3 \le e^{\beta}\, \beta_Z(y).$$
Here $f^2$ has weight $0$ in the first part and $2(p+q)$ in the second part of its bidegree.

Lean: `GlobalTheory.CovHt.KeySection.theta_function_le_bergman_kernel_alt`.

*Proof.* Three level statements enter: an eta bound in terms of the length and the unit, the thin part estimate for the Bergman kernel, and the thick part estimate above with its constant $B$. The theta constants of spanning classes give the bound $\|f^2\|_y \le e^{s}$ with an exponent $s$ that is controlled by the eta bound; put $\beta = P_\eta + B$, where $P_\eta$ is the constant of the eta bound. Then $T \beta \le C E$. The first inequality holds because $s \le \beta$. For the second, we use an elementary lemma:
$$a \le e^{s}, \quad 3 s \le P_\eta + B + t, \quad e^{t} \le G \implies a^3 \le e^{P_\eta + B} G.$$
On the thick part, $b \le M \lambda_1(y)^2$, we take $t = -B$ and $G = \beta_Z(y)$ by the previous theorem. On the thin part, $M \lambda_1(y)^2 < b$, the thin part estimate gives the value of $t$ and the lower bound $e^t \le \beta_Z(y)$. In both cases the lemma gives $\|f^2\|_y^3 \le e^{\beta} \beta_Z(y)$. $\square$

Now we construct the carrying section. Let $\lambda_H$ be the Hodge weight and put
$$u_1' = u_1 - 3(p + q) \lambda_H.$$
Entrywise, $u'_{1, \tau, k} = u_{1, \tau, k}$ for $k < p$ and $u'_{1, \tau, k} = u_{1, \tau, k} + 3(p+q)$ for $k \ge p$.

**Definition 2.6.3 (Carrying section).** Let $Z$ be a component, $u$ and $u'$ weights. A modular form $\theta$ *carries* $u'$ to $u$ on $Z$ if $\theta$ is a section of weight $8(u - u')$, its value at the generic point of $Z$ is not zero, and for every $k \ge 0$ and every cusp form $f$ of weight $8 k u'$ on $Z$, the product $\theta^k f$ is a cusp form of weight $8 k u$ on $Z$.

The integrality of $\theta$ at the finite places is measured as follows. Let $\lambda$ be a finite place of $F$. Let $R$ be a complete discrete valuation ring with an embedding of $F$ over $\lambda$ and an index $e_0 \ge 1$, and let $y$ be an integral framed point over $R$ that is algebraic. We write $v_{e_0}$ for the valuation of $R$ scaled by $e_0$, and $\phi_y$ for a number attached to $y$ (its slope at $\lambda$), which we do not unfold.

**Theorem 2.6.4 (A carrying section with bounded cost).** Under the same hypotheses, the following cover statement holds. For every quotient weight $u_1$ there is $c \ge 0$ with $T c \le C E$ such that for every component $Z$ there are a modular form $\theta$, a finitely supported function $e$ on the finite places of $F$ and a function $t$ on the complex embeddings of $F$ with:

1. $\theta$ carries $u_1'$ to $u_1$ on $Z$;
2. for every finite place $\lambda$, every $R$, $e_0$ and integral algebraic framed point $y$ as above at which some cusp form on $Z$ does not vanish, and every $\phi$ attached to $y$,
$$\frac{8}{2500} \cdot \frac{\phi}{e_0} - 8 e_\lambda \le v_{e_0}\bigl(\theta(y)\bigr);$$
3. at the infinite places, $\theta$ satisfies the bound $\mathrm{Inf}(t)$ for the weights $u_1$ and $8(u_1 - u_1')$ with the factor $8$;
4. the cost of $(e, t)$ is at most $c$.

Lean: `GlobalTheory.CovHt.KeySection.cover_height_section_bound_alt` (also `GlobalTheory.T.exists_section_bounded_by_bergman_kernel_alt`, a second name).

*Proof.* Take the constant $\beta$ of [Theorem 2.6.2](/entry/theta-function-le-bergman-kernel-alt/) and put $c = \beta / 2 + 10 P$. The level $M$ is divisible by $15^L$ for a large $L$, so $5^4$ divides $M$, and the lattice modulo $5^4$ is defined at the level. The flat degree condition gives a twist: a character twist of a theta rule of a spanning family, with weight $8(u_1 - u_1')$, that carries $u_1'$ to $u_1$. We take $\theta$ to be this section. The finite bound with the function $e$ comes from the integrality of the theta rule at the places outside a finite set and from the twist at the places inside it. The infinite bound with the function $t$ comes from the comparison of $\|f^2\|_y$ with the Bergman function in the previous theorem: with $\|f^2\|_y \le e^{\beta}$, the eighth power of the section has norm at most $e^{4\beta}$ times the factor of the twist. The cost of the twist is at most $\beta / 2 + 10 P$. $\square$

**Remark 2.6.5 (Formalization).** The thick part estimate takes five hypotheses and starts with `intro _ _ _ hS _`, so it uses only the size condition ([BergmanKernelThickPartEstimate.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BergmanKernelThickPartEstimate.lean#L17)); its second name is at line 87, and a copy of the file is also under `HodgeBundleWeights`. In that proof $B = C_0(\ell_1(u_1) + (f r)^8)$, with $C_0$ from `exists_cusp_form_peak_at_injective_chart_frame`, and the steps use `torus_length_lower_bound_quotient'`, `hostN_alt`, `wtN_z`, `cuspForm_lower_bound_bergmanFunction_on_component`, `orth_transfer`, `modelWt_shape` and `ball_injects`; we know these by their statements and names. The theta comparison and the carrying section are at [ExistsSectionBoundedByBergmanKernel.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsSectionBoundedByBergmanKernel.lean#L24) and line 75, with the second name at line 123; the carrying section uses `exists_twist`, `exists_section` and `twist_cost_le`. We have not unfolded `bergOn`, `homN`, `IsTauRule`, `framesOn`, `HasPhi`, `OverLa` or `nval`, so the description of the Bergman function is by name here. The infinite bound `InfBd` and the cost `cost` are unfolded in [the next section but one](/entry/height-lower-bound-general-alt/). The description of how the twist gives the finite and infinite bounds follows the inputs of the proof, not an unfolding of them.
