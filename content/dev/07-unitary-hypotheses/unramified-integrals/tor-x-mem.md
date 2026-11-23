---
id: tor-x-mem
title: The x-coordinate of a torsion point is a limit of unramified points
kind: theorem
decl: ReciprocityTheory.ChartRestriction.L1.tor_x_mem
module: ReciprocityTheory.ReductiveGroups.UnramifiedIntegrals.TorMain
covers: 330
status: drafted
drafted_by: writer@claude
---
This theorem is the main step of [the unramified torsion coordinates](/entry/tor-kur/). It shows that the $x$-coordinate of a torsion point $P$ of order prime to $\ell$, with $2P \neq O$, lies in $K$. The proof does not use Galois theory. It writes $P$ as the limit of the points $M^k Q$, where $Q$ has coordinates in $K$ and $M = \ell^{\varphi(N)}$. Since $K$ is closed, the limit stays in $K$.

## Statement

Let $\ell$, $K$, the `GoodPair` $(g_2, g_3)$ and the curve $E \colon y^2 = x^3 - (g_2/4)x - g_3/4$ be as in [the parent entry](/entry/tor-kur/). Let $P$ be a point of $E$ with $N \cdot P = O$ for some $N > 0$ with $\ell \nmid N$, and suppose $2P \neq O$. Then $x(P) \in K$.

## Proof

Write $E_1$ for the points $O$ and the points with $\|x\| > 1$. This is the kernel of reduction. Write $u = -x/y$ for the formal parameter on $E_1$ (Silverman, *The Arithmetic of Elliptic Curves*, Ch. IV and Prop. VII.2.2).

1. $P$ is a torsion point of order prime to $\ell$ and $P \neq O$, so $P \notin E_1$. Thus $\|x(P)\| \le 1$. Since $2P \neq O$, also $\|y(P)\| = 1$ (`tor_y_unit`).
2. The lemma `tor_lift` gives a point $Q$ with coordinates in $K$ such that $D = P - Q$ lies in $E_1$. It lifts the reduction of $x(P)$ to a Teichmüller-type element $a$ of $K$, and takes a square root in $K$ for the $y$-coordinate.
3. Let $M = \ell^{\varphi(N)}$. Then $\|M\| < 1$ and $M^k \equiv 1 \pmod N$ for every $k$, by the theorem of Euler. So $M^k P = P$, and
$$P - M^k Q = M^k D.$$
4. [The estimate for multiples](/entry/formal-group-nsmul-estimate/) gives $\|u(M^k D)\| \to 0$ as $k \to \infty$ (`formalGroup_pow_tendsto_zero`).
5. The lemma `tor_x_step` gives $\|x(P) - x(M^k Q)\| \le \|u(M^k D)\|$. It needs $P$, $M^k Q$ and $P + M^k Q$ outside $E_1$. These follow from $P, 2P \notin E_1$ and $M^k D \in E_1$. The bound itself comes from the identity $(x_A - x_B)^2 (x_{A+B} - x_{A-B}) = -4 y_A y_B$ for points $A, B$ (`chord_identity`).
6. So $x(M^k Q) \to x(P)$. Each $M^k Q$ has coordinates in $K$, because the group law has coefficients in $K$. $K$ is a topological closure, so it is closed, and $x(P) \in K$.

## In the Lean code

The theorem is at [TorMain.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorMain.lean#L64). The step bound `tor_x_step` is at line 31 of the same file, and the congruence $M^k P = P$ is `tor_nsmul_fix` at line 18. The lift is [tor_lift](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorLift.lean#L40). The $x$-bound is [norm_x_sub_le_of_formalGroup](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorClose.lean#L47), based on the chord identity at line 13 of that file. The closedness is `Subfield.isClosed_topologicalClosure` from Mathlib. Only the $x$-coordinate is proved here. The parent gets $y(P)$ from a square root.
