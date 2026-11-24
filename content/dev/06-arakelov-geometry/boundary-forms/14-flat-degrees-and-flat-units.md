---
title: Flat degrees and flat units
decls:
  - GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt
  - GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints
  - GlobalTheory.FlatDenom.unit_pow_clears_denominator_flat_model
  - GlobalTheory.FlatUnitInt.flat_unit_inverse_integral
  - GlobalTheory.T.inverse_of_flat_unit_isIntegral
  - GlobalTheory.FlatUnit.exists_flat_unit_section
  - GlobalTheory.T.detLine_flat_unit_exists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Flat degrees and flat units

[The section on flat sections](/entry/flat-exists-at-core-alt/) computed the degree of a flat section at the last level of the tower. This section does two things at the other levels. First, it proves the *flat degree condition*: on every good cover, flat sections exist and have degree equal to the flat degree value $\phi$. Second, it builds *flat units*: for every parallel weight, a modular form $\varphi$ of that weight with an inverse $\varphi'$ up to a nonzero constant, with $\varphi'$ integral at all finite places and $\varphi$ bounded at the archimedean places. The flat units let one shift a weight by a parallel weight without changing the size of cusp forms, and they are used in [the next section](/entry/exists-pow-mul-mem-cusp-forms-of-weight-match/) to match weights.

We keep the notation of [the section on flat sections](/entry/deg-lie-core-alt/). For a CM field $E$ with a Kronecker character $\chi$, write $\log \Omega(E, \chi)$ for the logarithmic period there, and $\phi(\log \Omega) = \frac{p - q}{2} \log \Omega$ for the flat degree value of a datum of signature $(p, q)$.

**Definition 2.14.1 (Flat degree condition).** A good cover $Y$ satisfies the *flat degree statement* with period $\log \Omega$ if, for each component $Z$ and each $\tau \in \Psi$, there is a flat section on $Z$ at $\tau$, and every flat section $s$ on $Z$ at $\tau$ has $\deg s = \phi(\log \Omega)$. The *flat degree condition* is the cover statement that every good cover at every point and level satisfies the flat degree statement with the period of the host of its record.

**Theorem 2.14.2 (The flat degree condition).** Assume the published Hodge bundle theorems. Then the flat degree condition holds.

Lean: `GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt` (also `GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints`, a second name).

*Proof.* We first prove a uniform statement: for every CM host field $E$ with a Kronecker character $\chi$, every datum and level, and every family of uniformizations that satisfies the laws of a good cover, the flat degree statement holds with period $\operatorname{Re} \log \Omega(E, \chi)$. This statement is proved by resolution of singularities in characteristic zero and principalization, as explained in the Notes and references. On a good cover the laws hold, and the logarithmic period of the record equals the period of the Kronecker character of the host. So each good cover satisfies the flat degree statement. The constants of the cover statement are all $0$. $\square$

Now the flat units. Let $D$ be a family with a core, let $Y$ be a deep good cover at level $j$, and assume $[E : \mathbb{Q}]/2 > 2$. For $\tau \in \Psi$ let $\varpi_\tau$ be the *flat weight* at $\tau$, the weight of a flat section at $\tau$. For a function $w \colon \Psi \to \mathbb{Z}$, the *parallel weight* of $w$ is
$$\operatorname{par}(w) = \sum_{\tau \in \Psi} (-w_\tau)\, \varpi_\tau.$$
Let $e_Z$ be the idempotent of the component $Z$ in the ring of rules: $e_Z$ is $1$ on $Z$ and $0$ on the other components. A rule $s$ is *supported on* $Z$ if $e_Z s = s$. For a component $Z$ and a weight $\lambda$, let $\operatorname{Val}_Z(\lambda)$ be the set of valuations that record the finite places on $Z$ in weight $\lambda$, and $\operatorname{Val}(\lambda)$ the set over all components. We say that a rule $f$ is *integral* at $v$ if $v(f) \ge 0$. At a good embedding $\sigma$ of $F$, the frames on $Z$ carry a pointwise norm $|s|_z$ of a rule $s$ of a weight, built from the Hodge metric.

**Definition 2.14.3 (Flat unit pair).** Let $Z$ be a component, $\tau \in \Psi$ and $n \in \mathbb{Z}$. A *flat unit pair* on $Z$ of weight $n \varpi_\tau$ is a pair of rules $(s, i)$ such that $s$ has weight $n \varpi_\tau$, $i$ has weight $-n \varpi_\tau$, both are supported on $Z$, $s i = e_Z$, and for every good embedding $\sigma$ there is $C$ with $|s|_z \le C$ and $|i|_z \le C$ at all frames $z$ on $Z$.

A flat unit pair is an invertible section of a flat line bundle, bounded at infinity together with its inverse. Its denominators at the finite places are the only remaining defect, and the next theorem clears them.

**Theorem 2.14.4 (Flat units have integral multiples).** Assume the published Hodge bundle theorems. Let $Y$ be a deep good cover with $[E : \mathbb{Q}]/2 > 2$, and let $(s, i)$ be a flat unit pair on $Z$ of weight $n \varpi_\tau$. Then there is an integer $m > 0$ such that $m s$ and $m i$ are integral at every valuation of $\operatorname{Val}_Z(\lambda)$, for every weight $\lambda$.

Lean: `GlobalTheory.FlatDenom.unit_pow_clears_denominator_flat_model` (also `GlobalTheory.FlatUnitInt.flat_unit_inverse_integral` and `GlobalTheory.T.inverse_of_flat_unit_isIntegral`, second names).

*Proof.* There is a reference pair with known denominators. The published list gives, on the flat model of $Z$, a horizontal nowhere vanishing section of the flat line bundle of weight $\varpi_\tau$, and with the boundary units at integral points this gives an *archimedean section*: a rule $s_0$ of weight $\varpi_\tau$ with an inverse $s_0^{-1}$ of weight $-\varpi_\tau$, supported on $Z$, whose pointwise norm is a constant $c_\sigma > 0$ on the frames at each good $\sigma$, together with $m_0 > 0$ such that $m_0 s_0$ and $m_0 s_0^{-1}$ are integral. Taking $n$-th powers gives such a pair $(s_0, s_0^{-1})$ of weight $n \varpi_\tau$, with a new $m_0$.

Put $g = s \, s_0^{-1}$ and $h = i \, s_0$. Both have weight $0$, are supported on $Z$, and $g h = (s i)(s_0 s_0^{-1}) = e_Z$. Their norms are bounded on the frames: $|g|_z = |s|_z \, c_\sigma^{-1} \le C c_\sigma^{-1}$ and $|h|_z \le C c_\sigma$. By the Koecher principle, a bounded rule of weight $0$ that is a unit on a component is constant there ([toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications)). So $g = a e_Z$ with $a \in F$, and $s = a s_0$. If $a = 0$ then $e_Z = s i = 0$, and a recording valuation of $e_Z$ would have value $+\infty$ and $0$ at once, which is absurd. So $a \ne 0$ and $i = a^{-1} s_0^{-1}$. Choose integers $n_1, n_2 > 0$ with $n_1 a$ and $n_2 a^{-1}$ integral at every finite place. Then $m = n_2 n_1 m_0$ works: $m s = n_2 (n_1 a)(m_0 s_0)$ and $m i = n_1 (n_2 a^{-1})(m_0 s_0^{-1})$ are products of integral factors. $\square$

**Theorem 2.14.5 (Flat unit sections).** Assume the published Hodge bundle theorems. Let $Y$ be a deep good cover with $[E : \mathbb{Q}]/2 > 2$. Then there is an integer $N > 0$ such that for every $w \colon \Psi \to \mathbb{Z}$ there are rules $\varphi, \varphi'$ and $t \in F$ with:

1. $\varphi$ is a section of the parallel weight $\operatorname{par}(N w)$;
2. $t \ne 0$ and $\varphi \varphi' = t \cdot 1$;
3. $\varphi'$ is integral at every valuation of $\operatorname{Val}(\lambda)$, for every weight $\lambda$;
4. for every good embedding $\sigma$ and every chart $k$ of the uniformization, the norm of $\varphi$ in the model weight is bounded by a constant on the domain of the chart.

Lean: `GlobalTheory.FlatUnit.exists_flat_unit_section` (also `GlobalTheory.T.detLine_flat_unit_exists`, a second name).

*Proof.* A cover statement of the published list gives $N > 0$ and, for each component $Z$ and each $\tau$, a flat unit pair $(s_{Z, \tau}, i_{Z, \tau})$ on $Z$ of weight $N \varpi_\tau$. The previous theorem gives $m_{Z, \tau} > 0$ that makes both integral. Fix $w$. On each $Z$, the products
$$s_Z = \prod_\tau s_{Z, \tau}^{-w_\tau}, \qquad t_Z = \prod_\tau i_{Z, \tau}^{-w_\tau},$$
with negative exponents read through the inverse of the pair, form a flat unit pair on $Z$ of weight $\operatorname{par}(N w)$, bounded at infinity, with an integer $m_Z > 0$ that makes both integral. Put
$$\varphi = \sum_Z s_Z, \qquad t = \prod_Z m_Z, \qquad \varphi' = t \sum_Z t_Z.$$
The components are finite in number, so $t \ne 0$ in $F$. Since $s_Z t_{Z'} = 0$ for $Z \ne Z'$ and $s_Z t_Z = e_Z$, we get $\varphi \varphi' = t \sum_Z e_Z = t \cdot 1$. Each $t \, t_Z$ is an integer multiple of the integral rule $m_Z t_Z$, so $\varphi'$ is integral. The bound at infinity of each $s_Z$ on the frames gives the bound of $\varphi$ on each chart, with constant the sum over $Z$ of the positive parts of the bounds of the $s_Z$, divided by the Lie factor of $Z$. $\square$

**Remark 2.14.6 (Formalization).** The flat degree theorem is a one-line proof from `UpperTheory.Lit.Flat.flat_tensor_swap_isIso`, discussed in the Notes and references, and it fills in the parameters of the cover statement with the constants $1$ and $0$ ([FlatDegreeStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean#L12)). Its second name, at line 22, refers to Scholze and Weinstein, although no result of theirs is used. The flat degree statement is `FlatDegree U x logOm`, that is, `FlatExistsAt U x (-flatDegVal Dw logOm)`, which asks for degree $\phi$ as in the section on flat sections. The Koecher principle is used in the form `CovTop.koecher_principle_unit_constant` (ExistsArchimedeanSectionWithDenominator.lean, line 111), and the archimedean section comes from line 47 of the same file. The pointwise norm `homN`, the valuation sets `valOn` and `valSet`, and the flat weight `flatWt` are not unfolded. The products over $\tau$ are formed by `exists_boundedUnit_sum_component`, whose proof we did not read.
