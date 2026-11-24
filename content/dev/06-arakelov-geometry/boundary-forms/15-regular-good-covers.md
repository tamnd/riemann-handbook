---
title: Regularity of good covers
decls:
  - GlobalTheory.WtMatchBar.exists_pow_mul_mem_cuspForms_of_weight_match
  - GlobalTheory.T.weight_match_pow_mul_cuspidal
  - GlobalTheory.CovTop.GoodDom.weight_lattice_span_on_domain
  - GlobalTheory.CovTop.GoodDom.covering_regular_at_domain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Regularity of good covers

The lattice of a weight on a good cover is the set of cusp forms of that weight that are integral at all finite places. The volume arguments of this chapter need it to be a lattice in the strict sense: finitely generated, of full rank, and with a Gram form at the archimedean places ([hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes)). This section proves this for every weight whose rows are decreasing and have a positive gap at the place of the signature. The key point is full rank: every cusp form has an integral multiple. It is proved by multiplying a power of the form with a flat unit of [the previous section](/entry/exists-flat-unit-section/) into a space of cusp forms where the denominators are under control, and then dividing again.

Let $D$ be a family with a core, $Y$ a deep good cover at level $j$ with $[E : \mathbb{Q}]/2 > 2$, and let the datum at level $j$ have signature $(p, q)$ with $p, q \ge 1$. For a weight $\lambda$ we write $V(\lambda)$ for the space of cusp forms of weight $\lambda$ on the cover, an $F$-vector space. Let $\operatorname{Val}(\lambda)$ be the set of recording valuations of [the previous section](/entry/flat-unit-inverse-integral/).

**Definition 2.15.1 (Weight lattice).** The *lattice of weight* $\lambda$ is
$$\Lambda(\lambda) = \{ f \in V(\lambda) : v(f) \ge 0 \text{ for every } v \in \operatorname{Val}(\mu) \text{ and every weight } \mu \}.$$
It is a module over the ring of integers $\mathcal{O}_F$.

A weight $\lambda$ has rows $\lambda_\tau = (\lambda_{\tau, 1}, \dots, \lambda_{\tau, p + q})$ for $\tau \in \Psi$. We say that $\lambda$ is *admissible* if each row is decreasing, $\lambda_{\tau, 1} \ge \lambda_{\tau, 2} \ge \cdots$, and the gap at $p$ is positive: $\lambda_{\tau, p} - \lambda_{\tau, p + 1} \ge 1$ for each $\tau$.

There is a second family of spaces, indexed by exponents. For a function $a \colon \operatorname{Hom}(E, \mathbb{C}) \times \mathbb{N} \to \mathbb{N}$ and an integer $n$, let $\mathcal{S}(a, n)$ be the space of cusp forms with exponent $a$ and parameter $n$. The pair $(a, n)$ is *dominant* if $i \mapsto a(\tau, i)$ is decreasing for each $\tau$ and $n$ is even. On these spaces the finite denominators are bounded in advance: for dominant $(a, n)$ with $n$ large enough, every element of $\mathcal{S}(a, n)$ has, after multiplication by a nonzero constant, nonnegative value at every recording valuation.

**Theorem 2.15.2 (Weight matching).** Assume the published Hodge bundle theorems. Let $\lambda$ be admissible, and let $f \in V(\lambda)$. Then there are an integer $k \ge 0$, a dominant pair $(a, n)$ with
$$n \ge 4 \bigl([E : \mathbb{Q}] \, r\bigr) + 4,$$
rules $g$ and $h$, and $t \in F$, such that
$$f^{k + 1} g \in \mathcal{S}(a, n), \qquad t \ne 0, \qquad g h = t \cdot 1,$$
and $h$ is integral at every recording valuation. Here $r$ is the rank of the family.

Lean: `GlobalTheory.WtMatchBar.exists_pow_mul_mem_cuspForms_of_weight_match` (also `GlobalTheory.T.weight_match_pow_mul_cuspidal`, a second name).

*Proof.* Two kinds of units are used. The first is an invariant unit: there are rules $u, u'$ and $t_1 \ne 0$ with $u$ a modular form, $u u' = t_1 \cdot 1$ and $u'$ integral at every recording valuation. The second is the family of [flat unit sections](/entry/exists-flat-unit-section/), with its integer $N > 0$. Put $M = 4([E : \mathbb{Q}] r) + 4$. The pair $(u^M, u'^M)$ is again a unit pair, with $u^M u'^M = t_1^M \cdot 1$.

A cover statement on products with units gives an integer $K$ with the following property: for every $k \ge K$, every flat unit $(\varphi, \varphi', t_2)$ that is bounded at infinity and every dominant $(a, 2M)$, if $f^{k + 1} u^M \varphi$ has the weight of $\mathcal{S}(a, 2M)$, then it lies in $\mathcal{S}(a, 2M)$. Take $k = \max(K, 2M + N)$. A combinatorial lemma on weights now matches the weight: since $\lambda$ is admissible and $k \ge 2M + N$, there are $w \colon \Psi \to \mathbb{Z}$ and a dominant $(a, 2M)$ such that $(k + 1)\lambda + M \cdot \mathrm{wt}(u) + \operatorname{par}(N w)$ is the weight of $\mathcal{S}(a, 2M)$. Take the flat unit $(\varphi, \varphi', t_2)$ of the parallel weight $\operatorname{par}(N w)$. Then
$$g = u^M \varphi, \qquad h = u'^M \varphi', \qquad t = t_1^M t_2, \qquad n = 2M$$
work. Indeed, $f^{k+1} g \in \mathcal{S}(a, n)$ by the choice of $K$, $g h = (u u')^M (\varphi \varphi') = t_1^M t_2 \cdot 1$, and $t \ne 0$. At each recording valuation $v$, $v(h) = M v(u') + v(\varphi') \ge 0$. $\square$

**Theorem 2.15.3 (Full rank of the weight lattice).** Under the hypotheses of the previous theorem, the lattice $\Lambda(\lambda)$ spans $V(\lambda)$ over $F$.

Lean: `GlobalTheory.CovTop.GoodDom.weight_lattice_span_on_domain`.

*Proof.* Let $f \in V(\lambda)$, and take $k, a, n, g, h, t$ from the previous theorem. Since $(a, n)$ is dominant and $n$ is large, there is $s \ne 0$ in $F$ such that $s \, f^{k + 1} g$ is integral at every recording valuation. Then
$$(s t) \, f^{k + 1} = \bigl(s f^{k + 1} g\bigr) h$$
is integral, since valuations add on products and both factors are integral. So a power of $f$ has an integral multiple. A lemma on valuations turns this into a statement about $f$ itself: if $c \, f^{k + 1}$ is integral at a family of valuations for some $c \ne 0$, then $c' f$ is integral for some $c' \ne 0$. So $c' f \in \Lambda(\lambda)$ and $f = c'^{-1} (c' f)$ lies in the $F$-span of $\Lambda(\lambda)$. $\square$

A good cover is *good at* a weight $\lambda$ if the lattice $\Lambda(\lambda)$ has a Gram form at every embedding (the Petersson norm on it is given by a positive definite hermitian matrix), is finitely generated over $\mathcal{O}_F$, and spans $V(\lambda)$. It is *good on* a component $Z$ at $\lambda$ if the same holds for the part of the lattice on $Z$.

**Theorem 2.15.4 (Good covers are good at admissible weights).** Assume the published Hodge bundle theorems. Let $D$ be a family whose core satisfies the laws, let $p, q \ge 1$ at level $j$, let $[E : \mathbb{Q}]/2 > 2$, and let the level be in the range of the family. Let $Y$ be a deep good cover and $\lambda$ admissible. Then $Y$ is good at $\lambda$, and good on every component $Z$ at $\lambda$.

Lean: `GlobalTheory.CovTop.GoodDom.covering_regular_at_domain` (also `GlobalTheory.T.covering_domain_lattice_regularity`, a second name).

*Proof.* The space $V(\lambda)$ is finite dimensional on a good cover. The Gram form comes from goodness of the cover. The lattice is finitely generated: for each nonzero $f \in V(\lambda)$ there is a CM point that detects $f$, with a denominator $N \ne 0$ such that $N f(y)$ is integral for every integral $f$. So the linear functionals $f \mapsto N f(y)$ separate the points of $V(\lambda)$ and take integral values on the lattice, and a lemma on integral functionals gives that the lattice is finitely generated over $\mathcal{O}_F$. The lattice spans $V(\lambda)$ by the previous theorem. So $Y$ is good at $\lambda$, and goodness on each component follows from goodness at $\lambda$. $\square$

**Remark 2.15.5 (Formalization).** The assumption that the level is in the range of the family (`InR D j`) is introduced as `_` and never used ([CoveringDomainLatticeRegularity.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CoveringDomainLatticeRegularity.lean#L70)). The second name `GlobalTheory.T.covering_domain_lattice_regularity` (line 91) is not in the outline of the chapter. Finite generation is the separate result `weight_lattice_fg_on_domain` (line 26), outside the brief of this chapter. The invariant unit is `inverse_invariant_integral`, the cover statement on products is `exists_pow_mul_unit_mem_cusp`, the weight lemma is `exists_dominant_exponents_matching_weight_bar_gap`, the denominator bound is `divisor_multiple_nonneg_eventually` and the valuation lemma is `SupFull.exists_smul_nonneg_of_pow`; we read only their statements as used. The spaces $\mathcal{S}(a, n)$ (`cusp a n`) are not unfolded.
