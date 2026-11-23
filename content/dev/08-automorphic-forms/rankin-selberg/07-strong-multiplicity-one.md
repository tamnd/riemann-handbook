---
title: Rigidity of Satake parameters
decls:
  - GlobalTheory.JSW.Rigid.abs_re_logRS_bdd
  - GlobalTheory.JSW.Rigid.vanish
  - GlobalTheory.JSW.jacquetShalikaRigidity_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rigidity of Satake parameters

This section proves the classification theorem of Jacquet and Shalika for [isobaric sums](/learn/automorphic-forms/#isobaric-sums). Take two finite families of cuspidal representations of general linear groups over $E$. If the sums of their Satake parameters agree at almost every place, then the two families are the same up to order. The proof compares the logarithms of Rankin-Selberg L-functions near $s = 1$. The pole of $L^T(s, \sigma \times \bar\sigma)$ from [the pole theorem](/entry/cell-lintegral/) makes one term large, and [the nonvanishing at $s = 1$](/entry/tendsto-partial-l-ne-zero/) keeps the other terms bounded. [The theorem on integral Satake parameters at all places](/entry/slope-all-of/) uses the result to obtain a Gelfand-Kazhdan duality.

We keep the notation of [the first section](/entry/cell-lintegral/). In particular, for unitary cuspidal $\sigma, \sigma'$ unramified outside $T$ and $x > 1$,
$$\log L^T(x, \sigma, \sigma') = \sum_{w \notin T} \sum_{k \ge 1} \frac{p_k(\mathrm{sat}(\sigma, w))\, \overline{p_k(\mathrm{sat}(\sigma', w))}\, Nw^{-kx}}{k},$$
which converges absolutely, and $\exp \log L^T(x, \sigma, \sigma')$ is the partial L-function $L^T(x, \sigma \times \bar\sigma')$, by [the logarithm lemma](/entry/cell-lintegral/).

**Definition 8.7.1 (Twist by a power of the norm).** For $t \in \mathbb{R}$ let $|\cdot|^t$ be the Hecke character $x \mapsto \|x\|^t$ of $\mathbb{A}^\times / E^\times$. For a cuspidal representation $\pi$ of $\mathrm{GL}_a$, the twist $\pi \otimes |\cdot|^t$ is the space of functions $g \mapsto \phi(g)\,\|\det g\|^t$ with $\phi \in \pi$. If $B$ is a Satake parameter of $\pi$ at $w$, then $Nw^{-t} B = \{Nw^{-t}\alpha : \alpha \in B\}$ is a Satake parameter of $\pi \otimes |\cdot|^t$ at $w$, since $\|\varpi_w\|^t = Nw^{-t}$.

**Lemma 8.7.2 (Unitary part).** Every cuspidal representation $\pi$ of $\mathrm{GL}_a$ with $a \ge 1$ is $\pi_0 \otimes |\cdot|^t$ for a unitary cuspidal $\pi_0$ and some $t \in \mathbb{R}$. If $\pi$ is unramified outside $T$, then so is $\pi_0$.

Lean: `GlobalTheory.CuspRep.CG.exists_isUnitary_twist_absPow`.

*Proof.* Let $\omega$ be the central character of $\pi$. Its absolute value is a continuous character of $\mathbb{A}^\times/E^\times$ with values in $\mathbb{R}_{>0}$, so it is $\|x\|^c$ for some $c \in \mathbb{R}$. Put $t = c/a$ and $\pi_0 = \pi \otimes |\cdot|^{-t}$. The central character of $\pi_0$ is $\omega |\cdot|^{-at}$, which has absolute value $1$. For the second claim, twist the Satake parameters of $\pi$ by $Nw^{t}$. $\square$

The first three results below bound the real part of $\log L^T(x, \sigma, \sigma')$ as $x \to 1^+$, according to how $\sigma$ and $\sigma'$ are related, and what the shift of $x$ is.

**Lemma 8.7.3 (Shifted logarithm).** Let $\sigma, \sigma'$ be unitary and unramified outside $T$, and let $\delta > 0$. Then there is $C$ with $|\log L^T(x + \delta, \sigma, \sigma')| \le C$ for all $x > 1$.

Lean: `GlobalTheory.JSW.Rigid.norm_logRS_add_le`.

*Proof.* The $(w, k)$-term at $x + \delta$ is the term at $1 + \delta$ times $Nw^{-k(x - 1)}$, whose absolute value is at most $1$. So $C$ can be the sum of the absolute values of the terms at $1 + \delta$, which is finite by the logarithm lemma. $\square$

**Lemma 8.7.4 (Bounded real part off the diagonal).** Let $\sigma$ on $\mathrm{GL}_a$ and $\sigma'$ on $\mathrm{GL}_b$ be different unitary cuspidal representations, with $a, b \ge 1$, unramified outside $T$. Then there is $C$ such that $|\operatorname{Re} \log L^T(x, \sigma, \sigma')| \le C$ for all $x > 1$ near $1$.

Lean: `GlobalTheory.JSW.Rigid.abs_re_logRS_bdd`.

*Proof.* By [the nonvanishing theorem](/entry/rankin-selberg-partial-l-tendsto-ne-zero-at-one/), $L^T(x, \sigma \times \bar\sigma') \to z$ as $x \to 1^+$, with $z \neq 0$. For $x > 1$ this function is $\exp \log L^T(x, \sigma, \sigma')$, so
$$\operatorname{Re} \log L^T(x, \sigma, \sigma') = \log |L^T(x, \sigma \times \bar\sigma')| \to \log |z|.$$
Near $1$ the real part lies in $[\log|z| - 1, \log|z| + 1]$. Take $C = |\log |z|| + 1$. $\square$

The imaginary part is a value of the argument and is not controlled here. The proof below does not need it.

**Lemma 8.7.5 (Pole of the logarithm).** Let $\pi$ be a unitary cuspidal representation of $\mathrm{GL}_a$, $a \ge 1$, unramified outside $T$. Then $\operatorname{Re} \log L^T(x, \pi, \pi) \to +\infty$ as $x \to 1^+$.

Lean: `GlobalTheory.JSW.Rigid.tendsto_re_logRS_self`.

*Proof.* Let $L$ and $c > 0$ be as in [the pole theorem](/entry/cell-lintegral/). For $x > 1$, $\exp \log L^T(x, \pi, \pi) = L(x) \ge 1$, so the real part of the logarithm is $\log L(x)$. Since $(x - 1)L(x) \to c > 0$, $L(x) \to +\infty$. $\square$

**Theorem 8.7.6 (Independence of twisted power sums).** Let $S$ be a finite set of pairs $p = (\sigma_p, t_p)$, where $\sigma_p$ is a unitary cuspidal representation of some $\mathrm{GL}_{a_p}$, $a_p \ge 1$, unramified outside $T$, and $t_p \in \mathbb{R}$. Let $c \colon S \to \mathbb{Z}$, and suppose that for every $w \notin T$ and every $k \ge 1$
$$\sum_{p \in S} c(p)\, Nw^{-k t_p}\, p_k(\mathrm{sat}(\sigma_p, w)) = 0.$$
Then $c(p) = 0$ for all $p \in S$.

Lean: `GlobalTheory.JSW.Rigid.vanish`.

*Proof.* Suppose not. Among the $p$ with $c(p) \neq 0$, choose $p_0 = (\sigma_0, t_0)$ with the least $t_p$, and let $S'$ be the set of $p$ with $c(p) \neq 0$. For $p \in S'$ and $x > 1$ put
$$\ell_p(x) = \log L^T(x + t_p - t_0, \sigma_p, \sigma_0).$$
Since $t_p \ge t_0$, each $\ell_p(x)$ is an absolutely convergent double series. Multiply the hypothesis by $\overline{p_k(\mathrm{sat}(\sigma_0, w))}\, Nw^{-k(x - t_0)}/k$ and sum over $w$ and $k$. Because $Nw^{-k t_p} Nw^{-k(x - t_0)} = Nw^{-k(x + t_p - t_0)}$, we may exchange the finite sum over $p$ with the series, and we get
$$\sum_{p \in S'} c(p)\, \ell_p(x) = 0 \qquad (x > 1).$$
Take real parts. For $p \in S'$ with $p \neq p_0$ there are two cases.

1. If $t_p > t_0$, then $|\ell_p(x)|$ is bounded for $x > 1$, by the lemma on the shifted logarithm with $\delta = t_p - t_0$.
2. If $t_p = t_0$, then $\sigma_p \neq \sigma_0$ as pairs $(a_p, \sigma_p)$, since $p \neq p_0$. So $\operatorname{Re} \ell_p(x)$ is bounded for $x$ near $1$, by the lemma on the bounded real part.

So there is $C$ with $|\sum_{p \neq p_0} c(p) \operatorname{Re} \ell_p(x)| \le C$ for $x > 1$ near $1$. Hence $|c(p_0)| \operatorname{Re} \ell_{p_0}(x) \le C$ there. But $\ell_{p_0}(x) = \log L^T(x, \sigma_0, \sigma_0)$, whose real part tends to $+\infty$ by the lemma on the pole, and $|c(p_0)| \ge 1$. This is a contradiction. $\square$

**Theorem 8.7.7 (Jacquet-Shalika rigidity).** Let $(\pi_i)_{i \in I}$ and $(\pi'_j)_{j \in J}$ be finite families, where $\pi_i$ is a cuspidal representation of $\mathrm{GL}_{m_i}$ and $\pi'_j$ one of $\mathrm{GL}_{m'_j}$ over $E$, with all $m_i, m'_j \ge 1$. Suppose that for all but finitely many finite places $w$ there are Satake parameters $B_i$ of $\pi_i$ and $B'_j$ of $\pi'_j$ at $w$ with
$$\sum_{i \in I} B_i = \sum_{j \in J} B'_j$$
as multisets. Then there is a bijection $s \colon I \to J$ with $m'_{s(i)} = m_i$ and $\pi'_{s(i)} = \pi_i$ for all $i$.

Lean: `GlobalTheory.JSW.jacquetShalikaRigidity_holds`.

*Proof.* The steps are as follows.

1. By the lemma on the unitary part, write $\pi_i = \pi_{0,i} \otimes |\cdot|^{t_i}$ and $\pi'_j = \pi'_{0,j} \otimes |\cdot|^{t'_j}$ with $\pi_{0,i}$ and $\pi'_{0,j}$ unitary.
2. Let $T$ be the finite set of places where the hypothesis fails. Every $\pi_i$ and $\pi'_j$ is unramified outside $T$, so every $\pi_{0,i}$ and $\pi'_{0,j}$ is too. Since Satake parameters are unique, $B_i = Nw^{-t_i}\,\mathrm{sat}(\pi_{0,i}, w)$ and $B'_j = Nw^{-t'_j}\,\mathrm{sat}(\pi'_{0,j}, w)$ for $w \notin T$.
3. Let $M$ be the multiset of the pairs $(\pi_{0,i}, t_i)$, $i \in I$, and $M'$ the multiset of the pairs $(\pi'_{0,j}, t'_j)$, $j \in J$. Let $S$ be the set of pairs that occur in $M$ or $M'$, and let $c(p)$ be the multiplicity of $p$ in $M$ minus its multiplicity in $M'$.
4. Take the $k$-th power sum of the identity $\sum_i B_i = \sum_j B'_j$. Since $p_k(Nw^{-t} B) = Nw^{-kt} p_k(B)$, we get
$$\sum_{p \in S} c(p)\, Nw^{-k t_p}\, p_k(\mathrm{sat}(\sigma_p, w)) = 0$$
for all $w \notin T$ and $k \ge 1$.
5. By the independence theorem, $c = 0$, so $M = M'$. Apply the map $(\sigma, t) \mapsto \sigma \otimes |\cdot|^t$ to both sides. This shows that the multiset of the $\pi_i$ equals the multiset of the $\pi'_j$, with their degrees.
6. Two maps from finite sets with the same multiset of values differ by a bijection of the index sets. This gives $s$. $\square$

With $I$ and $J$ of one element each, the theorem is strong multiplicity one: two cuspidal representations with the same Satake parameters at almost all places are equal. Only the Satake parameters enter; no condition at the archimedean places is needed.

**Remark 8.7.8 (Formalization).** The statement is `JacquetShalikaRigidity` in [StrongMultiplicityOne.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/StrongMultiplicityOne.lean#L189), and `IsUnitary` (a unitary central character exists) is at [line 89](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/StrongMultiplicityOne.lean#L89) of that file. The proofs are in [JacquetShalikaRigidityHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L131): the three bounds at lines 38, 62 and 78, the independence theorem at line 131 and the rigidity theorem at line 250. The double series is `logRS`, a sum over pairs $(w, r)$ with $k = r + 1$, in [RsTerm.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RsTerm.lean#L18). The unitary part is in [ExistsIsUnitaryTwistAbsPow.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsIsUnitaryTwistAbsPow.lean#L114). The pairs of $S$ are elements of `(Σ a, CG E a) × ℝ`, so "different" compares the degree and the class together. Since `sat` returns the empty multiset where no parameter exists, step 2 needs that the unitary parts are unramified outside $T$ (`unrOutside_of_twist`) before it can identify $B_i$ with a twist of `sat`. The final step is `exists_equiv_of_map_eq`, at line 103. The rigidity statement sits next to `JacquetShalikaBound`, the bound $Nw^{-1/2} < |\alpha| < Nw^{1/2}$, in the same file; `jacquetShalika_of` puts the two together for the slope theorem.
