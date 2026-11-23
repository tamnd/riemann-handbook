---
id: tor-kur
title: Torsion points of order prime to ℓ are unramified
kind: theorem
decl: ReciprocityTheory.ChartRestriction.L1.tor_kur
module: ReciprocityTheory.ReductiveGroups.UnramifiedIntegrals.TorMain
covers: 335
status: drafted
drafted_by: writer@claude
---
This theorem is the local step of [the torsion values theorem](/entry/cm-torsion-of-point/). It says that a torsion point of order prime to $\ell$ on an [[elliptic curve|427N6S6QQW]] with good reduction over $K$ has its coordinates in $K$. This is a special case of the criterion of Néron-Ogg-Shafarevich: for good reduction, the torsion of order prime to the residue characteristic is unramified (Serre and Tate, "Good reduction of abelian varieties", Ann. of Math. 88, 1968). The Lean proof does not cite that criterion. It works with explicit $\ell$-adic estimates.

## Statement

Let $\ell$, $K$ and the `GoodPair` $(g_2, g_3)$ be as in [the parent entry](/entry/cm-torsion-of-point/). Let $E$ be the curve $y^2 = x^3 - (g_2/4)x - g_3/4$ over $\mathbb{C}_\ell$. Let $P \neq O$ be a [[point|P7V1BQJPSS]] of $E$ with $N \cdot P = O$ for some $N > 0$ with $\ell \nmid N$. Then $x(P) \in K$ and $y(P) \in K$.

## Proof

There are two cases.

1. Suppose $2P = O$. A point of order 2 is not in the kernel of reduction, so $\|x(P)\| \le 1$. Then $y(P) = 0$, and $x(P)$ is a root of the cubic $X^3 - (g_2/4)X - g_3/4$. Since the discriminant is a unit, the derivative of the cubic at $x(P)$ has norm 1. The Hensel lemma `hensel_mem` then puts $x(P)$ in $K$. This case is `tor_two`.
2. Suppose $2P \neq O$. [The membership of the $x$-coordinate](/entry/tor-x-mem/) gives $x(P) \in K$. This is the main step. The lemma `tor_y_unit` gives $\|y(P)\| = 1$.
3. In case 2, $y(P)^2 = x(P)^3 - (g_2/4)x(P) - g_3/4$, and the right side lies in $K$.
4. Since $\ell \ge 5$, $\|2\| = 1$. So $y(P)$ is a simple root of $T^2 - y(P)^2$, a polynomial over $K$ of norm at most 1, and its derivative $2y(P)$ has norm 1. The Hensel lemma gives $y(P) \in K$. This is `sqrt_mem`.

## In the Lean code

The theorem is at [TorMain.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorMain.lean#L88). The case $2P = O$ is [tor_two](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorTwo.lean#L26). It gets the unit derivative from `UnitKap_of`, which I did not unfold. The Hensel lemma is [hensel_mem](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorHensel.lean#L16), and [sqrt_mem](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorHensel.lean#L84) applies it to $X^2 - c$. The theorem `tor_kur` itself is short. The real content is in [tor_x_mem](/entry/tor-x-mem/).
