---
title: The Hilbert-Samuel bound on components
decls:
  - GlobalTheory.HSShortRun.hilbertSamuel_estimate_at_level
  - GlobalTheory.HSShortRun.hsClaim_short_alt_alt
  - GlobalTheory.T.exists_degree_parameters_bound_alt_alt
  - GlobalTheory.CovTop.ShortRoad.hilbertSamuel_of_component_estimates_alt
  - GlobalTheory.T.coverHeightSum_of_flatDeg_coverDegree_share
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hilbert-Samuel bound on components

The height lower bound needs a lower bound for the degree of the lattice of cusp forms of the weight of the level, on each component of a good cover. This is an arithmetic Hilbert-Samuel bound: the degree grows like the length $T$ times the height of the component, up to errors of smaller order ([arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness)). This section proves it in three steps. First, on one cover and for one path of weights, a short basis argument gives an explicit inequality with many parameters. Second, the parameters are bounded uniformly over the family. Third, the inequality is turned into the cover height sum condition, the form in which the bound enters [the height lower bound](/entry/height-lower-bound-general-alt/).

We fix a family, a point $p$, a level $i$ with $i + 1 < m$ and a good cover $Y$ at level $i + 1$. Let $d$ be the flag dimension of the datum at level $i + 1$, $T$ the length and $E$ the unit of error, as in [the first section](/entry/to-classical-theorems/). For a weight $u$ and a component $Z$ of the moduli space of $Y$ we write:

- $\delta_Z(u) \in \mathbb{N}$ for the generic degree of $u$ on $Z$;
- $h_Z(u) \in \mathbb{R}$ for the height of $Z$ with respect to $u$;
- $r_Z(u)$ and $\deg_Z(u)$ for the rank and the Arakelov degree of the lattice of cusp forms of weight $u$ on $Z$ ([hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes)).

We do not unfold the generic degree or the height. A *weight path* $\Pi$ is a sequence of weights $w_0, \dots, w_T$ together with two weights $u_1$ and $u_2$; the path is *big* if its gaps are large enough. A *cusp frame* of weight $u$ on $Z$ is a family of $n$ cusp forms with a matrix at each complex embedding.

**Definition 2.7.1 (Hilbert-Samuel claim).** Let $C > 0$, $T, D \in \mathbb{N}$, and let $n, j_0, \Lambda, \beta, \Lambda_D, \Lambda_T, J, \delta, h, r, g$ be real numbers. Put
$$\begin{aligned} G &= \tfrac{1}{2}(D + 1)(\log n + 1) + 1, \qquad R = \tbinom{T - 1}{D}, \qquad z = 1 - \frac{R \delta}{r}, \\ \rho &= \log \Lambda + C \log\bigl( n D j_0 \delta (2 + |h| + \log \Lambda) \bigr). \end{aligned}$$
The *Hilbert-Samuel claim* says that $0 \le z \le 1$ and
$$\begin{aligned} & (1 - z) \Bigl( T h - 3(D + 1) |h| - J - C D^2 \log(e^{\rho} T) \\ & \qquad - (T + D + 1) \log \beta - (T + D^2)(G + 2) \Bigr) \\ & \quad - z \bigl( T \log(2 e^{\rho} \sqrt{\beta}) + \log \Lambda_D + \log \Lambda_T \bigr) \le \frac{g}{r}. \end{aligned}$$

We use it with $C = 26$, $D = d$, $j_0 = 1$, $\delta = \delta_Z(u_1)$, $h = h_Z(u_1)$, $r = r_Z(w_T)$ and $g = \deg_Z(w_T)$. Then $g / r$ is the slope of the lattice of cusp forms of the last weight of the path, and the main term on the left is $(1 - z) T h$.

**Theorem 2.7.2 (Hilbert-Samuel estimate on one cover).** Assume the hypotheses of the second kind on the family, Grothendieck's deformation theory, the quoted results, Nadel vanishing, principalisation, the toroidal integral, the toroidal charts for fans and the seminegativity of the Lie algebra. Let $Y$ be good, with $[E : \mathbb{Q}] / 2 > 2$. Let $Z$ be a component and $\Pi$ a big weight path of length $T$ such that $Y$ is good at each weight $w_j$, $j \le T$. Let $P_0, \kappa \ge 0$. Let $f_1$ and $f_2$ be cusp frames of weights $u_1$ and $u_2$, with $f_1$ of size $n$, and let $\Lambda, \beta \ge 1$ such that:

1. the frame norms of $f_1$ are at most $\Lambda$ at every embedding;
2. the Bergman kernel bound with constant $\beta$ holds for $u_1$ on $Z$;
3. the cusp forms of weights $u_1$ and $u_2$ are birational on $Z$;
4. the lattice of cusp forms of weight $w_0$ is spanned by lattice vectors of Petersson norm at most $e^{d P_0 (\kappa / T + 1)}$;
5. for each $j \le T$, the lattice of cusp forms of weight $w_j$ is spanned by lattice vectors of Petersson norm at most $e^{P_0 \kappa}$.

Then $1 \le n$, and the Hilbert-Samuel claim holds with $\Lambda_D = \Lambda_T = e^{P_0 \kappa}$ and $J = d P_0 (\kappa / T + 1)$.

Lean: `GlobalTheory.HSShortRun.hilbertSamuel_estimate_at_level`.

*Proof.* The published inputs give a toroidal model of $Z$, a modification of it and a hermitian Hodge bundle on the model that is generated at the weights of the path. On this model the cusp form ratios of weights $u_1$ and $u_2$ generate the function field at the generic point, by the birationality hypothesis. The spanning families of hypotheses 4 and 5 give short families at the steps $0$, $d$ and $T$ of the path; the inequality $d \le T$ comes from the path. These data verify the hermitian geometric hypothesis of the short basis bound, which is [Theorem 3.12](/entry/hilbert-samuel-component-short-basis-bound/) of an earlier chapter. Its conclusion is the claim for the degree of the lattice of weight $w_T$, with $\log e^{d P_0 (\kappa / T + 1)} = d P_0 (\kappa / T + 1)$ as the term $J$. The rank in it is the dimension of the space of cusp forms of weight $w_T$, since the lattice is of full rank by goodness. The frame size satisfies $1 \le n$ by the geometric data. $\square$

Now the parameters. Let $\kappa$ be the size of the column weight of the level, a sum of absolute values, so $\kappa \ge 0$. Let $P$ be the parameter of the family at the point. The *standard path* at $(p, i)$ is the weight path with start $u_W$, the base character, $k - 2$ steps of the inner index and length $T$. Its weight $u_1$ is the quotient weight of the level.

**Theorem 2.7.3 (Bounded Hilbert-Samuel parameters).** Assume the hypotheses on the family, the published Hodge bundle theorems, Grothendieck's deformation theory, the quoted results, the toroidal integral, the toroidal compactifications, the seminegativity of the Lie algebra, deep goodness, the size condition and the flat degree condition. Then the following cover statement holds. For every good cover $Y$ and every component $Z$ there are $n, \Lambda, \beta, \Lambda_D, \Lambda_T, J \ge 1$ with
$$\log n, \ \log \beta, \ \log \delta_Z(u_1) \le P, \qquad \log \Lambda \le P \Bigl( \frac{\kappa}{T} + 1 \Bigr), \qquad \log \Lambda_D, \ \log \Lambda_T \le P \kappa,$$
$$J \le 4 \Bigl( d P \Bigl( \frac{\kappa}{T} + 1 \Bigr) + T P \Bigr) + 2 P \frac{\kappa}{T} d,$$
such that the Hilbert-Samuel claim holds for the standard path on $Z$.

Lean: `GlobalTheory.HSShortRun.hsClaim_short_alt_alt` (also `GlobalTheory.T.exists_degree_parameters_bound_alt_alt`, a second name).

*Proof.* Eight cover statements are combined. They give: cusp frames $f_1$ and $f_2$ for the standard path with constants $\Lambda$ and $\beta$, the frame bound, the Bergman kernel bound, and $\log n, \log \beta \le P$, $\log \Lambda \le P(\kappa / T + 1)$; birationality on both weights; the bound $\log \delta_Z(u_1) \le P$, which uses the flat degree condition; bigness of the standard path; the gap and size bounds for the family; the spanning families with Petersson norms at most $e^{P \kappa}$ along the path and $e^{d P(\kappa/T+1)}$ at the start. The regularity of the covering domain lattice gives the goodness of $Y$ at each weight of the path. The constant of the cover statement is $0$. At each cover and component, the previous theorem applies, with $\Lambda_D = \Lambda_T = e^{P \kappa}$ and $J = d P (\kappa / T + 1)$. The bound on $J$ holds since the other terms on the right are nonnegative. $\square$

The constant of this cover statement is $0$, because all its bounds are in terms of $P$, $\kappa$ and $T$, not $E$.

**Theorem 2.7.4 (The cover height sum).** Assume the hypotheses of the previous theorem, the cover degree condition and the share condition. Then the cover height sum condition holds: there is a constant $C$ such that, as a cover statement, for every quotient weight $u_1$ there are $A > 0$ and $R \ge 0$ with
$$A \log \max(A, 1) + R \le C E,$$
and for every component $Z$, with $h = h_Z(u_1)$, $\delta = \delta_Z(u_1)$ and $b_T = \binom{T-1}{d}$,
$$b_T \, \delta \bigl( T h - 3(d + 1) |h| - A \log(2 + |h|) - R \bigr) \le \deg_Z(u_M).$$
Here $u_M$ is the weight of the level.

Lean: `GlobalTheory.CovTop.ShortRoad.hilbertSamuel_of_component_estimates_alt` (also `GlobalTheory.T.coverHeightSum_of_flatDeg_coverDegree_share`, a second name).

*Proof.* The published list gives a constant $C_p \ge 0$ of a lower bound for the degree of twisted bundles, and the ranks of twisted flat bundles. Take $C = 10000 + 2 C_p$. Fix a point, a level, a good cover $Y$ and a quotient weight $u_1$. The quotient weight is unique, so $u_1$ is the weight of the standard path, and the last weight of the path is $u_M$. Let $\zeta$ be the exponent of the first section and $z_0 \ge 1$ the base of the host numerics. The host numerics give $z_0^{12} \le P$ and $T P \le \sqrt{b}$, so $z_0^2 \le b$, and the size condition gives $1 \le b \le E$. Put
$$A = 26 \bigl( 26 d^2 + 2 \zeta T \bigr), \qquad R = 4000 b + 2 C_p z_0^2.$$
An elementary estimate bounds $A \log \max(A, 1)$ by a multiple of $b$, and this gives $A \log \max(A, 1) + R \le C E$. Now fix a component $Z$. By the cover degree condition $0 < \delta_Z(u_1)$, and as the generic degree is an integer, $\delta_Z(u_1) \ge 1$. By the share condition,
$$(1 - \zeta) \, r_Z(u_M) \le b_T \, \delta_Z(u_1) \le r_Z(u_M),$$
so $r_Z(u_M) > 0$. The twisted bundle bound compares the degree of the lattice of weight $u_M$ with the degree of a twisted flat bundle, with an error $C_p z_0^2$. The previous theorem gives the Hilbert-Samuel claim with bounded parameters. A numerical lemma combines the claim, the parameter bounds, the share condition, the bound $\rho_B(u_1) < 1$ and $\zeta < 1$ of the size condition and the twisted bound into the inequality above. $\square$

The proof shows the role of the share condition: it turns the factor $1 - z = b_T \delta / r$ of the claim into the factor $b_T \delta$ of the cover height sum, up to an error that $\zeta$ controls.

**Remark 2.7.5 (Formalization).** In the estimate on one cover ([ExistsDegreeParametersBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsDegreeParametersBound.lean#L33)), the constants of the data are set with a field `0` at line 55, and the section used in the data is `th := 0` at line 56; the conclusion does not depend on them. That file also holds an older `hsClaim_short_alt`. The bounded parameters are in [ExistsDegreeParametersBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsDegreeParametersBound.lean#L34): the cover constant is `0` (`refine ⟨0, le_rfl, …⟩`), and the bound on `J` is weak, since `J` is $d P(\kappa/T + 1)$ and the bound is closed by `linarith`. Its second name at line 84 restates the whole statement on one long line and is proved by `first`. The cover height sum is at [HilbertSamuelLowerBoundOfComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HilbertSamuelLowerBoundOfComponents.lean#L25), with its second name at line 128; it uses `obtain rfl := hqe u1 hu1`, so the quotient weight is determined by the level. Its last step is `GlobalTheory.CovHSNum.deg_bound_of_claim_numbers`, the bound on $A$ is `GlobalTheory.hilbertSamuel_ALogA_le`, and the twisted bounds are `twisted_bundle_degree_lower_bound` and `twisted_flat_bundle_ranks`. We have not unfolded the generic degree `Deep.dg`, the height `Deep.ht`, the weight paths `WtPar`, `WtBig`, `CuspFrame`, `BergLe`, `BirOn` or the base `zBase`; their descriptions follow their names and uses. A copy of the cover height sum is also under `HodgeBundleWeights`.
