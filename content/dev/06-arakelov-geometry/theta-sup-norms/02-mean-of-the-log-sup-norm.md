---
title: The mean of the log sup norm of a theta section
decls:
  - GlobalTheory.CompanionTheory.Ar.Sl.Sup.mean_log_sup
  - GlobalTheory.T.exists_theta_sup_bound_log_mean
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The mean of the log sup norm of a theta section

This section proves a global sup norm bound for a theta section of a principally polarized abelian scheme over the ring of integers of a number field $L$. At each complex embedding $\sigma$ of $L$ the section gives a theta function, and Section 1 bounds it by its $L^2$ norm $b_\sigma$ times $\exp(E(\rho_\sigma))$. The factor $\exp(E(\rho_\sigma))$ is large when $\rho_\sigma$ is small. The second part of Section 1 and the product formula show that $\rho_\sigma$ cannot be small on average. The result is a bound for the mean over $\sigma$ of $\log$ of the sup norm. It enters [the line bound of a key](/entry/line-of-key/), where the sup norm of a theta section controls the height of a line in the space of sections.

### The setting

Let $E$ be a CM field with a host, and let $L$ be a number field. A principally polarized datum $D$ over $L$ consists of an abelian scheme $A$ with CM structure over $\mathcal{O}_L$, its generic fibre with a principal polarization, and a hermitian vector bundle $B$ over $\mathcal{O}_L$ that is the Lie algebra of $A$ with the Hodge metric. Its genus $g$ is the rank of $B$. For each embedding $\sigma : L \to \mathbb{C}$ we have the archimedean frames of the fibre at $\sigma$, as in Section 1, for the line bundle $P$ of the polarization. A global section $s$ of $P$ restricts in each frame $a$ to a theta function $\vartheta_{s,a}$ of level one.

For a function $f$ on the embeddings of $L$ we write
$$
\operatorname{mean}_\sigma f(\sigma) = \frac{1}{[L : \mathbb{Q}]} \sum_{\sigma : L \to \mathbb{C}} f(\sigma) .
$$

**Definition 10.2.1.** Let $s$ be a section of $P$ and let $\Phi$ be a real number. The section $s$ has $L^2$ size $\Phi$ if there are numbers $b_\sigma$ such that, for every $\sigma$ and every frame $a$ at $\sigma$, the number $b_\sigma$ is the $L^2$ norm of $\vartheta_{s,a}$, and $\operatorname{mean}_\sigma \log b_\sigma \leq \Phi$. Numbers $M_\sigma$ bound $s$ if $\lVert\vartheta_{s,a}\rVert(w) \leq M_\sigma$ for every $\sigma$, every frame $a$ at $\sigma$ and every $w$.

**Theorem 10.2.2 (Mean of the log sup norm).** There is $C \geq 0$ with this property. Let $D$ be a principally polarized datum over $L$ of genus $g \geq 1$, let $s$ be a section of $P$, and let $\Phi \geq 0$. If $s$ has $L^2$ size $\Phi$, then there are numbers $M_\sigma > 0$ that bound $s$ with
$$
\operatorname{mean}_\sigma \log M_\sigma \leq \Phi + C g \log(2 + g + \Phi) .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Sl.Sup.mean_log_sup` (also `GlobalTheory.T.exists_theta_sup_bound_log_mean`, a second name).

*Proof.* Let $C_0$ be the constant of [the theta bound in one frame](/entry/nform/) and write $E(\rho)$ as there. Let $b_\sigma$ be the numbers of the hypothesis.

Step 1: one frame at each place. Each embedding $\sigma$ has at least one archimedean frame, and in each frame $a$ the section $s$ gives exactly one theta function $\vartheta_{s,a}$. The multiplier of the frame is a quadratic semicharacter, so the frame satisfies the four conditions of Section 1. The theta bound gives a number $\rho_{\sigma,a}$ with $0 < \rho_{\sigma,a} \leq \sqrt{2g}$ and the two parts of the theorem for $\vartheta_{s,a}$ with $L^2$ norm $b_\sigma$. Put
$$
\varphi(\rho) = \frac{\pi}{96 \rho^2} - E(\rho) .
$$

Step 2: the torsion inequality. Fix one frame $a_\sigma$ at each $\sigma$. We claim
$$
\sum_\sigma \varphi(\rho_{\sigma, a_\sigma}) \leq \sum_\sigma \log b_\sigma .
$$
Choose $m \geq 1$ so large that part 2 of the theta bound holds at every $\sigma$. There is a finite extension $K$ of $L$ over which all $m$-torsion points of $A$ are rational. At an $m$-torsion point $x$ where $s$ does not vanish, the value of $s$ against the rigidification and the cubical structure of $P$ is a nonzero algebraic integer $T_x$ in $K$, and this value does not depend on the base change. Its absolute value at an embedding of $K$ over $\sigma$ is the normalized value of $\vartheta_{s,a_\sigma}$ at the point, divided by the factor that the rigidification fixes. For a nonzero algebraic integer the product of the absolute values over all embeddings is the absolute value of its norm, which is a nonzero integer. So
$$
0 \leq \sum_{\tau : K \to \mathbb{C}} \log \lvert\tau(T_x)\rvert .
$$
Summing over the torsion points and comparing with part 2 of the theta bound at each $\sigma$ gives the claim, since every $\sigma$ has at least one torsion point where $s$ does not vanish.

Step 3: a bound for $E$ at each place. We have $\log(1 + t) \leq t$ and $2 g t \leq \frac{\pi}{96} t^2 + \frac{96}{\pi} g^2$ for $t = 1/\rho$. So
$$
E(\rho) \leq \varphi(\rho) + K_1, \qquad K_1 = 2 C_0 g \log(2g) + \frac{96}{\pi} g^2 .
$$
In particular $\varphi(\rho) + K_1 \geq 0$. Fix $\sigma_0$ and a frame $a$ at $\sigma_0$, and use $a$ at $\sigma_0$ and the fixed frames elsewhere in Step 2. All terms $\varphi + K_1$ are nonnegative, so
$$
\varphi(\rho_{\sigma_0, a}) + K_1 \leq \sum_\sigma \log b_\sigma + [L : \mathbb{Q}]\, K_1 .
$$
So $E(\rho_{\sigma_0,a})$ is bounded over the frames $a$ at $\sigma_0$. Let $e_\sigma$ be its least upper bound, and put $M_\sigma = b_\sigma \exp(e_\sigma)$. Part 1 of the theta bound shows that the numbers $M_\sigma$ bound $s$.

Step 4: the mean. Choose at each $\sigma$ a frame $a_\sigma$ with $E(\rho_\sigma) > e_\sigma - 1$, where $\rho_\sigma = \rho_{\sigma,a_\sigma}$. Then
$$
\log M_\sigma \leq \log b_\sigma + g \log\Bigl(1 + \frac{1}{\rho_\sigma}\Bigr) + C_0 g \log(2g) + 1 .
$$
By Step 2, $\operatorname{mean}_\sigma \varphi(\rho_\sigma) \leq \Phi$. A lemma on finite means of numbers in $(0, \sqrt{2g}]$ turns this into a bound of the form
$$
\operatorname{mean}_\sigma \rho_\sigma^{-2} \leq C \bigl(\Phi + g^2 \log(2g)\bigr)
$$
with $C > 0$ that depends only on $C_0$. Since $\log(1 + t) \leq \log 2 + \log^+ t$ and the mean of $\log^+(1/\rho_\sigma)$ is at most $\frac12 \log(1 + \operatorname{mean}_\sigma \rho_\sigma^{-2})$, we get
$$
\begin{aligned}
\operatorname{mean}_\sigma \log M_\sigma \leq \Phi
&+ g \log 2 + \tfrac{g}{2} \log\bigl(1 + C(\Phi + g^2 \log 2g)\bigr) \\
&+ C_0 g \log(2g) + 1 .
\end{aligned}
$$
The right side is at most $\Phi + C' g \log(2 + g + \Phi)$ for a constant $C'$ that depends only on $C_0$ and $C$, because $g \geq 1$ and $\Phi \geq 0$. $\square$

The constant $96/\pi$ in $K_1$ is the price of the square completion in Step 3; it only enters the bound through the logarithm.

**Remark 10.2.3 (Formalization).** The second name only restates the theorem (`Development/AutomorphicSpectrum/Proofs/MetricProofs/ExistsThetaSupBoundLogMeanStatement.lean`). The definitions of frames, theta functions, the $L^2$ size and the sup bound are in `Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsThetaMeanSquareNorm.lean` (lines 26 to 120). The proof in `ExistsThetaSupBoundLogMean.lean` has the torsion inequality of Step 2 as `tors_mean` (line 190), the bound of Step 3 as `Ef_le` (line 328) and the final estimate as `final_bound` (line 353); the product formula step is `sum_log_norm_nonneg` (line 121). The lemma on finite means in Step 4 is `WeakMatrixArithmetic.intersectionNumber_baseChange`, called at line 457; its name suggests a statement about intersection numbers, but it is an inequality between finite means of real numbers. I did not unfold this lemma, nor the lemmas `GlobalTheory.T.torsion_value_integral` and `GlobalTheory.T.torsion_value_norm_eq_theta_norm` behind Step 2, so the description of those parts follows their use in the proof. The proof chooses the frames with a least upper bound over all frames at a place, since the type of frames at a place is not finite.
