---
title: Symmetric cocycles modulo an ideal
decls:
  - GlobalTheory.symmetric_cocycle_is_coboundary_mod
  - GlobalTheory.T.swap_sub_in_of_cob2_in
  - GlobalTheory.SymCob.step
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Symmetric cocycles modulo an ideal

This section proves a form of Lazard's lemma on symmetric $2$-cocycles of a formal group law, with coefficients taken modulo an ideal and with bounded denominators. It says that a series $c$ in two sets of variables that is a symmetric cocycle modulo an ideal $N$ is a coboundary $\delta^1 g$ modulo $N$, and that $g$ has denominators of the same kind as $c$. The theorem on period matrices ([Theorem 5.4.3](/entry/window-matrices/)) uses it when it lifts the adapted basis of [the last section](/entry/adapted-basis/) from $O$ to a frame: at each step the error of a lift is a symmetric cocycle, and the lemma removes it.

We keep the notation of the last section. So $(B, Q, \theta)$ is a frame for $p$ with $\theta : B \to O$, and power series over $B$ are also read as power series over $Q$. For a series $c$ in variables $X$ and $Y$, and a $d$-tuple $\mu$ of such series, put
$$\begin{aligned}
\delta^2_\mu c &= c(Y, Z) - c(\mu(X, Y), Z) + c(X, \mu(Y, Z)) - c(X, Y), \\
\mathrm{sw}(c) &= c(Y, X).
\end{aligned}$$
For $f$ in $X$ alone, $\delta^1_\mu f = f(\mu(X, Y)) - f(X) - f(Y)$ as before. If $\mu$ is a formal group law, then $\delta^2_\mu \delta^1_\mu f = 0$ and $\mathrm{sw}(\delta^1_\mu f) = \delta^1_\mu f$, since $\mu$ is commutative and associative. So a coboundary is a symmetric cocycle, and the lemma is a converse.

**Definition 5.2.1 (Lift of a law).** A $d$-tuple $\mu$ of series over $B$ in $X$ and $Y$ is a *lift* of a law along $\theta$ if its constant terms are $0$, if $\mu(X, 0) = X$, if $\mu(X, Y) = \mu(Y, X)$, and if the image of $\mu$ under $\theta$ is a formal group law over $O$.

A lift need not be associative over $B$. Only its image over $O$ is a formal group law. This is why the theorem below has an alternative hypothesis.

**Definition 5.2.2 (Bounded denominators).** Let $J$ be an ideal of $B$. Let $V(J) \subseteq Q$ be the set of $q$ such that $p^k q$ is the image of an element of $J$ for some $k \geq 0$. Let $N_Q \subseteq Q$ be the image of an ideal $N$. Both are $B$-submodules of $Q$, and $N_Q \subseteq V(J)$ if $N \subseteq J$.

In $V(J)/N_Q$, multiplication by $p$ is surjective, since $p$ is a unit in $Q$, and multiplication by each $n$ prime to $p$ is bijective, since $n$ is a unit in $B$. These two facts are what the combinatorics below needs.

**Theorem 5.2.3 (Symmetric cocycles are coboundaries modulo $N$).** Let $(B, Q, \theta)$ be a frame for $p$. Let $d \geq 0$ and let $\mu$ be a lift of a law along $\theta$ in dimension $d$. Let $N \subseteq J$ be ideals of $B$. Let $c$ be a series over $Q$ in $X$ and $Y$ such that:

1. $\mu$ is a formal group law over $B$, or $c$ has derivatives in $N$;
2. the constant term of $c$ is $0$;
3. every coefficient of $c$ lies in $V(J)$;
4. $\delta^2_\mu c$ has coefficients in $N$;
5. $\mathrm{sw}(c) - c$ has coefficients in $N$.

Then there is a series $g$ over $Q$ in $X$ with constant term $0$ and $\mathrm{lin}(g) = 0$, with every coefficient in $V(J)$, such that $c - \delta^1_\mu g$ has coefficients in $N$.

Lean: `GlobalTheory.symmetric_cocycle_is_coboundary_mod` (also `GlobalTheory.T.swap_sub_in_of_cob2_in`, a wrapper).

The proof goes degree by degree. For $m \geq 0$ we say that $c$ satisfies the *invariant at level $m$* if it satisfies conditions 1 to 5 of the theorem, and if every coefficient of $c$ of total degree less than $m$ lies in $N_Q$. Here the total degree of a monomial in $X$ and $Y$ counts both sets of variables.

**Lemma 5.2.4 (One degree).** Let $(B, Q, \theta)$, $\mu$ and $N \subseteq J$ be as in the theorem. Let $m \neq 0$ and let $c$ satisfy the invariant at level $m$. Then there is a series $h$ over $Q$ in $X$ such that:

1. the coefficient of $X^\alpha$ in $h$ is $0$ whenever $|\alpha| < 2$ or $|\alpha| \neq m$;
2. every coefficient of $h$ lies in $V(J)$;
3. $c - \delta^1_\mu h$ satisfies the invariant at level $m + 1$.

Lean: `GlobalTheory.SymCob.step`.

*Proof.* Let $m = 1$. Take $h = 0$. The coefficients of $c$ of degree $0$ lie in $N_Q$, since the constant term is $0$. We take as given the following maintenance step, which is proved in the same file: if $h$ is homogeneous of degree $m$ with coefficients in $V(J)$, if $h$ has derivatives in $N$ whenever $c$ does, and if
$$c_{a,e} - \prod_i \binom{a_i + e_i}{a_i}\, h_{a+e} \in N_Q$$
for all nonzero multi-indices $a$ and $e$ in $d$ variables with $|a + e| = m$, then $c - \delta^1_\mu h$ satisfies the invariant at level $m + 1$. Here $c_{a,e}$ is the coefficient of $X^a Y^e$ in $c$. For $m = 1$ there are no such $a$ and $e$, since both have degree at least $1$. So the step applies with $h = 0$.

Let $m \geq 2$. For a multi-index $n$ of degree $m$ and $a \leq n$, let $c_n(a)$ be the class of $c_{a, n-a}$ in $V(J)/N_Q$. Condition 5 gives $c_n(a) = c_n(n - a)$. We take as given that the degree $m$ part of the cocycle condition 4, together with the fact that the coefficients of degree less than $m$ lie in $N_Q$, gives the relations
$$\prod_i \binom{a_i + b_i}{a_i}\, c_n(a + b) = \prod_i \binom{n_i - a_i}{b_i}\, c_n(a)$$
for nonzero $a$ and $b$ with $a + b \leq n$ and $a + b \neq n$. These are the relations of the additive law, because $\mu(X, Y) = X + Y$ plus terms of degree at least $2$. We take as given the combinatorial fact behind Lazard's lemma: in a module where $p$ acts surjectively and each $n$ prime to $p$ acts bijectively, a symmetric family with these relations has the form $c_n(a) = \prod_i \binom{n_i}{a_i}\, \bar q_n$ for a class $\bar q_n$, for all $a \neq 0, n$. Choose $q_n \in V(J)$ in the class $\bar q_n$, and let $h$ be the homogeneous series of degree $m$ with coefficients $q_n$. Then $h$ satisfies the congruence of the maintenance step. If $c$ has derivatives in $N$, then so has $h$, by the same file. So the maintenance step gives the claim. $\square$

*Proof of the theorem.* Put $s_0 = c$ and $s_{k+1} = s_k - \delta^1_\mu h_k$, where $h_k$ is the series of the lemma for $s_k$ at level $k + 1$. By induction on $k$, the series $s_k$ satisfies the invariant at level $k + 1$. For $k = 0$ this is the hypothesis, since the constant term of $c$ is $0$. The step from $k$ to $k + 1$ is the lemma with $m = k + 1 \neq 0$.

The series $h_k$ is homogeneous of degree $k + 1$, and it is $0$ for $k + 1 < 2$. So the sum $g = \sum_k h_k$ is a well defined series: each coefficient of $X^\alpha$ gets a contribution only from $h_{|\alpha| - 1}$. The constant term and the linear part of $g$ are $0$, and every coefficient of $g$ lies in $V(J)$.

It remains to show that $c - \delta^1_\mu g$ has coefficients in $N$. The constant terms of $\mu$ are $0$, so $\delta^1_\mu$ of a series with no terms of degree below $M$ has no terms of degree below $M$. Fix a monomial of degree $D$ in $X$ and $Y$. Its coefficient in $\delta^1_\mu g$ equals its coefficient in $\delta^1_\mu (h_0 + \cdots + h_{D})$, because the rest of $g$ has degree above $D$. So its coefficient in $c - \delta^1_\mu g$ equals its coefficient in $s_{D+1}$. By the invariant at level $D + 2$, this coefficient lies in $N_Q$. $\square$

The theorem is used three times. Over the frame $(O, C, \mathrm{id})$ with $N = 0$ and $J = O$, it gives a series $g$ with $c = \delta^1_\mu g$ exactly. This is how a logarithm with a given linear part is built, which the last section takes as given. Over the same frame with $N = J = O$, it is used for quasi-logarithms. Over a general frame with $N = J = \ker \theta$, it lifts quasi-logarithms from $O$ to $B$. In the first two uses the law is associative. In the third one only has a lift, and the alternative in condition 1 is used.

**Remark 5.2.5 (Formalization).** The theorem and the lemma are in [SwapSubInOfCob2In.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SwapSubInOfCob2In.lean#L402), the lemma at line 360, the invariant `Inv` at line 354, and $V(J)$ and $N_Q$ as `V` and `NS` at lines 25 and 40. The maintenance step is `maint` at line 136 and the construction for $m \geq 2$ is `build` at line 216. Inside `build` the facts we take as given are `GlobalTheory.T.coboundary_degree_part_cocycle_mod_ideal` and `GlobalTheory.T.exists_eq_prod_choose_smul_of_choose_relation`, whose proofs we did not open. The operators $\delta^1$, $\delta^2$ and the swap are `cob1`, `cob2` and `swap` in FormalCoboundarySmul.lean, and a lift is `IsLift` in EqZeroOfForallPowDvd.lean, which does not ask for associativity. The three uses are in ExistsFormalGroupLawLogWithLinearPart.lean (line 104), SymmetricCocycleModIdealEqCoboundaryQuasiLog.lean (line 133) and LiftQuasiLogarithmAlongPdThickening.lean (line 342). The lemma takes $h = 0$ for all $m < 2$, not only for $m = 1$; the case $m = 0$ is excluded by its hypothesis. The file name describes condition 5, not the conclusion.
