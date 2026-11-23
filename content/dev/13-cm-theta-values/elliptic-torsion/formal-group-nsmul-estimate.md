---
id: formal-group-nsmul-estimate
title: Multiplication by n on the kernel of reduction, to second order
kind: theorem
decl: ReciprocityTheory.ChartRestriction.L1.formalGroup_nsmul_estimate
module: ReciprocityTheory.ReductiveGroups.UnramifiedIntegrals.TorContr
covers: 301
status: drafted
drafted_by: writer@claude
---
This theorem says that on the kernel of reduction of a curve with good reduction, multiplication by $n$ is multiplication by $n$ on the formal parameter, up to an error of second order. [The $x$-coordinate theorem](/entry/tor-x-mem/) uses it to make $u(M^k D)$ tend to 0 when $\|M\| < 1$. In the language of formal groups, it is the fact $[n](T) = nT + (\text{terms of degree} \ge 2)$ (Silverman, *The Arithmetic of Elliptic Curves*, Ch. IV).

## Statement

Let $C$ be a complete field with an ultrametric norm. Let $W$ be a [[Weierstrass curve|427N6S6QQW]] over $C$ whose coefficients have norm at most 1 and whose discriminant has norm 1. Let $E_1$ be the set of points $O$ and the points with $\|x\| > 1$. Let $u = -x/y$ on $E_1$, with $u(O) = 0$. For $D \in E_1$ and $n \ge 0$:

$$nD \in E_1 \qquad \text{and} \qquad \|u(nD) - n\,u(D)\| \le \|u(D)\|^2.$$

## Proof

Induction on $n$. For $n = 0$ both sides are 0. Suppose the claim holds for $n$.

1. Since $D \in E_1$, $\|u(D)\| < 1$ (`formalGroup_param_norm_lt_one`). Thus $\|u(D)\|^2 \le \|u(D)\|$.
2. $E_1$ is closed under addition (`formal_group_points_subgroup`). So $(n+1)D = nD + D \in E_1$.
3. The norm is ultrametric, so $\|n\| \le 1$. With the claim for $n$, this gives $\|u(nD)\| \le \|u(D)\|$.
4. [The estimate for addition](/entry/formal-group-add-estimate/) applied to $nD$ and $D$ gives $\|u(nD + D) - u(nD) - u(D)\| \le \|u(D)\|^2$.
5. Write $u((n+1)D) - (n+1)u(D)$ as the sum of the error in step 4 and the error for $n$. The ultrametric inequality gives the bound.

The next lemma in the file, `formalGroup_pow_tendsto_zero`, applies this with $n = M$ again and again. Let $c = \max(\|M\|, \|u(D)\|) < 1$. Then $\|u(M^k D)\| \le c^k \|u(D)\|$, which tends to 0.

## In the Lean code

The theorem is at [TorContr.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorContr.lean#L15), and `formalGroup_pow_tendsto_zero` is at line 50. The condition $\|\Delta\| = 1$ is used only in step 2, through `formal_group_points_subgroup`. I did not unfold that lemma. The membership in $E_1$ is `InFormalGroupPoints` and $u$ is `uOf`, both in the Formalism library.
