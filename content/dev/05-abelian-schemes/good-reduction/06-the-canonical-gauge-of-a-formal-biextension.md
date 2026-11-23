---
title: The canonical gauge of a formal biextension
decls:
  - GlobalTheory.canonGauge_exists
  - GlobalTheory.canonGauge_of_log
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The canonical gauge of a formal biextension

A formal biextension with an action of an order is given in coordinates by four families of power series: two cocycles, a symmetry and an adjointness series. This section proves that over a $\mathbb{Q}$-algebra all four are exponentials of coboundaries of a single power series $h$ in two sets of variables, which we call a canonical gauge. The proof uses the logarithm of a formal group and removes the four series one at a time. The result is used through [the step on characters from the literature](/step/every-character-of-literature/), together with [the comparison of charts](/entry/jrel-of-sab-map/) of the next section. Formal group laws and their logarithms are treated in [formal group laws](/learn/formal-groups/#formal-group-laws) and [the invariant derivation and the logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm) of Volume 1.

### Formal groups with an action

Let $R$ be a commutative ring and $d \geq 1$. We write $X, Y, Z, W$ for sets of $d$ variables, and $R[[X, Y]]$ for the power series ring in $2d$ variables.

**Definition 3.6.1 (Formal group law).** A *formal group law* of dimension $d$ over $R$ is a $d$-tuple $F(X, Y)$ of power series in $R[[X, Y]]$ without constant term such that $F(0, Y) = Y$, $F(Y, X) = F(X, Y)$ and $F(F(X, Y), Z) = F(X, F(Y, Z))$. We write $X + Y$ for $F(X, Y)$ when $F$ is fixed.

**Definition 3.6.2 (Action of a ring).** Let $O$ be a commutative ring. An *action* of $O$ on $F$ is a family of $d$-tuples $[a](X)$ of power series without constant term, one for each $a \in O$, such that $[a](X + Y) = [a](X) + [a](Y)$, $[a + b](X) = [a](X) + [b](X)$, $[ab] = [a] \circ [b]$ and $[1](X) = X$.

**Definition 3.6.3 (Formal biextension).** Let $O$ be a commutative ring with an involution $a \mapsto a^*$. A *formal biextension* over $R$ of dimension $d$ with an action of $O$ consists of a formal group law $F$ with an action of $O$, series $\phi_1, \phi_2 \in R[[X, Y, Z]]$, a series $s \in R[[X, Y]]$ and series $\alpha_a \in R[[X, Y]]$ for $a \in O$, which satisfy the following laws.

1. *Normalization.* $\phi_1$ and $\phi_2$ are $1$ when any one of their three variables is $0$, and $s$ and each $\alpha_a$ are $1$ when either variable is $0$.
2. *First cocycle.* $\phi_1(X, Y, W)\, \phi_1(X + Y, Z, W) = \phi_1(Y, Z, W)\, \phi_1(X, Y + Z, W)$ and $\phi_1(Y, X, Z) = \phi_1(X, Y, Z)$.
3. *Second cocycle.* $\phi_2(X, Y, Z)\, \phi_2(X, Y + Z, W) = \phi_2(X, Z, W)\, \phi_2(X, Y, Z + W)$ and $\phi_2(X, Z, Y) = \phi_2(X, Y, Z)$.
4. *Interchange.* $\phi_1(X, Y, Z)\, \phi_1(X, Y, W)\, \phi_2(X + Y, Z, W) = \phi_2(X, Z, W)\, \phi_2(Y, Z, W)\, \phi_1(X, Y, Z + W)$.
5. *Symmetry.* $s(X, Y)\, s(Y, X) = 1$ and $\phi_2(X, Y, Z)\, s(X, Y)\, s(X, Z) = s(X, Y + Z)\, \phi_1(Y, Z, X)$.
6. *Adjointness with the cocycles.* For each $a \in O$,
$$
\begin{aligned}
\phi_1([a]X, [a]Y, Z)\, \alpha_a(X + Y, Z) &= \alpha_a(X, Z)\, \alpha_a(Y, Z)\, \phi_1(X, Y, [a^*]Z), \\
\phi_2([a]X, Y, Z)\, \alpha_a(X, Y + Z) &= \alpha_a(X, Y)\, \alpha_a(X, Z)\, \phi_2(X, [a^*]Y, [a^*]Z).
\end{aligned}
$$
7. *Adjointness with the ring.* $\alpha_1 = 1$, $\alpha_{ab}(X, Y) = \alpha_a([b]X, Y)\, \alpha_b(X, [a^*]Y)$, and
$$
\phi_1([a]X, [b]X, Y)\, \alpha_{a+b}(X, Y) = \alpha_a(X, Y)\, \alpha_b(X, Y)\, \phi_2(X, [a^*]Y, [b^*]Y).
$$
8. *Adjointness with the symmetry.* $\alpha_a(X, Y)\, \alpha_{a^*}(Y, X)\, s([a]X, Y) = s(X, [a^*]Y)$.

In classical terms, $\phi_1$ and $\phi_2$ are the cocycles of the two partial group laws of a biextension of the formal group by the formal multiplicative group, in the sense of Mumford, $s$ describes a symmetry, and $\alpha_a$ describes how the endomorphism $[a]$ is adjoint to $[a^*]$.

### The gauge and the logarithm

**Definition 3.6.4 (Canonical gauge).** Let $k$ be a $\mathbb{Q}$-algebra with a ring map $R \to k$, and let $B$ be a formal biextension over $R$. A *canonical gauge* of $B$ over $k$ is a series $h \in k[[X, Y]]$ with $h(0, Y) = 0$ and $h(X, 0) = 0$ such that, after mapping the coefficients of $B$ to $k$,
$$
\begin{aligned}
\phi_1(X, Y, Z) &= \exp\bigl(h(X, Z) + h(Y, Z) - h(X + Y, Z)\bigr), \\
\phi_2(X, Y, Z) &= \exp\bigl(h(X, Y) + h(X, Z) - h(X, Y + Z)\bigr), \\
s(X, Y) &= \exp\bigl(h(Y, X) - h(X, Y)\bigr), \\
\alpha_a(X, Y) &= \exp\bigl(h([a]X, Y) - h(X, [a^*]Y)\bigr) \quad (a \in O).
\end{aligned}
$$

The exponentials make sense because the arguments have no constant term, by the normalization of $h$.

**Definition 3.6.5 (Logarithm).** A *logarithm* of a formal group law $F$ over $k$ is a $d$-tuple $\ell(X)$ of power series without constant term whose linear part is the identity, such that $\ell(X + Y) = \ell(X) + \ell(Y)$, where on the right $+$ is the sum of power series.

**Theorem 3.6.6 (Existence of the logarithm).** Every formal group law over a $\mathbb{Q}$-algebra has a logarithm.

Lean: `GlobalTheory.FormalLog.logSt_and_logDerivSt`.

This is classical; see [the invariant derivation and the logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm) in Volume 1. A logarithm has an inverse $\ell^{-1}$ under composition, since its linear part is invertible, and $\ell$ is then an isomorphism from $F$ to the additive formal group law.

**Theorem 3.6.7 (Canonical gauge from the logarithm).** Assume that every formal group law over a $\mathbb{Q}$-algebra has a logarithm. Let $R$ be a commutative ring, $O$ a commutative reduced ring with involution which is free of finite rank as a $\mathbb{Z}$-module, $k$ a $\mathbb{Q}$-algebra with a ring map $R \to k$, and $B$ a formal biextension over $R$ with an action of $O$. Then $B$ has a canonical gauge over $k$.

Lean: `GlobalTheory.canonGauge_of_log`.

*Proof.* For a series $h \in k[[X, Y]]$ write $\delta_1 h$, $\delta_2 h$, $\delta_s h$ and $\delta_a h$ for the four arguments of $\exp$ in the definition of a canonical gauge. Each is additive in $h$ and has no constant term when $h(0, Y) = 0$. Call $h$ *normalized* if $h(0, Y) = h(X, 0) = 0$. The proof uses the following six facts, each proved elsewhere.

1. *Base change.* Mapping the coefficients along $R \to k$ gives a formal biextension $B_0$ over $k$.
2. *Regauging.* If $B$ is a formal biextension over $k$ and $h$ is normalized, there is a formal biextension $B'$ over $k$ with the same group law and action such that $\phi_1 = \phi'_1 \exp(\delta_1 h)$, $\phi_2 = \phi'_2 \exp(\delta_2 h)$, $s = s' \exp(\delta_s h)$ and $\alpha_a = \alpha'_a \exp(\delta_a h)$.
3. *First law.* There is a normalized $h_1$ with $\phi_1 = \exp(\delta_1 h_1)$.
4. *Second law.* If $\phi_1 = 1$, there is a normalized $h_2$ with $\delta_1 h_2 = 0$ and $\phi_2 = \exp(\delta_2 h_2)$.
5. *Action.* If $\phi_1 = \phi_2 = 1$, there is a normalized $h_3$ with $\delta_1 h_3 = \delta_2 h_3 = 0$ and $\alpha_a = \exp(\delta_a h_3)$ for all $a$.
6. *Symmetry.* If $\phi_1 = \phi_2 = 1$ and $\alpha_a = 1$ for all $a$, there is a normalized $h_4$ with $\delta_1 h_4 = \delta_2 h_4 = \delta_a h_4 = 0$ and $s = \exp(\delta_s h_4)$.

We also use cancellation: if $c$ has no constant term and $\exp(c) = p \exp(c)$, then $p = 1$, since $\exp(c)$ is a unit.

Start from $B_0$. Take $h_1$ by 3 and regauge $B_0$ by $h_1$ to get $B_1$. Then $\exp(\delta_1 h_1) = \phi_1^{(1)} \exp(\delta_1 h_1)$, so $\phi^{(1)}_1 = 1$ by cancellation. Take $h_2$ by 4 and regauge $B_1$ by $h_2$ to get $B_2$. Since $\delta_1 h_2 = 0$, still $\phi^{(2)}_1 = 1$, and $\phi^{(2)}_2 = 1$ by cancellation. Take $h_3$ by 5 and regauge to get $B_3$, with $\phi^{(3)}_1 = \phi^{(3)}_2 = 1$ and $\alpha^{(3)}_a = 1$. Finally take $h_4$ by 6 for $B_3$.

Put $h = h_1 + h_2 + h_3 + h_4$, which is normalized. For each of the four series the regauging equations chain. For example, for the symmetry,
$$
\begin{aligned}
s^{(0)} &= s^{(1)} e^{\delta_s h_1} = s^{(2)} e^{\delta_s h_2} e^{\delta_s h_1} = s^{(3)} e^{\delta_s h_3} e^{\delta_s h_2} e^{\delta_s h_1} \\
&= e^{\delta_s h_4} e^{\delta_s h_3} e^{\delta_s h_2} e^{\delta_s h_1} = e^{\delta_s h},
\end{aligned}
$$
using that $\delta_s$ is additive and $\exp(u + v) = \exp(u)\exp(v)$ for $u, v$ without constant term. For $\phi_1$ the chain ends with $\phi^{(3)}_1 = 1 = \exp(\delta_1 h_4)$, and similarly for $\phi_2$ and $\alpha_a$. So $h$ is a canonical gauge of $B$ over $k$. $\square$

We indicate the classical content of the steps. In 3, for fixed $Z$, $\log \phi_1$ is a symmetric additive $2$-cocycle of $F$ in $X$ and $Y$. Transported by the logarithm to the additive formal group, it is a symmetric $2$-cocycle of the additive group over a $\mathbb{Q}$-algebra, hence a coboundary, and this gives $h_1$. A power series which is additive in its first variable is determined by its partial derivatives at $0$, which gives the normalizations. In 5, the hypotheses on $O$ make $O \otimes \mathbb{Q}$ a finite product of number fields, a separable $\mathbb{Q}$-algebra, and a separability element shows that a derivation of $O$ into a bimodule is inner. This is where the assumptions that $O$ is reduced, free and finite enter.

**Theorem 3.6.8 (Existence of the canonical gauge).** Let $R$, $O$, $k$ and $B$ be as in the previous theorem. Then $B$ has a canonical gauge over $k$.

Lean: `GlobalTheory.canonGauge_exists`.

*Proof.* Combine the existence of the logarithm with the previous theorem. $\square$

A canonical gauge is not unique. If $h$ and $h'$ are canonical gauges, then $h - h'$ is normalized and its four coboundaries vanish: it is additive in each variable, symmetric and balanced, $(h - h')([a]X, Y) = (h - h')(X, [a^*]Y)$. Conversely, adding such a series to a canonical gauge gives another one.

**Remark 3.6.9 (Formalization).** The four steps, the regauging and the base change are the results `GlobalTheory.GaugeFirstLaw.exists_gauge_first_law`, `GlobalTheory.SecondLawGauge.exists_gauge_second_law`, `GlobalTheory.ActionGauge.exists_action_gauge`, `GlobalTheory.SymGauge.exists_gauge_of_symmetry`, `GlobalTheory.exists_regauge` and `GlobalTheory.exists_formalBiext_map`, assembled by `GlobalTheory.canonGauge_of_steps` ([CanonGaugeOfSteps.lean](lean:Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/CanonGaugeOfSteps.lean#L73)); we have followed the assembly and not unfolded the steps. The first two steps use the coboundary lemma `GlobalTheory.FormalCocycle.exists_coboundary_of_symm_cocycle`, which takes the logarithm as a hypothesis, and the third uses `derivation_inner_of_reduced_order` with a separability element. The definition of a canonical gauge asserts existence only: the word canonical in it does not mean unique, as the remark above shows. The base change $R \to k$ is arbitrary, and the definition places the equations over $k$, not over $R$. The theorem is unconditional once the logarithm is supplied ([CanonGaugeExists.lean](lean:Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/CanonGaugeExists.lean#L11)).
