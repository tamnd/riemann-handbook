---
title: The lower bound at the base level
decls:
  - GlobalTheory.CompanionTheory.Ar.Top.test_height_bound_slope_flat
  - GlobalTheory.T.test_height_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The lower bound at the base level

Theorem B of [the tower conditions](/entry/full-intersection-tower-i8-identity/) writes the top intersection numbers of a tower as the volume times a fixed functional $h$ minus two shift terms, with coefficients $A$ and $b$, up to an error $C \log B / B$. The mean slope bound needs a lower bound for the coefficient $A$ at the base level. This section proves it: if the tower identity holds at the level $B_0$ with coefficients $A_0$ and $b_0$, then $A_0 \ge -c\,\Lambda_{B_0}$ with an explicit constant $c$. The proof evaluates the identity at the test polynomial of [the previous section](/entry/finite-bound/). The result is used in [the chain of tower estimates](/entry/chain-tower/).

We keep the notation of the previous sections: a root tower $T$ of type $(\Psi, N)$ with index $j$ and bad primes $\mathcal{B}$, an intersection system $\mathrm{II}$, the total top functional $\mathrm{PP}_B$, the total volume $\operatorname{vol}(T)$, the shift functionals $\operatorname{Sh}_j(\tau, \cdot)$ and $\operatorname{Tot}(\tau, \cdot)$, the test polynomial $F_T = \mu^{D+1}\mathrm{fib}$ with $D = |\Psi| j (N-j)$, and the test degree $\delta$. Put $m = \min(j, N - j)$ and, for real $\mathrm{rd}$ and $L$, $\Lambda_B = \log(B\,\mathrm{rd}) + |L|$.

**Definition 9.4.1 (Tower identity at a level).** Let $h \colon R \to \mathbb{R}$ be linear and let $\mathrm{frob}$ be a label map. The tower identity holds at the level $B_0$ with coefficients $A_0, b_0 \in \mathbb{R}$ if, for every $\tau$, every $1 \le k \le N$ and every $Q$ homogeneous of degree $d + 1 - k$,

$$
\begin{aligned}
\mathrm{PP}_{B_0}(p_k^\tau Q) = \operatorname{vol}(T)\Big(&h(p_k^\tau Q) - A_0 \sum_\sigma \operatorname{Sh}_j(\sigma, p_k^\tau Q) \\
&- b_0 \sum_\sigma \operatorname{Tot}(\sigma, p_k^\tau Q) + \mathrm{Rest}_{B_0}(\tau, k, Q)\Big).
\end{aligned}
$$

The identity is what Proposition 6 gives when the level goes to infinity and Theorem B is used at the top. The coefficients $A_0$ and $b_0$ are not known in advance; the point of this section is to bound $A_0$ from below.

**Definition 9.4.2 (Slope lower bound, lower bound at the base).** Let $C, \mathrm{rd}, L \in \mathbb{R}$.

1. The tower has the slope lower bound with $C$ if, for every $B \ge 128$ with $B \ge 4|\Psi| N^2$ and $B \ge |\mathcal{B}|$,

$$
\mathrm{PP}_B(F_T) \ge -C\,|\Psi|\, m\, \Lambda_B \cdot (D + 1)\operatorname{vol}(T)\,\delta.
$$

2. The tower has the lower bound at the base for $h$, $\mathrm{frob}$ and $C$ if $A_0 \ge -C \Lambda_{B_0}$ whenever the tower identity holds at $B_0$ with coefficients $A_0, b_0$, and $B_0 \ge 128$, $B_0 \ge 4|\Psi| N^2$ and $B_0 \ge |\mathcal{B}|$.

Here the slope lower bound is a hypothesis. For good towers it is proved in [the volume theorem](/entry/volume-theorem-x-of-inputs/) from the [base settings of the good tower](/entry/base-setting-of-good-tower/).

We use four facts about the test polynomial and the identity. They are computations with the flag degree.

1. $F_T$ is homogeneous of degree $d + 1$, and $\delta > 0$. If $N - j \le j$, then $\operatorname{Sh}_j(\tau, F_T) = 0$ and $\operatorname{Tot}(\tau, F_T) = (D + 1)(N - j)\delta$ for every $\tau$. If $N - j > j$, then $\operatorname{Sh}_j(\tau, F_T) = \operatorname{Tot}(\tau, F_T) = -(D + 1) j \delta$ for every $\tau$. These follow from the Leibniz rule, $\partial \mu^{D+1} = (D+1)\mu^D \partial\mu$, and the fact that the derivatives of $\mathrm{fib}$ in the sum have flag degree $0$.
2. Every homogeneous polynomial of degree $d + 1$ has a power sum decomposition, for $N \ge 2$.
3. If the tower identity holds at $B_0$ and $Q$ is a power sum decomposition of $F$, then $\mathrm{PP}_{B_0}(F)$ is $\operatorname{vol}(T)$ times $h(F) - A_0 \sum_\sigma \operatorname{Sh}_j(\sigma, F) - b_0 \sum_\sigma \operatorname{Tot}(\sigma, F) + \sum_{\tau, k} \mathrm{Rest}_{B_0}(\tau, k, Q_{\tau, k})$. This is the sum of the identities over the decomposition.
4. If the tower is proportional, $h$ satisfies I9, Proposition F holds with $C'$, $B_0 \ge 128$, $B_0 \ge |\mathcal{B}|$ and the identity holds at $B_0$, then $|j A_0 + N b_0| \le C' N \Lambda_{B_0}$. This is the identity applied to $p_1^\tau Q$: the term $h(p_1^\tau Q)$ vanishes by I9, the remainder vanishes since $r_p(\tau, 1, \cdot) = 0$, and Proposition F bounds the left side.

**Theorem 9.4.3 (Lower bound at the base).** Let $\Psi$ be nonempty, let $h$ be linear, let $\mathrm{frob}$ be a label map, and let $C, C' \ge 0$ and $\mathrm{rd} \ge 1$. Assume that the tower is proportional, that $h$ satisfies I9, that Proposition F holds with $C'$, $\mathrm{rd}$, $L$, that the tower has the slope lower bound with $C$, and that

$$
h(F_T) \le (D + 1)\,\delta\, |\Psi|\, \frac{m}{2}\log(N + 1).
$$

Then the tower has the lower bound at the base for $h$, $\mathrm{frob}$ and the constant $2(C + C') + 3$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.test_height_bound_slope_flat` (also `GlobalTheory.T.test_height_bound`, a second name)

*Proof.* Let the identity hold at $B_0$ with $A_0, b_0$, with $B_0$ in the range. Put $\Lambda = \Lambda_{B_0}$, $\ell = \log(N+1)$ and $f = |\Psi| \ge 1$. Choose a power sum decomposition $Q$ of $F_T$ (fact 2) and sum the identity over it (fact 3):

$$
\mathrm{PP}_{B_0}(F_T) = \operatorname{vol}(T)\Big(h(F_T) - A_0 \sum_\sigma \operatorname{Sh}_j(\sigma, F_T) - b_0 \sum_\sigma \operatorname{Tot}(\sigma, F_T) + R\Big),
$$

where $R$ is the total remainder. By the [theorem on the remainder of the test polynomial](/entry/test-rest-bound/), $|R| \le 1.6(D+1)\delta$. The volume is positive, since each $\operatorname{vol}(c) > 0$ and there is at least one component. Divide the slope lower bound at $B_0$ by $\operatorname{vol}(T)$.

Case $N - j \le j$. Then $m = N - j$, the shift terms of $F_T$ vanish and $\sum_\sigma \operatorname{Tot}(\sigma, F_T) = f(D+1) m \delta$. Put $K = (D+1)\delta > 0$. We get

$$
-C f m \Lambda K \le h(F_T) - b_0 f K m + R,
$$

with $h(F_T) \le K f (m/2)\ell$ and $|R| \le 1.6 K$. Since $f m \ge 1$, dividing by $f K m$ gives $b_0 \le C\Lambda + \ell/2 + 1.6$. Fact 4 gives $j A_0 \ge -N b_0 - C' N \Lambda \ge -N(C\Lambda + \ell/2 + 1.6 + C'\Lambda)$. Since $N \le 2j$ and the bracket is nonnegative, $A_0 \ge -2(C\Lambda + \ell/2 + 1.6 + C'\Lambda)$.

Case $N - j > j$. Then $m = j$ and $\operatorname{Sh}_j(\sigma, F_T) = \operatorname{Tot}(\sigma, F_T) = -K j$, so the identity reads $\mathrm{PP}_{B_0}(F_T) = \operatorname{vol}(T)(h(F_T) + (A_0 + b_0) f K m + R)$. The same division gives $-(A_0 + b_0) \le C\Lambda + \ell/2 + 1.6$. Now $(N - j) A_0 = N(A_0 + b_0) - (j A_0 + N b_0)$, so by fact 4, $(N-j)A_0 \ge -N(C\Lambda + \ell/2 + 1.6 + C'\Lambda)$. Since $N \le 2(N-j)$, the same bound for $A_0$ follows.

In both cases $A_0 \ge -2(C\Lambda + C'\Lambda + \ell/2 + 1.6)$. It remains to bound $\ell$ and $1.6$ by $\Lambda$. Since $\mathrm{rd} \ge 1$, $\log B_0 \le \log(B_0\,\mathrm{rd}) \le \Lambda$. Since $B_0 \ge 4|\Psi| N^2 \ge N + 1$, $\ell \le \log B_0$. Since $B_0 \ge 128$, $\log B_0 \ge 7 \log 2 > 1.6$. So $\ell/2 + 1.6 \le \frac{3}{2}\Lambda$ and $A_0 \ge -(2(C + C') + 3)\Lambda$. $\square$

The bound on $h(F_T)$ is checked for the arithmetic flag height in [the chain of tower estimates](/entry/chain-tower/).

**Remark 9.4.4 (Formalization).** The name of the theorem mentions a flat slope, but the statement has no flatness condition; the slope lower bound is a plain hypothesis. All hypotheses are used. The label map has no condition and enters only through the tower identity. Proportionality is used only for $\operatorname{vol}(T) > 0$ and in fact 4. The four facts are separate statements with their own proofs in the development; we have not unfolded the proofs of facts 1 and 4, and the explanations given with them are our reading. The final inequality $1.6 \le \log 128$ is proved from $\log 2 > 0.693$ ([TestHeightBound.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestHeightBound.lean#L32)).
