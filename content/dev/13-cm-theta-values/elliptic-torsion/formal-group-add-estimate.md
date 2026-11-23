---
id: formal-group-add-estimate
title: Addition on the kernel of reduction, to second order
kind: theorem
decl: ReciprocityTheory.ChartRestriction.L1.formalGroup_add_estimate
module: ReciprocityTheory.ReductiveGroups.UnramifiedIntegrals.TorChord
covers: 300
status: drafted
drafted_by: writer@claude
---
This theorem says that on the kernel of reduction, the group law adds the formal parameters, up to an error of second order. It is the base case of [the estimate for multiples](/entry/formal-group-nsmul-estimate/). The source of the bound is the formal group law of the curve. That law is a power series $F(T_1, T_2) = T_1 + T_2 + (\text{terms of degree} \ge 2)$ with coefficients in $\mathbb{Z}[a_1, a_2, a_3, a_4, a_6]$ (Silverman, *The Arithmetic of Elliptic Curves*, Ch. IV).

## Statement

Let $C$ be a complete field with an ultrametric norm. Let $W$ be a [[Weierstrass curve|427N6S6QQW]] over $C$ whose coefficients $a_i$ have norm at most 1. Let $E_1$ and $u = -x/y$ be as in [the parent entry](/entry/formal-group-nsmul-estimate/). For $P, Q \in E_1$:

$$\|u(P + Q) - u(P) - u(Q)\| \le \max(\|u(P)\|, \|u(Q)\|)^2.$$

There is no hypothesis on the discriminant.

## Proof

1. The lemma `wSeriesUnique` gives a power series $w$. I did not unfold it. In Silverman, Ch. IV, $w$ is the series for $-1/y$ in terms of $z = -x/y$.
2. The lemma `wChordSeries` gives a series $F$ in two variables. Its coefficients lie in the ring $\mathbb{Z}[a_1, \dots, a_6] \subset C$. It has $F(0,0) = 0$, and the coefficients of $T_1$ and of $T_2$ are 1.
3. Every element of $\mathbb{Z}[a_1, \dots, a_6]$ has norm at most 1, since the $a_i$ do and the norm is ultrametric (`chord_adjoin_le`). So $F$ is integral.
4. The lemma `formal_group_points_hom` gives $u(P + Q) = F(u(P), u(Q))$ for $P, Q \in E_1$. This is the statement that $E_1$ is the group of the formal group (Silverman, Prop. VII.2.2).
5. Points of $E_1$ have $\|u\| < 1$ (`formalGroup_param_norm_lt_one`). For $a, b$ of norm less than 1, put $r = \max(\|a\|, \|b\|)$. Every term of $F(a,b) - a - b$ has degree at least 2, so it has norm at most $r^2$. The series converges because $C$ is complete. The ultrametric inequality gives $\|F(a,b) - a - b\| \le r^2$. This is `chord_eval_est`.

## In the Lean code

The theorem is at [TorChord.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorChord.lean#L147). The proof is five lines. The bound on the series is `chord_eval_est` at line 101 and the integrality is `chord_adjoin_le` at line 85 of the same file. The three lemmas `wSeriesUnique`, `wChordSeries` and `formal_group_points_hom` come from the Formalism library, with $u$ defined in [FormalGroupPointsParametrisation.lean](lean:Formalism/EllipticTorsion/FormalGroupPointsParametrisation.lean#L21). Since the theorem does not need $\|\Delta\| = 1$, it holds for any integral model.
